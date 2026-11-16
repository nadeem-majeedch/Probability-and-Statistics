"""Scaffold a new module page from the standard twelve-section template.

Every module in this course has the same anatomy (planning/07-design-specification.md
§5). Writing that skeleton by hand invites drift: a missing "Intuition" section, a
forgotten prerequisites block, quizzes that appear before worked examples.

This tool writes the skeleton with the correct front matter, the twelve sections in
order, and explicit authoring prompts. It refuses to overwrite an existing file.

Usage
-----
    python tools/new_module.py --number 14 --title "Variance, Covariance and Correlation" \
        --part 3 --level Core --hours 8 --prereq 13 --prereq 12

    # preview without writing
    python tools/new_module.py --number 14 --title "..." --part 3 --level Core --hours 8 --dry-run
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

PART_DIRS = {
    1: "part-1-foundations",
    2: "part-2-probability",
    3: "part-3-random-variables",
    4: "part-4-sampling",
    5: "part-5-inference",
    6: "part-6-modelling",
    7: "part-7-comparative",
    8: "part-8-modern",
}

MODULES = [
    "mathematical-foundations",
    "data-and-statistical-thinking",
    "descriptive-statistics",
    "data-visualization",
    "counting-and-combinatorics",
    "axioms-of-probability",
    "conditional-probability",
    "bayes-theorem",
    "random-variables",
    "discrete-distributions",
    "continuous-distributions",
    "joint-distributions",
    "expectation-and-moments",
    "variance-and-covariance",
    "sampling-distributions",
    "law-of-large-numbers",
    "central-limit-theorem",
    "point-estimation",
    "confidence-intervals",
    "hypothesis-testing",
    "correlation-and-association",
    "simple-linear-regression",
    "multiple-linear-regression",
    "anova",
    "chi-square-tests",
    "nonparametric-statistics",
    "bayesian-statistics",
    "monte-carlo",
    "statistics-in-practice",
    "capstone",
]

TEMPLATE = """---
title: {title}
description: TODO — one sentence, 120–160 characters, states what the student can do after this module.
module: {number}
part: {part}
level: {level}
hours: {hours}
prerequisites: [{prereqs}]
---

# {number}. {title}

**Part {part_roman} · Module {number} of 30 · {level} · {hours} study hours**

TODO: a two-sentence orientation — what this module answers, and why it comes here.

## Learning objectives

By the end of this module you can:

1. TODO — measurable action.
2. TODO
3. TODO
4. TODO
5. TODO

## Before you start

- TODO: link the exact prerequisite section, not just the module.
- TODO: the one formula or idea to recall.
- Time needed: about {hours} hours.

## The idea in plain language

TODO: no symbols. Explain the concept the way you would to a colleague.

## Notation and derivation

TODO: define every symbol at first use. Number equations that are referred to later.

\\[
  TODO
\\]

TODO: one sentence reading the equation in words.

## Intuition

TODO: a second explanation — geometric, physical, or a simulation argument.

## Worked examples

!!! example "Example 1"

    TODO: a complete numerical solution, arithmetic shown, interpretation at the end.

## Where this is used

TODO: 2–3 specific data-science applications, not generic claims.

## Visual explanations

TODO: 2–5 figures (from the module notebook), each with a caption stating the finding.
Every figure needs alt text describing the finding, not the file.

## Python demonstration

```python
# TODO: reproduce the mathematics in this module, then extend it.
# Always seed: rng = np.random.default_rng(2026)
# Always show output.
```

TODO: read the output line by line.

## Exercises

??? example "Exercise ★"

    TODO — recall or one-step application.

??? example "Exercise ★★"

    TODO — multi-step, choose the method.

??? example "Exercise ★★★"

    TODO — prove, construct a counterexample, or simulate.

## Self-assessment quiz

??? question "1. TODO"

    ??? success "Answer"

        TODO — explanation, not just the answer.

## Summary and revision

**Key results**

- TODO

**Formula box**

\\[
  TODO
\\]

**Common errors**

- TODO

**You can now**

- TODO

**Further reading**

- TODO — verified references only (planning/10-interactive-simulation-spec.md §7).

---

**Next:** TODO · **Previous:** TODO
"""


def roman(n: int) -> str:
    numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
    return numerals[n - 1]


def slug_for(number: int, title: str) -> str:
    if 1 <= number <= len(MODULES):
        return MODULES[number - 1]
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def main() -> int:
    ap = argparse.ArgumentParser(description="Scaffold a module page.")
    ap.add_argument("--number", type=int, required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--part", type=int, required=True, choices=sorted(PART_DIRS))
    ap.add_argument("--level", default="Core", choices=["Beginner", "Core", "Advanced"])
    ap.add_argument("--hours", type=int, default=8)
    ap.add_argument("--prereq", type=int, action="append", default=[])
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not 1 <= args.number <= 30:
        print("error: module number must be 1–30")
        return 2

    number = f"{args.number:02d}"
    filename = f"{number}-{slug_for(args.number, args.title)}.md"
    target = pathlib.Path("docs") / PART_DIRS[args.part] / filename

    if target.exists():
        print(f"refusing to overwrite existing file: {target}")
        return 1

    content = TEMPLATE.format(
        title=args.title,
        number=number,
        part=args.part,
        part_roman=roman(args.part),
        level=args.level,
        hours=args.hours,
        prereqs=", ".join(str(p) for p in args.prereq),
    )

    if args.dry_run:
        print(f"would write {target} ({len(content.splitlines())} lines)")
        return 0

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    print(f"wrote {target}")
    print("next: add it to `nav` in mkdocs.yml, then replace every TODO.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
