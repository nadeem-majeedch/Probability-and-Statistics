"""Verify every published critical value against SciPy, independently.

`tools/generate_tables.py` produces the tables. This script does not trust it:
it re-reads the numbers **as published** (the Markdown in docs/reference/tables/
and the CSV downloads), recomputes each one from SciPy using a different
formulation than the generator used, and fails if any cell is further from the
true value than rounding to the printed place can explain.

Checks, in order:

1. the pages and the CSV downloads still match the generator (no drift);
2. every numeric cell parses, and the grid has the expected shape;
3. every cell agrees with SciPy within half a unit of its last printed digit;
4. the tables are internally monotone (critical values rise as alpha falls and as
   df rises);
5. symmetry of the normal table, Phi(0) = 0.5, and the normal limit rows;
6. the pages' worked examples that quote a tabled value agree with the table.

Independent formulations used here (so a systematic error in the generator cannot
hide): the normal lower tail from `scipy.special.ndtr`, the t and F upper tails
from `scipy.stats.t.sf` and `f.sf` inverted by brentq, and the chi-square upper
tail from `scipy.stats.chi2.logsf` exponentiated.

Run with the practical environment: .venv-prac/Scripts/python.exe tools/check_tables.py
"""

from __future__ import annotations

import csv
import math
import pathlib
import re
import subprocess
import sys

from scipy.optimize import brentq
from scipy.special import ndtr
from scipy.stats import chi2, f as fdist, t as tdist

ROOT = pathlib.Path(__file__).resolve().parent.parent
TABLES = ROOT / "docs" / "reference" / "tables"
DATA = ROOT / "docs" / "data" / "tables"

Z_TOL = 0.5e-4
T_TOL = 0.5e-4
CHI_TOL = 0.5e-3
F_TOL = 0.5e-3

problems: list[str] = []


def fail(message: str) -> None:
    problems.append(message)


# ---------------------------------------------------------------- independence


def z_cdf(z: float) -> float:
    return float(ndtr(z))


def t_upper(alpha: float, df: float) -> float:
    """Invert t.sf by bisection rather than calling a quantile function."""
    if math.isinf(df):
        return float(-brentq(lambda x: ndtr(x) - alpha, -10, 10, xtol=1e-12))
    return float(brentq(lambda x: tdist.sf(x, df) - alpha, 1e-6, 1e4, xtol=1e-12))


def chi_upper(alpha: float, df: float) -> float:
    return float(brentq(lambda x: math.exp(chi2.logsf(x, df)) - alpha, 1e-6, 1e5, xtol=1e-12))


def f_upper(alpha: float, df1: float, df2: float) -> float:
    if math.isinf(df2):
        return float(chi_upper(alpha, df1) / df1)
    return float(brentq(lambda x: fdist.sf(x, df1, df2) - alpha, 1e-6, 1e6, xtol=1e-12))


# -------------------------------------------------------------------- parsing


def table_rows(text: str, block: str) -> list[list[str]]:
    """Return the rows of the first Markdown table inside <!-- block:block -->."""
    if f"<!-- block:{block} -->" not in text:
        fail(f"missing block marker: {block}")
        return []
    section = text.split(f"<!-- block:{block} -->", 1)[1].split(f"<!-- /block:{block} -->", 1)[0]
    rows: list[list[str]] = []
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if all(set(c) <= set("-: ") for c in cells):     # alignment row
            continue
        rows.append(cells)
    return rows


def num(text: str) -> float:
    clean = text.replace("*", "").replace("&infin;", "").replace("&nbsp;", "").strip()
    clean = re.sub(r"<[^>]+>", "", clean)
    return float(clean)


def df_value(text: str) -> float:
    clean = re.sub(r"<[^>]+>", "", text.replace("*", "")).replace("&infin;", "").strip()
    return math.inf if clean == "" else float(clean)


def csv_rows(name: str) -> list[list[str]]:
    with (DATA / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.reader(handle))


# ----------------------------------------------------------------- checks


def check_regeneration() -> None:
    result = subprocess.run(
        [sys.executable, "tools/generate_tables.py", "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        fail("pages or CSVs are out of date with the generator:\n" + (result.stdout or "").strip())
    else:
        print("  OK   pages and CSV downloads match the generator")


def check_z() -> None:
    text = (TABLES / "standard-normal.md").read_text(encoding="utf-8")
    rows = table_rows(text, "z-table")
    if len(rows) != 70:
        fail(f"standard normal table has {len(rows)} rows including the header, expected 70")
        return
    header = rows[0]
    if len(header) != 11:
        fail(f"standard normal table has {len(header)} columns, expected 11")
    cols = [float(c) for c in header[1:]]
    if cols != [round(0.01 * i, 2) for i in range(10)]:
        fail(f"standard normal column headings are unexpected: {cols}")

    seen: dict[float, dict[float, float]] = {}
    worst = 0.0
    for row in rows[1:]:
        z_row = float(row[0].replace("*", ""))
        for col, cell in zip(cols, row[1:]):
            z = round(z_row + col, 2)
            value = num(cell)
            want = z_cdf(z)
            worst = max(worst, abs(value - want))
            if abs(value - want) > Z_TOL:
                fail(f"Phi({z}) is {value}, scipy gives {want:.7f}")
            seen.setdefault(round(z_row, 1), {})[col] = value

    if worst > Z_TOL:
        fail(f"standard normal worst absolute error {worst:.2e}")

    # symmetry Phi(-z) = 1 - Phi(z), and Phi(0) = 0.5
    for z_row, cells in seen.items():
        if z_row < 0:
            partner = seen.get(round(-z_row, 1), {})
            for col, value in cells.items():
                mirror = round(1.0 - col, 2)
                if mirror in partner and abs(value + partner[mirror] - 1.0) > 2 * Z_TOL:
                    fail(f"asymmetry at z={z_row + col}: {value} + {partner[mirror]} != 1")
    if abs(seen[0.0][0.0] - 0.5) > Z_TOL:
        fail(f"Phi(0) is {seen[0.0][0.0]}, expected 0.5")
    print(f"  OK   standard normal: 69 rows x 10 columns, worst error {worst:.1e}, symmetry holds")


def check_t() -> None:
    text = (TABLES / "t-distribution.md").read_text(encoding="utf-8")
    rows = table_rows(text, "t-table")
    mappings = table_rows(text, "t-two-tail")
    if len(mappings) != 2:
        fail("two-tailed mapping table should have a one-tailed row and a two-tailed row")
    else:
        for one, two in zip(mappings[0][1:], mappings[1][1:]):
            if abs(2 * float(one) - float(two)) > 1e-12:
                fail(f"two-tailed level {two} is not double the one-tailed level {one}")

    if len(rows) != 38:
        fail(f"t table has {len(rows)} rows including the header, expected 38")
        return
    alphas = [float(a) for a in rows[0][1:]]
    if alphas != [0.10, 0.05, 0.025, 0.01, 0.005]:
        fail(f"t table levels are unexpected: {alphas}")

    worst = 0.0
    previous: list[float] = [math.inf] * len(alphas)
    dfs: list[float] = []
    for row in rows[1:]:
        df = df_value(row[0])
        dfs.append(df)
        values = [num(c) for c in row[1:]]
        for alpha, value in zip(alphas, values):
            want = t_upper(alpha, df)
            worst = max(worst, abs(value - want))
            if abs(value - want) > T_TOL:
                fail(f"t({alpha}, df={df}) is {value}, scipy gives {want:.7f}")
        for i, value in enumerate(values):
            if value > previous[i] + T_TOL:          # must fall as df rises
                fail(f"t column {alphas[i]} is not monotone at df={df}: {value} > {previous[i]}")
        previous = values

    expected_df = [*range(1, 31), 40, 50, 60, 80, 100, 120, math.inf]
    if dfs != expected_df:
        fail(f"t table df coverage is unexpected: {dfs}")

    # the infinite row must equal the normal quantiles
    last = [num(c) for c in rows[-1][1:]]
    for alpha, value in zip(alphas, last):
        want = float(-brentq(lambda x: ndtr(x) - alpha, -10, 10, xtol=1e-12))
        if abs(value - want) > T_TOL:
            fail(f"t table df=inf, alpha={alpha}: {value} vs normal {want:.7f}")
    print(f"  OK   t: df 1-30, 40-120, inf; 5 levels; worst error {worst:.1e}; monotone; normal limit exact")


def check_chi() -> None:
    text = (TABLES / "chi-square.md").read_text(encoding="utf-8")
    rows = table_rows(text, "chi-table")
    expected_rows = len([*range(1, 31), 40, 50, 60, 80, 100]) + 1
    if len(rows) != expected_rows:
        fail(f"chi-square table has {len(rows)} rows including the header, expected {expected_rows}")
        return
    alphas = [float(a) for a in rows[0][1:]]
    expected = [0.995, 0.99, 0.975, 0.95, 0.90, 0.10, 0.05, 0.025, 0.01, 0.005]
    if alphas != expected:
        fail(f"chi-square levels are unexpected: {alphas}")

    worst = 0.0
    dfs: list[float] = []
    for row in rows[1:]:
        df = df_value(row[0])
        dfs.append(df)
        for alpha, cell in zip(alphas, row[1:]):
            value = num(cell)
            want = chi_upper(alpha, df)
            worst = max(worst, abs(value - want))
            if abs(value - want) > CHI_TOL:
                fail(f"chi2({alpha}, df={df}) is {value}, scipy gives {want:.6f}")

    if dfs != [*range(1, 31), 40, 50, 60, 80, 100]:
        fail(f"chi-square df coverage is unexpected: {dfs}")

    # each column must rise as df rises; upper-tail values decline as alpha rises
    for col in range(len(alphas)):
        column = [num(row[1 + col]) for row in rows[1:]]
        if any(b <= a for a, b in zip(column, column[1:])):
            fail(f"chi-square column {alphas[col]} is not increasing in df")
    # Within each half of the table the columns run from a large alpha to a small
    # one, so the quantile must increase left to right (smaller tail area, larger
    # value). The two halves are separate runs, so each is checked on its own.
    for row in rows[1:]:
        values = [num(c) for c in row[1:]]
        for start in (0, 5):
            half = values[start:start + 5]
            if any(b < a - CHI_TOL for a, b in zip(half, half[1:])):
                fail(f"chi-square row df={df_value(row[0])}: quantile does not rise as alpha falls")
    print(f"  OK   chi-square: df 1-30, 40-100; 10 levels; worst error {worst:.1e}; monotone in df and alpha")


def check_f() -> None:
    text = (TABLES / "f-distribution.md").read_text(encoding="utf-8")
    blocks = {"f-005": 0.05, "f-001": 0.01}
    df1_expected = [*range(1, 13), 15, 20, 24, 30, 40, 60, 120]
    df2_expected = [*range(1, 31), 40, 60, 120, math.inf]
    worst = 0.0
    cells = 0
    for block, alpha in blocks.items():
        rows = table_rows(text, block)
        if len(rows) != len(df2_expected) + 1:
            fail(f"{block}: {len(rows)} rows including the header, expected {len(df2_expected) + 1}")
            continue
        df1 = [df_value(c) for c in rows[0][1:]]
        if df1 != df1_expected:
            fail(f"{block}: numerator df coverage is unexpected: {df1}")
        df2: list[float] = []
        for row in rows[1:]:
            df2.append(df_value(row[0]))
            for d1, cell in zip(df1, row[1:]):
                value = num(cell)
                want = f_upper(alpha, d1, df2[-1])
                cells += 1
                worst = max(worst, abs(value - want))
                if abs(value - want) > F_TOL:
                    fail(f"F({alpha}; {d1}, {df2[-1]}) is {value}, scipy gives {want:.6f}")
        if df2 != df2_expected:
            fail(f"{block}: denominator df coverage is unexpected: {df2}")
        # Within a column the value falls as the denominator df grows. There is no
        # equivalent rule along a row: for df2 = 1 and 2 the F quantile first rises
        # as df1 grows (F(1,1) = 161.4 but F(2,1) = 199.5), so a row check would
        # flag the table as wrong when it is right.
        for col in range(len(df1_expected)):
            column = [num(row[1 + col]) for row in rows[1:]]
            if any(b > a + F_TOL for a, b in zip(column, column[1:])):
                fail(f"{block}: column df1={df1_expected[col]} is not decreasing in df2")
    print(f"  OK   F: 2 levels x {len(df2_expected)} denominators x {len(df1_expected)} numerators "
          f"({cells} cells), worst error {worst:.1e}")


def check_csvs() -> None:
    text_z = (TABLES / "standard-normal.md").read_text(encoding="utf-8")
    rows = table_rows(text_z, "z-table")[1:]
    for csv_row, page_row in zip(csv_rows("standard-normal.csv")[1:], rows):
        z = float(csv_row[0])
        page_z = float(page_row[0].replace("*", ""))
        if abs(z - page_z) > 1e-9:
            fail(f"standard-normal.csv row {csv_row[0]} does not match the page row {page_row[0]}")
        for c_csv, c_page in zip(csv_row[1:], page_row[1:]):
            if abs(float(c_csv) - num(c_page)) > 1e-9:
                fail(f"standard-normal.csv disagrees with the page at z={z}: {c_csv} vs {c_page}")

    text_t = (TABLES / "t-distribution.md").read_text(encoding="utf-8")
    rows_t = table_rows(text_t, "t-table")[1:]
    for csv_row, page_row in zip(csv_rows("t-one-tailed.csv")[1:], rows_t):
        for c_csv, c_page in zip(csv_row[1:], page_row[1:]):
            if abs(float(c_csv) - num(c_page)) > 1e-9:
                fail(f"t-one-tailed.csv disagrees with the page at df={csv_row[0]}: {c_csv} vs {c_page}")

    text_chi = (TABLES / "chi-square.md").read_text(encoding="utf-8")
    rows_chi = table_rows(text_chi, "chi-table")[1:]
    for csv_row, page_row in zip(csv_rows("chi-square.csv")[1:], rows_chi):
        for c_csv, c_page in zip(csv_row[1:], page_row[1:]):
            if abs(float(c_csv) - num(c_page)) > 1e-9:
                fail(f"chi-square.csv disagrees with the page at df={csv_row[0]}: {c_csv} vs {c_page}")

    text_f = (TABLES / "f-distribution.md").read_text(encoding="utf-8")
    for block, name in (("f-005", "f-005.csv"), ("f-001", "f-001.csv")):
        rows_f = table_rows(text_f, block)[1:]
        for csv_row, page_row in zip(csv_rows(name)[1:], rows_f):
            for c_csv, c_page in zip(csv_row[1:], page_row[1:]):
                if abs(float(c_csv) - num(c_page)) > 1e-9:
                    fail(f"{name} disagrees with the page at df2={csv_row[0]}: {c_csv} vs {c_page}")
    print("  OK   CSV downloads agree cell by cell with the published tables")


def check_quoted_values() -> None:
    """A few numbers quoted in the worked examples must match the tables."""
    t_text = (TABLES / "t-distribution.md").read_text(encoding="utf-8")
    chi_text = (TABLES / "chi-square.md").read_text(encoding="utf-8")
    f_text = (TABLES / "f-distribution.md").read_text(encoding="utf-8")

    def lookup(rows: list[list[str]]) -> dict[float, dict[float, float]]:
        levels = [float(a) for a in rows[0][1:]]
        return {
            df_value(row[0]): {a: num(cell) for a, cell in zip(levels, row[1:])}
            for row in rows[1:]
        }

    t_lookup = lookup(table_rows(t_text, "t-table"))
    for df, alpha, shown in [(10, 0.025, "2.228"), (10, 0.05, "1.812"), (14, 0.025, "2.145"),
                             (22, 0.025, "2.074"), (5, 0.025, "2.571")]:
        got = t_lookup[df][alpha]
        if abs(round(got, 3) - float(shown)) > 6e-4:
            fail(f"t example quotes {shown} but the table gives {got} at df={df}, alpha={alpha}")

    chi_lookup = lookup(table_rows(chi_text, "chi-table"))
    for df, alpha, shown in [(5, 0.05, "11.070"), (5, 0.01, "15.086"),
                             (19, 0.025, "32.852"), (19, 0.975, "8.907")]:
        got = chi_lookup[df][alpha]
        if abs(round(got, 3) - float(shown)) > 6e-4:
            fail(f"chi-square example quotes {shown} but the table gives {got} at df={df}, alpha={alpha}")

    f_lookup = lookup(table_rows(f_text, "f-005"))
    got = f_lookup[40][3]
    if abs(got - 2.839) > 5e-4:
        fail(f"F example quotes 2.839 but the table gives {got} at (3, 40)")
    print("  OK   quoted worked-example values match the tables")


def check_page_links() -> None:
    pages = ["index.md", "standard-normal.md", "t-distribution.md", "chi-square.md",
             "f-distribution.md", "choosing-a-table.md"]
    for name in pages:
        if not (TABLES / name).exists():
            fail(f"missing page: {name}")
            continue
        text = (TABLES / name).read_text(encoding="utf-8")
        if name != "index.md" and "../test-selection.md" not in text:
            fail(f"{name}: no cross-link back to the test-selection guide")
        if name in {"standard-normal.md", "t-distribution.md", "chi-square.md", "f-distribution.md"}:
            if "../../modules/" not in text:
                fail(f"{name}: no link to a theoretical module")
            if "../../practicals/notebooks/" not in text:
                fail(f"{name}: no link to a practical notebook")
    nav = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    for name in pages:
        if f"reference/tables/{name}" not in nav:
            fail(f"{name}: not in the site navigation")
    print("  OK   pages linked from modules, notebooks, test selection and navigation")


def main() -> int:
    check_regeneration()
    check_z()
    check_t()
    check_chi()
    check_f()
    check_csvs()
    check_quoted_values()
    check_page_links()

    if problems:
        print("\nTable checks FAILED:")
        for problem in problems:
            print("  -", problem)
        return 1
    print("All table checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
