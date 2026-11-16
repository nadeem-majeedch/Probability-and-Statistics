---
title: "M10 — Continuous Probability Distributions"
description: "Densities as areas: uniform, exponential, gamma, beta, normal, lognormal and Weibull, and how to choose a lifetime model."
module: 10
part: 3
level: Core
hours: 14
prerequisites: [8, 9]
---

# M10 · Continuous Probability Distributions

<div class="psds-meta" markdown>
<span class="psds-chip psds-chip--core">Core</span>
<span class="psds-chip">Part III · Random variables</span>
<span class="psds-chip">14 study hours</span>
<span class="psds-chip">Module 10 of 18</span>
</div>

## Introduction

For a continuous variable, probability is **area**. That single sentence reorganises
everything: a density is not a probability, it can exceed 1, and \(\Pr(X=x)=0\) for
every single point — which is why continuous models never answer "what is the chance
of exactly this value" but always "what is the chance of this range".

This module supplies the continuous families that applied work actually uses, and it
spends the most time on the normal distribution — not because everything is normal,
but because so much of inference is built by assuming it, approximating it, or
transforming towards it. The normal is the reference distribution of this course, and
knowing when it is inappropriate is as important as knowing its properties.

The other families are not decoration. The exponential models waiting times; the gamma
models sums of waiting times; the beta models proportions and is the conjugate prior
of M18; the lognormal models incomes and concentrations; the Weibull models failure
time with a changing hazard. Choosing among them is a modelling decision with visible
consequences.

## Why this matters

Continuous models dominate measurement: time, money, temperature, concentration,
latency. And the practical failure modes are specific:

- Treating a density as a probability, then reporting "the probability of exactly
  3.2 seconds is 0.31".
- Applying a normal model to a strictly positive, heavily skewed variable, so that the
  model assigns mass to impossible negative values.
- Assuming normality without checking, so that intervals and tests are wrong in the
  tails — which is exactly where decisions get made.

## Learning objectives

By the end of this module you can:

1. Specify the uniform, exponential, gamma, beta, normal, lognormal and Weibull
   distributions: support, density, parameters, mean and variance.
2. Compute probabilities as integrals and with `scipy.stats`, and check them against
   the CDF.
3. Derive the exponential distribution's memorylessness and contrast it with the
   geometric case.
4. Standardise a normal variable, compute probabilities in both directions with tables
   and software, and state the 68–95–99.7 rule.
5. Explain linear transformations of normals and why the family is closed under them.
6. Model a positive skewed quantity with the lognormal and explain the mechanism.
7. Choose between exponential, gamma and Weibull for lifetime data using the hazard
   function, and interpret the shape parameter.
8. Assess normality with Q–Q plots and explain the limitations of that assessment.
9. Explain why the beta distribution is the natural model for a proportion, and connect
   it to M18.

## Prerequisites

| Need | From | Revise before |
|---|---|---|
| Density, CDF, expectation, variance | [M08](08-random-variables-and-expectation.md) | Units 2, 4–5 |
| Integration and improper integrals | [M02](02-mathematical-foundations.md) | Unit 7 |
| Discrete analogues (geometric, binomial limits) | [M09](09-discrete-distributions.md) | Units 3, 5 |
| Histograms and density plots | [M04](04-data-visualization.md) | Unit 3 |

## Topic breakdown

### Unit 1 — Density as area (2 h)

- From histogram to density: binning, scaling, and the limit.
- Why \(\Pr(X=x)=0\); why \(f(x)>1\) is legal; units of a density.
- CDF, quantile function, and the probability integral transform
  \(F(X)\sim U(0,1)\) — a result used for simulation in M18.
- Reading a density's shape: modes, tails, support.
- Common misreading: "most likely value" is a mode, not a probability.

### Unit 2 — Uniform and exponential (2.5 h)

- Continuous uniform: density, CDF, mean, variance; the reference for simulation.
- Exponential: density \(\lambda e^{-\lambda t}\), CDF, mean \(1/\lambda\), variance
  \(1/\lambda^2\).
- **Memorylessness proved** and interpreted: the past tells you nothing about the
  remaining wait.
- Where exponential models fail: ageing components, human lifetimes, anything with a
  changing hazard.
- Relationship to the Poisson process (M09): exponential gaps.

### Unit 3 — Gamma and Weibull (2 h)

- Gamma as a sum of \(k\) independent exponentials; shape and rate parameters.
- Mean \(\alpha/\beta\), variance \(\alpha/\beta^2\); the chi-square as a special case
  (used in M12).
- Weibull: shape \(k\), scale \(\lambda\); hazard increasing, constant or decreasing.
- Reading a hazard function; bathtub curves.
- Choosing between exponential, gamma and Weibull for failure data, and the
  consequences of choosing wrongly.

### Unit 4 — The normal distribution (4 h)

- Density, parameters, standardisation \(z=(x-\mu)/\sigma\).
- Computing probabilities with the z-table and with software, both directions
  (value → probability, probability → quantile).
- The 68–95–99.7 rule; why it is a rule about the normal, not about data.
- Linearity: \(aX+b\sim N(a\mu+b, a^2\sigma^2)\).
- Sums of independent normals (proved properly in M13).
- Why the normal is the reference distribution: maximum entropy for given variance, and
  the CLT limit.
- Assessing normality: Q–Q plots, histograms, and why one plot is not enough.

### Unit 5 — Lognormal and beta (2 h)

- Lognormal: \(\log X\sim N(\mu,\sigma^2)\); mean \(e^{\mu+\sigma^2/2}\); right skew;
  multiplicative mechanisms.
- Why income, prices and concentrations are often lognormal (multiplicative growth).
- Beta: support \((0,1)\), two shape parameters, mean \(a/(a+b)\); flexible shapes
  including U-shaped.
- Beta as the model for a proportion and as the conjugate prior for a Bernoulli
  probability (M18).
- Transforming between scales: what a mean on the log scale means on the original
  scale.

### Unit 6 — Simulation and model checking (1.5 h)

- Sampling from each family; comparing empirical and theoretical quantiles.
- Inverse-transform sampling using \(F^{-1}(U)\), implemented by hand.
- Q–Q plots for normal, exponential and lognormal fits to the same data.
- Simulating a lifetime dataset and comparing exponential and Weibull fits.

## Important mathematical concepts

**Exponential density and memorylessness.**

\[ f(t)=\lambda e^{-\lambda t}\;(t\ge 0), \qquad \E[T]=\frac{1}{\lambda}, \qquad
   \Pr(T>s+t\mid T>s)=\Pr(T>t) \]

**Standard normal density and standardisation.**

\[ \phi(z)=\frac{1}{\sqrt{2\pi}}e^{-z^{2}/2}, \qquad
   Z=\frac{X-\mu}{\sigma}\sim N(0,1) \]

**Normal probability as an integral.**

\[ \Pr(a\le X\le b)=\Phi\!\left(\frac{b-\mu}{\sigma}\right)-\Phi\!\left(\frac{a-\mu}{\sigma}\right) \]

**Lognormal moments.**

\[ \E[X]=e^{\mu+\sigma^{2}/2}, \qquad
   \Var(X)=\left(e^{\sigma^{2}}-1\right)e^{2\mu+\sigma^{2}} \]

**Beta density.**

\[ f(x)=\frac{x^{a-1}(1-x)^{b-1}}{B(a,b)}, \qquad x\in(0,1), \qquad
   \E[X]=\frac{a}{a+b} \]

## Expected knowledge after completion

You can, without notes:

- Compute \(\Pr(1<X<3)\) for an exponential with \(\lambda=2\) by integration and by
  CDF subtraction, and show they agree.
- Turn a raw score into a percentile and a percentile back into a raw score for a
  normal variable.
- Explain why a normal model is wrong for income, and what to use instead.
- Read a Q–Q plot and say whether the tails are heavier than normal.
- Explain memorylessness and name two situations where assuming it would be a serious
  error.

## Connections to Data Science

- **Latency and queueing**: exponential and gamma models of response times.
- **Feature scaling**: z-scores assume a location–scale family; the assumption is
  visible in the units.
- **Log-transforming skewed targets** is the lognormal mechanism, and it changes the
  interpretation of every coefficient.
- **Calibration and probability outputs** live in \((0,1)\), where the beta is the
  natural model.
- **Anomaly thresholds** stated in sigmas are normal-model statements, whether or not
  the author knows it.

## Practical applications

| Setting | Question | Family |
|---|---|---|
| Server latency | Probability a request exceeds 500 ms? | Exponential or lognormal |
| Exam scores | What score is the 90th percentile? | Normal |
| Component lifetime | Is the hazard increasing with age? | Weibull |
| Household income | Why is the mean above the median? | Lognormal |
| Click-through rate | How uncertain is this proportion? | Beta (M18) |

## Exercises and assessment plan

| Component | Count | Focus |
|---|---|---|
| ★ Drill | 8 | Densities, CDFs, standardisation |
| ★★ Application | 7 | Model choice; probability computations; quantiles |
| ★★★ Challenge | 4 | Prove memorylessness; derive lognormal mean; hazard analysis; normality assessment |
| Quiz | 10 items | Density versus probability; model selection |
| Practical notebook | 1 | Fit and compare continuous families to real measurements |
| Simulation lab | 1 | Inverse-transform sampling by hand versus `scipy` |

## Recommended study sequence

| Session | Focus | Hours |
|---|---|---|
| 1 | Unit 1: density as area | 2.0 |
| 2 | Unit 2: uniform and exponential | 2.5 |
| 3 | Unit 3: gamma and Weibull | 2.0 |
| 4 | Unit 4: the normal distribution | 4.0 |
| 5 | Unit 5: lognormal and beta | 2.0 |
| 6 | Unit 6: simulation and model checks | 1.5 |

**Before this module:** [M09](09-discrete-distributions.md). **After:**
[M11 — Joint Distributions](11-joint-distributions.md) moves from one variable to
several.
