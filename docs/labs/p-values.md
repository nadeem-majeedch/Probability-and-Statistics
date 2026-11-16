---
title: "Lab L-10: Hypothesis tests and p-values"
description: Simulate studies with and without a real effect, and see what p-values actually do — including how often they reject when nothing is there.
---

# Lab L-10: Hypothesis tests and p-values

**Lab L-10 · Module [15 · Hypothesis testing](../modules/15-hypothesis-testing/chapter.md) ·
paired with [Practical 15](../practicals/notebooks/15-hypothesis-testing.ipynb) · no installation required**

---

## Learning objectives

By the end of this laboratory you should be able to:

1. state the null and alternative hypotheses for a one-sample test of a mean;
2. compute a t statistic and its degrees of freedom, and read a p-value from it;
3. explain what a p-value is — and what it is not;
4. describe the distribution of p-values when the null hypothesis is true;
5. distinguish statistical significance from the size of the effect.

## The idea in one paragraph

A p-value answers one narrow question: *if the null hypothesis were true, how often
would data look at least this extreme?* It is a statement about the data given the
hypothesis, never about the hypothesis given the data. This lab runs the experiment
that makes that concrete. You set a true effect size (possibly zero) and a sample
size, and the lab simulates a thousand studies, computing a t statistic and a p-value
for each. Two pictures tell the story: the null distribution with the rejection region
shaded, and a histogram of the thousand p-values. With no real effect, that histogram
is flat — every p-value is equally likely, including 0.04.

## The mathematics

For a sample \(x_1,\dots,x_n\) with sample mean \(\bar x\) and sample standard
deviation \(s\), the one-sample t statistic for \(H_0: \mu = 0\) is

\[
t = \frac{\bar x}{s/\sqrt{n}}, \qquad \text{df} = n-1,
\]

and under \(H_0\) it follows a Student t distribution with \(n-1\) degrees of freedom.
For a two-sided alternative the p-value is

\[
p = \Pr(|T_{n-1}| \ge |t|) = 2\left[1 - F_{t_{n-1}}(|t|)\right],
\]

where \(F\) is the t CDF. For a one-sided alternative the whole tail is used:

\[
p = \Pr(T_{n-1} \ge t) \quad \text{or} \quad \Pr(T_{n-1} \le t).
\]

The test rejects when \(p \le \alpha\). When \(H_0\) is true the p-value is uniformly
distributed on \((0,1)\): \(\Pr(p \le \alpha) = \alpha\) exactly. That uniformity is
the flat histogram in the lab, and it is why "\(p = 0.049\)" is not by itself evidence
of a real effect — it is exactly what a null study produces 4.9 % of the time.

When a real effect \(\delta\) (in standard-deviation units) is present, the statistic
follows a noncentral t distribution. The probability of rejection is the power, which
[Lab L-13](power-and-errors.md) studies directly; this lab measures it by simulation
instead.

## How to run the experiment

1. Start with no true effect: \(\delta = 0\), \(n = 30\), \(\alpha = 0.05\), two-sided.
2. Confirm that about 5 % of the simulated studies reject, and that the p-value
   histogram is flat.
3. Set \(\delta = 0.5\) and watch the rejection rate climb and the histogram pile up
   near zero.
4. Change \(\alpha\) to 0.01: the critical value moves out, the rejection rate falls,
   and the flat histogram is cut at 1 %.
5. Switch to a one-sided alternative with \(\delta = 0\): the rate is still \(\alpha\),
   which is the point — the level is a choice, not a discovery.

<div class="psds-lab" data-lab="pvalues" data-seed="2026">
  <p class="psds-lab__instruction">
    The upper chart is the null t distribution with the rejection region shaded. The
    lower chart is the p-value from each simulated study.
  </p>
  <div class="psds-lab__grid">
    <div class="psds-lab__controls" data-role="controls">
      <noscript>
        <p><strong>This laboratory needs JavaScript.</strong> Default state: no true
        effect, \(n = 30\), \(\alpha = 0.05\), two-sided. The critical value is
        \(|t| = 2.045\) on 29 degrees of freedom, about 5 % of simulated studies reject,
        and the p-values are uniformly distributed.</p>
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

Four numbers carry the argument. The **critical value** is where the rejection region
starts on the t scale; it depends on \(\alpha\) and on the degrees of freedom, which
depend on \(n\). The **observed rejection rate** is the share of simulated studies that
came out significant — with no effect it estimates \(\alpha\). The **mean p-value** is
0.5 when the null is true and falls towards zero as the effect grows. The **first
study** line shows a single t and p, which is what a real paper reports; one study
tells you much less than the histogram does.

The histogram is the most useful object in the lab. Flat means "no effect"; piled up at
zero means "effect large enough to be detected at this \(n\)"; and a shape that is flat
but with a spike near zero is what happens with a small effect and modest power.

## Guided activities

1. **Uniformity.** With \(\delta = 0\) and \(B = 3000\), estimate the share of
   p-values below 0.10, 0.05 and 0.01. Compare with the levels.
2. **Power by simulation.** Set \(\delta = 0.5\), \(n = 30\) and record the rejection
   rate. Compare it with the analytic power from [Lab L-13](power-and-errors.md),
   which is about 0.78 for a z test.
3. **Threshold shopping.** With \(\delta = 0.2\), \(n = 20\), run several times. How
   often does a "significant" result appear? What would reporting only the significant
   run amount to?
4. **One-sided tests.** Set the alternative to one-sided, \(\delta = 0.3\). Does the
   rejection rate rise or fall compared with two-sided? Is that a free lunch?

## Independent challenges

1. **Sample size.** Find the smallest \(n\) (multiple of 5) at which a true effect of
   \(\delta = 0.3\) is detected at least 80 % of the time with \(\alpha = 0.05\)
   two-sided.
2. **p-hacking by simulation.** Keep \(\delta = 0\) but imagine running five independent
   tests and reporting the smallest p. Simulate this in the notebook: what is the
   chance that at least one of five null tests gives \(p < 0.05\)?
3. **Effect versus evidence.** With \(n = 200\), set \(\delta = 0.1\). The rejection
   rate is high, yet the effect is tiny. Write two sentences a policy reader could
   follow explaining why "significant" is not "important".
4. **Degrees of freedom.** At fixed \(\delta\) and \(n\), compare the critical value for
   \(n = 6\) and \(n = 200\). Which one is closer to 1.96, and why?

## Expected observations

| Setting | Critical value | Rejection rate | p-value histogram |
|---|---|---|---|
| \(\delta=0, n=30, \alpha=0.05\) | 2.045 | ≈ 5 % | flat |
| \(\delta=0, n=30, \alpha=0.01\) | 2.756 | ≈ 1 % | flat, cut at 1 % |
| \(\delta=0.5, n=30\) | 2.045 | ≈ 70–80 % | piled near 0 |
| \(\delta=0.5, n=10\) | 2.262 | ≈ 30–40 % | partly piled, mostly flat |
| \(\delta=1.0, n=30\) | 2.045 | > 99 % | almost all below 0.01 |

## Self-assessment

<details><summary>1. What exactly does \(p = 0.03\) mean?</summary>

If \(H_0\) were true, 3 % of studies of this design would produce a t statistic at
least this far from zero. It is not the probability that \(H_0\) is true, and it is not
the probability that the result is wrong.
</details>

<details><summary>2. Why are p-values uniform when the null is true?</summary>

Because the p-value is the probability integral transform of the test statistic: under
\(H_0\), \(F(T)\) is uniform on \((0,1)\). That is why \(\Pr(p \le \alpha) = \alpha\)
exactly, for any \(\alpha\).
</details>

<details><summary>3. Does a smaller p-value mean a larger effect?</summary>

No. The p-value depends on the effect size *and* the sample size (and on the
variability). A tiny effect measured precisely can give a smaller p-value than a large
effect measured noisily.
</details>

<details><summary>4. Why does the critical value change with n?</summary>

Because the reference distribution is Student t with \(n-1\) degrees of freedom, which
has heavier tails than the normal for small \(n\). As \(n\) grows, t converges to
normal and the 5 % critical value tends to 1.96.
</details>

## Where this connects

- [Module 15](../modules/15-hypothesis-testing/chapter.md) develops the logic of
  tests, one- and two-sided alternatives, and the t distribution.
- [Practical 15](../practicals/notebooks/15-hypothesis-testing.ipynb) runs these
  tests with `scipy.stats.ttest_1samp` and examines p-value distributions.
- The decision-theoretic side — Type I and Type II errors — is
  [Lab L-13](power-and-errors.md).
- [Figure 11.1 in Module 15](../modules/15-hypothesis-testing/chapter.md) draws the
  two distributions and the α and β areas.

## Next

- [Lab L-11 — Correlation and linear regression](correlation-regression.md)
- Back to the [laboratory index](index.md)
