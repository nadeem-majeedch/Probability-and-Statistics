---
title: Distribution comparison
description: Every distribution in the course in one table — support, formula, mean, variance, when to use it, and how the families connect.
---

# Distribution comparison

One table per family, then the relationships that let you derive one from another. If you know the
situation and not the distribution, read the "use it for" column.

## Discrete distributions

| Distribution | Support | PMF | Mean | Variance | Use it for |
|---|---|---|---|---|---|
| Bernoulli(p) | 0, 1 | p^x (1−p)^(1−x) | p | p(1−p) | one yes/no trial |
| Binomial(n, p) | 0…n | C(n,k) p^k (1−p)^(n−k) | np | np(1−p) | successes in n independent trials |
| Geometric(p) | 1, 2, … | (1−p)^(k−1) p | 1/p | (1−p)/p² | trials until first success |
| Negative binomial(r, p) | r, r+1, … | C(k−1,r−1) p^r (1−p)^(k−r) | r/p | r(1−p)/p² | trials until r-th success; over-dispersed counts |
| Poisson(λ) | 0, 1, … | e^(−λ) λ^k / k! | λ | λ | counts of rare events per exposure |
| Hypergeometric(N, K, n) | max(0, n+K−N)…min(n,K) | C(K,k)C(N−K,n−k)/C(N,n) | nK/N | n(K/N)(1−K/N)(N−n)/(N−1) | successes when sampling without replacement |
| Discrete uniform(a…b) | a…b | 1/(b−a+1) | (a+b)/2 | ((b−a+1)²−1)/12 | equally likely outcomes |
| Multinomial(n, p₁…p_k) | counts summing to n | n!/(k₁!…k_k!) ∏ pᵢ^kᵢ | npᵢ | npᵢ(1−pᵢ) | several categories at once |

**Quick discrimination.** Fixed number of trials → binomial. Fixed number of successes → negative
binomial. No fixed number at all → Poisson. Sampling without replacement → hypergeometric.

## Continuous distributions

| Distribution | Support | Density | Mean | Variance | Use it for |
|---|---|---|---|---|---|
| Uniform(a, b) | [a, b] | 1/(b−a) | (a+b)/2 | (b−a)²/12 | ignorance on an interval; simulation |
| Exponential(λ) | x ≥ 0 | λ e^(−λx) | 1/λ | 1/λ² | waiting time, memoryless process |
| Gamma(α, β) | x > 0 | x^(α−1)e^(−x/β)/(Γ(α)β^α) | αβ | αβ² | waiting for α events; skewed positive data |
| Normal(μ, σ²) | ℝ | (1/(σ√(2π))) e^(−(x−μ)²/(2σ²)) | μ | σ² | errors, means by the CLT |
| Lognormal(μ, σ²) | x > 0 | 1/(xσ√(2π)) e^(−(ln x−μ)²/(2σ²)) | e^(μ+σ²/2) | (e^(σ²)−1)e^(2μ+σ²) | incomes, sizes, multiplicative growth |
| Beta(a, b) | (0, 1) | x^(a−1)(1−x)^(b−1)/B(a,b) | a/(a+b) | ab/((a+b)²(a+b+1)) | a proportion or probability |
| Chi-square(k) | x > 0 | — | k | 2k | variances, goodness of fit |
| t(k) | ℝ | — | 0 (k > 1) | k/(k−2) (k > 2) | means with estimated SD |
| F(d₁, d₂) | x > 0 | — | d₂/(d₂−2) | — | variance ratios, ANOVA |

**Quick discrimination.** Positive, right-skewed, waiting time → exponential or gamma. Positive,
right-skewed, multiplicative → lognormal. Bounded 0–1 → beta. Symmetric, unbounded → normal or t.
Squared distances → chi-square.

## Relationships worth knowing

- **Bernoulli → binomial.** Binomial is a sum of n independent Bernoulli trials.
- **Binomial → Poisson.** As n → ∞ with p → 0 and np → λ, binomial probabilities approach
  Poisson(λ). This is why rare events are modelled as Poisson.
- **Poisson → exponential.** If counts arrive as a Poisson process with rate λ, the gaps between
  arrivals are exponential with rate λ.
- **Gamma ← exponential.** The sum of α independent exponentials with rate λ is Gamma(α, 1/λ).
- **Chi-square ← normal.** The sum of k squared standard normals is Chi-square(k). So
  (n−1)s²/σ² ~ Chi-square(n−1).
- **t ← normal and chi-square.** Normal over the square root of an independent scaled chi-square
  gives t.
- **F ← chi-square.** A ratio of two independent scaled chi-squares gives F. And t(k)² = F(1, k).
- **Beta ← binomial.** With a Beta prior, a binomial likelihood gives a Beta posterior — the
  conjugate pair behind Bayesian proportions.
- **Lognormal ← normal.** If ln X is normal, X is lognormal; never fit a normal to lognormal data.

## Shape cheat sheet

| Situation | Signature |
|---|---|
| Symmetric, bell-shaped, unbounded | normal |
| Right-skewed, positive, single peak | gamma, lognormal, exponential |
| U-shaped or flat | uniform, or a mixture of two groups |
| Spike at zero plus a right tail | zero-inflated count model |
| Two peaks | mixture of two populations — investigate before modelling |
| Much heavier tails than a normal | t, Cauchy, or a contaminated mixture |

## Choosing by question

| Question | Distribution |
|---|---|
| "How many successes out of n?" | binomial |
| "How many events per hour?" | Poisson |
| "How long until the next event?" | exponential |
| "How long until r events?" | gamma |
| "What proportion of a population?" | beta (as a prior), binomial (as data) |
| "Is this measurement extreme?" | normal, via a z-score |
| "How variable is this process?" | chi-square for the variance |
| "Are these group variances equal?" | F |
| "How many draws without replacement?" | hypergeometric |
