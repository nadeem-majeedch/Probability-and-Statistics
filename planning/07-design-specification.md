# 07 — Design Specification

A professional academic design for a modern documentation site: confident
typography, restrained colour, generous whitespace, and a page structure a student
can navigate blindfolded by the third module.

**Design intent.** A university press monograph that happens to be a website —
not a SaaS landing page and not a corporate wiki. Authority comes from structure,
consistency and legibility, not decoration.

---

## 1. Colour

Two complete palettes. Both are defined as CSS custom properties in
`docs/assets/stylesheets/extra.css`, with `primary: custom` / `accent: custom` in
`mkdocs.yml` so Material inherits them.

### Light

| Token | Hex | Use |
|---|---|---|
| `--psds-primary` | `#1E3A8A` | header, active nav, section rules |
| `--psds-primary-light` | `#3B5BC0` | hover states |
| `--psds-primary-dark` | `#14265E` | pressed states, dark headers |
| `--psds-accent` | `#0F766E` | links, focus rings, active TOC marker |
| `--psds-accent-soft` | `#E6F4F2` | highlighted callout backgrounds |
| `--psds-bg` | `#FFFFFF` | page background |
| `--psds-surface` | `#F5F7FB` | cards, table stripes, sidebar |
| `--psds-border` | `#E2E8F0` | rules, card borders |
| `--psds-text` | `#1A2233` | body text |
| `--psds-text-muted` | `#5B6577` | captions, metadata |
| `--psds-success` | `#15803D` | correct answers, "complete" |
| `--psds-warning` | `#B45309` | pitfalls, caution |
| `--psds-danger` | `#B91C1C` | critical errors, counterexamples |

### Dark

| Token | Hex | Use |
|---|---|---|
| `--psds-primary` | `#8FA8FF` | headers, active nav |
| `--psds-accent` | `#2DD4BF` | links, focus rings |
| `--psds-bg` | `#0B1220` | page background |
| `--psds-surface` | `#111A2B` | cards, sidebar, table stripes |
| `--psds-border` | `#1E2A3D` | rules, borders |
| `--psds-text` | `#E6EDF7` | body text |
| `--psds-text-muted` | `#A3B0C2` | captions, metadata |

**Rules.**

- Accent teal means "interactive" and never "important". Semantic colour is
  reserved for admonitions.
- Never encode meaning in colour alone — every status also carries an icon or a
  word (accessibility, §9).
- Figures use a colour-blind-safe qualitative palette (Okabe–Ito), not the theme
  palette, so a chart in a module and the same chart in a notebook look identical.

```css
/* chart palette, shared by matplotlib style file and CSS legends */
#0072B2 /* blue */   #D55E00 /* vermillion */  #009E73 /* green */
#CC79A7 /* purple */ #E69F00 /* orange */      #56B4E9 /* sky */
```

## 2. Typography

| Role | Family | Size / weight | Notes |
|---|---|---|---|
| Body | **Inter** | 16 px / 400, line-height 1.65 | `--md-text-font-family` |
| Headings | Inter | h1 2.0 rem/700, h2 1.5 rem/600, h3 1.2 rem/600 | tight tracking (−0.01 em) |
| Code | **JetBrains Mono** | 0.875 rem / 400 | tabular figures for numeric output |
| Captions | Inter | 0.875 rem / 400, muted | precedes or follows every figure |
| Math | MathJax CHTML | 1.0 em, inherits body colour | must not sit in a smaller font than prose |

**Optional academic variant.** For a more book-like feel, body text can be set in
a serif (`Source Serif 4`) while headings stay Inter:

```css
:root { --md-text-font-family: "Source Serif 4", Georgia, serif; }
```

This is documented as a one-line switch, not adopted by default: Inter survives
small screens and dense notation better, and consistency between the site,
notebooks and print matters more than stylistic flavour. Decide in Phase 1 by
looking at one real module both ways.

**Measure.** Body text is capped at ~72 characters:

```css
.md-content__inner > :is(p, ul, ol, blockquote) { max-width: 46rem; }
```

Long lines are the most common readability failure in documentation themes, and
statistics pages are read line by line, not skimmed.

## 3. Layout

| Breakpoint | Behaviour |
|---|---|
| ≥ 1220 px | sidebar + content + TOC, three columns |
| 960–1219 px | sidebar + content, TOC collapses |
| 600–959 px | drawer navigation, full-width content |
| < 600 px | single column, 1 rem side padding, tables scroll horizontally |

Content hierarchy per page:

1. Breadcrumb path (part → module)
2. Title + metadata strip (level · hours · prerequisites · last updated)
3. Progress control ("Mark complete")
4. Table of contents (right, sticky on desktop)
5. Body
6. Previous / next module footer

Module pages carry two deliberate structural cues: a **"You are here"** line under
the title (*Part III · Module 14 of 30*), and a **prerequisite chip row** linking
Modules 13 and 15. Both exist because the single biggest self-study failure is
losing the thread of a long course.

## 4. Course homepage anatomy

```
┌──────────────────────────────────────────────────────────────┐
│  header · logo · search · light/dark toggle · GitHub         │
├──────────────────────────────────────────────────────────────┤
│  HERO                                                        │
│  Probability and Statistics for Data Science                 │
│  A complete self-study course for BS Data Science students   │
│  [ Start with Module 01 ]  [ Read the syllabus ]             │
│  Instructor · Programme · 30 modules · ~270 hours            │
├──────────────────────────────────────────────────────────────┤
│  STAT STRIP   30 modules │ 8 parts │ 18 notebooks │ 400+ ex. │
├──────────────────────────────────────────────────────────────┤
│  "WHERE TO START"  three cards:                              │
│    New to statistics → path A (Modules 01→20)                │
│    Know probability → path B (Modules 15→20)                 │
│    Here for modelling → path C (Modules 21→26)               │
├──────────────────────────────────────────────────────────────┤
│  COURSE MAP  eight part cards, each listing its modules      │
│  with level chips and hour counts                            │
├──────────────────────────────────────────────────────────────┤
│  HOW IT WORKS  4 icons: derivations · worked examples ·      │
│  Python · self-assessment                                    │
├──────────────────────────────────────────────────────────────┤
│  PROJECTS  three cards                                       │
├──────────────────────────────────────────────────────────────┤
│  ABOUT THE INSTRUCTOR · licence · citation                   │
└──────────────────────────────────────────────────────────────┘
```

The homepage is built from `mkdocs-material`'s grid (`md_in_html` + `attr_list`)
with cards defined in `extra.css` — no template override, so it survives a theme
upgrade.

## 5. Module page template

Every one of the 30 module pages uses this skeleton, in this order. Consistency is
the pedagogy: by Module 03 the student knows where the derivation lives and where
the exercises are.

| # | Section | Content obligations |
|---|---|---|
| 1 | **Learning objectives** | 5–9 measurable statements, checkbox list |
| 2 | **Before you start** | prerequisite links, a 10-minute refresher, the one formula to recall |
| 3 | **The idea in plain language** | no symbols; the concept as if explaining to a colleague |
| 4 | **Notation and derivation** | every symbol defined at first use; numbered equations; every step justified |
| 5 | **Intuition** | a second explanation — physical, geometric or visual |
| 6 | **Worked examples** | 2–4 complete numerical solutions, arithmetic shown |
| 7 | **Where this is used** | 2–3 data-science applications, each specific |
| 8 | **Visual explanations** | 2–5 figures, each with a caption saying what to look at |
| 9 | **Python demonstration** | runnable code that reproduces the mathematics, then extends it |
| 10 | **Exercises** | ★ / ★★ / ★★★, with marks and time estimates |
| 11 | **Self-assessment quiz** | 8–10 items, answers in collapsible blocks |
| 12 | **Summary and revision** | key results, formula box, common errors, "you can now…" |

Section 12 ends with explicit forward links: *"Next: Module 15 — Sampling
Distributions"* and *"If you struggled with §4, revisit Module 13 §3."*

## 6. Component vocabulary

Admonitions are used semantically, never decoratively. The same idea always looks
the same across 30 modules.

| Purpose | Syntax | Example use |
|---|---|---|
| Formal definition | `!!! abstract "Definition"` | "A random variable is…" |
| Theorem / result | `!!! theorem "Theorem 17.1 (CLT)"` | statement, then proof below |
| Proof | `!!! proof "Proof"` (collapsible) | derivation the student should attempt first |
| Worked example | `!!! example "Example"` | numbered, with a stated answer |
| Intuition | `!!! tip "Intuition"` | the informal second explanation |
| Pitfall | `!!! warning "Common error"` | "p is not the probability that H₀ is true" |
| Note | `!!! note` | clarification, aside |
| Real data | `!!! quote "In practice"` | application vignette |
| Historical | `!!! info "History"` | Bayes, Fisher, Gosset — used sparingly |
| Self-check | `??? question "Check yourself"` | collapsible question |
| Answer | `??? success "Answer"` | collapsible solution |
| Exercise | `???+ example "Exercise ★★"` | open by default, solution collapsed inside |

`extra.css` gives `theorem`, `proof` and `definition` a left rule in
`--psds-primary` and a subtle surface background, so a student can find the
mathematics by flipping pages quickly.

**Quiz pattern** (self-marking, no JavaScript, works offline):

```markdown
??? question "1. A test has sensitivity 0.99 and specificity 0.99. Prevalence is 0.1%. What is PPV?"
    Work it out with Bayes' theorem before opening the answer.

    ??? success "Answer"
        Approximately 9%. The base rate dominates: of 1,000 people, ~10 have the
        disease and ~1 is missed; ~10 false positives arise among 990 healthy
        people. \(9/(9+10) \approx 0.47\)… work the arithmetic yourself and check
        against §8.
```

**Tables.** Numeric columns right-aligned, units in the header, no vertical rules,
zebra striping only for tables longer than 8 rows.

## 7. Figures and code

**Figures.**

- Vector SVG for line art and diagrams; PNG at 150 dpi for dense scatter plots.
- Every figure has a caption *above* the image, one sentence: what it shows and
  what the reader should notice.
- Axes always labelled with units; no chartjunk; no 3-D; no rainbow colormaps
  (use viridis or the Okabe–Ito palette).
- Every figure is reproducible: the generating script is in the module notebook and
  the caption ends with the notebook reference.
- Alt text is mandatory and describes the *finding*, not the file
  ("Histogram of 1,000 exponential draws: right-skewed with mode at 0, mean 1").

**Code.**

- Python only, `python` fence, PEP 8, ≤ 79 characters, no line continuations
  inside strings.
- `rng = np.random.default_rng(2026)` at the top of any stochastic example; the
  seed is stated in the prose so a student gets the same numbers.
- Outputs shown directly under the code as a fenced block or a real figure — a
  demonstration without visible output is not a demonstration.
- `statsmodels` summaries are never pasted raw without a line-by-line reading: the
  teaching value is in the reading, not in the printout.

## 8. Mathematical notation standard

One symbol, one meaning, across all 30 modules. Enforced by MathJax macros (§4 of
[06](06-website-architecture.md)) and documented in `reference/notation.md`.

| Quantity | Notation | Never |
|---|---|---|
| Random variable | capital italic `X` | `x` for the variable |
| Realised value | lowercase `x` | `X` for the value |
| Sample mean | `\bar{x}` | `x̄` typed as a combining character |
| Expectation | `\E[X]` | `E(X)`, `mean(X)` |
| Variance | `\Var(X)` | `V(X)`, `σ²(X)` |
| Standard deviation | `\sd(X)` | `S(X)` |
| Standard error | `\se(\hat\theta)` | `SE` in body text without definition |
| Covariance | `\Cov(X,Y)` | `cov` lowercase in display math |
| Correlation (population/sample) | `\rho` / `r` | `R` |
| Parameter / estimator / estimate | `\theta` / `\hat\theta` / `\hat\theta_{\text{obs}}` | reusing `θ` for all three |
| Sample size | `n`; population size `N` | `N` for both |
| Significance level | `\alpha`; power `1-\beta` | `p < 0.05` as a definition of α |
| i.i.d. | `X_1,\dots,X_n \iid F` | "random sample" without a definition |
| Independent | `X \indep Y` | `X ⊥ Y` (ambiguous with orthogonality) |
| Normal | `X \sim N(\mu,\sigma^2)` | `N(μ, σ)` — variance, always |
| Probability | `\Pr(A)` | `P(A)` in display math |

Probability is always written as a number between 0 and 1 in derivations, and as a
percentage only in interpretation sentences, never both in the same expression.

## 9. Accessibility

Target: **WCAG 2.2 AA**.

| Requirement | Implementation |
|---|---|
| Contrast | body text ≥ 4.5:1, large text ≥ 3:1, verified per palette |
| Keyboard | all navigation, search, toggles and collapsibles operable without a mouse; visible focus ring in `--psds-accent` |
| Screen readers | semantic headings (one `h1` per page, no skipped levels); figure alt text; table headers via `attr_list`; math restated in words after display equations |
| Motion | `prefers-reduced-motion` disables the instant-navigation progress bar and hover transforms |
| Colour independence | admonitions carry icons and titles, not colour alone; charts annotated directly, not legend-only |
| Zoom | layout remains usable at 200% zoom and 320 px width |
| Language | `lang: en` on the theme; `abbr` tooltips for acronyms on first use per page |
| Print | `@media print` removes navigation, expands collapsed answers, forces black on white, keeps equations |

Math accessibility is the hardest part and is treated as a content rule rather
than a technical one: **every display equation that carries an argument is
followed by a one-sentence plain-language reading.** That sentence helps every
reader, and it is what makes the page usable with a screen reader.

## 10. Print and PDF

Students print revision sheets. Rules:

- Heading 1 starts a new page; no module page breaks inside a worked example.
- Admonition backgrounds become light grey; colour rules become black hairlines.
- Collapsed `???` blocks are expanded in print via CSS (`details[open]`), so an
  answer is never lost on paper.
- Page footer carries the module number and the course short title.

## 11. Voice and tone

Write as a careful lecturer writes on a board: direct, precise, never chatty, never
condescending.

- Second person for instructions ("derive this"), first person plural for shared
  reasoning ("we now have two estimators").
- Define a term before using it. Always.
- Prefer a concrete number to an adjective: "9% of positive tests are true
  positives", not "a surprisingly low proportion".
- No exclamation marks. No "simply", "obviously", "just" — they punish the student
  who is stuck.
- Every claim that could be false is either cited or derived.
- Humour only where it aids memory (the Monty Hall door, the prosecutor's fallacy).

## 12. Design do-nots

| Do not | Why |
|---|---|
| Use a hero image of "data" (circuit boards, blue binary) | signals a course without substance |
| Add a carousel, marquee, or animated banner | distraction; unreadable in print |
| Use more than two font families | visual noise |
| Use accent colour for emphasis in prose | accent means interactive |
| Put more than 8 figures in one module | sign the module should be split |
| Centre body text | destroys the reading line |
| Use `!!! danger` for ordinary warnings | dilutes the one case that matters |
| Hide essential content in tabs | tabs are for parallel alternatives only |
