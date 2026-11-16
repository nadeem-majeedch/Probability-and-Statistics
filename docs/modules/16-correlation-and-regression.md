---
title: "M16 — Correlation and Regression"
description: Measuring association, fitting lines by least squares, and diagnosing whether a model can be believed.
module: 16
part: 6
level: Core
hours: 18
prerequisites: [11, 14, 15]
---

# M16 · Correlation and Regression

<div class="psds-meta" markdown>
<span class="psds-chip psds-chip--core">Core</span>
<span class="psds-chip">Part VI · Relationships and modelling</span>
<span class="psds-chip">18 study hours</span>
<span class="psds-chip">Module 16 of 18</span>
</div>

## Introduction

Most applied statistics asks how one variable relates to another. Correlation measures
association; regression models it. Both are simple to compute and easy to misuse, and
the gap between a fitted model and a defensible one is almost entirely in the
diagnostics.

This module therefore spends as much time on checking as on fitting. A regression is a
claim: that the relationship is linear, that the errors are independent with constant
variance, that no small subset of points is driving the result, and that the
predictors are not redundant. Every one of those is testable, and most are visual.

Two ideas need care because they are widely mishandled. **Correlation is not
causation** — a phrase so familiar that it has stopped doing work; the module supplies
the mechanisms (confounding, reverse causation, selection) that make the warning
concrete. And **a coefficient is not an effect** unless the design supports that
reading; multiple regression gives you a *partial* association, holding other
predictors fixed, which is a different quantity from the marginal one.

## Why this matters

Regression is the workhorse of applied analytics: pricing models, risk scores, demand
forecasts, treatment-effect estimates. It is also the model behind ANOVA (M17), the
baseline against which machine-learning models are judged, and the source of the
coefficient tables that fill applied papers.

Getting it wrong is expensive in a specific way: the model still fits, the R² still
looks respectable, and the conclusion is still wrong. Diagnostics are the only defence.

## Learning objectives

By the end of this module you can:

1. Compute and interpret Pearson's r, including its relation to the regression slope
   and to \(R^2\).
2. Test \(H_0:\rho=0\) and construct an interval via Fisher's z-transformation.
3. Compute Spearman's \(\rho\) and Kendall's \(\tau\), and choose the right measure for
   each variable-type pair.
4. Construct and read a correlation matrix, including the multiplicity hazard of
   scanning many correlations.
5. Explain confounding, reverse causation and selection, and name the design that would
   establish causation.
6. Specify the simple linear model and derive the least-squares estimators.
7. Interpret slope, intercept, \(R^2\), residual standard error and the F statistic.
8. Construct confidence and prediction intervals and explain why they differ.
9. Check the four assumptions with residual plots, Q–Q plots and scale–location plots,
   and name a remedy for each failure.
10. Identify leverage, influence and outliers with the appropriate diagnostics.
11. Write and interpret a multiple regression with categorical predictors and
    interactions; diagnose multicollinearity with VIF.
12. Compare nested models with partial F tests and non-nested models with AIC/BIC and
    adjusted \(R^2\).

## Prerequisites

| Need | From | Revise before |
|---|---|---|
| Covariance, correlation, conditional expectation | [M11](11-joint-distributions.md) | Unit 5 |
| t tests, intervals, p-values | [M14](14-estimation-and-confidence-intervals.md), [M15](15-hypothesis-testing.md) | — |
| Residual and scatter thinking | [M04](04-data-visualization.md) | Units 3–4 |
| Matrix algebra (for the multiple case) | [M02](02-mathematical-foundations.md) | Unit 9 |

## Topic breakdown

### Unit 1 — Measuring association (3 h)

- Pearson's r: definition as standardised covariance; range and interpretation.
- r as the slope of the standardised regression; \(R^2=r^2\) in the simple case.
- Sensitivity: outlier, restriction of range, non-linearity.
- Inference: \(H_0:\rho=0\); Fisher's \(z=\operatorname{artanh} r\) with standard error
  \(1/\sqrt{n-3}\); the interval.
- Rank measures: Spearman's \(\rho\), Kendall's \(\tau\); when ranks are the right
  scale.
- Categorical association: point-biserial, phi, Cramér's V (computed in M17).
- Reading a correlation matrix honestly: multiplicity and the diagonal.

### Unit 2 — Association versus causation (2 h)

- Confounding, with a concrete numeric example where the marginal and conditional
  associations differ in sign.
- Reverse causation and simultaneity.
- Selection and collider bias, briefly.
- What establishes causation: randomisation, or a defensible identification strategy.
- Simpson's paradox revisited in continuous data.
- Language discipline: "associated with" versus "causes".

### Unit 3 — Simple linear regression (4 h)

- Model: \(Y=\beta_0+\beta_1x+\varepsilon\) with assumptions stated once, clearly.
- Least squares as minimisation; derivation of \(\hat\beta_1=S_{xy}/S_{xx}\) and
  \(\hat\beta_0=\bar y-\hat\beta_1\bar x\).
- Geometric reading: projection of the response vector onto the space spanned by the
  predictor.
- Fitted values, residuals, and the decomposition SST = SSR + SSE.
- \(R^2\) as explained variance; the residual standard error \(\hat\sigma\).
- Inference: t test on the slope, its equivalence to the F test and to the correlation
  test.
- Prediction interval versus confidence band; why the former is much wider.
- Extrapolation and its dangers.

### Unit 4 — Diagnostics (3 h)

- Linearity: residual versus fitted; partial residual plots.
- Independence: residual versus order/time; Durbin–Watson idea.
- Homoscedasticity: scale–location plot; what funnel shapes mean.
- Normality: Q–Q of residuals, and why it matters least for large \(n\) but most for
  prediction intervals.
- Leverage (hat values), influence (Cook's distance, DFBETAS), and outliers
  (studentised residuals) — three distinct concepts.
- Remedies: transformation, weighted least squares, robust standard errors, model
  respecification.
- A diagnostic protocol: what to check, in what order, and what to do about each
  finding.

### Unit 5 — Multiple regression (4 h)

- Matrix form: \(y=X\beta+\varepsilon\); \(\hat\beta=(X^{\top}X)^{-1}X^{\top}y\).
- Partial coefficients: the effect of one predictor holding others fixed — derived
  from the residual-on-residual regression.
- Dummy coding and reference categories; interpreting intercepts.
- Interactions: what a product term means, and how to read a main effect in the
  presence of an interaction.
- Multicollinearity: VIF, its effect on standard errors, and why dropping a variable
  changes the question rather than fixing the problem.
- Omitted-variable bias: direction of the bias from an omitted confounder.
- Adjusted \(R^2\), AIC/BIC, partial F tests, and the discipline of pre-specifying
  predictors.
- Prediction versus explanation: two different goals with different diagnostics.

### Unit 6 — Reporting and reproducibility (2 h)

- A model table that someone can read: coefficients, intervals, diagnostics, \(n\).
- Reporting assumptions checked, not assumed.
- Reproducible pipeline: same data, same seed, same numbers.
- Presenting a model to a non-specialist: what to say about uncertainty and limits.

## Important mathematical concepts

**Correlation.**

\[ r=\frac{\sum (x_i-\bar x)(y_i-\bar y)}
        {\sqrt{\sum (x_i-\bar x)^{2}}\;\sqrt{\sum (y_i-\bar y)^{2}}},
   \qquad r^{2}=R^{2}\ \text{(simple regression)} \]

**Least-squares slope and intercept.**

\[ \hat\beta_1=\frac{S_{xy}}{S_{xx}}, \qquad \hat\beta_0=\bar y-\hat\beta_1\bar x, \qquad
   \Var(\hat\beta_1)=\frac{\sigma^{2}}{S_{xx}} \]

**Decomposition of variation.**

\[ \underbrace{\sum (y_i-\bar y)^{2}}_{\text{SST}}
   =\underbrace{\sum (\hat y_i-\bar y)^{2}}_{\text{SSR}}
   +\underbrace{\sum (y_i-\hat y_i)^{2}}_{\text{SSE}} \]

**Multiple regression estimator.**

\[ \hat\beta=(X^{\top}X)^{-1}X^{\top}y, \qquad
   \Var(\hat\beta)=\sigma^{2}(X^{\top}X)^{-1} \]

**Variance inflation.**

\[ \mathrm{VIF}_j=\frac{1}{1-R_j^{2}} \]

*In words:* if predictor \(j\) can be well predicted by the others, its coefficient is
estimated imprecisely — the standard error inflates by \(\sqrt{\mathrm{VIF}}\).

## Expected knowledge after completion

You can, without notes:

- Derive the least-squares slope by differentiating the residual sum of squares.
- Read a `statsmodels` summary line by line without skipping anything.
- Identify heteroscedasticity from a residual plot and name two remedies.
- Explain why a prediction interval is wider than a confidence interval for the mean
  response.
- Explain a sign reversal between simple and multiple regression using an omitted
  variable.
- Distinguish an outlier, a high-leverage point and an influential point.

## Connections to Data Science

- **Feature importance** is not coefficient size when predictors are correlated.
- **Regularisation** (ridge, lasso) is the answer to multicollinearity and
  high-dimensionality; ridge shrinks exactly the directions where \(X^{\top}X\) is
  nearly singular.
- **Model evaluation**: in-sample \(R^2\) is optimistic; held-out error is the honest
  measure.
- **Causal inference** starts by asking whether the regression coefficient is a causal
  effect at all.
- **Explainable ML** borrows partial dependence and coefficient-style interpretations
  from here.

## Practical applications

| Setting | Question | Method |
|---|---|---|
| Student performance | Does study time predict marks? | Simple regression with diagnostics |
| House prices | Effect of size holding location fixed? | Multiple regression with dummies |
| Marketing | Which channels matter? | Regression with collinearity check |
| Clinical | Does the biomarker track severity? | Correlation plus interval |
| Forecasting | Predicted value for a new case | Prediction interval, not confidence band |

## Exercises and assessment plan

| Component | Count | Focus |
|---|---|---|
| ★ Drill | 8 | Correlation, slope, \(R^2\) computation |
| ★★ Application | 8 | Full model with diagnostics and interpretation |
| ★★★ Challenge | 4 | Derive the OLS slope; sign reversal; collinearity simulation; influence analysis |
| Quiz | 10 items | Diagnostics and interpretation |
| Practical notebook | 1 | End-to-end regression: specification, diagnostics, report |
| Simulation lab | 1 | Correlation and regression explorer: drag a point, watch r and β̂ |

## Recommended study sequence

| Session | Focus | Hours |
|---|---|---|
| 1 | Unit 1: measuring association | 3.0 |
| 2 | Unit 2: association versus causation | 2.0 |
| 3 | Unit 3: simple linear regression | 4.0 |
| 4 | Unit 4: diagnostics | 3.0 |
| 5 | Unit 5: multiple regression | 4.0 |
| 6 | Unit 6: reporting | 2.0 |

**Before this module:** [M11](11-joint-distributions.md),
[M14](14-estimation-and-confidence-intervals.md),
[M15](15-hypothesis-testing.md). **After:** [M17 — ANOVA, Chi-Square and
Nonparametric Statistics](17-anova-chi-square-nonparametric.md).
