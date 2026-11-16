"""Validate the project-based learning section.

Checks:

1. every project page carries the fifteen required sections, in order;
2. the dataset link and the starter-notebook link resolve;
3. each referenced notebook is valid JSON with at least one code cell and loads the
   dataset by its correct filename;
4. a reference solution exists for every project;
5. the capstone page names all eight required statistical areas;
6. the generated datasets still match a fresh run of the generator.

Run: python tools/check_projects.py
"""

from __future__ import annotations

import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROJECTS = ROOT / "docs/projects"

SECTIONS = [
    "## Real-world background",
    "## Problem statement",
    "## Learning objectives",
    "## Dataset",
    "## Dataset description",
    "## Research questions",
    "## Statistical methods required",
    "## Mathematical concepts",
    "## Step-by-step tasks",
    "## Python implementation requirements",
    "## Expected visualizations",
    "## Interpretation requirements",
    "## Deliverables",
    "## Evaluation rubric",
    "## Extension challenges",
]

CAPSTONE_AREAS = [
    "Descriptive statistics",
    "Probability",
    "Distributions",
    "Sampling",
    "Confidence intervals",
    "Hypothesis testing",
    "Correlation and regression",
    "Interpretation",
]

PROJECTS_LIST = [f"p{i:02d}" for i in range(1, 9)] + ["p09"]


def main() -> int:
    failures: list[str] = []
    pages = sorted(p for p in PROJECTS.glob("p*.md") if p.name != "index.md")
    if len(pages) != 9:
        failures.append(f"expected 9 project pages, found {len(pages)}")

    for page in pages:
        text = page.read_text(encoding="utf-8")
        position = -1
        for heading in SECTIONS:
            found = text.find(heading)
            if found == -1:
                failures.append(f"{page.name}: missing section {heading!r}")
                break
            if found < position:
                failures.append(f"{page.name}: section {heading!r} is out of order")
                break
            position = found

        title = page.read_text(encoding="utf-8").splitlines()[0]
        if not title.startswith("# "):
            failures.append(f"{page.name}: does not start with an H1 title")

        notebook = None
        dataset = None
        for link in __import__("re").findall(r"\]\(([^)]+)\)", text):
            if link.endswith(".ipynb"):
                notebook = (PROJECTS / link).resolve()
            if link.endswith(".csv"):
                dataset = (PROJECTS / link).resolve()
        if notebook is None or not notebook.exists():
            failures.append(f"{page.name}: starter notebook link missing or broken")
        if dataset is None or not dataset.exists():
            failures.append(f"{page.name}: dataset link missing or broken")

        if notebook and notebook.exists():
            try:
                doc = json.loads(notebook.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                failures.append(f"{notebook.name}: invalid notebook JSON ({exc})")
                doc = None
            if doc is not None:
                code = [c for c in doc.get("cells", []) if c.get("cell_type") == "code"]
                if len(code) < 3:
                    failures.append(f"{notebook.name}: only {len(code)} code cells")
                joined = "".join("".join(c.get("source", [])) for c in doc["cells"])
                if dataset and dataset.name not in joined:
                    failures.append(f"{notebook.name}: does not reference {dataset.name}")

        solution = PROJECTS / "solutions" / f"{page.stem.split('-')[0]}-solution.md"
        if not solution.exists():
            failures.append(f"{page.name}: no reference solution at solutions/{solution.name}")

    capstone = (PROJECTS / "p09-capstone.md").read_text(encoding="utf-8")
    for area in CAPSTONE_AREAS:
        if area not in capstone:
            failures.append(f"capstone: does not mention {area!r}")

    check = subprocess.run(
        [sys.executable, "tools/generate_project_data.py", "--check"],
        cwd=ROOT, capture_output=True, text=True,
    )
    if check.returncode != 0:
        failures.append("project datasets are out of date: " + check.stdout.strip())

    build = subprocess.run(
        [sys.executable, "tools/build_project_notebooks.py", "--check"],
        cwd=ROOT, capture_output=True, text=True,
    )
    if build.returncode != 0:
        failures.append("notebooks are out of date: " + build.stdout.strip())

    print(f"{len(pages)} project page(s), {len(list(PROJECTS.glob('solutions/*.md')))} solution(s), "
          f"{len(list((PROJECTS / 'notebooks').glob('*.ipynb')))} notebook(s)")
    if failures:
        print(f"\nFAILED {len(failures)} check(s):")
        for item in failures:
            print("  -", item)
        return 1
    print("\nAll project checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
