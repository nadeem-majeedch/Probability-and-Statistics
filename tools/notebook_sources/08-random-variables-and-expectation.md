# Practical 08 — Random Variables and Expectation

## 1. Introduction

A random variable turns an outcome into a number: the sum of two dice, the number of
heads in ten tosses, the waiting time until the next customer. Once outcomes are
numbers, we can average them — and the average of a random variable over infinitely
many repetitions is its **expectation**.

This practical computes expectations and variances from the definition, checks them by
simulation, and shows the two properties that make the rest of the course tractable:
linearity of expectation, and the way variance scales under linear transformations.

## 2. Learning objectives

By the end of this practical you can:

1. Write a PMF for a discrete random variable and check that it sums to 1.
2. Compute \(\E[X]\), \(\E[X^{2}]\) and \(\Var(X)\) from the definition.
3. Use linearity of expectation and \(\Var(aX+b)=a^{2}\Var(X)\).
4. Apply the law of the unconscious statistician to \(\E[g(X)]\).
5. Estimate an expectation by simulation and state the simulation's standard error.

## 3. Required libraries

| Library | Used for |
|---|---|
| `numpy` | simulation, vectorised expectation |
| `matplotlib` | PMF bars and convergence of the running mean |
| `math` | exact constants |

## 4. Concepts

### 4.1 From outcomes to numbers

A random variable \(X\) is a function from the sample space to the real numbers.
For a discrete \(X\), the **probability mass function** \(p(x)=\Pr(X=x)\) satisfies
\(p(x)\ge0\) and \(\sum_x p(x)=1\).

Two dice: \(X=\) sum, \(p(7)=6/36\). Coin tossing: \(X=\) number of heads,
\(p(k)=\binom{10}{k}2^{-10}\).

### 4.2 Expectation

\[ \E[X]=\sum_x x\,p(x) \]

is the probability-weighted average — the value the running mean converges to. It need
not be a possible value: the expected number of heads in one toss is 0.5, and the
expected sum of two dice is 7, which is possible, but the expected number of children
in a family can be 2.4.

### 4.3 Variance and its shortcut

\[ \Var(X)=\E[(X-\E X)^{2}]=\E[X^{2}]-(\E X)^{2}. \]

The second form is what you compute: one pass for \(\E[X^{2}]\), one for \(\E[X]\). The
standard deviation \(\sigma=\sqrt{\Var(X)}\) returns to the units of \(X\).

### 4.4 Properties worth memorising

\[ \E[aX+b]=a\E[X]+b,\qquad \Var(aX+b)=a^{2}\Var(X) \]

\[ \E[g(X)]=\sum_x g(x)p(x)\quad\text{(LOTUS)} \]

Shifting a distribution moves the mean and leaves the spread alone; scaling multiplies
the mean and the standard deviation, and multiplies the variance by the square.
Standardisation \(Z=(X-\mu)/\sigma\) therefore always has mean 0 and variance 1.

## 5. Formulas

\[ \E[X]=\sum_x x p(x),\qquad \E[X^{2}]=\sum_x x^{2}p(x),\qquad
   \Var(X)=\E[X^{2}]-(\E X)^{2} \]

For a fair die: \(\E[X]=\frac{1+2+\cdots+6}{6}=3.5\) and

\[ \E[X^{2}]=\frac{1^{2}+\cdots+6^{2}}{6}=\frac{91}{6}\approx15.1667,
   \qquad \Var(X)=\frac{91}{6}-3.5^{2}=\frac{35}{12}\approx2.9167. \]

For a continuous variable, \(\E[X]=\int x f(x)\,dx\); for \(X\sim\text{Exponential}(\lambda)\)
that integral gives \(1/\lambda\).

## 6. Implementation

### 6.1 A die: expectation from the definition

```python
import numpy as np
import matplotlib.pyplot as plt

outcomes = np.arange(1, 7)
pmf = np.full(6, 1 / 6)

assert np.isclose(pmf.sum(), 1.0)
mean_die = np.sum(outcomes * pmf)
second_moment = np.sum(outcomes**2 * pmf)
var_die = second_moment - mean_die**2

print(f"sum of pmf        : {pmf.sum():.6f}")
print(f"E[X]              : {mean_die:.4f}")
print(f"E[X^2]            : {second_moment:.4f}")
print(f"Var(X)            : {var_die:.4f}   (= 35/12 = {35/12:.4f})")
print(f"sd(X)             : {np.sqrt(var_die):.4f}")
```

### 6.2 The same quantities by simulation

```python
rng = np.random.default_rng(2026)
rolls = rng.integers(1, 7, size=100_000)

print(f"simulated mean     : {rolls.mean():.4f}   (exact {mean_die:.4f})")
print(f"simulated variance : {rolls.var(ddof=0):.4f}   (exact {var_die:.4f})")
print(f"standard error of the mean: {rolls.std(ddof=0)/np.sqrt(rolls.size):.4f}")
```

### 6.3 Linearity: the sum of two dice

```python
d1 = rng.integers(1, 7, size=100_000)
d2 = rng.integers(1, 7, size=100_000)
total = d1 + d2

print(f"E[d1 + d2] simulated = {total.mean():.4f}   exact = {2*mean_die:.4f}")
print(f"Var(d1 + d2)         = {total.var(ddof=0):.4f}   exact = {2*var_die:.4f}")
```

Adding independent variables adds their variances — no covariance term, because
independent variables have zero covariance. That is the result that makes the standard
error of a sum \(\sqrt{n\sigma^{2}}\), and the standard error of a mean
\(\sigma/\sqrt{n}\).

### 6.4 Linear transformations

```python
a, b = 3.0, -2.0
transformed = a * rolls + b

print(f"E[aX + b] : simulated {transformed.mean():9.4f}   "
      f"formula {a*mean_die + b:9.4f}")
print(f"Var(aX+b) : simulated {transformed.var(ddof=0):9.4f}   "
      f"formula {a**2*var_die:9.4f}")
print(f"sd(aX+b)  : simulated {transformed.std(ddof=0):9.4f}   "
      f"formula {abs(a)*np.sqrt(var_die):9.4f}")
```

### 6.5 LOTUS: the expectation of a function

A game pays 0 for a 1, 2 or 3, and 10 for a 4, 5 or 6. What is the expected payout?
You cannot get it by applying the function to \(\E[X]=3.5\).

```python
payout_table = {1: 0, 2: 0, 3: 0, 4: 10, 5: 10, 6: 10}
payout = np.array([payout_table[k] for k in range(1, 7)])

e_payout_lotus = np.sum(payout * pmf)
e_payout_sim = np.array([payout_table[k] for k in rolls]).mean()
e_payout_wrong = payout_table[int(mean_die)] if mean_die in payout_table else None

print(f"E[g(X)] by LOTUS      : {e_payout_lotus:.4f}")
print(f"E[g(X)] by simulation : {e_payout_sim:.4f}")
print(f"E[X] = {mean_die}, but g(E[X]) is undefined at a non-integer 3.5")
print(f"a naive substitution would give g(3) = {payout_table[3]} or g(4) = {payout_table[4]}")
```

### 6.6 Continuous expectation: the exponential

```python
lam = 0.5
waits = rng.exponential(scale=1/lam, size=200_000)
print(f"E[X] simulated : {waits.mean():.4f}   exact 1/lambda = {1/lam:.4f}")
print(f"Var(X) simulated: {waits.var(ddof=0):.4f}   exact 1/lambda^2 = {1/lam**2:.4f}")

# Numerical integration, as an independent check.
grid = np.linspace(0, 60, 600_001)
density = lam * np.exp(-lam * grid)
mean_numeric = np.trapezoid(grid * density, grid)
var_numeric = np.trapezoid((grid - mean_numeric) ** 2 * density, grid)
print(f"E[X] by integration    : {mean_numeric:.4f}")
print(f"Var(X) by integration  : {var_numeric:.4f}")
```

### 6.7 Standardisation always gives mean 0 and variance 1

```python
for name, sample in [("die", rolls.astype(float)),
                     ("payout", np.array([payout_table[k] for k in rolls], dtype=float)),
                     ("exponential", waits)]:
    z = (sample - sample.mean()) / sample.std(ddof=0)
    print(f"{name:12s} mean {z.mean():+.6f}  var {z.var(ddof=0):.6f}  "
           f"min {z.min():7.3f}  max {z.max():7.3f}")
```

### 6.8 An expected-value decision

A card is drawn from a shuffled deck. You win 10 if it is an ace and lose 1 otherwise.
Should you play?

```python
p_ace = 4 / 52
ev = 10 * p_ace - 1 * (1 - p_ace)
print(f"P(ace) = {p_ace:.4f}")
print(f"expected value = {ev:+.4f} per game")

rng2 = np.random.default_rng(5)
wins = rng2.random(100_000) < p_ace
result = np.where(wins, 10.0, -1.0)
print(f"simulated mean = {result.mean():+.4f}")
print(f"share of games won = {wins.mean():.4f}")
```

## 7. Output and interpretation

- **The die.** \(\E[X]=3.5\), \(\Var(X)=2.9167\), so the standard deviation is 1.708.
  The mean is not a face of the die, which is normal: expectation is a long-run average,
  not a prediction.
- **Simulation.** 100,000 rolls give a mean within about 0.005 of 3.5 — the standard
  error is \(1.708/\sqrt{100{,}000}=0.0054\). The simulated variance matches 2.9167 to
  two decimals.
- **Two dice.** The mean doubles to 7 and the variance doubles to 5.833. Means add
  because of linearity; variances add because the dice are independent.
- **Transformation.** \(3X-2\) has mean \(3(3.5)-2=8.5\), variance \(9(2.9167)=26.25\)
  and standard deviation \(3(1.708)=5.124\). Shifting by \(-2\) changed nothing about
  the spread; multiplying by 3 tripled the standard deviation.
- **LOTUS.** The expected payout is 5.00, not 0 or 10: three faces pay 0 and three pay
  10, so the average over many plays is 5. Applying \(g\) to \(\E[X]=3.5\) is
  meaningless — \(g\) is defined only at integers, and even if it were extended, \(g\)
  is not linear, so \(g(\E X)\neq\E[g(X)]\).
- **Exponential.** The simulated mean and variance both match \(1/\lambda\) and
  \(1/\lambda^{2}\), and the numerical integrals agree. The exponential is the only
  continuous distribution whose mean equals its standard deviation.
- **Standardisation.** Every standardised sample printed has mean 0 and variance 1 to
  six decimals, whatever the original shape. That is why z-tables work for any
  variable once you know its mean and standard deviation.

## 8. Visualisation

```python
fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))

axes[0].bar(outcomes, pmf, width=0.6, color="#4c72b0", edgecolor="white")
axes[0].axvline(mean_die, color="#c44e52", linestyle="--",
                label=f"E[X] = {mean_die}")
axes[0].set(xlabel="Face", ylabel="Probability", xticks=outcomes,
            title="PMF of a fair die: uniform, mean 3.5")
axes[0].legend(frameon=False)

running = np.cumsum(rolls) / np.arange(1, rolls.size + 1)
axes[1].plot(running, linewidth=1.2, color="#55a868")
axes[1].axhline(mean_die, color="#c44e52", linestyle="--", label="E[X] = 3.5")
axes[1].set(xscale="log", xlabel="Number of rolls (log scale)", ylabel="Running mean",
            title="The running mean converges to the expectation")
axes[1].legend(frameon=False)

fig.tight_layout()
plt.show()
```

**What to look at.** The left bars are equal because the die is fair, and the dashed
line falls between 3 and 4 — the expectation is a property of the distribution, not of
any outcome. On the right, the running mean starts anywhere (the first roll is an
integer) and settles towards 3.5 with fluctuations of size \(1/\sqrt{n}\).

## 9. Practical scenario

**Should a warranty be offered?** A laptop fails within the warranty period with
probability 0.04, and a replacement costs the seller 60,000. The warranty sells for
3,500.

```python
p_fail = 0.04
cost = 60_000
price = 3_500

ev_seller = price - p_fail * cost
print(f"expected profit per warranty = {ev_seller:+,.0f}")
print(f"break-even price             = {p_fail*cost:,.0f}")
print(f"expected cost of failures per 1,000 warranties = {p_fail*cost*1000:,.0f}")

# The customer's side: expected payout against the price.
print(f"customer expected payout = {p_fail*cost:,.0f} for a price of {price:,}")
```

The seller's expected profit is positive at this price; the customer's expected payout
is larger than the price, which is why the warranty feels like a bad deal to a
risk-neutral buyer and still sells — buyers are not risk-neutral about a 60,000 loss.
Expected value answers "on average, over many repetitions"; it does not by itself decide
what a single person should do.

## 10. Exercises

**Exercise 1.** For a fair coin tossed 3 times, write the PMF of the number of heads and
compute \(\E[X]\) and \(\Var(X)\) from the definition.

**Exercise 2.** Verify by simulation that \(\E[X]=np\) and \(\Var(X)=np(1-p)\) for
\(n=20\), \(p=0.3\).

**Exercise 3.** A random variable has \(\E[X]=10\), \(\Var(X)=4\). Compute
\(\E[5X-3]\) and \(\Var(5X-3)\).

**Exercise 4.** For the die, compute \(\E[X^{2}]\) two ways: from the definition and
using \(\Var(X)+(\E X)^{2}\).

**Exercise 5.** A lottery ticket costs 200 and wins 100,000 with probability 1/500,000.
Compute the expected value and explain why people still buy tickets.

## 11. Solutions

```python
# Solution 1
from math import comb
k = np.arange(4)
p = np.array([comb(3, i) / 8 for i in k])
mean = np.sum(k * p)
var = np.sum(k**2 * p) - mean**2
print("pmf:", p, "sum:", p.sum())
print(f"E[X] = {mean:.4f}, E[X^2] = {np.sum(k**2*p):.4f}, Var = {var:.4f}")
```

```python
# Solution 2
rng = np.random.default_rng(12)
n_trials, p = 20, 0.3
counts = rng.binomial(n_trials, p, size=200_000)
print(f"simulated mean {counts.mean():.4f}  exact np = {n_trials*p:.4f}")
print(f"simulated var  {counts.var(ddof=0):.4f}  exact np(1-p) = {n_trials*p*(1-p):.4f}")
```

```python
# Solution 3
print(f"E[5X-3] = {5*10-3}, Var(5X-3) = {25*4}, sd = {np.sqrt(25*4)}")
```

```python
# Solution 4
print(f"E[X^2] from definition : {second_moment:.4f}")
print(f"Var + (E X)^2          : {var_die + mean_die**2:.4f}")
print("equal?", np.isclose(second_moment, var_die + mean_die**2))
```

```python
# Solution 5
cost, prize, p_win = 200, 100_000, 1 / 500_000
ev = p_win * prize - cost
print(f"expected net = {ev:+.2f} per ticket")
print(f"expected return per unit staked = {(p_win*prize)/cost:.3f}")
```

The expected value is negative — about −199.8 per ticket, since the expected payout is
only 0.2. People buy because the price of a ticket buys a small chance of a
life-changing sum, and expected value is not the only thing people maximise. That is a
statement about preferences, not about arithmetic.

## 12. Summary

- A random variable is a numeric function of outcomes; its PMF gives the probabilities
  of its values and sums to 1.
- Expectation is the probability-weighted average; variance is the mean squared
  deviation, computed as \(\E[X^{2}]-(\E X)^{2}\).
- Linear transformations move the mean and scale the spread: \(\E[aX+b]=a\E X+b\),
  \(\Var(aX+b)=a^{2}\Var X\).
- LOTUS computes \(\E[g(X)]\) by summing \(g(x)p(x)\); \(g(\E X)\neq\E[g(X)]\) unless
  \(g\) is linear.
- Means add always; variances add for independent variables.
- Simulation estimates an expectation with error about \(\sigma/\sqrt{n}\).

Next: [Practical 09](09-discrete-distributions.ipynb) works through the named discrete
families.
