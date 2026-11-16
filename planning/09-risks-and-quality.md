# 09 — Risks and Quality Requirements

---

## 1. Risk register

Likelihood and impact are assessed for the *build* (authoring to release), not for
the repository's existence. Each risk has a named mitigation that is already
reflected in the plan, not an intention to "be careful".

| ID | Risk | Likelihood | Impact | Mitigation | Trigger to act |
|---|---|---|---|---|---|
| **R01** | **Scope creep**: modules grow beyond 12 sections and 8,000 words, and the course never finishes | High | High | Hard caps per module (12 sections, ≤ 8k words, ≤ 8 figures, 1 notebook); anything extra goes to an appendix or a follow-on list; `tools/new_module.py` scaffolds the cap | A module exceeds 10k words |
| **R02** | **Mathematical error** in a derivation, formula or worked example | Medium | Critical | Two-pass review (§4); numerical verification of every closed-form result by simulation or `sympy`; formula sheet re-derived independently | Any disagreement between a derivation and its simulation |
| **R03** | **Material for MkDocs reaches EOL 5 May 2027**; the site becomes unmaintained | Certain | Medium | Standard `mkdocs.yml` only; no Insiders features; all customisation in `extra.css`/two JS files; migration checkpoint at Phase 9; Zensical `classic` expected to be a config diff | Phase 9, or a security advisory against Material |
| **R04** | **Single-author bandwidth and bus factor**: one person writes, reviews and maintains everything | High | High | Modular structure so any part can ship independently; planning docs record every decision so work can be resumed or delegated; phase-based `nav` means a partial course is a usable course | Author unavailable for > 4 weeks |
| **R05** | **Accessibility regressions** from custom CSS and the progress script | Medium | Medium | Accessibility rules in 07 §9 are content rules; axe + Lighthouse at Phase 8; contrast verified per palette; keyboard walkthrough per phase | axe reports a serious issue |
| **R06** | **Repository bloat**: notebooks with outputs and figures push the repo past usability | Medium | Medium | Size budgets (03 §3): dataset < 1 MB, image < 250 KB, notebook < 2 MB, repo < 60 MB; `tools/check_assets.py` in the build | Repo > 40 MB |
| **R07** | **Toolchain mismatch**: system Python is 3.14, where `statsmodels`, `seaborn` or `pymc` wheels may be unavailable, producing a course that cannot be reproduced | High | High | Pin a 3.12/3.13 virtual environment; Phase-1 install gate; PyMC optional with a closed-form path for M27; frozen `requirements-lock.txt` | Any `pip install` failure in the pinned env |
| **R08** | **Notebook drift**: outputs in committed notebooks no longer match the code | Medium | High | `execute: false` in the site plugin; deterministic execution via `tools/execute_notebooks.py` before release; fixed seeds; re-execution in a fresh env at Phase 8 | A notebook fails to execute |
| **R09** | **Link rot**: external dataset URLs and references disappear | High | Low | Prefer mirrored CSVs in `docs/data/` over live URLs; record source URL *and* retrieval date; link check at every phase | Link checker failure |
| **R10** | **Dataset licensing or privacy problem** in published data | Low | Critical | Only openly licensed datasets; licence recorded per file in `docs/data/index.md`; no personal or re-identifiable data; synthetic data generated reproducibly | Any dataset without a stated licence |
| **R11** | **Windows case-insensitivity** (`core.ignorecase=true`) lets two files differ only by case, breaking the build on Linux CI | Medium | Medium | Lowercase-hyphen naming convention with no exceptions; CI runs on Ubuntu, which surfaces the error | A page works locally but 404s in CI |
| **R12** | **Solutions undermine learning**: students read answers instead of attempting problems | Medium | Medium | Exercise solutions collapsed behind `???`; "attempt first" instruction at the top of every exercise set; quiz answers one click away but the question requires work | — (design already mitigates) |
| **R13** | **First publication fails**: Pages not enabled, wrong permissions, `site_url` mismatch, broken assets under a project-site base path | Medium | Medium | Deployment runbook in 06 §9 with the three common failure modes named; `mkdocs build --strict` locally first; documentation of `permissions: pages: write, id-token: write` | First deploy attempt |
| **R14** | **Newcomer disorientation**: a 30-module course overwhelms a student who arrives mid-way | Medium | Medium | Three entry paths on the homepage; prerequisite chips on every page; "you are here" line; per-part overview pages; `roadmap.md` showing what is published | — (design already mitigates) |
| **R15** | **Numerical claim not reproducible** because a random example was unseeded | Medium | Medium | `np.random.default_rng(SEED)` mandated; seed printed in prose; no legacy global seeding anywhere | A student reports different output |

**The two risks that matter most** are R02 (a wrong derivation teaches the wrong
thing, at scale, permanently) and R07 (a course that cannot be installed is not a
course). Both have gates in Phase 1 and Phase 3 rather than hopes.

## 2. Quality requirements

Each requirement is measurable. "Looks right" is not a criterion anywhere in this
project.

### 2.1 Mathematical accuracy

| Requirement | Standard | Verified by |
|---|---|---|
| Every formula is correct, including its conditions of validity | zero known errors | independent re-derivation + numerical check |
| Notation is consistent across all 30 modules | one symbol, one meaning | `reference/notation.md` + grep audit |
| Every derivation has every step justified | no "it can be shown" without a pointer | checklist item 7 |
| Numerical examples are arithmetically correct | every intermediate value shown and checkable | recomputation in a notebook |
| Distributions are specified with support and parameters | no exceptions | template requirement |

### 2.2 Code correctness and reproducibility

| Requirement | Standard |
|---|---|
| Every code block runs | executed in the pinned environment before release |
| Every notebook executes top-to-bottom | zero errors, no manual intervention |
| Stochastic examples are seeded and the seed is visible | `default_rng(2026)`, seed stated in prose |
| Library versions are recorded | header cell in every notebook |
| Simulations agree with theory within Monte Carlo error | error quantified, not hand-waved |
| Deprecated APIs are not used | no `np.random.seed`, no `np.float`, no `df.append` |

### 2.3 Pedagogical completeness (self-study sufficiency)

The test of this course is whether a motivated student with no instructor can get
stuck *and get unstuck*.

| Requirement | Standard |
|---|---|
| Every module has all 12 sections | 12/12, no exceptions |
| Every objective is assessed | quiz or exercise item per objective |
| Every symbol is defined before use | checked in review |
| Every worked example is complete | final answer stated with units and interpretation |
| Every figure explains itself | caption states the finding |
| Exercises span three difficulty levels | ★/★★/★★★ all present |
| Solutions are complete and correct | full working, not answers only |
| "Before you start" links the exact prerequisite section | not merely the module |

### 2.4 Consistency and maintainability

| Requirement | Standard |
|---|---|
| File naming | lowercase-hyphen, numbered, no spaces |
| Front matter | all modules carry `title, description, module, part, level, hours, prerequisites` |
| Cross-links | relative, never absolute GitHub URLs |
| Admonition semantics | one purpose per type, per 07 §6 |
| Heading depth | ≤ `###` |
| Build | `mkdocs build --strict`, zero warnings |
| Planning material | never inside `docs/` |

### 2.5 Accessibility, performance and presentation

| Requirement | Standard |
|---|---|
| WCAG | 2.2 AA, axe zero critical/serious |
| Contrast | 4.5:1 body, 3:1 large |
| Keyboard | full operation, visible focus |
| Alt text | every figure, describing the finding |
| Math | plain-language restatement after each display equation |
| Lighthouse | performance ≥ 90, accessibility ≥ 95 |
| Page weight | < 1.5 MB excluding MathJax |
| Print | A4-readable, answers expanded, equations intact |
| Dark mode | every component verified in both palettes |

### 2.6 Legal and ethical

| Requirement | Standard |
|---|---|
| Content licence | CC BY-NC-SA 4.0, stated in `LICENSE`, the site footer and `about/licence.md` |
| Code licence | MIT, in `LICENSE-CODE` |
| Dataset licences | recorded per file, attributed in `docs/data/index.md` |
| Citation | `CITATION.cff` plus a "How to cite" block in the README |
| Privacy | no analytics, no trackers, no personal data; progress stored locally in the browser |
| Attribution of third-party figures | credited in the caption and in `acknowledgements.md` |

## 3. Module acceptance checklist (18 items)

A module is not complete until all 18 pass. This is the gate used at Phase 8 and
at every phase boundary for the modules that phase delivered.

1. Front matter complete; `nav` entry present.
2. All 12 sections present, in order.
3. 5–9 objectives, each measurable and each assessed.
4. "Before you start" links the specific prerequisite sections.
5. Every symbol defined before first use; notation matches `reference/notation.md`.
6. Every derivation step justified.
7. Every formula states its conditions of validity.
8. Intuition section present and genuinely different from the concept section.
9. 2–4 worked examples, each numerically complete with an interpretation sentence.
10. 2–3 specific data-science applications.
11. 2–5 figures, each reproducible, captioned with the finding, alt-texted.
12. Python demonstration runs, is seeded, and shows its output.
13. Exercises at ★, ★★ and ★★★ with marks and time estimates.
14. Solutions complete, collapsed, and correct.
15. Quiz of 8–10 items with explained answers.
16. Summary contains a formula box, common errors and "you can now…".
17. Forward and backward links present.
18. Build strict-clean; no broken links; accessibility checks pass.

## 4. Review process for mathematical content

Because R02 is the highest-impact risk, no derivation ships after a single reading.

**Pass 1 — construction.** Write the derivation with the conditions of validity
visible. Every step gets a reason.

**Pass 2 — adversarial read (≥ 24 hours later).** Re-derive each result on paper
without looking, then compare. Discrepancies are the finding; they are expected
and are how errors are caught.

**Pass 3 — numerical check.** For every closed-form result: simulate or integrate
numerically and compare. This catches sign errors, off-by-one degrees of freedom,
and factor-of-2 mistakes that reading never catches. `sympy` for symbolic cases,
`scipy.integrate.quad` or Monte Carlo for the rest.

**Pass 4 — edge cases.** Evaluate at n = 1, p = 0, p = 1, σ → 0, k = 1, and at
least one degenerate case. Every formula should behave sensibly or say why not.

A derivation failing any pass does not enter the module. This is the single most
expensive quality rule in the project and the one most worth keeping.

## 5. Automated checks

| Check | Tool | Runs |
|---|---|---|
| Build with strict links | `mkdocs build --strict` | every phase |
| External link rot | `lychee` or `mkdocs-htmlproofer` | every phase |
| Missing/oversized assets | `tools/check_assets.py` | pre-commit |
| Unbalanced math delimiters | `tools/check_math.py` | pre-commit |
| Glossary coverage of bolded terms | `tools/check_glossary.py` | Phase 7–8 |
| Notebook execution | `tools/execute_notebooks.py` (`nbclient`) | pre-release |
| Python lint/format | `ruff` via `nbqa` and `pre-commit` | pre-commit |
| Stray `$…$` math (must be `\(…\)`) | `tools/check_math.py` | pre-commit |
| Accessibility | axe DevTools + Lighthouse | Phase 8, and after any CSS change |
| Notation consistency | grep for forbidden symbols (`E(`, `V(`, `cov(`) | Phase 3 onward |

## 6. Release gate

Publishing is authorised only when **all** of the following hold:

1. 30/30 modules pass the 18-point checklist.
2. `mkdocs build --strict` is clean; external link check is clean.
3. All notebooks execute in a fresh Python 3.12 environment from the frozen
   requirements, with zero errors.
4. Lighthouse performance ≥ 90 and accessibility ≥ 95; axe shows no critical or
   serious issue.
5. Light and dark modes verified on home, a module and a notebook page, on desktop
   and at 375 px width.
6. Print view of two modules verified (equations, tables, expanded answers).
7. Licence files, dataset attributions and `CITATION.cff` present and accurate.
8. Instructor has read the QA report and signed off.

Failure of any item blocks publication. A site that is 95% correct about
statistics is a site that teaches errors.

## 7. Governance and maintenance

| Activity | Cadence | Owner |
|---|---|---|
| Errata triage (issues) | monthly during a taught semester | instructor |
| Dependency refresh (`numpy`, `scipy`, `pandas`, docs stack) | each semester start; re-run notebooks after | instructor |
| Notebook re-execution in a clean env | each release | instructor |
| Link check | each release | automated |
| Accessibility re-check | after any CSS or theme change | instructor |
| Material/Zensical migration review | before 5 May 2027 | instructor |
| Curriculum review (is Module *x* still the right content for a data-science degree?) | annually | instructor |
| Archive snapshot of a taught edition (tag) | at the end of each academic year | instructor |

**Errata policy.** Every accepted erratum produces a commit whose message names the
module and section, so a reader can see exactly what changed and why. Corrections
are never silent.

**Contribution policy.** Students and colleagues may report errors through issues;
accepted contributions are credited in `acknowledgements.md`. Substantive content
contributions require the instructor's review against the module checklist.

## 8. Traceability to the brief

| Brief requirement | Where it is satisfied |
|---|---|
| Task 1 — repository audit | [01](01-repository-audit.md): git state, remote, files, framework, workflows, licences, student content, toolchain, gap analysis |
| Task 2 — educational architecture | [02](02-curriculum.md): 30 modules, 8 parts, prerequisites, coverage matrix, schedules, assessment |
| Task 3 — student learning experience | [02](02-curriculum.md) §1, [04](04-module-learning-objectives.md), [07](07-design-specification.md) §5, `README.md` study protocol |
| Task 4 — website framework | [06](06-website-architecture.md): MkDocs Material, full config, nav, plugins, notebooks, datasets, projects, reference, maintenance separation |
| Task 5 — design specification | [07](07-design-specification.md): typography, palette, homepage, responsive, dark mode, search, sidebar, equations, code, print, accessibility |
| Task 6 — deliverable | [01](01-repository-audit.md)–[09](09-risks-and-quality.md), plus this plan's index |
| No content generated | only `README.md` (course homepage) and `planning/**` exist |
| No commit / push / publish | audit §4 records zero git write operations |
| Remote unchanged | audit §2.1 |
| Student-facing README | `README.md` contains no deployment or maintenance instructions |

## 9. Acceptance criteria for this deliverable

The architecture deliverable is accepted when the instructor confirms:

- [ ] The audit accurately describes the repository as it is.
- [ ] The 30-module curriculum is the right coverage for BS Data Science.
- [ ] The two-semester split (and the one-semester core track) fits the programme.
- [ ] The self-study contract (12 sections, 7-step protocol, self-marking) is
      sufficient without an instructor.
- [ ] MkDocs Material is the approved framework, with the EOL caveat understood.
- [ ] The design direction (palette, typography, page templates) is approved.
- [ ] The phased roadmap and its effort estimate are acceptable.
- [ ] The risk register and release gate are accepted as the working standard.
