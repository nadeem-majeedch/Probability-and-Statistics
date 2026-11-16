---
title: Student's t table — one-tailed and two-tailed critical values
description: The full t table by degrees of freedom, one-tailed and two-tailed levels, confidence-interval multipliers, one-sample and two-sample tests, and when the t distribution is required instead of the normal.
---

# Student's \(t\) table

The \(t\) distribution is the sampling distribution of

\[ t=\frac{\bar{x}-\mu}{s/\sqrt{n}}, \]

that is, of a standardised mean when the population standard deviation \(\sigma\) is
replaced by the sample standard deviation \(s\). That substitution costs
information — one degree of freedom — and the price is a heavier tail. The table
below prints the **upper-tail** critical value \(t_{\alpha,\nu}\), defined by

\[ P(T_\nu \ge t_{\alpha,\nu}) = \alpha . \]

## How the columns are labelled

Column headings are **one-tailed** levels. For a two-tailed test at level
\(\alpha\), read the column headed \(\alpha/2\):

<!-- block:t-two-tail -->

<!-- table:begin -->

<div class="psds-table-scroll" markdown>

| one-tailed &alpha; | 0.1 | 0.05 | 0.025 | 0.01 | 0.005 |
|---:|---:|---:|---:|---:|---:|
| two-tailed &alpha; | 0.2 | 0.1 | 0.05 | 0.02 | 0.01 |

</div>

<!-- table:end -->

<!-- /block:t-two-tail -->

So a two-tailed test at 5 % uses the column headed `0.025`; a one-tailed test at
5 % uses the column headed `0.05`. Same data, different boundary, and the
difference is not small at small \(\nu\): on 10 df the two boundaries are 2.228 and
1.812.

## The table

<!-- block:t-table -->

<!-- table:begin -->

<div class="psds-table-scroll" markdown>

| df | 0.1 | 0.05 | 0.025 | 0.01 | 0.005 |
|---:|---:|---:|---:|---:|---:|
| **1** | 3.0777 | 6.3138 | 12.7062 | 31.8205 | 63.6567 |
| **2** | 1.8856 | 2.9200 | 4.3027 | 6.9646 | 9.9248 |
| **3** | 1.6377 | 2.3534 | 3.1824 | 4.5407 | 5.8409 |
| **4** | 1.5332 | 2.1318 | 2.7764 | 3.7469 | 4.6041 |
| **5** | 1.4759 | 2.0150 | 2.5706 | 3.3649 | 4.0321 |
| **6** | 1.4398 | 1.9432 | 2.4469 | 3.1427 | 3.7074 |
| **7** | 1.4149 | 1.8946 | 2.3646 | 2.9980 | 3.4995 |
| **8** | 1.3968 | 1.8595 | 2.3060 | 2.8965 | 3.3554 |
| **9** | 1.3830 | 1.8331 | 2.2622 | 2.8214 | 3.2498 |
| **10** | 1.3722 | 1.8125 | 2.2281 | 2.7638 | 3.1693 |
| **11** | 1.3634 | 1.7959 | 2.2010 | 2.7181 | 3.1058 |
| **12** | 1.3562 | 1.7823 | 2.1788 | 2.6810 | 3.0545 |
| **13** | 1.3502 | 1.7709 | 2.1604 | 2.6503 | 3.0123 |
| **14** | 1.3450 | 1.7613 | 2.1448 | 2.6245 | 2.9768 |
| **15** | 1.3406 | 1.7531 | 2.1314 | 2.6025 | 2.9467 |
| **16** | 1.3368 | 1.7459 | 2.1199 | 2.5835 | 2.9208 |
| **17** | 1.3334 | 1.7396 | 2.1098 | 2.5669 | 2.8982 |
| **18** | 1.3304 | 1.7341 | 2.1009 | 2.5524 | 2.8784 |
| **19** | 1.3277 | 1.7291 | 2.0930 | 2.5395 | 2.8609 |
| **20** | 1.3253 | 1.7247 | 2.0860 | 2.5280 | 2.8453 |
| **21** | 1.3232 | 1.7207 | 2.0796 | 2.5176 | 2.8314 |
| **22** | 1.3212 | 1.7171 | 2.0739 | 2.5083 | 2.8188 |
| **23** | 1.3195 | 1.7139 | 2.0687 | 2.4999 | 2.8073 |
| **24** | 1.3178 | 1.7109 | 2.0639 | 2.4922 | 2.7969 |
| **25** | 1.3163 | 1.7081 | 2.0595 | 2.4851 | 2.7874 |
| **26** | 1.3150 | 1.7056 | 2.0555 | 2.4786 | 2.7787 |
| **27** | 1.3137 | 1.7033 | 2.0518 | 2.4727 | 2.7707 |
| **28** | 1.3125 | 1.7011 | 2.0484 | 2.4671 | 2.7633 |
| **29** | 1.3114 | 1.6991 | 2.0452 | 2.4620 | 2.7564 |
| **30** | 1.3104 | 1.6973 | 2.0423 | 2.4573 | 2.7500 |
| **40** | 1.3031 | 1.6839 | 2.0211 | 2.4233 | 2.7045 |
| **50** | 1.2987 | 1.6759 | 2.0086 | 2.4033 | 2.6778 |
| **60** | 1.2958 | 1.6706 | 2.0003 | 2.3901 | 2.6603 |
| **80** | 1.2922 | 1.6641 | 1.9901 | 2.3739 | 2.6387 |
| **100** | 1.2901 | 1.6602 | 1.9840 | 2.3642 | 2.6259 |
| **120** | 1.2886 | 1.6577 | 1.9799 | 2.3578 | 2.6174 |
| **&infin;** | 1.2816 | 1.6449 | 1.9600 | 2.3263 | 2.5758 |

</div>

<!-- table:end -->

<!-- /block:t-table -->

Rows beyond 30 are given at 40, 50, 60, 80, 100 and 120; interpolate between them
only if you must, and never for a decision near the boundary. At \(\nu=\infty\) the
row is the standard normal value, which is why 1.960 appears there.

## When to use \(t\) rather than \(z\)

| Situation | Use | Why |
|---|---|---|
| \(\sigma\) known, any \(n\) | \(z\) | the standardisation has no estimated quantity |
| \(\sigma\) unknown, \(n\) large | either; \(t\) is safer | the rows converge: \(t_{0.025,120}=1.980\) vs \(z=1.960\) |
| \(\sigma\) unknown, \(n\) small | \(t\) | the extra tail is the whole point; \(t_{0.025,5}=2.571\) |
| proportion, large \(n\) | \(z\) | the estimated variance enters differently, and the interval is wider than the naive \(z\) formula |
| variance or ratio of variances | chi-square, \(F\) | the statistic is not a standardised mean |

The honest rule: **if you computed \(s\), use \(t\).** The \(z\) approximation
understates uncertainty exactly when the sample is small enough for that to matter.
The one legitimate exception is the large-sample proportion test, where the
standard error is computed from the same data by construction and the \(z\)
reference is the conventional one.

## Confidence intervals

A \(100(1-\alpha)\) % interval for a mean with unknown \(\sigma\) is

\[ \bar{x} \pm t_{\alpha/2,\,n-1}\,\frac{s}{\sqrt{n}}, \]

so the table entry you need is the **two-tailed** one, on \(n-1\) df. The same
multiplier appears in a prediction interval (with an extra 1 under the square root)
and in the half-width of a regression slope interval (with the slope's standard
error).

**Worked example.** Fifteen measurements give \(\bar{x}=12.4\) and \(s=3.1\).

\[ SE=\frac{3.1}{\sqrt{15}}=0.8004,\qquad t_{0.025,14}=2.145, \]

\[ 12.4 \pm 2.145(0.8004) = 12.4\pm1.717 = (10.68,\ 14.12). \]

Had you used 1.96 the interval would be \((10.83, 13.97)\) — narrower, and
claiming precision the data do not support.

## One-sample test

Same data, \(H_0:\mu=12\) against a two-sided alternative:

\[ t=\frac{12.4-12}{0.8004}=0.50,\qquad \nu=14,\qquad t_{0.025,14}=2.145 . \]

\(\lvert 0.50\rvert<2.145\), so the sample does not provide evidence against
\(\mu=12\). The exact two-sided \(p\)-value is \(0.625\). Note the shape of the
conclusion: "not enough evidence", not "the mean is 12".

## Two-sample test

Two independent groups of 12, means \(12.4\) and \(10.9\), pooled standard
deviation \(2.6\). The pooled standard error is

\[ SE = s_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}} = 2.6\sqrt{\tfrac{2}{12}} = 1.061, \]

\[ t=\frac{12.4-10.9}{1.061}=1.41,\qquad \nu = n_1+n_2-2 = 22, \qquad t_{0.025,22}=2.074 . \]

\(1.41<2.074\), so no rejection at 5 %; the exact \(p\)-value is \(0.172\). With
Welch's correction the degrees of freedom become fractional — here 21.7, rounded
**down** to 21 for the table, which uses a slightly larger critical value and is
therefore the conservative choice. Welch is the default in this course because it
does not assume equal variances.

The pairing rule matters more than the arithmetic: paired observations are
analysed as the one-sample test on their differences, with \(n-1\) degrees of
freedom where \(n\) is the number of **pairs**, not the number of measurements.

## Other places the table appears

| Application | Degrees of freedom | Column |
|---|---|---|
| one-sample mean | \(n-1\) | two-tailed \(\alpha/2\) |
| paired mean difference | pairs \(-1\) | two-tailed \(\alpha/2\) |
| two-sample pooled | \(n_1+n_2-2\) | two-tailed \(\alpha/2\) |
| Welch | Welch–Satterthwaite, rounded down | two-tailed \(\alpha/2\) |
| regression slope | \(n-2\) | two-tailed \(\alpha/2\) |
| correlation \(r\) | \(n-2\) | two-tailed \(\alpha/2\) |
| difference of two proportions | large-sample \(z\) | — |

**Worked slope example.** A regression on 30 observations gives slope
\(\hat\beta_1=2.4\) with standard error \(0.8\). Then \(t=3.00\) on 28 df against
\(t_{0.025,28}=2.048\): reject \(H_0:\beta_1=0\). Report the slope with its interval,
\(2.4\pm2.048(0.8)=(0.76,4.04)\), and the units — marks per hour, not "significant".

## Reading the table on a phone

The \(t\) table is six columns wide, so it fits a phone in portrait with a small
font. If it does not, the table scrolls inside its frame; the page does not move.

## Self-check

1. Give \(t_{0.025,10}\), \(t_{0.05,10}\), \(t_{0.025,30}\) and \(t_{0.005,14}\).
2. Why is \(t_{0.025,1}=12.706\) so large?
3. A 95 % interval from \(n=9\) uses which entry?
4. A one-tailed test at 1 % on 20 df: which boundary, and what would it be
   two-tailed?
5. Two groups of 15 and 18 with equal variances: what df does the pooled test use?

**Answers.** (1) 2.228, 1.812, 2.042, 2.977. (2) On one degree of freedom the
estimate of \(\sigma\) rests on a single deviation, so the tail is extremely heavy;
\(t_1\) is the Cauchy distribution. (3) \(t_{0.025,8}=2.306\). (4) One-tailed 1 % is
the `0.01` column: 2.528; two-tailed 1 % would be the `0.005` column: 2.845.
(5) \(15+18-2=31\).

## Related pages

- Modules: [M14 · Estimation and confidence intervals](../../modules/14-estimation-and-confidence-intervals/chapter.md), [M15 · Hypothesis testing](../../modules/15-hypothesis-testing/chapter.md)
- Laboratories: [L-09 · Interval coverage](../../labs/confidence-intervals.md), [L-10 · p-values](../../labs/p-values.md), [L-13 · Errors and power](../../labs/power-and-errors.md)
- Notebooks: [14 · Confidence intervals](../../practicals/notebooks/14-estimation-and-confidence-intervals.ipynb), [15 · Hypothesis testing](../../practicals/notebooks/15-hypothesis-testing.ipynb)
- Formulas: [inference formula sheet](../formula-sheet-inference.md), sections 16–17
- Previous table: [standard normal](standard-normal.md) · Next: [chi-square](chi-square.md)

- Guides: [choosing a table](choosing-a-table.md) and [choosing a statistical test](../test-selection.md).
