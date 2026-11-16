---
title: "Lab L-06: The law of large numbers"
description: Watch a running average settle onto the population mean — and watch a Cauchy sample refuse to settle at all.
---

# Lab L-06: The law of large numbers

**Lab L-06 · Module [13 · The law of large numbers and the CLT](../modules/13-law-of-large-numbers-and-clt/chapter.md) ·
paired with [Practical 13](../practicals/notebooks/13-law-of-large-numbers-and-clt.ipynb) · no installation required**

---

## Learning objectives

By the end of this laboratory you should be able to:

1. state the weak law of large numbers and say what "in probability" adds to "usually";
2. explain why the running average settles but never locks onto \(\mu\);
3. compute the standard error of a mean and use it to judge how close the average
   should be at a given \(n\);
4. give an example of a distribution with no mean, and explain why the law fails there;
5. distinguish convergence of the average from convergence of the number of successes.

## The idea in one paragraph

The average of many independent observations from a population with mean \(\mu\) gets
close to \(\mu\), and stays close: that is the law of large numbers. It is the
justification for every "the sample mean estimates the population mean" sentence in
the course. But it is a statement about a limit, not a promise about your data. This
lab draws a path of running averages. It wobbles early, calms down, and never stops
wobbling entirely — the residual wobble has a size, \(\sigma/\sqrt{n}\), and you can
watch it shrink. Switch to the Cauchy population and the path never calms down at all,
because that population has no mean to converge to.

## The mathematics

Let \(X_1,\dots,X_n\) be independent with \(\E[X_i] = \mu\) and
\(\Var(X_i) = \sigma^2 < \infty\), and let \(\bar X_n = \frac1n\sum X_i\). Then

\[
\E[\bar X_n] = \mu, \qquad \Var(\bar X_n) = \frac{\sigma^2}{n}, \qquad
\se(\bar X_n) = \frac{\sigma}{\sqrt{n}}.
\]

The weak law states that for every \(\varepsilon > 0\),

\[
\Pr\left(|\bar X_n - \mu| > \varepsilon\right) \to 0 \quad \text{as } n \to \infty .
\]

Chebyshev's inequality gives the rate without any distributional assumption:

\[
\Pr\left(|\bar X_n - \mu| \ge \varepsilon\right) \le \frac{\sigma^2}{n\varepsilon^{2}} .
\]

Two consequences matter. First, the error is of order \(1/\sqrt{n}\): quadrupling the
sample halves the typical error, so precision is expensive. Second, the theorem needs
\(\E|X| < \infty\). The Cauchy distribution \(f(x) = 1/(\pi(1+x^2))\) has no mean — its
tails are so heavy that the sample mean has the *same* distribution as a single
observation for every \(n\). The running average then makes jumps that undo thousands
of observations, which is what the third population in this lab demonstrates.

## How to run the experiment

1. Start with the exponential population, rate 1, 5,000 trials. The path should settle
   near 1.
2. Press **New run** three times. The paths look completely different; the destination
   does not.
3. Increase the trials to 20,000 and note how the later wobble narrows (but does not
   vanish).
4. Switch to the Cauchy population and increase the trials to the maximum. Watch for
   the big jumps.
5. Compare the readout's standard error with the actual distance from \(\mu\).

<div class="psds-lab" data-lab="lln" data-seed="2026">
  <p class="psds-lab__instruction">
    The path is the running average after each observation. The dashed red line is the
    population mean — when it exists.
  </p>
  <div class="psds-lab__grid">
    <div class="psds-lab__controls" data-role="controls">
      <noscript>
        <p><strong>This laboratory needs JavaScript.</strong> Default state: 5,000 draws
        from an exponential population with rate 1. The running average ends near 1
        (the population mean) with a standard error of \(1/\sqrt{5000} = 0.014\). The
        Cauchy population has no mean, so its average does not settle.</p>
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

The readout reports the running average at the end of the path, the population mean,
and the standard error at that \(n\). Judge the average by comparing its distance from
\(\mu\) with \(2\se\): inside that band is ordinary, far outside is unusual but
possible, because the law is a statement about probability, not a guarantee for one
run.

The shape of the path carries the second lesson. Early points swing wildly because
each new observation still carries a large share of the weight \(1/n\). Later,
individual observations barely move the average. That is the arithmetic of \(1/n\)
weights, and it is also why a single outlier early in a series can distort a chart for
a long time.

## Guided activities

1. **Standard error check.** Run the exponential at \(n = 400\), \(n = 1{,}600\) and
   \(n = 6{,}400\). Tabulate the observed distance from \(\mu\) and \(2\se\). Do the
   distances shrink like \(1/\sqrt{n}\)?
2. **Cauchy failure.** With the Cauchy population, record the running average at
   \(n = 500\), 5,000 and 20,000. Is there any sign of settling?
3. **First impressions.** Press New run and note the running average after 20
   observations. How often is it within \(2\se\) of \(\mu\) at that point?
4. **Uniform.** Switch to the uniform population on \([0,2]\). Its mean is 1 and its SD
   is \(1/\sqrt3 = 0.577\). Predict the standard error at \(n = 5{,}000\), then check.

## Independent challenges

1. **How many observations?** You need the running average to be within 0.01 of
   \(\mu\) with 95 % confidence, when \(\sigma = 1\). Find \(n\) from the standard
   error formula and verify with the lab.
2. **A heavier tail.** The Cauchy has no mean. Sketch (in words) what you would expect
   from a distribution whose tails decay like \(1/|x|^{3}\), which has a mean but no
   variance.
3. **A permanent outlier.** Add one observation of 10,000 to 999 draws from a
   \(N(0,1)\) population. How far does the running average move, and how many ordinary
   observations does it take to undo that? Connect this to robustness.
4. **The casino's argument.** Explain why a casino can rely on the law of large
   numbers while a gambler cannot.

## Expected observations

| Population | Mean | SD | Running average at 5,000 | Typical distance from μ |
|---|---|---|---|---|
| Uniform \([0,2]\) | 1.000 | 0.577 | ≈ 1.00 | ≈ 0.008 |
| Exponential, rate 1 | 1.000 | 1.000 | ≈ 1.00 | ≈ 0.014 |
| Cauchy | does not exist | does not exist | jumps anywhere | unbounded |
| Repeated runs, fixed settings | same | same | different paths | same typical size |

## Self-assessment

<details><summary>1. Does the law of large numbers say the average will equal μ after enough trials?</summary>

No. It says the probability of being more than \(\varepsilon\) away tends to zero for
every fixed \(\varepsilon\). At any finite \(n\) there is still a spread of size
\(\sigma/\sqrt{n}\), and the running average keeps moving — just by less and less.
</details>

<details><summary>2. Why does the Cauchy distribution break the law?</summary>

Because the law requires a finite mean, and the Cauchy mean integral does not
converge. The average of \(n\) Cauchy observations has the same Cauchy distribution as
one observation, so no amount of data narrows the uncertainty.
</details>

<details><summary>3. Quadruple the sample: what happens to the typical error?</summary>

It halves. The standard error is \(\sigma/\sqrt{n}\), so multiplying \(n\) by 4 divides
it by 2. Getting ten times more precise costs a hundred times more data.
</details>

<details><summary>4. Is a path that stays on one side of μ for a long time evidence of bias?</summary>

Not by itself. Running averages are highly autocorrelated: if the average is above
\(\mu\), the next average usually is too. Runs and streaks are expected, and they are
why looking at a chart and concluding "it is drifting" is unreliable.
</details>

## Where this connects

- Statements and proofs for both laws are in
  [Module 13](../modules/13-law-of-large-numbers-and-clt/chapter.md).
- [Practical 13](../practicals/notebooks/13-law-of-large-numbers-and-clt.ipynb)
  computes these paths for several populations and compares convergence rates.
- The normal-shape limit is the next lab: [L-07 · the CLT](clt.md). The relationship
  between the two is that the LLN says *where* the average goes, while the CLT says
  *how it is distributed* around that destination.

## Next

- [Lab L-07 — The Central Limit Theorem](clt.md)
- Back to the [laboratory index](index.md)
