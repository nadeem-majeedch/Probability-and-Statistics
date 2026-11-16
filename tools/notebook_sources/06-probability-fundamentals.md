# Practical 06 — Random Experiments: Coins and Dice

## 1. Introduction

Probability begins with an experiment: a procedure with a set of possible outcomes.
This practical runs two of the oldest — tossing coins and rolling dice — and uses them
to check the three axioms, the addition rule, independence, and the complement rule.

Every experiment is run three ways: **enumerated** (all outcomes listed), **computed**
(the formula), and **simulated** (many repetitions with a fixed seed). When the three
agree, the theory is confirmed; when the simulation disagrees, either the simulation
or your understanding of the theory is wrong. Both are worth finding out.

## 2. Learning objectives

By the end of this practical you can:

1. Write a sample space and an event as sets, and compute a probability by counting.
2. Verify the axioms and the complement rule numerically.
3. Apply the addition rule for unions and say when \(\Pr(A\cap B)=\Pr(A)\Pr(B)\) holds.
4. Simulate coins and dice and compare the empirical proportion with the exact value.
5. Explain why simulation error shrinks like \(1/\sqrt{n}\), and estimate it.

## 3. Required libraries

| Library | Used for |
|---|---|
| `numpy` | random number generation with a seed |
| `itertools` | enumerating small sample spaces |
| `matplotlib` | running proportions, dice distributions |

## 4. Concepts

### 4.1 Sample space, event, probability

The **sample space** \(\Omega\) is the set of all outcomes. An **event** is a subset.
For equally likely outcomes, \(\Pr(A)=|A|/|\Omega|\). A probability satisfies three
axioms:

1. \(\Pr(A)\ge0\) for every event.
2. \(\Pr(\Omega)=1\).
3. For disjoint events, \(\Pr(A\cup B)=\Pr(A)+\Pr(B)\).

Everything else — complements, the addition rule, conditional probability — is a
consequence.

### 4.2 Two dice, and the most common mistake

Two fair dice have 36 equally likely **ordered** outcomes, from (1,1) to (6,6). The
sums are not equally likely: 7 occurs in 6 of the 36 outcomes, 2 in 1. Treating the
eleven possible sums as equally likely gives \(\Pr(7)=1/11\), which is wrong; the
sample space is pairs, not sums.

### 4.3 Independence

Events \(A\) and \(B\) are independent when

\[ \Pr(A\cap B)=\Pr(A)\Pr(B). \]

Independence is a property of the *mechanism*, not of the numbers: two separate dice
are independent by design; two tosses of the same coin are independent if the coin has
no memory. Mutually exclusive events are **not** independent (unless one has
probability zero) — that confusion is the most common conceptual error in the module.

### 4.4 The law of large numbers, empirically

The running proportion of heads converges to \(p\). The typical error after \(n\)
tosses is

\[ \text{se}=\sqrt{\frac{p(1-p)}{n}}, \]

so quadrupling \(n\) halves the error. This is the first appearance of the
\(1/\sqrt{n}\) law that governs every simulation in the course.

## 5. Formulas

\[ \Pr(A^{c})=1-\Pr(A),\qquad \Pr(A\cup B)=\Pr(A)+\Pr(B)-\Pr(A\cap B) \]

\[ \Pr(A\cap B)=\Pr(A)\Pr(B)\quad\text{(independent)} \]

\[ \Pr(X=k)=\binom{n}{k}p^{k}(1-p)^{n-k}\quad\text{(binomial)} \]

\[ \text{se}(\hat p)=\sqrt{\frac{p(1-p)}{n}},\qquad
   \hat p\pm1.96\,\text{se}\ \text{(approximate 95\% interval)} \]

## 6. Implementation

### 6.1 Enumerating the sample space

```python
import itertools as it
import numpy as np
import matplotlib.pyplot as plt

coins = list(it.product("HT", repeat=3))
print("three coins, sample space:", coins)
print("number of outcomes:", len(coins))

exactly_two_heads = [o for o in coins if o.count("H") == 2]
print("exactly two heads:", exactly_two_heads)
print("P(exactly two heads) =", len(exactly_two_heads) / len(coins))

dice = list(it.product(range(1, 7), repeat=2))
print("\ntwo dice: outcomes =", len(dice))
print("first five:", dice[:5])
sums = [a + b for a, b in dice]
for target in (2, 7, 12):
    count = sums.count(target)
    print(f"P(sum = {target:2d}) = {count}/36 = {count/36:.4f}")
```

### 6.2 Simulation, with a fixed seed

```python
rng = np.random.default_rng(2026)

n_tosses = 10_000
tosses = rng.integers(0, 2, size=n_tosses)   # 0 = tails, 1 = heads
heads = tosses.sum()

print(f"tosses: {n_tosses:,}")
print(f"heads : {heads:,}   proportion = {heads / n_tosses:.4f}")
print(f"exact : 0.5")
print(f"standard error = {np.sqrt(0.25 / n_tosses):.4f}")
print(f"difference     = {heads / n_tosses - 0.5:+.4f}")
```

### 6.3 The running proportion converges

```python
running = np.cumsum(tosses) / np.arange(1, n_tosses + 1)
checkpoints = [10, 100, 1_000, 10_000]
print(f"{'n':>8} {'proportion':>12} {'|error|':>10}")
for k in checkpoints:
    print(f"{k:>8,} {running[k-1]:>12.4f} {abs(running[k-1] - 0.5):>10.4f}")

print(f"\nexpected error at n=10    : {np.sqrt(0.25/10):.4f}")
print(f"expected error at n=10,000: {np.sqrt(0.25/10_000):.4f}")
```

### 6.4 Axioms and the addition rule

```python
A = set(o for o in coins if o.count("H") == 2)      # exactly two heads
B = set(o for o in coins if o[0] == "H")            # first toss is heads
omega = set(coins)

def prob(event, space=omega):
    return len(event & space) / len(space)

print(f"P(A)            = {prob(A):.4f}")
print(f"P(B)            = {prob(B):.4f}")
print(f"P(A or B)       = {prob(A | B):.4f}")
print(f"P(A) + P(B) - P(A and B) = {prob(A) + prob(B) - prob(A & B):.4f}")

print(f"\nP(not A)        = {prob(omega - A):.4f}   (1 - P(A) = {1 - prob(A):.4f})")
print(f"P(A and B)      = {prob(A & B):.4f},  P(A)P(B) = {prob(A)*prob(B):.4f}")
```

The event "exactly two heads" and "first toss heads" are **not** independent here:
their intersection has probability 0.25, while the product of their probabilities is
0.1875. Knowing the first toss was heads *raises* the chance of exactly two heads from
0.375 to 0.5, because one of the two required heads is then already accounted for. Two
separate tosses, by contrast, are independent — Section 6.6 shows that.

### 6.5 Two dice: exact against simulated

```python
rng = np.random.default_rng(11)
n_rolls = 20_000
rolls = rng.integers(1, 7, size=(n_rolls, 2))
sim_sums = rolls.sum(axis=1)

sim_probs = np.array([(sim_sums == s).mean() for s in range(2, 13)])
exact_probs = np.array([sums.count(s) / 36 for s in range(2, 13)])

print(f"{'sum':>3} {'exact':>8} {'simulated':>10} {'diff':>8}")
for s, e, m in zip(range(2, 13), exact_probs, sim_probs):
    print(f"{s:>3} {e:>8.4f} {m:>10.4f} {m - e:>+8.4f}")
print(f"\nmax absolute deviation: {np.abs(sim_probs - exact_probs).max():.4f}")
print(f"typical standard error: {np.sqrt(0.16 / n_rolls):.4f}")
```

### 6.6 Independence versus mutual exclusivity

```python
# Two mutually exclusive events: disjoint, hence strongly dependent.
C = set(o for o in coins if o.count("H") == 0)   # no heads
D = set(o for o in coins if o.count("H") == 3)   # three heads
print(f"P(C) = {prob(C):.4f}, P(D) = {prob(D):.4f}")
print(f"P(C and D) = {prob(C & D):.4f}   P(C)*P(D) = {prob(C)*prob(D):.4f}")
print(f"P(C or D)  = {prob(C | D):.4f}   = P(C)+P(D) = {prob(C)+prob(D):.4f}")
print("\nDisjoint events are dependent: knowing C rules out D entirely.")
```

```python
# Independence in a fair coin: the second toss is unrelated to the first.
first_heads = sum(1 for o in coins if o[0] == "H")
second_heads = sum(1 for o in coins if o[1] == "H")
both_heads = sum(1 for o in coins if o[0] == "H" and o[1] == "H")
print(f"P(first H) = {first_heads/8:.3f}, P(second H) = {second_heads/8:.3f}, "
      f"P(both) = {both_heads/8:.3f}")
print(f"product   = {first_heads/8 * second_heads/8:.3f}")
```

### 6.7 A biased coin

```python
p = 0.7
rng = np.random.default_rng(4)
biased = rng.random(10_000) < p
print(f"biased coin p = {p}")
print(f"simulated proportion of heads = {biased.mean():.4f}")
print(f"standard error                = {np.sqrt(p*(1-p)/10_000):.4f}")

# How many tosses are needed to distinguish p=0.7 from p=0.5 with confidence?
for n in (50, 200, 800):
    se = np.sqrt(p * (1 - p) / n)
    print(f"n = {n:4d}: se = {se:.4f}, 95% CI width = {2*1.96*se:.4f}")
```

## 7. Output and interpretation

- **Exact counts.** Three coins give 8 outcomes and 3 of them have exactly two heads,
  so \(\Pr=0.375\); the simulation prints a proportion within its standard error of
  that value. Two dice give \(\Pr(\text{sum}=7)=6/36=0.1667\), the largest of the
  eleven sums.
- **Convergence.** The running proportion at \(n=10\) can be far from 0.5 (0.8, say),
  and at \(n=10{,}000\) it is within about 0.005. The standard errors printed confirm
  the \(1/\sqrt{n}\) scale: 0.158 at 10, 0.005 at 10,000.
- **Addition rule.** \(\Pr(A\cup B)\) computed by counting the union equals
  \(\Pr(A)+\Pr(B)-\Pr(A\cap B)\). The subtraction is not a technicality: counting
  outcomes in the intersection twice is exactly the error the rule corrects.
- **Independence, checked rather than assumed.** With \(A=\) "exactly two heads" and
  \(B=\) "first toss heads", the intersection contains HHT and HTH, so
  \(\Pr(A\cap B)=0.25\), while \(\Pr(A)\Pr(B)=0.375\times0.5=0.1875\). The two differ,
  so the events are **dependent**: conditioning on a head first raises the probability
  of exactly two heads from 0.375 to 0.5. Two separate tosses, by contrast, are
  independent (0.5 x 0.5 = 0.25 for both heads), which is the contrast Section 6.6
  prints.
- **Disjoint events.** \(C\) and \(D\) have empty intersection but probabilities that
  multiply to a non-zero number, so they are dependent. Mutually exclusive is not the
  same as independent.

## 8. Visualisation

```python
fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))

axes[0].plot(np.arange(1, n_tosses + 1), running, linewidth=1, color="#4c72b0")
axes[0].axhline(0.5, color="#c44e52", linestyle="--", linewidth=1.2, label="p = 0.5")
axes[0].set(xscale="log", xlabel="Number of tosses (log scale)",
            ylabel="Running proportion of heads",
            title="The running proportion settles near p")
axes[0].legend(frameon=False)

axes[1].bar(range(2, 13), exact_probs, color="#dd8452", edgecolor="white",
            label="exact")
axes[1].plot(range(2, 13), sim_probs, "o", color="black", markersize=4,
             label="simulated")
axes[1].set(xlabel="Sum of two dice", ylabel="Probability",
            title="Triangular, not flat: 7 is the most likely sum")
axes[1].legend(frameon=False)

fig.tight_layout()
plt.show()
```

**What to look at.** On the log axis, the running proportion's swings shrink steadily —
the visual form of \(1/\sqrt{n}\). The dice bars form a triangle peaking at 7, because
there are more ordered pairs summing to 7 (six) than to any other value (one for 2 and
12). The simulated points sit on the bars, which is what a correct simulation looks
like.

## 9. Practical scenario

**Is this die fair?** A game designer hands you a die and 300 rolls. The six counts
come out uneven — is that evidence of bias, or ordinary variation?

```python
rng = np.random.default_rng(99)
observed = np.bincount(rng.integers(1, 7, size=300), minlength=7)[1:]
print("observed counts:", observed.tolist())
print("expected (fair):", [50] * 6)

# A first descriptive check: how far is each count from 50, in units of the
# standard deviation of a multinomial count, sqrt(n p (1-p)) = sqrt(300 * 1/6 * 5/6).
expected = 50.0
sd = np.sqrt(300 * (1/6) * (5/6))
print(f"sd of a fair count = {sd:.2f}")
print("z-scores:", np.round((observed - expected) / sd, 2).tolist())
```

A count two standard deviations from 50 is unremarkable; with six counts, one such
value is expected. The formal test is the chi-square goodness-of-fit in Practical 17,
which sums the squared standardised gaps. The descriptive habit here — compare to the
expected count in standard-deviation units — is enough to avoid crying bias at ordinary
noise.

## 10. Exercises

**Exercise 1.** Enumerate the sample space for two coins and compute
\(\Pr(\text{at least one head})\) by counting and by the complement rule.

**Exercise 2.** Roll two dice 5,000 times and estimate \(\Pr(\text{sum}\ge10)\).
Compare with the exact value from enumeration.

**Exercise 3.** Show numerically that \(\Pr(A\cup B)=\Pr(A)+\Pr(B)\) fails for two
non-disjoint events, using the three-coin space.

**Exercise 4.** Simulate a coin with \(p=0.35\) for \(n=100, 1000, 10{,}000\) and
report the absolute error each time. Does it fall like \(1/\sqrt{n}\)?

**Exercise 5.** Two events have probabilities 0.4 and 0.5. Give one value of
\(\Pr(A\cap B)\) for which they are independent, and one for which they are mutually
exclusive. Explain why both cannot hold.

## 11. Solutions

```python
# Solution 1
two_coins = list(it.product("HT", repeat=2))
at_least_one = [o for o in two_coins if "H" in o]
print("space:", two_coins)
print(f"by counting   : {len(at_least_one)}/{len(two_coins)} = {len(at_least_one)/4:.4f}")
print(f"by complement : 1 - P(no heads) = 1 - 1/4 = {1 - 1/4:.4f}")
```

```python
# Solution 2
rng = np.random.default_rng(3)
rolls = rng.integers(1, 7, size=(5000, 2)).sum(axis=1)
sim = (rolls >= 10).mean()
exact = sum(1 for s in sums if s >= 10) / 36
print(f"simulated = {sim:.4f}")
print(f"exact     = {exact:.4f}  ({sum(1 for s in sums if s >= 10)}/36)")
print(f"difference= {sim - exact:+.4f}, se ~ {np.sqrt(exact*(1-exact)/5000):.4f}")
```

```python
# Solution 3
A = set(o for o in coins if o.count("H") == 2)
B = set(o for o in coins if o[0] == "H")
print(f"P(A) + P(B)   = {prob(A) + prob(B):.4f}")
print(f"P(A or B)     = {prob(A | B):.4f}")
print(f"overcount     = {prob(A) + prob(B) - prob(A | B):.4f} = P(A and B) = {prob(A & B):.4f}")
```

```python
# Solution 4
p = 0.35
for n in (100, 1000, 10_000):
    rng = np.random.default_rng(1000 + n)
    est = (rng.random(n) < p).mean()
    print(f"n = {n:6d}: estimate {est:.4f}, |error| {abs(est-p):.4f}, "
          f"expected se {np.sqrt(p*(1-p)/n):.4f}")
```

The error does not fall monotonically — it is random — but its typical size scales like
\(1/\sqrt{n}\): each tenfold increase in \(n\) divides the expected error by about 3.16.

```python
# Solution 5 (written)
# Independent: P(A and B) = 0.4 * 0.5 = 0.20.
# Mutually exclusive: P(A and B) = 0, since the events cannot both occur.
# Both cannot hold: independence requires P(A and B) = 0.20 > 0, while mutual
# exclusivity requires it to be 0. Two events with positive probability are either
# disjoint (dependent) or overlapping (possibly independent), never both.
```

## 12. Summary

- A sample space is a set of outcomes; a probability is a ratio of counts when
  outcomes are equally likely.
- The addition rule subtracts the intersection; the complement rule is the fastest
  route to "at least one".
- Independence is \(\Pr(A\cap B)=\Pr(A)\Pr(B)\) and must be checked, not assumed from
  the story.
- Mutually exclusive events are dependent, not independent.
- Simulation converges at rate \(1/\sqrt{n}\); the standard error tells you how close
  to expect the answer.
- Two dice are not eleven equally likely sums — the sample space is ordered pairs.

Next: [Practical 07](07-conditional-probability-and-bayes.ipynb) conditions on
information and reverses it with Bayes' theorem.
