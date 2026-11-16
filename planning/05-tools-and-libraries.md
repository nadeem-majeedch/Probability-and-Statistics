# 05 — Required Tools and Libraries

Two environments are needed and must stay separate: one to **run the course**
(students' Python stack) and one to **build the website** (documentation stack).
Mixing them is the usual cause of a broken build.

---

## 1. Python version

| Requirement | Value |
|---|---|
| Course code and notebooks | **Python 3.12 or 3.13** |
| Documentation build | Python ≥ 3.11 (Material 9.8 requires it) |
| System interpreter on this machine | Python **3.14.10** — do **not** use it directly |

**Why not the system Python.** The scientific stack depends on compiled wheels.
Support for a newly released interpreter lags by months for `statsmodels`,
`seaborn` and especially `pymc`. Authoring 30 modules against an interpreter where
`pip install pymc` fails produces a course that cannot be reproduced. Pin 3.12 (the
most conservative choice with full wheel coverage) or 3.13.

**Phase-1 gate.** Before any content is written, run:

```bash
python -c "import numpy, scipy, pandas, matplotlib, seaborn, statsmodels, sklearn; print('ok')"
python -c "import pymc; print(pymc.__version__)"   # optional module 27
```

If either fails on the chosen interpreter, step down a minor version before
writing Module 01. Recorded as risk **R07**.

## 2. Environment management

**Recommendation: `uv`** (fast, lockfile-native, handles Python downloads).

```bash
uv venv --python 3.12
uv pip install -r requirements-course.txt
```

`pip` + `venv` remains fully supported and is documented for students whose
machines cannot install `uv`:

```bash
py -3.12 -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements-course.txt
```

Never install course packages into the global interpreter; the machine already
carries a global JupyterLab and students will confuse the two.

## 3. Course stack (`requirements-course.txt`)

Version policy: accept the current minor series with `>=`, pin the major; freeze
exact versions into `requirements-lock.txt` at each release so that a student in
2028 can still rebuild the notebooks.

| Library | Minimum | Purpose in this course |
|---|---|---|
| `numpy` | 2.0 | arrays, RNG (`Generator` API), linear algebra, simulation |
| `scipy` | 1.14 | `scipy.stats` distributions and tests, `integrate`, `optimize` |
| `pandas` | 2.2 | data handling, descriptive statistics, group operations |
| `matplotlib` | 3.9 | all figures; object-oriented API taught explicitly |
| `seaborn` | 0.13 | statistical graphics, distribution and regression plots |
| `plotly` | 5.24 | one interactive figure per relevant module (optional for students) |
| `statsmodels` | 0.14 | regression, ANOVA, diagnostics, power, contingency tables |
| `scikit-learn` | 1.5 | M29 only: cross-validation, regularisation, metrics |
| `sympy` | 1.13 | M01 and M18: symbolic differentiation, integration, likelihoods |
| `pingouin` | 0.5 | M24–M26: Welch ANOVA, Tukey, Dunn, effect sizes |
| `jupyterlab` | 4.2 | notebook authoring and student workspace |
| `ipykernel` | 6.29 | kernel registration for the project venv |
| `pymc` | 5.16 | M27 only — **optional**, listed separately, may fail to install |
| `arviz` | 0.19 | M27 posterior diagnostics (comes with PyMC) |

**Optional vs required.** Modules 01–26 and 28–30 must run without PyMC. Module
27 provides a PyMC path *and* a closed-form/`scipy` path for the same models, so a
student who cannot install PyMC still completes the module. This is also the
fallback if PyMC wheels lag the interpreter.

**Not used, deliberately.** No `R`/`rpy2` (single-language course), no
`tensorflow`/`torch` (out of scope), no plotting wrappers that hide matplotlib
(`plotnine` considered, rejected: too much syntax to teach alongside the
statistics).

## 4. Notebook and data tooling (instructor side)

| Tool | Purpose |
|---|---|
| `jupytext` | keep a `.py` percent-format twin of each notebook for clean diffs and review |
| `nbconvert` | HTML/PDF export of a module notebook for offline study |
| `nbclient` / `papermill` | deterministic execution in CI and in `tools/execute_notebooks.py` |
| `nbqa` + `ruff` | lint and format code inside notebooks |
| `nbval` or `pytest --nbval-lax` | smoke-test that committed notebooks run without error |
| `ruff` | formatting and linting of all Python and notebook code cells |
| `pre-commit` | run ruff, link check and the math check before the instructor commits |

## 5. Documentation stack (`requirements-docs.txt`)

| Package | Version | Role |
|---|---|---|
| `mkdocs` | ≥ 1.6, < 2 | static site generator |
| `mkdocs-material` | `>= 9.8, < 10` | theme; current release 9.8.1 (7 Nov 2026) |
| `pymdown-extensions` | ≥ 11 | `arithmatex`, `superfences`, `tabbed`, `details`, `highlight`, `tasklist` |
| `mkdocs-jupyter` | ≥ 0.27 | embed executed notebooks as site pages |
| `mkdocs-minify-plugin` | ≥ 0.8 | minify HTML/CSS/JS |
| `mkdocs-git-revision-date-localized-plugin` | ≥ 1.2 | "last updated" from git history |
| `mkdocs-glightbox` | ≥ 0.4 | image zoom for dense figures |
| `mkdocs-redirects` | ≥ 1.2 | preserve URLs when module slugs change |
| `mkdocs-htmlproofer` or `lychee` | current | link validation (external binary `lychee` is faster) |

**Deliberately excluded:** `mkdocs-material[imaging]` (social cards) — it needs
Cairo, which is painful on Windows and adds nothing pedagogically; the `social`
plugin; any analytics plugin. Progress tracking is a ~60-line custom script rather
than a plugin, so it cannot break the build.

**Version pinning.** `requirements-docs.txt` is a lockfile (`pip freeze`) committed
to the repository, per Material's own guidance: a theme major upgrade silently
changing the site is exactly the failure mode a course repository must avoid.

## 6. Front-end assets

| Asset | Source | Note |
|---|---|---|
| Inter (text) | Google Fonts via Material's `font` setting | downloaded at build time by Material, not at runtime by the reader |
| JetBrains Mono (code) | same | tabular figures matter for numerical tables |
| MathJax | CDN (`mathjax@3`, `tex-mml-chtml`) | pinned version string; full AMS coverage needed for `aligned`, `cases`, `\operatorname` |
| Mermaid | CDN, pinned | flow/decision diagrams only; statistics figures are matplotlib |
| Material icons | bundled with the theme | no extra dependency |

**Offline study.** Students may have intermittent connectivity. The site is static
and most pages work offline once cached, but MathJax and Mermaid come from a CDN.
If offline use becomes a requirement, vendor both into `docs/assets/vendor/`;
this is noted as an option, not adopted now (it adds ~1.5 MB to the repo).

## 7. Machine requirements

| Item | Minimum | Comfortable |
|---|---|---|
| OS | Windows 10, macOS 12, Ubuntu 20.04 | current release |
| RAM | 4 GB | 8 GB (PyMC sampling benefits from more) |
| Disk | 1.5 GB for the environment | 3 GB |
| Browser | any current evergreen browser | Chrome/Edge/Firefox for the site |
| Editor | VS Code with Jupyter, or JupyterLab | either; both documented |

No GPU is required anywhere in the course.

## 8. Install sequence (Phase 1)

```bash
# 1. clone (instructor or student)
git clone https://github.com/nadeem-majeedch/Probability-and-Statistics.git
cd Probability-and-Statistics

# 2. course environment
uv venv --python 3.12
uv pip install -r requirements-course.txt
uv run python -m ipykernel install --user --name psds --display-name "PSDS (3.12)"

# 3. documentation environment (separate)
uv venv .venv-docs --python 3.12
uv pip install -r requirements-docs.txt

# 4. verify
uv run python -c "import numpy, scipy, pandas, statsmodels; print('course ok')"
.venv-docs/Scripts/python -m mkdocs --version
```

The documentation environment is intentionally separate: a site build must never
fail because a notebook dependency changed, and vice versa.
