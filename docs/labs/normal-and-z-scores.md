---
title: "Lab L-05: The normal distribution and z-scores"
description: Change μ and σ, place an observation on the curve, and read off its z-score, percentile and tail probability — then check the empirical rule against simulated draws.
---

# Lab L-05: The normal distribution and z-scores

**Lab L-05 · Module [10 · Continuous distributions](../modules/10-continuous-distributions/chapter.md) ·
paired with [Practical 10](../practicals/notebooks/10-continuous-distributions.ipynb) · no installation required**

---

## Learning objectives

By the end of this laboratory you should be able to:

1. compute a z-score and explain it in words as a distance in standard deviations;
2. convert between a raw value, a z-score and a percentile;
3. use the empirical rule 68 – 95 – 99.7 and say why it holds only for the normal;
4. explain why standardising makes different scales comparable;
5. keep population parameters (\(\mu,\sigma\)) distinct from a single observation \(x\).

## The idea in one paragraph

The normal family is a shape with two dials: \(\mu\) slides it and \(\sigma\) stretches
it. Standardising removes both dials at once: \(z = (x-\mu)/\sigma\) says how many
standard deviations an observation sits above the mean, and after that transformation
every normal variable has the same distribution. That is why one table (or one CDF)
serves every normal problem, and why marks on a test with mean 70 and SD 8 can be
compared with a different test with mean 500 and SD 100. This lab lets you move both
dials and the observation, and it checks the empirical rule against simulated data.

## The mathematics

If \(X \sim N(\mu,\sigma^{2})\) then

\[
Z = \frac{X-\mu}{\sigma} \sim N(0,1), \qquad
\Pr(X \le x) = \Pr\!\left(Z \le \frac{x-\mu}{\sigma}\right) = \Phi(z).
\]

The density is \(f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)}\) and the
empirical rule follows from the standard normal CDF:

\[
\Pr(|Z| \le 1) = 0.6827, \quad \Pr(|Z| \le 2) = 0.9545, \quad \Pr(|Z| \le 3) = 0.9973.
\]

Those numbers are properties of the *normal* distribution. They are not a general law:
a uniform or exponential variable gives different shares, and using 68 – 95 – 99.7 on
skewed data is a common and consequential error.

Standardisation is affine, so it preserves the shape and rescales distances. It does
**not** make data normal: standardising a skewed variable gives a skewed z-score.

## How to run the experiment

1. Start with \(\mu = 70\), \(\sigma = 8\), observation \(x = 82\).
2. Read the readout: \(z = (82-70)/8 = 1.5\), percentile 93.3 %, \(\Pr(X \le 82) = 0.933\).
3. Move \(\mu\) to 60 and watch \(z\) rise to 2.75 without touching \(x\).
4. Move \(\sigma\) to 4 and watch the curve narrow; \(z\) becomes 3.0.
5. Compare the empirical 68/95/99.7 percentages with the theoretical ones as you change
   the number of simulated draws.

<div class="psds-lab" data-lab="normal" data-seed="2026">
  <p class="psds-lab__instruction">
    The shaded area is \(\Pr(X \le x)\); the dashed line marks \(x\). Changing μ or σ
    changes the area, changing \(x\) moves the line.
  </p>
  <div class="psds-lab__grid">
    <div class="psds-lab__controls" data-role="controls">
      <noscript>
        <p><strong>This laboratory needs JavaScript.</strong> Default state:
        \(\mu = 70\), \(\sigma = 8\), \(x = 82\), so \(z = 1.5\), the percentile is
        93.3 %, and the empirical rule gives 68.3 / 95.4 / 99.7 %.</p>
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

Four numbers matter and they answer four different questions. \(z\) is a position in
standard deviations. The percentile is the share of the population below \(x\). The
tail probability \(\Pr(X > x)\) is one minus the percentile. The empirical percentages
are a check on the model, not a separate result — with 2,000 draws each of the three
shares carries a standard error of about one percentage point.

Notice that \(z\) can be negative and that it has no units. A z-score of \(-2\) is not
"below zero probability"; it is two standard deviations below the mean, with a
percentile near 2.3 %.

## Guided activities

1. **Compare two tests.** Test A: \(\mu = 70, \sigma = 8\), score 82. Test B:
   \(\mu = 500, \sigma = 100\), score 650. Set the lab to each in turn. Both give
   \(z = 1.5\); explain why that means the two performances are equivalent relative to
   their cohorts.
2. **Percentile reading.** Find the score that puts a student at the 90th percentile of
   a \(N(70, 8)\) distribution. (You need \(\Phi^{-1}(0.90) = 1.2816\); the answer is
   \(70 + 1.2816 \times 8 = 80.25\).)
3. **Sigma's effect.** Hold \(x\) and \(\mu\) fixed, and halve \(\sigma\). Predict the
   new \(z\), then check.
4. **Empirical rule.** Set the draws to 5,000 and record the three observed
   percentages. Compute the standard error of the 68 % figure and decide whether the
   simulation is consistent with the model.

## Independent challenges

1. **Two-sided probability.** Compute \(\Pr(|X - 70| \le 16)\) for \(N(70,8)\) without
   the lab, then verify it. Which empirical-rule row is this?
2. **Cut-offs.** A scholarship goes to the top 5 %. For \(N(70,64)\) (that is,
   \(\sigma = 8\)), find the cut-off score.
3. **Not normal.** A variable has mean 70 and SD 8 but is strongly right-skewed.
   Is \(\Pr(X \le 82)\) larger or smaller than 0.933? Argue from the shape of the
   distribution.
4. **Standardisation limits.** Explain why converting exam marks to z-scores within
   each class changes nothing about the *shape* of the marks.

## Expected observations

| Setting | \(z\) | Percentile | Notes |
|---|---|---|---|
| \(\mu=70,\sigma=8,x=82\) | 1.50 | 93.3 % | default; tail 6.7 % |
| \(\mu=60,\sigma=8,x=82\) | 2.75 | 99.7 % | same \(x\), different cohort |
| \(\mu=70,\sigma=4,x=82\) | 3.00 | 99.87 % | narrower spread, further out |
| \(\mu=70,\sigma=8,x=70\) | 0.00 | 50.0 % | the mean is the median |
| Empirical 68/95/99.7 at 5,000 draws | — | — | within about ±2 points of theory |

## Self-assessment

<details><summary>1. What does \(z = 1.5\) mean in words?</summary>

The observation sits 1.5 standard deviations above the mean of its own distribution.
It says nothing about the raw units, which is exactly why it is comparable across
scales.
</details>

<details><summary>2. Is a z-score of 2 unusual?</summary>

It happens to about 2.3 % of a normal population on the upper side, and 4.6 % if you
count both tails. Unusual in everyday language, but entirely expected in a sample of
a few hundred observations.
</details>

<details><summary>3. Why can't the empirical rule be applied to any distribution with a mean and SD?</summary>

Because the percentages depend on the shape. Chebyshev's inequality guarantees only
that at least \(1 - 1/k^2\) of the probability lies within \(k\) standard deviations —
75 % at \(k=2\), against 95 % for the normal. The extra precision is bought with the
normality assumption.
</details>

<details><summary>4. What is the difference between \(\sigma\) and \(s\)?</summary>

\(\sigma\) is the population standard deviation, a parameter. \(s\) is the sample
standard deviation, a statistic computed from data, which varies from sample to
sample. The lab's slider sets \(\sigma\); a real study only ever sees \(s\).
</details>

## Where this connects

- [Module 10](../modules/10-continuous-distributions/chapter.md) covers the normal
  family, standardisation and the empirical rule.
- [Practical 10](../practicals/notebooks/10-continuous-distributions.ipynb) uses
  `scipy.stats.norm` for CDFs, quantiles and random draws.
- The standardisation figure is [Figure 9.1 in Module 10](../modules/10-continuous-distributions/chapter.md).
- The sampling version of this idea — the distribution of a mean — is
  [Lab L-08](sampling-distributions.md).

## Next

- [Lab L-06 — The law of large numbers](law-of-large-numbers.md)
- Back to the [laboratory index](index.md)
