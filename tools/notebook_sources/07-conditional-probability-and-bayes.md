# Practical 07 — Conditional Probability and Bayes' Theorem

## 1. Introduction

Most real probabilities are conditional: the chance a patient has a disease *given* a
positive test, the chance a message is spam *given* its words, the chance a customer
churns *given* their last three sessions.

Conditioning is also where intuition fails most reliably. A test that is "99% accurate"
can still leave a positive result far more likely to be wrong than right, because the
base rate dominates. This practical computes that case exactly, checks it by simulation,
and then applies the same arithmetic to sequential updating and a small spam filter.

## 2. Learning objectives

By the end of this practical you can:

1. Compute conditional probability from a two-way table and from a formula.
2. Use the multiplication rule and the law of total probability.
3. Apply Bayes' theorem in probability and odds form.
4. Explain the base-rate fallacy with numbers, and state what a positive test means.
5. Update a belief across two conditionally independent tests.

## 3. Required libraries

| Library | Used for |
|---|---|
| `numpy` | simulating a population with a fixed seed |
| `pandas` | contingency tables and grouped rates |
| `matplotlib` | posterior against prevalence |

## 4. Concepts

### 4.1 Conditioning narrows the sample space

\[ \Pr(A\mid B)=\frac{\Pr(A\cap B)}{\Pr(B)},\qquad \Pr(B)>0. \]

The definition is a renormalisation: "given \(B\)" throws away every outcome outside
\(B\) and rescales what remains so that it sums to 1. That is why conditional
probabilities can be much larger or much smaller than unconditional ones.

### 4.2 Multiplication rule and total probability

\[ \Pr(A\cap B)=\Pr(A\mid B)\Pr(B)=\Pr(B\mid A)\Pr(A). \]

If \(B_1,\dots,B_k\) partition the sample space,

\[ \Pr(A)=\sum_{i}\Pr(A\mid B_i)\Pr(B_i). \]

Total probability is how a rate is computed from subgroup rates: overall conversion is
the average of the per-group rates, weighted by group size.

### 4.3 Bayes' theorem

\[ \Pr(B_i\mid A)=\frac{\Pr(A\mid B_i)\Pr(B_i)}{\sum_j \Pr(A\mid B_j)\Pr(B_j)}. \]

In words: posterior \(\propto\) likelihood \(\times\) prior. The denominator is the
total probability of the evidence, and its job is only to normalise.

**Odds form**, which is what practitioners actually use:

\[ \underbrace{\frac{\Pr(D\mid +)}{\Pr(\text{not }D\mid +)}}_{\text{posterior odds}}
   =\underbrace{\frac{\Pr(+\mid D)}{\Pr(+\mid \text{not }D)}}_{\text{likelihood ratio}}
    \times\underbrace{\frac{\Pr(D)}{\Pr(\text{not }D)}}_{\text{prior odds}}. \]

The likelihood ratio is the test's diagnostic information: how much more often a
positive occurs in diseased than in healthy people. It multiplies the prior odds; it
does not replace them.

### 4.4 The base-rate fallacy

Confusing \(\Pr(+\mid D)\) with \(\Pr(D\mid +)\) is the error. The first is the test's
sensitivity, a property of the test. The second is what a patient and a clinician need,
and it depends on prevalence. When a disease is rare, most positives are false
positives even with a good test — arithmetic, not pessimism.

## 5. Formulas

\[ \Pr(D\mid +)=\frac{\Pr(+\mid D)\Pr(D)}
   {\Pr(+\mid D)\Pr(D)+\Pr(+\mid \text{not }D)\Pr(\text{not }D)} \]

With sensitivity \(s\), specificity \(c\), prevalence \(\pi\):

\[ \Pr(D\mid +)=\frac{s\pi}{s\pi+(1-c)(1-\pi)} \]

\[ \text{posterior odds}=\text{LR}\times\text{prior odds},\qquad
   \text{LR}^{+}=\frac{s}{1-c} \]

## 6. Implementation

### 6.1 The screening problem, exactly

A disease affects 1% of a population. The test has sensitivity 0.99 (detects 99% of
cases) and specificity 0.95 (correctly clears 95% of healthy people).

```python
prevalence = 0.01
sensitivity = 0.99      # P(+ | D)
specificity = 0.95      # P(- | not D)

p_pos_given_d = sensitivity
p_pos_given_not_d = 1 - specificity

p_pos = p_pos_given_d * prevalence + p_pos_given_not_d * (1 - prevalence)
p_d_given_pos = p_pos_given_d * prevalence / p_pos

print(f"P(+ | D)        = {p_pos_given_d:.4f}")
print(f"P(+ | not D)    = {p_pos_given_not_d:.4f}")
print(f"P(+)            = {p_pos:.4f}")
print(f"P(D | +)        = {p_d_given_pos:.4f}")
print(f"so a positive is wrong {1 - p_d_given_pos:.1%} of the time")
```

```python
# The same result in odds form: prior odds x likelihood ratio.
prior_odds = prevalence / (1 - prevalence)
lr_pos = p_pos_given_d / p_pos_given_not_d
posterior_odds = prior_odds * lr_pos
print(f"prior odds     = {prior_odds:.4f}  (1 in {1/prior_odds:.1f})")
print(f"likelihood ratio = {lr_pos:.2f}")
print(f"posterior odds = {posterior_odds:.4f}")
print(f"posterior prob = {posterior_odds / (1 + posterior_odds):.4f}")
```

### 6.2 Checking it on a simulated population

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(2026)
n_people = 200_000

has_disease = rng.random(n_people) < prevalence
test_positive = np.where(
    has_disease,
    rng.random(n_people) < sensitivity,
    rng.random(n_people) < (1 - specificity),
)

df = pd.DataFrame({"disease": has_disease, "positive": test_positive})
table = pd.crosstab(df["disease"], df["positive"],
                    rownames=["disease"], colnames=["test positive"])
print(table.to_string())

empirical = (table.loc[True, True] / table[True].sum())
print(f"\nP(D | +) simulated = {empirical:.4f}")
print(f"P(D | +) exact     = {p_d_given_pos:.4f}")
print(f"difference         = {empirical - p_d_given_pos:+.4f}")
```

```python
# The four groups, as counts per 100,000 people: this is the table that makes the
# arithmetic obvious.
counts = table / n_people * 100_000
print(counts.round(1).to_string())
print("\nof every 100,000 people, positives are split:")
print(f"  true positives  : {counts.loc[True, True]:.0f}")
print(f"  false positives : {counts.loc[False, True]:.0f}")
```

### 6.3 Two positive tests in a row

If the two tests are **conditionally independent** given disease status, the second
positive multiplies the odds by the same likelihood ratio again.

```python
posterior_after_one = posterior_odds
posterior_after_two = posterior_after_one * lr_pos
p_after_two = posterior_after_two / (1 + posterior_after_two)

print(f"after one positive: odds {posterior_after_one:.3f}, "
      f"probability {posterior_after_one/(1+posterior_after_one):.4f}")
print(f"after two positives: odds {posterior_after_two:.3f}, "
      f"probability {p_after_two:.4f}")
```

```python
# Simulate the same two-test procedure to confirm the arithmetic.
rng = np.random.default_rng(7)
n_people = 300_000
d = rng.random(n_people) < prevalence
t1 = np.where(d, rng.random(n_people) < sensitivity,
              rng.random(n_people) < (1 - specificity))
t2 = np.where(d, rng.random(n_people) < sensitivity,
              rng.random(n_people) < (1 - specificity))
both_positive = t1 & t2
sim_two = d[both_positive].mean()
print(f"simulated P(D | +,+) = {sim_two:.4f}")
print(f"exact                = {p_after_two:.4f}")
print(f"people with two positives: {both_positive.sum():,}")
```

The assumption matters: if the two tests share a mechanism (the same antibody, the same
imaging artefact), their errors are correlated and the second test adds less than this
calculation claims.

### 6.4 Conditioning in a table: a different question

```python
rng = np.random.default_rng(11)
n = 4000
df2 = pd.DataFrame({
    "programme": rng.choice(["DS", "CS"], size=n, p=[0.55, 0.45]),
})
df2["internship"] = np.where(
    df2["programme"] == "DS",
    rng.random(n) < 0.62,
    rng.random(n) < 0.48,
)

tab = pd.crosstab(df2["programme"], df2["internship"], normalize="index")
print("P(internship | programme):")
print(tab.round(3).to_string())

counts = pd.crosstab(df2["programme"], df2["internship"])
print("\ncounts:")
print(counts.to_string())

p_intern = df2["internship"].mean()
p_intern_ds = df2.loc[df2.programme == "DS", "internship"].mean()
p_intern_cs = df2.loc[df2.programme == "CS", "internship"].mean()
share_ds = (df2.programme == "DS").mean()
print(f"\noverall P(internship) = {p_intern:.4f}")
print(f"weighted average       = {share_ds*p_intern_ds + (1-share_ds)*p_intern_cs:.4f}")
```

The overall rate is the weighted average of the two conditional rates — that is the law
of total probability, computed from the data rather than assumed.

### 6.5 A tiny spam filter

Two words, three messages' worth of counts per class. The filter computes
\(\Pr(\text{spam}\mid\text{word})\) from
\(\Pr(\text{word}\mid\text{spam})\Pr(\text{spam})\).

```python
vocab = {"free": {"spam": 0.60, "ham": 0.05},
         "meeting": {"spam": 0.10, "ham": 0.40}}
p_spam = 0.30

for word, likelihoods in vocab.items():
    num = likelihoods["spam"] * p_spam
    den = num + likelihoods["ham"] * (1 - p_spam)
    print(f"P(spam | '{word}') = {num/den:.4f}   "
          f"(likelihood ratio {likelihoods['spam']/likelihoods['ham']:.2f})")

# A message containing both words, assuming conditional independence given class.
lr_free = vocab["free"]["spam"] / vocab["free"]["ham"]
lr_meeting = vocab["meeting"]["spam"] / vocab["meeting"]["ham"]
prior_odds_spam = p_spam / (1 - p_spam)
post_odds = prior_odds_spam * lr_free * lr_meeting
print(f"\nprior odds spam          = {prior_odds_spam:.4f}")
print(f"combined likelihood ratio = {lr_free*lr_meeting:.2f}")
print(f"posterior P(spam | both)  = {post_odds/(1+post_odds):.4f}")
```

The naive assumption — that words are independent given the class — is false in
English ("free meeting" is not two independent draws), which is exactly why the method
is called *naive* Bayes. It still works well in practice because the ranking of
messages is usually preserved.

## 7. Output and interpretation

- **The exact screening result.** With 1% prevalence, sensitivity 0.99 and specificity
  0.95, \(\Pr(D\mid +)=0.1667\): about one in six positives is a true case. The test is
  good (\({\rm LR}^{+}=19.8\)) and the disease is rare, so the prior odds of 1:99 are
  multiplied by 19.8 to give 1:5 — still unfavourable. That is the base-rate effect,
  and it is arithmetic, not opinion.
- **The simulation.** In 200,000 simulated people the counts agree with the exact
  answer to within about 0.002, which is the simulation's standard error. Out of every
  100,000 people, roughly 990 are true positives and 4,950 are false positives: five
  times as many.
- **A second test.** A second independent positive multiplies the odds again, taking
  the probability from 0.167 to about 0.80. Two tests are far more informative than one
  because the likelihood ratio compounds — and the calculation is only valid if the
  tests' errors are independent.
- **Conditioning in a table.** The overall internship rate is a weighted average of the
  programme-specific rates, and the weights are the programme shares. The same numbers
  answer two different questions: \(\Pr(\text{internship}\mid\text{programme})\) for
  "how does each programme do?", and \(\Pr(\text{programme}\mid\text{internship})\) for
  "who gets the internships?". They are not interchangeable.
- **The spam filter.** "free" is strong evidence (likelihood ratio 12), "meeting" is
  evidence against spam (ratio 0.25), and the message with both lands at a posterior
  above 0.9 — the same odds arithmetic as the medical test, with words instead of
  symptoms.

## 8. Visualisation

```python
import matplotlib.pyplot as plt

prevalences = np.logspace(-4, -0.3, 200)
posteriors = (sensitivity * prevalences) / (
    sensitivity * prevalences + (1 - specificity) * (1 - prevalences))

fig, axes = plt.subplots(1, 2, figsize=(11, 3.9))

axes[0].plot(prevalences * 100, posteriors, linewidth=2, color="#4c72b0")
axes[0].axhline(0.5, color="grey", linestyle=":", linewidth=1)
axes[0].axvline(1.0, color="#c44e52", linestyle="--", linewidth=1)
axes[0].scatter([1.0], [p_d_given_pos], color="#c44e52", zorder=3)
axes[0].annotate(f"1% prevalence: {p_d_given_pos:.2f}", xy=(1.0, p_d_given_pos),
                 xytext=(2.0, 0.35), fontsize=9,
                 arrowprops={"arrowstyle": "->", "color": "#c44e52"})
axes[0].set(xscale="log", xlabel="Prevalence (%)", ylabel="P(disease | positive test)",
            title="A positive test means little when the disease is rare")
axes[0].grid(alpha=0.3)

per_100k = 100_000
groups = pd.Series({
    "true positive": prevalence * sensitivity * per_100k,
    "false positive": (1 - prevalence) * (1 - specificity) * per_100k,
    "true negative": (1 - prevalence) * specificity * per_100k,
    "false negative": prevalence * (1 - sensitivity) * per_100k,
})
axes[1].bar(range(len(groups)), groups.values, color=["#c44e52", "#dd8452", "#55a868", "#4c72b0"])
axes[1].set_xticks(range(len(groups)))
axes[1].set_xticklabels(groups.index, rotation=20, ha="right", fontsize=9)
axes[1].set(ylabel="People per 100,000",
           title="The four outcomes, scaled to 100,000 people")
fig.tight_layout()
plt.show()

print(groups.round(1).to_string())
```

**What to look at.** The left panel shows the posterior rising with prevalence: at 0.01%
a positive is almost certainly false; by 5% it is roughly a coin flip; by 30% it is
strong evidence. The test has not changed — only the prior has. The right panel makes
the arithmetic concrete: the orange bar (false positives) is five times the red bar
(true positives) even though the test is "99% accurate".

## 9. Practical scenario

**Fraud alerts.** A bank's rule flags 2% of transactions. Of flagged transactions, 8%
are fraudulent; of unflagged, 0.2% are. The bank wants to know the precision of an
alert and the share of fraud it catches.

```python
p_flag = 0.02
p_fraud_given_flag = 0.08
p_fraud_given_none = 0.002

p_fraud = p_flag * p_fraud_given_flag + (1 - p_flag) * p_fraud_given_none
p_flag_given_fraud = p_fraud_given_flag * p_flag / p_fraud

print(f"P(fraud)                 = {p_fraud:.5f}")
print(f"precision of an alert    = {p_fraud_given_flag:.3f}")
print(f"share of fraud caught    = {p_flag_given_fraud:.4f}")
print(f"alerts per true fraud    = {1/p_fraud_given_flag:.1f}")
```

The alert is precise (8% of alerts are fraud, thousands of times the base rate) and
catches roughly half of all fraud. Both numbers matter: precision without recall lets
fraud through, recall without precision floods an investigation team. A model's
threshold moves the operating point along this trade-off, which is the subject of
Practical 18.

## 10. Exercises

**Exercise 1.** A test has sensitivity 0.90, specificity 0.98, prevalence 0.02. Compute
\(\Pr(D\mid +)\) and the positive likelihood ratio.

**Exercise 2.** Using the same test, compute \(\Pr(D\mid -)\), the probability a
negative result is wrong.

**Exercise 3.** In the internship table, compute
\(\Pr(\text{DS}\mid\text{internship})\) and compare it with
\(\Pr(\text{internship}\mid\text{DS})\). Explain the difference in one sentence.

**Exercise 4.** A spam filter has prior \(\Pr(\text{spam})=0.5\) and a word with
likelihood ratio 8 for spam. What is the posterior probability of spam?

**Exercise 5.** Two conditionally independent tests each have likelihood ratio 15.
Starting from prior odds 1:50, what is the posterior probability after one positive and
after two?

## 11. Solutions

```python
# Solution 1
s, c, pi = 0.90, 0.98, 0.02
p_pos = s * pi + (1 - c) * (1 - pi)
p_d_pos = s * pi / p_pos
print(f"P(+) = {p_pos:.5f}")
print(f"P(D | +) = {p_d_pos:.4f}")
print(f"LR+ = {s / (1 - c):.1f}")
```

```python
# Solution 2
p_neg_given_d = 1 - s
p_neg_given_not_d = c
p_neg = p_neg_given_d * pi + p_neg_given_not_d * (1 - pi)
p_d_neg = p_neg_given_d * pi / p_neg
print(f"P(D | -) = {p_d_neg:.5f}")
print(f"share of negatives that are wrong = {p_d_neg:.3%}")
```

```python
# Solution 3
p_intern_given_ds = df2.loc[df2.programme == "DS", "internship"].mean()
p_ds_given_intern = df2.loc[df2.internship, "programme"].eq("DS").mean()
print(f"P(internship | DS) = {p_intern_given_ds:.4f}")
print(f"P(DS | internship) = {p_ds_given_intern:.4f}")
# The first is a rate within a programme; the second is the composition of the
# internship group. They differ because DS is the larger programme, and because
# P(DS | internship) is weighted by how many DS students there are.
```

```python
# Solution 4
lr = 8
prior_odds = 1.0
post = prior_odds * lr
print(f"posterior odds = {post}, posterior probability = {post/(1+post):.4f}")
```

```python
# Solution 5
lr = 15
prior = 1 / 50
after1 = prior * lr
after2 = after1 * lr
print(f"prior           : {prior:.4f} -> {prior/(1+prior):.4f}")
print(f"after one test  : {after1:.4f} -> {after1/(1+after1):.4f}")
print(f"after two tests : {after2:.4f} -> {after2/(1+after2):.4f}")
```

## 12. Summary

- Conditioning renormalises the sample space: \(\Pr(A\mid B)=\Pr(A\cap B)/\Pr(B)\).
- Bayes' theorem turns \(\Pr(+\mid D)\) into \(\Pr(D\mid +)\); the prior prevalence is
  not optional.
- Odds form separates the evidence (likelihood ratio) from the belief (prior odds), and
  makes sequential updating multiplicative.
- A test's accuracy is not its predictive value: with rare outcomes, most positives are
  false positives.
- Conditional independence is an assumption to be argued; correlated tests add less
  information than the multiplication suggests.

Next: [Practical 08](08-random-variables-and-expectation.ipynb) formalises random
variables, expectation and variance.
