# Practical 11 — Joint Distributions

## 1. Introduction

Two variables measured together need a **joint distribution**: not just how each
behaves alone, but how they move together. This practical builds one from a small table,
takes it apart into marginals and conditionals, and measures the association with
covariance and correlation.

The central skill is knowing which of three questions is being asked:

- **marginal** — what is the distribution of \(Y\), ignoring \(X\)?
- **conditional** — what is the distribution of \(Y\) among cases with \(X=x\)?
- **joint** — what is the probability of a particular pair?

Confusing them produces the errors this practical is designed to prevent.

## 2. Learning objectives

By the end of this practical you can:

1. Build a joint PMF and verify that it sums to 1.
2. Derive marginal and conditional distributions from a joint table.
3. Test independence from the joint distribution.
4. Compute covariance and correlation, and interpret their signs.
5. Explain why zero correlation does not imply independence.

## 3. Required libraries

| Library | Used for |
|---|---|
| `numpy` | bivariate simulation |
| `pandas` | joint tables, groupby for conditionals |
| `matplotlib` | heatmaps and scatter plots |

## 4. Concepts

### 4.1 Joint, marginal, conditional

For discrete \(X,Y\): the joint PMF is \(p(x,y)=\Pr(X=x,Y=y)\), and

\[ p_X(x)=\sum_y p(x,y),\qquad p_Y(y)=\sum_x p(x,y) \]

are the **marginals** — sums over the other variable. The **conditional** is

\[ p_{Y\mid X}(y\mid x)=\frac{p(x,y)}{p_X(x)}. \]

Independence means \(p(x,y)=p_X(x)p_Y(y)\) for every pair.

### 4.2 Covariance

\[ \Cov(X,Y)=\E[(X-\E X)(Y-\E Y)]=\E[XY]-\E[X]\E[Y]. \]

Positive covariance means the variables tend to be above their means together. The
magnitude depends on units, so we standardise:

\[ \rho=\frac{\Cov(X,Y)}{\sigma_X\sigma_Y}\in[-1,1]. \]

### 4.3 Variance of a sum

\[ \Var(X+Y)=\Var(X)+\Var(Y)+2\Cov(X,Y). \]

Positive covariance increases the variance of a sum; negative covariance reduces it.
That single identity is the mathematics of portfolio diversification and of paired
experiments.

### 4.4 Zero correlation is not independence

Correlation measures **linear** association. If \(Y=X^{2}\) with \(X\) symmetric about 0,
then \(\Cov(X,Y)=\E[X^{3}]=0\), so \(\rho=0\), yet \(Y\) is a deterministic function of
\(X\). Independence implies zero correlation; the converse is false.

## 5. Formulas

\[ \E[XY]=\sum_x\sum_y xy\,p(x,y),\qquad
   \Cov(X,Y)=\E[XY]-\E X\E Y \]

\[ \rho=\frac{\Cov(X,Y)}{\sigma_X\sigma_Y},\qquad
   \Var(aX+bY)=a^{2}\Var X+b^{2}\Var Y+2ab\,\Cov(X,Y) \]

\[ \E[Y\mid X=x]=\sum_y y\,p_{Y\mid X}(y\mid x) \]

## 6. Implementation

### 6.1 A joint distribution from two dice

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

faces = np.arange(1, 7)
joint = pd.DataFrame(1/36, index=faces, columns=faces)
joint.index.name = "die 1"
joint.columns.name = "die 2"

print("total probability:", joint.to_numpy().sum())
print("\nfirst three rows:")
print(joint.iloc[:3, :3].round(4).to_string())

marginal_1 = joint.sum(axis=1)
marginal_2 = joint.sum(axis=0)
print("\nmarginal of die 1:", marginal_1.round(4).to_dict())
print("all marginals equal 1/6?", np.allclose(marginal_1, 1/6))

product = np.outer(marginal_1, marginal_2)
print("independent? (joint == product of marginals):",
      np.allclose(joint.to_numpy(), product))
```

```python
# Covariance of two fair dice: independent, so covariance must be zero.
d = np.arange(1, 7)
E1 = np.sum(d * marginal_1.to_numpy())
E2 = np.sum(d * marginal_2.to_numpy())
EXY = sum(i*j*joint.loc[i, j] for i in d for j in d)

print(f"E[X] = {E1:.4f}, E[Y] = {E2:.4f}")
print(f"E[XY] = {EXY:.4f}, E[X]E[Y] = {E1*E2:.4f}")
print(f"Cov(X,Y) = {EXY - E1*E2:.6f}")
```

### 6.2 A dependent joint distribution

Let \(X\) be study hours (1–3) and \(Y\) be pass/fail, with the table below.

```python
study = pd.DataFrame(
    {"fail": [0.10, 0.15, 0.05],
     "pass": [0.10, 0.25, 0.35]},
    index=pd.Index([1, 2, 3], name="hours"),
)
print(study.round(4).to_string())
print("\nsums to 1?", np.isclose(study.to_numpy().sum(), 1))

marg_hours = study.sum(axis=1)
marg_result = study.sum(axis=0)
print("\nP(hours):", marg_hours.round(4).to_dict())
print("P(result):", marg_result.round(4).to_dict())

# Conditional distribution of the result given hours.
conditional = study.div(marg_hours, axis=0)
print("\nP(result | hours):")
print(conditional.round(4).to_string())

print("\nP(pass)                =", round(marg_result['pass'], 4))
print("P(pass | hours = 1)    =", round(conditional.loc[1, 'pass'], 4))
print("P(pass | hours = 3)    =", round(conditional.loc[3, 'pass'], 4))
```

```python
# Independence check: compare each cell with the product of its margins.
expected_if_independent = np.outer(marg_hours, marg_result)
comparison = pd.DataFrame(expected_if_independent, index=study.index,
                          columns=study.columns)
print("observed - expected under independence:")
print((study - comparison).round(4).to_string())
print("\nindependent?", np.allclose(study.to_numpy(), expected_if_independent))
```

### 6.3 Covariance and correlation from the table

```python
x = np.array([1, 2, 3])
p_x = marg_hours.to_numpy()
p_y = marg_result.to_numpy()
y = np.array([0, 1])          # fail = 0, pass = 1

EX = np.sum(x * p_x)
EY = np.sum(y * p_y)
EXY = sum(study.loc[i, c] * i * j for i in x for j, c in zip(y, study.columns))
cov = EXY - EX * EY
sd_x = np.sqrt(np.sum((x - EX)**2 * p_x))
sd_y = np.sqrt(np.sum((y - EY)**2 * p_y))

print(f"E[X] = {EX:.4f}, E[Y] = {EY:.4f}")
print(f"E[XY] = {EXY:.4f}")
print(f"Cov(X,Y) = {cov:.4f}")
print(f"sd(X) = {sd_x:.4f}, sd(Y) = {sd_y:.4f}")
print(f"correlation = {cov/(sd_x*sd_y):.4f}")
```

### 6.4 Conditional expectation

```python
cond_expectation = conditional.mul(y, axis=1).sum(axis=1)
print("E[pass indicator | hours]:")
print(cond_expectation.round(4).to_string())
print("\nE[Y] computed by total expectation:",
      round(np.sum(cond_expectation.to_numpy() * p_x), 4))
print("E[Y] computed directly           :", round(EY, 4))
```

\(\E[Y]=\E[\E[Y\mid X]]\): the overall pass rate is the hours-weighted average of the
per-hours pass rates. That identity is the engine behind stratified analysis.

### 6.5 Bivariate normal simulation

```python
rng = np.random.default_rng(2026)
n = 5000
rho = 0.7
mean = [0, 0]
cov_matrix = [[1, rho], [rho, 1]]

sample = rng.multivariate_normal(mean, cov_matrix, size=n)
xs, ys = sample[:, 0], sample[:, 1]

print(f"sample correlation       : {np.corrcoef(xs, ys)[0, 1]:.4f}  (true {rho})")
print(f"sample covariance        : {np.cov(xs, ys)[0, 1]:.4f}  (true {rho})")
print(f"Var(X + Y) sample        : {np.var(xs + ys, ddof=1):.4f}")
print(f"Var(X) + Var(Y) + 2Cov   : {np.var(xs, ddof=1) + np.var(ys, ddof=1) + 2*np.cov(xs, ys)[0,1]:.4f}")

# Negative correlation reduces the variance of the sum.
neg = rng.multivariate_normal(mean, [[1, -0.6], [-0.6, 1]], size=n)
print(f"\nwith rho = -0.6, Var(X+Y) = {np.var(neg[:,0] + neg[:,1], ddof=1):.4f}  (< 2)")
```

### 6.6 Zero correlation without independence

```python
rng = np.random.default_rng(7)
u = rng.uniform(-1, 1, 5000)
v = u**2 + rng.normal(0, 0.02, 5000)

print(f"correlation between U and U^2: {np.corrcoef(u, v)[0,1]:+.4f}")
print("but V is a deterministic function of U (plus noise)")
print(f"E[V | U > 0.8] = {v[u > 0.8].mean():.3f}")
print(f"E[V | U < -0.8] = {v[u < -0.8].mean():.3f}")
```

The correlation is essentially zero, yet knowing the sign of \(U\) tells you a great deal
about \(V\). Any analysis that screens variables by correlation alone will discard a
strong non-linear relationship.

## 7. Output and interpretation

- **Independence of two dice.** The joint table is \(1/36\) in every cell, the marginals
  are \(1/6\), and \(\Cov=0\) to machine precision. Independence is visible as a flat
  table and a zero covariance together.
- **Study hours and passing.** The joint table is not a product of its margins: at 1 hour
  the pass rate is about 0.50, at 3 hours it is 0.875. The covariance is positive
  (about 0.11) and the correlation about 0.32 — a moderate positive association, in units
  of "pass indicator", which is why correlation on a binary variable needs care in
  interpretation.
- **Conditional expectation.** The per-hours pass rates, weighted by the hours
  distribution, reproduce the overall pass rate of 0.70. Stratifying and then reweighting
  is the same arithmetic.
- **Bivariate normal.** The sample correlation of 0.70, covariance 0.70 and
  \(\Var(X+Y)=2+2(0.7)=3.4\) all match theory. With \(\rho=-0.6\) the variance of the sum
  falls to 0.8, which is why negatively correlated assets reduce portfolio risk.
- **Zero correlation.** \(U\) and \(U^{2}\) have correlation near zero but a perfect
  functional relationship; conditional means of \(V\) differ sharply by the sign of \(U\).

## 8. Visualisation

```python
fig, axes = plt.subplots(1, 2, figsize=(11, 3.9))

im = axes[0].imshow(study.to_numpy(), cmap="Blues", aspect="auto")
axes[0].set_xticks([0, 1], ["fail", "pass"])
axes[0].set_yticks([0, 1, 2], ["1 h", "2 h", "3 h"])
for i in range(3):
    for j in range(2):
        axes[0].text(j, i, f"{study.iloc[i, j]:.2f}", ha="center", va="center",
                     color="black", fontsize=10)
axes[0].set(title="Joint PMF of hours and result", xlabel="Result", ylabel="Hours")
fig.colorbar(im, ax=axes[0], shrink=0.8)

axes[1].scatter(xs, ys, s=6, alpha=0.35, color="#4c72b0")
axes[1].set(title="Bivariate normal, rho = 0.7", xlabel="X", ylabel="Y")
axes[1].grid(alpha=0.3)

fig.tight_layout()
plt.show()
```

```python
fig, axes = plt.subplots(1, 2, figsize=(11, 3.6))
axes[0].scatter(u, v, s=5, alpha=0.3, color="#55a868")
axes[0].set(title="Zero correlation, strong dependence", xlabel="U", ylabel="V = U^2 + noise")
axes[0].grid(alpha=0.3)

bins = np.linspace(-1, 1, 11)
mid = (bins[:-1] + bins[1:]) / 2
cond_means = [v[(u >= lo) & (u < hi)].mean() for lo, hi in zip(bins[:-1], bins[1:])]
axes[1].plot(mid, cond_means, "o-", color="#c44e52")
axes[1].set(title="Conditional mean E[V | U = u]", xlabel="u", ylabel="mean of V")
axes[1].grid(alpha=0.3)
fig.tight_layout()
plt.show()
```

**What to look at.** The heatmap shows a joint distribution that is graded along the
diagonal — hours and passing rise together, and the cell values cannot be recovered from
the margins. The second pair of panels is the warning: the scatter is a clean parabola
with essentially zero correlation, and the conditional means trace the curve. A
correlation matrix would report "no relationship".

## 9. Practical scenario

**Portfolio risk.** Two investments have standard deviations 12% and 8%, with correlation
0.25. What is the risk of an equal-weighted portfolio?

```python
s1, s2, rho = 12.0, 8.0, 0.25
w1 = w2 = 0.5
portfolio_var = (w1*s1)**2 + (w2*s2)**2 + 2*w1*w2*rho*s1*s2
print(f"portfolio variance = {portfolio_var:.2f}")
print(f"portfolio sd       = {np.sqrt(portfolio_var):.2f}%")
print(f"weighted average sd (no diversification) = {w1*s1 + w2*s2:.2f}%")

for r in (-0.5, 0.0, 0.25, 0.9):
    var_r = (w1*s1)**2 + (w2*s2)**2 + 2*w1*w2*r*s1*s2
    print(f"rho = {r:+.2f} -> portfolio sd {np.sqrt(var_r):.2f}%")
```

The portfolio's risk is below the weighted average of its parts whenever \(\rho<1\):
that is diversification, and it is nothing more than the covariance term in
\(\Var(X+Y)\). At \(\rho=0.9\) almost all of the benefit disappears.

## 10. Exercises

**Exercise 1.** For the study-hours table, compute \(\Pr(\text{hours}=2\mid\text{pass})\)
and compare it with \(\Pr(\text{pass}\mid\text{hours}=2)\).

**Exercise 2.** Construct a \(2\times2\) joint table in which \(X\) and \(Y\) are
independent, and verify \(\Cov=0\).

**Exercise 3.** Simulate bivariate normal data with \(\rho=-0.5\) and verify that
\(\Var(X+Y)=\Var X+\Var Y+2\Cov\) holds.

**Exercise 4.** For the parabola example, compute the correlation between \(U\) and
\(V\) and the correlation between \(|U|\) and \(V\). Explain the difference.

**Exercise 5.** Two variables have \(\rho=0\). Give one reason they might still be
useful predictors of each other.

## 11. Solutions

```python
# Solution 1
p_hours2_given_pass = study.loc[2, "pass"] / marg_result["pass"]
print(f"P(hours=2 | pass) = {p_hours2_given_pass:.4f}")
print(f"P(pass | hours=2) = {conditional.loc[2, 'pass']:.4f}")
# They are different questions: the first describes the composition of the passing
# group, the second the success rate within the 2-hour group.
```

```python
# Solution 2
tab = pd.DataFrame({"y0": [0.30, 0.20], "y1": [0.30, 0.20]},
                   index=pd.Index(["x0", "x1"], name="x"))
print(tab.to_string())
print("row sums:", tab.sum(axis=1).round(3).tolist())
print("column sums:", tab.sum(axis=0).round(3).tolist())
print("all cells equal row x column?",
      np.allclose(tab.to_numpy(), np.outer(tab.sum(axis=1), tab.sum(axis=0))))
```

```python
# Solution 3
rng = np.random.default_rng(8)
s = rng.multivariate_normal([0, 0], [[1, -0.5], [-0.5, 1]], size=20_000)
x_, y_ = s[:, 0], s[:, 1]
lhs = np.var(x_ + y_, ddof=1)
rhs = np.var(x_, ddof=1) + np.var(y_, ddof=1) + 2*np.cov(x_, y_)[0, 1]
print(f"Var(X+Y) = {lhs:.4f}, formula = {rhs:.4f}, equal? {np.isclose(lhs, rhs)}")
```

```python
# Solution 4
print(f"corr(U, V)   = {np.corrcoef(u, v)[0,1]:+.4f}")
print(f"corr(|U|, V) = {np.corrcoef(np.abs(u), v)[0,1]:+.4f}")
# V depends on the *magnitude* of U, not its sign, so the signed correlation cancels
# to zero while the correlation with |U| is strong. Correlation detects only the
# linear-in-sign part of the relationship.
```

```python
# Solution 5 (written)
# Zero linear correlation does not rule out a non-linear relationship (the parabola
# above), or an interaction, or a relationship that is strong in a subpopulation. A
# scatter plot and a conditional-mean plot should come before discarding a variable.
```

## 12. Summary

- A joint distribution gives the probability of pairs; marginals sum over the other
  variable, conditionals fix it.
- Independence is \(p(x,y)=p_X(x)p_Y(y)\), which implies zero covariance.
- Covariance measures linear co-movement in squared units; correlation standardises it
  to \([-1,1]\).
- \(\Var(X+Y)\) includes \(2\Cov(X,Y)\): positive covariance raises risk, negative
  lowers it.
- \(\E[Y]=\E[\E[Y\mid X]]\) lets group rates be recombined into an overall rate.
- Zero correlation does not imply independence; plot before you discard.

Next: [Practical 12](12-sampling-and-sampling-distributions.ipynb) studies what happens
to a statistic across repeated samples.
