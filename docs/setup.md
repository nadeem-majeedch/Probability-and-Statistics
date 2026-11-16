---
title: Set up your computer
description: Install Python, Jupyter and the course libraries on Windows, macOS or Linux — all free and open source.
---

# Set up your computer

You need Python and a handful of free libraries. There is nothing to buy, no
licence key, no account and no cloud service anywhere in this course.

**This page takes about 20 minutes.** Do it before Module 01 so that the first
demonstration you meet is one you can run.

!!! warning "Use Python 3.12 or 3.13 — not 3.14 or newer"

    Parts of the scientific stack depend on compiled packages that appear some
    months after a new Python release. On a brand-new interpreter, `pip install`
    can fail in ways that are not your fault and are hard to diagnose. Python
    3.12 is the most reliable choice for this course.

## 1. Check what you have

Open a terminal (Windows: **Git Bash** or **PowerShell**; macOS/Linux: Terminal)
and run:

```bash
python --version
```

If you see 3.12 or 3.13, skip to step 3. If you see 3.14 or newer, or an error,
continue.

## 2. Install Python 3.12

**Windows.** Download the installer from
[python.org/downloads](https://www.python.org/downloads/release/python-3129/).
During installation, tick **"Add python.exe to PATH"** — this is the single most
common source of setup problems. Then verify:

```bash
py -3.12 --version
```

**macOS.** Use Homebrew, or the official installer:

```bash
brew install python@3.12
python3.12 --version
```

**Linux (Ubuntu/Debian).**

```bash
sudo apt update
sudo apt install python3.12 python3.12-venv python3-pip
python3.12 --version
```

If your distribution does not package 3.12, install
[`uv`](https://docs.astral.sh/uv/) and let it fetch an interpreter:

```bash
uv python install 3.12
```

## 3. Create a project environment

Never install course packages into the system Python. A virtual environment keeps
this course's libraries separate from everything else on your machine.

```bash
# from the repository folder
py -3.12 -m venv .venv          # Windows
python3.12 -m venv .venv        # macOS / Linux

# activate it
source .venv/Scripts/activate   # Windows (Git Bash)
source .venv/bin/activate       # macOS / Linux
```

Your prompt should now start with `(.venv)`. If it does not, the activation path
is wrong — check that `.venv` exists in the folder you are in.

## 4. Install the libraries

The course ships a requirements file listing exactly what is needed:

```bash
python -m pip install --upgrade pip
pip install -r requirements-course.txt
```

This installs NumPy, pandas, SciPy, Matplotlib, Seaborn, Plotly, statsmodels,
scikit-learn, SymPy, Pingouin and JupyterLab. It takes a few minutes.

If you prefer `uv` (much faster, same result):

```bash
uv venv --python 3.12
uv pip install -r requirements-course.txt
```

## 5. Verify the installation

Run this in the environment where you installed the libraries:

```bash
python -c "import numpy, scipy, pandas, matplotlib, seaborn, statsmodels, sklearn, sympy; print('all course libraries import correctly')"
```

If that prints the message, you are ready. If it raises `ModuleNotFoundError`, the
environment is not activated, or the install did not finish — reactivate and
re-run step 4.

## 6. Start Jupyter

```bash
jupyter lab
```

Your browser opens at `http://localhost:8888`. Create a notebook and run:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(2026)
x = rng.normal(0, 1, size=10_000)
print(f"mean = {x.mean():.3f}, sd = {x.std(ddof=1):.3f}")

plt.hist(x, bins=40, edgecolor="white")
plt.title("10,000 draws from a standard normal")
plt.show()
```

You should see a histogram centred near 0 with a spread near 1. That is the
distribution this course spends Module 11 on.

## 7. Get the course data

Datasets live in `docs/data/` in the repository and are also linked from each
module. Read them with a relative path from a notebook placed in the same folder,
or use an absolute path you control:

```python
import pandas as pd
df = pd.read_csv("docs/data/penguins.csv")
df.head()
```

Every dataset page states its source, licence and shape. Synthetic datasets are
labelled as synthetic.

## Optional: PyMC for Bayesian statistics

Module 27 offers two paths: a closed-form/`scipy` path that needs nothing extra,
and a PyMC path for full posterior sampling. PyMC is optional:

```bash
pip install pymc arviz
```

If that fails on your machine, you can complete the module — and the whole course
— without it.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `python: command not found` | PATH not set (Windows) | Reinstall and tick "Add to PATH", or use `py -3.12` |
| `ModuleNotFoundError` | Environment not activated | Activate `.venv`; check the prompt shows `(.venv)` |
| `pip` installs but imports fail | Installed into a different Python | `python -m pip install ...`, not bare `pip` |
| A wheel fails to build | Interpreter too new | Use 3.12 or 3.13 |
| Jupyter opens the wrong kernel | Kernel not registered | `python -m ipykernel install --user --name psds --display-name "PSDS"` |
| Plots do not render | Missing inline backend | Add `%matplotlib inline` (JupyterLab usually needs nothing) |
| Very slow installs | No binary wheels for your platform | Try `uv`, or update `pip` first |

## What you do not need

- No paid software, no licence keys, no accounts.
- No GPU.
- No cloud notebook service. Everything runs on your own computer, offline once
  installed.
- No specific editor: JupyterLab, VS Code with the Jupyter extension, or any editor
  that runs Python will do.

## Next

Read [how to study](how-to-study.md), then open [Part I](part-1-foundations/index.md).
