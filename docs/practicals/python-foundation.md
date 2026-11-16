---
title: Python foundation
description: The small subset of Python, NumPy, pandas and Matplotlib the practicals use — environment, types, arrays, functions, data loading and plotting.
---

# Python foundation

The eighteen practicals assume you can run a cell, create an array, call a function and
plot a column of a table. This page covers exactly that, and nothing more. It is not a
programming course: if you can already write a `for` loop and import `numpy`, read
Section 6 and start [Practical 01](notebooks/01-descriptive-statistics.ipynb).

The companion notebook is [Practical 00 — Python Foundation](notebooks/00-python-foundation.ipynb).
Every snippet below appears there, with output.

## 1. Environment and packages

Use a **virtual environment** so the course's package versions do not collide with other
projects. From the repository folder:

```bash
py -3.12 -m venv .venv          # Windows
python3.12 -m venv .venv        # macOS / Linux
source .venv/Scripts/activate   # Windows (Git Bash)
source .venv/bin/activate       # macOS / Linux
python -m pip install --upgrade pip
pip install -r requirements-course.txt
```

`requirements-course.txt` pins the stack: NumPy, pandas, SciPy, Matplotlib, Seaborn,
statsmodels, scikit-learn. The practicals use no other third-party library except
`scikit-learn` in Practical 18.

Check the installation:

```bash
python -c "import numpy, pandas, scipy, matplotlib, seaborn, statsmodels, sklearn; print('ok')"
```

If that raises `ModuleNotFoundError`, the environment is not activated — the prompt should
begin with `(.venv)`. This is the single most common setup problem, and it is not a code
error.

## 2. Jupyter

```bash
jupyter lab
```

A notebook is a list of cells. A cell is either **Markdown** (prose and mathematics) or
**Code** (executed by the kernel). `Shift+Enter` runs the current cell and moves to the
next.

Two habits prevent almost all confusion:

- **Run cells in order.** A notebook is a program with state; running cell 20 before
  cell 3 gives nonsense.
- **Restart and run all** before trusting any result (`Kernel → Restart Kernel and Run
  All Cells`). If a notebook only works in one particular order, it is broken.

## 3. Variables and data types

```python
n_students = 40          # int
mean_mark = 68.5         # float
course = "Probability"   # str
is_pass = True           # bool
```

| Type | Example | Watch out for |
|---|---|---|
| `int` | `42` | arbitrary precision |
| `float` | `3.5` | `0.1 + 0.2 != 0.3`; compare with `np.isclose` |
| `bool` | `True` | `True == 1`; `True + True == 2` |
| `str` | `"marks"` | text; concatenation, not addition |
| `None` | `None` | "no value"; not the same as `0` or `""` |

## 4. Lists and arrays

A **list** is a general container; arithmetic is not defined on it. A **NumPy array**
holds numbers of one dtype and supports elementwise arithmetic.

```python
marks_list = [72, 65, 81, 58, 90]
marks = np.array(marks_list)

marks_list + [100]        # concatenation -> [72, 65, 81, 58, 90, 100]
marks * 2                 # elementwise   -> [144, 130, 162, 116, 180]
marks.mean()              # 73.2
marks[marks > 70]         # boolean mask  -> [72, 81, 90]
(marks > 70).mean()       # proportion    -> 0.6
```

Boolean masks are the idiom the whole course uses: `array > threshold` produces `True`/
`False`, indexing with it selects, and `.mean()` of a boolean array is a proportion.

## 5. Basic mathematics

```python
marks.sum(), marks.min(), marks.max()
marks.mean()                       # arithmetic mean
marks.std(ddof=1)                  # SAMPLE standard deviation
marks.var(ddof=1)                  # SAMPLE variance
np.median(marks), np.quantile(marks, [0.25, 0.75])
np.log(x), np.exp(x), np.sqrt(x)   # elementwise
(marks - marks.mean()) / marks.std(ddof=1)   # z-scores
```

`ddof=1` is not optional detail. NumPy's default divides by \(n\) (population); every
interval and test in this course uses \(n-1\) (sample). Passing `ddof=1` is how you say
which one you mean.

## 6. Functions

```python
def summarise(values, name="data"):
    """Return n, mean and sample sd of a 1-D array."""
    values = np.asarray(values, dtype=float)
    if values.size < 2:
        raise ValueError("need at least two observations")
    return {"name": name, "n": values.size,
            "mean": values.mean(), "sd": values.std(ddof=1)}
```

Three habits: a docstring that states the assumption, a `raise` when the input cannot be
summarised, and a returned dict rather than a printed string — so the caller can use the
pieces.

## 7. Data loading

```python
import pandas as pd

df = pd.read_csv("marks.csv")     # also read_excel, read_json, read_parquet
df.shape                          # (rows, columns)
df.dtypes                         # is anything text that should be numeric?
df.head()
df.isna().sum()                   # missing values per column
df.describe()                     # count, mean, sd, quartiles, extremes
df.groupby("programme")["final"].mean()
```

The first pass on any new file is those five commands. They take a minute and find most
of the problems that otherwise cost an afternoon.

## 8. Plotting

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(df["final"], bins=20, edgecolor="white")
ax.set(xlabel="Final mark (out of 100)", ylabel="Number of students",
       title="Distribution of final marks")
fig.tight_layout()
plt.show()
```

A figure needs a title that states the finding and axes that state the units. Bars start
at zero; marker area, not radius, encodes a value; export PDF for documents and PNG at
high dpi for screens.

## 9. Reproducibility

Every practical that simulates fixes a seed:

```python
rng = np.random.default_rng(2026)
sample = rng.normal(0, 1, size=1000)
```

Using the generator object (`default_rng`) rather than the legacy global `np.random`
keeps the seed local, so two notebooks cannot interfere. When you change a simulation,
change the seed only if you intend the numbers to change.

## Where to go next

- [Practical 00](notebooks/00-python-foundation.ipynb) — the same material, executable.
- [Practical 01](notebooks/01-descriptive-statistics.ipynb) — descriptive statistics from
  examination data.
- [Notebook index](index.md) — all nineteen notebooks with their chapters.
