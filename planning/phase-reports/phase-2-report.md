# Phase 2 report — Educational framework for 18 modules

**Scope:** Tasks 1–5 of the approved module-framework brief. Framework only: no
chapter prose, no exercise sets, no notebooks.
**Date:** 14 November 2026
**Status:** Delivered and verified. No commits, pushes or deployment performed.

---

## 1. What was delivered

### TASK 1 — Directory and navigation structure

- `docs/modules/` created with 19 files: `index.md` plus one page per module
  (`NN-slug.md`, 01–18).
- `mkdocs.yml` gained a `Course map` entry (`modules/index.md`) and every part
  section now lists its modules beneath the part overview:

  | Nav section | Part | Modules |
  |---|---|---|
  | Part I — Foundations | I | M01–M04 |
  | Part II — Probability | II | M05–M07 |
  | Part III — Random variables | III | M08–M11 |
  | Part IV — Sampling and limit theorems | IV | M12–M13 |
  | Part V — Inference | V | M14–M15 |
  | Part VI — Relationships and modelling | VI | M16 |
  | Part VII — Comparative inference | VII | M17 |
  | Part VIII — Modern statistics | VIII | M18 |

- Eight part overview pages rewritten to the 18-module numbering (module tables with
  links, hours, misconception tables, "start here" pointers).
- No directories were moved or deleted; no content was removed.

### TASK 2 — Student-facing module overviews

Each of the 18 pages carries the same structure:

1. front matter (`module`, `part`, `level`, `hours`, `prerequisites`)
2. a chip row (level, part, hours, "module *n* of 18"), newly styled as `.psds-meta`
3. Introduction
4. Why this matters
5. Learning objectives (numbered, observational "you can…")
6. Prerequisites table with *what to revise and where*
7. Topic breakdown (units with hour allocations)
8. Important mathematical concepts (display maths + a plain-language gloss)
9. Expected knowledge after completion
10. Connections to Data Science
11. Practical applications (table)
12. Exercises and assessment plan (★/★★/★★★ counts, quiz, practical, lab)
13. Recommended study sequence (session table)
14. "Before this module / After" footer

Content is specific to each module: e.g. M12's introduction is built on "a statistic
is itself a random variable", M17's on the three chi-square designs, M18's on which
question a paradigm answers. No module page contains placeholder text.

### TASK 3 — Subtopic breakdown

Every module has 5–7 units with hour budgets, totalling the module's declared hours.
Each unit is a teachable chunk (e.g. "Unit 3 — Degrees of freedom and the chi-square
distribution", 3 h), not a heading. Hours per module:

| Part | Modules | Hours |
|---|---|---|
| I | M01 6, M02 12, M03 14, M04 12 | 44 |
| II | M05 10, M06 14, M07 14 | 38 |
| III | M08 16, M09 14, M10 14, M11 14 | 58 |
| IV | M12 14, M13 12 | 26 |
| V | M14 16, M15 18 | 34 |
| VI | M16 18 | 18 |
| VII | M17 16 | 16 |
| VIII | M18 18 | 18 |
| **Total** | **18 modules** | **252** |

### TASK 4 — Cross-module dependencies

- `docs/modules/index.md` holds: the module map, a Mermaid dependency graph, a
  prerequisite table, three study sequences (linear, inference-focused, modelling-
  focused), and an "if you are stuck here, revise this" table.
- Those sequences are also published as precomputed paths in three columns so they
  render without JavaScript.
- Every module page states its prerequisites with the specific units to revisit, and
  links forward to the next module.
- Dependencies are honest where the curriculum is not strictly linear: M16 needs
  M11/M14/M15; M17 needs M12 (F and chi-square); M18 needs M07 (Bayes) as well as
  M15 and M17 — the M18 prerequisite list names all four.

### TASK 5 — Navigation and roadmap

- `docs/roadmap.md` rewritten: available-today inventory (18 module frameworks, 2
  live labs), per-part release table, the twelve-section definition of "complete",
  and a 12-lab catalogue with correct module numbers.
- `docs/index.md`, `docs/syllabus.md`, `docs/how-to-study.md`, `README.md` and the
  part pages reconciled from 30 modules / 254 hours to **18 modules / 252 hours**.
- Syllabus schedules rebuilt: Semester 1 = M01–M12 (154 h), Semester 2 = M13–M18
  (98 h) plus the capstone; core track = M01–M08, M12, M14–M15 (≈146 h).
- `planning/11-module-framework.md` added as the authoritative record, including the
  full 30 → 18 mapping. `planning/02` and `planning/04` carry supersession banners
  and are retained (no deletions).

## 2. Verification

| Check | Command | Result |
|---|---|---|
| Strict site build | `.venv-docs/Scripts/python.exe -m mkdocs build --strict` | **exit 0** |
| Maths delimiters / stray `$` | `python tools/check_math.py` | **exit 0** — 39 files, balanced |
| Asset references | `python tools/check_assets.py` | **exit 0** — 2 references resolve |
| Internal `.md` links | script: every relative link resolved from its source directory | **0 broken** |
| Module pages present | glob `docs/modules/NN-*.md` | **18** |
| Hours reconcile | sum of `hours:` front matter | **252** |
| Nav entries | count of `modules/NN-` in `mkdocs.yml` | **18** |
| Stale counts | grep `thirty modules|30 modules|254` across `docs/`, `README.md`, `mkdocs.yml` | only SVG coordinates |

`--strict` treats a missing nav target as an error, so all 18 nav links resolve.

## 3. Gates (from `planning/10`)

| Gate | Status | Note |
|---|---|---|
| G-1 Content accuracy | Pass (framework level) | Every claim is a standard textbook result; no invented statistics, datasets or references. Chapter-level verification is a Phase 3 task. |
| G-2 Notation consistency | Pass | Only the macros declared in `mathjax.js` (`\E \Var \Cov \sd \se \iid \indep \R \P`) plus standard LaTeX are used. |
| G-3 Prose quality | Pass | Chapter-level, student-facing; no lecture-delivery material. |
| G-4 Interactive integrity | N/A this phase | No new widgets; the two existing labs were not modified. |
| G-5 Simulation protocol | N/A this phase | Frameworks name the experiments; protocols are written with the chapters. |
| G-6 Links and assets | Pass | 0 broken internal links; asset check exit 0. |
| G-7 Accessibility | Pass (structure) | Heading hierarchy H1→H2→H3 without skips; tables have header rows; no colour-only encoding; chips carry text. |
| G-8 Build | Pass | `--strict`, exit 0. |
| G-9 Honesty | Pass | Every page states that module pages are frameworks, not chapters; roadmap and README say the same. |

## 4. Defects found and fixed in this phase

| # | Defect | Fix |
|---|---|---|
| D4 | `.psds-meta` chip row had no CSS rule, so the four chips stacked with no separation | Added a flex-wrap rule with a bottom border in `extra.css` |
| D5 | M12 assessment table header read "Force" instead of "Focus" | Corrected |
| D6 | Homepage entry buttons and "Open Module 01" links pointed at part overviews rather than the module itself | Repointed to `modules/01-…`; added a course-map button |
| D7 | Part VIII card was labelled "Core" while M18 is Advanced | Corrected |

## 5. What is deliberately not done

- **No chapter prose.** The twelve-section chapter anatomy is defined and scoped, not
  written. Nothing is labelled "complete".
- **No exercise sets, quizzes, notebooks or projects.** Counts are specified per
  module so authors write to a fixed target.
- **Ten of the twelve planned labs are unimplemented**; the roadmap lists them as
  planned, and only the CLT and coverage labs are live.
- **No deployment, no commits, no pushes.** Working tree only; branch `main` still has
  zero commits, remote unchanged.
- **`docs/modules/index.md` study-sequence columns** are static text rather than a
  generated table; if the dependency graph changes, they must be updated by hand.

## 6. Next phase (proposed)

1. Write M01–M04 chapters to the twelve-section anatomy; verify each numerically.
2. Build the three planned Part I labs (mean/median/SD explorer, distribution
   explorer, plotting exercise).
3. Only then proceed part by part, keeping the roadmap honest at each release.
