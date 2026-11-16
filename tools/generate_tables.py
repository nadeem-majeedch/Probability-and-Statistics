"""Generate the critical-value tables in docs/reference/tables/.

Every number in the published tables comes from SciPy. Nothing is typed by
hand: the generator writes both the Markdown table blocks inside the reference
pages and the CSV downloads, so the page and the download cannot disagree.

How the values are produced
---------------------------
* Standard normal.  ``scipy.stats.norm.cdf(z)`` for the cumulative table, and
  ``scipy.stats.norm.ppf(1 - alpha)`` for the upper-tail critical values.
* Student t.        ``scipy.stats.t.ppf(1 - alpha, df)``; ``df = inf`` is the
  normal limit and is taken from ``norm.ppf``. The table is one-sided by
  construction, which is why the two-tailed level is always twice the column
  heading.
* Chi-square.      ``scipy.stats.chi2.isf(alpha, df)`` — the upper-tail
  quantile F^{-1}(1 - alpha).
* F.               ``scipy.stats.f.isf(alpha, df1, df2)``. For an infinite
  denominator the limit is ``chi2.isf(alpha, df1) / df1``; that identity is
  used rather than an arbitrary large number.

Tail convention
---------------
Every critical value is an **upper-tail** quantile: the tabled number c
satisfies P(X > c) = alpha. The normal table prints the *cumulative*
probability Phi(z) (lower tail), because that is how students read a z-table,
and the page explains that the upper tail is 1 - Phi(z).

Precision and rounding
----------------------
Values are computed in double precision (about 15-16 significant digits) and
formatted with the fixed number of decimals stated for each table:

* Phi(z): 4 decimals (about 5e-5 absolute error at most).
* t: 4 decimals; chi-square: 3 decimals; F: 3 decimals.

Python's format() rounds the binary value to the nearest printed decimal, so
each cell is within half a unit of the last printed place of the true value.
The verifier (tools/check_tables.py) recomputes every cell from a second SciPy
formulation and fails if any cell is off by more than that.

Usage
-----
    python tools/generate_tables.py           # rewrite the tables
    python tools/generate_tables.py --check   # fail if anything is out of date
"""

from __future__ import annotations

import csv
import io
import math
import pathlib
import sys

from scipy.stats import chi2, f as fdist, norm, t as tdist

ROOT = pathlib.Path(__file__).resolve().parent.parent
TABLES = ROOT / "docs" / "reference" / "tables"
DATA = ROOT / "docs" / "data" / "tables"

BEGIN = "<!-- table:begin -->"
END = "<!-- table:end -->"

# ------------------------------------------------------------------ grid design

Z_ROWS = [round(-3.4 + 0.1 * i, 1) for i in range(69)]  # -3.4 ... 3.4
Z_COLS = [round(0.01 * j, 2) for j in range(10)]  # 0.00 ... 0.09

T_DF = [*range(1, 31), 40, 50, 60, 80, 100, 120, math.inf]
T_ALPHAS = [0.10, 0.05, 0.025, 0.01, 0.005]  # one-tailed

CHI_DF = [*range(1, 31), 40, 50, 60, 80, 100]
CHI_ALPHAS = [0.995, 0.99, 0.975, 0.95, 0.90, 0.10, 0.05, 0.025, 0.01, 0.005]

F_DF1 = [*range(1, 13), 15, 20, 24, 30, 40, 60, 120]
F_DF2 = [*range(1, 31), 40, 60, 120, math.inf]
F_ALPHAS = [0.05, 0.01]


# ------------------------------------------------------------------- formatters


def fmt(value: float, places: int) -> str:
    """Round to `places` decimals, keeping the leading zero (0.0123, not .0123),
    because the prose examples on the pages are written with it."""
    return f"{value:.{places}f}"


def df_label(df: float) -> str:
    return "&infin;" if math.isinf(df) else str(int(df))


def alpha_label(alpha: float) -> str:
    """0.05 -> 0.05, 0.005 -> 0.005, 0.995 -> 0.995 (no trailing zeros)."""
    return f"{alpha:g}"


# ---------------------------------------------------------------- computations


def z_cumulative(z: float) -> float:
    return float(norm.cdf(z))


def t_critical(alpha: float, df: float) -> float:
    if math.isinf(df):
        return float(norm.ppf(1 - alpha))
    return float(tdist.ppf(1 - alpha, df))


def chi_critical(alpha: float, df: float) -> float:
    return float(chi2.isf(alpha, df))


def f_critical(alpha: float, df1: float, df2: float) -> float:
    if math.isinf(df2):
        return float(chi2.isf(alpha, df1) / df1)
    return float(fdist.isf(alpha, df1, df2))


# -------------------------------------------------------------------- builders


def build_z_table() -> str:
    lines = [
        "| z | " + " | ".join(f"{c:.2f}" for c in Z_COLS) + " |",
        "|---:|" + "---:|" * len(Z_COLS),
    ]
    for z in Z_ROWS:
        cells = [fmt(z_cumulative(round(z + c, 2)), 4) for c in Z_COLS]
        label = f"{z:.1f}"
        lines.append(f"| **{label}** | " + " | ".join(cells) + " |")
    return "\n".join(lines)


def build_z_head_table() -> str:
    """The row labels, repeated, so a reader can find -3.4 and 3.4 at a glance."""
    lines = ["| z | &Phi;(z) | upper tail 1 - &Phi;(z) |", "|---:|---:|---:|"]
    for z in (-3.0, -2.58, -2.0, -1.96, -1.645, -1.0, -0.5, 0.0, 0.5, 1.0, 1.645, 1.96, 2.0, 2.58, 3.0):
        phi = z_cumulative(z)
        lines.append(f"| {z:g} | {fmt(phi, 4)} | {fmt(1 - phi, 4)} |")
    return "\n".join(lines)


def build_t_table() -> str:
    head = "| df | " + " | ".join(alpha_label(a) for a in T_ALPHAS) + " |"
    lines = [head, "|---:|" + "---:|" * len(T_ALPHAS)]
    for df in T_DF:
        cells = [fmt(t_critical(a, df), 4) for a in T_ALPHAS]
        lines.append(f"| **{df_label(df)}** | " + " | ".join(cells) + " |")
    return "\n".join(lines)


def build_t_twotail_map() -> str:
    lines = [
        "| one-tailed &alpha; | " + " | ".join(alpha_label(a) for a in T_ALPHAS) + " |",
        "|---:|" + "---:|" * len(T_ALPHAS),
        "| two-tailed &alpha; | " + " | ".join(alpha_label(2 * a) for a in T_ALPHAS) + " |",
    ]
    return "\n".join(lines)


def build_chi_table() -> str:
    head = "| df | " + " | ".join(alpha_label(a) for a in CHI_ALPHAS) + " |"
    lines = [head, "|---:|" + "---:|" * len(CHI_ALPHAS)]
    for df in CHI_DF:
        cells = [fmt(chi_critical(a, df), 3) for a in CHI_ALPHAS]
        lines.append(f"| **{df_label(df)}** | " + " | ".join(cells) + " |")
    return "\n".join(lines)


def build_f_table(alpha: float) -> str:
    head = "| df<sub>2</sub> &#8595; / df<sub>1</sub> &#8594; | " + " | ".join(df_label(d) for d in F_DF1) + " |"
    lines = [head, "|---:|" + "---:|" * len(F_DF1)]
    for df2 in F_DF2:
        cells = [fmt(f_critical(alpha, df1, df2), 3) for df1 in F_DF1]
        lines.append(f"| **{df_label(df2)}** | " + " | ".join(cells) + " |")
    return "\n".join(lines)


# ------------------------------------------------------------------- generation

BLOCKS = {
    "standard-normal.md": {"z-table": build_z_table, "z-head": build_z_head_table},
    "t-distribution.md": {"t-table": build_t_table, "t-two-tail": build_t_twotail_map},
    "chi-square.md": {"chi-table": build_chi_table},
    "f-distribution.md": {
        "f-005": lambda: build_f_table(0.05),
        "f-001": lambda: build_f_table(0.01),
    },
}


def csv_text(header: list[str], rows: list[list[str]]) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(header)
    writer.writerows(rows)
    return buffer.getvalue()


def build_csvs() -> dict[str, str]:
    out: dict[str, str] = {}

    rows = [[f"{z:.1f}"] + [f"{z_cumulative(round(z + c, 2)):.4f}" for c in Z_COLS] for z in Z_ROWS]
    out["standard-normal.csv"] = csv_text(["z"] + [f"{c:.2f}" for c in Z_COLS], rows)

    rows = [[df_label(df)] + [f"{t_critical(a, df):.4f}" for a in T_ALPHAS] for df in T_DF]
    out["t-one-tailed.csv"] = csv_text(["df"] + [alpha_label(a) for a in T_ALPHAS], rows)

    rows = [[df_label(df)] + [f"{chi_critical(a, df):.3f}" for a in CHI_ALPHAS] for df in CHI_DF]
    out["chi-square.csv"] = csv_text(["df"] + [alpha_label(a) for a in CHI_ALPHAS], rows)

    for alpha in F_ALPHAS:
        rows = [[df_label(df2)] + [f"{f_critical(alpha, df1, df2):.3f}" for df1 in F_DF1] for df2 in F_DF2]
        out[f"f-{str(alpha).replace('.', '')}.csv"] = csv_text(
            ["df2"] + [df_label(d) for d in F_DF1], rows
        )
    return out


def render_block(name: str, body: str) -> str:
    return f'{BEGIN}\n\n<div class="psds-table-scroll" markdown>\n\n{body}\n\n</div>\n\n{END}'


def fill_page(path: pathlib.Path) -> bool:
    """Replace every marked block in one page. Returns True if the file changed."""
    text = path.read_text(encoding="utf-8")
    blocks = BLOCKS[path.name]
    for name, builder in blocks.items():
        open_tag = f"<!-- block:{name} -->"
        close_tag = f"<!-- /block:{name} -->"
        if open_tag not in text:
            raise SystemExit(f"{path.name}: missing marker {open_tag}")
        head, rest = text.split(open_tag, 1)
        _, tail = rest.split(close_tag, 1)
        text = head + open_tag + "\n\n" + render_block(name, builder()) + "\n\n" + close_tag + tail
    if text != path.read_text(encoding="utf-8"):
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main(argv: list[str]) -> int:
    check = "--check" in argv
    changed: list[str] = []

    for name in BLOCKS:
        path = TABLES / name
        if not path.exists():
            print(f"  MISSING page {path.relative_to(ROOT)}")
            return 1
        before = path.read_text(encoding="utf-8")
        fill_page(path)
        after = path.read_text(encoding="utf-8")
        if after != before:
            changed.append(str(path.relative_to(ROOT)))
            if check:
                path.write_text(before, encoding="utf-8")

    DATA.mkdir(parents=True, exist_ok=True)
    for name, content in build_csvs().items():
        path = DATA / name
        old = path.read_text(encoding="utf-8") if path.exists() else None
        if old != content:
            changed.append(str(path.relative_to(ROOT)))
            if not check:
                path.write_text(content, encoding="utf-8")

    if check:
        if changed:
            print("Tables are out of date. Run: python tools/generate_tables.py")
            for name in changed:
                print("  -", name)
            return 1
        print("  OK   tables and CSV downloads match SciPy")
        return 0

    if changed:
        print(f"updated {len(changed)} file(s):")
        for name in changed:
            print("  -", name)
    else:
        print("tables already up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
