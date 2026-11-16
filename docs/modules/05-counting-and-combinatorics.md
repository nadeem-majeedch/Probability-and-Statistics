---
title: "M05 — Counting and Combinatorics"
description: Permutations, combinations, multinomial counts and inclusion–exclusion — the arithmetic of equally likely outcomes.
module: 5
part: 2
level: Beginner
hours: 10
prerequisites: [2, 4]
---

# M05 · Counting and Combinatorics

<div class="psds-meta" markdown>
<span class="psds-chip psds-chip--beginner">Beginner</span>
<span class="psds-chip">Part II · Probability</span>
<span class="psds-chip">10 study hours</span>
<span class="psds-chip">Module 5 of 18</span>
</div>

## Introduction

When outcomes are equally likely, probability is counting:

\[ \Pr(A) = \frac{\text{number of outcomes in } A}{\text{number of outcomes in } \Omega} \]

Everything hard about this formula is in the numerator and denominator. Students who
"cannot do probability" usually cannot count — not because counting is difficult, but
because the same physical situation admits several correct-looking counts, and only
one of them matches the sample space you actually defined.

This module builds the four counting machines and, more importantly, the habit of
**defining the sample space before counting**. It ends with the classic traps
(birthday, occupancy, derangements) and with exhaustive enumeration in Python, which
settles disputes that argument cannot.

## Why this matters

Counting is the foundation of discrete probability. Binomial coefficients reappear in
the binomial distribution (M09), in the hypergeometric (M09), in the number of
subsets in a bootstrap resample (M18), and in the multiplicity corrections of M15.

The deeper reason is methodological. The single most common error in combinatorial
probability is **not** arithmetic: it is counting outcomes that are not equally
likely as though they were. Distinguishable versus indistinguishable, ordered versus
unordered, with or without replacement — each choice changes the denominator. Getting
that right is a modelling skill, and it transfers directly to defining sample spaces
in M06 and to designing simulations later.

## Learning objectives

By the end of this module you can:

1. Apply the multiplication principle and construct a tree diagram for a multi-stage
   process.
2. Count arrangements with and without repetition: \(n!\), \(nPr\), \(n^{r}\).
3. Count selections with the binomial coefficient, and decide whether order matters
   in a stated problem — then justify the decision.
4. Distinguish distinguishable from indistinguishable objects and count both.
5. Count permutations of a multiset (the multinomial coefficient) and distributions of
   identical objects into distinct boxes (stars and bars).
6. Apply inclusion–exclusion for two and three events and derive \(|A \cup B|\).
7. Use the pigeonhole principle in simple arguments.
8. Count via complement and via conditioning, and choose the cheaper route
   deliberately.
9. Compute exact probabilities for equally likely outcomes and verify them by
   exhaustive enumeration in Python.
10. Explain why enumeration fails at scale, motivating simulation (M18).

## Prerequisites

| Need | From | Revise before |
|---|---|---|
| Factorials; product notation \(\prod\) | [M02](02-mathematical-foundations.md) | Unit 4 |
| Summation and index manipulation | M02 | Unit 3 |
| Sets: union, intersection, complement | M02 | Unit 1 |
| The habit of looking at data before concluding | [M04](04-data-visualization.md) | — |

## Topic breakdown

### Unit 1 — The multiplication principle (1.5 h)

- Sequential choices: if stage \(k\) has \(m_k\) options, the total is
  \(m_1 m_2 \cdots m_k\).
- Tree diagrams as the honest picture of the sample space.
- When the principle fails: choices that are not independent of earlier ones.
- Counting the complement: sometimes "not" is easier than "yes".
- **Rule of practice:** write the sample space for small cases by hand before
  generalising.

### Unit 2 — Arrangements (2 h)

- Permutations of \(n\) distinct objects: \(n!\).
- \(k\)-permutations: \(n(n-1)\cdots(n-k+1) = n!/(n-k)!\).
- Arrangements with repetition allowed: \(n^{r}\).
- Circular arrangements: \((n-1)!\), and why the first seat is fixed.
- Arrangements of a multiset: \(n!/(n_1! n_2! \cdots n_k!)\).
- Distinguishable versus identical objects — the recurring trap.

### Unit 3 — Selections (2 h)

- Combinations: \(\binom{n}{k} = n!/(k!(n-k)!)\), and the meaning of "order does not
  matter".
- The symmetry \(\binom{n}{k} = \binom{n}{n-k}\), and Pascal's rule.
- The binomial theorem and where the coefficients come from.
- Stars and bars: distributing \(n\) identical objects into \(k\) distinct boxes,
  \(\binom{n+k-1}{k-1}\); with non-empty boxes, replace \(n\) by \(n-k\).
- Sampling without replacement from a finite population — the setup for the
  hypergeometric distribution in M09.

### Unit 4 — Inclusion and exclusion (1.5 h)

- Two sets: \(|A\cup B| = |A|+|B|-|A\cap B|\).
- Three sets, and the general alternating sum.
- Counting "at least one" via the complement of "none".
- Derangements as the canonical application: \(!n = n!\sum_{k=0}^{n}(-1)^k/k!\).
- The pigeonhole principle: proofs of existence, and the birthday problem's setup.

### Unit 5 — Classic models and traps (1.5 h)

- Birthday problem: \(\Pr(\text{all distinct}) = \frac{365\cdot364\cdots(365-n+1)}{365^n}\);
  \(n=23\) gives \(\Pr \approx 0.507\).
- Occupancy: balls into boxes, collisions, and the coupon-collector preview.
- The two-children problem and the role of how you learned the information.
- The Monty Hall reversal as a counting problem with unequal probabilities (resolved
  properly in M07).
- **The failure mode:** counting distinguishable outcomes as indistinguishable (or the
  reverse) and thereby changing the measure.

### Unit 6 — Counting with code (2 h)

- `math.comb`, `math.perm`, `itertools.product`, `permutations`, `combinations`.
- Exhaustive enumeration of a small sample space; comparing the count with the closed
  form.
- Randomised verification: simulate and compare frequencies with exact probabilities.
- Timing: how quickly enumeration becomes impossible (e.g. \(2^{30}\) subsets), and
  what replaces it.

## Important mathematical concepts

**Binomial coefficient and the binomial theorem.**

\[ \binom{n}{k} = \frac{n!}{k!\,(n-k)!}, \qquad
   (x+y)^{n} = \sum_{k=0}^{n}\binom{n}{k}x^{k}y^{n-k} \]

**Stars and bars.**

\[ \#\{(x_1,\dots,x_k) : x_i \ge 0,\; \textstyle\sum x_i = n\} = \binom{n+k-1}{k-1} \]

**Inclusion–exclusion for three sets.**

\[ |A\cup B\cup C| = |A|+|B|+|C| - |A\cap B| - |A\cap C| - |B\cap C| + |A\cap B\cap C| \]

**Birthday probability.**

\[ \Pr(\text{no shared birthday among } n) = \prod_{i=0}^{n-1}\left(1-\frac{i}{365}\right) \]

## Expected knowledge after completion

You can, without notes:

- Given a word problem, state the sample space, say whether order matters, and name
  the counting rule — before computing.
- Compute \(\binom{52}{5}\), the number of poker hands, and the probability of a flush.
- Explain why the birthday problem's answer is smaller than intuition suggests.
- Distribute 10 identical items into 4 boxes in \(\binom{13}{3}\) ways and explain
  each symbol.
- Write a five-line Python loop that verifies a counting answer exactly.

## Connections to Data Science

- **Feature subsets**: \(2^{p}\) possible subsets is why exhaustive feature selection
  is infeasible beyond about 20 predictors.
- **Bootstrap resampling**: the number of distinct resamples and the collision
  structure connect to the birthday problem.
- **Hypergeometric thinking** underlies "how surprising is this overlap between two
  gene lists or two customer segments".
- **Hash collisions** in data engineering are the birthday problem at scale.
- **Multiple comparisons** begin with counting how many tests you ran.

## Practical applications

| Setting | Question | Counting tool |
|---|---|---|
| Lottery or card game | What is the probability of this hand? | Combinations |
| Password policy | How large is the space? | \(n^{r}\) with and without repetition |
| A/B test assignment | How many distinct allocations? | Multinomial coefficients |
| Data quality | Probability two records collide on a key? | Birthday/occupancy |
| Quality control | Probability a batch contains no defectives? | Hypergeometric count |

## Exercises and assessment plan

| Component | Count | Focus |
|---|---|---|
| ★ Drill | 10 | Direct counting with the correct rule |
| ★★ Application | 6 | "Which rule applies and why", then compute |
| ★★★ Challenge | 3 | Prove a combinatorial identity; derangements; a simulation check |
| Quiz | 10 items | Model selection over formulas |
| Practical notebook | 1 | Enumeration versus closed form versus simulation for three problems |

## Recommended study sequence

| Session | Focus | Hours |
|---|---|---|
| 1 | Units 1–2: multiplication rule, arrangements | 2.5 |
| 2 | Unit 3: selections and stars and bars | 2.5 |
| 3 | Unit 4: inclusion–exclusion, pigeonhole | 2.0 |
| 4 | Unit 5: classic models and traps | 2.0 |
| 5 | Unit 6: counting with code; exercises | 1.0 |

**Before this module:** [M02](02-mathematical-foundations.md),
[M04](04-data-visualization.md). **After:** [M06 — Probability
Fundamentals](06-probability-fundamentals.md) turns counting into a measure.
