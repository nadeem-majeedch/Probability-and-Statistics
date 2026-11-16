"""Build the practical notebooks from Markdown sources.

Each source in ``tools/notebook_sources`` is Markdown in which a fenced
``python`` block becomes a code cell and everything else becomes a Markdown
cell. Other fenced blocks (``text``, ``bash``) stay inside the Markdown as
literal examples.

The generated notebooks are written to ``docs/practicals/notebooks`` with no
stored outputs, so the repository stays small and the site never embeds large
cell output. Execution is verified separately by ``tools/check_notebooks.py``.

Usage
-----
    python tools/build_notebooks.py            # regenerate every notebook
    python tools/build_notebooks.py --check     # verify the .ipynb files are current

Exits 0 on success, 1 when ``--check`` finds a stale or missing notebook.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

SRC = pathlib.Path("tools/notebook_sources")
OUT = pathlib.Path("docs/practicals/notebooks")

FENCE_OPEN = re.compile(r"^```([A-Za-z0-9+-]*)\s*$")
FENCE_CLOSE = re.compile(r"^```\s*$")

KERNELSPEC = {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3",
}
LANGUAGE_INFO = {"name": "python", "file_extension": ".py", "mimetype": "text/x-python"}


def cell(kind: str, text: str) -> dict:
    body = text.splitlines(keepends=True)
    if kind == "code":
        return {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": body,
        }
    return {"cell_type": "markdown", "metadata": {}, "source": body}


def cells(text: str) -> list[dict]:
    lines = text.splitlines()
    out: list[dict] = []
    md: list[str] = []

    def flush_md() -> None:
        body = "\n".join(md).strip("\n")
        if body.strip():
            out.append(cell("markdown", body))
        md.clear()

    i = 0
    while i < len(lines):
        m = FENCE_OPEN.match(lines[i])
        if not m:
            md.append(lines[i])
            i += 1
            continue
        lang = m.group(1)
        flush_md()
        j = i + 1
        block: list[str] = []
        while j < len(lines) and not FENCE_CLOSE.match(lines[j]):
            block.append(lines[j])
            j += 1
        if j >= len(lines):
            raise SystemExit(f"unclosed code fence in source near line {i + 1}")
        src = "\n".join(block).strip("\n")
        if lang == "python":
            out.append(cell("code", src + "\n"))
        else:
            out.append(cell("markdown", f"```{lang}\n{src}\n```"))
        i = j + 1
    flush_md()
    for index, c in enumerate(out):
        c["id"] = f"cell-{index:02d}"
    return out


def notebook(text: str) -> dict:
    return {
        "cells": cells(text),
        "metadata": {"kernelspec": KERNELSPEC, "language_info": LANGUAGE_INFO},
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def render(nb: dict) -> str:
    return json.dumps(nb, indent=1, ensure_ascii=False) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if outputs are stale")
    args = ap.parse_args()

    sources = sorted(SRC.glob("*.md"))
    if not sources:
        print("no notebook sources found")
        return 1

    OUT.mkdir(parents=True, exist_ok=True)
    stale: list[str] = []
    for src in sources:
        target = OUT / f"{src.stem}.ipynb"
        text = render(notebook(src.read_text(encoding="utf-8")))
        existing = target.read_text(encoding="utf-8") if target.exists() else None
        if args.check:
            if existing != text:
                stale.append(target.name)
            continue
        target.write_text(text, encoding="utf-8")

    if args.check:
        if stale:
            print(f"{len(stale)} notebook(s) out of date:")
            for name in stale:
                print("  -", name)
            print("run: python tools/build_notebooks.py")
            return 1
        print(f"all {len(sources)} notebooks are up to date")
        return 0

    print(f"wrote {len(sources)} notebooks to {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
