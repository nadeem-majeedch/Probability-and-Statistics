# Practical 00 — Python Foundation for the Course

## 1. Introduction

This notebook is the bridge between "I have Python installed" and "I can work
through Practical 01". It is deliberately short. It covers only what the eighteen
course notebooks actually use: variables and types, lists versus arrays, the
arithmetic you will need, functions, reading a data file, and drawing a labelled
plot.

It is **not** a Python course. If you can already write a `for` loop, define a
function and import `numpy`, skim Section 6 and go to Practical 01.

Everything here runs offline and needs no data file: the small dataset is
created in code, so there is nothing to download.

## 2. Learning objectives

By the end of this notebook you can:

1. Create and activate a virtual environment and install the course libraries.
2. Open JupyterLab and run, edit and re-run a cell.
3. Explain the difference between a Python list and a NumPy array.
4. Write a function with a docstring and call it twice with different arguments.
5. Read a CSV file into a pandas DataFrame and inspect its shape and dtypes.
6. Draw a labelled line plot and save it as a PNG.

## 3. Required libraries

| Library | Used for |
|---|---|
| `numpy` | arrays and vectorised arithmetic |
| `pandas` | tabular data (DataFrames) |
| `matplotlib` | plots |

Standard library only, otherwise: `pathlib`, `tempfile`, `statistics`.

## 4. Concepts

### 4.1 Environment, packages, Jupyter

A **virtual environment** is a private folder of packages. It keeps this course's
versions from colliding with other projects. From the repository folder:

```bash
py -3.12 -m venv .venv          # Windows
python3.12 -m venv .venv        # macOS / Linux
source .venv/Scripts/activate   # Windows (Git Bash)
source .venv/bin/activate       # macOS / Linux
pip install -r requirements-course.txt
jupyter lab
```

**JupyterLab** runs a local server and opens a browser tab. A notebook is a list of
cells. A cell is either *Markdown* (prose, rendered when you run it) or *Code*
(executed by the kernel). `Shift+Enter` runs the current cell and moves down.

Two habits prevent most confusion:

- **Run cells in order.** A notebook is a program with state; running cell 20 before
  cell 3 gives nonsense.
- **Restart and run all** before you trust a result (`Kernel → Restart Kernel and Run
  All Cells`). If it only works in one particular order, it is broken.

### 4.2 Variables and data types

A variable is a name bound to an object. The type determines what operations are
allowed.

| Type | Example | Notes |
|---|---|---|
| `int` | `42` | whole numbers, arbitrary size |
| `float` | `3.5` | binary floating point; `0.1 + 0.2 != 0.3` exactly |
| `bool` | `True` | `True == 1` |
| `str` | `"marks"` | text |
| `NoneType` | `None` | "no value" |

### 4.3 Lists versus arrays

A **list** is a general container: it can hold anything, and arithmetic is not
defined on it (`[1, 2] + [3]` concatenates). A **NumPy array** holds numbers of one
dtype and supports elementwise arithmetic, which is both shorter and much faster.

```text
list:  [1, 2, 3] * 2      -> [1, 2, 3, 1, 2, 3]
array: np.array([1,2,3])*2 -> [2, 4, 6]
```

### 4.4 Functions

A function packages a calculation so it can be tested and reused. The essential
pieces: a name, parameters, a body, a returned value, and a docstring that states
what it assumes.

## 5. Formulas

The arithmetic this course builds on, written once so the code has something to
check against. For observations \(x_1,\dots,x_n\):

\[ \bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i, \qquad
   s^{2}=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^{2}, \qquad
   s=\sqrt{s^{2}}. \]

A **z-score** rescales by the mean and standard deviation:

\[ z_i=\frac{x_i-\bar{x}}{s}. \]

A **linear model** predicts one variable from another:

\[ \hat{y}=b_0+b_1x. \]

Section 6 computes the first three by hand (with `sum` and a loop) and then with
NumPy, so you can see that the library is doing exactly the formula.

## 6. Implementation

### 6.1 Check the environment

The next cell prints the versions actually loaded. If it raises
`ModuleNotFoundError`, the environment is not activated — go back to Section 4.1.

```python
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Python     ", sys.version.split()[0])
print("NumPy      ", np.__version__)
print("pandas     ", pd.__version__)
print("Matplotlib ", plt.matplotlib.__version__)
```

### 6.2 Variables, types and the floating-point surprise

```python
n_students = 40          # int
mean_mark = 68.5         # float
course = "Probability"   # str
is_pass = True           # bool

for name, value in [("n_students", n_students), ("mean_mark", mean_mark),
                    ("course", course), ("is_pass", is_pass)]:
    print(f"{name:12s} = {value!r:15} type = {type(value).__name__}")

print()
print("0.1 + 0.2 ==", 0.1 + 0.2, " equals 0.3?", 0.1 + 0.2 == 0.3)
print("difference from 0.3:", abs((0.1 + 0.2) - 0.3))
```

The last two lines are not a bug to fix but a fact to remember: binary floats
cannot represent 0.1 or 0.2 exactly. Compare floats with `np.isclose`, never with
`==`, and round only when you *print*.

### 6.3 Lists and arrays

```python
marks_list = [72, 65, 81, 58, 90]
marks_array = np.array(marks_list)

print("list + list :", marks_list + [100])
print("array * 2   :", marks_array * 2)
print("array mean  :", marks_array.mean())
print("array dtype :", marks_array.dtype, " shape:", marks_array.shape)

# Boolean masks select elements; this is the idiom the whole course uses.
print("marks above 70:", marks_array[marks_array > 70])
print("share above 70:", (marks_array > 70).mean())
```

Lists concatenate and arrays broadcast. The mask `marks_array > 70` is an array of
`True`/`False`; indexing with it keeps the `True` positions, and `.mean()` of a
boolean array is the proportion of `True`.

### 6.4 Arithmetic, by hand and with NumPy

```python
marks = np.array([72, 65, 81, 58, 90, 77, 63, 85])

# by hand: the formulas from Section 5
n = len(marks)
mean_manual = sum(marks) / n
var_manual = sum((x - mean_manual) ** 2 for x in marks) / (n - 1)
sd_manual = var_manual ** 0.5

# with NumPy
mean_np = marks.mean()
var_np = marks.var(ddof=1)       # ddof=1 -> divide by n-1, the sample variance
sd_np = marks.std(ddof=1)

print(f"mean   manual {mean_manual:8.4f}   numpy {mean_np:8.4f}")
print(f"var    manual {var_manual:8.4f}   numpy {var_np:8.4f}")
print(f"sd     manual {sd_manual:8.4f}   numpy {sd_np:8.4f}")
print("identical?", np.isclose(mean_manual, mean_np),
      np.isclose(var_manual, var_np), np.isclose(sd_manual, sd_np))

z = (marks - marks.mean()) / marks.std(ddof=1)
print("\nz-scores:", np.round(z, 2))
print("z-scores have mean", round(z.mean(), 10), "and sd", round(z.std(ddof=1), 10))
```

`ddof=1` matters. NumPy's default `var()` divides by \(n\), which is the
**population** formula. The sample variance divides by \(n-1\), and every interval
and test in this course uses the sample version.

### 6.5 A function with a docstring

```python
def summarise(values, name="data"):
    """Return a one-line summary of a 1-D array of numbers.

    Assumes at least two finite observations; returns a dict so the caller can
    use individual pieces instead of parsing a string.
    """
    values = np.asarray(values, dtype=float)
    if values.size < 2:
        raise ValueError("need at least two observations")
    return {
        "name": name,
        "n": values.size,
        "mean": float(values.mean()),
        "median": float(np.median(values)),
        "sd": float(values.std(ddof=1)),
        "min": float(values.min()),
        "max": float(values.max()),
    }


for label, data in [("midterm", marks), ("final", marks + 4)]:
    s = summarise(data, label)
    print(f"{s['name']:8s} n={s['n']:3d} mean={s['mean']:6.2f} "
          f"median={s['median']:6.2f} sd={s['sd']:5.2f} "
          f"range=({s['min']:.0f}, {s['max']:.0f})")
```

Two calls, same code, different answers — the point of a function. The `raise`
line is the assumption made explicit: the function refuses input it cannot
summarise rather than returning a meaningless number.

### 6.6 Data loading: a CSV round trip

Real projects load files. To keep this notebook self-contained, the next cell
writes a small CSV to a temporary directory, reads it back, and lets the directory
be deleted — the same pattern works with any file you own.

```python
import tempfile

records = pd.DataFrame({
    "student_id": range(1, 9),
    "programme": ["DS"] * 5 + ["CS"] * 3,
    "midterm": [72, 65, 81, 58, 90, 77, 63, 85],
    "final": [75, 68, 79, 62, 88, 80, 66, 82],
})

with tempfile.TemporaryDirectory() as tmp:
    path = Path(tmp) / "marks.csv"
    records.to_csv(path, index=False)
    print("wrote", path.name, "of", path.stat().st_size, "bytes")
    loaded = pd.read_csv(path)

print("shape:", loaded.shape)
print("columns:", list(loaded.columns))
print(loaded.dtypes.to_string())
loaded.head()
```

```python
# A first look at the table, using the idioms you will repeat all course.
print(loaded.describe().round(2).to_string())
print()
print("mean by programme:")
print(loaded.groupby("programme")[["midterm", "final"]].mean().round(2).to_string())
```

`read_csv` infers types from the text; `describe()` gives count, mean, standard
deviation, quartiles and extremes for numeric columns; `groupby(...).mean()`
computes a summary per category. These three lines answer most first questions
about a new dataset.

## 7. Output and interpretation

Reading the output above in statistical language:

- The eight midterm marks average 73.9 with a standard deviation of 11.1. A typical
  mark is therefore about 74 ± 11; the range 58–90 is consistent with that.
- The **median** (74.5) is close to the mean, so this small sample is not strongly
  skewed. With \(n=8\) that is weak evidence — a single extreme mark would move the
  mean far more than the median.
- The z-scores sum to approximately zero and have standard deviation 1, which is
  what the formula guarantees: standardising does not change the shape, only the
  centre and scale.
- `groupby("programme")` shows the DS group's mean is higher on both assessments.
  With five and three students this is a description of these eight people, not
  evidence about programmes — a distinction Module 15 makes precise.

## 8. Visualisation

A plot is an argument, so it needs a title, labelled axes and units. The next cell
draws the two assessments against each other and adds the identity line: points
above it improved.

```python
fig, ax = plt.subplots(figsize=(6, 4.5))
ax.scatter(records["midterm"], records["final"], s=60, alpha=0.8,
           edgecolor="white", label="student")
lims = [50, 95]
ax.plot(lims, lims, linestyle="--", color="grey", linewidth=1,
        label="final = midterm")
ax.set(xlim=lims, ylim=lims,
       xlabel="Midterm mark", ylabel="Final mark",
       title="Eight students: final against midterm")
ax.legend(frameon=False)
ax.grid(alpha=0.3)
fig.tight_layout()
plt.show()
```

```python
# Saving a figure: use a real path you control, and a vector format for reports.
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    out = Path(tmp) / "scatter.png"
    fig.savefig(out, dpi=120)
    print("saved", out.name, "of", out.stat().st_size, "bytes")
```

Most points lie near the dashed line, and six of eight lie above it, which matches
the summary statistics (final mean 75.0 against midterm 73.9). A plot like this is
how you notice an outlier or a ceiling effect before computing anything.

## 9. Practical scenario

You are handed `marks.csv` from a colleague: 8 rows, 4 columns, no documentation.
The professional first pass is exactly what this notebook did:

1. `shape` and `dtypes` — how much data, and is anything stored as text that should
   be numeric?
2. `head()` — do the values make sense?
3. `describe()` — centre, spread, range, and whether the mean and median agree.
4. One plot — is the relationship roughly linear, and are there outliers?
5. Only then a model or a test.

Steps 1–4 take a minute and prevent most of the errors that take an afternoon to
find later.

## 10. Exercises

**Exercise 1.** Create an array of the five numbers 4, 8, 15, 16, 23 and print its
mean, sample standard deviation and maximum.

**Exercise 2.** Write a function `cv(values)` returning the coefficient of
variation \(s/\bar{x}\), and use it to compare the midterm and final marks. Which
assessment is more variable relative to its mean?

**Exercise 3.** Using `records`, compute the pass rate (mark ≥ 60) for the final
assessment with a boolean mask, and print it as a percentage.

**Exercise 4.** Add a column `improved` that is `True` when the final mark exceeds
the midterm mark, then count how many students improved.

**Exercise 5.** Explain in one sentence why `marks.var()` and `marks.var(ddof=1)`
differ, and which one a confidence interval for the mean uses.

## 11. Solutions

```python
# Solution 1
a = np.array([4, 8, 15, 16, 23])
print("mean", a.mean(), "sd", round(a.std(ddof=1), 4), "max", a.max())
```

```python
# Solution 2
def cv(values):
    """Coefficient of variation: sample sd divided by the mean."""
    values = np.asarray(values, dtype=float)
    return values.std(ddof=1) / values.mean()

print(f"midterm cv = {cv(records['midterm']):.3f}")
print(f"final   cv = {cv(records['final']):.3f}")
```

The midterm has the larger coefficient of variation, so relative to its own mean it
is the more variable assessment — even though the two standard deviations are
similar.

```python
# Solution 3
pass_rate = (records["final"] >= 60).mean()
print(f"pass rate: {pass_rate:.1%} ({(records['final'] >= 60).sum()} of {len(records)})")
```

```python
# Solution 4
records = records.assign(improved=records["final"] > records["midterm"])
print(records[["student_id", "midterm", "final", "improved"]].to_string(index=False))
print("improved:", int(records["improved"].sum()), "of", len(records))
```

```python
# Solution 5 (written)
# `var()` divides the sum of squared deviations by n: the population variance,
# treating the data as the whole population. `var(ddof=1)` divides by n-1: the
# sample variance, which is unbiased for the population variance. Every
# confidence interval and test in this course uses ddof=1, because the data are
# a sample from a larger population.
```

## 12. Summary

- A virtual environment isolates the course libraries; `pip install -r
  requirements-course.txt` reproduces them.
- Jupyter cells run in order and share state; "Restart and run all" is the test of a
  working notebook.
- Lists concatenate, arrays compute. Use arrays for data and lists for collections of
  mixed things.
- `ddof=1` gives the sample variance; the default `ddof=0` is the population version.
- Functions with docstrings and explicit `raise` statements are how assumptions stay
  visible.
- The first pass on any dataset: shape, dtypes, head, describe, one plot.

Next: [Practical 01](01-descriptive-statistics.ipynb) applies these tools to
descriptive statistics — centre, spread, and the plots that show them.
