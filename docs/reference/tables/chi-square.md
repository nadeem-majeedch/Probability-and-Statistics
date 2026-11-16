---
title: Chi-square table — upper-tail critical values by degrees of freedom
description: Chi-square critical values from 1 to 100 degrees of freedom, with the degrees-of-freedom rules for goodness of fit, independence and variance intervals, and worked tests.
---

# Chi-square table

The chi-square statistic is a sum of squared standardised deviations,

\[ X^2=\sum_{i}\frac{(O_i-E_i)^2}{E_i}, \]

and for a correct model with independent observations it follows a
\(\chi^2_\nu\) distribution. The table prints the **upper-tail** critical value

\[ \chi^2_{\alpha,\nu} \quad\text{with}\quad P(\chi^2_\nu \ge \chi^2_{\alpha,\nu})=\alpha . \]

Only the upper tail appears in testing, because only large values of \(X^2\)
contradict the model. The lower tail appears once, in the variance interval, and is
obtained from the same table by reading \(2.5\) % instead of \(97.5\) %.

## The table

<!-- block:chi-table -->

<!-- table:begin -->

<div class="psds-table-scroll" markdown>

| df | 0.995 | 0.99 | 0.975 | 0.95 | 0.9 | 0.1 | 0.05 | 0.025 | 0.01 | 0.005 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **1** | 0.000 | 0.000 | 0.001 | 0.004 | 0.016 | 2.706 | 3.841 | 5.024 | 6.635 | 7.879 |
| **2** | 0.010 | 0.020 | 0.051 | 0.103 | 0.211 | 4.605 | 5.991 | 7.378 | 9.210 | 10.597 |
| **3** | 0.072 | 0.115 | 0.216 | 0.352 | 0.584 | 6.251 | 7.815 | 9.348 | 11.345 | 12.838 |
| **4** | 0.207 | 0.297 | 0.484 | 0.711 | 1.064 | 7.779 | 9.488 | 11.143 | 13.277 | 14.860 |
| **5** | 0.412 | 0.554 | 0.831 | 1.145 | 1.610 | 9.236 | 11.070 | 12.833 | 15.086 | 16.750 |
| **6** | 0.676 | 0.872 | 1.237 | 1.635 | 2.204 | 10.645 | 12.592 | 14.449 | 16.812 | 18.548 |
| **7** | 0.989 | 1.239 | 1.690 | 2.167 | 2.833 | 12.017 | 14.067 | 16.013 | 18.475 | 20.278 |
| **8** | 1.344 | 1.646 | 2.180 | 2.733 | 3.490 | 13.362 | 15.507 | 17.535 | 20.090 | 21.955 |
| **9** | 1.735 | 2.088 | 2.700 | 3.325 | 4.168 | 14.684 | 16.919 | 19.023 | 21.666 | 23.589 |
| **10** | 2.156 | 2.558 | 3.247 | 3.940 | 4.865 | 15.987 | 18.307 | 20.483 | 23.209 | 25.188 |
| **11** | 2.603 | 3.053 | 3.816 | 4.575 | 5.578 | 17.275 | 19.675 | 21.920 | 24.725 | 26.757 |
| **12** | 3.074 | 3.571 | 4.404 | 5.226 | 6.304 | 18.549 | 21.026 | 23.337 | 26.217 | 28.300 |
| **13** | 3.565 | 4.107 | 5.009 | 5.892 | 7.042 | 19.812 | 22.362 | 24.736 | 27.688 | 29.819 |
| **14** | 4.075 | 4.660 | 5.629 | 6.571 | 7.790 | 21.064 | 23.685 | 26.119 | 29.141 | 31.319 |
| **15** | 4.601 | 5.229 | 6.262 | 7.261 | 8.547 | 22.307 | 24.996 | 27.488 | 30.578 | 32.801 |
| **16** | 5.142 | 5.812 | 6.908 | 7.962 | 9.312 | 23.542 | 26.296 | 28.845 | 32.000 | 34.267 |
| **17** | 5.697 | 6.408 | 7.564 | 8.672 | 10.085 | 24.769 | 27.587 | 30.191 | 33.409 | 35.718 |
| **18** | 6.265 | 7.015 | 8.231 | 9.390 | 10.865 | 25.989 | 28.869 | 31.526 | 34.805 | 37.156 |
| **19** | 6.844 | 7.633 | 8.907 | 10.117 | 11.651 | 27.204 | 30.144 | 32.852 | 36.191 | 38.582 |
| **20** | 7.434 | 8.260 | 9.591 | 10.851 | 12.443 | 28.412 | 31.410 | 34.170 | 37.566 | 39.997 |
| **21** | 8.034 | 8.897 | 10.283 | 11.591 | 13.240 | 29.615 | 32.671 | 35.479 | 38.932 | 41.401 |
| **22** | 8.643 | 9.542 | 10.982 | 12.338 | 14.041 | 30.813 | 33.924 | 36.781 | 40.289 | 42.796 |
| **23** | 9.260 | 10.196 | 11.689 | 13.091 | 14.848 | 32.007 | 35.172 | 38.076 | 41.638 | 44.181 |
| **24** | 9.886 | 10.856 | 12.401 | 13.848 | 15.659 | 33.196 | 36.415 | 39.364 | 42.980 | 45.559 |
| **25** | 10.520 | 11.524 | 13.120 | 14.611 | 16.473 | 34.382 | 37.652 | 40.646 | 44.314 | 46.928 |
| **26** | 11.160 | 12.198 | 13.844 | 15.379 | 17.292 | 35.563 | 38.885 | 41.923 | 45.642 | 48.290 |
| **27** | 11.808 | 12.879 | 14.573 | 16.151 | 18.114 | 36.741 | 40.113 | 43.195 | 46.963 | 49.645 |
| **28** | 12.461 | 13.565 | 15.308 | 16.928 | 18.939 | 37.916 | 41.337 | 44.461 | 48.278 | 50.993 |
| **29** | 13.121 | 14.256 | 16.047 | 17.708 | 19.768 | 39.087 | 42.557 | 45.722 | 49.588 | 52.336 |
| **30** | 13.787 | 14.953 | 16.791 | 18.493 | 20.599 | 40.256 | 43.773 | 46.979 | 50.892 | 53.672 |
| **40** | 20.707 | 22.164 | 24.433 | 26.509 | 29.051 | 51.805 | 55.758 | 59.342 | 63.691 | 66.766 |
| **50** | 27.991 | 29.707 | 32.357 | 34.764 | 37.689 | 63.167 | 67.505 | 71.420 | 76.154 | 79.490 |
| **60** | 35.534 | 37.485 | 40.482 | 43.188 | 46.459 | 74.397 | 79.082 | 83.298 | 88.379 | 91.952 |
| **80** | 51.172 | 53.540 | 57.153 | 60.391 | 64.278 | 96.578 | 101.879 | 106.629 | 112.329 | 116.321 |
| **100** | 67.328 | 70.065 | 74.222 | 77.929 | 82.358 | 118.498 | 124.342 | 129.561 | 135.807 | 140.169 |

</div>

<!-- table:end -->

<!-- /block:chi-table -->

Every column heading is an **upper-tail** area, so column `0.025` holds the value
with 2.5 % of the distribution above it — the 97.5th percentile — and column `0.975`
holds the value with 97.5 % above it, that is the 2.5th percentile. The left-hand
columns (0.995 to 0.90) are therefore the small values, the right-hand columns the
large ones. Chi-square is skewed to the right, so the two halves do not mirror: on
19 df the entries are 8.907 and 32.852, not \(\nu\pm\) something.

Beyond 100 df the distribution is close to normal with mean \(\nu\) and variance
\(2\nu\), but do not use that shortcut for a decision; use software.

## Choosing the degrees of freedom

| Procedure | Statistic | Degrees of freedom | Notes |
|---|---|---|---|
| Goodness of fit | \(\sum (O-E)^2/E\) over \(k\) categories | \(k-1-m\) | \(m\) = number of parameters estimated from the data |
| Independence | contingency table \(r\times c\) | \((r-1)(c-1)\) | total count fixed, row and column totals fixed |
| Homogeneity | several samples, one categorical variable | \((r-1)(c-1)\) | same arithmetic, different sampling design |
| Variance interval or test | \((n-1)s^2/\sigma_0^2\) | \(n-1\) | requires normal data |
| Variance ratio | — | use the [\(F\) table](f-distribution.md) | chi-square cannot compare two variances |
| McNemar, 2×2 paired | — | use the binomial or a corrected test | not this table |

**Goodness of fit example of the rule.** Test whether a die is fair with six
observed counts: \(k=6\), no parameter estimated from the data, so \(\nu=5\). If you
fitted a Poisson and estimated \(\lambda\) from the same counts, you would lose one
more: \(\nu=k-2\).

**Independence example of the rule.** A table of three regions by four product
categories has \((3-1)(4-1)=6\) df. A 2×2 table has 1 df, which is why small
counts hurt so much there: with one degree of freedom the statistic cannot
average away noise.

**A trap.** Merging categories to raise expected counts reduces \(k\) and therefore
reduces the degrees of freedom. That is legitimate, but the table you then use has
fewer df, and the critical value falls — so a merged test can be either more or
less significant. Report what you merged.

## Goodness of fit: worked example

A die is rolled 120 times, with counts \(25, 24, 26, 12, 18, 15\). Under fairness
each expected count is 20.

\[ X^2=\frac{(25-20)^2+(24-20)^2+(26-20)^2+(12-20)^2+(18-20)^2+(15-20)^2}{20}
=\frac{25+16+36+64+4+25}{20}=8.50 . \]

With \(\nu=6-1=5\), the 5 % boundary is \(11.070\) and the 1 % boundary is
\(15.086\). Since \(8.50<11.070\), the data do not provide evidence that the die
is biased at 5 %. The exact \(p\)-value is \(0.131\) — weak evidence at best, and
certainly not proof of fairness. That distinction is the point of the exercise: a
large \(p\)-value says the data are *compatible* with fairness, not that fairness is
established.

Every expected count here is 20, comfortably above the usual rule of thumb of 5.
Below that, the chi-square reference distribution is inaccurate and an exact test
should replace it.

## Independence: worked example

A survey cross-tabulates three regions against four satisfaction levels, 480
responses, giving \(X^2=14.2\) on \((3-1)(4-1)=6\) df. The 5 % boundary is
\(12.592\), so \(14.2>12.592\): reject independence at 5 %. The exact \(p\)-value is
\(0.027\).

That is a statement about association, not about its size or its cause. Report a
measure of association (Cramér's \(V\), or the largest standardised residual) and
say what the design cannot rule out — here, that regions differ in age structure,
which may be the real driver.

## Variance inference

For normal data, \((n-1)s^2/\sigma^2\sim\chi^2_{n-1}\), which inverts into the
interval

\[ \left(\frac{(n-1)s^2}{c_{0.025,\,n-1}},\ \frac{(n-1)s^2}{c_{0.975,\,n-1}}\right), \]

where \(c_{a,\nu}\) is the entry in column \(a\) of the table above (the value with
\(a\) of the distribution above it). The 2.5 % entry gives the **lower** limit and
the 97.5 % entry gives the **upper** limit, because dividing by a larger number
makes the bound smaller.

Twenty observations with \(s^2=4\) give \((n-1)s^2=76\), \(c_{0.025,19}=32.852\) and
\(c_{0.975,19}=8.907\):

\[ \left(\frac{76}{32.852},\ \frac{76}{8.907}\right)=(2.31,\ 8.53), \]

so \(\sigma\) is between \(1.52\) and \(2.92\). The interval is uselessly wide, and
that is the honest lesson: with \(n=20\), a variance is barely estimated. The
assumption of normality is also doing heavy lifting — for skewed data this interval
can be badly wrong, which is why process capability studies insist on checking
normality first.

## Reading the conclusion

1. Compute \(X^2\) from the counts, not from proportions.
2. Compare with the boundary on the correct df and tail.
3. If \(X^2\) exceeds the boundary, the model or the independence assumption is
   rejected; if not, the data are compatible with it.
4. Report the statistic, the df, the \(p\)-value, the effect size and the
   assumption check on expected counts.

## Self-check

1. Give \(\chi^2_{0.05,5}\), \(\chi^2_{0.01,5}\) and \(\chi^2_{0.05,10}\).
2. A 5×3 table: how many df?
3. A goodness-of-fit test on 8 categories with a Poisson parameter estimated from
   the data: how many df?
4. Why does a variance interval use two different chi-square columns?
5. \(X^2=4.5\) on 5 df — significant at 5 %?

**Answers.** (1) 11.070, 15.086, 18.307. (2) \((5-1)(3-1)=8\). (3) \(8-1-1=6\).
(4) Because the interval is built from a two-tailed probability statement: the
lower limit divides by the 2.5 % entry (32.852) and the upper limit by the 97.5 %
entry (8.907). Using one column would give a one-sided bound.
(5) No: \(4.5<11.070\), \(p=0.48\).

## Related pages

- Module: [M17 · ANOVA, chi-square and nonparametric](../../modules/17-anova-chi-square-nonparametric/chapter.md)
- Laboratory: [L-14 · ANOVA and multiple groups](../../labs/anova.md) (the \(F\) side of the same chapter)
- Notebook: [17 · ANOVA and chi-square](../../practicals/notebooks/17-anova-chi-square-nonparametric.ipynb)
- Formulas: [inference formula sheet](../formula-sheet-inference.md), sections on chi-square and variance
- Previous table: [Student's \(t\)](t-distribution.md) · Next: [\(F\) distribution](f-distribution.md)

- Guides: [choosing a table](choosing-a-table.md) and [choosing a statistical test](../test-selection.md).
