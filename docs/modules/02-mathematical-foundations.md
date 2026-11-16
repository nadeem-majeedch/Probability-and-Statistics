---
title: "M02 — Mathematical Foundations for Statistics"
description: Sets, functions, summation, limits, derivatives, integrals, series and matrices — exactly the mathematics the rest of the course uses.
module: 2
part: 1
level: Beginner
hours: 12
prerequisites: [1]
---

# M02 · Mathematical Foundations for Statistics

<div class="psds-meta" markdown>
<span class="psds-chip psds-chip--beginner">Beginner</span>
<span class="psds-chip">Part I · Foundations</span>
<span class="psds-chip">12 study hours</span>
<span class="psds-chip">Module 2 of 18</span>
</div>

## Introduction

This is not a calculus course. It is the specific subset of mathematics that
statistics actually uses, rebuilt at exactly the depth the later modules require —
no more, and no less.

Two ideas organise it. The first is **notation**: statistics is written in sums,
products and functions, and a student who cannot read \(\sum_{i=1}^{n} x_i^2\)
fluently is locked out of every formula in Part III. The second is **the two
operations that turn distributions into numbers**: differentiation, which recovers a
density from a cumulative distribution, and integration, which accumulates
probability over an interval. Roughly 80% of the technical work in Modules 08–14 is
one of those two operations, done carefully.

If your calculus is rusty, this is the module that fixes it. If it is strong, take
the diagnostic at the start and skip to the units you fail.

## Why this matters

Three concrete dependencies, so you can see the stakes:

\[ \Pr(a < X < b) = \int_a^b f(x)\,dx \qquad
   f(x) = \frac{d}{dx}F(x) \qquad
   \Var(X) = \sum_{x} (x-\mu)^2 p(x) \]

The first is a probability (M10). The second recovers a density from a CDF (M08).
The third is a variance (M08). Without integration, the first is a picture; without
differentiation, the second is a definition you cannot use; without summation, the
third is a word.

The same applies later: the normalising constant of a density, the likelihood you
maximise in M14, and the log-likelihood you differentiate are all this module's
material with statistical meaning attached.

## Learning objectives

By the end of this module you can:

1. Use set notation and operations — union, intersection, complement, difference,
   Cartesian product, power set — and read set-builder notation.
2. Recognise a function, state its domain and range, and form compositions and
   inverses; distinguish injective, surjective and bijective maps.
3. Evaluate and manipulate sums and products, including double sums, index shifts,
   and the linearity and splitting rules.
4. Work fluently with exponents, logarithms, factorials and binomial coefficients,
   including the log-scale reasoning used for likelihoods.
5. Evaluate limits, identify discontinuities, and use continuity to justify taking a
   limit inside a function.
6. Differentiate using the power, product, quotient and chain rules, and interpret a
   derivative as a rate of change.
7. Integrate using standard forms, substitution and integration by parts; interpret a
   definite integral as area and as accumulated probability.
8. Recognise and sum arithmetic and geometric series, state convergence conditions,
   and use a first-order Taylor expansion for approximation.
9. Perform basic matrix operations, compute a determinant and an inverse for 2×2 and
   3×3 cases, and read a matrix equation as a system.
10. Use inequalities — including the triangle inequality and Jensen's inequality in
    preview — to bound quantities.

## Prerequisites

| Need | From | Revise before |
|---|---|---|
| Statistical vocabulary (population, sample, statistic) | [M01](01-introduction-to-statistics.md) | Unit 1 of this module |
| Arithmetic with fractions and percentages | school | Unit 4 |
| Reading a formula aloud | school | anywhere |

## Topic breakdown

### Unit 1 — Sets and logic (1 h)

- Sets, elements, subset, equality; set-builder notation \(\{x : x > 0\}\).
- Union, intersection, complement, difference, symmetric difference.
- Cartesian product; power set and its size \(2^{n}\).
- De Morgan's laws, and why they reappear verbatim as probability rules in M06.
- Quantifiers: "for all" and "there exists"; reading a definition without ambiguity.

### Unit 2 — Functions (1.5 h)

- A function as a rule with a domain: \(f: A \to B\).
- Domain, codomain, range; restrictions and piecewise definitions.
- Composition \(f \circ g\), inverse \(f^{-1}\), and when an inverse exists.
- Injective, surjective, bijective; monotonicity.
- Why the CDF must be non-decreasing (M08) and why a monotone transformation
  preserves order (M11).

### Unit 3 — Summation and product notation (2 h)

- \(\sum_{i=1}^{n} x_i\), the index, the limits, the summand.
- Constants, linearity: \(\sum (a x_i + b) = a\sum x_i + nb\).
- Splitting a sum; changing the index; reversing the order.
- Double sums \(\sum_i \sum_j x_{ij}\) and when the order can be exchanged.
- Product notation \(\prod\) and the log trick: \(\log \prod x_i = \sum \log x_i\).
- **Statistical payoff:** every mean, variance, covariance and likelihood is a sum.

### Unit 4 — Exponents, logarithms and factorials (1.5 h)

- Exponent rules; \(e^{x}\) and its derivative; exponential growth and decay.
- Logarithms as inverses; \(\log(ab) = \log a + \log b\); change of base.
- Log scale: why a variable spanning orders of magnitude is analysed on a log scale,
  and how to interpret a difference on a log scale as a ratio.
- Factorials and their growth; Stirling's approximation (stated).
- Binomial coefficients \(\binom{n}{k}\), Pascal's rule, and their role in M05.

### Unit 5 — Limits and continuity (1 h)

- Limits from the left and right; one-sided limits; infinite limits.
- Continuous functions; removable and jump discontinuities.
- Limits of sequences; \(\lim_{n\to\infty} a_n = L\).
- Why \(\lim_{n \to \infty} (1 + x/n)^n = e^{x}\) matters (it proves the CLT in the
  MGF case, M13).
- Continuity from the right as a CDF property (M08).

### Unit 6 — Differentiation (2 h)

- Derivative as a limit, and as a slope; notation \(f'(x)\), \(dy/dx\).
- Power, constant, sum, product, quotient and **chain** rules.
- Derivatives of \(e^{x}\), \(\ln x\), \(x^{n}\), and simple compositions.
- Second derivative; concavity and convexity.
- **Statistical payoff:** the derivative of a log-likelihood is the score function
  (M14); setting it to zero gives maximum-likelihood estimates.

### Unit 7 — Integration (2 h)

- Antiderivatives and the indefinite integral; the constant of integration.
- Definite integral as signed area; the fundamental theorem.
- Standard forms: powers, \(e^{x}\), \(1/x\).
- Substitution; integration by parts.
- Improper integrals and convergence — essential for heavy-tailed distributions.
- **Statistical payoff:** normalisation of densities, probabilities as areas,
  expectation of a continuous variable (M08, M10).

### Unit 8 — Sequences and series (1 h)

- Arithmetic and geometric series; sum and convergence condition \(|r| < 1\).
- Infinite series: partial sums, convergence, divergence.
- Taylor expansion about a point; first-order approximation
  \(f(x) \approx f(a) + f'(a)(x-a)\).
- Why the geometric series is the engine behind the geometric distribution (M09)
  and the Poisson limit (M09).
- The exponential series and its use in the CLT proof.

### Unit 9 — Matrices and linear algebra (1 h)

- Vectors, matrices, dimensions; addition, scalar multiplication, multiplication.
- Transpose; identity; inverse; determinant of 2×2 and 3×3.
- Matrix form of a linear system: \(X\beta = y\).
- Why least squares solves \((X^{\top}X)^{-1}X^{\top}y\) (M16), and what
  singularity means for a regression.

## Important mathematical concepts

**Linearity of summation.** The single most-used identity in the course:

\[ \sum_{i=1}^{n}(a x_i + b) \;=\; a\sum_{i=1}^{n} x_i \;+\; n b \]

**Geometric series.** Converges exactly when \(|r|<1\):

\[ \sum_{k=0}^{\infty} r^{k} = \frac{1}{1-r} \]

**Derivative of a log-likelihood.** The step that produces every estimator in M14:

\[ \frac{d}{d\theta}\ell(\theta) = 0 \quad\Longrightarrow\quad \hat{\theta} \]

**Probability as an integral.** The bridge from M02 to M10:

\[ \Pr(a \le X \le b) = \int_{a}^{b} f(x)\,dx \]

*In words:* probability is the area under the density curve between the two limits.

## Expected knowledge after completion

You can, without notes:

- Expand and simplify a double sum, and justify swapping its order.
- Differentiate a product of three functions and a nested composition.
- Integrate \(x e^{-x}\), \(\frac{1}{1+x}\), and a density over \([0,\infty)\).
- Explain why \(\int_{-\infty}^{\infty} f(x)dx = 1\) is a requirement, not a result.
- Sum an infinite geometric series and state when it diverges.
- Write a regression model in matrix form and say what \((X^{\top}X)^{-1}\) requires.

## Connections to Data Science

- **Log-scale thinking** underpins cross-entropy loss, log-likelihood maximisation and
  the interpretation of coefficients in a log-linear model.
- **Derivatives** are gradients: every gradient-descent step is Unit 6 applied to a
  loss function.
- **Matrices** are how data is actually represented: an \(n \times p\) design matrix
  is a dataset, and its rank determines whether a model is identifiable.
- **Series** explain why algorithms converge, and when they do not.
- **Numerical care** starts here: floating-point cancellation in a variance
  computation is a real failure mode.

## Practical applications

| Setting | Mathematics used |
|---|---|
| Computing a variance in one pass | Algebraically equivalent formulas differ in numerical stability |
| Modelling count data with an offset | Log scale and exponentials |
| Fitting a logistic regression | Chain rule on a log-likelihood |
| Reading a coefficient table with \(p\) predictors | Matrix algebra and rank |
| Detecting a heavy-tailed variable | Improper integrals that diverge |

## Exercises and assessment plan

| Component | Count | Focus |
|---|---|---|
| ★ Drill | 10 | Sums, derivatives, integrals, series |
| ★★ Application | 6 | Set up and evaluate the mathematics of a statistical expression |
| ★★★ Challenge | 3 | Prove an identity; derive a density normalisation; show a series diverges |
| Diagnostic self-test | 20 items | Placement: score ≥ 80% and move to M03 |
| Practical | 1 notebook | Verify every hand computation symbolically with `sympy` |

**Mastery threshold:** 80% on the diagnostic. This module is the one place where
"nearly right" is not acceptable, because every later module compounds it.

## Recommended study sequence

| Session | Focus | Hours |
|---|---|---|
| 1 | Units 1–2: sets and functions | 2.0 |
| 2 | Units 3–4: summation, logs, factorials | 2.5 |
| 3 | Unit 5–6: limits and differentiation | 2.5 |
| 4 | Unit 7: integration | 2.5 |
| 5 | Units 8–9: series and matrices | 2.0 |
| 6 | Diagnostic, exercises, `sympy` verification | 0.5 |

**Before this module:** [M01](01-introduction-to-statistics.md). **After:**
[M03 — Data and Descriptive Statistics](03-data-and-descriptive-statistics.md) uses
the summation notation established here on real data.
