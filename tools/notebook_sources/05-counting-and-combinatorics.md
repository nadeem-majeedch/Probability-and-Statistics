# Practical 05 — Counting and Combinatorics

## 1. Introduction

Counting is how probability gets its denominators. "Three of the ten students" is a
statement about a set; "the probability of a full house" needs the number of five-card
hands, which is 2,598,960, and no amount of simulation replaces knowing why.

This practical derives the counting rules, then **checks every formula by brute force
enumeration** on small cases. If `math.comb(5, 2)` says 10 and `itertools` also finds
10 pairs, the formula is right for that case and you know what it means. Then the same
rules are applied to a birthday-problem simulation, where exact counting becomes
impractical and simulation takes over.

## 2. Learning objectives

By the end of this practical you can:

1. Apply the multiplication rule to multi-stage experiments.
2. Distinguish permutations from combinations, and with from without replacement.
3. Verify a counting formula by exhaustive enumeration.
4. Compute the birthday-problem probability exactly and by simulation.
5. Explain why a "1 in 14 million" lottery ticket and a hash collision have the same
   underlying count.

## 3. Required libraries

| Library | Used for |
|---|---|
| `math` | `factorial`, `comb`, `perm` |
| `itertools` | exhaustive enumeration of small cases |
| `numpy` | seeded simulation |
| `matplotlib` | birthday curve |

## 4. Concepts

### 4.1 The multiplication rule

If a procedure has \(n_1\) outcomes at stage 1, \(n_2\) at stage 2, and so on, the
number of outcome sequences is \(n_1n_2\cdots n_k\). A four-digit PIN has
\(10^4=10{,}000\) codes; three dice have \(6^3=216\) ordered outcomes.

### 4.2 Ordered or not, repeated or not

Two questions decide the formula:

1. **Does order matter?** A password `1234` differs from `4321`; a committee of four
   does not change when listed alphabetically.
2. **Can items repeat?** Choosing three people is without replacement; choosing three
   digits with repetition allowed is not.

| | Without replacement | With replacement |
|---|---|---|
| **Order matters** | \({}_nP_r=\dfrac{n!}{(n-r)!}\) | \(n^{r}\) |
| **Order ignored** | \(\dbinom{n}{r}=\dfrac{n!}{r!(n-r)!}\) | \(\dbinom{n+r-1}{r}\) |

The last cell is *stars and bars*: the number of ways to choose \(r\) items from \(n\)
types when repeats are allowed and order is irrelevant.

### 4.3 Why combinations appear in probability

When every outcome is equally likely, a probability is a ratio of counts:

\[ \Pr(A)=\frac{\#A}{\#\Omega}. \]

For a five-card hand, \(\#\Omega=\binom{52}{5}=2{,}598{,}960\). Each hand is equally
likely, so counting hands is the whole calculation. This is why \(\binom{n}{r}\)
appears in the binomial distribution: it counts the orders in which \(r\) successes
can occur among \(n\) trials.

### 4.4 The birthday problem

With \(n\) people, the probability that all birthdays differ is

\[ \Pr(\text{all distinct})=\prod_{k=1}^{n-1}\left(1-\frac{k}{365}\right), \]

so the probability of at least one shared birthday is one minus that product. The
product is the multiplication rule applied to "the second person avoids the first,
the third avoids both, ...".

## 5. Formulas

\[ {}_nP_r=\frac{n!}{(n-r)!},\qquad
   \binom{n}{r}=\frac{n!}{r!\,(n-r)!},\qquad
   \binom{n}{r}=\binom{n}{n-r} \]

\[ \Pr(\text{at least one match})=1-\prod_{k=1}^{n-1}\frac{365-k}{365} \]

\[ \binom{n}{0}=\binom{n}{n}=1,\qquad
   \sum_{r=0}^{n}\binom{n}{r}=2^{n} \]

The last identity counts every subset of an \(n\)-element set: for each element there
are two choices, in or out.

## 6. Implementation

### 6.1 Four counting rules, side by side

```python
from math import comb, perm, factorial
import itertools as it
import numpy as np
import matplotlib.pyplot as plt

n, r = 6, 3
print("n =", n, " r =", r)
print(f"ordered,   with replacement : {n**r}")
print(f"ordered,   without          : {perm(n, r)}")
print(f"unordered, without          : {comb(n, r)}")
print(f"unordered, with replacement : {comb(n + r - 1, r)}")
print(f"check factorial identity    : {perm(n, r) == factorial(n) // factorial(n - r)}")
```

### 6.2 Every formula checked by enumeration

```python
items = list("ABCDEF")

ordered_no_replace = list(it.permutations(items, r))
unordered_no_replace = list(it.combinations(items, r))
ordered_with_replace = list(it.product(items, repeat=r))

print(f"permutations('ABCDEF', 3) enumerated : {len(ordered_no_replace)}")
print(f"combinations('ABCDEF', 3) enumerated : {len(unordered_no_replace)}")
print(f"product('ABCDEF', repeat=3) enumerated: {len(ordered_with_replace)}")
print("first three permutations :", ordered_no_replace[:3])
print("all ten combinations     :", unordered_no_replace[:10])
```

Enumeration is only possible for small \(n\); its value is to confirm the formula once,
so that you can trust it at \(n=52\).

### 6.3 A committee problem, counted two ways

How many ways can a committee of 3 be chosen from 10 students, and how many of those
committees contain a particular student (call her Aisha)?

```python
total = comb(10, 3)
with_aisha = comb(9, 2)
print(f"all committees          : {total}")
print(f"containing Aisha        : {with_aisha}")
print(f"not containing Aisha    : {comb(9, 3)}")
print(f"sum check               : {with_aisha + comb(9, 3) == total}")
print(f"probability Aisha serves: {with_aisha / total:.4f}   (= 3/10 = {3/10:.4f})")
```

The identity \(\binom{9}{2}+\binom{9}{3}=\binom{10}{3}\) is Pascal's rule. The
probability 3/10 has a shortcut: each of the 10 students is equally likely to occupy
any of the 3 seats.

### 6.4 Poker hands

```python
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["S", "H", "D", "C"]
deck = [(v, s) for v in values for s in suits]
print("deck size:", len(deck))

hands = comb(52, 5)
flushes = 4 * comb(13, 5)
straight_flushes = 4 * 10
print(f"five-card hands          : {hands:,}")
print(f"flushes (any suit)       : {flushes:,}")
print(f"straight flushes         : {straight_flushes}")
print(f"P(flush, including SF)   : {flushes / hands:.6f}")
print(f"P(straight flush)        : {straight_flushes / hands:.8f}")
```

A **flush** here includes straight flushes, as the conventional count does before
subtracting them. Every probability is a ratio of two exact integers, so the sixth
decimal is meaningful — unlike a simulation with 10,000 hands, whose standard error is
about 0.0002.

### 6.5 The birthday problem: exact and simulated

```python
def birthday_exact(n_people, days=365):
    """Probability that at least two of n_people share a birthday."""
    p_all_distinct = 1.0
    for k in range(n_people):
        p_all_distinct *= (days - k) / days
    return 1 - p_all_distinct


for n_people in (10, 20, 23, 30, 40, 50, 60):
    print(f"n = {n_people:2d}   P(shared birthday) = {birthday_exact(n_people):.4f}")
```

```python
rng = np.random.default_rng(2026)
reps = 5000
sim = {}
for n_people in (10, 23, 30, 50):
    matches = 0
    for _ in range(reps):
        bdays = rng.integers(0, 365, size=n_people)
        if len(np.unique(bdays)) < n_people:
            matches += 1
    sim[n_people] = matches / reps

print(f"{'n':>4} {'exact':>8} {'simulated':>10} {'difference':>11}")
for n_people, p in sim.items():
    exact = birthday_exact(n_people)
    print(f"{n_people:>4} {exact:>8.4f} {p:>10.4f} {p - exact:>+11.4f}")
print(f"\nsimulation standard error (n=23): "
      f"{np.sqrt(birthday_exact(23) * (1 - birthday_exact(23)) / reps):.4f}")
```

### 6.6 With repetition: stars and bars

How many ways can 5 identical prizes be distributed among 3 students, allowing a
student to receive none?

```python
ways = comb(5 + 3 - 1, 5)
print("distributions of 5 identical prizes among 3 students:", ways)

# Enumerate to confirm: each distribution is a triple summing to 5.
solutions = [(a, b, 5 - a - b) for a in range(6) for b in range(6 - a)]
print("enumerated:", len(solutions), " first five:", solutions[:5])
```

## 7. Output and interpretation

- **The four rules.** For \(n=6, r=3\): 216 ordered with replacement, 120 ordered
  without, 20 unordered without, 56 unordered with. The ratios are what you would
  expect — allowing repetition multiplies the count, and ignoring order divides it by
  \(r!=6\).
- **Enumeration agrees.** 120, 20 and 216 are exactly what `itertools` produced. The
  formulas are not approximations; they are counts, and now you have seen them counted.
- **Committees.** 120 committees, 36 of which contain Aisha, giving probability 0.3.
  The complement agrees: 84 of 120 do not contain her, and 36 + 84 = 120.
- **Poker.** 2,598,960 hands; 5,148 flushes including straight flushes, so
  \(\Pr(\text{flush})\approx0.00198\), about 1 in 505. Straight flushes are 40 of
  2,598,960, about 1 in 64,974.
- **Birthdays.** The exact curve crosses 0.5 at 23 people (0.5073), and reaches 0.97 at
  50 (0.9704). The simulation at 5,000 replications agrees to within about 0.007, which
  is the size of its standard error at \(n=23\) (0.0071). Agreement at that level is
  all a simulation can promise.

## 8. Visualisation

```python
ns = np.arange(1, 71)
probs = np.array([birthday_exact(k) for k in ns])

fig, ax = plt.subplots(figsize=(6.6, 3.9))
ax.plot(ns, probs, linewidth=2, color="#4c72b0")
ax.axhline(0.5, color="grey", linestyle=":", linewidth=1)
ax.axvline(23, color="#c44e52", linestyle="--", linewidth=1)
ax.annotate("23 people: P = 0.507", xy=(23, 0.507), xytext=(30, 0.35),
            arrowprops={"arrowstyle": "->", "color": "#c44e52"})
ax.set(xlabel="Number of people", ylabel="P(at least one shared birthday)",
       title="The birthday probability rises much faster than intuition suggests")
ax.grid(alpha=0.3)
fig.tight_layout()
plt.show()
```

**What to look at.** The curve is steep between 15 and 40 people, then flattens towards
1. The reason is that the number of *pairs* grows like \(n^{2}\), not \(n\): at 23
people there are 253 pairs, each with a 1/365 chance of matching. Intuition fails
because it compares 23 people with 365 days, while the relevant quantity is 253
comparisons.

## 9. Practical scenario

**Duplicate identifiers.** A data pipeline generates an 8-character identifier from 62
characters (letters and digits). How many identifiers exist, and how many records can
be stored before a duplicate becomes likely?

```python
space = 62 ** 8
print(f"identifier space: {space:,} (~{space:.2e})")

# Same birthday mathematics: probability of a collision among n ids.
def collision_prob(n_ids, space):
    p_distinct = 1.0
    for k in range(n_ids):
        p_distinct *= (space - k) / space
    return 1 - p_distinct

for n_ids in (10_000, 100_000, 1_000_000):
    print(f"n = {n_ids:>9,}   P(collision) = {collision_prob(n_ids, space):.4f}")
```

The square-root rule is the lesson: collisions become likely at about
\(\sqrt{\text{space}}\approx1.5\times10^{7}\) identifiers, not at
\(2\times10^{14}\).
This is the birthday problem in production clothing — the same count, a different
story, and the reason hash functions are long.

## 10. Exercises

**Exercise 1.** A password is 4 lowercase letters followed by 2 digits. How many
passwords are possible? How many if letters may not repeat?

**Exercise 2.** From 12 students, how many ways can a president, secretary and
treasurer be chosen? How many ways can a 3-person committee be chosen?

**Exercise 3.** Verify Pascal's rule \(\binom{12}{5}=\binom{11}{4}+\binom{11}{5}\)
numerically and by enumerating subsets of a 12-element set.

**Exercise 4.** A bag has 4 red and 6 blue balls. How many ways can 3 balls be drawn
without replacement, and how many of those draws contain exactly 2 red balls?

**Exercise 5.** Using the birthday function, find the smallest \(n\) for which the
probability of a shared birthday exceeds 0.99.

## 11. Solutions

```python
# Solution 1
with_repeats = 26**4 * 10**2
without_repeats = perm(26, 4) * 10**2
print(f"with repeats   : {with_repeats:,}")
print(f"no repeat      : {without_repeats:,}")
```

```python
# Solution 2
print(f"officers  : {perm(12, 3)}")
print(f"committee : {comb(12, 3)}")
```

The officer count is 6 times the committee count, because each 3-person committee can
be arranged into 3! = 6 distinct officer assignments.

```python
# Solution 3
print(f"C(12,5) = {comb(12, 5)}")
print(f"C(11,4) + C(11,5) = {comb(11, 4) + comb(11, 5)}")

subsets = list(it.combinations(range(12), 5))
with_zero = [s for s in subsets if 0 in s]
without_zero = [s for s in subsets if 0 not in s]
print(f"enumerated total {len(subsets)}, with 0: {len(with_zero)}, without 0: {len(without_zero)}")
```

```python
# Solution 4
total_draws = comb(10, 3)
two_red = comb(4, 2) * comb(6, 1)
print(f"all draws        : {total_draws}")
print(f"exactly 2 red    : {two_red}")
print(f"probability      : {two_red / total_draws:.4f}")
```

```python
# Solution 5
n_people = 1
while birthday_exact(n_people) <= 0.99:
    n_people += 1
print(f"smallest n with P > 0.99: {n_people} (P = {birthday_exact(n_people):.4f})")
```

## 12. Summary

- The multiplication rule counts sequences; order and replacement decide which formula
  applies.
- \(\binom{n}{r}\) counts unordered selections and is the denominator of most
  equally-likely probability calculations.
- Enumeration on small cases is the fastest way to be sure a formula means what you
  think.
- The birthday problem is about pairs, not people: the probability grows like
  \(n^{2}/365\), so 23 people are enough for a coin flip.
- The same count explains hash collisions and the square-root rule for identifier
  space.

Next: [Practical 06](06-probability-fundamentals.ipynb) puts these counts to work in
simulated coin and dice experiments.
