# 03 — Repository Structure

The layout below is the target for the completed course. It is designed around one
hard rule from the brief: **student learning material and technical maintenance
material must never mix.** Everything under `docs/` is published; everything
outside it is instructor infrastructure.

---

## 1. Target tree

```
Probability-and-Statistics/
│
├── README.md                        # Student-facing course homepage (published front door)
├── LICENSE                          # Content licence (CC BY-NC-SA 4.0)
├── LICENSE-CODE                     # Code licence (MIT)
├── CITATION.cff                     # Machine-readable citation for the course
├── CONTRIBUTING.md                  # Errata and contribution policy (technical)
├── .gitignore
│
├── mkdocs.yml                       # Site configuration (Phase 1)
├── requirements-docs.txt            # Documentation build environment (Phase 1)
├── requirements-course.txt          # Student/notebook environment (Phase 1)
│
├── planning/                        # INSTRUCTOR ONLY — never published
│   ├── README.md
│   ├── 01-repository-audit.md
│   ├── 02-curriculum.md
│   ├── 03-repository-structure.md
│   ├── 04-module-learning-objectives.md
│   ├── 05-tools-and-libraries.md
│   ├── 06-website-architecture.md
│   ├── 07-design-specification.md
│   ├── 08-implementation-roadmap.md
│   ├── 09-risks-and-quality.md
│   └── deployment-notes.md          # Pages/CI runbook — added in Phase 9 only
│
├── docs/                            # PUBLISHED STUDENT SITE (MkDocs docs_dir)
│   │
│   ├── index.md                     # Course homepage (hero, path, module cards)
│   ├── syllabus.md                  # Full syllabus: outcomes, schedule, assessment
│   ├── how-to-study.md              # The seven-step self-study protocol
│   ├── setup.md                     # Student environment setup (Python, Jupyter, data)
│   ├── faq.md
│   ├── roadmap.md                   # What is published, what is coming
│   │
│   ├── part-1-foundations/
│   │   ├── index.md                 # Part overview: why this part, what it unlocks
│   │   ├── 01-mathematical-foundations.md
│   │   ├── 02-data-and-statistical-thinking.md
│   │   ├── 03-descriptive-statistics.md
│   │   └── 04-data-visualization.md
│   ├── part-2-probability/
│   │   ├── index.md
│   │   ├── 05-counting-and-combinatorics.md
│   │   ├── 06-axioms-of-probability.md
│   │   ├── 07-conditional-probability.md
│   │   └── 08-bayes-theorem.md
│   ├── part-3-random-variables/
│   │   ├── index.md
│   │   ├── 09-random-variables.md
│   │   ├── 10-discrete-distributions.md
│   │   ├── 11-continuous-distributions.md
│   │   ├── 12-joint-distributions.md
│   │   ├── 13-expectation-and-moments.md
│   │   └── 14-variance-and-covariance.md
│   ├── part-4-sampling/
│   │   ├── index.md
│   │   ├── 15-sampling-distributions.md
│   │   ├── 16-law-of-large-numbers.md
│   │   └── 17-central-limit-theorem.md
│   ├── part-5-inference/
│   │   ├── index.md
│   │   ├── 18-point-estimation.md
│   │   ├── 19-confidence-intervals.md
│   │   └── 20-hypothesis-testing.md
│   ├── part-6-modelling/
│   │   ├── index.md
│   │   ├── 21-correlation-and-association.md
│   │   ├── 22-simple-linear-regression.md
│   │   └── 23-multiple-linear-regression.md
│   ├── part-7-comparative/
│   │   ├── index.md
│   │   ├── 24-anova.md
│   │   ├── 25-chi-square-tests.md
│   │   └── 26-nonparametric-statistics.md
│   ├── part-8-modern/
│   │   ├── index.md
│   │   ├── 27-bayesian-statistics.md
│   │   ├── 28-monte-carlo.md
│   │   ├── 29-statistics-in-practice.md
│   │   └── 30-capstone.md
│   │
│   ├── practice/                    # Runnable notebooks, one per two modules
│   │   ├── index.md
│   │   ├── notebooks/
│   │   │   ├── m03_descriptive_statistics.ipynb
│   │   │   ├── m04_visualization.ipynb
│   │   │   ├── m05_counting_simulation.ipynb
│   │   │   ├── ...
│   │   │   └── m28_monte_carlo.ipynb
│   │   └── src/                     # Importable helpers used by notebooks
│   │       ├── __init__.py
│   │       ├── plotting.py
│   │       └── simkit.py            # simulate_mean, bootstrap_ci, permutation_test
│   │
│   ├── data/                        # Curated, small, openly licensed datasets
│   │   ├── index.md                 # Provenance, licence and shape of every file
│   │   ├── students.csv
│   │   ├── penguins.csv
│   │   ├── ames_subset.csv
│   │   ├── births.csv
│   │   └── ...
│   │
│   ├── projects/
│   │   ├── index.md
│   │   ├── project-1-describing-data.md
│   │   ├── project-2-probability-by-simulation.md
│   │   ├── project-3-inference-study.md
│   │   └── project-rubric.md
│   │
│   ├── assessments/
│   │   ├── index.md
│   │   ├── quizzes/                 # One quiz page per module (answers in <details>)
│   │   ├── exercise-sets/           # Consolidated sets per part
│   │   └── solutions/               # Full worked solutions
│   │
│   ├── reference/
│   │   ├── formula-sheet.md         # Appendix B
│   │   ├── statistical-tables.md    # Appendix A
│   │   ├── python-cookbook.md       # Appendix D
│   │   ├── notation.md              # One canonical symbol table
│   │   └── glossary.md              # Appendix C, 300+ terms
│   │
│   ├── about/
│   │   ├── instructor.md
│   │   ├── licence.md
│   │   └── acknowledgements.md
│   │
│   └── assets/
│       ├── images/
│       │   ├── modules/             # Figures, named by module
│       │   ├── diagrams/            # Mermaid-adjacent static diagrams
│       │   └── brand/               # Logo, favicon, social card source
│       ├── stylesheets/
│       │   └── extra.css            # All visual customisation lives here
│       └── javascripts/
│           ├── mathjax.js           # MathJax 3 configuration
│           └── progress.js          # Local progress tracker (localStorage)
│
├── tools/                           # INSTRUCTOR ONLY — quality and build scripts
│   ├── check_links.py
│   ├── check_math.py                # Unbalanced $ / \( \) detection
│   ├── execute_notebooks.py         # Deterministic notebook execution
│   ├── check_assets.py              # Missing figures, oversized files
│   └── new_module.py                # Scaffold a module from the standard template
│
└── .github/
    └── workflows/                   # Deferred to Phase 9 — see 06 and 08
```

## 2. Why the top level looks like this

| Path | Published? | Reason |
|---|---|---|
| `docs/` | Yes | `docs_dir` for MkDocs; every file here is student-facing |
| `planning/` | **No** | Curriculum design, audit, risks, deployment runbook. Lives outside `docs/` so the site cannot accidentally publish it |
| `tools/` | **No** | Automation for the instructor; students never need it |
| `.github/` | **No** | CI configuration |
| `README.md` | GitHub only | The repository front page. MkDocs uses `docs/index.md` as the site home, so this file is not duplicated into the site |

The README/site-home split is deliberate: the README is what a student sees
arriving at GitHub, the site is what they study in. Both are student-facing; they
are written to different lengths and never contain maintenance instructions.

## 3. Conventions

### File and folder naming

| Rule | Example | Rationale |
|---|---|---|
| Lowercase, hyphen-separated for pages | `23-multiple-linear-regression.md` | Readable URLs, no case-sensitivity issues (`core.ignorecase=true` on this machine) |
| Module files prefixed with a two-digit number | `09-random-variables.md` | Sort order matches teaching order in every file browser |
| Notebooks prefixed `mNN_` | `m14_covariance.ipynb` | Traceable to its module |
| Figures prefixed by module | `m17-clt-n30.svg` | Prevents orphaned assets |
| No spaces anywhere in paths | — | Avoids URL encoding and shell quoting bugs |
| No symlinks, no executable bits | — | `core.symlinks=false`, `core.filemode=false` on Windows |

### Page conventions

- Every module page opens with YAML front matter: `title`, `description`,
  `module`, `part`, `level`, `hours`, `prerequisites`.
- Every module page contains the twelve standard sections, in order (see
  [07 — Design Specification](07-design-specification.md)).
- Heading depth is capped at `###`; if a section needs `####` it is a sign the
  page should be split.
- Cross-references use relative Markdown links, never absolute GitHub URLs, so
  that the site and the repository both resolve correctly.

### Notebook policy

- One notebook per two modules, plus one capstone notebook. Target: **16–18
  notebooks**.
- **Committed notebooks contain outputs.** A student must be able to read the
  notebook on GitHub or the site without running anything; outputs are part of the
  explanation, not litter.
- Every notebook begins with a *Reproducibility* block: library versions, dataset
  hash, `RANDOM_SEED`, and the exact command to rebuild it.
- Every stochastic notebook seeds `numpy.random.default_rng(SEED)` and uses the
  modern `Generator` API, never the legacy global seed. This is a correctness
  requirement: unseeded examples teach students that results are unrepeatable.
- Notebooks are executed by `tools/execute_notebooks.py` before release; the
  build fails if execution raises.
- Notebook cells are kept short (≤15 lines) and end with a *visible* result or a
  printed interpretation — code that produces no output is not a demonstration.
- No notebook exceeds 2 MB; figures are saved as compressed PNG at 150 dpi or as
  SVG for line art.

### Dataset policy

| Requirement | Standard |
|---|---|
| Size | < 1 MB per file, < 8 MB total |
| Format | CSV (UTF-8, header row) unless a parquet is genuinely needed |
| Licence | Open, and recorded in `docs/data/index.md` with source URL and licence name |
| Provenance | Exact source, retrieval date, and any transformation applied |
| Cleaning | Not pre-cleaned beyond what a student should see; messiness is pedagogically useful and must be documented |
| Privacy | No personal or identifiable data, ever — including "anonymised" data that can be re-identified |
| Synthetic data | Generated reproducibly by a script in `tools/`, never hand-edited |

Candidate sources: UCI Machine Learning Repository, Palmer Penguins, Ames
Housing, Gapminder, `statsmodels`/`seaborn` built-in datasets, OpenML. Each is
checked for licence before inclusion.

### Asset and size budget

| Constraint | Budget |
|---|---|
| Repository size (excluding `.git`) | < 60 MB |
| Any single file | < 2 MB |
| Site build output | < 40 MB |
| Images per module | ≤ 8, each < 250 KB |
| External fonts/scripts | Only via the theme or a documented CDN; no trackers |

## 4. Publication boundary

Three mechanical guarantees keep planning material off the site:

1. `docs_dir: docs` — MkDocs cannot read outside its `docs_dir`.
2. `planning/`, `tools/` and `.github/` are outside `docs/`, so they are
   structurally unreachable rather than merely "not in the nav".
3. `mkdocs.yml` uses an explicit `nav:` (see 06), so no page appears in
   navigation by accident.

A file placed in `docs/` **is published**, whether or not it is in the nav. This
is the single rule content authors must remember.
