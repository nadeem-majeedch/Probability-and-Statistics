# Practical 16 — Correlation and Regression

## 1. Introduction

Correlation summarises how two variables move together; regression predicts one from the
other. Both are easy to run and easy to misread, so this practical spends as much time on
diagnostics and interpretation as on fitting.

You will fit a simple regression, read its coefficient table, check the four assumptions
with residual plots, extend to multiple regression, and measure multicollinearity. The
final section is the one that matters most: why none of this establishes causation.

## 2. Learning objectives

By the end of this practical you can:

1. Compute Pearson and Spearman correlations and say when each applies.
2. Fit and interpret a simple linear regression with `statsmodels`.
3. Read \(R^{2}\), the residual standard error and confidence intervals on coefficients.
4. Diagnose non-linearity, heteroscedasticity and influential points from residuals.
5. Detect multicollinearity with VIF, and explain why a coefficient is not a causal
   effect.

## 3. Required libraries

| Library | Used for |
|---|---|
| `numpy`, `pandas` | data handling |
| `statsmodels` | OLS with a full summary table, VIF, ANOVA |
| `scipy.stats` | Spearman, Pearson tests |
| `matplotlib`, `seaborn` | scatter, residual and Q–Q plots |

## 4. Concepts

### 4.1 Correlation

\[ r=\frac{\sum(x_i-\bar x)(y_i-\bar y)}
        {\sqrt{\sum(x_i-\bar x)^{2}}\sqrt{\sum(y_i-\bar y)^{2}}}\in[-1,1]. \]

Pearson measures **linear** association and is sensitive to outliers.
Spearman applies Pearson to ranks and measures **monotone** association; it is robust and
works for ordinal data.

### 4.2 The simple regression model

\[ y_i=\beta_0+\beta_1x_i+\varepsilon_i,\qquad
   \varepsilon_i\ \text{independent},\ \E[\varepsilon]=0,\ \Var(\varepsilon)=\sigma^{2}. \]

Least squares chooses \(\hat\beta_0,\hat\beta_1\) to minimise \(\sum(y_i-\hat y_i)^{2}\).
The solution is \(\hat\beta_1=S_{xy}/S_{xx}\) and \(\hat\beta_0=\bar y-\hat\beta_1\bar x\).

### 4.3 Inference and fit

\[ s_e=\sqrt{\frac{\text{SSE}}{n-2}},\qquad
   \se(\hat\beta_1)=\frac{s_e}{\sqrt{S_{xx}}},\qquad
   R^{2}=1-\frac{\text{SSE}}{\text{SST}}. \]

\(R^{2}\) is the share of variance in \(y\) explained by the linear fit. Adjusted
\(R^{2}\) penalises extra predictors:

\[ \bar R^{2}=1-(1-R^{2})\frac{n-1}{n-k-1}. \]

### 4.4 Assumptions and their diagnostics

| Assumption | Diagnostic | Failure |
|---|---|---|
| Linearity | residuals vs fitted | curvature |
| Independence | residuals vs order | runs, cycles |
| Constant variance | residuals vs fitted | funnel shape |
| Normality of errors | Q–Q plot | S-shape, heavy tails |

### 4.5 Multicollinearity

\[ \text{VIF}_j=\frac{1}{1-R_j^{2}}, \]

where \(R_j^{2}\) comes from regressing predictor \(j\) on the others. VIF above about 5
inflates standard errors by more than \(\sqrt5\approx2.2\).

### 4.6 Association is not causation

A coefficient is a partial association **in these data**. Confounding, reverse causation
and selection can all produce a large, precise coefficient with no causal relationship.
Only randomisation or a credible identification strategy supports "causes".

## 5. Formulas

\[ \hat\beta_1=\frac{S_{xy}}{S_{xx}},\qquad \hat\beta_0=\bar y-\hat\beta_1\bar x,\qquad
   t=\frac{\hat\beta_1}{\se(\hat\beta_1)}\sim t_{n-2} \]

\[ \text{prediction interval}=\hat y_0\pm t\,s_e
   \sqrt{1+\frac1n+\frac{(x_0-\bar x)^{2}}{S_{xx}}} \]

## 6. Implementation

### 6.1 Build data with a known relationship

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
rng = np.random.default_rng(2026)
n = 200

df = pd.DataFrame({
    "hours": np.clip(rng.gamma(4, 1.6, n), 0.5, 30),
    "attendance": np.clip(rng.normal(78, 11, n), 30, 100),
})
df["score"] = np.clip(38 + 1.7*df["hours"] + 0.18*df["attendance"]
                      + rng.normal(0, 6, n), 0, 100)
df["engagement"] = 0.8*df["hours"] + rng.normal(0, 1.2, n)   # collinear with hours

print(df.describe().round(2).to_string())
print("\ncorrelations with score:")
print(df.corr()["score"].round(3).to_string())
```

### 6.2 Pearson and Spearman

```python
pearson = stats.pearsonr(df["hours"], df["score"])
spearman = stats.spearmanr(df["hours"], df["score"])
print(f"Pearson  r = {pearson.statistic:.4f}, p = {pearson.pvalue:.2e}")
print(f"Spearman rho = {spearman.statistic:.4f}, p = {spearman.pvalue:.2e}")
print(f"r^2 = {pearson.statistic**2:.4f}")

# Effect of one contaminated point.
contaminated = df.copy()
contaminated.loc[0, "hours"] = 29.5
contaminated.loc[0, "score"] = 30.0
print(f"\nafter adding one outlier: Pearson {stats.pearsonr(contaminated['hours'], contaminated['score']).statistic:.4f}, "
      f"Spearman {stats.spearmanr(contaminated['hours'], contaminated['score']).statistic:.4f}")
```

### 6.3 Simple linear regression

```python
X = sm.add_constant(df["hours"])
model = sm.OLS(df["score"], X).fit()
print(model.summary().tables[1])
print(f"R^2 = {model.rsquared:.4f}, adjusted R^2 = {model.rsquared_adj:.4f}")
print(f"residual standard error = {np.sqrt(model.mse_resid):.4f}")
print(f"slope 95% CI = {model.conf_int().loc['hours'].round(3).tolist()}")
```

```python
# Prediction for a new student, with a prediction interval.
new = pd.DataFrame({"const": [1.0], "hours": [12.0]})
pred = model.get_prediction(new)
summary = pred.summary_frame(alpha=0.05)
print(summary[["mean", "mean_ci_lower", "mean_ci_upper",
               "obs_ci_lower", "obs_ci_upper"]].round(3).to_string())
```

The **mean** interval is for the average score of all students who study 12 hours; the
**obs** interval is for one new student. The second is much wider because it includes the
irreducible noise.

### 6.4 Residual diagnostics

```python
fitted = model.fittedvalues
resid = model.resid

fig, axes = plt.subplots(1, 3, figsize=(12.5, 3.4))
axes[0].scatter(df["hours"], df["score"], s=18, alpha=0.6, color="#4c72b0")
xs = np.linspace(df["hours"].min(), df["hours"].max(), 100)
axes[0].plot(xs, model.params["const"] + model.params["hours"]*xs,
             color="#c44e52", linewidth=2)
axes[0].set(title="Data and fitted line", xlabel="Hours", ylabel="Score")

axes[1].scatter(fitted, resid, s=18, alpha=0.6, color="#55a868")
axes[1].axhline(0, color="black", linewidth=1)
axes[1].set(title="Residuals vs fitted", xlabel="Fitted", ylabel="Residual")

stats.probplot(resid, dist="norm", plot=axes[2])
axes[2].set_title("Q-Q plot of residuals")
fig.tight_layout()
plt.show()

print(f"residual mean {resid.mean():+.2e}, sd {resid.std(ddof=1):.3f}")
print(f"residual skewness {stats.skew(resid):+.3f}, correlation with fitted {np.corrcoef(fitted, resid)[0,1]:+.3f}")
```

### 6.5 Multiple regression and adjusted \(R^{2}\)

```python
X2 = sm.add_constant(df[["hours", "attendance"]])
model2 = sm.OLS(df["score"], X2).fit()
print(model2.summary().tables[1])
print(f"R^2 = {model2.rsquared:.4f}, adjusted R^2 = {model2.rsquared_adj:.4f}")

# Adding a predictor that is pure noise should raise R^2 slightly but lower adjusted R^2.
noise = rng.normal(0, 1, n)
X3 = sm.add_constant(df[["hours", "attendance"]].assign(noise=noise))
model3 = sm.OLS(df["score"], X3).fit()
print(f"\nwith noise column: R^2 = {model3.rsquared:.4f}, "
      f"adjusted R^2 = {model3.rsquared_adj:.4f}")
```

### 6.6 Multicollinearity

```python
X_vif = sm.add_constant(df[["hours", "engagement"]])
vif = pd.Series(
    [variance_inflation_factor(X_vif.values, i) for i in range(X_vif.shape[1])],
    index=X_vif.columns,
)
print("VIF with hours and engagement:")
print(vif.round(2).to_string())

print(f"\ncorrelation(hours, engagement) = {df['hours'].corr(df['engagement']):.4f}")
print(f"standard error of hours coefficient in this model: "
      f"{sm.OLS(df['score'], X_vif).fit().bse['hours']:.4f}")
print(f"standard error of hours coefficient alone: "
      f"{model.bse['hours']:.4f}")
```

### 6.7 A non-linear relationship that linear regression mishandles

```python
x = np.linspace(0, 6, 120)
y = 10 + 2*x - 0.45*x**2 + rng.normal(0, 0.9, 120)
quad_df = pd.DataFrame({"x": x, "y": y})

linear_fit = sm.OLS(y, sm.add_constant(x)).fit()
Xq = sm.add_constant(np.column_stack([x, x**2]))
quad_fit = sm.OLS(y, Xq).fit()

print(f"linear model R^2 {linear_fit.rsquared:.4f}, residual sd {np.sqrt(linear_fit.mse_resid):.3f}")
print(f"quadratic R^2    {quad_fit.rsquared:.4f}, residual sd {np.sqrt(quad_fit.mse_resid):.3f}")

fig, axes = plt.subplots(1, 2, figsize=(10.5, 3.6))
axes[0].scatter(x, y, s=12, alpha=0.6, color="#4c72b0")
axes[0].plot(x, linear_fit.fittedvalues, color="#c44e52", label="linear")
axes[0].plot(x, quad_fit.fittedvalues, color="#55a868", label="quadratic")
axes[0].legend(frameon=False)
axes[0].set(title="A curve fitted with a line and a parabola",
            xlabel="x", ylabel="y")

axes[1].scatter(linear_fit.fittedvalues, linear_fit.resid, s=12, alpha=0.6,
                color="#c44e52")
axes[1].axhline(0, color="black", linewidth=1)
axes[1].set(title="Residuals from the linear fit show the curve",
            xlabel="fitted", ylabel="residual")
fig.tight_layout()
plt.show()
```

## 7. Output and interpretation

- **Correlations.** Hours correlate with score at about 0.6 and attendance at about 0.3;
  Pearson and Spearman agree closely, which is evidence the relationship is roughly
  linear and not driven by outliers. After moving one point to an extreme, Pearson falls
  while Spearman barely moves — the standard demonstration of robustness.
- **Simple regression.** The slope is about 1.7 marks per hour, with a narrow confidence
  interval, and the intercept is the predicted score at zero hours (an extrapolation, so
  interpret it cautiously). \(R^{2}\approx0.45\): hours explain less than half the
  variation, which is typical for educational data and is not a defect.
- **Prediction.** At 12 hours the fitted score is around 65. The mean interval is roughly
  \(\pm2\) marks, the prediction interval \(\pm15\): knowing the average is much easier
  than predicting an individual.
- **Residuals.** The residual plot shows no curvature and roughly constant spread; the
  Q–Q plot is close to a straight line. That is what a well-specified linear model looks
  like, and it is the check that justifies the inference.
- **Multiple regression.** Adding attendance raises \(R^{2}\) and adjusted \(R^{2}\), so it
  earns its place. Adding a noise column raises \(R^{2}\) trivially but lowers adjusted
  \(R^{2}\) — the adjustment's whole purpose.
- **Multicollinearity.** Hours and engagement have a correlation above 0.9 and VIF above
  5; the standard error of the hours coefficient roughly doubles compared with the model
  containing hours alone. The coefficient is still unbiased, but it is imprecise, and its
  sign can flip between samples.
- **Non-linearity.** The linear fit has a clear U-shaped residual pattern and a lower
  \(R^{2}\); the quadratic term removes the pattern. The residuals, not \(R^{2}\), tell you
  the model is wrong.

## 8. Visualisation

```python
fig, axes = plt.subplots(1, 2, figsize=(11, 4))

sns.regplot(data=df, x="hours", y="score", ax=axes[0],
            scatter_kws={"s": 18, "alpha": 0.55}, line_kws={"color": "#c44e52"})
axes[0].set(title=f"Score against hours (r = {df['hours'].corr(df['score']):.2f})",
            xlabel="Study hours per week", ylabel="Score")

sns.scatterplot(data=df, x="hours", y="engagement", ax=axes[1],
                s=18, alpha=0.55, color="#55a868")
axes[1].set(title=f"Two collinear predictors (r = {df['hours'].corr(df['engagement']):.2f})",
            xlabel="Hours", ylabel="Engagement score")
fig.tight_layout()
plt.show()
```

**What to look at.** The left panel shows a positive but noisy relationship: a fitted line
is useful, and the vertical spread around it is large. The right panel is the
multicollinearity picture — the points lie near a line, so the two predictors carry
almost the same information and the model cannot separate their effects.

## 9. Practical scenario

**Does tutoring raise marks?** A department compares students who attended optional
tutoring with those who did not, and finds a coefficient of +6 marks with \(p<0.001\).

```python
rng = np.random.default_rng(99)
n = 400
motivation = rng.normal(0, 1, n)
attended = (motivation + rng.normal(0, 0.8, n) > 0).astype(int)
score = 55 + 3*motivation + 4*attended + rng.normal(0, 8, n)

naive = sm.OLS(score, sm.add_constant(attended)).fit()
adjusted = sm.OLS(score, sm.add_constant(np.column_stack([attended, motivation]))).fit()

print(f"naive model:   tutoring coefficient {naive.params[1]:.2f} "
      f"(p = {naive.pvalues[1]:.2e})")
print(f"adjusted:      tutoring coefficient {adjusted.params[1]:.2f} "
      f"(p = {adjusted.pvalues[1]:.4f})")
print(f"true generating effect: 4.00")
```

The naive estimate is inflated because motivated students are both more likely to attend
and more likely to score well. Adjusting for motivation moves the estimate towards the
truth. The lesson is not "adjust for everything" — adjusting for a consequence of the
treatment would introduce a different bias — but that an unadjusted coefficient is a
description of a comparison, not an estimate of an effect.

## 10. Exercises

**Exercise 1.** Compute Pearson and Spearman correlations between `attendance` and
`score`, and compare them.

**Exercise 2.** Fit `score ~ attendance` alone and report the slope, its 95% interval and
\(R^{2}\).

**Exercise 3.** Add an interaction term between hours and attendance to the model. Is it
significant, and what would a significant interaction mean?

**Exercise 4.** Use VIF to check a model containing hours, attendance and engagement.
Which predictor would you drop, and why?

**Exercise 5.** Explain in three sentences why the tutoring coefficient in Section 9 is
not a causal effect, and what design would estimate one.

## 11. Solutions

```python
# Solution 1
p = stats.pearsonr(df["attendance"], df["score"])
s = stats.spearmanr(df["attendance"], df["score"])
print(f"Pearson {p.statistic:.4f} (p {p.pvalue:.1e}), Spearman {s.statistic:.4f}")
```

```python
# Solution 2
m = sm.OLS(df["score"], sm.add_constant(df["attendance"])).fit()
print(f"slope {m.params['attendance']:.4f}, CI {m.conf_int().loc['attendance'].round(3).tolist()}")
print(f"R^2 {m.rsquared:.4f}")
```

```python
# Solution 3
X_int = sm.add_constant(df[["hours", "attendance"]].assign(
    interaction=df["hours"]*df["attendance"]))
m_int = sm.OLS(df["score"], X_int).fit()
print(m_int.summary().tables[1])
# A significant interaction would mean the effect of hours depends on attendance
# level (or vice versa): the two predictors are not additive.
```

```python
# Solution 4
X_all = sm.add_constant(df[["hours", "attendance", "engagement"]])
v = pd.Series([variance_inflation_factor(X_all.values, i)
               for i in range(X_all.shape[1])], index=X_all.columns)
print(v.round(2).to_string())
# Drop engagement: it is nearly a linear function of hours, so it adds little
# information and inflates the standard error of the hours coefficient.
```

```python
# Solution 5 (written)
# Students chose whether to attend, and the choice is related to motivation, which
# independently raises marks -- so the coefficient mixes the effect of tutoring with the
# effect of the kind of student who attends. Randomly assigning tutoring would break that
# link; short of that, the analysis needs an identification strategy and an explicit
# argument that no unmeasured confounder remains.
```

## 12. Summary

- Pearson measures linear association and is outlier-sensitive; Spearman measures
  monotone association on ranks.
- Least squares gives \(\hat\beta_1=S_{xy}/S_{xx}\); \(s_e\) is the typical residual and
  \(R^{2}\) the share of variance explained.
- Prediction intervals are much wider than intervals for the mean response.
- Residual plots diagnose the assumptions that \(R^{2}\) cannot see.
- Adjusted \(R^{2}\) penalises predictors; VIF above 5 signals collinearity that inflates
  standard errors.
- A regression coefficient is an association. Causation needs a design.

Next: [Practical 17](17-anova-chi-square-nonparametric.ipynb) compares groups and counts.
