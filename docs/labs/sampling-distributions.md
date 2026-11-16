---
title: "Lab L-08: Sampling distributions and standard error"
description: Take repeated samples of size n, and watch the distribution of the sample mean narrow as 1/√n around the population mean.
---

# Lab L-08: Sampling distributions and standard error

**Lab L-08 · Module [12 · Sampling and sampling distributions](../modules/12-sampling-and-sampling-distributions/chapter.md) ·
paired with [Practical 12](../practicals/notebooks/12-sampling-and-sampling-distributions.ipynb) · no installation required**

---

## Learning objectives

By the end of this laboratory you should be able to:

1. distinguish the distribution of the data from the distribution of a statistic;
2. state and use \(\se(\bar X) = \sigma/\sqrt{n}\);
3. explain why the standard error is a property of the sampling design, not of the
   sample;
4. predict how the spread of the sampling distribution changes when \(n\) is
   quadrupled;
5. explain why "±1.96 SE" covers about 95 % of samples when the sampling distribution
   is normal.

## The idea in one paragraph

Every sample gives one number, and a different sample would have given a different
number. The distribution of all those possible numbers is the **sampling
distribution** of the statistic, and its spread is the standard error. This lab draws
\(B\) independent samples of size \(n\) from a normal population and histograms the
\(B\) sample means. The histogram is narrow — much narrower than the population — and
it narrows further as \(n\) grows. The key conceptual move is that the histogram is
*not* the data. It is the behaviour of an estimator, and that is what a confidence
interval or a p-value is ultimately built from.

## The mathematics

Let \(X_1,\dots,X_n\) be independent with mean \(\mu\) and variance \(\sigma^2\), and
let \(\bar X = \frac1n \sum X_i\). Then, exactly and without any normality assumption,

\[
\E[\bar X] = \mu, \qquad \Var(\bar X) = \frac{\sigma^2}{n}, \qquad
\se(\bar X) = \frac{\sigma}{\sqrt{n}} .
\]

If the population is normal, the sampling distribution is normal for every \(n\), so

\[
\bar X \sim N\!\left(\mu, \frac{\sigma^2}{n}\right),
\qquad
\Pr\left(|\bar X - \mu| \le 1.96\,\frac{\sigma}{\sqrt{n}}\right) = 0.95 .
\]

If the population is not normal, the same mean and variance hold, and the shape becomes
approximately normal as \(n\) grows — the Central Limit Theorem, which is
[Lab L-07](clt.md). What this lab isolates is the *scaling*: the spread depends on
\(n\) and on \(\sigma\), and on nothing else.

Note the two different standard deviations in play. \(\sigma\) describes individual
observations; \(\sigma/\sqrt{n}\) describes the estimator. At \(n = 10\) and
\(\sigma = 15\) the second is 4.74, about a third of the first — that is the reward for
averaging.

## How to run the experiment

1. Start with \(\mu = 100\), \(\sigma = 15\), \(n = 10\), \(B = 1000\).
2. Read the readout: the mean of the means should be near 100, and the SD of the means
   near \(\sigma/\sqrt{n} = 4.74\).
3. Raise \(n\) to 40 (four times larger). The spread should roughly halve.
4. Raise \(n\) to 100. Compare with the first setting: the histogram is less than a
   third as wide.
5. Increase \(B\) and notice that the histogram gets smoother but does not get
   narrower. \(B\) is about the precision of the picture, not about the precision of
   the estimate.

<div class="psds-lab" data-lab="sampling" data-seed="2026">
  <p class="psds-lab__instruction">
    The histogram is the distribution of the sample mean over B repeated samples; the
    red band is ±σ/√n around μ.
  </p>
  <div class="psds-lab__grid">
    <div class="psds-lab__controls" data-role="controls">
      <noscript>
        <p><strong>This laboratory needs JavaScript.</strong> Default state:
        \(\mu = 100\), \(\sigma = 15\), \(n = 10\), \(B = 1000\). The standard error is
        \(15/\sqrt{10} = 4.74\), so the histogram of means is about a third as wide as
        the population.</p>
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

The ratio *observed SD of the means / theoretical standard error* is the number to
watch. It should sit near 1.00, with Monte Carlo noise of roughly
\(1/\sqrt{2B}\) — about 2 % at \(B = 1000\). A ratio near 1 is evidence that the
simulation and the formula agree; the formula is exact under the model, so a large
deviation means something is wrong with the experiment, not with the theory.

The share within ±1.96 SE should be near 95 %. This is a property of the *procedure*:
if you built an interval \(\bar X \pm 1.96\,\sigma/\sqrt{n}\) from each sample, about
95 % of those intervals would contain \(\mu\). That is exactly the machinery behind
[Lab L-09](confidence-intervals.md).

## Guided activities

1. **Square root law.** Fill in the observed SD of the means for \(n = 4, 16, 64\).
   Is the pattern \(1/\sqrt{n}\)? Compute the ratio of consecutive values.
2. **Cost of precision.** You want the standard error to fall from 4.74 to 1.5. What
   \(n\) is needed? Then halve it again — how much more data does that cost?
3. **σ's role.** Double \(\sigma\) from 15 to 30. Predict the new standard error before
   reading it.
4. **B is not n.** Set \(n = 10\) and \(B = 3000\). Compare the width with the \(B=200\)
   case. Then set \(n = 40\) and \(B = 200\) and compare again. Which control changed
   the spread?

## Independent challenges

1. **Sketch before running.** For \(\mu = 100, \sigma = 15\), sketch the sampling
   distribution at \(n = 4\) and \(n = 100\) on the same axis. Mark \(\pm 2\) SE.
2. **A non-normal population.** The lab draws from a normal population, so the shape is
   normal at every \(n\). Explain what would change — and what would not — if the
   population were exponential. (You can test your answer in [Lab L-07](clt.md).)
3. **Standard error of a proportion.** For a proportion with \(p = 0.2\) and
   \(n = 200\), the standard error is \(\sqrt{p(1-p)/n} = 0.028\). Verify by simulating
   200 Bernoulli trials many times (in the notebook) and comparing.
4. **The wrong standard error.** A report says "the standard deviation is 15, so the
   mean is uncertain by 15". What is wrong with that sentence, and what is the correct
   uncertainty at \(n = 25\)?

## Expected observations

| \(n\) | \(\se = \sigma/\sqrt n\) | Observed SD of the means | Share within ±1.96 SE |
|---|---|---|---|
| 10 | 4.74 | ≈ 4.7 | ≈ 95 % |
| 40 | 2.37 | ≈ 2.4 | ≈ 95 % |
| 100 | 1.50 | ≈ 1.5 | ≈ 95 % |
| any \(n\), \(B\) raised | unchanged | unchanged | unchanged |
| any \(n\), \(\sigma\) doubled | doubled | doubled | ≈ 95 % |

## Self-assessment

<details><summary>1. What is the difference between the standard deviation and the standard error?</summary>

The standard deviation describes the spread of individual observations. The standard
error describes the spread of an estimator across repeated samples. At \(n = 10\) with
\(\sigma = 15\), they are 15 and 4.74 — the same data, two different objects.
</details>

<details><summary>2. Why does increasing B not narrow the histogram?</summary>

Because \(B\) is the number of simulated samples: more samples give a smoother estimate
of the sampling distribution but do not change its width. Only \(n\) (and \(\sigma\))
change the width. This is the same distinction as "more simulations versus more data".
</details>

<details><summary>3. Is the sampling distribution of the mean always normal?</summary>

No. It is normal for every \(n\) only when the population is normal. Otherwise it is
approximately normal for large \(n\), and its exact shape depends on the population.
Mean and variance, however, are always \(\mu\) and \(\sigma^2/n\).
</details>

<details><summary>4. Why is the standard error smaller than σ?</summary>

Averaging cancels independent errors: positive and negative deviations from \(\mu\)
partly offset. The variance of a sum of \(n\) independent terms is \(n\sigma^2\), so
the variance of the average is \(\sigma^2/n\) and the standard deviation is
\(\sigma/\sqrt n\).
</details>

## Where this connects

- [Module 12](../modules/12-sampling-and-sampling-distributions/chapter.md) defines
  sampling distributions, standard error and the finite-population correction.
- [Practical 12](../practicals/notebooks/12-sampling-and-sampling-distributions.ipynb)
  simulates these distributions and verifies the standard error for several statistics.
- [Figure 6.1 in Module 12](../modules/12-sampling-and-sampling-distributions/chapter.md)
  shows the population and the sampling distribution to the same scale.
- Confidence intervals built from this standard error are
  [Lab L-09](confidence-intervals.md).

## Next

- [Lab L-09 — Confidence interval coverage](confidence-intervals.md)
- Back to the [laboratory index](index.md)
