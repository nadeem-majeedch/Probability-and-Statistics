# Practical 01 — Descriptive Statistics from Examination Data

## 1. Introduction

Thirty students sat the same examination. Before asking whether one teaching
method beats another, or whether this cohort differs from last year's, we have to
describe what happened. That is the job of descriptive statistics: a small number
of summaries that answer "where is the centre?", "how spread out is it?", and
"what shape is it?".

This practical computes each summary twice — once by hand from the formula, once
with a library — and then checks that the two agree. It ends by looking at the
same data as a histogram and a box plot, because numbers alone hide shape.

The dataset is fixed in the code below (not random), so every number you see can be
reproduced on paper.

## 2. Learning objectives

By the end of this practical you can:

1. Compute and interpret the mean, median and mode of a small dataset.
2. Compute quartiles, the interquartile range and the 1.5 × IQR outlier fences.
3. Distinguish the population standard deviation from the sample standard
   deviation, and say which one a report should use.
4. Explain why the mean is sensitive to outliers and the median is not.
5. Read a histogram and a box plot, and describe shape, centre and spread.
6. Compute a z-score and a coefficient of variation and say what each is for.

## 3. Required libraries

| Library | Used for |
|---|---|
| `numpy` | arrays, quantiles, vectorised arithmetic |
| `pandas` | a DataFrame view of the marks and summary tables |
| `scipy.stats` | skewness, kurtosis, mode |
| `matplotlib`, `seaborn` | histogram, box plot, ECDF |

## 4. Concepts

### 4.1 Three measures of centre

- **Mean** — the balance point. Every observation contributes; one extreme value
  moves it.
- **Median** — the middle value in order. Half the data lie below it. It ignores how
  far away the extremes are, which is why it is called *robust*.
- **Mode** — the most frequent value. The only one of the three that makes sense for
  categorical data.

When mean and median agree, the distribution is roughly symmetric. When the mean is
larger, the right tail is longer (right skew); when smaller, the left tail is longer.

### 4.2 Quantiles

The \(p\)-th quantile is the value below which a proportion \(p\) of the data lie.
Quartiles cut the data into quarters: \(Q_1\) at 0.25, the median at 0.50,
\(Q_3\) at 0.75. There is no single universally correct formula for small samples —
different conventions interpolate differently — so software must be told which one
to use. This practical uses linear interpolation (the NumPy/pandas default).

### 4.3 Variance and standard deviation

Variance is the mean squared distance from the mean. Squaring makes it sensitive to
outliers and puts it in squared units, so we take the square root to return to the
original units: that is the standard deviation.

Two versions exist:

- **Population variance** divides by \(n\). Use it when the data *are* the whole
  population.
- **Sample variance** divides by \(n-1\). Use it when the data are a sample, because
  the sample mean is itself estimated from the data and the deviations are then
  slightly too small; dividing by \(n-1\) corrects this on average.

A report about a class of 30 students that is the entire class of interest may use
\(n\); a report about a sample from a larger cohort must use \(n-1\). This course
uses \(n-1\) for every interval and test.

### 4.4 Outliers, IQR and robustness

The \(\text{IQR}=Q_3-Q_1\) spans the middle half of the data. A common rule flags
values below \(Q_1-1.5\,\text{IQR}\) or above \(Q_3+1.5\,\text{IQR}\) as *possible*
outliers. The rule is a convention for starting an investigation, not a verdict: a
flagged value may be a data-entry error, or the most interesting observation in the
set.

## 5. Formulas

\[ \bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i \]

\[ s^{2}=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^{2},
   \qquad \sigma^{2}=\frac{1}{n}\sum_{i=1}^{n}(x_i-\mu)^{2} \]

\[ \text{IQR}=Q_3-Q_1,\qquad
   \text{fences}=Q_1-1.5\,\text{IQR},\quad Q_3+1.5\,\text{IQR} \]

\[ z_i=\frac{x_i-\bar{x}}{s},\qquad
   \text{CV}=\frac{s}{\bar{x}} \]

The z-score says how many standard deviations an observation lies from the mean;
the coefficient of variation expresses spread as a fraction of the mean, so two
variables on different scales can be compared.

## 6. Implementation

### 6.1 The data

```python
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

MARKS = [45, 52, 58, 61, 63, 64, 65, 67, 68, 68,
         69, 70, 70, 71, 72, 73, 73, 74, 75, 76,
         77, 78, 79, 81, 83, 85, 88, 91, 94, 98]

marks = np.array(MARKS)
df = pd.DataFrame({"mark": marks})
print("n =", marks.size)
print("sorted:", marks)
```

### 6.2 Centre, computed by hand

```python
n = marks.size
mean_manual = marks.sum() / n

ordered = np.sort(marks)
if n % 2 == 1:
    median_manual = ordered[n // 2]
else:
    median_manual = (ordered[n // 2 - 1] + ordered[n // 2]) / 2

values, counts = np.unique(marks, return_counts=True)
mode_manual = values[counts == counts.max()]

print(f"mean   (hand) = {mean_manual:.4f}")
print(f"median (hand) = {median_manual:.4f}")
print(f"mode   (hand) = {mode_manual}  with counts {counts[counts == counts.max()]}")
```

### 6.3 The same three with libraries

```python
print(f"mean   numpy  = {marks.mean():.4f}")
print(f"median numpy  = {np.median(marks):.4f}")
mode_result = stats.mode(marks, keepdims=False)
print(f"mode   scipy  = {mode_result.mode}  (count {mode_result.count})")
print()
print("all agree?",
      np.isclose(mean_manual, marks.mean()),
      np.isclose(median_manual, np.median(marks)),
      mode_manual[0] == mode_result.mode)
```

### 6.4 Quantiles and the five-number summary

```python
qs = np.quantile(marks, [0.25, 0.5, 0.75])
q1, q2, q3 = qs
iqr = q3 - q1

print(f"Q1 = {q1:.2f}   median = {q2:.2f}   Q3 = {q3:.2f}")
print(f"IQR = {iqr:.2f}")
print(f"fences: lower {q1 - 1.5 * iqr:.2f}, upper {q3 + 1.5 * iqr:.2f}")

flagged = marks[(marks < q1 - 1.5 * iqr) | (marks > q3 + 1.5 * iqr)]
print("flagged by the 1.5 x IQR rule:", flagged)

print()
print(df["mark"].describe().round(2).to_string())
```

`describe()` prints the count, mean, sample standard deviation, minimum, quartiles
and maximum — the five-number summary plus the two moments. Note that its standard
deviation uses `ddof=1`, and its quartiles match `np.quantile` with linear
interpolation.

### 6.5 Spread: variance and standard deviation, both conventions

```python
var_sample = ((marks - marks.mean()) ** 2).sum() / (n - 1)
var_pop = ((marks - marks.mean()) ** 2).sum() / n

print(f"sample variance (n-1) = {var_sample:.4f}   numpy ddof=1: {marks.var(ddof=1):.4f}")
print(f"population var   (n)  = {var_pop:.4f}   numpy ddof=0: {marks.var(ddof=0):.4f}")
print(f"sample sd             = {np.sqrt(var_sample):.4f}")
print(f"population sd         = {np.sqrt(var_pop):.4f}")
print(f"ratio of variances    = {var_pop / var_sample:.4f}   (= (n-1)/n = {(n-1)/n:.4f})")
```

### 6.6 Shape: skewness, kurtosis, and the mean–median comparison

```python
print(f"mean - median      = {marks.mean() - np.median(marks):+.4f}")
print(f"skewness (Fisher)  = {stats.skew(marks, bias=False):+.4f}")
print(f"excess kurtosis    = {stats.kurtosis(marks, bias=False):+.4f}")
print(f"coefficient of variation = {marks.std(ddof=1) / marks.mean():.4f}")

z = (marks - marks.mean()) / marks.std(ddof=1)
print("\nlargest z-score:", f"{z.max():.4f}", "at mark", marks[z.argmax()])
print("smallest z-score:", f"{z.min():.4f}", "at mark", marks[z.argmin()])
print("share of marks within 1 sd:", f"{(np.abs(z) <= 1).mean():.1%}")
```

The **skewness** is positive when the right tail is longer. The **excess kurtosis**
is 0 for a normal distribution; positive values mean heavier tails. Both are
sample statistics with large uncertainty at \(n=30\) — report them as descriptions,
not as tests.

## 7. Output and interpretation

Reading the numbers above in statistical language:

- **Centre.** The mean is 72.93 and the median is 72.50. They are close, so the
  distribution is close to symmetric; the sample skewness in Section 6.6 is -0.01, so
  the small mean-median gap is not evidence of skew.
- **Spread.** The sample standard deviation is 11.71 marks, so a typical mark lies
  roughly 73 ± 12. The sample variance is 137.17 (marks²) — a unit nobody can
  interpret, which is exactly why we report the standard deviation.
- **The two conventions.** Dividing by \(n\) instead of \(n-1\) gives a variance of
  132.60 rather than 137.17: a 3.3% reduction, exactly the factor \((n-1)/n=29/30\).
  With 30 observations the difference is small; with 3 it is not. The convention must
  be stated, not assumed.
- **Quartiles.** \(Q_1=67.25\), \(Q_3=78.75\), so the middle half of the class spans
  11.5 marks. The fences are 50.00 and 96.00, which flags **45 and 98** as possible
  outliers. Neither is impossible for an examination; the honest response is to check
  the scripts, not to delete the values.
- **Mode.** 68 occurs twice, and several other marks also occur twice, so the mode is
  a weak summary here: for continuous-ish marks with few repeats it carries little
  information. It would matter for a categorical variable such as grade band.
- **z-scores.** 98 lies 2.14 standard deviations above the mean and 45 lies 2.39 below.
  Under a normal distribution about 3.2% of values would lie beyond ±2.14, so these are
  unusual but not astonishing — with 30 observations, seeing one is unsurprising.

## 8. Visualisation

### 8.1 Histogram with a density curve

```python
fig, ax = plt.subplots(figsize=(7, 4.2))
sns.histplot(marks, bins=10, stat="density", color="#4c72b0",
             edgecolor="white", ax=ax, label="marks (density)")
xs = np.linspace(marks.min() - 5, marks.max() + 5, 200)
ax.plot(xs, stats.norm.pdf(xs, marks.mean(), marks.std(ddof=1)),
        color="#c44e52", linewidth=2, label="normal, same mean and sd")
ax.axvline(marks.mean(), color="black", linestyle="--", linewidth=1, label="mean")
ax.axvline(np.median(marks), color="grey", linestyle=":", linewidth=1.5, label="median")
ax.set(xlabel="Mark", ylabel="Density", title="Distribution of 30 examination marks")
ax.legend(frameon=False, fontsize=9)
fig.tight_layout()
plt.show()
```

### 8.2 Box plot, with the fences drawn

```python
fig, ax = plt.subplots(figsize=(7, 2.6))
sns.boxplot(x=marks, ax=ax, color="#dd8452", width=0.4)
ax.axvline(q1 - 1.5 * iqr, color="grey", linestyle="--", linewidth=1)
ax.axvline(q3 + 1.5 * iqr, color="grey", linestyle="--", linewidth=1)
ax.set(xlabel="Mark", title="Box plot: median, quartiles, whiskers and flagged points")
fig.tight_layout()
plt.show()
```

### 8.3 Empirical cumulative distribution

```python
fig, ax = plt.subplots(figsize=(7, 4))
sns.ecdfplot(marks, ax=ax, color="#55a868", linewidth=2)
for p in (0.25, 0.5, 0.75):
    ax.axhline(p, color="grey", linewidth=0.8, linestyle=":")
ax.set(xlabel="Mark", ylabel="Proportion at or below",
       title="ECDF: read any quantile directly off the curve")
fig.tight_layout()
plt.show()
```

**What the figures show.** The histogram is roughly bell-shaped but flatter than the
normal curve with the same mean and standard deviation, and it has a gap at the low
end where 45 sits alone. The box plot makes that visible as a point beyond the lower
whisker. The ECDF is the most informative of the three for quantiles: the height of
the curve at a mark is the proportion of students at or below it, so the median is
where the curve crosses 0.5.

## 9. Practical scenario

A departmental meeting asks two different questions about these marks.

**"What was a typical performance?"** Report the median and the IQR: "the median was
72.5, with the middle half between 67.25 and 78.75". The median is the right summary
because the question is about a typical student and the data contain extremes.

**"What total do we need to allocate for a prize based on the average?"** Report the
mean, 72.93, because a total is a sum and the mean is the sum divided by \(n\).
Averaging medians does not give a total.

That is the general rule: **use the mean when the arithmetic of totals matters, the
median when robustness to extremes matters, and always report a measure of spread
next to either.** A mean without a standard deviation invites over-reading.

## 10. Exercises

**Exercise 1.** Remove the value 45 and recompute the mean, median and sample
standard deviation. Which changed more, and why?

**Exercise 2.** Compute the coefficient of variation and interpret it in one
sentence. Would you compare the variability of marks (0–100) and heights (cm) using
standard deviations or CVs?

**Exercise 3.** Compute the z-score of 98. Is it beyond 2 standard deviations? What
proportion of a normal distribution lies beyond that z-score?

**Exercise 4.** Compute the 10th and 90th percentiles. State what they mean for a
student at the 10th percentile.

**Exercise 5.** The department proposes reporting the *mode* as the headline
statistic. Give one reason this is a poor choice for these data, and one situation
where the mode is the best of the three.

## 11. Solutions

```python
# Solution 1
reduced = marks[marks != 45]
print(f"n = {reduced.size}")
print(f"mean   {reduced.mean():.4f}  (was {marks.mean():.4f}, change {reduced.mean() - marks.mean():+.4f})")
print(f"median {np.median(reduced):.4f}  (was {np.median(marks):.4f}, change {np.median(reduced) - np.median(marks):+.4f})")
print(f"sd     {reduced.std(ddof=1):.4f}  (was {marks.std(ddof=1):.4f}, change {reduced.std(ddof=1) - marks.std(ddof=1):+.4f})")
```

The mean rises by about one mark and the median by half a mark, while the standard
deviation falls by about 1.1. The mean moved most because it uses the size of every
deviation; removing a value 28 marks below the mean shrinks the total and the
squared deviations at the same time.

```python
# Solution 2
cv = marks.std(ddof=1) / marks.mean()
print(f"CV = {cv:.4f}  ({cv:.1%} of the mean)")

# Solution 2 (written)
# A CV of about 0.16 says the standard deviation is 16% of the mean: for marks,
# typical variation of roughly one sixth of the average performance. To compare
# marks with heights, use the CV: standard deviations are in the units of the
# variable and cannot be compared across scales.
```

```python
# Solution 3
z98 = (98 - marks.mean()) / marks.std(ddof=1)
print(f"z(98) = {z98:.4f}")
print("beyond 2 sd?", z98 > 2)
print("normal tail beyond |z| =", f"{2 * (1 - stats.norm.cdf(abs(z98))):.4f}")
```

```python
# Solution 4
p10, p90 = np.quantile(marks, [0.10, 0.90])
print(f"10th percentile = {p10:.2f}, 90th percentile = {p90:.2f}")
print(f"students at or below the 10th percentile: {(marks <= p10).sum()} of {marks.size}")
```

A student at the 10th percentile scored 60.70, which is at or above only about 10% of
the class. The 10th and 90th percentiles bracket the central 80% of performance:
60.70 to 88.30.

```python
# Solution 5 (written)
# Poor choice: with 30 marks and repeated values, the mode is 68 with a count of
# only 2 — it describes 2 of 30 students and would change if one script were
# re-marked. It also throws away the magnitude of every other observation.
# Good situation: a categorical variable such as "most common grade band" or
# "most common mode of attendance", where the values have no arithmetic meaning
# and a mean is undefined.
```

## 12. Summary

- Mean, median and mode answer "where is the centre?"; report the median when
  extremes matter, the mean when totals do.
- Quartiles and the IQR describe spread in a way that ignores extremes; the sample
  standard deviation describes spread using every value.
- Divide by \(n-1\) for a sample, \(n\) for a population — and say which you used.
- The 1.5 × IQR rule flags candidates for inspection, not values to delete.
- Skewness and kurtosis describe shape, and are unstable in small samples.
- A histogram shows shape; a box plot shows the same information compactly and marks
  outliers; an ECDF lets you read any quantile directly.

Next: [Practical 02](02-mathematical-foundations.ipynb) works through the functions,
derivatives and integrals the later modules rely on.
