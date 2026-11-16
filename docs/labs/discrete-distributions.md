---
title: "Lab L-03: Discrete probability distributions"
description: Switch between binomial, Poisson and geometric models, move the parameters, and compare the exact mass function with simulated frequencies.
---

# Lab L-03: Discrete probability distributions

**Lab L-03 · Module [09 · Discrete distributions](../modules/09-discrete-distributions/chapter.md) ·
paired with [Practical 09](../practicals/notebooks/09-discrete-distributions.ipynb) · no installation required**

---

## Learning objectives

By the end of this laboratory you should be able to:

1. read a probability mass function and state what its heights mean;
2. compute \(\E[X]\) and \(\Var(X)\) for the binomial, Poisson and geometric families;
3. explain why the Poisson is the "count of rare events" model and why its mean equals
   its variance;
4. use a cumulative probability \(\Pr(X \le k)\) and interpret it correctly;
5. compare a model with data by looking at whether the simulated frequencies agree
   within sampling error.

## The idea in one paragraph

A discrete random variable takes separated values, so its distribution is a set of
heights that must add to one — a probability mass function. This lab draws the exact
mass function as bars for whichever family you choose, overlays the frequencies from a
simulated sample, and shades the region \(\Pr(X \le k)\). The comparison between bars
and dots is the whole method: a model is credible when data look like draws from it,
and the size of an acceptable discrepancy is set by sampling error, not by taste.

## The mathematics

**Binomial.** \(X\) counts successes in \(n\) independent trials with success
probability \(p\):

\[
\Pr(X = k) = \binom{n}{k} p^{k}(1-p)^{n-k}, \qquad \E[X] = np, \qquad \Var(X) = np(1-p).
\]

**Poisson.** \(X\) counts events in a fixed interval when they occur independently at
rate \(\lambda\):

\[
\Pr(X = k) = \frac{\lambda^{k} e^{-\lambda}}{k!}, \qquad \E[X] = \Var(X) = \lambda.
\]

The equality of mean and variance is a testable signature; real count data with
variance far above the mean are *overdispersed* and need a different model.

**Geometric.** \(X\) counts trials up to and including the first success:

\[
\Pr(X = k) = (1-p)^{k-1}p, \quad k = 1, 2, \dots, \qquad
\E[X] = \frac{1}{p}, \qquad \Var(X) = \frac{1-p}{p^{2}}.
\]

The cumulative probability is a **sum**, \(\Pr(X \le k) = \sum_{j \le k} \Pr(X = j)\),
not an integral. This is the discrete counterpart of the area under a density, and
mixing the two is the most common error in this part of the course.

The simulated frequencies are multinomial with the same probabilities, so each
observed proportion has standard error \(\sqrt{p_k(1-p_k)/m}\) for \(m\) simulated
draws. Deviations larger than about twice that are worth a second look; smaller ones
are noise.

## How to run the experiment

1. Start with the binomial at \(n = 10\), \(p = 0.30\), threshold \(k = 3\).
2. Check the readout against the formulas: \(\E[X] = 3.0\), \(\Var(X) = 2.1\),
   \(\Pr(X \le 3) = 0.650\).
3. Switch to Poisson with \(\lambda = 4\): the mean and the variance both read 4.
4. Switch to geometric with \(p = 0.30\): the mean is 3.33 and the mass function has
   its maximum at \(k = 1\).
5. Drag \(k\) and watch the shaded region and the cumulative probability move together.

<div class="psds-lab" data-lab="discrete" data-seed="2026">
  <p class="psds-lab__instruction">
    Bars are the exact mass function; dots are relative frequencies from the simulated
    sample; the shaded bars are \(\Pr(X \le k)\).
  </p>
  <div class="psds-lab__grid">
    <div class="psds-lab__controls" data-role="controls">
      <noscript>
        <p><strong>This laboratory needs JavaScript.</strong> Default state: binomial
        with \(n=10\), \(p=0.30\). The mass function peaks at \(k=3\) with
        \(\Pr(X=3)=0.267\), the mean is 3.0, the variance 2.1, and
        \(\Pr(X \le 3)=0.650\).</p>
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

Compare the two columns of numbers in the results panel: theory and simulation. The
means should agree to about two decimal places with 2,000 draws; the variances are
noisier, because a variance uses squared deviations and is more sensitive to the tail.
If the simulated mean is far from the theoretical mean, check that you have not left
the simulation size at its minimum.

The shaded bars are a reminder that "less than or equal to" includes the bar at \(k\).
For a discrete variable \(\Pr(X < k) \ne \Pr(X \le k)\) — they differ by exactly
\(\Pr(X=k)\), a point that costs marks every year.

## Guided activities

1. **Variance of the binomial.** Hold \(p = 0.3\) and increase \(n\) from 5 to 40.
   Predict how the peak height and the spread change, then check. Which one moves
   faster?
2. **p = 0.5.** Set the binomial to \(p = 0.5\). The distribution is symmetric; find
   the two \(k\) values with equal mass and verify with the readout.
3. **Poisson as a limit.** Set the binomial to \(n = 40\), \(p = 0.075\) (so
   \(np = 3\)) and compare its shape with a Poisson at \(\lambda = 3\). How close are
   the two mass functions at \(k = 0\)?
4. **Geometric tail.** With \(p = 0.3\), compute \(\Pr(X > 5) = (1-p)^{5}\) by hand and
   confirm with \(\Pr(X \le 5)\).

## Independent challenges

1. **Overdispersion.** Simulated Poisson counts have variance ≈ mean. Describe a
   real dataset (complaints per day, accidents per site) where you would expect
   variance ≫ mean, and say what that implies for a Poisson model.
2. **Threshold choice.** For binomial \(n = 20\), \(p = 0.2\), find the smallest \(k\)
   with \(\Pr(X \le k) \ge 0.95\). This is the logic of acceptance sampling.
3. **Design.** You need \(\Pr(X \ge 1) \ge 0.99\) with \(p = 0.02\) per trial. How
   many independent trials must you run? Use the complement rule.
4. **Which family?** A dataset counts the number of goals per match. Argue for or
   against a Poisson model using the mean–variance relationship.

## Expected observations

| Setting | Mean | Variance | Notable |
|---|---|---|---|
| Binomial \(n=10, p=0.3\) | 3.0 | 2.1 | peak at \(k=3\), \(\Pr(X=3)=0.267\) |
| Binomial \(n=10, p=0.5\) | 5.0 | 2.5 | symmetric about 5 |
| Poisson \(\lambda=4\) | 4.0 | 4.0 | mean = variance, right skew |
| Geometric \(p=0.3\) | 3.33 | 7.78 | maximum at \(k=1\), long tail |
| Simulation, 2,000 draws | ±0.05 of theory | ±0.2 of theory | dots track bar heights |

## Self-assessment

<details><summary>1. Why must the bars sum to 1 while a density can have heights above 1?</summary>

Because the bars *are* probabilities of separated outcomes and the outcomes are
exhaustive, so the total is exactly one. A density assigns probability per unit of
length, so its height is only meaningful after integrating; there is no constraint
that \(f(x) \le 1\).
</details>

<details><summary>2. What does \(\Pr(X \le 3) = 0.650\) mean, precisely?</summary>

That the model puts 65 % of its probability on the values 0, 1, 2 and 3 together. In
repeated samples, about 65 % of them would have three or fewer successes.
</details>

<details><summary>3. Why is the Poisson variance equal to its mean?</summary>

Because the Poisson arises as a limit of the binomial with \(n \to \infty\),
\(p \to 0\), \(np \to \lambda\); then \(np(1-p) \to \lambda\). Mean and variance are
equal by construction, not by coincidence.
</details>

<details><summary>4. The geometric mean is 3.33 but the most likely value is 1. Is that a contradiction?</summary>

No. The distribution is heavily right-skewed: small values are most likely
individually, but the long tail pulls the mean up. The median is 3, not 1.
</details>

## Where this connects

- Derivation, moments and the Poisson limit are in
  [Module 09](../modules/09-discrete-distributions/chapter.md).
- [Practical 09](../practicals/notebooks/09-discrete-distributions.ipynb) fits these
  models to data in Python and checks them with SciPy.
- The figure [Figure 5.1 in Module 09](../modules/09-discrete-distributions/chapter.md)
  shows binomial shapes in three panels.
- Continuous counterparts are in [Lab L-04](continuous-distributions.md).

## Next

- [Lab L-04 — Continuous probability distributions](continuous-distributions.md)
- Back to the [laboratory index](index.md)
