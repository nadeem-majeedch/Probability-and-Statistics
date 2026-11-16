---
title: Part VII — Comparative Inference
description: ANOVA, chi-square tests and nonparametric methods. Module M17.
---

# Part VII — Comparative Inference

**Module M17 · 16 study hours · Advanced · Prerequisites: Parts I–VI**

---

## Why this part exists

Three questions dominate applied analysis: do these groups differ, are these two
categorical variables associated, and what do I do when the assumptions fail? This part
answers all three, as one coherent argument rather than three unrelated procedures.

The unifying idea is variance decomposition. ANOVA splits total variation into what the
group structure explains and what it leaves unexplained; the chi-square statistic is the
same logic applied to counts; the F statistic is a ratio of two such decompositions.
Seen this way, ANOVA is regression with a categorical predictor — which is literally what
the software computes.

The nonparametric methods are the honest answer to violated assumptions, and the
resampling methods introduced here are the bridge to modern practice: the permutation
test and the bootstrap require almost no distributional assumptions, only a design you
can defend.

## Module

| # | Module | Level | Hours | Focus |
|---|---|---|---|---|
| M17 | [ANOVA, Chi-Square and Nonparametric Statistics](../modules/17-anova-chi-square-nonparametric.md) | Advanced | 16 | One- and two-way ANOVA, post-hoc, χ² family, rank tests, permutation and bootstrap |

## What you will be able to do

- Complete an ANOVA table from partial information and compute an effect size from it.
- Explain why a significant F does not say which groups differ, and run Tukey correctly.
- Choose between goodness-of-fit, independence and homogeneity for three described
  designs, and compute the degrees of freedom for each.
- State what Mann–Whitney actually tests, and why "it tests medians" is unreliable.
- Implement a permutation test and a bootstrap interval, and state their assumptions.
- Choose a method for a described dataset and defend the choice in writing.

## Simulation experiments in this part

The χ² approximation failing at small expected counts; a permutation test on a skewed
metric; bootstrap coverage under skew; multiplicity inflation in post-hoc comparisons.

## Common misconceptions this part removes

| Misconception | Corrected in |
|---|---|
| "ANOVA tells you which groups differ" | M17 |
| "Chi-square is always valid for any table" | M17 |
| "Mann–Whitney tests medians" | M17 |
| "Nonparametric means assumption-free" | M17 |
| "A significant normality test means you cannot use *t*" | M17 |
| "Bootstrap works for any statistic" | M17, M18 |

## Start

Begin with [M17 — ANOVA, Chi-Square and Nonparametric Statistics](../modules/17-anova-chi-square-nonparametric.md).
