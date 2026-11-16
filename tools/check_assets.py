"""Check that every referenced asset exists, and that nothing is oversized.

Guards two quality risks:
  R06  repository bloat (size budgets in planning/03-repository-structure.md)
  G-5  broken references (images, downloads)

Checks
------
1. Every local image / asset referenced from a Markdown page exists.
2. No file under docs/ exceeds 2 MB.
3. Report total size of docs/ against the 40 MB build budget.

Usage
-----
    python tools/check_assets.py

Exits 0 when clean, 1 when a reference is broken or a size budget is exceeded.
"""

from __future__ import annotations

import pathlib
import re
import sys

DOCS = pathlib.Path("docs")
MAX_FILE = 2 * 1024 * 1024
MAX_TOTAL = 40 * 1024 * 1024

IMG_MD = re.compile(r"!\[[^\]]*\]\(([^)\s]+)")
IMG_HTML = re.compile(r"<img[^>]+src=\"([^\"]+)\"", re.IGNORECASE)
LINK_ASSET = re.compile(r"\]\(([^)\s]+\.(?:svg|png|jpg|jpeg|gif|webp|csv|ipynb|pdf))\)")


def references(text: str) -> list[tuple[str, str]]:
    """Return (reference, resolution rule) pairs.

    Two rules, because MkDocs treats the two kinds of reference differently:

    * Markdown images and links are parsed by MkDocs, which rewrites the URL for
      the output page. Authors therefore write the path relative to the SOURCE
      file: `../assets/x.svg` from `docs/labs/clt.md`.

    * Raw HTML `<img src="...">` is passed through untouched. The browser then
      resolves it against the PAGE URL, and with `use_directory_urls: true` the
      page for `docs/labs/clt.md` lives at `/labs/clt/`. Authors therefore need
      one extra level: `../../assets/x.svg`.

    Resolving both cases with one rule is how a broken image ships unnoticed.
    """
    refs: list[tuple[str, str]] = []
    for m in IMG_MD.finditer(text):
        refs.append((m.group(1), "source"))
    for m in LINK_ASSET.finditer(text):
        refs.append((m.group(1), "source"))
    for m in IMG_HTML.finditer(text):
        refs.append((m.group(1), "page"))
    return refs


def main() -> int:
    problems: list[str] = []
    checked = 0

    for page in sorted(DOCS.rglob("*.md")):
        text = page.read_text(encoding="utf-8")
        for ref, rule in references(text):
            if ref.startswith(("http://", "https://", "#", "mailto:", "data:")):
                continue
            clean = ref.split("#")[0]
            base = page.parent if rule == "source" else page.parent / page.stem
            target = (base / clean).resolve()
            checked += 1
            if not target.exists():
                hint = " (raw HTML resolves against the page URL; add one ../)" if rule == "page" else ""
                problems.append(f"{page}: broken asset reference '{ref}'{hint}")

    total = 0
    for f in sorted(DOCS.rglob("*")):
        if not f.is_file():
            continue
        size = f.stat().st_size
        total += size
        if size > MAX_FILE:
            problems.append(f"{f}: {size / 1048576:.2f} MB exceeds the 2 MB per-file budget")

    if total > MAX_TOTAL:
        problems.append(f"docs/ total {total / 1048576:.1f} MB exceeds the 40 MB budget")

    print(f"checked {checked} asset references across {DOCS}/")
    print(f"docs/ total size: {total / 1024:.0f} KB")
    if problems:
        for p in problems:
            print("  FAIL", p)
        return 1
    print("  OK   all references resolve, all sizes within budget")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
