---
title: Quick revision sheets
description: One compact sheet per part of the course — the definitions, the formulas and the one thing that usually goes wrong.
---

# Quick revision sheets

Eight parts, one page each. Nothing here is new; everything is compressed.

## Part I — Foundations (M01–M04)

| Idea | Content |
|---|---|
| Population vs sample | parameters are unknown and fixed; statistics are known and random |
| Centre | mean (balance point), median (middle), mode (peak) |
| Spread | SD, IQR, range, CV = s/x̄ |
| Shape | skewness, kurtosis, bimodality |
| Standard score | z = (x − x̄)/s |
| Plots | histogram (shape), box plot (spread/outliers), scatter (relationship), bar (categories) |

**Usually wrong:** using the mean for skewed data, or reading a histogram's y-axis as probability.

## Part II — Probability (M05–M07)

| Idea | Content |
|---|---|
| Counting | nPr ordered, nCr unordered, n! arrangements |
| Rules | P(Aᶜ) = 1 − P(A); P(A∪B) = P(A)+P(B)−P(A∩B) |
| Conditional | P(A\|B) = P(A∩B)/P(B) |
| Independence | P(A∩B) = P(A)P(B) |
| Total probability | P(B) = Σ P(B\|Aᵢ)P(Aᵢ) |
| Bayes | P(A\|B) = P(B\|A)P(A)/P(B) |

**Usually wrong:** treating P(A|B) and P(B|A) as the same number — the base-rate fallacy.

## Part III — Random variables (M08–M11)

| Idea | Content |
|---|---|
| Description | PMF (discrete), PDF (continuous), CDF (both) |
| Expectation | E[X] = Σx p(x) or ∫x f(x) dx; linear always |
| Variance | Var(X) = E[X²] − (E[X])²; Var(aX+b) = a²Var(X) |
| Sums | Var(X±Y) = Var X + Var Y ± 2Cov(X,Y) |
| Covariance | Cov = E[XY] − E[X]E[Y]; ρ = Cov/(σxσy) |
| Families | Bernoulli, binomial, geometric, Poisson; uniform, exponential, normal, gamma |

**Usually wrong:** adding variances of dependent variables, or writing N(μ, σ).

## Part IV — Sampling and limits (M12–M13)

| Idea | Content |
|---|---|
| Standard error | SE(x̄) = s/√n; SE(p̂) = √(p̂(1−p̂)/n) |
| Sampling distribution | the distribution of a statistic over repeated samples |
| LLN | x̄ → μ as n grows |
| CLT | (x̄ − μ)/(σ/√n) → N(0,1) |
| Rule of thumb | n ≥ 30 helps for mildly skewed data; heavy tails need far more |

**Usually wrong:** saying the CLT makes the *data* normal, or applying it to extreme quantiles.

## Part V — Inference (M14–M15)

| Idea | Content |
|---|---|
| CI for a mean | x̄ ± t·s/√n |
| CI for a proportion | p̂ ± z√(p̂(1−p̂)/n) |
| Test statistic | (estimate − hypothesised value)/SE |
| p-value | P(data at least this extreme \| H₀) |
| Errors | α = P(reject \| H₀ true); β = P(fail to reject \| H₁ true) |
| Power | 1 − β; rises with effect size, n, and α |

**Usually wrong:** reading a p-value as P(H₀ true), or a CI as a 95 % chance the parameter is inside.

## Part VI — Relationships (M16)

| Idea | Content |
|---|---|
| Pearson r | linear association, −1 to 1 |
| Test for r | t = r√((n−2)/(1−r²)) on n − 2 df |
| Regression | ŷ = b₀ + b₁x, b₁ = Cov(x,y)/Var(x) |
| Fit | R² = 1 − SSE/SST; sₑ = residual SD |
| Caveats | correlation ≠ causation; extrapolation is unsafe |

**Usually wrong:** interpreting R² as "the model is correct", or a slope as causal.

## Part VII — Comparative inference (M17)

| Idea | Content |
|---|---|
| ANOVA | F = MS_between/MS_within; k − 1 and N − k df |
| After ANOVA | Tukey HSD for pairwise differences |
| Chi-square | Σ(O−E)²/E; df = (r−1)(c−1) for independence |
| Effect sizes | η², Cramér's V, rank-biserial |
| Nonparametric | Wilcoxon, Mann–Whitney, Kruskal–Wallis, Friedman |

**Usually wrong:** running many t-tests instead of ANOVA, then reporting the smallest p.

## Part VIII — Modern methods (M18)

| Idea | Content |
|---|---|
| Bayes | posterior ∝ prior × likelihood |
| Conjugate | Beta–binomial, normal–normal, gamma–Poisson |
| Intervals | credible interval: posterior probability statement |
| Resampling | bootstrap SE and percentile intervals |
| Monte Carlo | simulate to integrate, and report the simulation error |

**Usually wrong:** using a flat prior and calling the result "objective", or bootstrapping dependent data.
