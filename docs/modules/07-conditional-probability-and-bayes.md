---
title: "M07 — Conditional Probability and Bayes' Theorem"
description: How information changes probability, what independence really claims, and how to reverse a conditional correctly.
module: 7
part: 2
level: Core
hours: 14
prerequisites: [6]
---

# M07 · Conditional Probability and Bayes' Theorem

<div class="psds-meta" markdown>
<span class="psds-chip psds-chip--core">Core</span>
<span class="psds-chip">Part II · Probability</span>
<span class="psds-chip">14 study hours</span>
<span class="psds-chip">Module 7 of 18</span>
</div>

## Introduction

All the interesting probability in the world is conditional. "The chance of rain" is
meaningless; "the chance of rain given that it is cloudy" is a forecast.

Conditional probability formalises what happens to a probability model when you learn
something. The definition is one line — \(\Pr(A\mid B) = \Pr(A\cap B)/\Pr(B)\) — and
it is a renormalisation: knowledge that \(B\) occurred restricts the sample space to
\(B\), and the probabilities inside must be rescaled so they sum to one again.

From that definition two things follow that carry most of applied statistics. The
**law of total probability** lets you compute a probability by partitioning the
world into cases. **Bayes' theorem** lets you reverse a conditional — turning
\(\Pr(\text{positive test} \mid \text{disease})\) into
\(\Pr(\text{disease} \mid \text{positive test})\). That reversal is the single most
consequential idea in this part, and getting it wrong is the most common quantitative
error in medicine, law and machine learning.

## Why this matters

**Base rates dominate.** A test with 99% sensitivity and 99% specificity, applied to a
disease with 0.1% prevalence, yields a positive predictive value near 9%. Most
positive results are false positives. This is not a paradox; it is Bayes' theorem,
and it explains why screening programmes for rare conditions generate anxiety at
scale.

**Conditioning changes what is true.** Two variables can be independent and become
dependent given a third (explaining-away), or dependent and become independent given
a third. Ignoring this produces models that look fine on average and fail on
subgroups.

**Independence is an assumption with consequences.** Naive Bayes assumes conditional
independence of features given the class. It is usually false. It often works. Knowing
why requires this module.

## Learning objectives

By the end of this module you can:

1. Define conditional probability and justify it as a renormalisation of the measure.
2. Apply the multiplication rule to chains: \(\Pr(A\cap B\cap C)=\Pr(A)\Pr(B\mid A)\Pr(C\mid A\cap B)\).
3. Use the law of total probability with a partition, and represent it as a tree.
4. Test independence from a definition, and distinguish pairwise from mutual
   independence with a counterexample.
5. Explain conditional independence, give an example where it differs from
   independence, and explain "explaining away".
6. Derive Bayes' theorem from the definition and the law of total probability.
7. Identify prior, likelihood, evidence and posterior in an applied problem.
8. Compute posterior odds as prior odds × likelihood ratio.
9. Solve diagnostic-testing problems and quantify the base-rate fallacy.
10. Explain naive Bayes as Bayes' theorem plus a conditional-independence assumption,
    and why it works despite the assumption failing.
11. Update sequentially and show that the order of evidence does not change the final
    posterior.
12. Recognise the prosecutor's fallacy and the inversion error in published claims.

## Prerequisites

| Need | From | Revise before |
|---|---|---|
| Axioms, addition rule, independence definition | [M06](06-probability-fundamentals.md) | Units 2, 5 |
| Sets and partitions | [M02](02-mathematical-foundations.md) | Unit 1 |
| Combinatorial probability (for the worked examples) | [M05](05-counting-and-combinatorics.md) | Unit 3 |
| Conditional proportions in a two-way table | [M03](03-data-and-descriptive-statistics.md) | Unit 8 |

## Topic breakdown

### Unit 1 — Conditioning as renormalisation (2 h)

- Definition and intuition: restrict to \(B\), rescale by \(\Pr(B)\).
- Why \(\Pr(\cdot\mid B)\) is itself a probability measure (it satisfies all three
  axioms).
- Reading a two-way table as conditional distributions: row versus column
  percentages.
- The chain rule for three or more events.
- **Worked trap:** equally likely outcomes stop being equally likely after
  conditioning when you condition on information that changes the space.

### Unit 2 — Partitions and total probability (2.5 h)

- Partition: mutually exclusive, exhaustive events.
- Law of total probability: \(\Pr(A)=\sum_i \Pr(A\mid B_i)\Pr(B_i)\).
- Tree diagrams as bookkeeping: multiply along branches, add across.
- Choosing the partition: by cause, by group, by time.
- Simpson's paradox revisited as a failure of aggregation (M03 link).
- Reverse trees: computing a conditional by summing over the other branch.

### Unit 3 — Independence and conditional independence (2.5 h)

- Independence: \(\Pr(A\cap B)=\Pr(A)\Pr(B)\); equivalently
  \(\Pr(A\mid B)=\Pr(A)\) when \(\Pr(B)>0\).
- Independence of \(n\) events (mutual): every subcollection factorises.
- Pairwise independence without mutual independence — explicit construction with two
  coin tosses and a parity event.
- Conditional independence: \(A \indep B \mid C\).
- Independence does not imply conditional independence, and vice versa: both
  counterexamples, both drawn.
- Explaining away: a cause becomes less likely once another cause is observed.

### Unit 4 — Bayes' theorem (3 h)

- Derivation from the definition plus total probability.
- Prior, likelihood, marginal likelihood (evidence), posterior.
- Odds form: posterior odds = prior odds × likelihood ratio.
- Sequential updating and order-invariance.
- Natural frequencies versus conditional probabilities: why "10 in 1,000" is easier
  to reason with than "1%".
- Diagnostic testing: sensitivity, specificity, prevalence, PPV, NPV.
- **Worked computation:** 99%/99% test, 0.1% prevalence → PPV ≈ 9%.

### Unit 5 — Bayesian reasoning in practice (2 h)

- Naive Bayes classification: posterior class probabilities from feature likelihoods.
- Laplace smoothing and why it is needed.
- Why a false independence assumption can still rank cases well.
- Spam filtering as the canonical worked example.
- Beta–Bernoulli updating as a preview of M18 conjugacy.
- Common fallacies: base-rate neglect, prosecutor's fallacy, confusion of the
  conditional (transposed conditional).

### Unit 6 — Simulation of conditional models (2 h)

- Simulating a partitioned population and verifying total probability.
- Monty Hall: full enumeration, conditioning argument, and 10⁵-trial simulation.
- Simulating a screening programme to reproduce the PPV.
- Checking sequential Bayesian updating numerically.
- Reporting the Monte Carlo error alongside the estimate.

## Important mathematical concepts

**Conditional probability.**

\[ \Pr(A\mid B) = \frac{\Pr(A\cap B)}{\Pr(B)}, \qquad \Pr(B) > 0 \]

**Law of total probability** for a partition \(\{B_1,\dots,B_k\}\):

\[ \Pr(A) = \sum_{i=1}^{k} \Pr(A\mid B_i)\,\Pr(B_i) \]

**Bayes' theorem.**

\[ \Pr(B_j\mid A) = \frac{\Pr(A\mid B_j)\,\Pr(B_j)}{\sum_{i}\Pr(A\mid B_i)\,\Pr(B_i)} \]

**Odds form** — the version to use in your head:

\[ \underbrace{\frac{\Pr(H\mid E)}{\Pr(H^c\mid E)}}_{\text{posterior odds}}
   = \underbrace{\frac{\Pr(H)}{\Pr(H^c)}}_{\text{prior odds}}
   \times \underbrace{\frac{\Pr(E\mid H)}{\Pr(E\mid H^c)}}_{\text{likelihood ratio}} \]

*In words:* evidence multiplies your prior odds by how much more likely the evidence is
under the hypothesis than under its alternative. Evidence that is equally likely
either way changes nothing.

## Expected knowledge after completion

You can, without notes:

- Compute a PPV from sensitivity, specificity and prevalence in under a minute, and
  explain the result to a non-specialist.
- Write the multiplication rule for a three-stage process and compute it.
- Construct two events that are independent but not conditionally independent.
- Explain why a 99% accurate test can be wrong most of the time it is positive.
- Say precisely what naive Bayes assumes and what happens when the assumption fails.

## Connections to Data Science

- **Classifier calibration** is a conditional probability: \(\Pr(Y=1\mid \hat{p}=p)\).
- **Precision and recall** in an imbalanced problem are the PPV/sensitivity story.
- **Naive Bayes**, the classical baseline, is this module in six lines of code.
- **Bayesian A/B testing** (M18) is sequential updating with a decision rule.
- **Causal graphs** use conditional independence as their language: a path is blocked
  given a set of variables.

## Practical applications

| Setting | Question | Method |
|---|---|---|
| Medical screening | Given a positive result, what is the chance of disease? | Bayes with prevalence |
| Spam filtering | Is this message spam given these words? | Naive Bayes |
| Fraud alerts | Why do most alerts turn out benign? | Base rate and PPV |
| Quality inspection | Probability a defect came from line B? | Total probability + Bayes |
| Court evidence | Is "1 in a million" the probability of innocence? | Prosecutor's fallacy |

## Exercises and assessment plan

| Component | Count | Focus |
|---|---|---|
| ★ Drill | 8 | Conditional computation from tables |
| ★★ Application | 7 | Tree diagrams; diagnostic testing; naive Bayes by hand |
| ★★★ Challenge | 4 | Independence counterexamples; proving order-invariance; PPV paradox; simulate a screening programme |
| Quiz | 10 items | Interpretation, including three fallacy items |
| Practical notebook | 1 | Bayes updater for a diagnostic test and a spam filter |
| Simulation lab | 1 | Monty Hall: enumerate, condition, simulate, reconcile |

## Recommended study sequence

| Session | Focus | Hours |
|---|---|---|
| 1 | Unit 1: conditioning and tables | 2.0 |
| 2 | Unit 2: partitions and trees | 2.5 |
| 3 | Unit 3: independence, both kinds | 2.5 |
| 4 | Unit 4: Bayes' theorem and diagnostics | 3.0 |
| 5 | Unit 5: naive Bayes and fallacies | 2.0 |
| 6 | Unit 6: simulation | 2.0 |

**Before this module:** [M06](06-probability-fundamentals.md). **After:**
[M08 — Random Variables and Expectation](08-random-variables-and-expectation.md)
applies conditioning to whole distributions rather than single events.
