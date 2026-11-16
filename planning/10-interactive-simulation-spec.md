# 10 — Interactive and Simulation Specification

**Status: binding.** This document converts the approved master requirements into
testable rules. It applies to every phase from Phase 1 onward, to module pages,
notebooks, labs, projects and the website. Where it conflicts with an earlier
planning document, **this document wins**.

Requirements are labelled `I-` (interactive), `S-` (simulation), `P-` (Python),
`M-` (mathematical understanding), `A-` (academic integrity), `L-` (learner
experience), `G-` (phase gates). Each is referenced by ID in phase reports, so
compliance is auditable rather than asserted.

> **Status as built (TASK 16).** The shipped collection is fourteen laboratories,
> L-01 to L-14, catalogued in `docs/labs/index.md`, whose table is authoritative for
> the code, module and notebook of each lab. The lab tables below are the original
> planning sketch: their `L-` numbers and module numbers predate the finished
> curriculum (M06–M18) and do not match the shipped order. The binding requirements
> in sections 1–3 still apply to every laboratory.

---

## 1. Technology decision

Three kinds of "interactive" are possible on GitHub Pages. Only one is safe.

| Approach | Works on static hosting | Verdict |
|---|---|---|
| Dash / Streamlit / Shiny | No — needs a running Python server | **Rejected** |
| `ipywidgets` / Jupyter kernel | No — needs a live kernel; the site is static HTML | **Rejected** (used only in a student's own local notebook, never relied on by a page) |
| Client-side JavaScript / SVG / Canvas | Yes | **Adopted** |
| Plotly via CDN | Yes, but ~3.5 MB per page and a runtime CDN dependency | **Not used for site labs**; available inside notebooks for student exploration |

### 1.1 Site labs: dependency-free SVG + vanilla JavaScript

Every interactive on the website is built on:

- **SVG** for graphics (crisp at any zoom, printable, inspectable, no canvas
  resolution bugs, works with `prefers-reduced-motion`).
- **Vanilla ES2020 JavaScript** — no framework, no build step, no bundler.
- **One shared helper**, `docs/assets/javascripts/viz.js` (scales, axes, line,
  area, bars, scatter, rug plot), and **one shared runtime**,
  `docs/assets/javascripts/labs.js` (widget registry, controls, readouts, reset,
  keyboard support).

Why not Plotly for the site: three megabytes of JavaScript per page for a chart
that needs two axes and a thousand points is a poor trade on a course read on
mobile data; it also fails the offline-study goal and adds a CDN dependency that
can disappear. The custom path costs about 12 KB uncompressed total and gives full
control of accessibility and print output. Plotly remains the right tool *inside*
notebooks, where the student has a kernel and wants rotation, zoom and hover — a
policy already recorded in [05](05-tools-and-libraries.md).

**Consequence accepted:** we maintain the plotting helper ourselves. It is
therefore capped at what the course actually needs (line, area, bar, scatter,
rug, reference lines, annotations) and covered by the lab regression checks in
§9. It is not a general charting library and must not grow into one.

### 1.2 Hard constraints (I-1)

| ID | Constraint | Verification |
|---|---|---|
| I-1.1 | No backend, no server-side code, no database | static files only; `mkdocs build` output inspected |
| I-1.2 | No API keys, no paid services, no account | grep for `api_key`, `token`, `fetch(` in lab sources |
| I-1.3 | No third-party runtime dependency for a lab | `grep -r "https://" docs/assets/javascripts/` returns nothing |
| I-1.4 | Works with JavaScript disabled (degrades to a static figure + the full worked example) | `<noscript>` block on every lab page |
| I-1.5 | Responsive from 320 px to 2560 px | viewport checks at 320/768/1440 |
| I-1.6 | Total lab JavaScript < 40 KB uncompressed per page | file sizes summed at build |
| I-1.7 | Keyboard operable; every control reachable and labelled | tab-through check, ARIA audit |
| I-1.8 | Respects `prefers-reduced-motion` | animation gated on the media query |

## 2. What every interactive must contain (I-2)

The ten requirements from the brief, made concrete. A widget that omits any of
these is not finished.

| ID | Requirement | Implementation rule |
|---|---|---|
| I-2.1 | **Clear instructions** | A one-sentence instruction above the controls, in the imperative: "Drag *n* to change the sample size." |
| I-2.2 | **Meaningful defaults** | Defaults produce an *interesting* result immediately — never an empty plot or a degenerate case. Defaults are stated in the prose. |
| I-2.3 | **Immediate visual feedback** | Updates on `input` (while dragging), debounced to one frame; no "Run" button unless the computation exceeds ~50 ms (Monte Carlo labs use an explicit "Run simulation" button and say why). |
| I-2.4 | **Explains what changes** | A live sentence under the figure that restates the current state in words, e.g. "*n* = 10: the histogram of the mean is still skewed; the normal curve does not fit yet." |
| I-2.5 | **Mathematical explanation alongside** | Every lab page carries the formula, the notation, and why the visual behaves as it does — the widget illustrates mathematics that is written out on the same page. |
| I-2.6 | **Not decorative** | Each lab has a stated *learning claim* in the catalogue (§4). If the claim cannot be written, the lab is not built. |
| I-2.7 | **Accessible** | `role="img"` + descriptive `aria-label` on the SVG, updated with state; the textual readout duplicates the visual information; controls are real `<input>`/`<button>` elements. |
| I-2.8 | **Print-safe** | In print, the widget shows its default state as a static figure plus the explanation (CSS hides controls). |
| I-2.9 | **Reset** | Every widget has a "Reset to defaults" button. |
| I-2.10 | **Try-this prompt** | Each lab ends with two or three specific experiments ("Set *n* = 2, then 5, then 30. At what *n* does the skew disappear?") and a short reflection question whose answer is in the module. |

### 2.1 Standard widget anatomy

```
┌─────────────────────────────────────────────────────────┐
│  Lab title · module reference                           │
├─────────────────────────────────────────────────────────┤
│  Instruction (imperative, one sentence)                 │
│  ┌─────────── controls ───────────┐  ┌── figure ─────┐  │
│  │ n        [ 1 ──●──── 100 ]  10 │  │  SVG axes     │  │
│  │ p        [ 0.5 ──●── 0.9 ] 0.5 │  │  + curve      │  │
│  │ [Run] [Reset]                  │  │  + histogram  │  │
│  └────────────────────────────────┘  └───────────────┘  │
│  Readout: "B = 2,000 samples · SE = 0.158 · skew = 1.2" │
│  What changed: "Doubling n halves the standard error."  │
├─────────────────────────────────────────────────────────┤
│  The mathematics (formula + one paragraph)               │
│  Try this: three experiments                             │
└─────────────────────────────────────────────────────────┘
```

## 3. Simulation protocol (S)

Simulation is a first-class method in this course, not an illustration. Every
important simulation — in a module page or a notebook — follows the same eight
steps, in order. A section that skips a step is incomplete.

| Step | Requirement |
|---|---|
| **S-1** | *Theory.* State the concept and the exact result being simulated, with symbols. |
| **S-2** | *Experiment.* Define the random experiment precisely: the sample space, the number of replications *B*, the statistic recorded per replication. |
| **S-3** | *Expected result.* State the mathematical expectation **before** running anything — E[X̄] = μ, Var = σ²/n, P(heads) = 0.5. Prediction precedes observation. |
| **S-4** | *Implementation.* Reproducible code: `rng = np.random.default_rng(2026)`, vectorised, no loops where an array operation exists. |
| **S-5** | *Results.* Show output: a figure, a table, or a printed comparison — always with the seed stated. |
| **S-6** | *Comparison.* Put theory and simulation side by side numerically, with the discrepancy expressed in Monte Carlo standard errors, not as "close enough". |
| **S-7** | *Explanation of discrepancy.* Why they differ: sampling variability of the estimate, finite *B*, approximation error of a limit theorem, numerical precision. |
| **S-8** | *Student modification.* 2–3 concrete parameter changes the student must make and predict, each with a question they can answer themselves. |

### 3.1 Mandatory simulation catalogue

These experiments must exist, each with all eight steps, in the module or notebook
named. Phase column shows where it is delivered.

| # | Experiment | Module | Deliverable | Phase |
|---|---|---|---|---|
| 1 | Coin tossing (fair and biased, LLN) | 05, 06 | Notebook `m05` | 2 |
| 2 | Dice experiments (sums, distributions, CLT seed) | 05, 10 | Notebook `m05`, lab L-01 | 2 |
| 3 | Card probability (without replacement, hypergeometric) | 05, 10 | Notebook `m10` | 3 |
| 4 | Random sampling and the standard error | 15 | Lab L-03, notebook `m15` | 4 |
| 5 | Monte Carlo estimation of π and of an integral | 28 | Notebook `m28` | 6 |
| 6 | Law of Large Numbers (normal and Cauchy) | 16 | Lab L-02, notebook `m16` | 4 |
| 7 | Central Limit Theorem across parents and *n* | 17 | **Lab L-04 (Phase 1 reference lab)**, notebook `m17` | 1, 4 |
| 8 | Sampling distributions of X̄ and s² | 15 | Lab L-03, notebook `m15` | 4 |
| 9 | Bootstrap sampling (SE and percentile CI) | 26, 28 | Lab L-11, notebook `m26` | 5 |
| 10 | Permutation test | 26 | Lab L-12, notebook `m26` | 5 |
| 11 | Bayesian updating (Beta–Bernoulli) | 08, 27 | Lab L-09, notebook `m08` | 2 |
| 12 | Confidence-interval coverage | 19 | **Lab L-05 (Phase 1 reference lab)** | 1 |
| 13 | Power, Type I and Type II error | 20 | Lab L-07, notebook `m20` | 4 |
| 14 | Regression with noise (sampling variability of β̂) | 22 | Lab L-08, notebook `m22` | 5 |

## 4. Interactive lab catalogue

Learning claim = what a student can do after using the lab that they could not do
before. Labs without a claim are not built (I-2.6).

| ID | Lab | Module | Student manipulates | Updates live | Learning claim | Phase |
|---|---|---|---|---|---|---|
| L-01 | Distribution explorer | 10, 11 | family, parameters *n, p, λ, μ, σ* | PMF/PDF + CDF, mean, variance, skew | Match a real scenario to a family by *shape*, not by formula recall | 3 |
| L-02 | LLN running mean | 16 | *B*, distribution, heavy-tailed toggle | running average vs trials, ±2 SE band | Distinguish "average converges" from "data become normal" | 4 |
| L-03 | Sampling machine | 15 | *n*, *B*, parent skew | histogram of X̄, theoretical SE overlay | See that a statistic has its own distribution | 4 |
| L-04 | **CLT** | 17 | *n*, parent distribution, *B* | histogram of standardised mean, normal overlay, QQ inset | Predict when the normal approximation is acceptable | **1** |
| L-05 | **CI coverage** | 19 | confidence level, *n*, *B* | 100 intervals vs μ, coverage counter | Interpret "95%" as a property of the procedure | **1** |
| L-06 | p-value and rejection region | 20 | effect size, *n*, α, one/two-tailed | test statistic distribution, shaded tails, p-value | See that p depends on *n* as well as on effect | 4 |
| L-07 | Errors and power | 20 | δ, *n*, σ, α | overlap of H₀/H₁, β, power, sample-size curve | Trade off α, β and n explicitly | 4 |
| L-08 | Correlation and regression | 21, 22 | r, n, noise, one draggable outlier | scatter, fitted line, r, slope, CI | See how one point moves r and β̂ | 5 |
| L-09 | Bayes updater | 08, 27 | prior α, β, observed successes | prior, likelihood, posterior densities | Watch the base rate dominate a "99% accurate" test | 2 |
| L-10 | Mean/SD explorer | 03 | data points (draggable), distribution shape | mean, median, SD, IQR, box plot | See that one point moves the mean but not the median | 2 |
| L-11 | Bootstrap | 26 | *B*, statistic (mean/median), sample | resampling distribution, CI | Resampling approximates sampling without formulas | 5 |
| L-12 | Permutation test | 26 | group labels, *B*, effect | null distribution, p-value | Randomisation is the reference distribution | 5 |
| L-13 | Prior sensitivity | 27 | prior strength, data count | posterior family of curves | Quantify how much the prior matters with little data | 6 |

**Phase 1 delivers L-04 and L-05** — deliberately the two most conceptually
difficult ideas in the course — because they prove the technology, the
accessibility pattern and the shared helper under real conditions. Every later lab
reuses the same runtime; adding one is a data file, not a new framework.

## 5. Theory-to-Python integration (P)

| ID | Rule |
|---|---|
| P-1 | Every module that introduces a computable quantity has a runnable Python demonstration on the page **and** an exercise the student must code. |
| P-2 | Every practical explains four things: the **mathematics**, the **code**, the **output**, and the **statistical interpretation**. Code without interpretation is not a demonstration. |
| P-3 | Manual calculation and Python must both be shown for the same number at least once per module — the student must see the arithmetic that the function performs. |
| P-4 | The stack is Python 3, NumPy, pandas, SciPy, Matplotlib, Seaborn, statsmodels, scikit-learn where relevant (and PyMC only in M27, optionally). |
| P-5 | No black boxes: `statsmodels`/`scipy` output is always read line by line, and every analytical result is cross-checked numerically. |

### 5.1 Mandatory concept → practical mapping

| Mathematical concept | Practical application | Where |
|---|---|---|
| Bayes' theorem | Medical diagnostic probability, PPV vs prevalence | M08 page + Lab L-09 + notebook `m08` |
| Binomial distribution | Student pass/fail simulation | M10 page + notebook `m10` |
| Normal distribution | Examination score analysis, z-scores, percentiles | M11 page + notebook `m11` |
| Central Limit Theorem | Repeated sampling simulation | M17 page + Lab L-04 + notebook `m17` |
| Confidence intervals | Average customer spending estimation | M19 page + Lab L-05 + notebook `m19` |
| Hypothesis testing | Comparing two teaching methods | M20 page + notebook `m20` |
| Regression | Student performance prediction | M22–M23 pages + Lab L-08 + notebooks |
| ANOVA | Comparing multiple product groups | M24 page + notebook `m24` |
| Sampling distributions | Standard error of the mean across *n* | M15 page + Lab L-03 |
| Probability foundations | Coin/dice/card experiments | M05–M06 + notebook `m05` |
| Covariance | Portfolio variance of two assets | M14 + notebook `m14` |
| Chi-square | Contingency table of survey responses | M25 + notebook `m25` |
| Nonparametrics | Paired before/after measurements | M26 + notebooks |
| Bayesian updating | Beta–Bernoulli learning curve | M27 + Lab L-09 + notebook `m27` |
| Monte Carlo | π, integrals, rare-event probability | M28 + notebook `m28` |
| Experimental design | A/B test with peeking demonstration | M29 + notebook `m29` |

Each mapping is satisfied only when the page, the lab and the notebook all exist;
a phase report must state which leg is missing.

## 6. Understanding before memorisation (M)

| ID | Rule |
|---|---|
| M-1 | No formula appears before its intuition. The order on the page is: idea in words → picture → symbols → derivation → computation. |
| M-2 | Every formula block carries: **intuition**, **symbol definitions**, **derivation or justification**, **numerical example**, **assumptions**, **when to use**, **limitations**. |
| M-3 | Limit theorems are taught empirically first: repeated sampling and visualisation precede the formal statement (this is why L-04 exists in Phase 1, before Module 17 is written). |
| M-4 | Confidence intervals, p-values and hypothesis tests are introduced through their *procedure* and long-run behaviour, with the misinterpretation corrected explicitly in the same section. |
| M-5 | A "why it looks like that" sentence accompanies every figure. |

### 6.1 Formula block template

```markdown
!!! theorem "Result — Standard error of the mean"

    \[ \se(\bar X) = \frac{\sigma}{\sqrt{n}} \]

    **In words.** Averaging \(n\) independent observations shrinks the typical
    error of the average by a factor of \(\sqrt{n}\).

    **Symbols.** ...

    **Where it comes from.** ... (derivation)

    **Numbers.** For \(\sigma = 10\), \(n = 100\): \(\se = 1.0\).

    **Assumptions.** Independent observations; finite variance; fixed \(n\).

    **Use it when.** ...

    **Limits.** ...
```

## 7. Academic quality (A)

| ID | Rule |
|---|---|
| A-1 | Explanations are original prose. Where a treatment follows a specific source, cite it in the text and list it in "Further reading". |
| A-2 | Every numerical example is independently recomputed (Python and, where feasible, by hand) before release. |
| A-3 | Every derivation is checked by the four-pass review in [09 §4](09-risks-and-quality.md). |
| A-4 | **No fabricated references.** Every citation is a real, verifiable work with correct author, year, title and publisher. If a page number is uncertain, omit the page number rather than invent one. |
| A-5 | No fabricated datasets, sources or research findings. Dataset provenance is recorded with URL, retrieval date and licence. |
| A-6 | Synthetic data is labelled as synthetic, visibly, in the page, the caption and the notebook header. |
| A-7 | Conclusions are scoped to the evidence; no causal language without a design that supports it. |
| A-8 | Assumptions and limitations are stated for every procedure, not only when violated. |
| A-9 | Copyright is respected: figures are original or openly licensed and attributed; quotations are short and attributed. |

### 7.1 Reference standard

Further reading is drawn from works that exist and are standard in the field. The
canonical list (to be used consistently, not exhaustively):

- Casella, G. & Berger, R. L. *Statistical Inference*, 2nd ed., Duxbury, 2002.
- Ross, S. *A First Course in Probability*, 10th ed., Pearson, 2019.
- Wasserman, L. *All of Statistics*, Springer, 2004.
- DeGroot, M. H. & Schervish, M. J. *Probability and Statistics*, 4th ed., Pearson, 2012.
- Gelman, A. et al. *Bayesian Data Analysis*, 3rd ed., CRC Press, 2013.
- James, G. et al. *An Introduction to Statistical Learning*, 2nd ed., Springer, 2021.
- Efron, B. & Tibshirani, R. J. *An Introduction to the Bootstrap*, Chapman & Hall, 1993.
- McKinney, W. *Python for Data Analysis*, 3rd ed., O'Reilly, 2022.
- American Statistical Association. *Ethical Guidelines for Statistical Practice*, 2022.

Editions and years are verified against the publisher before a module ships; any
entry that cannot be verified is removed rather than guessed.

## 8. Learner experience (L)

| ID | Rule |
|---|---|
| L-1 | Written directly to the student ("you", "we"), never as a lesson plan. |
| L-2 | No lecture-delivery instructions, no timing scripts, no classroom-management material anywhere in `docs/`. |
| L-3 | Instructor information appears only on the homepage, the syllabus and the About page. |
| L-4 | Every module ends with guided exercises, independent challenges, a self-assessment quiz with explained answers, a revision summary and further reading. |
| L-5 | Difficulty is signposted: ★ guided, ★★ application, ★★★ independent challenge. |
| L-6 | "Where you are" cues on every page: part, module number, prerequisites, next step. |
| L-7 | Every lab and simulation ends with a modification task (I-2.10, S-8), so interaction always produces learning work. |

## 9. Phase quality gates (G)

No phase is declared complete until all nine gates pass **with recorded evidence**.
A phase report that cannot cite evidence marks the item incomplete.

| Gate | Requirement | Evidence required |
|---|---|---|
| **G-1** Mathematical correctness | every new formula, derivation and numeric example checked | four-pass review notes; simulation or `sympy` cross-check output |
| **G-2** Educational completeness | every new page passes the 18-point module checklist | checklist results per page |
| **G-3** Python execution | all new notebooks run end-to-end in a clean environment | `tools/execute_notebooks.py` exit status |
| **G-4** Visualisation validation | every new lab renders, responds, resets, and works by keyboard; no console errors | recorded interaction log + console/network check |
| **G-5** Internal links | zero broken internal links | `mkdocs build --strict` + link checker output |
| **G-6** Markdown and math rendering | equations render before and after client-side navigation; tables and admonitions correct | rendered-page check on at least one page per part |
| **G-7** Site build | `mkdocs build --strict` clean | command output |
| **G-8** No regression | previously delivered files unmodified except where this phase intends it | file manifest and diff review |
| **G-9** Honest reporting | incomplete or unverifiable items listed explicitly with the phase that will complete them | phase report §"Incomplete or deferred" |

**G-4 procedure** (in full, because it is the gate most easily faked):

1. Load the lab page in the local preview server.
2. Confirm the default state renders a non-empty figure and a numeric readout.
3. Move each control; confirm the figure updates and the "what changed" sentence
   updates.
4. Press Reset; confirm defaults are restored exactly.
5. Tab through every control; confirm focus is visible and order is logical.
6. Confirm a descriptive `aria-label` is present and changes with state.
7. Check the console for errors and the network panel for failed requests.
8. Reload with JavaScript disabled; confirm the static fallback and the text
   explanation are present.

## 10. Scope of this phase and what is deferred

Per the implementation instruction, anything not completable now is recorded here
with its destination phase rather than implied to be done.

| Item | Status after Phase 1 | Phase |
|---|---|---|
| Shared lab runtime (`viz.js`, `labs.js`) | delivered | 1 |
| Labs L-04 (CLT), L-05 (CI coverage) | delivered | 1 |
| Labs L-01, L-02, L-03, L-06, L-07 | specified in §4 | 3–4 |
| Labs L-08, L-11, L-12 | specified in §4 | 5 |
| Labs L-09, L-13 | specified in §4 | 2, 6 |
| Lab L-10 | specified in §4 | 2 |
| Simulation catalogue (14 experiments) | specified in §3.1 | 2–6 |
| Theory→Python mappings (16) | specified in §5.1 | 2–6 |
| `tools/execute_notebooks.py` | not yet needed (no notebooks) | 2 |
| Glossary, formula sheet, tables | not yet created | 7 |
| Deployment workflow | documented, not installed | 9, on authorisation |
