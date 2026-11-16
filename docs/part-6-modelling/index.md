---
title: Part VI — Relationships and Modelling
description: Correlation, simple and multiple regression, diagnostics and reporting. Module M16.
---

# Part VI — Relationships and Modelling

**Module M16 · 18 study hours · Core · Prerequisites: Parts I–V**

---

## Why this part exists

Most applied questions are about relationships: does this predict that, by how much, and
can we believe the answer? This part answers all three, and spends as much time on the
third as on the first two.

Correlation and regression are taught together because they are the same geometry seen
at two scales. The correlation coefficient is the slope of the regression of standardised
*y* on standardised *x*; the coefficient of determination is its square. Taught
separately, students memorise two formulas and miss that one is a rescaling of the other.

The diagnostics carry the weight. A regression always fits; the question is whether the
fit is a description of the data or an artefact of a violated assumption, a handful of
influential points, or a confounder that was never measured.

## Module

| # | Module | Level | Hours | Focus |
|---|---|---|---|---|
| M16 | [Correlation and Regression](../modules/16-correlation-and-regression.md) | Core | 18 | Pearson and rank correlation, OLS derivation, inference, diagnostics, multiple regression, interactions, collinearity, reporting |

## What you will be able to do

- Derive the least-squares slope by differentiating the residual sum of squares.
- Interpret every line of a regression summary, including what each standard error is a
  standard error *of*.
- Diagnose non-linearity, heteroscedasticity, non-normal residuals, and influential
  points from plots, and name a remedy for each.
- Explain a sign reversal between simple and multiple regression via an omitted variable.
- Read a coefficient as a partial association, and say why that is not automatically a
  causal effect.
- Write a model report a non-specialist can act on.

## Simulation experiments in this part

Drag-a-point correlation explorer (r and β̂ respond live); heteroscedasticity and its
effect on standard errors; the effect of an influential point on the fitted line;
collinearity inflating standard errors as a function of VIF.

## Common misconceptions this part removes

| Misconception | Corrected in |
|---|---|
| "Correlation implies causation" | M16 |
| "R² = 0.9 means the model is good" | M16 |
| "A high-leverage point is an outlier" | M16 |
| "Standard errors are about the data" | M16 |
| "Dropping a collinear variable fixes the problem" | M16 |
| "Prediction intervals and confidence bands are the same" | M16 |

## Start

Begin with [M16 — Correlation and Regression](../modules/16-correlation-and-regression.md).
If you have not yet met the F distribution, revisit [M12](../modules/12-sampling-and-sampling-distributions.md)
Unit 5 first.
