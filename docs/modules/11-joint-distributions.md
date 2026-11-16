---
title: "M11 — Joint Probability Distributions"
description: "Two variables at once: marginals, conditionals, convolution, order statistics, covariance and conditional expectation."
module: 11
part: 3
level: Advanced
hours: 14
prerequisites: [9, 10]
---

# M11 · Joint Probability Distributions

<div class="psds-meta" markdown>
<span class="psds-chip psds-chip--advanced">Advanced</span>
<span class="psds-chip">Part III · Random variables</span>
<span class="psds-chip">14 study hours</span>
<span class="psds-chip">Module 11 of 18</span>
</div>

## Introduction

Real data has more than one column. A joint distribution describes several variables
together and encodes something a list of marginals cannot: **how they move
together**.

This module is the gateway to everything multivariate in the course. Covariance and
correlation are defined here, which makes regression (M16) possible. Conditional
expectation is defined here, which makes the law of total variance — the engine behind
ANOVA (M17), shrinkage (M18) and regression's \(R^2\) — available. Convolution is
defined here, which explains why sums of random variables have the distributions they
do, and therefore why the CLT (M13) is true.

It is marked Advanced for one reason: the two-variable calculus is genuinely harder
than the one-variable case. You must integrate over regions, choose the order of
integration, and keep track of supports. That is a skill, and it is learned by doing
the exercises, not by reading.

## Why this matters

Three ideas from this module do most of the work later.

**Covariance is shared variation.** It is the numerator of every correlation, the
core of every regression coefficient, and the reason a portfolio of correlated assets
is riskier than its parts suggest.

**Marginals do not determine the joint.** Two variables can each be standard normal
and still be wildly different jointly. Any model that claims to describe a dataset by
its column-wise summaries is making an assumption it cannot check.

**Conditional expectation is a projection.** \(\E[Y\mid X]\) is the best
mean-squared-error predictor of \(Y\) from \(X\) — which is precisely what a
regression estimates. This module is where "prediction" becomes a mathematical
statement.

## Learning objectives

By the end of this module you can:

1. Describe a bivariate distribution by its joint PMF/PDF and joint CDF, and verify
   normalisation.
2. Compute marginal distributions by summation or integration.
3. Compute conditional distributions and conditional expectations from a joint law.
4. Test independence from factorisation and from the shape of the support.
5. Apply the bivariate transformation technique with a Jacobian, and derive the
   distribution of a sum by convolution.
6. Derive the distributions of maxima and minima of \(n\) independent variables.
7. Define and compute covariance; prove the Cauchy–Schwarz inequality and hence
   \(|\rho|\le 1\).
8. State the variance of a sum with and without independence, and use indicator
   decompositions.
9. Apply the law of total expectation and the law of total variance.
10. Recognise the multivariate normal, its covariance matrix, and the fact that linear
    combinations remain normal.
11. Construct a pair of variables with strong dependence and zero correlation, and
    explain why the reverse claim (independence from zero correlation) is only valid
    for jointly normal variables.

## Prerequisites

| Need | From | Revise before |
|---|---|---|
| PMF, PDF, CDF, transformations | [M08](08-random-variables-and-expectation.md) | Units 2–3 |
| Variance algebra | M08 | Unit 5 |
| Discrete families (marginals by summation) | [M09](09-discrete-distributions.md) | — |
| Continuous families and integration | [M10](10-continuous-distributions.md) | Units 1–4 |
| Double sums, iterated integrals | [M02](02-mathematical-foundations.md) | Units 3, 7 |

## Topic breakdown

### Unit 1 — Joint laws (2.5 h)

- Joint PMF for discrete pairs; the table as the object of study.
- Joint PDF for continuous pairs; \(f(x,y)\) as a density over the plane.
- Joint CDF \(F(x,y)=\Pr(X\le x, Y\le y)\); mixed partial derivatives.
- Support as a region, and why drawing it prevents most integration errors.
- Normalisation: the double sum or double integral must equal 1.

### Unit 2 — Marginals and conditionals (3 h)

- Marginals by summing or integrating out the other variable.
- Conditional PMF/PDF: \(f_{Y\mid X}(y\mid x)=f(x,y)/f_X(x)\).
- Conditional expectation \(\E[Y\mid X=x]\) as a function of \(x\), and
  \(\E[Y\mid X]\) as a random variable.
- Conditional variance.
- Reading a joint table: row percentages versus column percentages.
- **Key structural fact:** marginals do not determine the joint; construct two joints
  with identical marginals and different dependence.

### Unit 3 — Independence in two dimensions (1.5 h)

- Factorisation \(f(x,y)=f_X(x)f_Y(y)\); support must be a product set.
- Why a triangular support implies dependence immediately.
- Independence implies zero covariance; the converse fails except under joint
  normality.
- Independence and conditional independence, revisited from M07 in distributional form.

### Unit 4 — Transformations and convolution (3 h)

- Bivariate transformation: Jacobian determinant, change of variables.
- Distribution of a sum: convolution
  \(f_{X+Y}(z)=\int f_X(x)f_Y(z-x)\,dx\).
- Sums of Poissons, normals, gammas — the closure properties that matter later.
- Distribution of \(X+Y\) when the supports are bounded (the triangular shape).
- Order statistics: \(F_{\max}=F^{n}\), \(F_{\min}=1-(1-F)^{n}\), and their densities.
- Worked derivation: maximum of \(n\) uniforms; minimum of \(n\) exponentials.

### Unit 5 — Covariance and correlation (2.5 h)

- Definition \(\Cov(X,Y)=\E[(X-\mu_X)(Y-\mu_Y)]\), and the shortcut form.
- Bilinearity; \(\Var(X+Y)\) with the covariance term.
- Correlation \(\rho=\Cov/(\sigma_X\sigma_Y)\); scale-free; bounded by Cauchy–Schwarz.
- What \(\rho\) measures (linear association) and what it does not.
- The counterexample: \(Y=X^2\) with symmetric \(X\) gives \(\rho=0\) and perfect
  dependence.
- Covariance matrices; positive semi-definiteness as a consistency requirement.

### Unit 6 — Conditional expectation and the two laws (1.5 h)

- Tower property: \(\E[Y]=\E[\E[Y\mid X]]\).
- Law of total variance:
  \(\Var(Y)=\E[\Var(Y\mid X)]+\Var(\E[Y\mid X])\).
- Interpretation: within-group plus between-group variation — the identity behind
  ANOVA (M17) and \(R^2\) (M16).
- Conditional expectation as the best MSE predictor: a preview of regression.

### Unit 7 — The multivariate normal (1 h)

- Density in matrix form; mean vector and covariance matrix.
- Linear combinations are normal; marginals are normal; conditional distributions are
  normal with a variance that shrinks as correlation rises.
- Zero correlation *does* imply independence in this family — the exception that
  proves the rule.
- Simulation with `numpy.random.multivariate_normal`; contour plots.

## Important mathematical concepts

**Marginal from a joint density.**

\[ f_X(x)=\int_{-\infty}^{\infty} f(x,y)\,dy \]

**Convolution.**

\[ f_{X+Y}(z)=\int_{-\infty}^{\infty} f_X(x)\,f_Y(z-x)\,dx \]

**Covariance and correlation.**

\[ \Cov(X,Y)=\E[XY]-\E[X]\E[Y], \qquad
   \rho=\frac{\Cov(X,Y)}{\sigma_X\sigma_Y}, \qquad |\rho|\le 1 \]

**Variance of a sum.**

\[ \Var(X+Y)=\Var(X)+\Var(Y)+2\Cov(X,Y) \]

**Law of total variance.**

\[ \Var(Y)=\underbrace{\E\big[\Var(Y\mid X)\big]}_{\text{within}}
   +\underbrace{\Var\big(\E[Y\mid X]\big)}_{\text{between}} \]

*In words:* total variation is what remains unexplained inside groups plus the
variation explained by the group means — which is exactly the ANOVA decomposition.

## Expected knowledge after completion

You can, without notes:

- Integrate a joint density over a specified region, drawing the support first.
- Compute a marginal, a conditional density and a conditional expectation from a joint
  law.
- Derive the density of a sum of two uniforms and explain the triangular shape.
- Derive the density of the maximum of \(n\) uniforms.
- Compute covariance from a joint table by hand and check it with `numpy.cov`.
- State the law of total variance and explain each term.

## Connections to Data Science

- **Regression coefficients** are covariances divided by variances: \(\beta_1 =
  \Cov(X,Y)/\Var(X)\) is this module (M16).
- **\(R^2\)** is the between-group share of total variance — the law of total variance
  in disguise.
- **Feature dependence** invalidates naive independence assumptions and motivates
  dimensionality reduction.
- **Gaussian processes and Kalman filters** are multivariate normal conditioning.
- **Portfolio risk** is variance of a weighted sum with covariances.

## Practical applications

| Setting | Question | Concept |
|---|---|---|
| Portfolio | Risk of two correlated assets? | Variance of a sum |
| Two-item order | Probability both arrive within 5 days? | Joint CDF |
| Survey | Does satisfaction depend on tenure? | Conditional distribution |
| Queue | Distribution of total service time? | Convolution |
| Auctions | Expected highest of \(n\) bids? | Order statistics |

## Exercises and assessment plan

| Component | Count | Focus |
|---|---|---|
| ★ Drill | 6 | Marginals and covariance from tables |
| ★★ Application | 6 | Conditionals, convolution, order statistics |
| ★★★ Challenge | 4 | Non-independence from marginals; zero-correlation dependence; total variance proof; Jacobian transformation |
| Quiz | 10 items | Structure and interpretation |
| Practical notebook | 1 | Bivariate normal simulation, marginals, conditionals, contours |
| Simulation lab | 1 | Convolution and order statistics verified numerically |

## Recommended study sequence

| Session | Focus | Hours |
|---|---|---|
| 1 | Unit 1: joint laws and supports | 2.5 |
| 2 | Unit 2: marginals and conditionals | 3.0 |
| 3 | Unit 3: independence | 1.5 |
| 4 | Unit 4: transformations and convolution | 3.0 |
| 5 | Unit 5: covariance and correlation | 2.5 |
| 6 | Units 6–7: total variance, multivariate normal | 1.5 |

**Before this module:** [M10](10-continuous-distributions.md). **After:**
[M12 — Sampling and Sampling Distributions](12-sampling-and-sampling-distributions.md)
applies these tools to the distribution of a statistic, where inference begins.
