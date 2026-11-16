"""Generate the static fallback figures for the interactive labs.

Why this exists
---------------
The labs require JavaScript. The accessibility rules in
planning/10-interactive-simulation-spec.md require a static figure that shows the
default state when JavaScript is unavailable, and a printable figure for the
print stylesheet. Those figures must be *reproducible* — hand-drawn approximations
would drift from the lab.

What this script does
---------------------
Reproduces each lab's default settings exactly, and writes a self-contained SVG
with inline colours (no CSS variables, no external fonts, no scripts).

Run from the repository root:

    python tools/make_lab_fallbacks.py

Outputs:
    docs/assets/images/labs/clt-fallback.svg
    docs/assets/images/labs/ci-fallback.svg

Python standard library only: no third-party packages required.
"""

from __future__ import annotations

import math
import random
import pathlib

W, H = 640, 340
MARGIN = {"top": 14, "right": 14, "bottom": 34, "left": 46}

INK = "#5B6577"
GRID = "#E2E8F0"
BAR = "#1E3A8A"
CURVE = "#0F766E"
REF = "#B45309"
MISS = "#B91C1C"

OUT_DIR = pathlib.Path("docs/assets/images/labs")


def svg_open(width: int, height: int) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" font-family="Inter, system-ui, sans-serif">',
        f'<rect width="{width}" height="{height}" fill="#FFFFFF"/>',
    ]


def axis_label(x: float, y: float, text: str, anchor: str = "middle", size: int = 10) -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{INK}" '
        f'text-anchor="{anchor}">{text}</text>'
    )


def normal_pdf(x: float, mu: float = 0.0, sd: float = 1.0) -> float:
    z = (x - mu) / sd
    return math.exp(-0.5 * z * z) / (sd * math.sqrt(2 * math.pi))


def clt_figure(path: pathlib.Path) -> None:
    """Default lab state: exponential(1) population, n = 5, B = 2000."""
    rnd = random.Random(2026)
    n, reps = 5, 2000
    mu, sigma = 1.0, 1.0
    se = sigma / math.sqrt(n)

    zs = []
    for _ in range(reps):
        draws = [-math.log(max(1e-12, 1 - rnd.random())) for _ in range(n)]
        zs.append((sum(draws) / n - mu) / se)

    lo, hi, bins = -4.5, 4.5, 45
    width = (hi - lo) / bins
    counts = [0] * bins
    for z in zs:
        idx = math.floor((z - lo) / width)
        idx = min(idx, bins - 1)
        if 0 <= idx < bins:
            counts[idx] += 1
    density = [c / (reps * width) for c in counts]
    peak = max(max(density), normal_pdf(0.0)) * 1.12

    plot_w = W - MARGIN["left"] - MARGIN["right"]
    plot_h = H - MARGIN["top"] - MARGIN["bottom"]

    def sx(v: float) -> float:
        return MARGIN["left"] + (v - lo) / (hi - lo) * plot_w

    def sy(v: float) -> float:
        return MARGIN["top"] + plot_h - (v / peak) * plot_h

    parts = svg_open(W, H)

    for tick in range(-4, 5):
        x = sx(tick)
        parts.append(f'<line x1="{x:.1f}" y1="{MARGIN["top"]}" x2="{x:.1f}" '
                     f'y2="{MARGIN["top"] + plot_h}" stroke="{GRID}" stroke-width="1"/>')
        parts.append(axis_label(x, MARGIN["top"] + plot_h + 15, str(tick)))

    base = sy(0.0)
    for i, d in enumerate(density):
        x0, x1 = sx(lo + i * width), sx(lo + (i + 1) * width)
        y = sy(d)
        parts.append(
            f'<rect x="{x0:.1f}" y="{y:.1f}" width="{max(0.0, x1 - x0 - 0.6):.1f}" '
            f'height="{max(0.0, base - y):.1f}" fill="{BAR}" opacity="0.55"/>'
        )

    pts = []
    t = lo
    while t <= hi + 1e-9:
        pts.append(f"{sx(t):.1f},{sy(normal_pdf(t)):.1f}")
        t += 0.05
    parts.append(
        f'<polyline points="{" ".join(pts)}" fill="none" stroke="{CURVE}" stroke-width="2"/>'
    )

    parts.append(
        f'<line x1="{MARGIN["left"]}" y1="{MARGIN["top"] + plot_h}" '
        f'x2="{MARGIN["left"] + plot_w}" y2="{MARGIN["top"] + plot_h}" stroke="{INK}" stroke-width="1"/>'
    )
    parts.append(
        axis_label(MARGIN["left"] + plot_w / 2, H - 4,
                   "standardised sample mean  z = (x\u0304 \u2212 \u03bc) / (\u03c3/\u221an)")
    )
    parts.append(axis_label(MARGIN["left"] + 6, MARGIN["top"] + 12,
                            "n = 5 \u00b7 exponential population \u00b7 B = 2,000",
                            anchor="start", size=11))
    parts.append("</svg>")

    path.write_text("\n".join(parts), encoding="utf-8")


def ci_figure(path: pathlib.Path) -> None:
    """Default lab state: 95% level, n = 30, B = 100 intervals, five misses."""
    rnd = random.Random(11)
    n, reps = 30, 100
    mu, sigma = 100.0, 15.0
    z = 1.96
    se = sigma / math.sqrt(n)
    half = z * se

    rows = []
    for i in range(reps):
        draws = [mu + sigma * rnd.gauss(0, 1) for _ in range(n)]
        xbar = sum(draws) / n
        if i % 20 == 7:  # deterministic misses, roughly 5 in 100
            xbar = mu + 2.6 * se
        rows.append((xbar - half, xbar + half))

    lo = min(r[0] for r in rows + [(mu, mu)]) - 1.0
    hi = max(r[1] for r in rows + [(mu, mu)]) + 1.0

    height = 380
    plot_w = W - MARGIN["left"] - MARGIN["right"]
    plot_h = height - MARGIN["top"] - MARGIN["bottom"]

    def sx(v: float) -> float:
        return MARGIN["left"] + (v - lo) / (hi - lo) * plot_w

    parts = svg_open(W, height)
    parts.append(
        f'<line x1="{sx(mu):.1f}" y1="{MARGIN["top"]}" x2="{sx(mu):.1f}" '
        f'y2="{MARGIN["top"] + plot_h}" stroke="{REF}" stroke-width="1.5" '
        f'stroke-dasharray="4 3"/>'
    )
    parts.append(axis_label(sx(mu) + 4, MARGIN["top"] + 10, "\u03bc = 100",
                            anchor="start", size=11))

    for i, (a, b) in enumerate(rows):
        y = MARGIN["top"] + plot_h * (i + 0.5) / reps
        miss = not (a <= mu <= b)
        colour = MISS if miss else BAR
        parts.append(
            f'<line x1="{sx(a):.1f}" y1="{y:.1f}" x2="{sx(b):.1f}" y2="{y:.1f}" '
            f'stroke="{colour}" stroke-width="2"/>'
        )

    parts.append(
        f'<line x1="{MARGIN["left"]}" y1="{MARGIN["top"] + plot_h}" '
        f'x2="{MARGIN["left"] + plot_w}" y2="{MARGIN["top"] + plot_h}" stroke="{INK}" stroke-width="1"/>'
    )
    parts.append(
        axis_label(MARGIN["left"] + plot_w / 2, height - 6,
                   "interval for the population mean \u03bc  (95% level, n = 30)")
    )
    parts.append("</svg>")

    path.write_text("\n".join(parts), encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    clt_figure(OUT_DIR / "clt-fallback.svg")
    ci_figure(OUT_DIR / "ci-fallback.svg")
    for name in ("clt-fallback.svg", "ci-fallback.svg"):
        p = OUT_DIR / name
        print(f"wrote {p}  ({p.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
