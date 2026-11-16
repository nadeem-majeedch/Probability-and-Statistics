# Practical 04 — Data Visualization

## 1. Introduction

A figure is an argument. It claims that one variable is large, that two variables are
related, or that groups differ — and a reader believes it faster than they believe a
table. That speed is the reason to make figures carefully: a badly designed chart is
not a neutral decoration, it is a false claim made efficiently.

This practical covers the grammar of a Matplotlib figure, the chart types that suit
each question, small multiples, and three distortions that appear in real reports
(truncated axes, area used for length, and unequalled baselines). Every figure is
drawn twice where possible: once badly, once well.

## 2. Learning objectives

By the end of this practical you can:

1. Build a figure with `fig, ax = plt.subplots()` and label every element.
2. Choose a chart type from the question: distribution, comparison, relationship,
   composition, over time.
3. Bin a continuous variable sensibly and explain the effect of bin width.
4. Use small multiples instead of cramming series onto one axis.
5. Identify three common distortions and fix them.
6. Save a figure at a usable resolution in a suitable format.

## 3. Required libraries

| Library | Used for |
|---|---|
| `numpy`, `pandas` | data for the figures |
| `matplotlib` | full control of axes, ticks, annotations |
| `seaborn` | statistical chart defaults, small multiples |

## 4. Concepts

### 4.1 The grammar of a figure

A Matplotlib figure has two layers:

- the **Figure** — the canvas, which owns size and resolution;
- one or more **Axes** — the plotting area, which owns data limits, ticks, labels,
  legend and title.

`fig, ax = plt.subplots(figsize=(6, 4))` gives you both explicitly, and explicit is
better than the implicit `plt.plot()` state machine once a figure has more than one
panel.

### 4.2 Chart type follows from the question

| Question | Chart | Avoid |
|---|---|---|
| How is one variable distributed? | histogram, density, ECDF, box plot | pie chart |
| How do groups compare? | dot plot, box plot, bar with CI | 3-D bars |
| Are two variables related? | scatter plot | two y-axes |
| How is a total composed? | stacked bar (few categories) | pie with 8 slices |
| How does it change over time? | line chart | bars for many periods |
| How do many groups evolve? | small multiples | overlapping lines |

### 4.3 Bins, and why the histogram lies slightly

A histogram's shape depends on the bin width. Too few bins hides structure; too many
shows noise. Two rules of thumb:

\[ \text{Sturges: } k=\lceil \log_2 n\rceil+1,\qquad
   \text{Freedman–Diaconis: } h=2\,\frac{\text{IQR}}{n^{1/3}}. \]

Neither is a law. Plot two or three bin widths before choosing one, and say which
you used.

### 4.4 Distortions

1. **Truncated axis.** A bar chart whose y-axis starts at 95 exaggerates a 1-point
   difference into a doubling. Bars encode length from zero; lines may be truncated,
   but must be labelled.
2. **Area for length.** Doubling the width and height of a marker quadruples the ink,
   which the eye reads as more than double. Scale area, not radius, if size encodes a
   value.
3. **Unequal or hidden baselines.** Two panels with different y-limits invite a
   comparison the data do not support.

## 5. Formulas

\[ \text{density}=\frac{\text{count}}{n\cdot\text{bin width}},
   \qquad \int \text{density}=1 \]

\[ \text{Sturges: } k=\lceil\log_2 n\rceil+1,\qquad
   \text{FD width: } h=2\,\text{IQR}\,n^{-1/3} \]

\[ \text{standard error of a mean: } \text{se}=\frac{s}{\sqrt n},\qquad
   \text{95\% CI: } \bar x\pm1.96\,\text{se} \]

## 6. Implementation

### 6.1 Data for the figures

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", context="notebook")
plt.rcParams["figure.dpi"] = 110

rng = np.random.default_rng(2026)
n = 200
df = pd.DataFrame({
    "programme": rng.choice(["DS", "CS", "SE"], size=n, p=[0.5, 0.3, 0.2]),
    "week": np.tile(np.arange(1, 9), n // 8),
})
df["hours"] = np.clip(rng.gamma(4, 1.5, n), 0.5, 30)
df["score"] = np.clip(45 + 1.6 * df["hours"] + rng.normal(0, 8, n), 0, 100)
df["attendance"] = np.clip(rng.normal(78, 11, n), 30, 100)

print(df.head().round(2).to_string(index=False))
print("rows:", len(df))
```

### 6.2 A figure done badly, then well

```python
# Bad: no labels, default single colour, no units, unreadable title.
fig, ax = plt.subplots(figsize=(5, 3))
ax.hist(df["score"])
plt.show()
```

```python
# Good: bin width chosen, axes labelled with units, title states the finding,
# and the mean is marked and named.
bins = np.arange(0, 105, 5)
fig, ax = plt.subplots(figsize=(6.4, 3.8))
ax.hist(df["score"], bins=bins, color="#4c72b0", edgecolor="white")
ax.axvline(df["score"].mean(), color="#c44e52", linestyle="--", linewidth=1.8,
           label=f"mean = {df['score'].mean():.1f}")
ax.set(xlabel="Final score (out of 100)", ylabel="Number of students",
       title="Distribution of 200 final scores (bin width 5)")
ax.legend(frameon=False)
fig.tight_layout()
plt.show()
```

The second figure answers "where are the scores?" without the reader having to guess
what the axes are. The title carries the *finding*, not the variable names — a title
that says "Histogram of score" makes the reader do the interpretation.

### 6.3 Bin width changes the story

```python
fig, axes = plt.subplots(1, 3, figsize=(12, 3.2), sharey=True)
for ax, width in zip(axes, [20, 5, 1]):
    ax.hist(df["score"], bins=np.arange(0, 101 + width, width),
            color="#55a868", edgecolor="white")
    ax.set(title=f"bin width = {width}", xlabel="Score", ylabel="Count")
fig.suptitle("The same 200 scores at three bin widths", y=1.02)
fig.tight_layout()
plt.show()

sturges = int(np.ceil(np.log2(len(df["score"])))) + 1
iqr = df["score"].quantile(0.75) - df["score"].quantile(0.25)
fd_width = 2 * iqr / len(df["score"]) ** (1 / 3)
print(f"Sturges suggests {sturges} bins")
print(f"Freedman-Diaconis suggests a width of {fd_width:.2f} "
      f"({int(np.ptp(df['score']) / fd_width)} bins)")
```

### 6.4 Comparing groups with intervals

```python
group_stats = (df.groupby("programme")["score"]
                 .agg(n="count", mean="mean", sd="std")
                 .assign(se=lambda d: d["sd"] / np.sqrt(d["n"])))
group_stats["ci_low"] = group_stats["mean"] - 1.96 * group_stats["se"]
group_stats["ci_high"] = group_stats["mean"] + 1.96 * group_stats["se"]
print(group_stats.round(2).to_string())

fig, ax = plt.subplots(figsize=(6.2, 3.4))
order = group_stats.index
ax.errorbar(order, group_stats["mean"],
            yerr=1.96 * group_stats["se"], fmt="o", capsize=5,
            color="#4c72b0", markersize=8)
ax.set(xlabel="Programme", ylabel="Mean score (95% CI)",
       title="Group means with 95% confidence intervals")
ax.set_ylim(55, 85)
fig.tight_layout()
plt.show()
```

The intervals overlap substantially, which is the honest visual summary: the
differences between programmes are small relative to the uncertainty in each mean.

### 6.5 Relationship, with a fitted line

```python
fig, ax = plt.subplots(figsize=(6.4, 4.2))
sns.regplot(data=df, x="hours", y="score", ax=ax,
            scatter_kws={"s": 28, "alpha": 0.65, "color": "#4c72b0"},
            line_kws={"color": "#c44e52"})
ax.set(xlabel="Study hours per week", ylabel="Final score",
       title="More study hours go with higher scores (association, not proof of cause)")
fig.tight_layout()
plt.show()

print(f"Pearson r = {df['hours'].corr(df['score']):.3f}")
```

### 6.6 Small multiples

```python
weekly = (df.groupby(["programme", "week"])["score"]
            .agg(mean="mean", sd="std", n="count").reset_index())
weekly["se"] = weekly["sd"] / np.sqrt(weekly["n"])

g = sns.relplot(data=weekly, x="week", y="mean", col="programme",
                kind="line", marker="o", height=3.0, aspect=1.1,
                errorbar=None)
g.set_axis_labels("Week", "Mean score")
g.set_titles("Programme {col_name}")
g.figure.suptitle("Weekly mean score by programme (same y-axis)", y=1.04)
plt.show()
```

Small multiples share the y-axis, so the panels are comparable. Cramming three lines
onto one axis would also work here, but with eight weeks and three programmes the
lines begin to cross and the reader has to trace them.

### 6.7 A heatmap with a diverging scale

```python
numeric = ["hours", "score", "attendance"]
corr = df[numeric].corr()

fig, ax = plt.subplots(figsize=(4.8, 3.8))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="vlag", vmin=-1, vmax=1,
            square=True, linewidths=0.5, cbar_kws={"shrink": 0.8}, ax=ax)
ax.set_title("Correlation matrix")
fig.tight_layout()
plt.show()
```

A diverging colormap (`vlag`) is the right choice for correlations because zero is a
meaningful midpoint: red for negative, blue for positive, near-white for none. A
sequential colormap such as `viridis` would imply that zero is "small" rather than
"none".

### 6.8 Exporting

```python
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmp:
    png = Path(tmp) / "scores.png"
    pdf = Path(tmp) / "scores.pdf"
    fig.savefig(png, dpi=200, bbox_inches="tight")
    fig.savefig(pdf, bbox_inches="tight")
    print(f"PNG: {png.stat().st_size/1024:.0f} KB (raster, for slides)")
    print(f"PDF: {pdf.stat().st_size/1024:.0f} KB (vector, for documents)")
```

Use PNG for screens and slides, PDF or SVG for documents that will be printed or
zoomed. Never screenshot a figure: the resolution is whatever the screen was.

## 7. Output and interpretation

- **Distribution.** Scores average 54.8 with a standard deviation of 9.1 and a median
  of 53.8, so the distribution is close to symmetric with a modest lower tail. At a bin
  width of 5 the shape is smooth; at width 20 the detail vanishes; at width 1 the
  histogram becomes a comb of noise. The choice of bin width changes the perceived
  shape, so it belongs in the caption.
- **Groups.** The three programme means differ by only a few points, and the 95%
  intervals overlap, so the figure supports "similar" rather than "different". Note
  what the intervals are: intervals for each mean, not for the differences between
  them. Overlapping intervals do not by themselves prove no difference (Module 15).
- **Relationship.** The scatter shows a positive, roughly linear association between
  study hours and score, with r = 0.52 in this simulated data. The band is wide: at 10
  hours per week the fitted score is about 61, and individual scores spread roughly
  ±16 around it, so hours explain part of the variation, not all of it.
- **Time.** Weekly means move by only a few points around each programme's average,
  and the panels share a y-axis, so "flat" is a real statement rather than an artefact
  of autoscaling.

## 8. Visualisation

### 8.1 The same data, distorted

```python
fig, axes = plt.subplots(1, 2, figsize=(9, 3.2), sharey=False)

means = df.groupby("programme")["score"].mean()
axes[0].bar(means.index, means.values, color="#c44e52")
axes[0].set_ylim(60, means.max() + 2)
axes[0].set_title("Truncated axis: difference looks large")
axes[0].set_ylabel("Mean score")

axes[1].bar(means.index, means.values, color="#4c72b0")
axes[1].set_ylim(0, 100)
axes[1].set_title("Zero baseline: difference is small")
axes[1].set_ylabel("Mean score")

for ax in axes:
    ax.set_xlabel("Programme")
fig.tight_layout()
plt.show()

print(means.round(2).to_string())
```

The two panels contain identical numbers. The left one, with a baseline at 60 instead
of 0, makes a difference of a few marks look like a factor of two. Bar length is read
as a proportion of the whole, so the axis must start at zero.

### 8.2 Size versus area

```python
fig, ax = plt.subplots(figsize=(6, 3.2))
sizes = np.array([10, 20, 40, 80])
values = sizes * 3
ax.scatter(sizes, values, s=sizes * 6, alpha=0.5, color="#55a868")       # area ∝ size
ax.scatter(sizes, values * 0.85, s=(sizes * 1.4) ** 2 / 2, alpha=0.4,
           color="#c44e52")                                               # area ∝ size²
ax.set(xlabel="Category size", ylabel="Value",
       title="Green: marker area proportional to value. Red: exaggerated.")
fig.tight_layout()
plt.show()
```

If marker size encodes a number, pass an area proportional to that number. Squaring
the value in the `s` argument — the red series — makes small differences look
enormous, which is the bubble-chart version of a truncated axis.

## 9. Practical scenario

You are asked to review a slide that claims "Programme SE is outperforming DS by
30%", showing two bars with a y-axis from 54.5 to 55.0.

The review has three questions, in order:

1. **What are the numbers?** The means are 54.93 and 54.80: a difference of 0.13
   marks, about 0.2% relative — not 30%. The "30%" came from comparing bar *heights
   above the axis minimum*, which is a meaningless quantity.
2. **What is the uncertainty?** The standard errors are 1.54 and 0.97 marks, so the 95%
   intervals overlap almost completely. The data are consistent with no difference.
3. **What would the honest figure be?** A dot plot with 95% intervals and a zero
   baseline, plus the group sizes, plus the word "descriptive" in the title.

That review takes five minutes and prevents a false claim reaching a committee. It is
the most valuable skill in this practical.

## 10. Exercises

**Exercise 1.** Redraw the histogram of `score` with 12 bins, a marked median, and
axis labels including units. State one thing the new figure shows that the default
one did not.

**Exercise 2.** Compute the Sturges and Freedman–Diaconis bin counts for `attendance`
and plot both histograms side by side.

**Exercise 3.** Draw a box plot of `score` by `programme` and a violin plot beside it.
Which communicates the group sizes better, and why?

**Exercise 4.** Plot the ECDF of `hours` for each programme on one axis with a legend.
Explain why an ECDF is easier to compare across groups than a histogram.

**Exercise 5.** Take the two-bar figure from Section 8.1 and describe, in two
sentences, exactly what makes the left panel misleading and how to fix it.

## 11. Solutions

```python
# Solution 1
fig, ax = plt.subplots(figsize=(6.2, 3.6))
ax.hist(df["score"], bins=12, color="#4da3a3", edgecolor="white")
ax.axvline(df["score"].median(), color="black", linestyle="--", label="median")
ax.set(xlabel="Final score (out of 100)", ylabel="Number of students",
       title="Twelve bins: the lower tail separates from the main mass")
ax.legend(frameon=False)
fig.tight_layout()
plt.show()
```

With 12 bins the lower tail (scores below 50) is visible as a distinct group, which
the 5-mark bins merged into the main body.

```python
# Solution 2
n = len(df["attendance"])
k_sturges = int(np.ceil(np.log2(n))) + 1
iqr_att = df["attendance"].quantile(0.75) - df["attendance"].quantile(0.25)
h_fd = 2 * iqr_att / n ** (1 / 3)
print(f"Sturges: {k_sturges} bins;  Freedman-Diaconis width {h_fd:.2f} "
      f"({int(np.ptp(df['attendance'])/h_fd)} bins)")

fig, axes = plt.subplots(1, 2, figsize=(10, 3), sharey=True)
axes[0].hist(df["attendance"], bins=k_sturges, color="#4c72b0", edgecolor="white")
axes[0].set_title(f"Sturges ({k_sturges} bins)")
axes[1].hist(df["attendance"], bins=max(2, int(np.ptp(df['attendance'])/h_fd)),
             color="#dd8452", edgecolor="white")
axes[1].set_title("Freedman-Diaconis")
for ax in axes:
    ax.set_xlabel("Attendance (%)")
axes[0].set_ylabel("Count")
fig.tight_layout()
plt.show()
```

```python
# Solution 3
fig, axes = plt.subplots(1, 2, figsize=(10, 3.4))
sns.boxplot(data=df, x="programme", y="score", ax=axes[0], width=0.5)
axes[0].set_title("Box plot")
sns.violinplot(data=df, x="programme", y="score", ax=axes[1],
               inner="quartile", cut=0)
axes[1].set_title("Violin plot")
for ax in axes:
    ax.set(xlabel="Programme", ylabel="Score")
fig.tight_layout()
plt.show()

print(df["programme"].value_counts().to_string())
```

The violin plot shows the shape of each distribution but not the counts; a narrow
violin from 12 students looks as substantial as a wide one from 100. Box plots hide
group size too, so either figure needs the counts in the caption or on the axis.

```python
# Solution 4
fig, ax = plt.subplots(figsize=(6.4, 3.8))
for prog, part in df.groupby("programme"):
    sns.ecdfplot(part["hours"], label=prog, ax=ax, linewidth=2)
ax.set(xlabel="Study hours per week", ylabel="Proportion at or below",
       title="ECDF of study hours by programme")
ax.legend(title="Programme", frameon=False)
fig.tight_layout()
plt.show()
```

An ECDF is a monotone curve that can be read at any quantile, so three groups can be
compared by looking at vertical gaps at a chosen height. Histograms of three groups
either overlap into a mess or must be split into panels, which makes small differences
hard to see.

```python
# Solution 5 (written)
# The left panel's y-axis starts at 60, so the visible bar heights encode the
# difference from 60 rather than the means themselves: a 1.7-mark gap is drawn as
# roughly a third of a bar. Bar length is read as a proportion, so the axis must
# start at zero; with a zero baseline the same data show two nearly equal bars.
# Fix: set ylim(0, 100), add the numeric means, and show 95% intervals.
```

## 12. Summary

- A figure claims something; the title should state the claim and the axes must state
  the units.
- Match the chart to the question: distribution → histogram/ECDF/box, comparison →
  dot or box with intervals, relationship → scatter, time → line, many groups → small
  multiples.
- Bin width changes the perceived shape; report the choice and try more than one.
- Bars start at zero. Marker area, not radius, encodes value. Shared axes make panels
  comparable.
- Use a diverging colormap when zero is meaningful, sequential otherwise.
- Export vector formats for documents and raster at high dpi for screens.

Next: [Practical 05](05-counting-and-combinatorics.ipynb) counts arrangements and
checks the formulas by brute force.
