---
title: "Lab: the Central Limit Theorem"
description: Change the population shape and sample size, and watch the distribution of the sample mean become normal — or fail to.
---

# Lab: the Central Limit Theorem

**Lab L-07 · Module [13 · The law of large numbers and the CLT](../modules/13-law-of-large-numbers-and-clt/chapter.md) ·
paired with [Practical 13](../practicals/notebooks/13-law-of-large-numbers-and-clt.ipynb) · no installation required**

---

## Learning objectives

By the end of this laboratory you should be able to:

1. define the sampling distribution of the mean and standardise it with
   \\(Z_n = (\\bar X_n - \\mu)/(\\sigma/\\sqrt n)\\);
2. explain why population shape stops mattering as \(n\) grows, and why \(\sigma^2 < \infty\)
   is required;
3. distinguish approximation error (fixed by \(n\)) from Monte Carlo error (fixed by \(B\));
4. describe how the skewness of \(Z_n\) falls as \(n\) grows, and what that means for using
   z and t procedures.

---

## What this lab shows

Draw a sample of size \(n\) from some population and record its mean. Repeat that
thousands of times and you have a new distribution: the **sampling distribution of
the mean**. The Central Limit Theorem says this new distribution is approximately
normal, whatever shape the population had — and this lab lets you watch that happen,
and watch it fail.

**What to do.** Set the population shape, drag the sample size \(n\), and press
**Run simulation**. The histogram shows the standardised sample means from \(B\)
replications; the smooth curve is the standard normal density. The readout reports
the mean and standard deviation of those means, and how far the histogram is from
normal.

<div class="psds-lab" data-lab="clt" data-seed="2026">
  <p class="psds-lab__instruction">
    Choose a population, set the sample size, then run the simulation. Start with
    the exponential population at <em>n</em> = 5 and increase <em>n</em>.
  </p>
  <div class="psds-lab__grid">
    <div class="psds-lab__controls" data-role="controls">
      <noscript>
        <p><strong>This lab needs JavaScript.</strong> The figure below shows the
        result at the default settings: 2,000 sample means of size 5 from an
        exponential population. The histogram is strongly right-skewed, so the
        normal curve fits badly. The mathematics is written out below.</p>
      </noscript>
    </div>
    <div class="psds-lab__figure">
      <div data-role="chart">
        <img class="psds-lab__fallback"
             src="../../assets/images/labs/clt-fallback.svg"
             alt="Histogram of 2,000 standardised sample means, n = 5, drawn from an exponential population. The histogram is strongly right-skewed and the standard normal curve fits it poorly, especially in the right tail.">
        <p class="psds-lab__caption">
          Default state (<em>n</em> = 5, exponential population): the sampling
          distribution is right-skewed and the normal curve does not fit.
        </p>
      </div>
    </div>
  </div>
  <p class="psds-lab__readout" data-role="readout" aria-live="polite"></p>
  <p class="psds-lab__hint" data-role="hint"></p>
</div>

## The mathematics

Let \(X_1, \dots, X_n\) be independent observations from a population with mean
\(\mu\) and finite variance \(\sigma^2\), and let

\[ \bar{X}_n = \frac{1}{n}\sum_{i=1}^{n} X_i \]

be the sample mean. Then \(\E[\bar{X}_n] = \mu\) and \(\Var(\bar{X}_n) = \sigma^2/n\),
so the **standardised** mean is

\[ Z_n = \frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} . \]

The Central Limit Theorem states that, as \(n \to \infty\),

\[ Z_n \xrightarrow{\ d\ } N(0,1), \]

that is, for any fixed \(z\),

\[ \Pr(Z_n \le z) \to \Phi(z). \]

**In words.** Whatever shape the population has, the *average* of many independent
observations is approximately normally distributed around the population mean, with
a spread that shrinks like \(1/\sqrt{n}\) — provided the population has a finite
variance.

**What the lab plots.** The histogram is of \(Z_n\), not of \(\bar{X}_n\). That is why
it is centred at 0 with spread 1 regardless of the population you choose, and why
the standard normal curve is the correct overlay. The readout also reports
\(\sigma/\sqrt{n}\), the standard error, which is the spread on the *original* scale.

### Why it is true (the shape of the argument)

The proof you will meet in [Module 13](../modules/13-law-of-large-numbers-and-clt/chapter.md) uses moment generating functions. The idea is
short enough to state now:

1. The MGF of a sum of independent variables is the **product** of their MGFs.
2. Expand \(M(t)\) of the standardised variable in a Taylor series around 0. The
   first two terms are fixed by the mean and variance: \(1 + t^2/2 + \cdots\).
3. Raising that to the \(n\)th power, as the product rule requires, gives
   \(\left(1 + t^2/(2n) + \cdots\right)^n \to e^{t^2/2}\).
4. \(e^{t^2/2}\) is the MGF of \(N(0,1)\), and MGFs identify distributions.

So the theorem is not magic: it is what happens when you multiply many nearly-1
quantities together.

### The conditions — and why this lab has a Cauchy option

The theorem requires **finite variance**. The Cauchy distribution has none; its
tails are so heavy that the sample mean has the *same* distribution as a single
observation, for every \(n\). Choose the Cauchy population in the lab and drag \(n\)
from 5 to 200: the histogram does not become normal, because the theorem's premise
is false. This is the most important lesson in the lab.

Independence matters too. Observations that are strongly dependent — a time series,
a clustered sample — can violate the conclusion even with finite variance.

## What changes when you move the controls

| Control | What it changes | Why |
|---|---|---|
| **Population** | the shape of \(X\) | tests whether the conclusion is really distribution-free |
| **Sample size \(n\)** | spread of \(\bar{X}_n\), and the quality of the normal approximation | \(\se = \sigma/\sqrt{n}\); skewness of \(Z_n\) falls roughly like \(1/\sqrt{n}\) |
| **Replications \(B\)** | smoothness of the histogram only | more replications reduce Monte Carlo noise, not the approximation error |

That last row is the trap. Increasing \(B\) makes the histogram *prettier*. It does
not make the normal approximation *better*. Only \(n\) does that. If you take one
thing from this lab, take this: **simulation error and approximation error are
different things**, and only one of them is under your control here.

## Guided activities

1. **Exponential, \(n\) = 5 → 30 → 100.** At what \(n\) does the histogram stop
   looking skewed? Sketch the three shapes in your notes and write the \(n\) at
   which you would be willing to use a normal approximation.
2. **Uniform, \(n\) = 2.** The population is flat, so the theorem "should" apply —
   but \(n\) = 2 is not "many". Describe what the histogram actually looks like and
   explain why the theorem is not contradicted.
3. **Bimodal, \(n\) = 30.** The two peaks are real structure in the population. Does
   the sampling distribution preserve them at \(n\) = 30? At \(n\) = 100?
4. **Cauchy, any \(n\).** Explain why nothing changes. Which condition of the theorem
   fails, and what does that mean for using a t-test on such data?

## Independent challenges

1. **How large is large?** For a population with skewness \(\gamma_1\), the skewness
   of \(Z_n\) is about \(\gamma_1/\sqrt n\). Using the lab's skewness readout,
   estimate the \(n\) needed to bring the skew below 0.1 for the exponential
   population, and check your estimate.
2. **A heavier tail.** The lab offers Cauchy. Explain what you would expect for a
   distribution with finite mean but infinite variance (for example a t with 2 degrees
   of freedom), and describe how you could test it in the notebook.
3. **Design decision.** You are planning a study of incomes, which are strongly
   right-skewed, with \(n = 40\). Write two sentences justifying a t-based interval,
   and two sentences a sceptical reviewer could write against it.
4. **Simulation error versus model error.** Suppose the histogram looks lumpy. Give
   two different fixes, say which one is a genuine improvement in the approximation,
   and explain why the other is cosmetic.
5. **Bootstrap.** The CLT is one route to a reference distribution for a mean. Describe
   in words how a bootstrap would produce a similar distribution without assuming
   normality, and name one situation where it is preferable.

## A worked comparison

Take the exponential population with rate \(\lambda = 1\), so \(\mu = 1\) and
\(\sigma = 1\).

| Quantity | Theory | What the lab should show at \(n\) = 30 |
|---|---|---|
| \(\E[\bar{X}]\) | 1.000 | readout mean ≈ 1.00 |
| \(\se(\bar{X}) = \sigma/\sqrt{n}\) | \(1/\sqrt{30} = 0.183\) | readout SD ≈ 0.18 |
| Shape of \(Z_n\) | approximately \(N(0,1)\) | histogram close to the curve |
| Skewness of \(Z_n\) | \(\approx \gamma_1/\sqrt{n} = 2/\sqrt{30} = 0.37\) | small but visible right skew |

At \(n\) = 30 the approximation is usable but not perfect, and the residual skewness
is why some textbooks insist on larger samples for heavily skewed data. At \(n\) = 5
the same table would show a skewness near 0.9 and a visibly poor fit — which is
exactly the default state of the lab.

## Expected observations

| Setting | What the lab should show |
|---|---|
| Exponential, \(n = 5\) | clearly right-skewed histogram, poor normal fit, skew ≈ 0.9 |
| Exponential, \(n = 30\) | usable but visibly skewed (skew ≈ 0.37), SE = 0.183 |
| Exponential, \(n = 100\) | close to normal, skew ≈ 0.2 |
| Uniform, \(n = 2\) | a triangular shape: the theorem's limit has not arrived yet |
| Bimodal, \(n = 30\) | the two peaks have merged into one bell |
| Cauchy, any \(n\) | no convergence at all: the premise fails, not the theorem |

## Self-assessment

<details><summary>1. Does the CLT say the data become normal as n grows?</summary>

No. It says the distribution of the *sample mean*, after standardisation, approaches
the standard normal. The data keep whatever shape the population has.
</details>

<details><summary>2. Why does increasing B not improve the normal approximation?</summary>

\(B\) is the number of simulated samples. It reduces Monte Carlo noise in the
histogram, but the approximation error is governed by \(n\). Making the picture
smoother does not make the theorem's conclusion truer at that \(n\).
</details>

<details><summary>3. What exactly fails for the Cauchy population?</summary>

The finite-variance condition. The Cauchy distribution has no mean and no variance, so
there is no \(\sigma/\sqrt n\) to standardise by, and the sample mean has the same
Cauchy distribution as one observation for every \(n\).
</details>

<details><summary>4. Why do t and z procedures still work for skewed data in practice?</summary>

Because at moderate \(n\) the sampling distribution is close enough to normal for the
tail probabilities used by the procedure — typically \(n \ge 30\) for mild skew, and
much larger for heavy tails. The lab shows why that rule of thumb is about \(n\), not
about the data's appearance.
</details>

## Where this is used

The CLT is the reason the classical procedures in Parts V–VII work at all: the
t-test, the confidence interval for a mean, the normal approximation to the binomial,
and the standard error in a regression table all rest on it. When someone reports a
"95% confidence interval" from a sample of 40 skewed observations, this lab is the
reason to ask whether the approximation is defensible.

## Next

- Continue to [Part IV — Sampling and Limit Theorems](../part-4-sampling/index.md),
  where the theorem is stated, proved and applied.
- See also [confidence interval coverage](confidence-intervals.md) — the CLT in
  action, as a property of a procedure rather than a distribution.
- The full treatment, with exercises and solutions, is
  [Module 13](../modules/13-law-of-large-numbers-and-clt/chapter.md).
- The companion lab that isolates the *where* rather than the *shape* is
  [L-06 · the law of large numbers](law-of-large-numbers.md).
