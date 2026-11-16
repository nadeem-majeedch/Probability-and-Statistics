# Practical 03 — Working with a Student Dataset

## 1. Introduction

Practical 01 described one variable. Real analysis starts with a table: several
variables, several groups, and usually some missing values. This practical works
through the standard first pass on a dataset — inspect, summarise, compare groups,
check missingness, look for outliers — using pandas.

The dataset is **simulated**, not real student data. It is generated with a fixed
seed, so every table and number below is reproducible; the relationships built into
it (attendance and study time both help, programmes differ slightly) are there so
that the descriptive tools have something to find.

## 2. Learning objectives

By the end of this practical you can:

1. Build and inspect a DataFrame: shape, dtypes, head, missing counts.
2. Produce a summary table of centre and spread, overall and by group.
3. Detect and handle missing values deliberately, and say what the choice costs.
4. Compute z-scores within groups and explain why that can mislead.
5. Read a correlation matrix and a crosstab, with their limits.

## 3. Required libraries

| Library | Used for |
|---|---|
| `numpy` | random generation, numerical work |
| `pandas` | DataFrame construction, grouping, summaries |
| `matplotlib`, `seaborn` | box plots, scatter, heatmap |

## 4. Concepts

### 4.1 Tidy data

A table is **tidy** when each row is one observation, each column is one variable,
and each cell is one value. Almost every pandas operation assumes this shape. The
common untidy forms — one column per month, group totals mixed with individual
rows, a cell holding `"68; 71; 65"` — must be reshaped before analysis
(`melt`, `pivot`, `explode`).

### 4.2 Variable types decide the summary

| Type | Examples | Summarise with |
|---|---|---|
| Numeric, continuous | mark, attendance % | mean, sd, median, IQR |
| Numeric, discrete | number of attempts | counts, median |
| Categorical, nominal | programme | counts, mode |
| Categorical, ordinal | grade band | median, counts |
| Identifier | student_id | nothing — never average it |

Averaging an identifier or a nominal category is the most common beginner error: it
produces a number with no meaning.

### 4.3 Missing data is information

Three cases, with different consequences:

- **MCAR** (missing completely at random): dropping rows loses power but not
  validity.
- **MAR** (missing at random, given observed variables): dropping rows biases the
  result; imputation using other columns is better.
- **MNAR** (missing not at random): the missingness depends on the unobserved value
  itself (weak students skipping the test). No statistical fix exists without
  assumptions; the analysis must say so.

Always report the count of missing values per column *before* dropping anything.

### 4.4 Robustness and grouping

A group mean is sensitive to one extreme member, and small groups are unstable. When
comparing programmes with 10–60 students each, report the median and IQR alongside
the mean and sd, and report the group sizes. A difference between groups of size 8
and 60 is mostly noise.

## 5. Formulas

\[ \bar{x}=\frac1n\sum x_i,\qquad s=\sqrt{\frac{1}{n-1}\sum (x_i-\bar x)^2} \]

\[ z_i=\frac{x_i-\bar x}{s}\quad\text{(within a group if computed by group)} \]

\[ r=\frac{\sum (x_i-\bar x)(y_i-\bar y)}
        {\sqrt{\sum (x_i-\bar x)^2}\sqrt{\sum (y_i-\bar y)^2}} \]

\[ \text{missing share}=\frac{\#\text{missing}}{n} \]

## 6. Implementation

### 6.1 Build the dataset

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
pd.set_option("display.width", 100)

rng = np.random.default_rng(2026)
n = 120

programme = rng.choice(["DS", "CS", "SE"], size=n, p=[0.5, 0.3, 0.2])
ability = rng.normal(0, 1, n) + np.where(programme == "DS", 0.25, 0.0)
attendance = np.clip(rng.normal(78, 12, n) + 4 * ability, 30, 100)
study_hours = np.clip(rng.gamma(4, 1.6, n) + 0.8 * ability, 0.5, 40)

midterm = np.clip(55 + 8 * ability + 0.15 * attendance + rng.normal(0, 7, n), 0, 100)
final = np.clip(50 + 9 * ability + 0.20 * attendance + 1.2 * study_hours
                + rng.normal(0, 6, n), 0, 100)

df = pd.DataFrame({
    "student_id": np.arange(1001, 1001 + n),
    "programme": programme,
    "attendance_pct": attendance.round(1),
    "study_hours_wk": study_hours.round(1),
    "midterm": midterm.round(1),
    "final": final.round(1),
})
df["grade"] = pd.cut(df["final"], bins=[0, 50, 60, 70, 80, 101],
                     labels=["F", "D", "C", "B", "A"], right=False)

# Make missingness realistic: 6% of attendance and 4% of study hours unrecorded.
mask_att = rng.random(n) < 0.06
mask_study = rng.random(n) < 0.04
df.loc[mask_att, "attendance_pct"] = np.nan
df.loc[mask_study, "study_hours_wk"] = np.nan

print(df.shape)
df.head()
```

### 6.2 Inspect before summarising

```python
print(df.dtypes.to_string())
print()
print("missing values per column:")
print(df.isna().sum().to_string())
print()
print("share missing:", f"{df.isna().mean().round(3).to_dict()}")
print("\ngroup sizes:", df["programme"].value_counts().to_dict())
print("grade counts:", df["grade"].value_counts().sort_index().to_dict())
```

### 6.3 Summary statistics, overall

```python
numeric = ["attendance_pct", "study_hours_wk", "midterm", "final"]
print(df[numeric].describe().round(2).to_string())

print("\nmedian and IQR:")
summary = pd.DataFrame({
    "median": df[numeric].median(),
    "q1": df[numeric].quantile(0.25),
    "q3": df[numeric].quantile(0.75),
})
summary["iqr"] = summary["q3"] - summary["q1"]
print(summary.round(2).to_string())
```

`describe()` uses the sample standard deviation (\(n-1\)) and excludes `NaN`.
Notice that the count differs by column: pandas drops missing values per column
rather than per row, so each statistic uses a slightly different sample.

### 6.4 By group

```python
by_programme = df.groupby("programme")[numeric].agg(["count", "mean", "median", "std"])
print(by_programme.round(2).to_string())

print("\npass rate (final >= 50) by programme:")
print(df.assign(passed=df["final"] >= 50)
        .groupby("programme")["passed"]
        .agg(["mean", "count"])
        .rename(columns={"mean": "pass_rate"})
        .round(3)
        .to_string())
```

### 6.5 Missing values, handled deliberately

```python
att_missing_final = df.loc[df["attendance_pct"].isna(), "final"]
att_present_final = df.loc[df["attendance_pct"].notna(), "final"]

print(f"students with attendance missing: {att_missing_final.size}")
print(f"  mean final (missing attendance) : {att_missing_final.mean():.2f}")
print(f"  mean final (attendance present) : {att_present_final.mean():.2f}")
print(f"  difference                      : {att_missing_final.mean() - att_present_final.mean():+.2f}")

# Complete-case analysis (drop rows with any missing value) changes n:
complete = df.dropna(subset=numeric)
print(f"\nrows before: {len(df)}, after complete-case: {len(complete)} "
      f"({len(complete)/len(df):.1%} retained)")
print(f"mean final, all rows     : {df['final'].mean():.2f}")
print(f"mean final, complete rows: {complete['final'].mean():.2f}")

# Median imputation inside each programme, so the fill respects group level:
df_imputed = df.copy()
df_imputed[numeric] = (df_imputed.groupby("programme")[numeric]
                       .transform(lambda s: s.fillna(s.median())))
print(f"missing after imputation : {int(df_imputed[numeric].isna().sum().sum())}")
```

### 6.6 z-scores, within and across groups

```python
df["final_z_overall"] = (df["final"] - df["final"].mean()) / df["final"].std(ddof=1)
df["final_z_within"] = df.groupby("programme")["final"].transform(
    lambda s: (s - s.mean()) / s.std(ddof=1))

print(df[["programme", "final", "final_z_overall", "final_z_within"]]
      .sort_values("final", ascending=False).head(8).round(2).to_string(index=False))

print("\nlargest within-group z-score:",
      df.loc[df["final_z_within"].idxmax(), ["programme", "final", "final_z_within"]].to_dict())
```

### 6.7 Relationships: correlation and a crosstab

```python
corr = df[numeric + ["final"]].corr(numeric_only=True)
print(corr.round(3).to_string())

print("\nattendance vs final, Pearson r = "
      f"{df['attendance_pct'].corr(df['final']):.3f}")
print("attendance vs final, Spearman rho = "
      f"{df['attendance_pct'].corr(df['final'], method='spearman'):.3f}")

print("\ngrade by programme:")
print(pd.crosstab(df["programme"], df["grade"]).to_string())
```

## 7. Output and interpretation

- **Size and completeness.** 120 rows and 7 columns. Six percent of attendance
  values and four percent of study-hour values are missing; the outcome variables are
  complete. That pattern matters: a missing *predictor* can be imputed, but a missing
  *outcome* cannot be recovered.
- **Centre and spread.** Final marks average 74.5 with a standard deviation of 13.7,
  and the median (75.6) is slightly above the mean, so the distribution leans left.
  Attendance averages 78.5 with a standard deviation of 12.5.
- **Groups.** The DS group is the largest (59 students), so its mean is the most
  stable; SE is the smallest (18), so its mean is the least stable of the three.
  Compare medians as well as means, and read the counts before believing any
  difference.
- **Missingness.** Students with missing attendance have a *higher* mean final mark
  here (about 78 against 74), which is the opposite of what dropping a low-attendance
  group would produce. That is expected: in this simulation attendance is missing
  completely at random, so the gap is sampling noise from only seven students, not a
  systematic bias. Complete-case analysis therefore loses rows but does not shift the
  mean in any particular direction. Real missingness is often not random, which is why
  the mechanism has to be argued, not assumed.
- **z-scores.** A student can be average overall and far from average within their own
  programme; the two z-scores answer different questions ("compared with everyone" vs
  "compared with their classmates").
- **Correlation.** Attendance and final correlate positively at about 0.4, and study
  hours correlate positively as well. This is an association in simulated data with a
  known generating process; in real data the same correlation would not establish that
  attending *causes* higher marks, because motivation could drive both.

## 8. Visualisation

```python
fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))

sns.boxplot(data=df, x="programme", y="final", ax=axes[0], width=0.5)
axes[0].set(title="Final marks by programme", xlabel="Programme", ylabel="Final mark")

sns.boxplot(data=df, x="programme", y="attendance_pct", ax=axes[1], width=0.5,
            color="#dd8452")
axes[1].set(title="Attendance by programme", xlabel="Programme", ylabel="Attendance (%)")
fig.tight_layout()
plt.show()
```

```python
fig, ax = plt.subplots(figsize=(6.4, 4.4))
sns.scatterplot(data=df, x="attendance_pct", y="final", hue="programme",
                s=45, alpha=0.8, ax=ax)
ax.set(xlabel="Attendance (%)", ylabel="Final mark",
       title="Final mark against attendance, coloured by programme")
ax.legend(title="Programme", frameon=False, fontsize=9)
fig.tight_layout()
plt.show()
```

```python
fig, ax = plt.subplots(figsize=(5.6, 4.2))
sns.heatmap(df[numeric].corr(), annot=True, fmt=".2f", cmap="vlag",
            vmin=-1, vmax=1, square=True, cbar_kws={"shrink": 0.8}, ax=ax)
ax.set_title("Correlation matrix of the numeric variables")
fig.tight_layout()
plt.show()
```

**What the figures show.** The box plots put the group comparison and the spread in
one picture; the boxes overlap heavily, which is the visual form of "the differences
are small relative to the variation". The scatter plot shows the positive trend and
makes clear that programme does not separate the points into distinct clouds. The
heatmap's strongest cell is on the diagonal (always 1.00), so read the off-diagonal
cells only.

## 9. Practical scenario

A programme coordinator asks: "Which programme is performing best, and should we
change the admissions policy?"

The analysis that answers this honestly has four parts:

1. **Describe, do not rank prematurely.** Report median, IQR and group size per
   programme. With groups of 18, 43 and 59, differences of a few marks are within
   noise.
2. **Check confounding.** Programmes differ in attendance and study hours, and those
   variables are themselves associated with the outcome. A raw comparison mixes the
   programme effect with the composition of the group.
3. **Test before claiming.** A one-way ANOVA (Practical 17) asks whether the group
   means differ more than sampling variation would explain. Only then is a claim
   justified.
4. **State the limits.** These are simulated data. On real data the same steps apply,
   plus a check of how students were assigned to programmes — if they chose, the
   comparison is observational and cannot support a causal claim about teaching.

## 10. Exercises

**Exercise 1.** Report the number of missing values per column, and the share of rows
that are complete across the four numeric variables.

**Exercise 2.** Compute the mean and median final mark for each programme, with group
sizes, and say which programme has the highest median.

**Exercise 3.** Compute the correlation between `study_hours_wk` and `final` both
overall and within each programme. Does the relationship survive within groups?

**Exercise 4.** A colleague averages `student_id` to "summarise the cohort". Explain
in one sentence why that is meaningless, and give a meaningful replacement.

**Exercise 5.** Create a new column `attendance_band` with three levels (low < 70,
medium 70–85, high > 85) and report the mean final mark per band.

## 11. Solutions

```python
# Solution 1
print("missing per column:")
print(df.isna().sum().to_string())
complete_rows = df[numeric].dropna()
print(f"\ncomplete rows: {len(complete_rows)} of {len(df)} ({len(complete_rows)/len(df):.1%})")
```

```python
# Solution 2
table = (df.groupby("programme")["final"]
           .agg(n="count", mean="mean", median="median")
           .round(2)
           .sort_values("median", ascending=False))
print(table.to_string())
print("\nhighest median:", table["median"].idxmax())
```

```python
# Solution 3
overall = df["study_hours_wk"].corr(df["final"])
print(f"overall r = {overall:.3f}")
for prog, part in df.groupby("programme"):
    r = part["study_hours_wk"].corr(part["final"])
    print(f"  {prog}: n = {len(part):3d}  r = {r:.3f}")
```

The within-group correlations are similar in sign and size to the overall one, so the
association is not an artefact of programme composition — though it remains an
association, not a demonstrated cause.

```python
# Solution 4 (written)
# student_id is an identifier: it labels rows and has no magnitude or order, so its
# average (e.g. 1060.5) corresponds to no student and no quantity. A meaningful
# alternative is to report the number of students (count), or the mean of a real
# measured variable such as the final mark.

df["student_id"].agg(["count", "min", "max"]).to_string()
```

```python
# Solution 5
df["attendance_band"] = pd.cut(
    df["attendance_pct"],
    bins=[0, 70, 85, 100],
    labels=["low", "medium", "high"],
    right=False,
)
print(df.groupby("attendance_band", observed=False)["final"]
        .agg(n="count", mean="mean", median="median").round(2).to_string())
```

## 12. Summary

- Inspect a new table with `shape`, `dtypes`, `isna().sum()` and `head()` before
  computing anything.
- `describe()` uses the sample standard deviation and drops missing values per column;
  the count can therefore differ between columns.
- Group summaries need group sizes; small groups produce unstable means.
- Missing data has mechanisms (MCAR, MAR, MNAR), and dropping rows is a choice with a
  cost that should be stated.
- Correlations describe association within the observed range only, and z-scores
  computed within groups answer a different question from z-scores computed overall.

Next: [Practical 04](04-data-visualization.ipynb) turns these tables into figures that
are honest and readable.
