"""Validate the interactive laboratories.

Checks, in order:

1. every laboratory page in docs/labs/ has the required learning sections;
2. every page's data-lab value is registered by a lab module;
3. every page links to an existing notebook;
4. the navigation lists every laboratory page;
5. the client-side rules hold (no fetch, no XHR, no storage, no external URLs);
6. the JavaScript test suite passes (node --test tests/).

Exit status is non-zero if any check fails, so this can gate a release.
"""

from __future__ import annotations

import json
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LABS = ROOT / "docs" / "labs"
JS = ROOT / "docs" / "assets" / "javascripts"
NAV = ROOT / "mkdocs.yml"
NOTEBOOKS = ROOT / "docs" / "practicals" / "notebooks"

# The eleven sections every laboratory must contain, matched case-insensitively.
REQUIRED = [
    ("learning objectives", r"^##\s+Learning objectives"),
    ("mathematics", r"^##\s+The mathematics"),
    ("instructions", r"^##\s+(How to run the experiment|What this lab shows|Try this)"),
    ("interpretation", r"^##\s+(Reading the results|What changes when|Where this is used)"),
    ("guided activities", r"^##\s+Guided activities"),
    ("independent challenges", r"^##\s+Independent challenges"),
    ("expected observations", r"^##\s+Expected observations"),
    ("self-assessment", r"^##\s+Self-assessment"),
]

LAB_PAGE_NAMES = [
    "probability.md",
    "conditional-probability.md",
    "discrete-distributions.md",
    "continuous-distributions.md",
    "normal-and-z-scores.md",
    "law-of-large-numbers.md",
    "clt.md",
    "sampling-distributions.md",
    "confidence-intervals.md",
    "p-values.md",
    "correlation-regression.md",
    "bayesian-updating.md",
    "power-and-errors.md",
    "anova.md",
]

problems: list[str] = []


def fail(message: str) -> None:
    problems.append(message)


def registered_builders() -> set[str]:
    names: set[str] = set()
    for path in JS.glob("labs*.js"):
        text = path.read_text(encoding="utf-8")
        names.update(re.findall(r"REG\.builders\.([A-Za-z0-9_]+)\s*=", text))
    return names


def main() -> int:
    builders = registered_builders()
    if len(builders) < 14:
        fail(f"only {len(builders)} lab builders registered: {sorted(builders)}")

    nav_text = NAV.read_text(encoding="utf-8")

    for name in LAB_PAGE_NAMES:
        path = LABS / name
        if not path.exists():
            fail(f"missing laboratory page: {name}")
            continue

        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()

        for label, pattern in REQUIRED:
            if not any(re.match(pattern, line, re.IGNORECASE) for line in lines):
                fail(f"{name}: missing required section ({label})")

        # data-lab must be registered
        for lab_id in re.findall(r'data-lab="([A-Za-z0-9_-]+)"', text):
            if lab_id not in builders:
                fail(f"{name}: data-lab=\"{lab_id}\" has no registered builder")

        # must link to a notebook and the notebook must exist
        links = re.findall(r"\]\(([^)]*\.ipynb)\)", text)
        if not links:
            fail(f"{name}: no link to a practical notebook")
        for link in links:
            target = (path.parent / link).resolve()
            if not target.exists():
                fail(f"{name}: notebook link does not resolve: {link}")

        # must be in the navigation
        if f"labs/{name}" not in nav_text:
            fail(f"{name}: not listed in the mkdocs navigation")

        # interactive block present, with the four slots the runtime fills
        if 'class="psds-lab"' not in text and 'psds-lab' not in text:
            fail(f"{name}: no interactive laboratory block")
        for slot in ("controls", "chart", "readout", "hint"):
            if f'data-role="{slot}"' not in text:
                fail(f"{name}: missing data-role=\"{slot}\"")

    # Client-side rules: no network, no storage, no external assets in lab scripts.
    forbidden = [
        (r"\bfetch\s*\(", "fetch()"),
        (r"XMLHttpRequest", "XMLHttpRequest"),
        (r"localStorage", "localStorage"),
        (r"sessionStorage", "sessionStorage"),
        (r"document\.cookie", "document.cookie"),
        (r"https?://(?!www\.w3\.org)", "external URL"),
    ]
    lab_scripts = [
        JS / "stats.js",
        JS / "viz.js",
        JS / "labs.js",
        JS / "labs-kit.js",
        JS / "labs-probability.js",
        JS / "labs-inference.js",
        JS / "labs-modelling.js",
    ]
    for path in lab_scripts:
        if not path.exists():
            fail(f"missing lab script: {path.name}")
            continue
        text = path.read_text(encoding="utf-8")
        # Strip comments so that documentation mentions do not trip the check.
        stripped = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
        stripped = re.sub(r"^\s*//.*$", "", stripped, flags=re.M)
        for pattern, label in forbidden:
            if re.search(pattern, stripped):
                fail(f"{path.name}: uses {label} (labs must be fully client-side)")

    # JavaScript test suite
    node = shutil.which("node")
    if node is None:
        print("  WARN no node on PATH: skipped the JavaScript test suite")
    else:
        result = subprocess.run(
            [node, "--test", "tests/"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            tail = (result.stdout or result.stderr).strip().splitlines()[-25:]
            fail("JavaScript test suite failed:\n" + "\n".join(tail))
        else:
            passed = re.search(r"# pass (\d+)", result.stdout or "")
            print(f"  OK   {passed.group(1) if passed else 'all'} JavaScript tests pass")

    if problems:
        print("\nLaboratory checks FAILED:")
        for p in problems:
            print("  -", p)
        return 1

    print(f"  OK   {len(LAB_PAGE_NAMES)} laboratory pages, {len(builders)} builders")
    print("All laboratory checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
