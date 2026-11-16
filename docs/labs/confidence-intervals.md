---
title: "Lab: confidence interval coverage"
description: Watch one hundred confidence intervals capture or miss a fixed mean, and see what "95% confidence" actually guarantees.
---

# Lab: confidence interval coverage

**Lab L-09 · Module [14 · Estimation and confidence intervals](../modules/14-estimation-and-confidence-intervals/chapter.md) ·
paired with [Practical 14](../practicals/notebooks/14-estimation-and-confidence-intervals.ipynb) · no installation required**

---

## Learning objectives

By the end of this laboratory you should be able to:

1. state what "95 % confidence" means as a property of the procedure;
2. compute a confidence interval for a mean with known \(\sigma\) and explain each term;
3. predict how the level, the sample size and \(\sigma\) change the width;
4. explain why a particular interval either contains \(\mu\) or does not, and why that
   is not a probability statement about this interval.

---

## What this lab shows

A 95% confidence interval is not a statement that the parameter has a 95% chance of
lying inside *this* interval. It is a statement about the **procedure**: if you
repeated your sampling many times, about 95% of the intervals you built would contain
the parameter.

That is a claim about long-run behaviour, which is exactly the kind of claim a
simulation can settle. This lab draws many samples from a known population, builds an
interval for each, and counts how many capture the true mean — which you can see,
because in a simulation the truth is known.

**What to do.** Set the confidence level and the sample size, then press **Run**. Each
horizontal line is one interval; the vertical line is the true mean \(\mu\). Intervals
that miss are drawn in the warning colour. The readout gives the observed coverage
against the nominal level.

<div class="psds-lab" data-lab="ci" data-seed="2026">
  <p class="psds-lab__instruction">
    Set a confidence level and sample size, then run. Start at 95% with
    <em>n</em> = 30, then try 80% and 99%.
  </p>
  <div class="psds-lab__grid">
    <div class="psds-lab__controls" data-role="controls">
      <noscript>
        <p><strong>This lab needs JavaScript.</strong> The figure below shows the
        default result: 100 intervals at the 95% level from samples of size 30.
        About five of them miss the true mean, which is what 95% coverage means.</p>
      </noscript>
    </div>
    <div class="psds-lab__figure">
      <div data-role="chart">
        <img class="psds-lab__fallback"
             src="../../assets/images/labs/ci-fallback.svg"
             alt="One hundred horizontal confidence intervals stacked vertically, each from a sample of size 30 at the 95% level. A vertical line marks the true mean at 100. Five intervals do not cross the line.">
        <p class="psds-lab__caption">
          Default state (95%, <em>n</em> = 30): most intervals cross the true mean;
          a few miss. Coverage is a property of the procedure, not of one interval.
        </p>
      </div>
    </div>
  </div>
  <p class="psds-lab__readout" data-role="readout" aria-live="polite"></p>
  <p class="psds-lab__hint" data-role="hint"></p>
</div>

## The mathematics

Let \(X_1, \dots, X_n\) be independent \(N(\mu, \sigma^2)\) observations with
\(\sigma\) known. Then

\[ \bar{X} \sim N\!\left(\mu, \frac{\sigma^2}{n}\right)
\quad\Longrightarrow\quad
Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0,1). \]

Choose \(z_{1-\alpha/2}\) so that \(\Pr(-z_{1-\alpha/2} \le Z \le z_{1-\alpha/2})
= 1 - \alpha\). Rearranging the inequality to isolate \(\mu\) gives the interval

\[ \mathrm{CI}_{1-\alpha} =
\left[\, \bar{X} - z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}},\;\;
       \bar{X} + z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}} \,\right]. \]

**In words.** Take the sample mean, and step away from it by \(z\) standard errors in
each direction. Because \(\bar{X}\) varies from sample to sample, so does the
interval: it is a random object.

**Why coverage is \(1-\alpha\).** The interval contains \(\mu\) exactly when
\(|Z| \le z_{1-\alpha/2}\), an event with probability \(1-\alpha\) — *before* you
observe the data. Once the data are in, the interval is fixed and \(\mu\) is fixed;
either it contains \(\mu\) or it does not. The probability statement is about the
procedure, and the lab makes this concrete by showing you many procedures at once.

**When \(\sigma\) is unknown.** Replace \(\sigma\) with \(s\) and \(z\) with
\(t_{n-1,\,1-\alpha/2}\). The interval becomes wider, increasingly so for small
\(n\) — which is why the lab's coverage at \(n\) = 5 is worth inspecting closely
even though this version uses the known-\(\sigma\) formula.

## What changes when you move the controls

| Control | What it changes | Why |
|---|---|---|
| **Confidence level** | the width of every interval, and the miss rate | higher confidence demands a wider interval and misses less often |
| **Sample size \(n\)** | width, as \(1/\sqrt{n}\) | quadrupling \(n\) halves the width |
| **Number of intervals \(B\)** | how stable the observed coverage is | Monte Carlo noise, not statistical accuracy |

Two things worth noticing, and they are the point of the lab:

1. **A 99% interval is not "better" than a 95% interval.** It is wider. If you want
   both high confidence and a narrow interval, the only lever is more data.
2. **Some 95% intervals miss.** At the default settings roughly 5 in 100 will. That
   is not a bug in the procedure; it is what the number means. A procedure that never
   missed would be claiming certainty it does not have.

## Guided activities

1. **95%, \(n\) = 30.** Run it twice. How much does the observed coverage move
   between runs? Explain why that variation is not a flaw in the method.
2. **95% → 99%.** Record the average width at both levels. Compute the ratio of the
   two \(z\) multipliers and check it against your measurement.
3. **\(n\) = 30 → 120.** Predict the new average width before running. Then check:
   did it halve?
4. **80% level.** How many intervals miss? Is an 80% interval useless, or is it
   simply a different trade-off? Write two sentences defending your answer.
5. **\(n\) = 5.** Look at the coverage and the width. Now imagine repeating this with
   \(s\) instead of \(\sigma\), as you must in practice. Why does the t interval exist?

## Independent challenges

1. **Design a study.** You want the half-width of a 95 % interval for a mean to be at
   most 2 units, and you believe \(\sigma pprox 12\). Find the sample size, then
   check that the average width in the lab matches.
2. **Budget.** Halving the width costs four times the data. Estimate the cost of going
   from a half-width of 4 to a half-width of 1, in units of "samples of size 30".
3. **Wrong model.** Suppose the data are heavily skewed and \(n = 12\). Simulate a
   skewed population in the notebook and compute the coverage of
   \(ar x \pm 1.96\,\sigma/\sqrt n\) empirically. How far below 95 % does it fall?
4. **Interpretation for a report.** A colleague writes: "the true mean is 100 with 95 %
   probability, because the interval is [98.1, 101.9]". Correct the sentence without
   using the word "wrong", and say what the 95 % actually refers to.
5. **A different statistic.** The same logic gives an interval for a proportion using
   \(\hat p \pm z\sqrt{\hat p(1-\hat p)/n}\). Explain which quantity in the lab's
   construction is replaced, and what stays the same.

## Expected observations

| Setting | Coverage you should see | Mean width |
|---|---|---|
| 95 %, \(n = 30\), \(B = 100\) | about 95 of 100 intervals capture \(\mu\) | \(2 	imes 1.96 	imes 15/\sqrt{30} = 10.74\) |
| 99 %, \(n = 30\) | about 99 of 100 | wider: 15.44 |
| 80 %, \(n = 30\) | about 80 of 100 | narrower: 7.86 |
| 95 %, \(n = 120\) | still about 95 of 100 | half the width: 5.37 |
| any setting, rerun | the count moves by a few | unchanged by \(B\) alone |

## Self-assessment

<details><summary>1. After computing a 95 % interval, may you say "there is a 95 % chance μ is in it"?</summary>

Not in the frequentist framework. \(\mu\) is fixed and the interval is random: this
particular interval either contains it or not, and the 95 % refers to the long-run
share of intervals that do. A Bayesian credible interval does support the probability
statement — see [Lab L-12](bayesian-updating.md).
</details>

<details><summary>2. Why does the width fall like 1/√n rather than 1/n?</summary>

Because the standard error of the mean is \(\sigma/\sqrt n\). Cutting the width in
half needs four times the sample, which is why precision is expensive.
</details>

<details><summary>3. What happens to coverage if you use 1.96 but the data are heavily skewed and n is small?</summary>

Coverage falls below 95 %. The interval relies on the sampling distribution being
approximately normal; when it is not, the nominal level is not achieved. This is the
practical consequence of the [CLT lab](clt.md).
</details>

<details><summary>4. Does a wider interval mean a better estimate?</summary>

No. Width measures precision, not correctness. A wide interval is honest about
uncertainty; a narrow one built on a violated assumption can be confidently wrong.
</details>

## A worked comparison

Population: \(\mu = 100\), \(\sigma = 15\), so the standard error at \(n = 30\) is
\(15/\sqrt{30} = 2.739\).

| Level | \(z_{1-\alpha/2}\) | Half-width | Interval width | Expected misses in 100 |
|---|---|---|---|---|
| 80% | 1.282 | 3.51 | 7.02 | 20 |
| 90% | 1.645 | 4.51 | 9.01 | 10 |
| 95% | 1.960 | 5.37 | 10.74 | 5 |
| 99% | 2.576 | 7.06 | 14.11 | 1 |

At the 95% level, the readout's observed coverage should sit near 95% with a
fluctuation of roughly \(\sqrt{0.95 \times 0.05 / 100} \approx 2.2\) percentage
points across repeated runs of 100 intervals. If you see 88%, that is more than two
standard deviations low and worth investigating; if you see 97%, that is ordinary
noise.

## Where this is used

Every confidence interval in Parts V–VII — for a mean, a proportion, a difference in
means, a regression coefficient — is built the same way and interpreted the same way.
The lab's lesson transfers directly: report the level, report the width, and never
say "there is a 95% probability that \(\mu\) is in this interval".

## Next

- Continue to [Part V — Statistical Inference](../part-5-inference/index.md).
- The distribution the intervals are built from is the subject of
  [the CLT lab](clt.md).
- Full treatment with the t interval, the proportion interval and exercises:
  [Module 14](../modules/14-estimation-and-confidence-intervals/chapter.md).
