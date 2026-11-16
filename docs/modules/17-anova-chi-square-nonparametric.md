---
title: "M17 — ANOVA, Chi-Square and Nonparametric Statistics"
description: Comparing several groups, testing categorical association, and what to do when distributional assumptions fail.
module: 17
part: 7
level: Advanced
hours: 16
prerequisites: [15, 16]
---

# M17 · ANOVA, Chi-Square and Nonparametric Statistics

<div class="psds-meta" markdown>
<span class="psds-chip psds-chip--advanced">Advanced</span>
<span class="psds-chip">Part VII · Comparative inference</span>
<span class="psds-chip">16 study hours</span>
<span class="psds-chip">Module 17 of 18</span>
</div>

## Introduction

Three questions dominate applied analysis: *do these groups differ?*, *are these two
categorical variables associated?*, and *what do I do when the assumptions fail?* This
module answers all three, and it answers them as one coherent story rather than three
unrelated procedures.

ANOVA is a variance decomposition: total variation splits into what the group
structure explains and what it leaves unexplained. Once seen that way, it is not a
separate technique but regression with a categorical predictor — which is literally
what the software does.

The chi-square family covers three procedures that students routinely confuse. The
arithmetic is identical; the *design* is not, and the design determines what the
conclusion means. A goodness-of-fit test asks whether a distribution matches a claim;
a test of independence asks whether two variables in one population are related; a test
of homogeneity asks whether one variable has the same distribution across several
populations.

Nonparametric methods are the honest answer to the question the earlier modules raise:
if the data cannot support a distributional assumption, what remains? Ranks, signs and
resampling — and the two resampling ideas introduced here, the permutation test and
the bootstrap, are the bridge from classical inference to modern computational
practice.

## Why this matters

These are the procedures most often run on real data, and the ones most often run
without their assumptions being checked.

- **ANOVA** is used whenever a metric is compared across more than two segments — and
  post-hoc comparisons are routinely omitted or done wrongly.
- **Chi-square** is used on every contingency table, frequently with expected counts
  far too small for the approximation.
- **Rank tests** are used as a safety net, sometimes when the parametric test was
  perfectly appropriate, and sometimes with the wrong interpretation ("Mann–Whitney
  tests medians" is false in general).

## Learning objectives

By the end of this module you can:

1. State the one-way ANOVA model and its assumptions, and identify the hypotheses it
   tests.
2. Decompose total sum of squares into between- and within-group components and derive
   the F statistic.
3. Show that F = t² when \(k=2\), and explain why ANOVA and the pooled t test agree.
4. Read an ANOVA table line by line.
5. Run Tukey post-hoc comparisons after a significant F and explain why uncorrected
   pairwise tests are invalid.
6. Report and interpret \(\eta^2\), \(\omega^2\) and Cohen's f.
7. Choose remedies for violated assumptions: Welch ANOVA, transformation, rank-based
   alternatives.
8. Analyse a two-way design, interpret main effects in the presence of interaction, and
   explain why main effects can mislead.
9. Conduct goodness-of-fit, independence and homogeneity tests, count degrees of
   freedom correctly, and state the expected-count condition.
10. Compute Cramér's V and the odds ratio as effect sizes; apply Fisher's exact and
    McNemar's tests where appropriate.
11. Conduct the sign, Wilcoxon signed-rank, Mann–Whitney, Kruskal–Wallis and Friedman
    tests, and state what each actually tests.
12. Implement a permutation test and a bootstrap interval, and state their assumptions.

## Prerequisites

| Need | From | Revise before |
|---|---|---|
| Hypothesis testing, errors, effect sizes | [M15](15-hypothesis-testing.md) | Units 1–5 |
| Regression, sums of squares, F statistic | [M16](16-correlation-and-regression.md) | Units 3–5 |
| Variance decomposition | [M11](11-joint-distributions.md) | Unit 6 |
| Chi-square and F distributions | [M12](12-sampling-and-sampling-distributions.md) | Units 3, 5 |

## Topic breakdown

### Unit 1 — One-way ANOVA (3.5 h)

- Model: \(y_{ij}=\mu+\tau_i+\varepsilon_{ij}\), with the assumptions stated.
- Hypotheses: all group means equal versus at least one differs.
- Decomposition: \(SST=SSB+SSW\); degrees of freedom \(k-1\), \(N-k\), \(N-1\).
- Mean squares and \(F=MSB/MSW\); the ratio's distribution under \(H_0\).
- Reading the table; the relationship \(F=t^{2}\) for two groups.
- Effect sizes: \(\eta^{2}=SSB/SST\), \(\omega^{2}\) as the less biased version.
- Assumptions: independence, normality of residuals, equal variances — and how each is
  checked.

### Unit 2 — Post-hoc and multiple comparisons (2 h)

- Why a significant F does not identify which groups differ.
- Tukey HSD and the studentised range; family-wise control.
- Dunnett (many groups versus one control), Bonferroni-adjusted pairwise tests.
- Reporting a compact letter display or an interval plot.
- The multiplicity link back to M15.

### Unit 3 — Two-way ANOVA and interactions (2.5 h)

- Two factors, main effects, interaction term.
- Reading an interaction plot; ordinal versus disordinal interactions.
- Why main effects can be misleading when interaction is present.
- Unbalanced designs and Type I/II/III sums of squares (conceptually, not by hand).
- Repeated-measures designs: why independence fails, and the mixed-model idea (named,
  not developed).

### Unit 4 — Chi-square: three procedures (3 h)

- The statistic \(\chi^{2}=\sum (O-E)^{2}/E\), and its approximate distribution.
- Goodness of fit: expected counts from a hypothesised distribution; df = categories −
  1 − estimated parameters.
- Independence: expected counts under \(H_0\) from margins; df = \((r-1)(c-1)\).
- Homogeneity: same computation, different design; what changes is the sampling scheme.
- Expected-count condition (≥5), and remedies: collapsing, exact tests, permutation.
- Effect sizes: Cramér's V, odds ratio; Fisher's exact for 2×2; McNemar for paired
  binary data.
- Ordered categories: why chi-square ignores order, and what to use instead.

### Unit 5 — Nonparametric methods (3.5 h)

- What "distribution-free" means, and which assumption each rank test removes.
- Sign test; Wilcoxon signed-rank for paired data; the symmetry assumption.
- Mann–Whitney U as a test of stochastic dominance; the median-test misconception.
- Kruskal–Wallis for \(k\) groups; Dunn post-hoc with correction.
- Friedman for randomised blocks.
- Correlation alternatives: Spearman, Kendall, and their inference.
- Normality tests (Shapiro–Wilk, Kolmogorov–Smirnov) and why a non-significant result
  does not establish normality.
- Efficiency: the ~0.955 asymptotic efficiency of Wilcoxon versus t under normality.

### Unit 6 — Resampling: permutation and bootstrap (3 h)

- Permutation test: shuffle labels, recompute, count; exchangeability as the only
  assumption.
- The p-value formula \((1+\#\{T^{*}\ge T\})/(B+1)\) and why the +1 matters.
- Bootstrap: resample with replacement; standard error; percentile and BCa intervals.
- When the bootstrap fails: extreme quantiles, very small \(n\), dependent data.
- Comparing parametric, rank-based and resampling answers on the same dataset, and
  defending the choice.

### Unit 7 — Choosing a method (0.5 h)

- A decision procedure: design → variable types → assumptions → power.
- A table of alternatives for each violated assumption.
- What to report regardless of method: effect size, interval, \(n\), and the checks.

## Important mathematical concepts

**ANOVA decomposition.**

\[ \sum_{i}\sum_{j}(y_{ij}-\bar y)^{2}
   =\sum_{i} n_i(\bar y_i-\bar y)^{2}+\sum_{i}\sum_{j}(y_{ij}-\bar y_i)^{2} \]

**The F statistic.**

\[ F=\frac{SSB/(k-1)}{SSW/(N-k)}\sim F_{k-1,\,N-k}\ \text{ under } H_0 \]

**Chi-square statistic.**

\[ \chi^{2}=\sum_{ij}\frac{(O_{ij}-E_{ij})^{2}}{E_{ij}}, \qquad
   E_{ij}=\frac{(\text{row}_i)(\text{col}_j)}{n} \]

**Mann–Whitney U** as a count of pairwise orderings:

\[ U=\#\{(i,j): x_i>y_j\} \]

**Permutation p-value** with \(B\) random permutations:

\[ \hat p=\frac{1+\#\{b: T^{*}_{b}\ge T_{\text{obs}}\}}{B+1} \]

## Expected knowledge after completion

You can, without notes:

- Complete an ANOVA table from partial information and compute \(\eta^2\).
- Explain why Tukey is needed after a significant F.
- Choose between goodness of fit, independence and homogeneity for three described
  designs.
- Compute expected counts and df for an \(r\times c\) table.
- State what Mann–Whitney actually tests and why the median description is unreliable.
- Write a permutation test in ten lines and interpret its p-value.

## Connections to Data Science

- **Segment comparison** in dashboards is ANOVA or its nonparametric equivalent, with
  multiplicity.
- **Categorical features versus a binary target** is chi-square, or better, a
  proportion test with an interval.
- **A/B tests with more than two variants** are one-way ANOVA.
- **Permutation tests** are the gold standard for A/B analysis when the metric is
  unusual.
- **Distribution-free methods** matter for latency and revenue metrics, which are
  skewed and heavy-tailed.

## Practical applications

| Setting | Question | Method |
|---|---|---|
| Three teaching methods | Do they differ? | One-way ANOVA + Tukey |
| Product groups and region | Does the effect depend on region? | Two-way ANOVA with interaction |
| Survey responses | Are satisfaction and tenure associated? | Chi-square independence + Cramér's V |
| Paired before/after | Did the campaign shift the metric? | Wilcoxon signed-rank |
| Skewed revenue metric | Is variant B better? | Permutation test |

## Exercises and assessment plan

| Component | Count | Focus |
|---|---|---|
| ★ Drill | 8 | ANOVA tables, χ² computation, df |
| ★★ Application | 8 | Full analyses with post-hoc, effect sizes, interpretation |
| ★★★ Challenge | 4 | Prove F = t²; simulate the χ² approximation failing; implement a permutation test; bootstrap versus t under skew |
| Quiz | 10 items | Method selection |
| Practical notebook | 1 | Three-group comparison with assumption audit and sensitivity analysis |
| Simulation lab | 1 | Bootstrap and permutation test |

## Recommended study sequence

| Session | Focus | Hours |
|---|---|---|
| 1 | Unit 1: one-way ANOVA | 3.5 |
| 2 | Unit 2: post-hoc comparisons | 2.0 |
| 3 | Unit 3: two-way and interactions | 2.5 |
| 4 | Unit 4: chi-square family | 3.0 |
| 5 | Unit 5: nonparametric tests | 3.5 |
| 6 | Units 6–7: resampling and method choice | 2.5 |

**Before this module:** [M16](16-correlation-and-regression.md). **After:**
[M18 — Bayesian Statistics and Statistical Methods for Data
Science](18-bayesian-and-data-science-methods.md).
