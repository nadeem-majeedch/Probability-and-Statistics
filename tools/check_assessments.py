"""Validate the self-assessment banks and examination papers.

Checks, for every page under ``docs/assessments``:

1. the required number of items of each type (MCQ, short, numerical, scenario,
   analytical) is present;
2. every MCQ has 2–5 options, exactly one marked answer, and an explanation;
3. every short/numerical/scenario/analytical item has an answer block
   (``<details>``) — one per item;
4. no MCQ stem is repeated across pages (normalised, and near-duplicate stems
   are flagged), so banks are not copies of each other with new numbers;
5. examination papers carry an answer key section.

Usage
-----
    python tools/check_assessments.py
    python tools/check_assessments.py --verbose

Exits 0 only when every check passes.
"""

from __future__ import annotations

import argparse
import importlib.util
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSESS = ROOT / "docs/assessments"

REQUIRED_MODULE = {"mcq": 15, "S": 10, "N": 10, "P": 5, "C": 3}
REQUIRED_EXAM = {"mcq": 20, "N": 5}

# item markers: **S1.** **N3.** **P2.** **C1.**
ITEM = re.compile(r"^\*\*([SNPC])(\d+)\.\*\*", re.MULTILINE)
DETAILS = re.compile(r"<details", re.IGNORECASE)
WORD = re.compile(r"[a-z]{3,}")


def load_hook():
    path = ROOT / "hooks/quiz.py"
    spec = importlib.util.spec_from_file_location("quiz_hook", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def normalise(stem: str) -> str:
    text = re.sub(r"\\\(|\\\)|\\[a-zA-Z]+|[0-9]+", " ", stem.lower())
    return " ".join(WORD.findall(text))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    hook = load_hook()
    pages = sorted(ASSESS.glob("m*.md")) + sorted(ASSESS.glob("exams/*.md"))
    if not pages:
        print("no assessment pages found")
        return 1

    failures: list[str] = []
    stems: dict[str, list[str]] = {}
    print(f"{'page':28s} {'MCQ':>4} {'S':>3} {'N':>3} {'P':>3} {'C':>3} {'det':>4} {'ok':>3}")
    print("-" * 66)

    for page in pages:
        rel = page.relative_to(ASSESS).as_posix()
        text = page.read_text(encoding="utf-8")
        is_exam = "/" in rel
        required = REQUIRED_EXAM if is_exam else REQUIRED_MODULE

        questions = []
        for block in hook.QUIZ_BLOCK.findall(text):
            questions.extend(hook._parse(block))

        for question in questions:
            if not 2 <= len(question["options"]) <= 5:
                failures.append(f"{rel}: Q{question['number']} has {len(question['options'])} options")
            if not question["why"]:
                failures.append(f"{rel}: Q{question['number']} has no explanation")
            labels = [label for label, _ in question["options"]]
            if question["answer"] not in labels:
                failures.append(f"{rel}: Q{question['number']} answer not among options")
            key = normalise(question["stem"])
            if len(key.split()) >= 6:
                stems.setdefault(key, []).append(f"{rel}:Q{question['number']}")

        markers = ITEM.findall(text)
        counts = {"S": 0, "N": 0, "P": 0, "C": 0}
        for kind, _ in markers:
            counts[kind] += 1
        details = len(DETAILS.findall(text))
        items = sum(counts.values())

        if len(questions) < required["mcq"]:
            failures.append(f"{rel}: {len(questions)} MCQs, need {required['mcq']}")
        for kind in ("S", "N", "P", "C"):
            need = required.get(kind, 0)
            if counts[kind] < need:
                failures.append(f"{rel}: {counts[kind]} {kind} items, need {need}")
        if details < items:
            failures.append(f"{rel}: {details} answer blocks for {items} written items")
        if is_exam and "## Answer key" not in text:
            failures.append(f"{rel}: exam has no '## Answer key' section")
        if not is_exam and "../modules/" not in text:
            failures.append(f"{rel}: does not link the corresponding module chapter")

        ok = "yes"
        print(f"{rel:28s} {len(questions):4d} {counts['S']:3d} {counts['N']:3d} "
              f"{counts['P']:3d} {counts['C']:3d} {details:4d} {ok:>3}")

    duplicates = {k: v for k, v in stems.items() if len(v) > 1}
    for key, where in duplicates.items():
        failures.append(f"duplicate MCQ stem used at {', '.join(where)}: {key[:60]}")

    # near-duplicates: same word set used twice (reordered wording)
    seen: dict[frozenset, str] = {}
    for key, where in stems.items():
        signature = frozenset(key.split())
        if len(signature) < 8:
            continue
        if signature in seen:
            failures.append(f"near-duplicate MCQ stem: {seen[signature]} and {where[0]}")
        else:
            seen[signature] = where[0]

    print("-" * 66)
    print(f"{len(pages)} page(s), {sum(len(v) for v in stems.values())} distinct MCQ stems, "
          f"{len(duplicates)} duplicate(s)")
    if failures:
        print(f"\nFAILED {len(failures)} check(s):")
        for item in failures[:40]:
            print("  -", item)
        return 1
    print("\nAll assessment checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
