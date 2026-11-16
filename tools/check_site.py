"""Validate the generated website in ``site/``.

The build itself is validated by ``mkdocs build --strict``. This script checks
the *output*: that the pages and files a reader needs were actually produced,
that internal links in the generated HTML resolve, that maths is configured for
rendering, and that notebook downloads exist at their published paths.

Checks
------
1. Core artefacts exist: ``index.html``, ``sitemap.xml``, ``404.html``, search index.
2. Every ``.ipynb`` linked from the Markdown exists in ``docs/`` **and** was
   copied to the same path under ``site/``.
3. MathJax is configured and the maths spans reached the HTML.
4. Internal ``href``/``src`` targets in every generated page resolve.
5. No absolute filesystem, localhost or ``file://`` references leaked into the site.

Usage
-----
    mkdocs build --strict
    python tools/check_site.py

Exits 0 only when every check passes.
"""

from __future__ import annotations

import pathlib
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"

REQUIRED_FILES = ["index.html", "sitemap.xml", "404.html", "search/search_index.json"]

# The minify plugin strips quotes from attribute values, so accept both forms.
LINK_RE = re.compile(r'(?:href|src)=(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))')
IPYNB_RE = re.compile(r"\]\(([^)\s]+\.ipynb)\)")

SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "javascript:", "data:", "#")


def site_base_path() -> str:
    """The URL path the site is published under, e.g. /Probability-and-Statistics.

    GitHub Pages project sites are served from a subpath, and the 404 page uses
    absolute links that include it. Strip it before resolving against site/.
    """
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    match = re.search(r"^site_url:\s*(\S+)\s*$", config, re.MULTILINE)
    if not match:
        return ""
    return urlsplit(match.group(1)).path.rstrip("/")


BASE_PATH = site_base_path()


def html_pages() -> list[pathlib.Path]:
    return sorted(SITE.rglob("*.html"))


def resolve(target: str, page: pathlib.Path) -> pathlib.Path | None:
    """Resolve a link from a generated page to a file on disk, or None."""
    parts = urlsplit(target)
    path = unquote(parts.path)
    if not path:
        return None  # pure fragment
    if path.startswith("/"):
        base = BASE_PATH
        if base and (path == base or path.startswith(base + "/")):
            path = path[len(base):] or "/"
        candidate = SITE / path.lstrip("/")
    else:
        candidate = (page.parent / path).resolve()
    if candidate.is_dir():
        candidate = candidate / "index.html"
    return candidate


def main() -> int:
    failures: list[str] = []
    notes: list[str] = []

    if not SITE.is_dir():
        print(f"FAIL: no site/ directory; run 'mkdocs build --strict' first.")
        return 1

    # 1 — core artefacts
    for name in REQUIRED_FILES:
        if not (SITE / name).exists():
            failures.append(f"missing generated file: site/{name}")

    pages = html_pages()
    if len(pages) < 100:
        failures.append(f"only {len(pages)} HTML pages generated; expected the full course")
    notes.append(f"{len(pages)} HTML pages")

    # 2 — notebook download references
    nb_links = 0
    for md in sorted(DOCS.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        for target in IPYNB_RE.findall(text):
            if target.startswith(("http://", "https://")):
                continue
            nb_links += 1
            source = (md.parent / urlsplit(target).path).resolve()
            if not source.exists():
                failures.append(f"{md.relative_to(ROOT)}: notebook link target missing: {target}")
                continue
            published = SITE / source.relative_to(DOCS)
            if not published.exists():
                failures.append(
                    f"notebook not published: {source.relative_to(DOCS)} "
                    f"(linked from {md.relative_to(ROOT)})"
                )
    notes.append(f"{nb_links} notebook download links verified")
    if nb_links == 0:
        failures.append("no .ipynb download links found; the practicals table may have changed")

    # 3 — maths configuration and rendered spans
    mathjax_config = SITE / "assets/javascripts/mathjax.js"
    if not mathjax_config.exists():
        failures.append("missing site/assets/javascripts/mathjax.js (maths will not render)")
    index_html = (SITE / "index.html").read_text(encoding="utf-8", errors="replace")
    if "mathjax" not in index_html.lower():
        failures.append("index.html does not reference MathJax")
    math_spans = sum(
        p.read_text(encoding="utf-8", errors="replace").count("arithmatex") for p in pages
    )
    if math_spans < 1000:
        failures.append(f"only {math_spans} rendered maths spans; expected thousands")
    notes.append(f"{math_spans} maths spans")

    # 4 and 5 — link resolution
    checked = 0
    broken: list[str] = []
    for page in pages:
        html = page.read_text(encoding="utf-8", errors="replace")
        for groups in LINK_RE.findall(html):
            target = next((g for g in groups if g), "").replace("&amp;", "&")
            if not target:
                continue
            if target.startswith(SKIP_PREFIXES) or target.startswith("//"):
                continue
            checked += 1
            if "localhost" in target or target.startswith("file:"):
                broken.append(f"{page.relative_to(SITE)} -> {target} (non-public reference)")
                continue
            resolved = resolve(target, page)
            if resolved is not None and not resolved.exists():
                broken.append(f"{page.relative_to(SITE)} -> {target}")
    if broken:
        failures.append(f"{len(broken)} broken internal reference(s) in the generated site")
        failures.extend("    " + item for item in broken[:15])
        if len(broken) > 15:
            failures.append(f"    ... and {len(broken) - 15} more")
    notes.append(f"{checked} internal references resolved")

    # Assets must be present for the styles the pages request
    for asset in ["assets/stylesheets/extra.css", "assets/javascripts/labs.js"]:
        if not (SITE / asset).exists():
            failures.append(f"missing published asset: {asset}")

    print(f"site/ checks: {'; '.join(notes)}")
    if failures:
        print(f"\nFAILED {len(failures)} check(s):")
        for item in failures:
            print("  -", item)
        return 1
    print("\nGenerated site is complete and internally consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
