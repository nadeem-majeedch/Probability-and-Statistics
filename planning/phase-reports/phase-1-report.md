# Phase 1 Report — Site skeleton, design system and lab platform

**Date:** 13 November 2026
**Scope:** phases 1 of [08 — Implementation Roadmap](../08-implementation-roadmap.md), executed
against the binding rules in [10 — Interactive and Simulation Spec](../10-interactive-simulation-spec.md).
**Committed by:** the instructor. This phase performed **no** git write operation.

---

## 1. What was delivered

### Site and configuration

| File | Purpose |
|---|---|
| `mkdocs.yml` | Material configuration: nav, palettes, search, minify, maths, Mermaid, script load order |
| `requirements-docs.txt` | Documentation environment (MkDocs 1.6.1, Material 9.8.1, pymdown-extensions 11.0.2) |
| `requirements-course.txt` | Student environment, Python 3.12/3.13 pinned, PyMC optional |
| `LICENSE`, `LICENSE-CODE` | CC BY-NC-SA 4.0 for content, MIT for code |
| `CITATION.cff` | Machine-readable citation (CFF 1.2.0) |

### Student-facing pages (14 Markdown pages)

| Page | Notes |
|---|---|
| `docs/index.md` | Full homepage: hero, stat strip, three entry paths, eight part cards, teaching approach |
| `docs/syllabus.md` | Outcomes, two-semester and one-semester schedules, assessment, reading, policies |
| `docs/how-to-study.md` | Seven-step protocol, weekly rhythm, stuck-ladder, "what finished means" |
| `docs/setup.md` | Python 3.12 install, venv, verification, troubleshooting |
| `docs/roadmap.md` | Honest inventory of what exists and what is planned |
| `docs/faq.md` | 17 questions, including why the CLT is taught empirically first |
| `docs/part-1…8/index.md` | Eight part overviews with module tables, outcomes, simulation lists, misconceptions |
| `docs/reference/notation.md` | Canonical notation: 4 distinctions, 6 symbol tables, reading rules |
| `docs/about/instructor.md`, `docs/about/licence.md` | Instructor, licence, citation, disclosed third-party requests |

### Interactive lab platform

| File | Purpose |
|---|---|
| `docs/assets/javascripts/viz.js` | ~200-line SVG helper: scales, histogram, normal density, axes, marks |
| `docs/assets/javascripts/labs.js` | Lab runtime: widget registry, accessible controls, readouts, hints, reset |
| `docs/assets/javascripts/progress.js` | Private progress tracking in `localStorage` (activates with Module 01) |
| `docs/assets/javascripts/mathjax.js` | MathJax config + notation macros + re-typeset on instant navigation |
| `docs/assets/stylesheets/extra.css` | Design system: palette, typography, cards, labs, progress, print, reduced motion |
| `docs/labs/clt.md` | **Lab L-04** — Central Limit Theorem, with mathematics and "Try this" tasks |
| `docs/labs/confidence-intervals.md` | **Lab L-05** — CI coverage, with worked comparison table |
| `docs/labs/index.md` | Lab catalogue, usage protocol, design guarantees, 11 planned labs |
| `tools/make_lab_fallbacks.py` | Generates the two static no-JS/print fallback figures |
| `docs/assets/images/labs/*.svg` | Generated fallbacks (8.1 KB, 9.3 KB) |

### Tooling

| File | Purpose |
|---|---|
| `tools/new_module.py` | Scaffolds the 12-section module template; refuses to overwrite |
| `tools/check_math.py` | Unbalanced `\( \)` / `\[ \]`, stray `$` maths, unclosed environments |
| `tools/check_assets.py` | Broken asset references (two resolution rules), per-file and total size budgets |
| `.gitignore` | Python, notebook checkpoints, `site/`, `.venv-docs/`, secrets, OS files |

**Not created, deliberately:** no module pages, no notebooks, no datasets, no
deployment workflow, no `site/` commit. Phase 1 is foundation only.

---

## 2. Gate evidence (G-1 … G-9)

| Gate | Result | Evidence |
|---|---|---|
| **G-1** Mathematical correctness | **PASS for delivered content** | Lab statistics validated against theory by direct computation in the running page: at *n* = 100, SD of means 0.098 vs σ/√n = 0.100; skewness 0.24 vs theoretical 0.20; CI mean width 10.74 vs 2×1.96×2.739 = 10.74; 99% width 7.73 vs 2×2.5758×1.5 = 7.73. Cauchy sampler quantiles: q75 1.003 (theory 1.0), q90 3.069 (3.078), q97.5 12.653 (12.706). |
| **G-2** Educational completeness | **N/A this phase; PASS for the page types delivered** | Orientation pages follow their own specification (no module checklist applies until Module 01). Lab pages carry: instructions, mathematics, symbol definitions, parameter-effect table, worked comparison, "Try this", and next steps. |
| **G-3** Python execution | **N/A** | No notebooks exist yet. `tools/make_lab_fallbacks.py` runs clean on the system interpreter; `requirements-course.txt` is written but not installed (no course code to run). |
| **G-4** Visualisation validation | **PASS** | Both labs driven in a real browser: default render (45 bars + curve + readout), control change → "settings changed" hint, Run → updated statistics, Reset → defaults restored exactly (n = 5, exponential; 95%, n = 30). 100 intervals drawn with 4–5 misses. Keyboard: all 5 controls focusable and named. 380 px viewport: single-column stack, no horizontal overflow (scrollWidth 363 ≤ 380). Console and network clean; all local assets HTTP 200. |
| **G-5** Internal links | **PASS** | `mkdocs build --strict` exit 0 (strict turns a single broken internal link into failure) + `tools/check_assets.py` exit 0. |
| **G-6** Markdown and maths rendering | **PASS** | Notation page: 234 rendered `mjx-container` nodes, 5 tables. Equations still render after client-side navigation (57 nodes on the CLT page reached via instant nav). No literal `\(`/`\[` left in page text. |
| **G-7** Site build | **PASS** | `mkdocs build --strict` exit 0, 21 HTML pages, 3.5 MB output. |
| **G-8** No regression | **PASS** | `git log` still empty (zero commits); `git remote -v` unchanged; all phase-0 files intact and only edited where this phase intended (part-page links, licence disclosure). |
| **G-9** Honest reporting | **PASS** | §4 and §5 below. |

---

## 3. Defects found by the quality gates, and fixed

Recording these because they are the point of the gates: none was visible from a
successful build.

| # | Defect | How it was caught | Fix |
|---|---|---|---|
| D1 | `viz.js` was never added to `extra_javascript`, so `labs.js` returned at its guard clause and **both labs silently did nothing** | G-4 browser probe: `PSDSViz` undefined, `data-psds-ready` null | Added `viz.js` to `extra_javascript` **before** `labs.js` |
| D2 | Raw HTML `<img src="../assets/…">` resolved against the page URL (`/labs/clt/`) → **404 for the no-JS fallback figure** | Server log during live reload | Paths corrected to `../../assets/…`; `check_assets.py` taught the two resolution rules so it cannot recur |
| D3 | Lab readout labelled the standard deviation of the **standardised** values (≈1.0) as "SD of means" (true value σ/√n) | G-1 cross-check against theory | Statistic changed to the SD of the raw means; now reads 0.454 vs σ/√n = 0.447 |

**One false alarm, recorded for honesty.** I initially judged the Cauchy lab wrong
because only 70% of standardised means fell within ±1.96, expecting 85.6%. The
expectation was mine, not the code's: for a standard Cauchy, P(|X| ≤ 1.96) = 70%,
because 85.6% is the *normal* figure. Empirical quantiles confirmed the sampler is
correct, so the lab was left alone. Checking a claim against theory before
"fixing" working code is the behaviour this file is meant to enforce.

---

## 4. Deferred, with destination phase

| Item | Why deferred | Phase |
|---|---|---|
| `git-revision-date-localized` plugin | requires commit history; the repository has zero commits until the instructor's first commit | 2 (after first commit) |
| Module pages 01–30 | phase scope | 2–6 |
| Notebooks, datasets, projects | phase scope | 2–7 |
| `mkdocs-jupyter`, `mkdocs-glightbox` | nothing to render yet | 2 |
| Labs L-01, L-02, L-03, L-06–L-13 | specified in 10 §4 | 3–6 |
| Simulation catalogue (14 experiments) | specified in 10 §3.1 | 2–6 |
| Glossary, formula sheet, statistical tables | phase scope | 7 |
| Deployment workflow and Pages enablement | explicitly not authorised | 9, on request |
| Cross-browser testing (Firefox/Safari), full axe audit, Lighthouse scoring | single Chromium available locally | 8 |
| Print stylesheet visual verification | no printer/PDF pipeline exercised yet | 8 |
| Contrast measurement per palette | AA targeted by design; not measured with a tool yet | 8 |

---

## 5. Known limitations of this phase

1. **The site has never been published**, so the Pages URL in `site_url` is a
   prediction. Everything was verified on a local server.
2. **Local preview URL includes the base path.** Because `site_url` carries the
   project subpath, `mkdocs serve` mounts at
   `http://127.0.0.1:8123/Probability-and-Statistics/`. Requests to `/` 404 — this
   is correct behaviour, not a fault, and it is documented in the runbook.
3. **Two CDNs remain** (MathJax, Mermaid) plus one GitHub API call for the release
   badge. The labs themselves are entirely local. Vendoring MathJax/Mermaid for
   offline study is an option, not adopted.
4. **Progress tracking is installed but dormant**: no page carries
   `data-psds-module` until Module 01 exists.
5. **Fonts are fetched at build time** by Material; a build machine without network
   access will fail or fall back. Not exercised.
6. **`api.github.com/.../releases/latest` returns 404** until the repository has a
   release. Cosmetic, and disclosed in `about/licence.md`.

---

## 6. Instructor actions before Phase 2

1. Review the rendered site locally:
   `pip install -r requirements-docs.txt` then `mkdocs serve`.
2. Commit Phase 0 + Phase 1 (`docs: add architecture, curriculum and site skeleton`
   / `feat(site): scaffold MkDocs Material site with interactive lab platform`).
3. Decide the two open design questions: body font (Inter vs a serif variant), and
   whether the dark palette's indigo (#8FA8FF) is the intended accent for headings.
4. Confirm the licence choice so dataset acquisition can begin in Phase 2.
