---
title: "Lab L-12: Bayesian updating"
description: Start from a Beta prior, add data batch by batch, and watch the posterior move — and narrow — as the evidence accumulates.
---

# Lab L-12: Bayesian updating

**Lab L-12 · Module [18 · Bayesian and data-science methods](../modules/18-bayesian-and-data-science-methods/chapter.md) ·
paired with [Practical 18](../practicals/notebooks/18-bayesian-and-data-science-methods.ipynb) · no installation required**

---

## Learning objectives

By the end of this laboratory you should be able to:

1. express a prior belief about a proportion as a Beta distribution and read its mean
   and strength;
2. derive the Beta posterior from a binomial likelihood;
3. explain how the prior and the data are weighted, and what changes that weighting;
4. interpret a 95 % credible interval, and contrast it with a confidence interval;
5. describe how the posterior narrows as evidence accumulates, and how robust it is to
   a wrong prior.

## The idea in one paragraph

Bayesian updating is arithmetic for changing your mind. You start with a distribution
over the unknown rate — the prior — and each batch of data multiplies it by the
likelihood, producing a posterior. With a Beta prior the arithmetic is exact and the
result is another Beta, which is why this is the standard teaching example: the
posterior mean is a weighted average of the prior mean and the observed proportion,
with weights proportional to how many pseudo-observations the prior is worth and how
many real observations you have. Press "Observe another batch" and watch the curve
slide towards the truth and narrow as it goes.

## The mathematics

Model the data as \(k\) successes in \(n\) independent trials, \(K \sim
\mathrm{Binomial}(n,\theta)\), and put a Beta prior on the rate:

\[
\theta \sim \mathrm{Beta}(a_0,b_0), \qquad
f(\theta) = \frac{\theta^{a_0-1}(1-\theta)^{b_0-1}}{B(a_0,b_0)} .
\]

Because the Beta is conjugate to the binomial, the posterior is

\[
\theta \mid (k,n) \sim \mathrm{Beta}(a_0+k,\; b_0+n-k),
\]

with posterior mean and variance

\[
\E[\theta \mid k,n] = \frac{a_0+k}{a_0+b_0+n},
\qquad
\Var(\theta \mid k,n) = \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)},
\]

where \(\alpha = a_0+k\) and \(\beta = b_0+n-k\). The prior contributes
\(a_0+b_0\) pseudo-observations; the data contribute \(n\). So the posterior mean is a
weighted average with weights in that ratio. A \(95\,\%\) **credible interval** is the
central interval containing 95 % of the posterior probability — a direct statement
about \(\theta\), unlike a confidence interval, which is a statement about the
procedure.

The posterior predictive probability of a success in the next observation is the
posterior mean, \(\Pr(\text{success} \mid \text{data}) = \alpha/(\alpha+\beta)\).

## How to run the experiment

1. Leave the prior at mean 0.30 with strength 4 (so \(a_0 = 1.2\), \(b_0 = 2.8\)) and
   the true rate at 0.35.
2. Press **Observe another batch** once: the posterior jumps towards the data, because
   four pseudo-observations cannot resist forty real ones.
3. Press it four more times and watch the curve narrow around the true rate.
4. Now reset, set the prior strength to 40 and repeat. The prior resists longer.
5. Finally, set the true rate far from the prior (say prior mean 0.2, truth 0.7) with
   strength 40 and observe several batches: does the data win in the end?

<div class="psds-lab" data-lab="bayes" data-seed="2026">
  <p class="psds-lab__instruction">
    Teal is the prior, red is the posterior, the shaded region is the 95 % credible
    interval, and the dashed vertical line is the observed proportion so far.
  </p>
  <div class="psds-lab__grid">
    <div class="psds-lab__controls" data-role="controls">
      <noscript>
        <p><strong>This laboratory needs JavaScript.</strong> Default state: prior
        Beta(1.2, 2.8), true rate 0.35, batches of 40. After one batch of about 14
        successes the posterior is roughly Beta(15.2, 28.8) with mean 0.345 and a 95 %
        credible interval of about ±0.14.</p>
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

The results panel gives the two distributions side by side: the prior with its strength
and mean, and the posterior with its mean, SD and credible interval. The width of the
interval is the honest summary of what you know — it shrinks like \(1/\sqrt{n}\), the
same rate as a standard error, because it is answering the same question from the other
direction.

Watch the posterior mean, not just the interval. With a weak prior it lands close to
the observed proportion \(\hat\theta = k/n\). With a strong prior it lands between the
prior mean and \(\hat\theta\), and the weights are exactly
\((\text{prior strength}) : n\). This is the arithmetic of "the prior counts as
pseudo-data", and it is the most useful sentence in the Bayesian toolkit.

## Guided activities

1. **Weighting.** Prior mean 0.3, strength 4, then 40. With a batch of 40, compute the
   posterior mean by hand using the weighted-average formula and check it.
2. **Evidence accumulates.** Observe five batches and record the interval width after
   each. Is the sequence close to \(1/\sqrt{n}\)?
3. **Prior sensitivity.** Use two batches of data (80 observations) with prior mean
   0.2 and 0.8, both at strength 4. How different are the posteriors? Then repeat at
   strength 40.
4. **Credible versus confidence.** Write one sentence for each interval type, in the
   form "there is a 95 % probability that …", and note which sentence is legitimate for
   which interval.

## Independent challenges

1. **A stubborn prior.** Find a prior strength at which the posterior mean after 40
   observations still lies outside 0.05 of the data proportion. Is that prior
   defensible in a real application?
2. **Sequential versus batch.** Show that updating with two batches of 20 gives the
   same posterior as one batch of 40. This is the coherence property of Bayesian
   updating.
3. **Decision rule.** With a posterior for a conversion rate, write down a rule for
   launching a feature when \(\Pr(\theta > 0.30 \mid \text{data}) > 0.95\). How would
   you compute that probability from the Beta posterior?
4. **Diagnostic testing.** The prevalence/sensitivity version of Bayes' theorem —
   where the prior is a prevalence and the likelihood is a test result — is
   [Lab L-02](conditional-probability.md). Explain how this lab's continuous version
   reduces to it.

## Expected observations

| Setting | Posterior mean | 95 % credible interval |
|---|---|---|
| prior only, no data | 0.300 | wide, roughly 0.10 – 0.55 |
| one batch, 40 observations, truth 0.35 | ≈ 0.345 | ≈ ± 0.14 |
| five batches, 200 observations | ≈ 0.35 | ≈ ± 0.06 |
| prior strength 40, one batch | ≈ 0.31 | between prior and data |
| prior mean 0.2, truth 0.7, strength 4, 5 batches | ≈ 0.70 | narrow, prior forgotten |

## Self-assessment

<details><summary>1. What does "the prior counts as pseudo-observations" mean?</summary>

That a Beta(\(a_0,b_0\)) prior behaves, in the posterior mean, exactly like
\(a_0+b_0\) extra observations with the prior's mean. With four pseudo-observations
against forty real ones, the data dominate 10 to 1.
</details>

<details><summary>2. Why is the Beta a conjugate prior for the binomial?</summary>

Because multiplying the Beta density by the binomial likelihood gives another Beta
density — the exponents simply add. Conjugacy is algebraic convenience, not a
requirement for Bayesian inference, though it makes the updating exact and transparent.
</details>

<details><summary>3. Is a 95 % credible interval the same as a 95 % confidence interval?</summary>

Numerically they often look similar with weak priors and large samples, but they mean
different things. The credible interval says the parameter lies in this range with
95 % posterior probability, given the model and prior. The confidence interval says
that 95 % of intervals built this way would contain the parameter — a statement about
the procedure, not about this interval.
</details>

<details><summary>4. What happens as the data grow without limit?</summary>

The likelihood term dominates, the posterior concentrates around the true rate, and
the prior is asymptotically irrelevant, provided it does not assign zero probability to
the truth. That is dovetailing: Bayesian and frequentist answers agree in large samples.
</details>

## Where this connects

- [Module 18](../modules/18-bayesian-and-data-science-methods/chapter.md) covers
  priors, likelihoods, conjugacy, credible intervals and Bayes factors.
- [Practical 18](../practicals/notebooks/18-bayesian-and-data-science-methods.ipynb)
  fits Beta–Binomial and normal models and computes posteriors numerically.
- [Figure 12.1 in Module 18](../modules/18-bayesian-and-data-science-methods/chapter.md)
  draws a prior, likelihood and posterior together.
- The discrete two-hypothesis case is [Lab L-02](conditional-probability.md).

## Next

- [Lab L-13 — Type I and Type II errors, and power](power-and-errors.md)
- Back to the [laboratory index](index.md)
