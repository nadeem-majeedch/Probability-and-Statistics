"""Check mathematics delimiters in the course Markdown.

The site renders maths with MathJax in `pymdownx.arithmatex` generic mode, which
means inline maths must be written with \\( ... \\) and display maths with
\\[ ... \\]. A stray `$` is not maths on this site: it renders literally and, in a
page about money or shell commands, can corrupt surrounding text.

Checks performed
----------------
1. Unbalanced \\( \\) or \\[ \\] delimiters within a file.
2. Dollar signs used as maths delimiters (`$...$` or `$$...$$`).
3. `\\begin{...}` environments without a matching `\\end{...}`.

Usage
-----
    python tools/check_math.py            # report and exit 1 on problems
    python tools/check_math.py --quiet    # exit code only

Exits 0 when clean, 1 when problems are found.
"""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path("docs")
FENCE = re.compile(r"^(```|~~~)")


def code_mask(lines: list[str]) -> list[bool]:
    """True where a line is inside a fenced code block (skip those)."""
    inside = False
    mask = []
    for line in lines:
        if FENCE.match(line.strip()):
            inside = not inside
            mask.append(True)
            continue
        mask.append(inside)
    return mask


def check_file(path: pathlib.Path) -> list[str]:
    problems = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    mask = code_mask(lines)

    for i, line in enumerate(lines, 1):
        if mask[i - 1]:
            continue
        # Strip inline code spans: `$HOME` in backticks is legitimate prose.
        cleaned = re.sub(r"`[^`]*`", "", line)
        if "$" in cleaned:
            problems.append(f"{path}:{i}: dollar sign outside inline code: {line.strip()[:90]}")

    body = "\n".join(l for l, m in zip(lines, mask) if not m)
    pairs = [("\\( ", " \\)"), ("\\(", "\\)"), ("\\[", "\\]")]
    for opener, closer in (("\\(", "\\)"), ("\\[", "\\]")):
        if body.count(opener) != body.count(closer):
            problems.append(
                f"{path}: unbalanced {opener} ... {closer} "
                f"({body.count(opener)} open vs {body.count(closer)} close)"
            )

    for env in set(re.findall(r"\\begin\{([a-zA-Z*]+)\}", body)):
        starts = body.count("\\begin{" + env + "}")
        ends = body.count("\\end{" + env + "}")
        if starts != ends:
            problems.append(f"{path}: environment '{env}' has {starts} begin, {ends} end")

    return problems


def main() -> int:
    quiet = "--quiet" in sys.argv
    files = sorted(ROOT.rglob("*.md"))
    problems: list[str] = []
    for f in files:
        problems.extend(check_file(f))

    if not quiet:
        print(f"checked {len(files)} Markdown files under {ROOT}/")
        if problems:
            for p in problems:
                print("  FAIL", p)
        else:
            print("  OK   delimiters balanced, no stray dollar maths")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
