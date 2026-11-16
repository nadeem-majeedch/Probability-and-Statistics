"""Validate the case studies.

Checks, for every page in ``docs/case-studies``:

1. the twelve required sections are present, in order;
2. every ``../data/case-studies/*.csv`` link points at an existing file;
3. every Python code block executes without error (matplotlib forced to Agg);
4. the synthetic datasets match a fresh run of ``tools/generate_case_data.py``.

Usage
-----
    python tools/check_case_studies.py             # full check (executes the code)
    python tools/check_case_studies.py --no-exec   # structure and links only

Run with the environment that has the course libraries installed, e.g.
``.venv-prac/Scripts/python.exe tools/check_case_studies.py``.

Exits 0 only when every check passes.
"""

from __future__ import annotations

import argparse
import os
import pathlib
import re
import subprocess
import sys
import tempfile
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ROOT / "docs/case-studies"
DATA = ROOT / "docs/data/case-studies"

REQUIRED = [
    "## A. Problem statement",
    "## B. Background and context",
    "## C. Dataset description",
    "## D. Questions to investigate",
    "## E. Relevant probability and statistical concepts",
    "## F. Mathematical formulation",
    "## G. Step-by-step analytical approach",
    "## H. Student tasks",
    "## I. Python practical implementation",
    "## J. Visualization and interpretation",
    "## K. Expected conclusions",
    "## L. Detailed solution and discussion",
]

CODE_BLOCK = re.compile(r"```python\n(.*?)```", re.DOTALL)
DATASET_LINK = re.compile(r"\.\./data/case-studies/([\w.-]+\.csv)")

failures: list[str] = []


def fail(page: str, message: str) -> None:
    failures.append(f"{page}: {message}")


def check_structure(path: pathlib.Path) -> tuple[list[str], int]:
    name = path.name
    text = path.read_text(encoding="utf-8")

    positions = []
    for section in REQUIRED:
        index = text.find(section)
        if index < 0:
            fail(name, f"missing section: {section[3:]}")
        else:
            positions.append(index)
    if positions != sorted(positions):
        fail(name, "sections are out of order")

    linked = set(DATASET_LINK.findall(text))
    if not linked:
        fail(name, "no dataset link to ../data/case-studies/")
    for filename in sorted(linked):
        if not (DATA / filename).exists():
            fail(name, f"dataset link does not resolve: {filename}")

    blocks = CODE_BLOCK.findall(text)
    if len(blocks) < 2:
        fail(name, f"only {len(blocks)} python block(s); expected at least 2")
    return blocks, len(text)


def run_blocks(path: pathlib.Path, blocks: list[str], timeout: int) -> float:
    name = path.name
    code = "\n\n".join(blocks)
    code = "import matplotlib\nmatplotlib.use('Agg')\n" + code
    handle = tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8")
    handle.write(code)
    handle.close()
    env = dict(os.environ, MPLBACKEND="Agg", PYTHONIOENCODING="utf-8")
    started = time.time()
    try:
        result = subprocess.run(
            [sys.executable, handle.name],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=env,
        )
        elapsed = time.time() - started
        if result.returncode != 0:
            tail = (result.stderr or "").strip().splitlines()[-6:]
            fail(name, "python block failed: " + " | ".join(tail))
        return elapsed
    except subprocess.TimeoutExpired:
        fail(name, f"python blocks exceeded {timeout}s")
        return float(timeout)
    finally:
        pathlib.Path(handle.name).unlink(missing_ok=True)


def check_datasets() -> None:
    result = subprocess.run(
        [sys.executable, "tools/generate_case_data.py", "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        detail = (result.stdout + result.stderr).strip().splitlines()[-2:]
        failures.append("datasets: " + " ".join(detail))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-exec", action="store_true", help="skip executing the code")
    ap.add_argument("--timeout", type=int, default=180, help="per-page timeout (s)")
    args = ap.parse_args()

    pages = sorted(p for p in PAGES.glob("*.md") if p.name != "index.md")
    if not pages:
        print("no case-study pages found")
        return 1

    print(f"{'page':34s} {'chars':>6} {'blocks':>6} {'secs':>6}")
    print("-" * 58)
    total = 0.0
    for page in pages:
        blocks, chars = check_structure(page)
        if args.no_exec:
            print(f"{page.name:34s} {chars:6d} {len(blocks):6d} {'-':>6}")
            continue
        elapsed = run_blocks(page, blocks, args.timeout)
        total += elapsed
        print(f"{page.name:34s} {chars:6d} {len(blocks):6d} {elapsed:6.1f}")

    print("-" * 58)
    if args.no_exec:
        print(f"{len(pages)} page(s) checked structurally; code not executed")
    else:
        print(f"{len(pages)} page(s) checked in {total:.1f}s")
        check_datasets()

    if failures:
        print(f"\nFAILED {len(failures)} check(s):")
        for item in failures:
            print("  -", item)
        return 1
    print("\nAll case-study checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
