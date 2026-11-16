---
title: Part III — Random Variables and Distributions
description: Random variables, expectation, the named discrete and continuous families, and joint distributions. Modules M08–M11.
---

# Part III — Random Variables and Distributions

**Modules M08–M11 · 58 study hours · Core, one advanced · Prerequisites: Parts I–II**

---

## Why this part exists

This is the technical heart of the course. A random variable turns outcomes into
numbers; a distribution describes those numbers; expectation and variance summarise
them; a joint distribution describes several at once. Everything in Parts IV–VIII is
built on these four modules.

It is also the part where students most often settle for symbol-pushing. The defence is
structural: every definition is followed by a computation you do by hand, a figure you
look at, and a simulation you run. A density is not "a formula with an integral" — it is
a shape whose area is probability, and you will have computed that area numerically
before you are asked to integrate it.

M11 is marked Advanced and is the gateway to modelling: covariance is defined there,
and so is conditional expectation — the object regression estimates and ANOVA
decomposes.

## Modules

| # | Module | Level | Hours | Focus |
|---|---|---|---|---|
| M08 | [Random Variables and Mathematical Expectation](../modules/08-random-variables-and-expectation.md) | Core | 16 | PMF/PDF/CDF, transformations, expectation, variance, moments, inequalities |
| M09 | [Discrete Probability Distributions](../modules/09-discrete-distributions.md) | Core | 14 | Bernoulli, binomial, geometric, negative binomial, hypergeometric, Poisson, multinomial |
| M10 | [Continuous Probability Distributions](../modules/10-continuous-distributions.md) | Core | 14 | Uniform, exponential, gamma, beta, normal, lognormal, Weibull; hazards |
| M11 | [Joint Probability Distributions](../modules/11-joint-distributions.md) | Advanced | 14 | Marginals, conditionals, convolution, order statistics, covariance, total variance |

## What you will be able to do

- Verify that a proposed function is a valid PMF or PDF, and find the constant that makes
  it one.
- Go from density to CDF to interval probability and back, by hand and in software.
- Decide between the discrete families for a described experiment, and say why the
  others are wrong.
- Explain memorylessness for the geometric and exponential cases, and what it does not
  imply.
- Compute covariance and correlation from a joint table, then check by simulation.
- State and use the law of total variance — the identity behind regression's R² and
  ANOVA's decomposition.

## Simulation experiments in this part

Transformation of a variable (simulated density versus derived density), convolution of
sums, order statistics, the Poisson limit of the binomial, and the total-variance
decomposition.

## Common misconceptions this part removes

| Misconception | Corrected in |
|---|---|
| "*f*(*x*) is a probability" | M08 |
| "Linearity of expectation needs independence" | M08 |
| "Var(*X* + *Y*) = Var(*X*) + Var(*Y*)" | M11 |
| "Zero correlation means independence" | M11 |
| "The marginal distributions determine the joint" | M11 |
| "λ is the mean of an exponential" | M10 |

## Start

Begin with [M08 — Random Variables and Mathematical Expectation](../modules/08-random-variables-and-expectation.md).
Expect to spend longer here than in Parts I or II; the hours reflect that.
