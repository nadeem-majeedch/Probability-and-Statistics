---
title: "Lab L-02: Conditional probability and Bayes' theorem"
description: Move prevalence, sensitivity and the false-positive rate, and watch the posterior probability — and the mosaic of people behind it.
---

# Lab L-02: Conditional probability and Bayes' theorem

**Lab L-02 · Module [07 · Conditional probability and Bayes](../modules/07-conditional-probability-and-bayes/chapter.md) ·
paired with [Practical 07](../practicals/notebooks/07-conditional-probability-and-bayes.ipynb) · no installation required**

---

## Learning objectives

By the end of this laboratory you should be able to:

1. distinguish \(\Pr(A \mid B)\) from \(\Pr(B \mid A)\) and say why they differ;
2. derive Bayes' theorem from the definition of conditional probability and the law
   of total probability;
3. compute the posterior probability of a condition given a positive test from its
   prevalence, sensitivity and false-positive rate;
4. explain the base-rate effect: why a good test on a rare condition produces mostly
   false positives;
5. convert a probability into odds and use the odds form of Bayes' theorem.

## The idea in one paragraph

Conditional probability is probability *after* you learn something. A test result is
information, and the question "given that this person tested positive, what is the
chance they have the condition?" is not the same as "given that they have the
condition, what is the chance they test positive?". The first is the posterior, the
second is the sensitivity the manufacturer quotes. The mosaic plot shows the people
behind the arithmetic: each rectangle is a group of people, its width is how common
the condition is, its height is how the test behaves. The vertical strip through the
top row is everyone who tested positive — and the posterior is the share of that
strip that belongs to the narrow left column.

## The mathematics

For events \(A\) (has the condition) and \(B\) (tests positive), with
\(\Pr(B) > 0\),

\[
\Pr(A \mid B) = \frac{\Pr(A \cap B)}{\Pr(B)}
= \frac{\Pr(B \mid A)\Pr(A)}{\Pr(B \mid A)\Pr(A) + \Pr(B \mid A^{c})\Pr(A^{c})},
\]

where the denominator is the law of total probability. Writing \(\pi = \Pr(A)\),
\(\operatorname{sens} = \Pr(B \mid A)\) and \(\operatorname{fpr} = \Pr(B \mid A^{c})\),

\[
\Pr(A \mid B) = \frac{\operatorname{sens}\,\pi}
{\operatorname{sens}\,\pi + \operatorname{fpr}\,(1-\pi)} .
\]

The negative predictive value is the same calculation on the other side:

\[
\Pr(A^{c} \mid B^{c}) = \frac{(1-\operatorname{fpr})(1-\pi)}
{(1-\operatorname{fpr})(1-\pi) + (1-\operatorname{sens})\pi}.
\]

In odds form, \(\text{posterior odds} = \text{likelihood ratio} \times \text{prior odds}\):

\[
\frac{\Pr(A \mid B)}{\Pr(A^{c} \mid B)}
= \frac{\operatorname{sens}}{\operatorname{fpr}}\cdot\frac{\pi}{1-\pi}.
\]

With the defaults — \(\pi = 0.10\), sensitivity 0.90, false-positive rate 0.05 — the
likelihood ratio is 18, the prior odds are 1 : 9, so the posterior odds are 2 : 1 and
\(\Pr(A \mid B) = 0.667\). Two out of three positives are true positives even though
the test is "90 % accurate". Nothing is wrong with the test; the condition is simply
rarer than the test is wrong.

## How to run the experiment

1. Start from the defaults: prevalence 0.10, sensitivity 0.90, false positive 0.05,
   2,000 simulated people.
2. Read the mosaic: the left column is the 10 % with the condition, the top row is
   everyone who tested positive. The headline gives the exact posterior and the
   observed one.
3. Lower the prevalence to 0.01 and watch the posterior collapse. This is the
   base-rate trap and it is the point of the lab.
4. Raise the false-positive rate to 0.30. Explain what happens to the posterior in
   one sentence.
5. Press **New run** with the settings unchanged: the counts change, the theoretical
   posterior does not.

<div class="psds-lab" data-lab="conditional" data-seed="2026">
  <p class="psds-lab__instruction">
    Each rectangle is a group of people: width = how common the condition is, height =
    how the test behaves. The posterior is the share of the positive row that lies in
    the "has the condition" column.
  </p>
  <div class="psds-lab__grid">
    <div class="psds-lab__controls" data-role="controls">
      <noscript>
        <p><strong>This laboratory needs JavaScript.</strong> At the defaults — 10 %
        prevalence, 90 % sensitivity, 5 % false positives — the posterior probability
        of the condition after a positive test is \(0.667\), and the negative
        predictive value is \(0.988\). The derivation is above.</p>
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

Three numbers carry the lesson. \(\Pr(B)\), the chance of a positive test, is usually
much larger than the prevalence — here 0.135, so about one person in seven tests
positive. The posterior \(\Pr(A \mid B)\) is the answer to the question everyone
actually asks, and it is 0.667, not 0.90. The negative predictive value 0.988 is much
higher than the sensitivity, for the mirror-image reason: negatives are common, so
most negatives are true negatives.

Notice what never changes: sensitivity and the false-positive rate are properties of
the *test*. The posterior is a property of the *population plus the test*. Change the
population and the same test tells a different story.

## Guided activities

1. **Base rates.** Set prevalence to 0.30, then 0.10, then 0.01, keeping sensitivity
   and false-positive rate fixed. Tabulate the posterior for each. Where does it fall
   below 0.5?
2. **Odds form.** Compute the likelihood ratio 0.90 / 0.05 = 18 by hand; multiply by
   the prior odds for \(\pi = 0.10\) and convert back. Confirm you get 0.667.
3. **A perfect test.** Set sensitivity to 1.00 and the false-positive rate to 0.
   Predict the posterior, then check. Which of the two sliders matters more here?
4. **The mirror question.** Read \(\Pr(A^{c} \mid B^{c})\) at 0.10 prevalence and
   explain why it is higher than 0.90 even though the test is 90 % sensitive.

## Independent challenges

1. **Two tests.** A patient tests positive twice. Using the posterior from the first
   test as the new prior, compute the posterior after the second. (Assume conditional
   independence given the condition — say why that assumption is needed.)
2. **Screening policy.** A condition affects 1 in 5,000. A test with sensitivity 0.99
   and false-positive rate 0.02 is proposed for mass screening. Compute the posterior
   and write two sentences advising a health authority.
3. **Break-even prevalence.** For sensitivity 0.90 and false-positive rate 0.05, find
   the prevalence at which the posterior reaches 0.5. Solve it algebraically and check
   with the lab.
4. **Where the simulation disagrees.** At small prevalence and small \(n\), the
   observed posterior can jump between 0 and 1. Explain why, in terms of how few true
   positives exist in the sample.

## Expected observations

| Setting | Posterior \(\Pr(A\mid B)\) | What it means |
|---|---|---|
| 0.10 / 0.90 / 0.05 (default) | 0.667 | two of three positives are genuine |
| 0.30 / 0.90 / 0.05 | 0.885 | common condition, test looks good |
| 0.01 / 0.90 / 0.05 | 0.154 | rare condition, most positives are false |
| 0.10 / 0.90 / 0.30 | 0.250 | a sloppy test wastes the prior |
| 0.10 / 1.00 / 0.00 | 1.000 | perfect test: posterior is certainty |

## Self-assessment

<details><summary>1. Why is \(\Pr(A\mid B) \neq \Pr(B\mid A)\) in general?</summary>

Because conditional probability normalises by a different event. \(\Pr(A\mid B)\)
divides by \(\Pr(B)\), which includes false positives; \(\Pr(B\mid A)\) divides by
\(\Pr(A)\), which is the prevalence. They coincide only when \(\Pr(A)=\Pr(B)\), or when
the test is perfect.
</details>

<details><summary>2. A test is 99 % sensitive and 99 % specific. Can a positive result still be more likely false than true?</summary>

Yes. Specificity 0.99 means a 1 % false-positive rate. If the prevalence is 1 in
10,000, then in 10,000 people there are about 1 true case and 100 false positives, so
the posterior is about 1 %. Accuracy on a balanced sample says nothing about a rare
one.
</details>

<details><summary>3. What does the mosaic's area represent?</summary>

The number of people in each of the four cells. Areas are proportional to joint
probabilities, which is why the posterior can be read as a ratio of areas inside the
top row.
</details>

<details><summary>4. Why do repeated runs change the observed posterior but not the theoretical one?</summary>

The theoretical value is a function of the three parameters. The observed value is a
ratio of simulated counts, which carries binomial sampling error — small when the
numbers in each cell are large, erratic when they are tiny.
</details>

## Where this connects

- The definition, the multiplication rule, independence and Bayes' theorem are in
  [Module 07](../modules/07-conditional-probability-and-bayes/chapter.md).
- [Practical 07](../practicals/notebooks/07-conditional-probability-and-bayes.ipynb)
  repeats this calculation in Python and extends it to a confusion matrix.
- The case study [E3 · Diagnostic test accuracy](../case-studies/e3-diagnostic-accuracy.md)
  applies it to a real table of results.
- Continuous Bayesian updating is [Lab L-12](bayesian-updating.md).

## Next

- [Lab L-03 — Discrete probability distributions](discrete-distributions.md)
- Back to the [laboratory index](index.md)
