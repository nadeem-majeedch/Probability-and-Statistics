# Phase 6 report — Python practical environment

**Scope.** Build a runnable practical environment for the eighteen-module course: a
Python foundation page, one Jupyter notebook per module, a notebook index with download
links, links from the chapters, and programmatic validation.

**Status.** Complete. Nothing was committed, pushed or deployed.

## 1. What was delivered

| Component | Location |
|---|---|
| Python foundation page | `docs/practicals/python-foundation.md` |
| Practical 00 (foundation notebook) | `docs/practicals/notebooks/00-python-foundation.ipynb` |
| Modules 01–18 notebooks | `docs/practicals/notebooks/NN-*.ipynb` |
| Notebook index (download links, chapter links, experiment map) | `docs/practicals/index.md` |
| Notebook sources (Markdown + fenced Python) | `tools/notebook_sources/*.md` |
| Builder | `tools/build_notebooks.py` |
| Validator | `tools/check_notebooks.py` |
| Chapter links | `**Run it.**` block added to all 18 chapters |
| Navigation | "Python practicals" section in `mkdocs.yml` |

Nineteen notebooks, 26–31 cells each, 14–18 code cells each, every one with the twelve
required sections: introduction, objectives, required libraries, concepts, formulas,
implementation, output and interpretation, visualisation, practical scenario, exercises,
solutions, summary.

## 2. Required experiments and where they live

| Experiment | Notebook |
|---|---|
| Descriptive statistics from examination data | 01, 03 |
| Mean, median, mode and quantiles | 01 |
| Variance and standard deviation | 01, 08 |
| Histograms and box plots | 01, 04 |
| Random experiments, coin tossing | 06 |
| Dice simulations | 06 |
| Conditional probability | 07 |
| Bayes' theorem | 07 |
| Discrete distribution simulations | 09 |
| Normal distribution, density and CDF | 10 |
| Monte Carlo estimation | 13, 18 |
| Law of Large Numbers | 13 |
| Central Limit Theorem | 13 |
| Sampling distribution simulations | 12 |
| Confidence intervals | 14 |
| Hypothesis testing | 15 |
| Correlation analysis | 16 |
| Linear regression | 16 |
| ANOVA | 17 |
| Chi-square tests | 17 |
| Bootstrap estimation | 18 |
| Bayesian updating | 07, 18 |

## 3. Engineering decisions

- **Sources are Markdown, not `.ipynb` JSON.** Each notebook is authored as Markdown with
  fenced `python` blocks in `tools/notebook_sources/`, then converted by
  `tools/build_notebooks.py`. This keeps the sources readable and reviewable, and makes
  regenerating all nineteen notebooks deterministic.
- **Shipped notebooks carry no stored outputs.** The site never embeds large cell output,
  the files stay small (31 KB in total for the repository copy is not the goal; the
  absence of megabytes of base64 images is), and the validator proves the notebooks run.
- **Data are generated, not downloaded.** There is no `docs/data/` directory in the
  repository, so every notebook creates its own data with a fixed seed. That makes the
  notebooks self-contained, offline, and reproducible, at the cost of not using a "real"
  dataset — stated explicitly in each notebook that simulates.
- **Seeds use `np.random.default_rng(...)`**, never the legacy global `np.random`, so two
  notebooks cannot interfere and the seed is local to the notebook.
- **No heavy dependencies**: NumPy, pandas, SciPy, Matplotlib, Seaborn, statsmodels and
  scikit-learn only — all already listed in `requirements-course.txt`.

## 4. Validation

`tools/check_notebooks.py` performs five classes of check:

1. every source has an up-to-date `.ipynb` (byte comparison against a fresh build);
2. the twelve required sections are present and in order;
3. at least eight code cells, no empty code cells, and a seeded generator wherever
   randomness is used;
4. stored outputs are empty in every code cell;
5. every notebook executes top to bottom in a fresh kernel with no error, produces at
   least one image where it calls `plt.show()`, and stays within output-size budgets
   (20,000 characters per output, 120,000 per notebook).

Results of the final run: **19/19 notebooks executed with zero errors**, all structural
checks passed. Runtime is about 90 seconds for the whole set; the heaviest notebook is
Practical 15 (power simulations), at roughly 24 seconds.

Site checks after the changes:

| Check | Result |
|---|---|
| `mkdocs build --strict` | exit 0, 0 warnings |
| `check_math.py` | 59 files, delimiters balanced |
| `check_assets.py` | 43 references resolve, docs/ total 1.2 MB (budget 40 MB; largest file well under 2 MB) |
| relative `.md` links | 0 broken |
| `check_examples.py` | unchanged, 506/506 assertions pass |

## 5. Known limitations

- The notebooks are validated by execution and structural checks, not by rendering: cell
  output was inspected in the logs for errors and sizes, but no human read every rendered
  notebook in JupyterLab.
- The environment used for validation is Python 3.14 with NumPy 2.5, pandas 3.1, SciPy
  1.18, statsmodels 0.15 and scikit-learn 1.9. The course's `requirements-course.txt`
  recommends Python 3.12/3.13 for PyMC compatibility; these notebooks do not use PyMC and
  run on 3.14, but the pinned recommendation is unchanged.
- Notebooks are not executed during the MkDocs build (deliberate: the build must not
  require the scientific stack), so a broken notebook is caught by the validator, not by
  publishing.
- Practical 18 uses scikit-learn only lightly (one classifier, cross-validation, AUC,
  calibration-free Brier score); it does not cover deep learning.

## 6. Integrity notes

- All data are synthetic and labelled as such; no real student records and no external
  datasets are used.
- Every interpretation section discusses what the numbers mean and, where relevant, what
  they do not: correlation is not causation (Practical 16), a p-value is not the
  probability that the null is true (Practical 15), and normal-model results depend on the
  normal assumption (Practical 10).
- Seeds are fixed and reported, so every printed number in the notebooks is reproducible.
