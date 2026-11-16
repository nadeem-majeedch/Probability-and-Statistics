---
title: "M09 — Discrete Probability Distributions"
description: Bernoulli, binomial, geometric, negative binomial, hypergeometric, Poisson and multinomial — and how to choose between them.
module: 9
part: 3
level: Core
hours: 14
prerequisites: [8]
---

# M09 · Discrete Probability Distributions

<div class="psds-meta" markdown>
<span class="psds-chip psds-chip--core">Core</span>
<span class="psds-chip">Part III · Random variables</span>
<span class="psds-chip">14 study hours</span>
<span class="psds-chip">Module 9 of 18</span>
</div>

## Introduction

Statistics has a small library of named distributions, and most practical modelling
of counts is choosing the right book from that shelf. This module teaches the
shelf — seven families — and, more importantly, the question that identifies which
one applies.

The question is never "which formula looks right". It is a sequence of structural
questions about the experiment: How many trials? Is the number of trials fixed in
advance or random? Are trials independent? Is the probability of success constant?
Are you sampling with or without replacement? Are you counting successes, trials, or
arrivals in an interval? Each answer eliminates families.

Students who learn the formulas without the questions end up applying the binomial to
without-replacement data and the Poisson to bounded counts, and the arithmetic is
perfect while the model is wrong.

## Why this matters

Counts are everywhere in data: clicks per session, defects per batch, arrivals per
minute, successes in \(n\) trials, conversions per visitor. The distribution you
assume determines the standard errors, the tests, and the simulation you design.

Two specific consequences. First, **the Poisson/binomial distinction controls
variance**: Poisson assumes variance equals mean, binomial assumes variance below
mean. Choosing wrongly distorts every interval built on it — a fact that reappears
as "overdispersion" in M17. Second, **with versus without replacement** decides between
binomial and hypergeometric, and the difference is not academic when the sample is a
large fraction of the population.

## Learning objectives

By the end of this module you can:

1. Specify the Bernoulli, binomial, geometric, negative binomial, hypergeometric,
   discrete uniform, Poisson and multinomial distributions: support, PMF, parameters,
   mean and variance.
2. Choose the family for a described experiment by asking the structural questions,
   and justify the choice against the alternatives.
3. Derive the binomial mean and variance using indicator variables.
4. Derive the Poisson PMF as a limit of the binomial, and state the Poisson process
   assumptions.
5. Use the memorylessness of the geometric distribution and explain precisely what it
   does and does not imply.
6. Compute exact probabilities and tail probabilities, and choose between exact
   computation and approximation.
7. Apply the hypergeometric finite-population correction and explain when it matters.
8. Simulate each family, verify the empirical mean and variance against theory, and
   report the Monte Carlo error.

## Prerequisites

| Need | From | Revise before |
|---|---|---|
| Expectation, variance, indicators | [M08](08-random-variables-and-expectation.md) | Units 4–5 |
| PMF and CDF | M08 | Unit 2 |
| Binomial coefficients, counting | [M05](05-counting-and-combinatorics.md) | Unit 3 |
| Independence | [M07](07-conditional-probability-and-bayes.md) | Unit 3 |

## Topic breakdown

### Unit 1 — The choice problem (1.5 h)

- The structural question tree: number of trials fixed or not; independence;
  constant \(p\); replacement; counting successes/trials/arrivals.
- The decision table, worked through eight examples.
- The commonest misapplications: binomial on without-replacement data; Poisson on
  bounded counts; geometric when the trial count is fixed.
- Why "the data are counts" is not enough information to choose a model.

### Unit 2 — Bernoulli and binomial (3 h)

- Bernoulli: the atom of discrete modelling; mean \(p\), variance \(p(1-p)\).
- Binomial: \(n\) independent trials, constant \(p\); PMF and its derivation by
  counting.
- Mean \(np\) and variance \(np(1-p)\) derived via indicators — the model proof of the
  course.
- Shape: symmetric at \(p=0.5\), skewed otherwise; when the normal approximation is
  reasonable (formalised in M13).
- Sums of binomials; the success-count decomposition.
- Worked examples: pass/fail simulation, defect counts, conversion counts.

### Unit 3 — Geometric and negative binomial (2.5 h)

- Geometric: number of trials until the first success; PMF \((1-p)^{k-1}p\).
- Mean \(1/p\), variance \((1-p)/p^2\).
- Memorylessness: \(\Pr(X>m+n\mid X>m)=\Pr(X>n)\), derived and interpreted.
- Negative binomial: trials until the \(r\)-th success; PMF and mean \(r/p\).
- The common error: treating "count until the third failure" as binomial.
- Applications: reliability, retries, customer acquisition.

### Unit 4 — Hypergeometric (2 h)

- Sampling without replacement; PMF \(\binom{K}{k}\binom{N-K}{n-k}/\binom{N}{n}\).
- Mean \(nK/N\); variance with the finite-population correction \((N-n)/(N-1)\).
- When the binomial approximation is adequate (small \(n/N\)) and when it is not.
- Applications: quality control, audit sampling, overlap between two lists.

### Unit 5 — Poisson (3 h)

- The Poisson process assumptions: independent increments, constant rate, no
  simultaneous events.
- Derivation as the limit of binomial with \(np\to\lambda\).
- PMF \(e^{-\lambda}\lambda^k/k!\); mean = variance = \(\lambda\).
- Additivity of independent Poissons; thinning.
- Inter-arrival times are exponential (forward link to M10).
- Overdispersion in practice: real counts usually exceed Poisson variance, and what to
  do about it (M17).
- Worked examples: call arrivals, server errors, radioactive decays.

### Unit 6 — Discrete uniform and multinomial (1 h)

- Discrete uniform: the reference model for equally likely outcomes.
- Multinomial: counts in \(k\) categories; PMF, means, variances, and negative
  covariance between categories.
- Applications: categorical survey counts, token frequencies, dice experiments.

### Unit 7 — Simulation and model checking (1 h)

- Sampling from each family with `scipy.stats`.
- Comparing empirical mean/variance to theory; the variance-mean ratio as a diagnostic
  for overdispersion.
- Simulating a Poisson process and checking the exponential gaps.
- Design of a "which distribution fits?" comparison.

## Important mathematical concepts

**Binomial PMF and moments.**

\[ \Pr(X=k)=\binom{n}{k}p^{k}(1-p)^{n-k}, \qquad
   \E[X]=np, \qquad \Var(X)=np(1-p) \]

**Geometric and negative binomial.**

\[ \Pr(X=k)=(1-p)^{k-1}p, \qquad \E[X]=\frac{1}{p};
   \qquad
   \Pr(X=k)=\binom{k-1}{r-1}p^{r}(1-p)^{k-r} \]

**Hypergeometric.**

\[ \Pr(X=k)=\frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}, \qquad
   \Var(X)=n\frac{K}{N}\left(1-\frac{K}{N}\right)\frac{N-n}{N-1} \]

**Poisson.**

\[ \Pr(X=k)=e^{-\lambda}\frac{\lambda^{k}}{k!}, \qquad \E[X]=\Var(X)=\lambda \]

**Poisson as a binomial limit.** With \(p=\lambda/n\) and \(n\to\infty\),

\[ \binom{n}{k}p^{k}(1-p)^{n-k} \longrightarrow e^{-\lambda}\frac{\lambda^{k}}{k!} \]

## Expected knowledge after completion

You can, without notes:

- Given an experiment in words, name the family, its parameters, and its mean and
  variance — and say which alternative you rejected and why.
- Compute a binomial tail probability by hand and with `scipy.stats.binom`.
- Explain memorylessness with a concrete example and say why it is surprising.
- Decide when the finite-population correction is needed.
- Explain why real count data is often overdispersed relative to Poisson.

## Connections to Data Science

- **Conversion rates** are binomial; **sessions per user** are usually overdispersed
  Poisson (negative binomial).
- **A/B testing** uses binomial variance implicitly in every power calculation (M15,
  M18).
- **Click models and arrival processes** are Poisson.
- **Imbalanced classification** metrics are binomial proportions with small \(p\),
  which is why Wald intervals fail there (M14).
- **Sampling audits** without replacement are hypergeometric.

## Practical applications

| Setting | Question | Family |
|---|---|---|
| Email campaign | Probability at least 5 of 100 recipients convert? | Binomial |
| Support queue | Probability the next call arrives within 2 minutes? | Geometric (discrete approximation) |
| Quality audit | Probability 2 defectives in a sample of 20 from 500? | Hypergeometric |
| Website traffic | Expected arrivals in 10 minutes at 12/hour? | Poisson |
| Survey | Are category counts consistent with equal preference? | Multinomial (tested in M17) |

## Exercises and assessment plan

| Component | Count | Focus |
|---|---|---|
| ★ Drill | 10 | PMF, mean, variance for each family |
| ★★ Application | 8 | Model selection from described experiments |
| ★★★ Challenge | 4 | Derive binomial variance with indicators; Poisson limit; memorylessness proof; simulate and diagnose overdispersion |
| Quiz | 10 items | "Which distribution and why" |
| Practical notebook | 1 | Fit and compare families on real count data |
| Simulation lab | 1 | Coin, dice, and arrival simulations with theory comparison |

## Recommended study sequence

| Session | Focus | Hours |
|---|---|---|
| 1 | Unit 1: the choice problem | 2.0 |
| 2 | Unit 2: Bernoulli and binomial | 3.0 |
| 3 | Unit 3: geometric and negative binomial | 2.5 |
| 4 | Unit 4: hypergeometric | 2.0 |
| 5 | Unit 5: Poisson | 3.0 |
| 6 | Units 6–7: uniform, multinomial, simulation | 1.5 |

**Before this module:** [M08](08-random-variables-and-expectation.md). **After:**
[M10 — Continuous Distributions](10-continuous-distributions.md) supplies the
continuous counterparts, including the exponential gaps of a Poisson process.
