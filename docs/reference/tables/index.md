---
title: Statistical tables and critical values
description: Generated standard normal, t, chi-square and F tables with the tail convention, a reading guide, printable and downloadable versions, and links to the modules that use them.
---

# Statistical tables and critical values

Four distributions decide almost every test in this course. Each has a page here
with the table you need, the convention it uses, a worked example and the module it
belongs to.

| Table | What it gives you | Typical use | Page |
|---|---|---|---|
| Standard normal | \(\Phi(z)\), the cumulative probability, for \(z\) from \(-3.4\) to \(3.4\) | \(z\)-tests, \(z\)-intervals, any normal probability | [Standard normal](standard-normal.md) |
| Student's \(t\) | upper-tail critical value \(t_{\alpha,\nu}\) for \(\nu=1,\dots,30,40,\dots,120,\infty\) | \(t\)-tests, \(t\)-intervals, regression slopes | [Student's \(t\)](t-distribution.md) |
| Chi-square | upper-tail critical values \(\chi^2_{\alpha,\nu}\) | goodness of fit, independence, variance intervals | [Chi-square](chi-square.md) |
| \(F\) | upper-tail values at the 5 % and 1 % levels, for every \((\nu_1,\nu_2)\) | one-way ANOVA, variance ratios, nested models | [\(F\) distribution](f-distribution.md) |

Not sure which one you need? [Choosing a table](choosing-a-table.md) takes you from
the question to the right table, the degrees of freedom, and the sentence that
reports the conclusion.

## Every number here is generated, not typed

The tables are produced by `tools/generate_tables.py`, which calls SciPy's quantile
functions and writes both the Markdown you see and the CSV files you can download.
No value in this section was copied from a textbook or typed by hand.

| What | How it is computed |
|---|---|
| \(\Phi(z)\) | `scipy.stats.norm.cdf(z)` |
| \(t_{\alpha,\nu}\) | `scipy.stats.t.ppf(1 - alpha, df)`, and `norm.ppf` at \(\nu=\infty\) |
| \(\chi^2_{\alpha,\nu}\) | `scipy.stats.chi2.isf(alpha, df)` |
| \(F_{\alpha,\nu_1,\nu_2}\) | `scipy.stats.f.isf(alpha, df1, df2)`; the \(\nu_2=\infty\) limit is \(\chi^2_{\alpha,\nu_1}/\nu_1\) |

`tools/check_tables.py` re-derives every printed cell from a second SciPy
formulation, checks that the downloads and the pages agree, and fails the build if a
single digit drifts.

## The one convention you must not get wrong

Every critical value in these pages is an **upper-tail** quantile: the table entry
\(c\) satisfies

\[ P(X \ge c) = \alpha \quad\text{so}\quad P(X \le c) = 1-\alpha . \]

The standard normal page is the exception, because students read a \(z\)-table
cumulatively: it prints \(\Phi(z) = P(Z \le z)\), and the upper tail is
\(1-\Phi(z)\).

A two-tailed test at level \(\alpha\) therefore reads the column headed
\(\alpha/2\) (0.025 for 5 %), while a one-tailed test reads the column headed
\(\alpha\). Reaching for the wrong column is the single most common table error; it
doubles or halves your evidence without changing your data.

## Rounding and precision

| Table | Decimals | Largest rounding error in a cell |
|---|---|---|
| \(\Phi(z)\) | 4 | \(5\times10^{-5}\) |
| \(t\) | 4 | \(5\times10^{-5}\) |
| Chi-square | 3 | \(5\times10^{-4}\) |
| \(F\) | 3 | \(5\times10^{-4}\) |

Values are computed in double precision and rounded to the printed place, so a
hand calculation that lands within a couple of units of the last digit of a
critical value is agreement, not error. When a test statistic falls within that
band of a critical value, report the \(p\)-value from software rather than a
verdict from the table.

## Download and print

Each table is available as a CSV for spreadsheets and scripts:

| File | Contents |
|---|---|
| [standard-normal.csv](../../data/tables/standard-normal.csv) | \(\Phi(z)\), \(z=-3.4\) to \(3.4\) by hundredths |
| [t-one-tailed.csv](../../data/tables/t-one-tailed.csv) | \(t_{\alpha,\nu}\) for one-tailed \(\alpha\) |
| [chi-square.csv](../../data/tables/chi-square.csv) | \(\chi^2_{\alpha,\nu}\), upper tail |
| [f-005.csv](../../data/tables/f-005.csv), [f-001.csv](../../data/tables/f-001.csv) | \(F\) at 5 % and 1 % |

Every table page prints on its own: press `Ctrl + P` (Windows/Linux) or `Cmd + P`
(macOS). The site's print stylesheet removes the navigation, the search bar and the
buttons, shrinks the table type, keeps each row unbroken across a page, and repeats
the column headers on every printed page. Choose **Landscape** for the \(F\) table,
which has nineteen numerator columns.

For an examination you are usually allowed one sheet: print the
[standard normal](standard-normal.md) and [\(t\)](t-distribution.md) pages and write
the four or five critical values you actually use on the same sheet. That is faster
than shuffling paper, and it forces you to notice which numbers your course really
relies on.

## Reading a table on a phone

The wide tables scroll sideways inside their own frame; the page itself never
scrolls sideways. If you are reading on a phone, turn it landscape for the \(F\)
table, or use the search box on the page to jump to a row: every row label is
text, so searching for `df 24` finds it.

## Where these tables are used

| Table | Module | Laboratory | Notebook |
|---|---|---|---|
| Standard normal | [M10 · Continuous distributions](../../modules/10-continuous-distributions/chapter.md) | [L-05 · Normal and z-scores](../../labs/normal-and-z-scores.md) | [10 · Continuous distributions](../../practicals/notebooks/10-continuous-distributions.ipynb) |
| Student's \(t\) | [M14 · Estimation and CIs](../../modules/14-estimation-and-confidence-intervals/chapter.md) | [L-09 · Interval coverage](../../labs/confidence-intervals.md) | [14 · Confidence intervals](../../practicals/notebooks/14-estimation-and-confidence-intervals.ipynb) |
| Chi-square | [M17 · ANOVA, chi-square, nonparametric](../../modules/17-anova-chi-square-nonparametric/chapter.md) | [L-14 · ANOVA](../../labs/anova.md) | [17 · ANOVA and chi-square](../../practicals/notebooks/17-anova-chi-square-nonparametric.ipynb) |
| \(F\) | [M17 · ANOVA, chi-square, nonparametric](../../modules/17-anova-chi-square-nonparametric/chapter.md) | [L-14 · ANOVA](../../labs/anova.md) | [17 · ANOVA and chi-square](../../practicals/notebooks/17-anova-chi-square-nonparametric.ipynb) |

The formulas behind each table are on the [inference formula sheet](../formula-sheet-inference.md);
the choice between tests is in [choosing a statistical test](../test-selection.md).

## A caution about crossing from table to conclusion

A table gives you a boundary. It does not give you a \(p\)-value, an effect size or a
decision about anything that matters. The sequence is always:

1. state the hypotheses and the level before looking at the data;
2. compute the statistic from the data;
3. compare it with the tabled boundary (or, better, read the exact \(p\)-value);
4. report the estimate and its interval, not just the verdict;
5. say what the result does not establish.

The tables make step 3 possible on paper. They add nothing to steps 1, 4 and 5,
which is where marks and mistakes actually live.
