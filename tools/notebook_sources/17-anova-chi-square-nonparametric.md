# Practical 17 — ANOVA, Chi-Square and Nonparametric Tests

## 1. Introduction

Three questions, three families of test:

- **Do three or more group means differ?** Analysis of variance, then a post-hoc
  comparison to find which groups differ.
- **Is a count distribution compatible with a claim, or are two categorical variables
  related?** Chi-square tests.
- **What if the data are ordinal, skewed, or full of outliers?** Rank-based tests.

This practical runs each one on simulated data with a known answer, so the output can be
checked against the truth as well as interpreted.

## 2. Learning objectives

By the end of this practical you can:

1. Run a one-way ANOVA and read the \(F\) statistic, df and \(\eta^{2}\).
2. Follow up with Tukey's HSD and explain why uncorrected pairwise tests are wrong.
3. Run a two-way ANOVA with an interaction term.
4. Run chi-square goodness-of-fit and independence tests, with effect sizes.
5. Choose and run Mann–Whitney, Wilcoxon and Kruskal–Wallis tests.

## 3. Required libraries

| Library | Used for |
|---|---|
| `scipy.stats` | `f_oneway`, `chi2_contingency`, `chisquare`, rank tests |
| `statsmodels` | OLS + `anova_lm`, `pairwise_tukeyhsd` |
| `pandas`, `matplotlib`, `seaborn` | tables and figures |

## 4. Concepts

### 4.1 Why not repeated t tests?

With three groups there are three pairwise comparisons. Three tests at 5% give a
family-wise error of \(1-0.95^{3}=14.3\%\). ANOVA tests all means simultaneously with a
single 5% error rate.

### 4.2 The ANOVA decomposition

\[ \underbrace{\sum_i\sum_j(y_{ij}-\bar y)^{2}}_{\text{SST}}
   =\underbrace{\sum_i n_i(\bar y_i-\bar y)^{2}}_{\text{SSB}}
   +\underbrace{\sum_i\sum_j(y_{ij}-\bar y_i)^{2}}_{\text{SSW}}, \]

\[ F=\frac{\text{SSB}/(k-1)}{\text{SSW}/(N-k)}\sim F_{k-1,N-k}\ \text{under }H_0. \]

\(F\) is a signal-to-noise ratio: between-group variation divided by within-group
variation. A significant \(F\) says *some* mean differs — not which.

### 4.3 Chi-square

\[ \chi^{2}=\sum\frac{(O-E)^{2}}{E}. \]

Goodness of fit compares one categorical variable with a hypothesised distribution
(\(k-1\) df); independence compares two categorical variables in a table
(\((r-1)(c-1)\) df). Expected counts should be at least 5.

### 4.4 Rank tests

| Design | Parametric | Nonparametric |
|---|---|---|
| Two independent groups | two-sample t | Mann–Whitney \(U\) |
| Two paired measurements | paired t | Wilcoxon signed-rank |
| Three or more groups | one-way ANOVA | Kruskal–Wallis |

They test the same *null of identical distributions* (or a shift, under equal shapes)
without assuming normality. The cost is power when the normality assumption actually
holds.

## 5. Formulas

\[ F=\frac{\text{MSB}}{\text{MSW}},\qquad
   \eta^{2}=\frac{\text{SSB}}{\text{SST}} \]

\[ \text{HSD}=q_{k,N-k,1-\alpha}\sqrt{\frac{\text{MSW}}{n}} \]

\[ H=\frac{12}{N(N+1)}\sum_i n_i\bar R_i^{2}-3(N+1)
   \quad\text{(Kruskal–Wallis)} \]

\[ V=\sqrt{\frac{\chi^{2}}{N\min(r-1,c-1)}}\quad\text{(Cramér's V)} \]

## 6. Implementation

### 6.1 Simulate three teaching methods

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
rng = np.random.default_rng(2026)
n_per_group = 25

methods = {"lecture": 68, "tutorial": 73, "project": 76}
data = pd.DataFrame({
    "method": np.repeat(list(methods), n_per_group),
    "score": np.concatenate([rng.normal(m, 8, n_per_group) for m in methods.values()]),
})
print(data.groupby("method")["score"].agg(["count", "mean", "std"]).round(2).to_string())
```

### 6.2 One-way ANOVA

```python
aov_model = ols("score ~ C(method)", data=data).fit()
table = sm.stats.anova_lm(aov_model, typ=2)
print(table.round(4).to_string())

ssb = table.loc["C(method)", "sum_sq"]
ssw = table.loc["Residual", "sum_sq"]
print(f"\neta^2 = {ssb/(ssb+ssw):.4f}")
print(f"F from scipy: {stats.f_oneway(*[g['score'].values for _, g in data.groupby('method')]):}")
```

### 6.3 Tukey's HSD

```python
tukey = pairwise_tukeyhsd(data["score"], data["method"], alpha=0.05)
print(tukey.summary().as_text())
```

```python
# What happens without correction: three t tests at 5%.
pairs = [("lecture", "tutorial"), ("lecture", "project"), ("tutorial", "project")]
for a, b in pairs:
    res = stats.ttest_ind(data.loc[data.method == a, "score"],
                          data.loc[data.method == b, "score"])
    print(f"{a:8s} vs {b:8s}: t {res.statistic:6.2f}, p {res.pvalue:.4f}")
print(f"\nfamily-wise error for 3 tests at 5%: {1-0.95**3:.4f}")
```

### 6.4 Two-way ANOVA with an interaction

```python
rng = np.random.default_rng(7)
n = 30
two_way = pd.DataFrame({
    "method": np.repeat(["lecture", "project"], n),
    "level": np.tile(np.repeat(["beginner", "advanced"], n//2), 2),
})
boost = np.where((two_way.method == "project") & (two_way.level == "advanced"), 8, 0)
two_way["score"] = 65 + boost + rng.normal(0, 6, two_way.shape[0])

model2 = ols("score ~ C(method) * C(level)", data=two_way).fit()
print(sm.stats.anova_lm(model2, typ=2).round(4).to_string())
print("\ncell means:")
print(two_way.groupby(["method", "level"])["score"].mean().round(2).to_string())
```

### 6.5 Chi-square: goodness of fit

```python
observed = np.array([15, 18, 22, 25, 20, 20])
expected = np.full(6, observed.sum()/6)
chi2, p = stats.chisquare(observed, expected)
print(f"observed: {observed.tolist()}  total {observed.sum()}")
print(f"expected: {expected.tolist()}")
print(f"chi2 = {chi2:.4f}, df = {len(observed)-1}, p = {p:.4f}")
print(f"critical value at 5%: {stats.chi2.ppf(0.95, 5):.4f}")
```

### 6.6 Chi-square: independence, with an effect size

```python
table = pd.DataFrame({"internship": [40, 20], "no_internship": [60, 80]},
                     index=["DS", "CS"])
print(table.to_string())

chi2, p, dof, expected = stats.chi2_contingency(table, correction=False)
print(f"\nchi2 = {chi2:.4f}, df = {dof}, p = {p:.6f}")
print("expected counts:")
print(pd.DataFrame(expected, index=table.index, columns=table.columns).round(2).to_string())

odds_ratio = (40/60) / (20/80)
cramers_v = np.sqrt(chi2 / (table.values.sum() * (min(table.shape)-1)))
print(f"\nodds ratio = {odds_ratio:.3f}")
print(f"Cramer's V = {cramers_v:.3f}")
```

### 6.7 Nonparametric tests

```python
rng = np.random.default_rng(11)
a = rng.exponential(5, 40)          # skewed, so a rank test is appropriate
b = rng.exponential(8, 40)

mw = stats.mannwhitneyu(a, b, alternative="two-sided")
print(f"Mann-Whitney U = {mw.statistic:.1f}, p = {mw.pvalue:.5f}")
print(f"mean ranks: a {stats.rankdata(np.concatenate([a,b]))[:40].mean():.1f}, "
      f"b {stats.rankdata(np.concatenate([a,b]))[40:].mean():.1f}")

before = rng.normal(60, 7, 30)
after = before + rng.normal(1.8, 3, 30)
wil = stats.wilcoxon(after, before)
print(f"Wilcoxon signed-rank: W = {wil.statistic:.1f}, p = {wil.pvalue:.5f}")

groups_kw = [rng.exponential(m, 30) for m in (4, 7, 9)]
kw = stats.kruskal(*groups_kw)
print(f"Kruskal-Wallis H = {kw.statistic:.4f}, p = {kw.pvalue:.6f}")
```

### 6.8 When the parametric test is fine

```python
rng = np.random.default_rng(21)
normal_groups = [rng.normal(m, 5, 40) for m in (50, 52, 54)]
print(f"ANOVA on normal data: F {stats.f_oneway(*normal_groups).statistic:.3f}, "
      f"p {stats.f_oneway(*normal_groups).pvalue:.4f}")
print(f"Kruskal on the same data: H {stats.kruskal(*normal_groups).statistic:.3f}, "
      f"p {stats.kruskal(*normal_groups).pvalue:.4f}")
```

Both find the difference, but the ANOVA p-value is smaller: when the assumptions hold,
the parametric test is more powerful.

## 7. Output and interpretation

- **One-way ANOVA.** The between-group mean square is far larger than the within-group
  mean square, so \(F\) is large and the p-value is tiny. \(\eta^{2}\approx0.2\) means
  about 20% of the variation in scores is between methods — a moderate effect, and the
  number to report beside \(F\).
- **Tukey.** The project group differs from both others, while lecture and tutorial
  differ less. Tukey's simultaneous intervals are wider than the individual t intervals,
  which is the price of controlling the family-wise error; that is why one pairwise
  comparison may be non-significant in Tukey while its uncorrected t test was
  significant.
- **Two-way.** The interaction term is large and significant: the project method helps
  advanced students much more than beginners. With an interaction present, the main
  effects are averages over a pattern that differs by cell, so the cell means are the
  result to report.
- **Goodness of fit.** \(\chi^{2}\) is far below the 5% critical value, so the observed
  counts are compatible with a fair die. Note that a *significant* result with 1,200 rolls
  would indicate a tiny bias of no practical importance.
- **Independence.** The chi-square is highly significant, the odds ratio shows the DS
  group has more than twice the odds of an internship, and Cramér's \(V\) says the
  association is moderate. Report all three: significance, direction, strength.
- **Rank tests.** Mann–Whitney detects the shift between the two exponential samples
  despite the skew; Wilcoxon does the same for paired data; Kruskal–Wallis extends it to
  three groups. All three p-values are small because the effects are large relative to
  the noise.
- **Power.** On normal data the ANOVA p-value is smaller than Kruskal's. Using a rank test
  when the assumptions hold is safe but wasteful.

## 8. Visualisation

```python
fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))

sns.boxplot(data=data, x="method", y="score", ax=axes[0], width=0.5)
sns.stripplot(data=data, x="method", y="score", ax=axes[0], color="black",
              size=3, alpha=0.5)
axes[0].set(title="Scores by method", xlabel="Method", ylabel="Score")

sns.pointplot(data=two_way, x="method", y="score", hue="level",
              dodge=0.15, errorbar="se", ax=axes[1], markers=["o", "s"])
axes[1].set(title="Interaction: project helps advanced students", xlabel="Method",
            ylabel="Mean score")
axes[1].legend(title="Level", frameon=False)

fig.tight_layout()
plt.show()
```

```python
fig, ax = plt.subplots(figsize=(6.6, 3.6))
sns.histplot(a, bins=15, alpha=0.55, label="group A", ax=ax, stat="density")
sns.histplot(b, bins=15, alpha=0.55, label="group B", ax=ax, stat="density")
ax.set(title="Skewed groups: a rank test is appropriate", xlabel="Value", ylabel="Density")
ax.legend(frameon=False)
fig.tight_layout()
plt.show()
```

**What to look at.** The box plot and the strip plot together show both the summary and
the raw data: the boxes overlap, but the project group sits higher. In the interaction
plot the lines are not parallel — the gap between beginner and advanced is much larger
for the project method, which is what the significant interaction term reports. The
skewed histograms show why a t test on means would be less reliable than a rank test.

## 9. Practical scenario

**Comparing four checkout designs.** An e-commerce team tests four variants on 2,000
sessions each. Conversion is binary, so ANOVA is the wrong tool; the correct test is a
chi-square on the 4×2 table, followed by pairwise comparisons with a correction.

```python
rng = np.random.default_rng(31)
rates = {"A": 0.10, "B": 0.105, "C": 0.13, "D": 0.128}
n_sessions = 2000
counts = {k: rng.binomial(n_sessions, p) for k, p in rates.items()}
tab = pd.DataFrame({"converted": list(counts.values()),
                    "not_converted": [n_sessions - c for c in counts.values()]},
                   index=list(counts))
print(tab.to_string())

chi2, p, dof, _ = stats.chi2_contingency(tab, correction=False)
print(f"\nchi2 = {chi2:.3f}, df = {dof}, p = {p:.5f}")

# Which variants differ? Bonferroni-corrected pairwise chi-square tests.
pairs = [("A", "C"), ("B", "C"), ("A", "D"), ("C", "D")]
for x, y in pairs:
    sub = tab.loc[[x, y]]
    _, p_pair, _, _ = stats.chi2_contingency(sub, correction=False)
    print(f"{x} vs {y}: p = {p_pair:.4f}, Bonferroni threshold {0.05/len(pairs):.4f}")
```

The overall test says the variants differ; the pairwise tests locate the difference in C
and D, and the correction keeps the family-wise error at 5%. The next question — how much
does the change earn? — needs the effect size and its interval, not the p-value.

## 10. Exercises

**Exercise 1.** Run a one-way ANOVA on three groups you simulate with means 10, 12, 14
and sd 3, \(n=30\) each. Report \(F\), p and \(\eta^{2}\).

**Exercise 2.** Apply Tukey's HSD to the same data and state which pairs differ.

**Exercise 3.** Test whether a die is fair using counts 12, 20, 18, 22, 14, 14 out of 100
rolls.

**Exercise 4.** Test independence in a 2×2 table with counts 30/50 and 20/50, and report
the odds ratio.

**Exercise 5.** Compare a t test and a Mann–Whitney test on heavily skewed data with the
same true shift. Which is more sensitive, and why?

## 11. Solutions

```python
# Solution 1
rng = np.random.default_rng(501)
groups = [rng.normal(m, 3, 30) for m in (10, 12, 14)]
res = stats.f_oneway(*groups)
print(f"F = {res.statistic:.3f}, p = {res.pvalue:.5f}")
grand = np.concatenate(groups).mean()
ssb = sum(len(g)*(g.mean()-grand)**2 for g in groups)
sst = sum(((g-grand)**2).sum() for g in groups)
print(f"eta^2 = {ssb/sst:.4f}")
```

```python
# Solution 2
frame = pd.DataFrame({"score": np.concatenate(groups),
                      "group": np.repeat(["g1", "g2", "g3"], 30)})
print(pairwise_tukeyhsd(frame["score"], frame["group"]).summary().as_text())
```

```python
# Solution 3
obs = np.array([12, 20, 18, 22, 14, 14])
chi2, p = stats.chisquare(obs)
print(f"chi2 = {chi2:.3f}, df = 5, p = {p:.4f}")
```

```python
# Solution 4
t2 = pd.DataFrame({"yes": [30, 20], "no": [20, 30]}, index=["exposed", "unexposed"])
chi2, p, dof, _ = stats.chi2_contingency(t2, correction=False)
print(f"chi2 = {chi2:.3f}, p = {p:.5f}, OR = {(30/20)/(20/30):.2f}")
```

```python
# Solution 5
rng = np.random.default_rng(502)
skew_a = rng.lognormal(0, 1.0, 200)
skew_b = rng.lognormal(0.3, 1.0, 200)
print(f"t test      p = {stats.ttest_ind(skew_a, skew_b).pvalue:.5f}")
print(f"Mann-Whitney p = {stats.mannwhitneyu(skew_a, skew_b).pvalue:.5f}")
# On lognormal data the t test is still reliable at n=200 (CLT for the mean), but
# Mann-Whitney is often more powerful here because it uses ranks rather than
# letting a few extreme values dominate the mean.
```

## 12. Summary

- ANOVA compares all group means at once, using the ratio of between- to within-group
  variance; a significant \(F\) needs a post-hoc procedure to locate the difference.
- Tukey's HSD controls the family-wise error; uncorrected pairwise t tests do not.
- Two-way ANOVA adds an interaction, and a significant interaction means the main effects
  are averages over a pattern that differs by cell.
- Chi-square tests counts: goodness of fit for one variable, independence for a table;
  report Cramér's \(V\) or an odds ratio as well as the p-value.
- Rank tests handle skew, ordinal data and outliers, at some cost in power when the
  parametric assumptions hold.
- The design decides the test; the p-value never does.

Next: [Practical 18](18-bayesian-and-data-science-methods.ipynb) closes the course with
Bayesian updating, resampling and model evaluation.
