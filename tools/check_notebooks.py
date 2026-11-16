"""Validate the practical notebooks.

Checks, in order:

1. Every source in ``tools/notebook_sources`` has an up-to-date .ipynb.
2. Each notebook has the twelve required sections, in order.
3. Code cells are non-empty, and notebooks that simulate define a seeded
   ``np.random.default_rng``.
4. Stored outputs are empty (the shipped notebooks carry no output).
5. Every notebook executes from top to bottom in a fresh kernel with no error,
   and its output stays within a size budget.

Usage
-----
    python tools/check_notebooks.py             # full check, executes everything
    python tools/check_notebooks.py --no-exec   # structure only (fast)

Run it with the environment that has the course libraries installed, e.g.
``.venv-prac/Scripts/python.exe tools/check_notebooks.py``.

Exits 0 only when every check passes.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import shutil
import sys
import tempfile
import time

import nbformat
from nbclient import NotebookClient

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "tools/notebook_sources"
OUT = ROOT / "docs/practicals/notebooks"

REQUIRED = [
    "1. Introduction",
    "2. Learning objectives",
    "3. Required libraries",
    "4. Concepts",
    "5. Formulas",
    "6. Implementation",
    "7. Output and interpretation",
    "8. Visualisation",
    "9. Practical scenario",
    "10. Exercises",
    "11. Solutions",
    "12. Summary",
]

MIN_CODE_CELLS = 8
MAX_CELL_TEXT = 20_000        # characters in a single stream output
MAX_NOTEBOOK_TEXT = 120_000   # characters of text output per notebook

failures: list[str] = []


def fail(name: str, message: str) -> None:
    failures.append(f"{name}: {message}")


def sections(nb: nbformat.NotebookNode) -> list[str]:
    pattern = re.compile(r"^##\s+(\d+\.\s+[^\n]+?)\s*$", re.MULTILINE)
    found: list[str] = []
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            found.extend(m.group(1).rstrip() for m in pattern.finditer(cell.source))
    return found


def check_structure(path: pathlib.Path, nb: nbformat.NotebookNode) -> tuple[int, int]:
    name = path.name
    headings = sections(nb)
    missing = [s for s in REQUIRED if s not in headings]
    if missing:
        fail(name, f"missing sections: {missing}")
    present = [s for s in headings if s in REQUIRED]
    if present != [s for s in REQUIRED if s in present]:
        fail(name, "required sections are out of order")

    code = [c for c in nb.cells if c.cell_type == "code"]
    md = [c for c in nb.cells if c.cell_type == "markdown"]
    if len(code) < MIN_CODE_CELLS:
        fail(name, f"only {len(code)} code cells (expected at least {MIN_CODE_CELLS})")
    if not md:
        fail(name, "no markdown cells")
    for index, cell in enumerate(code):
        if not cell.source.strip():
            fail(name, f"code cell {index} is empty")

    joined = "\n".join(c.source for c in code)
    if ("rng" in joined or "random" in joined) and "default_rng(" not in joined:
        fail(name, "uses randomness without a seeded np.random.default_rng")

    for index, cell in enumerate(code):
        outputs = cell.get("outputs") or []
        if outputs:
            fail(name, f"code cell {index} stores {len(outputs)} output(s)")
            break
    return len(code), len(md)


def execute(path: pathlib.Path, nb: nbformat.NotebookNode, timeout: int) -> dict:
    name = path.name
    workdir = pathlib.Path(tempfile.mkdtemp(prefix="psds-nb-"))
    try:
        started = time.time()
        client = NotebookClient(
            nb,
            timeout=timeout,
            kernel_name="python3",
            allow_errors=False,
            resources={"metadata": {"path": str(workdir)}},
        )
        client.execute()
        elapsed = time.time() - started

        text_chars = 0
        images = 0
        errors = 0
        for cell in nb.cells:
            for output in cell.get("outputs", []):
                if output.get("output_type") == "error":
                    errors += 1
                if output.get("output_type") == "stream":
                    size = len(output.get("text", ""))
                    text_chars += size
                    if size > MAX_CELL_TEXT:
                        fail(name, f"a single output is {size} characters")
                if output.get("output_type") == "display_data" and "image/png" in output.get("data", {}):
                    images += 1

        if text_chars > MAX_NOTEBOOK_TEXT:
            fail(name, f"text output totals {text_chars} characters (budget {MAX_NOTEBOOK_TEXT})")
        if errors:
            fail(name, f"{errors} cell(s) raised an error")
        if "plt.show()" in "\n".join(c.source for c in nb.cells if c.cell_type == "code") and images == 0:
            fail(name, "calls plt.show() but produced no image")
        return {"seconds": elapsed, "images": images, "text_kb": text_chars / 1024}
    except Exception as exc:  # noqa: BLE001 - report the failure, do not crash
        fail(name, f"execution failed: {type(exc).__name__}: {str(exc)[:300]}")
        return {"seconds": 0.0, "images": 0, "text_kb": 0.0}
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-exec", action="store_true", help="skip execution")
    ap.add_argument("--timeout", type=int, default=300, help="per-notebook timeout (s)")
    args = ap.parse_args()

    sources = sorted(SRC.glob("*.md"))
    if not sources:
        print("no notebook sources found")
        return 1

    notebooks = sorted(OUT.glob("*.ipynb"))
    if len(notebooks) != len(sources):
        fail("notebooks", f"{len(notebooks)} .ipynb files for {len(sources)} sources "
                          f"(run tools/build_notebooks.py)")

    if not args.no_exec:
        import build_notebooks  # noqa: PLC0415 - local import keeps --no-exec dependency-free

        stale = [s.name for s in sources
                 if not (OUT / f"{s.stem}.ipynb").exists()
                 or (OUT / f"{s.stem}.ipynb").read_text(encoding="utf-8")
                 != build_notebooks.render(build_notebooks.notebook(
                     s.read_text(encoding="utf-8")))]
        if stale:
            fail("sources", f"stale notebooks (rebuild with tools/build_notebooks.py): {stale}")

    print(f"{'notebook':50s} {'cells':>6} {'code':>5} {'img':>4} {'out KB':>7} {'secs':>6}")
    print("-" * 84)
    total = 0
    for path in notebooks:
        nb = nbformat.read(path, as_version=4)
        code_cells, md_cells = check_structure(path, nb)
        if args.no_exec:
            print(f"{path.name:50s} {len(nb.cells):6d} {code_cells:5d} {'-':>4} {'-':>7} {'-':>6}")
            continue
        stats = execute(path, nb, args.timeout)
        total += stats["seconds"]
        print(f"{path.name:50s} {len(nb.cells):6d} {code_cells:5d} "
              f"{stats['images']:4d} {stats['text_kb']:7.1f} {stats['seconds']:6.1f}")

    print("-" * 84)
    if args.no_exec:
        print(f"{len(notebooks)} notebook(s) checked structurally; execution skipped")
    else:
        print(f"{len(notebooks)} notebook(s) executed in {total:.1f}s total")

    if failures:
        print(f"\nFAILED {len(failures)} check(s):")
        for item in failures:
            print("  -", item)
        return 1
    print("\nAll notebook checks passed.")
    return 0


if __name__ == "__main__":
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    sys.exit(main())
