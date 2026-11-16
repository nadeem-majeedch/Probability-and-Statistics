# Maintainer quality standards

This file records the standards that every part of the course must meet before a
change is merged. It is written for whoever maintains the site next: the rules are
deliberately mechanical, because "looks fine" is not a review standard.

Run the whole suite from the repository root before opening a pull request:

```bash
python tools/check_math.py
python tools/check_assets.py
python tools/check_examples.py
python tools/check_assessments.py
python tools/check_projects.py
python tools/check_case_studies.py
python tools/check_notebooks.py
python tools/check_labs.py
python tools/check_tables.py
python tools/make_figures.py --check
mkdocs build --strict
python tools/check_site.py
```

`tools/check_labs.py` also runs the JavaScript test suite (`node --test tests/`), so
Node is required for a full check. Without Node the lab tests are skipped with a
warning; that is not acceptable for a release.

## 1. Content standards

- **Every numerical claim is computed.** Numbers in prose are reproduced by
  `tools/check_examples.py`, by a notebook, or by an interactive laboratory.
- **No approximations without a label.** If a formula is asymptotic, a normal
  approximation, or a Monte Carlo estimate, the text says so next to the number.
- **Population parameters and sample statistics are never conflated.** Use
  \(\mu, \sigma, p\) for parameters and \(\bar x, s, \hat p\) for statistics.
- **Density is not probability.** Any continuous distribution is introduced through
  area, and every lab that plots a density states in the figure or caption that the
  height is not a probability.
- **Significance is not importance.** Effects are reported with a size measure
  (\(R^2\), \(\eta^2\), a difference in original units), not only a p-value.
- **Assumptions are stated where they are used**, not in a footnote: independence,
  finite variance, normality, equal variances, linearity.

## 2. Interactive laboratory standards

Every laboratory page must contain, in this order:

1. title and a line naming its code, module and paired notebook;
2. learning objectives;
3. a conceptual introduction;
4. the mathematical foundation, with assumptions;
5. instructions for the experiment;
6. the interactive block (`<div class="psds-lab" data-lab="…">`) with controls and a
   live figure;
7. a results panel of calculated values and a written interpretation;
8. guided activities and independent challenges;
9. an expected-observations table;
10. self-assessment questions with worked answers;
11. links to the module, the notebook and the neighbouring labs.

Technical rules for laboratories:

- **Client-side only.** No backend, no API keys, no network requests, no cookies, no
  `localStorage`. `tools/check_labs.py` fails on `fetch(`, `XMLHttpRequest`,
  `localStorage` or an `http` URL in the lab scripts.
- **One numerical core.** All probability and distribution functions live in
  `docs/assets/javascripts/stats.js`. Lab modules must not re-implement a CDF, a
  quantile or a p-value.
- **Registered builders.** A lab page's `data-lab` value must appear as
  `REG.builders.<name>` in one of the lab modules, or the figure silently never
  appears.
- **Deterministic defaults.** Each lab seeds its PRNG from `data-seed`, so the default
  state is reproducible. Any control that resamples says so in its hint text.
- **Accessible output.** Every SVG gets `role="img"` and a state-dependent
  `aria-label`; the numeric results are restated in text; controls are real
  `<input type="range">` and `<select>` elements so the keyboard works.
- **Honest simulation language.** If a number is simulated, the page says repeated runs
  differ and reports the relevant Monte Carlo error or replication count.

## 3. Numerical testing standards

`tests/labs.test.js` is run by `node --test`. It must cover:

- **Reference agreement.** Distribution functions are compared with SciPy values
  pasted into the test file, with tolerances stated per test (typically 1e-13).
- **Boundaries.** `k < 0`, `k > n`, `p = 0`, `p = 1`, zero within-group variance,
  constant variables, `p` at 0 and 1 in `normInv`.
- **Ranges.** Every density is non-negative; every CDF, tail probability and p-value
  lies in \([0,1]\).
- **Stability.** Extreme inputs (a t statistic of \(10^6\), a normal tail at \(-30\),
  \(\lambda = 500\)) return finite values rather than `NaN` or `Infinity`.
- **Model identities.** \(\sum \text{pmf} = 1\), CDF differences equal PMF values,
  \(\int f = 1\), \(R^2 = r^2\), \(\text{SSB} + \text{SSW} = \text{SST}\), and
  power at zero effect equals \(\alpha\).

If a test fails, fix the mathematics. Do not loosen a tolerance without a comment
explaining why, and never delete a boundary test to get a green run.

## 3b. Statistical table standards

The reference tables in `docs/reference/tables/` are generated artefacts. Rules:

- **Never hand-edit a number in a table.** Run `python tools/generate_tables.py`;
  it rewrites the Markdown blocks between the `<!-- block:name -->` markers and the
  CSV downloads in `docs/data/tables/`.
- **Every value comes from SciPy quantile functions**, with the tail convention
  stated on the page and in the generator docstring (upper tail, except the normal
  table which prints the CDF).
- **`tools/check_tables.py` must pass.** It re-derives every published cell from a
  second formulation (bisection on the survival function), checks the CSV downloads
  against the pages, checks monotonicity, symmetry and the normal limit row, and
  checks that every quoted worked example matches its table.
- **State the precision.** Each table's decimals and the resulting maximum rounding
  error are documented on the overview page; a new table needs the same disclosure.

## 4. Site and build standards

- `mkdocs build --strict` must exit 0 with no warnings.
- `tools/check_site.py` must report the generated site as complete and internally
  consistent (links, anchors, navigation).
- Figures: `tools/make_figures.py` regenerates every SVG deterministically and
  `--check` verifies that every referenced figure exists and none is orphaned.
- Notebooks are executed by `tools/check_notebooks.py`; a notebook that errors is a
  failing build.
- New pages must be added to the navigation in `mkdocs.yml`; a page outside the
  navigation is a warning in strict mode.
- Laboratory scripts load in this order: `mathjax.js`, `stats.js`, `viz.js`,
  `labs.js`, `labs-kit.js`, then the lab modules, then `quiz.js` and `progress.js`.
  Changing that order breaks the registry.

## 5. Browser checks

Before a release, open the built site and check at 390 px, 834 px and 1440 px, in both
light and dark themes:

- no horizontal page overflow (`document.documentElement.scrollWidth` within 1 px of
  the viewport);
- every lab initialises: controls present, figure drawn, results table filled;
- moving each control updates the readout;
- the console has no errors.

## 6. What to do when adding a laboratory

1. Add the mathematics to `stats.js` if it is not already there, with a comment naming
   the formula.
2. Add a builder in the matching `labs-*.js` module and register it with
   `REG.builders.<name> = build…;`.
3. Write the page with all eleven required sections and the `data-lab` block.
4. Add the page to the navigation, the laboratory index table, the module callout and
   the practicals cross-reference.
5. Add tests for the new mathematics and run the whole suite above.
