# 08 — Implementation Roadmap

Nine phases. Each has a scope, a deliverable list, and **exit criteria** that must
be demonstrably true before the next phase begins. Phases are ordered so that
nothing is written twice: the skeleton and the tooling exist before content, and
content exists before automation polishes it.

The instructor commits and pushes at the end of each phase; this plan performs no
git write operations.

**Definition of done, course-wide:** every module page passes the 18-point module
checklist in [09 — Risks and Quality](09-risks-and-quality.md), every notebook
executes from a clean environment, and `mkdocs build --strict` passes with zero
warnings.

---

## Phase 0 — Audit and architecture ✅ complete

**Scope.** Inspect the repository, design the curriculum, specify the site and the
design, plan delivery.

**Deliverables.** `planning/01`–`09`, `README.md`, `.gitignore`.

**Exit criteria.** Curriculum covers every requested topic; every module has
objectives; structure and configuration are specified to the point of being
copy-in ready; audit facts are measured, not assumed.

**Effort.** Complete.

---

## Phase 1 — Site skeleton and tooling

**Scope.** Make an empty-but-real website. No course content.

**Deliverables.**
1. `mkdocs.yml` with `nav` restricted to the eight orientation pages that exist
   in this phase (the full nav is enabled progressively, per phase, so the build
   never fails).
2. `requirements-docs.txt` (frozen) and `requirements-course.txt`.
3. `docs/index.md` — full homepage per the wireframe in 07 §4, module cards
   linking to part indexes (marked "coming soon" where empty).
4. `docs/syllabus.md`, `docs/how-to-study.md`, `docs/setup.md`, `docs/faq.md`,
   `docs/roadmap.md`.
5. Eight `docs/part-N-*/index.md` part overviews.
6. `docs/assets/stylesheets/extra.css`, `docs/assets/javascripts/mathjax.js`,
   `docs/assets/javascripts/progress.js`.
7. `LICENSE` (CC BY-NC-SA 4.0), `LICENSE-CODE` (MIT), `CITATION.cff`,
   `CONTRIBUTING.md`.
8. `tools/new_module.py` (scaffolds the 12-section template) and
   `tools/check_assets.py`.
9. Placeholder brand assets: `logo.svg`, `favicon.png`.

**Exit criteria.**
- `mkdocs build --strict` passes.
- Homepage, syllabus and one part index render correctly in light and dark modes.
- An inline equation, a display equation, a `cases` environment and a Mermaid
  diagram all render; equations still render *after* an internal navigation
  (the `document$` re-typeset test).
- A code block with a line annotation and a copy button renders.
- Python 3.12 environment installs cleanly and imports the full stack (§1 of 05).
- Site is shown to the instructor via local preview. **Not deployed.**

**Effort.** 2–3 working days.

---

## Phase 2 — Part I and Part II (Modules 01–08)

**Scope.** Foundations and probability. This phase sets the editorial standard for
everything after it, so it is deliberately slower per module than later phases.

**Deliverables.** 8 module pages; 3 notebooks (`m03`, `m04`, `m05`); 4 datasets
(`students.csv`, `penguins.csv`, `births.csv`, one messy CSV for M02);
1 quiz page per module; exercise sets for Parts I–II; solutions; Part I–II formula
sheets; glossary seeded with ~120 terms.

**Exit criteria.**
- Module 03 and Module 07 pass the full checklist, and the instructor has approved
  them as the *reference standard* (all later modules are matched against these).
- Every figure reproducible from a notebook.
- Exercises present at all three difficulty levels, with solutions.
- `mkdocs build --strict` passes; `nav` updated for 8 modules.

**Effort.** 10–14 working days.

---

## Phase 3 — Part III (Modules 09–14)

**Scope.** Random variables and distributions — the mathematical core, and the
phase with the highest risk of symbolic errors.

**Deliverables.** 6 module pages; notebooks `m09`–`m14`; 3 datasets (inter-arrival
times, lifetimes, a bivariate pair); 6 quizzes; Part III exercise set and
solutions; ~60 glossary terms; notation page finalised.

**Exit criteria.**
- Every derivation independently re-checked (see the two-pass review in 09 §4).
- PMF/PDF/CDF figures for all major families generated from one script.
- Simulations reproduce theoretical means and variances within Monte Carlo error,
  and the reported error is consistent with the replication count.
- `reference/notation.md` frozen; no module may introduce a new symbol afterwards
  without adding it there.

**Effort.** 12–16 working days.

---

## Phase 4 — Part IV and Part V (Modules 15–20)

**Scope.** Sampling distributions, limit theorems, estimation, intervals, testing.
The pedagogical pivot of the course.

**Deliverables.** 6 module pages; notebooks `m15`–`m20`; the "sampling distribution
machine" and "coverage simulation" utilities in `docs/practice/src/simkit.py`;
Project 2 brief; 6 quizzes; exercise sets; solutions.

**Exit criteria.**
- Coverage simulation shows empirical coverage within ~1% of nominal for
  n = 30 and above, and the module explains the shortfall at small n.
- CLT failure demonstration (Cauchy, and a highly skewed parent) present and
  explained.
- Test-selection decision tree (Mermaid) published and consistent with M20 §1.
- Project 2 is completable using only Modules 01–17.

**Effort.** 12–16 working days.

---

## Phase 5 — Part VI and Part VII (Modules 21–26)

**Scope.** Correlation, regression, ANOVA, chi-square, nonparametrics. The most
computationally dense part, and the one students will use most.

**Deliverables.** 6 module pages; notebooks `m21`–`m26`; datasets (Ames subset,
a clinical-style trial table, a contingency table, a paired-measures set); Project 3
brief and rubric page; 6 quizzes; exercise sets; solutions.

**Exit criteria.**
- Every `statsmodels` summary used in a module is read line by line in the prose.
- Residual diagnostics shown for a *deliberately violated* assumption in each of
  M22, M23 and M24, with the remedy applied.
- Nonparametric alternatives cross-checked against their parametric counterparts
  on the same data, with the difference discussed.
- Project 3 completable using only Modules 01–26.

**Effort.** 14–18 working days.

---

## Phase 6 — Part VIII (Modules 27–30)

**Scope.** Bayesian inference, Monte Carlo, practice, capstone.

**Deliverables.** 4 module pages; notebooks `m27`, `m28`, plus the capstone
starter; `simkit.py` completed (bootstrap, permutation, power simulation); capstone
brief and self-review template; A/B-testing case study; 4 quizzes; solutions.

**Exit criteria.**
- M27 works **both** with PyMC and with the closed-form path, verified on an
  environment without PyMC.
- MCMC diagnostics shown on a real fit (trace, R̂, ESS), including one
  deliberately bad fit that fails R̂.
- M29 leakage demonstration reproduces the inflated score, and the fix is shown.
- Capstone rubric applied to a worked exemplar supplied by the instructor.

**Effort.** 12–15 working days.

---

## Phase 7 — Practice layer, projects and reference

**Scope.** The material that makes the course a course rather than a book.

**Deliverables.** Remaining notebooks (target 16–18 total); `docs/practice/index.md`
indexed by module; `docs/data/index.md` with provenance and licences for every
file; `reference/python-cookbook.md`; `reference/statistical-tables.md`;
`reference/glossary.md` complete (300+ terms); all assessments consolidated;
solutions audited for completeness.

**Exit criteria.**
- Every module links to at least one notebook and one dataset (or explicitly
  states why none is needed — M02 and M30 are the only candidates).
- Every dataset entry carries source URL, retrieval date, licence and shape.
- Glossary covers every bolded term in every module (checked by script, see 09 §5).
- All 30 modules present in `nav`.

**Effort.** 8–10 working days.

---

## Phase 8 — Quality, accessibility and polish

**Scope.** Turn a complete draft into a releasable course. No new content.

**Deliverables.** Full QA report; fixes for every failed checklist item; link
check clean; notebook execution clean; Lighthouse and axe results recorded;
print stylesheet verified on two modules; errata page.

**Exit criteria (release gate).**
- 18/18 checklist items pass on all 30 modules.
- `mkdocs build --strict` clean; zero broken internal or external links.
- All notebooks execute end-to-end in a fresh Python 3.12 environment.
- Lighthouse: performance ≥ 90, accessibility ≥ 95 on a module page.
- axe: zero critical or serious issues.
- Dark and light modes both verified on home, a module and a notebook page.
- Site size < 40 MB; no file > 2 MB.

**Effort.** 6–8 working days.

---

## Phase 9 — Publication readiness and theme migration checkpoint

**Scope.** Everything needed to publish — **and nothing executed without explicit
authorisation**.

**Deliverables.** `planning/deployment-notes.md` runbook; the workflow file
`docs.yml` prepared but not committed until authorised; repository metadata
(description, topics); Pages enablement checklist; Zensical evaluation note.

**Exit criteria.**
- Instructor has reviewed and approved the release gate report.
- Deployment runbook tested in a dry run (`mkdocs build --strict` in a clean
  container or fresh venv).
- **Zensical/Material migration decision recorded** before 5 May 2027 (risk R03):
  stay on Material 9.8, or move to Zensical `classic` with a config diff.

**Effort.** 2–3 days, plus an ongoing annual review.

---

## Sequencing and dependencies

```
Phase 0 ──► Phase 1 ──► Phase 2 ──► Phase 3 ──► Phase 4 ──► Phase 5 ──► Phase 6
                            │            │            │            │
                            └────────────┴────────────┴────────────┴──► Phase 7
                                                                          │
                                                     Phase 8 ◄────────────┘
                                                        │
                                                     Phase 9
```

Hard dependencies worth stating:

- Phase 1 before everything: the toolchain and the standard must exist before
  content, or 30 modules get written in 30 styles.
- Phase 2 before Phase 3: Modules 03 and 07 define the editorial reference
  standard.
- Phase 7 after Phase 6: the practice index can only be assembled once all modules
  exist.
- Phase 8 after Phase 7, always. Polishing an incomplete corpus wastes the polish.
- Phase 9 last, and gated on explicit authorisation.

## Effort summary

| Phase | Effort (working days) | Cumulative |
|---|---|---|
| 0 | complete | — |
| 1 | 2–3 | 3 |
| 2 | 10–14 | 17 |
| 3 | 12–16 | 33 |
| 4 | 12–16 | 49 |
| 5 | 14–18 | 67 |
| 6 | 12–15 | 82 |
| 7 | 8–10 | 92 |
| 8 | 6–8 | 100 |
| 9 | 2–3 | 103 |

≈ 100 working days of authoring, or roughly five months at one phase per fortnight
alongside teaching. Phases 2–6 can be interleaved with a semester, since each part
is independently usable as it lands — which is why the `nav` grows phase by phase
rather than all at once.

## Commit strategy for the instructor

Not performed by this plan; recommended for consistency of history:

| Phase | Commit | Message style |
|---|---|---|
| 0 | 1 | `docs: add repository audit, curriculum and architecture plan` |
| 1 | 1–2 | `feat(site): scaffold MkDocs Material site with maths, navigation and design system` |
| 2–6 | 1 per module + 1 per part | `feat(m07): conditional probability and independence` |
| 7 | 1 per artifact type | `feat(practice): add notebooks, datasets and reference pages` |
| 8 | small, frequent | `fix(m19): correct coverage simulation seed in example 3` |
| 9 | 1 | `chore(ci): add Pages build workflow` (when authorised) |

One module per commit keeps history bisectable and makes an erratum traceable to
the exact change that introduced it.
