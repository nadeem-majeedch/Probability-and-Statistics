---
title: Test comparison
description: Every hypothesis test in the course in one table — statistic, assumptions, degrees of freedom, effect size and nonparametric alternative.
---

# Test comparison

The [selection guide](../test-selection.md) walks through the decision. This page is the lookup
table: what each test computes, what it assumes, and what to report alongside it.

## Tests on means and locations

| Test | Null hypothesis | Statistic | Assumptions | df | Effect size | Nonparametric alternative |
|---|---|---|---|---|---|---|
| One-sample z | μ = μ₀ | (x̄ − μ₀)/(σ/√n) | known σ, normal or large n | — | d = (x̄−μ₀)/s | sign test |
| One-sample t | μ = μ₀ | (x̄ − μ₀)/(s/√n) | normal or large n | n − 1 | Cohen's d | Wilcoxon signed-rank |
| Two-sample t (Welch) | μ₁ = μ₂ | (x̄₁−x̄₂)/√(s₁²/n₁+s₂²/n₂) | independent, normal or large n | Welch–Satterthwaite | Cohen's d | Mann–Whitney U |
| Two-sample t (pooled) | μ₁ = μ₂ | same, pooled s | equal variances | n₁+n₂−2 | Cohen's d | Mann–Whitney U |
| Paired t | μ_d = 0 | d̄/(s_d/√n) | normal differences | n − 1 | d_z | Wilcoxon signed-rank |
| One-way ANOVA | μ₁ = … = μ_k | MS_between/MS_within | independent, normal, equal variances | k−1, N−k | η² | Kruskal–Wallis |
| Repeated-measures ANOVA | equal means over time | F ratio on within-subject SS | sphericity, normality | — | partial η² | Friedman |
| Tukey HSD | all pairs equal | q = range/√(MS_E/n) | as ANOVA, balanced | k, N−k | mean difference | Dunn's test |

## Tests on proportions and counts

| Test | Null hypothesis | Statistic | Assumptions | df | Effect size | Alternative |
|---|---|---|---|---|---|---|
| One-proportion z | p = p₀ | (p̂−p₀)/√(p₀(1−p₀)/n) | np₀, n(1−p₀) ≥ 5 | — | h = 2 arcsin√p | exact binomial |
| Two-proportion z | p₁ = p₂ | (p̂₁−p̂₂)/SE_pooled | independent, expected counts ≥ 5 | — | risk difference, RR | Fisher's exact |
| Chi-square goodness of fit | p = p₀ (all cells) | Σ(O−E)²/E | independent, E ≥ 5 | k−1 | Cohen's w | exact multinomial |
| Chi-square independence | no association | Σ(O−E)²/E | independent, E ≥ 5 | (r−1)(c−1) | Cramér's V | Fisher's exact (2×2) |
| McNemar | no change (paired) | (b−c)²/(b+c) | matched pairs, discordant pairs ≥ 10 | 1 | odds ratio | exact McNemar |
| Poisson rate test | λ = λ₀ | (Σx − nλ₀)/√(nλ₀) | Poisson counts, exposure known | — | rate ratio | negative binomial if over-dispersed |

## Tests on variances and distributions

| Test | Null hypothesis | Statistic | Assumptions | df | Notes |
|---|---|---|---|---|---|
| Chi-square variance | σ² = σ₀² | (n−1)s²/σ₀² | **normal data** (fragile) | n − 1 | very sensitive to non-normality |
| F test for two variances | σ₁² = σ₂² | s₁²/s₂² | normal data, independent | n₁−1, n₂−1 | use Levene instead for robustness |
| Levene / Brown–Forsythe | equal variances | ANOVA on absolute deviations | independent groups | k−1, N−k | the standard assumption check |
| Shapiro–Wilk | data are normal | W | — | — | good for n < 50; not a proof |
| Kolmogorov–Smirnov | F = F₀ | sup\|F̂ − F₀\| | continuous, fully specified F₀ | — | parameters estimated from data invalidate it |

## Tests on relationships

| Test | Null hypothesis | Statistic | Assumptions | df | Effect size |
|---|---|---|---|---|---|
| Pearson correlation | ρ = 0 | t = r√((n−2)/(1−r²)) | linearity, bivariate normality | n − 2 | r² |
| Spearman correlation | ρ_s = 0 | rank correlation, t approximation | monotone relationship | n − 2 | ρ_s² |
| Regression slope | β₁ = 0 | b₁/SE(b₁) | linearity, homoscedastic, normal errors | n − 2 | R², sₑ |
| Multiple regression F | all slopes zero | (SSR/k)/(SSE/(n−k−1)) | as above, no collinearity | k, n−k−1 | adjusted R² |
| Chi-square independence | no association | Σ(O−E)²/E | expected counts ≥ 5 | (r−1)(c−1) | Cramér's V |

## Nonparametric tests at a glance

| Test | Design | What it compares | Ties | Small-sample note |
|---|---|---|---|---|
| Sign test | paired | median difference | dropped | exact binomial available |
| Wilcoxon signed-rank | paired | median difference, assumes symmetry | average ranks | exact for n ≤ 25 |
| Mann–Whitney U | two independent | stochastic dominance / shift | average ranks | exact tables for small n |
| Kruskal–Wallis | k independent | distribution location | average ranks | χ² approximation needs n ≥ 5 per group |
| Friedman | k repeated | rankings within subjects | average ranks | exact for small k, n |
| Runs test | sequence | randomness / clustering | — | useful for residual checks |

## What to report for any test

1. The estimate and its interval, in the units of the problem.
2. The test statistic and degrees of freedom.
3. The p-value, to no more than three decimals.
4. The effect size and what counts as small or large in this context.
5. The assumptions checked, and what happened when they were strained.
6. The design limitation: observational, confounded, underpowered, or generalisable.

A result missing items 1 and 4 is a verdict rather than an analysis.
