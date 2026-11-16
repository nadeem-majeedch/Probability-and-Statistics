---
title: Interactive labs
description: Fourteen browser-based statistical laboratories — probability, distributions, sampling, inference, regression, Bayesian updating, power and ANOVA — with no installation.
---

# Interactive laboratories

Some statistical ideas are easier to *see* than to read. A confidence interval's
"95%" is a statement about a procedure's long-run behaviour, not about one interval —
and that becomes obvious the moment you watch a hundred intervals fall around a fixed
line, some of them missing. The same is true of a p-value, a posterior, or the
standard error: the definitions are short, and the behaviour is what students actually
need.

These fourteen laboratories each pair a small experiment with the mathematics behind
it. You change parameters, the figure responds, a numeric table gives the exact
values, and a written interpretation tells you what to notice. Nothing is installed,
nothing is sent anywhere, and every calculation runs in your browser.

## The laboratory set

| Lab | Topic | Module | Paired practical |
|---|---|---|---|
| [L-01](probability.md) | Random events and long-run frequency | 06 | [Practical 06](../practicals/notebooks/06-probability-fundamentals.ipynb) |
| [L-02](conditional-probability.md) | Conditional probability and Bayes' theorem | 07 | [Practical 07](../practicals/notebooks/07-conditional-probability-and-bayes.ipynb) |
| [L-03](discrete-distributions.md) | Discrete distributions | 09 | [Practical 09](../practicals/notebooks/09-discrete-distributions.ipynb) |
| [L-04](continuous-distributions.md) | Continuous distributions | 10 | [Practical 10](../practicals/notebooks/10-continuous-distributions.ipynb) |
| [L-05](normal-and-z-scores.md) | The normal distribution and z-scores | 10 | [Practical 10](../practicals/notebooks/10-continuous-distributions.ipynb) |
| [L-06](law-of-large-numbers.md) | The law of large numbers | 13 | [Practical 13](../practicals/notebooks/13-law-of-large-numbers-and-clt.ipynb) |
| [L-07](clt.md) | The Central Limit Theorem | 13 | [Practical 13](../practicals/notebooks/13-law-of-large-numbers-and-clt.ipynb) |
| [L-08](sampling-distributions.md) | Sampling distributions and standard error | 12 | [Practical 12](../practicals/notebooks/12-sampling-and-sampling-distributions.ipynb) |
| [L-09](confidence-intervals.md) | Confidence interval coverage | 14 | [Practical 14](../practicals/notebooks/14-estimation-and-confidence-intervals.ipynb) |
| [L-10](p-values.md) | Hypothesis tests and p-values | 15 | [Practical 15](../practicals/notebooks/15-hypothesis-testing.ipynb) |
| [L-11](correlation-regression.md) | Correlation and linear regression | 16 | [Practical 16](../practicals/notebooks/16-correlation-and-regression.ipynb) |
| [L-12](bayesian-updating.md) | Bayesian updating | 18 | [Practical 18](../practicals/notebooks/18-bayesian-and-data-science-methods.ipynb) |
| [L-13](power-and-errors.md) | Type I and Type II errors, and power | 15 | [Practical 15](../practicals/notebooks/15-hypothesis-testing.ipynb) |
| [L-14](anova.md) | ANOVA and comparison of multiple groups | 17 | [Practical 17](../practicals/notebooks/17-anova-chi-square-nonparametric.ipynb) |

## What every laboratory contains

Each page follows the same contract, so you always know where to look:

1. **Learning objectives** — what you should be able to do afterwards.
2. **Conceptual introduction** — the idea in one paragraph, before any symbols.
3. **Mathematical foundation** — the formulas, and the assumptions behind them.
4. **Experiment instructions** — exactly which controls to move and in what order.
5. **The interactive experiment** — controls, a live figure, a legend, and a results
   table of calculated values.
6. **Reading the results and interpretation** — what the numbers mean and which ones
   matter.
7. **Guided activities** — a sequence with specific settings to try.
8. **Independent challenges** — open problems with no prescribed path.
9. **Expected observations** — a table of default and extreme settings so you can check
   you are seeing what the model predicts.
10. **Self-assessment** — questions with worked answers behind a disclosure triangle.
11. **Connections** — links to the module, the notebook, the figures and the adjacent
    labs.

## How to use a laboratory

Labs are not illustrations to click through. Use them like a physical experiment:

1. **Read the mathematics on the page first.** The lab shows you what the formula
   does; it cannot tell you why the formula is right.
2. **Note the default state** and predict what will change before you change it.
3. **Move one control at a time.** Watch the numeric results as well as the picture.
4. **Answer the guided activities in writing.** Each one names the settings, so your
   answer can be checked against the expected observations table.
5. **Return to the module** and check whether your prediction was right. If it was not,
   that is the useful part.

Where a laboratory simulates, it says so. Repeated runs give different empirical
results — that is sampling variation, not a bug — and every lab states which quantities
are exact (theoretical probabilities, standard errors, p-values from the reference
distribution) and which are estimated from the run. Each simulation is seeded, so the
default state is reproducible on every visit and on every computer.

## Design guarantees

These are properties of every lab on this site, not aspirations:

- **No installation, no account, no key.** Each lab runs entirely in your browser.
- **No backend.** The site is static; nothing you do is sent anywhere.
- **Nothing is tracked.** No analytics, no cookies, no storage of your inputs.
- **Correct by construction.** Every formula is implemented once, in a shared,
  tested numerical core, and checked against SciPy values in an automated test suite.
- **Responsive.** Works from a phone at 320 px to a large monitor.
- **Keyboard operable.** Every control can be reached with Tab and adjusted with the
  arrow keys.
- **Accessible by description.** Each figure carries a text description, a results
  table restates the numbers, and the interpretation is written out in words.
- **Light and dark.** The palette is drawn from the site's own tokens, so both themes
  are native rather than inverted.
- **Print-safe.** Printing shows the instruction, the explanation and the fallback
  description; no interactive element is required to follow the mathematics.
- **Honest defaults.** Defaults are chosen to show something interesting immediately,
  and they are stated in the text.

## Current limitations

An honest list, because a laboratory that hides its assumptions teaches the wrong
habit:

- The power laboratory uses the exact formula for a z test with known \(\sigma\); for
  a t test it is a labelled approximation, good above \(n \approx 30\).
- Simulation-based results carry Monte Carlo error; each lab reports the relevant
  standard error or the number of replications so you can judge the noise.
- The labs run in JavaScript on your device, not on a server, so very large
  experiments (millions of replications) are deliberately capped to keep phones
  responsive.
- No laboratory attempts a multiple regression, a mixed model or a bootstrap; those are
  covered in the notebooks and case studies instead.

## The technology

The labs are plain JavaScript drawing SVG: no framework, no build step, and no
third-party chart library. The whole laboratory runtime — the numerical core, the
charting helpers and fourteen experiments — is under 100 KB of source, and it is
loaded only as static files. That choice is deliberate: a chart that needs three
megabytes of JavaScript to show two axes is a poor trade on a mobile connection, and
this course is meant to work on a student's phone.

The notebooks, which you run on your own computer, do use Plotly for figures where
zoom and hover genuinely help. There is no conflict: the labs illustrate, the notebooks
let you explore, and the mathematics is identical in both.
