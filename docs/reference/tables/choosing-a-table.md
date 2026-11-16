---
title: Choosing a table — from question to critical value
description: A student-facing guide to picking the right statistical table, finding its degrees of freedom, reading the correct tail, and turning the comparison into a defensible conclusion, with four worked examples.
---

# Choosing a table

There are four tables in this section and exactly one question that decides between
them: **what is the test statistic built from?** Answer that and the table follows.
Everything else — the level, the direction, the conclusion — is a small number of
mechanical steps that this page spells out.

If you have not yet decided *which test* to run, start with
[choosing a statistical test](../test-selection.md) and come back here with the
test in hand.

## The decision path

| Your statistic is… | Table | Degrees of freedom |
|---|---|---|
| a standardised mean or proportion using a **known** \(\sigma\), or any normal probability | [standard normal](standard-normal.md) | none |
| a standardised mean using an **estimated** \(s\) | [Student's \(t\)](t-distribution.md) | \(n-1\), pairs \(-1\), \(n_1+n_2-2\), or Welch |
| a sum of squared standardised deviations (counts, variance) | [chi-square](chi-square.md) | \(k-1-m\), \((r-1)(c-1)\), or \(n-1\) |
| a **ratio** of two variance estimates | [\(F\)](f-distribution.md) | \((\nu_1,\nu_2)\): numerator then denominator |

Two traps sit inside that table. First, a test of two **proportions** is a \(z\)
test even though the data are counts — the statistic is a standardised difference of
means of 0/1 variables. Second, a chi-square test of **variance** exists, but a
comparison of two variances is an \(F\) test; chi-square cannot compare, it can only
describe one variance against a hypothesised value.

## 1. Standard normal

**When to use it.** A \(z\)-test or \(z\)-interval for a mean with known \(\sigma\); a
large-sample test or interval for one or two proportions; any probability question
about normally distributed data; the normal approximation to the binomial.

**Required information.** The statistic (or the raw mean, \(\sigma\) and \(n\)), the
significance level, and whether the test is one- or two-sided.

**Assumptions.** Independent observations. For means: normality of the population or
a large enough \(n\) for the CLT. For proportions: \(n\hat p\ge5\) and
\(n(1-\hat p)\ge5\).

**Degrees of freedom.** None. That is what makes the table one page.

**Finding the critical value.** Two-sided at \(\alpha\): find \(z\) with upper tail
\(\alpha/2\) — \(1.960\) at 5 %, \(2.576\) at 1 %. One-sided at \(\alpha\): \(1.645\),
\(2.326\).

**Comparing.** Reject when \(\lvert z\rvert>z_{\alpha/2}\) (two-sided) or
\(z>z_\alpha\) in the direction of \(H_1\) (one-sided). Squaring is not needed and
not valid for a one-sided test.

**Conclusion.** "The sample mean differs from 25.0 mm by more than sampling error
would explain (\(z=-2.20\), two-sided \(p=0.028\)); the estimated shortfall is
0.22 mm, 95 % CI 0.02 to 0.42." State the direction and the size, not only the
verdict.

## 2. Student's \(t\)

**When to use it.** Any test or interval for a mean, a mean difference, a slope or a
correlation where the standard deviation is **estimated from the sample**: one-sample,
paired, two-sample (pooled or Welch), regression coefficients, and the correlation
test.

**Required information.** The statistic, the df, the level and the direction.

**Assumptions.** Independence; approximate normality of the data (or of the
differences, or of the residuals). Equal variances only for the pooled two-sample
version — Welch drops it. With \(n\gtrsim30\) and mild skew, the CLT covers the
normality requirement for means.

**Degrees of freedom.** \(n-1\) for one sample; number of pairs \(-1\) for paired
data; \(n_1+n_2-2\) for pooled two samples; Welch–Satterthwaite (round **down**) for
Welch; \(n-2\) for a slope or a correlation.

**Finding the critical value.** Two-sided at \(\alpha\): the column headed
\(\alpha/2\) — 0.025 for 5 %. One-sided: the column headed \(\alpha\). At
\(\nu=\infty\) the row equals the normal values.

**Comparing.** \(\lvert t\rvert>t_{\alpha/2,\nu}\) for two-sided;
\(t>t_{\alpha,\nu}\) in the direction of \(H_1\) for one-sided.

**Conclusion.** Report the estimate, its interval, the statistic, the df and the
\(p\)-value. "Mean waiting time is 1.5 minutes longer under design B (95 % CI −0.7 to
3.7; \(t_{22}=1.41\), \(p=0.17\)): the study is inconclusive, and the interval is
wide enough to contain differences of practical importance in both directions."

## 3. Chi-square

**When to use it.** Goodness of fit of observed counts to a claimed distribution;
independence or homogeneity in a contingency table; an interval or test for a single
variance under normality.

**Required information.** Observed and expected counts (or \(s^2\), \(n\) and
\(\sigma_0^2\)), the df, the level.

**Assumptions.** Independent observations; expected counts of at least about 5 in
each cell (otherwise exact tests or merged categories); for the variance version,
normal data — the most fragile assumption in the course.

**Degrees of freedom.** \(k-1-m\) for goodness of fit (\(m\) parameters estimated);
\((r-1)(c-1)\) for independence or homogeneity; \(n-1\) for a variance.

**Finding the critical value.** Always the upper tail: the column headed \(\alpha\)
(5 % → 11.070 on 5 df). For a variance interval only, the \(97.5\) % column supplies
the denominator of the upper limit.

**Comparing.** Reject when \(X^2>\chi^2_{\alpha,\nu}\). Never test the lower tail
unless you are asking whether the data are *too good* to be true.

**Conclusion.** Report \(X^2\), df, \(p\), the effect size (Cramér's \(V\) or the
standardised residuals) and what the design cannot rule out. "Satisfaction and
region are associated (\(X^2=14.2\), df = 6, \(p=0.027\), Cramér's \(V=0.17\)): a
weak but detectable association, and the survey cannot separate region from the age
composition of the regions."

## 4. \(F\)

**When to use it.** One-way or multi-way ANOVA; comparing two variances; comparing
nested regression models; any test whose statistic is a ratio of mean squares.

**Required information.** The \(F\) statistic, \(\nu_1\) (numerator), \(\nu_2\)
(denominator), the level.

**Assumptions.** Independence; normal residuals; equal variances (for the pooled
version); for nested models, correct specification of the larger model.

**Degrees of freedom.** \(\nu_1=k-1\), \(\nu_2=N-k\) for one-way ANOVA;
\((n_1-1,\,n_2-1)\) for a variance ratio; extra parameters and residual df for nested
models. Numerator first in the notation \(F_{\nu_1,\nu_2}\).

**Finding the critical value.** Row \(\nu_2\), column \(\nu_1\), in the 5 % or 1 %
table. For a two-sided variance test read the \(2.5\) % column; for the lower
boundary use \(1/F_{\alpha,\nu_2,\nu_1}\).

**Comparing.** Reject when \(F>F_{\alpha,\nu_1,\nu_2}\). Order matters: the same two
df swapped give a different quantile.

**Conclusion.** Report \(F\), both df, \(p\), \(\eta^2\), the group means with
intervals, and the post-hoc comparison that identifies *where* the difference is.
"Methods differ (\(F_{3,44}=7.53\), \(p<0.001\), \(\eta^2=0.34\)); Tukey shows method
C above A and B by 4.1 and 3.6 marks, and C is not distinguishable from D."

## Four worked examples, end to end

### A \(z\)-test with known \(\sigma\)

Bags are filled to a mean of 500 g with \(\sigma=6\) g. A sample of 25 has mean
497 g. Test at 5 %, two-sided.

1. \(H_0:\mu=500\), \(H_1:\mu\ne500\), \(\alpha=0.05\).
2. \(z=(497-500)/(6/\sqrt{25})=-3/1.2=-2.50\).
3. Boundary \(z_{0.025}=1.960\); \(\lvert -2.50\rvert>1.96\).
4. Reject; exact \(p=2\Phi(-2.50)=0.0124\). The machine is under-filling by about
   3 g, 95 % CI 0.65 to 5.35 g. That is a specification problem, not just a
   statistical one.

### A one-sample \(t\)-test with estimated \(s\)

The same 25 bags, but \(\sigma\) unknown and \(s=6.4\). Then
\(t=-3/(6.4/5)=-2.34\) on 24 df. The boundary is \(t_{0.025,24}=2.064\), so reject
again, with \(p=0.028\) — larger than the \(z\) version, which is the cost of
estimating \(\sigma\). Note both the change in statistic and the change in
reference distribution; quoting \(z=-2.50\) and a \(t\) boundary would be a mixed
calculation.

### A chi-square test of independence

A 2×3 table (two interfaces × three satisfaction levels), 300 responses, gives
\(X^2=7.4\) on \((2-1)(3-1)=2\) df. The 5 % boundary is \(5.991\), so reject
(\(p=0.025\)). Cramér's \(V=\sqrt{7.4/300}=0.16\): a real but small association.
The report must say so, and must not translate "significant" into "the interfaces
are meaningfully different".

### A one-way ANOVA

Four suppliers, 11 orders each, \(F=3.42\). \(\nu_1=3\), \(\nu_2=40\); the 5 %
boundary is \(2.839\), so reject (\(p=0.026\)). With \(\eta^2=0.22\), supplier
explains about a fifth of the variation in delivery time. The follow-up is Tukey's
HSD: the omnibus test says "somewhere", the post-hoc says "supplier 4".

## The comparison, in one line each

| Table | Reject when | Typical sentence |
|---|---|---|
| Normal | \(\lvert z\rvert>z_{\alpha/2}\) | "\(z=-2.50\), \(p=0.012\)" |
| \(t\) | \(\lvert t\rvert>t_{\alpha/2,\nu}\) | "\(t_{24}=-2.34\), \(p=0.028\)" |
| Chi-square | \(X^2>\chi^2_{\alpha,\nu}\) | "\(X^2=7.40\), df 2, \(p=0.025\)" |
| \(F\) | \(F>F_{\alpha,\nu_1,\nu_2}\) | "\(F_{3,40}=3.42\), \(p=0.026\)" |

## Five errors that cost marks

| Error | What it looks like | Fix |
|---|---|---|
| wrong tail | using the 0.05 column for a two-sided 5 % test | two-sided means \(\alpha/2\) |
| wrong df | \(n\) instead of \(n-1\); \(N\) instead of \(N-k\) | count the constraints |
| transposed \(F\) | \(F_{44,3}\) instead of \(F_{3,44}\) | numerator = restrictions |
| table instead of \(p\) | "significant because 2.82 < 7.53" with no \(p\) or interval | report the \(p\)-value and the estimate |
| verdict without size | "significant" and nothing else | add the effect size and its interval |

## Related pages

- [Choosing a statistical test](../test-selection.md) — the test, before the table
- [Standard normal](standard-normal.md) · [Student's \(t\)](t-distribution.md) · [Chi-square](chi-square.md) · [\(F\)](f-distribution.md)
- Formulas: [foundations](../formula-sheet.md) and [inference](../formula-sheet-inference.md)
- Revision: [test comparison](../revision/tests.md), [common mistakes](../revision/mistakes.md)
