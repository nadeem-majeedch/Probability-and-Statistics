---
title: "Lab L-01: Random events and long-run frequency"
description: Run an experiment with n trials and k outcomes, and watch relative frequency settle onto probability — with the sampling error visible.
---

# Lab L-01: Random events and long-run frequency

**Lab L-01 · Module [06 · Probability fundamentals](../modules/06-probability-fundamentals/chapter.md) ·
paired with [Practical 06](../practicals/notebooks/06-probability-fundamentals.ipynb) · no installation required**

---

## Learning objectives

By the end of this laboratory you should be able to:

1. explain why a probability is a property of a *model* and a relative frequency is
   a property of a *run of data*;
2. use the addition rule for disjoint events to compute the probability of "A or B";
3. state the standard error of an estimated probability, \(\sqrt{p(1-p)/n}\), and use
   it to judge whether an observed frequency is consistent with the model;
4. describe what happens to the running average as \(n\) grows, and why it still
   wobbles;
5. explain why a large \(k\) (many outcomes) makes each individual probability
   smaller without changing the total.

## The idea in one paragraph

Toss a biased coin a thousand times and about half the tosses come up heads — but not
exactly half, and the gap shrinks as you keep tossing. That is the whole of the
frequency interpretation of probability: the long-run proportion converges to the
model's probability, while any finite run carries sampling error. This lab makes the
two objects separate and visible. You set the model (\(p\) and the number of outcomes
\(k\)), you choose how much data to generate (\(n\)), and the figure shows the
observed proportions as bars against the theoretical probabilities as ticks.

## The mathematics

Let \(A\) be the event "outcome 1" with model probability \(p\), and let the remaining
\(k-1\) outcomes be equally likely, so each has probability \((1-p)/(k-1)\). The
events are disjoint and exhaustive, so

\[
\sum_{i=1}^{k} \Pr(O_i) = p + (k-1)\cdot\frac{1-p}{k-1} = 1 .
\]

For \(B=\{\text{outcome 1 or outcome 2}\}\), disjointness gives the addition rule

\[
\Pr(B) = \Pr(O_1) + \Pr(O_2) = p + \frac{1-p}{k-1},
\]

and the complement rule gives \(\Pr(A^{c}) = 1-p\).

If \(X\) is the number of times \(A\) occurs in \(n\) independent trials, then
\(X \sim \mathrm{Binomial}(n,p)\), so the estimator \(\hat p = X/n\) has

\[
\E[\hat p] = p, \qquad \se(\hat p) = \sqrt{\frac{p(1-p)}{n}} .
\]

That is the exact standard deviation of the estimator — not an approximation. The two
standard-error band used in the interpretation is \(\hat p \pm 2\sqrt{p(1-p)/n}\),
which for a normal-approximation argument covers about 95 % of runs. With \(p=0.5\)
and \(n=1000\) the band is \(\pm 0.032\), and the readout should almost always land
inside it.

## How to run the experiment

1. Leave the defaults: \(n = 1000\) trials, \(p = 0.50\), \(k = 3\) outcomes.
2. Read the bar chart: bars are observed relative frequencies, red ticks are the
   model probabilities. The lower chart traces the running estimate of \(p\).
3. Press **New run** five times without changing anything. Write down the five values
   of observed \(P(A)\).
4. Now raise \(n\) to 5000 and press **New run**. Compare the spread of the five old
   values with this new one.
5. Change \(k\) to 5 and watch the bars shrink; the total is still 1.

<div class="psds-lab" data-lab="probability" data-seed="2026">
  <p class="psds-lab__instruction">
    Bars are observed frequencies, red ticks are the theoretical probabilities. Press
    <strong>New run</strong> repeatedly: the bars move, the ticks never do.
  </p>
  <div class="psds-lab__grid">
    <div class="psds-lab__controls" data-role="controls">
      <noscript>
        <p><strong>This laboratory needs JavaScript.</strong> At the defaults — 1,000
        trials, \(p = 0.50\), three outcomes — the model is 0.50, 0.25, 0.25, and a
        real run typically gives frequencies within about ±0.03 of those values. The
        mathematics is written out above.</p>
      </noscript>
    </div>
    <div class="psds-lab__figure">
      <div data-role="chart"></div>
      <div data-role="legend"></div>
      <div data-role="results"></div>
    </div>
  </div>
  <p class="psds-lab__readout" data-role="readout" aria-live="polite"></p>
  <p class="psds-lab__hint" data-role="hint"></p>
</div>

## Reading the results

The readout gives four numbers that matter: the observed \(P(A)\), the observed
\(P(A \text{ or } B)\), the theoretical values, and the standard error. Judge the
experiment by the **last** one — the gap between observed and theoretical is only
interesting relative to the standard error, never on its own. A gap of 0.02 with
\(\se = 0.016\) is ordinary; a gap of 0.02 with \(\se = 0.001\) would be a bug.

The lower chart is the same information as a process rather than a snapshot. Early
on, the running estimate swings widely; later it calms down, but it never freezes.
The calm is \(1/\sqrt{n}\): to halve the width of the wobble you need four times the
trials.

## Guided activities

1. **The standard error in action.** Set \(n = 100\), press New run ten times and
   record the ten observed values of \(P(A)\). Compute their spread. Compare with
   \(\sqrt{0.25/100} = 0.05\).
2. **Quadruple the sample.** Set \(n = 400\) and repeat. Is the spread roughly half?
   Is it exactly half?
3. **Addition rule check.** With \(k = 4\), compute \(\Pr(A \text{ or } B)\) by hand
   and compare with the readout. Then set \(p = 0.9\) and repeat — the second term is
   now very small, which is why "A or B" barely exceeds \(p\).
4. **Complement.** Confirm that the observed \(P(\text{not } A)\) equals
   \(1 - P(A)\) to the last decimal shown. If it did not, the simulation would be
   broken.

## Independent challenges

1. **Design the run.** You want the estimate of a probability near 0.5 to be within
   0.01 of the truth in 95 % of runs. What \(n\) do you need? Check your answer by
   running the lab at that \(n\) several times.
2. **Rare events.** Set \(p = 0.05\) and \(n = 100\). What does the normal-approximation
   band do here, and why is \(\sqrt{p(1-p)/n}\) still the right standard error? What
   changes about the *shape* of the sampling distribution?
3. **Many outcomes.** With \(k = 5\), each non-A outcome has probability
   \((1-p)/4 = 0.125\). Predict both the bar heights and the observed counts at
   \(n = 1000\), then check.
4. **A prediction before the run.** Before pressing New run, write down a range in
   which you expect observed \(P(A)\) to fall. Be honest about how often you would be
   right.

## Expected observations

| Setting | What you should see |
|---|---|
| \(n=1000, p=0.5, k=3\) | frequencies near 0.500 / 0.250 / 0.250, typically within ±0.03 |
| \(n=5000, p=0.5, k=3\) | the same targets, visibly tighter (about ±0.014 at 2 SE) |
| \(n=1000, k=5, p=0.5\) | one bar near 0.5 and four near 0.125 |
| \(p=0.9, k=3\) | bars near 0.90 / 0.05 / 0.05; "A or B" barely above 0.90 |
| Repeated New runs, fixed settings | different bars every time, identical ticks |

## Self-assessment

<details><summary>1. A run gives observed \(P(A)=0.47\) when the model says 0.50. Is the model wrong?</summary>

Not necessarily. At \(n=1000\) the standard error is \(\sqrt{0.25/1000}=0.0158\), so
0.47 is about 1.9 standard errors below the model — unusual but inside the ordinary
range. You need the standard error before you can call a gap surprising.
</details>

<details><summary>2. Why does the bar chart not simply show probabilities?</summary>

Because the chart's job is to compare two different objects: a property of the model
(ticks) and a property of the data (bars). Showing only the model would hide the
sampling error, which is the thing being taught.
</details>

<details><summary>3. What exactly converges as \(n \to \infty\)?</summary>

The relative frequency \(X/n\) converges to \(p\) in probability (the weak law of
large numbers). The *number* of successes \(X\) does not converge; it grows like
\(np\). Convergence is of the proportion, not of the count.
</details>

<details><summary>4. Does changing \(k\) change \(P(A)\)?</summary>

No — \(p\) is set independently. Changing \(k\) redistributes the remaining
\(1-p\) across the other outcomes, which is why the non-A bars get shorter as \(k\)
grows.
</details>

## Where this connects

- The axioms, sample spaces and the algebra of events are in
  [Module 06](../modules/06-probability-fundamentals/chapter.md).
- The same experiment in Python, with exact binomial checks and a convergence plot, is
  [Practical 06](../practicals/notebooks/06-probability-fundamentals.ipynb).
- The formal limit is the law of large numbers — see
  [Lab L-06](law-of-large-numbers.md) and
  [Module 13](../modules/13-law-of-large-numbers-and-clt/chapter.md).

## Next

- [Lab L-02 — Conditional probability and Bayes' theorem](conditional-probability.md)
- Back to the [laboratory index](index.md)
