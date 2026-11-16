---
title: "M08 — Random Variables and Mathematical Expectation"
description: "From outcomes to numbers: PMFs, densities, CDFs, transformations, expectation, variance and the inequalities that bound them."
module: 8
part: 3
level: Core
hours: 16
prerequisites: [6, 7]
---

# M08 · Random Variables and Mathematical Expectation

<div class="psds-meta" markdown>
<span class="psds-chip psds-chip--core">Core</span>
<span class="psds-chip">Part III · Random variables</span>
<span class="psds-chip">16 study hours</span>
<span class="psds-chip">Module 8 of 18</span>
</div>

## Introduction

Probability theory became useful when it stopped talking about events and started
talking about numbers. A random variable is exactly that move: a function that
assigns a number to each outcome, so that the machinery of arithmetic — sums,
averages, spreads — applies to randomness.

This module builds the whole apparatus in one place. The distribution of a variable
can be described three ways (mass or density, cumulative distribution, and the
moments), and you must be fluent in all three and in moving between them. Then
expectation turns a distribution into a single number — the long-run average — and
variance turns it into a second number describing spread.

Two results in this module are worth more than the rest. **Linearity of expectation**
holds always, even for dependent variables, and it is the reason indicator-variable
arguments are so powerful. **Chebyshev's inequality** converts a variance into a
guarantee about spread without knowing the distribution at all, and it is the tool
that proves the Law of Large Numbers in M13.

## Why this matters

Every model in data science produces a random variable: a prediction, a loss, a
count, a rate. Every evaluation metric is an expectation: accuracy, mean squared
error, expected calibration error. Every uncertainty statement is a variance or a
standard error.

The three-representation fluency matters practically. Machine-learning libraries
give you log-densities; statistics textbooks give you CDFs; simulation gives you
samples. Being able to convert between them is the difference between using a tool
and understanding it.

## Learning objectives

By the end of this module you can:

1. Define a random variable as a measurable function from \(\Omega\) to \(\mathbb{R}\),
   and classify it as discrete or continuous.
2. Verify that a proposed PMF or PDF is valid, and find the constant that makes it
   one.
3. Explain why \(\Pr(X=x)=0\) for continuous \(X\) while \(f(x)\) can exceed 1.
4. Derive a CDF from a PMF/PDF, use it to compute interval probabilities, and recover
   the PMF/PDF from it.
5. Derive the distribution of \(Y=g(X)\) by the CDF method, and use the Jacobian
   formula for monotone transformations.
6. Compute \(\E[X]\) from a definition, and \(\E[g(X)]\) using the law of the
   unconscious statistician.
7. Prove and use linearity of expectation, including for dependent variables, and
   express counts as sums of indicators.
8. Define raw and central moments and compute them for standard families.
9. Compute \(\Var(X)\) two ways and apply the variance rules
   \(\Var(aX+b)=a^2\Var(X)\) and \(\Var(X)=\E[X^2]-\E[X]^2\).
10. Apply Markov's, Chebyshev's and Jensen's inequalities and explain what each buys.
11. Define the moment generating function, derive it for the main families, and use it
    to identify distributions of sums.

## Prerequisites

| Need | From | Revise before |
|---|---|---|
| Axioms and rules of probability | [M06](06-probability-fundamentals.md) | Unit 2 |
| Conditioning and independence | [M07](07-conditional-probability-and-bayes.md) | Units 1, 3 |
| Integration, differentiation | [M02](02-mathematical-foundations.md) | Units 6–7 |
| Series (geometric, exponential) | M02 | Unit 8 |

## Topic breakdown

### Unit 1 — Random variables and their laws (2 h)

- Formal definition; why measurability is mentioned and not required here.
- Discrete, continuous, and mixed variables.
- The induced distribution: pushing a probability measure through a function.
- Indicator variables and why they are the most useful random variables in proofs.
- Notation discipline: \(X\) versus \(x\), \(\Pr(X\le x)\) versus \(p_X(x)\).

### Unit 2 — Mass, density and distribution functions (3 h)

- PMF: properties, normalisation, examples.
- PDF: properties, why it is not a probability, units of density.
- CDF: four properties (non-decreasing, right-continuous, limits 0 and 1), and reading
  probabilities off it.
- Relationships: \(F'=f\); \(p(x)=F(x)-F(x^-)\); interval probabilities.
- Worked conversions in both directions, by hand and in `scipy.stats`.

### Unit 3 — Transformations of variables (2.5 h)

- The CDF method, which always works: \(F_Y(y)=\Pr(g(X)\le y)\).
- Monotone transformations and the Jacobian: \(f_Y(y)=f_X(g^{-1}(y))\,|dg^{-1}/dy|\).
- Non-monotone cases (e.g. \(Y=X^2\)): split the event into preimages.
- Linear transformations and their effect on mean and variance.
- Why "the distribution of a transformed variable" is a modelling question, not just
  algebra: log-transforming a skewed variable changes what a mean means.

### Unit 4 — Expectation (3.5 h)

- Definition for discrete and continuous variables; why it is a weighted average.
- The law of the unconscious statistician: compute \(\E[g(X)]\) without finding the
  distribution of \(g(X)\).
- Linearity, proved from the definition for the discrete case.
- Indicator trick: \(\E[\text{number of successes}]=\sum \Pr(\text{success}_i)\),
  regardless of dependence — derived and used.
- Conditional expectation preview: \(\E[X\mid Y]\) as a random variable.
- When the expectation does not exist: Cauchy, and why this is not a technicality.

### Unit 5 — Variance and spread (2.5 h)

- Definition; derivation of \(\Var(X)=\E[X^2]-\E[X]^2\).
- Why variance is in squared units, and why the standard deviation exists.
- Rules: \(\Var(aX+b)=a^2\Var(X)\); \(\Var(X+c)=\Var(X)\).
- Variance of a sum, previewing covariance (proved in M11).
- Standard deviation as the natural scale; standardisation.

### Unit 6 — Moments and inequalities (2.5 h)

- Raw and central moments; skewness and kurtosis as standardised moments.
- Moment generating function: definition, existence conditions, and moment extraction
  by differentiation.
- MGF of a sum of independent variables is the product of MGFs — the tool behind M13.
- Markov's inequality: \(\Pr(X\ge a)\le \E[X]/a\) for non-negative \(X\).
- Chebyshev: \(\Pr(|X-\mu|\ge k\sigma)\le 1/k^2\).
- Jensen: \(\E[g(X)]\ge g(\E[X])\) for convex \(g\) — and its role in likelihood and
  information theory.

### Unit 7 — Simulation and verification (2 h)

- Sampling from a PMF/PDF with `scipy.stats.rvs`.
- Empirical mean and variance versus theory, with Monte Carlo error.
- Verifying a transformation numerically: simulate \(Y=g(X)\), compare with the
  derived density.
- Chebyshev checked empirically: the bound is loose but always true.

## Important mathematical concepts

**CDF and its inverse relationship with the density.**

\[ F_X(x)=\Pr(X\le x)=\int_{-\infty}^{x} f_X(t)\,dt,
   \qquad \frac{d}{dx}F_X(x)=f_X(x) \]

**Expectation and the LOTUS.**

\[ \E[X]=\sum_x x\,p_X(x) \quad\text{or}\quad \int_{-\infty}^{\infty} x\,f_X(x)\,dx,
   \qquad \E[g(X)]=\sum_x g(x)p_X(x) \]

**Variance, two forms.**

\[ \Var(X)=\E\left[(X-\E[X])^2\right]=\E[X^2]-\left(\E[X]\right)^2 \]

**Chebyshev's inequality.**

\[ \Pr\big(|X-\mu|\ge k\sigma\big)\le \frac{1}{k^{2}} \qquad (k>0) \]

*In words:* at least \(1-1/k^2\) of any distribution's mass lies within \(k\) standard
deviations of its mean — for \(k=2\), at least 75%, whatever the shape.

**MGF of a sum** (independence required):

\[ M_{X+Y}(t)=M_X(t)\,M_Y(t) \]

## Expected knowledge after completion

You can, without notes:

- Verify that \(f(x)=cx(1-x)\) on \([0,1]\) is a density and find \(c\).
- Go from a density to a CDF to an interval probability and back.
- Derive the density of \(Y=X^2\) for standard normal \(X\).
- Compute \(\E[X]\) and \(\Var(X)\) for a distribution given only its PMF table.
- Compute the expected number of fixed points in a random permutation using
  indicators, without any distribution of the count.
- State Chebyshev and use it to bound the probability of a large deviation.

## Connections to Data Science

- **Loss functions are expectations**: MSE is \(\E[(Y-\hat{Y})^2]\), decomposed into
  bias and variance.
- **Indicators** underlie every counting argument in feature engineering and evaluation
  (expected number of errors, expected overlap).
- **Chebyshev** justifies why a standardised score of 4 is unusual regardless of the
  distribution, and why z-score outlier rules are heuristics, not laws.
- **MGFs** are the technical route to the CLT, and the same exponential-family
  structure powers logistic regression.
- **Log-transformations** are Unit 3 in practice: they change the meaning of every
  subsequent mean.

## Practical applications

| Setting | Question | Method |
|---|---|---|
| Insurance | Expected claim cost per policy? | Expectation of a compound variable |
| Manufacturing | Expected number of defects per batch? | Indicators and linearity |
| Scoring | Is this z-score unusual? | Chebyshev versus normal reference |
| Feature engineering | Effect of a log transform on the mean? | Transformation of variables |
| Simulation design | How variable is my estimate? | Variance of a sample mean (preview of M12) |

## Exercises and assessment plan

| Component | Count | Focus |
|---|---|---|
| ★ Drill | 10 | PMF/PDF/CDF conversions, expectations |
| ★★ Application | 8 | Transformations; indicator arguments; variance rules |
| ★★★ Challenge | 4 | Derive a non-monotone transformation; prove linearity; Chebyshev bound; MGF of a sum |
| Quiz | 10 items | Representation fluency and inequality conditions |
| Practical notebook | 1 | Simulate, derive and compare for three distributions |
| Simulation lab | 1 | Transformation of a variable: derived versus simulated |

## Recommended study sequence

| Session | Focus | Hours |
|---|---|---|
| 1 | Units 1–2: variables, PMF/PDF/CDF | 3.5 |
| 2 | Unit 3: transformations | 3.0 |
| 3 | Unit 4: expectation and indicators | 3.5 |
| 4 | Unit 5: variance | 2.5 |
| 5 | Unit 6: moments and inequalities | 2.5 |
| 6 | Unit 7: simulation and exercises | 1.0 |

**Before this module:** [M07](07-conditional-probability-and-bayes.md). **After:**
[M09 — Discrete Distributions](09-discrete-distributions.md) applies expectation to
the named families you will actually use.
