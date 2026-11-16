# Practical 09 — Discrete Distributions

## 1. Introduction

Four discrete families cover most counting and waiting problems in data science:

| Family | Counts | Typical question |
|---|---|---|
| Bernoulli | one trial, success/failure | conversion of a single visitor |
| Binomial | successes in \(n\) trials | clicks out of 1,000 impressions |
| Geometric | trials until the first success | sessions until a sign-up |
| Poisson | events in a fixed interval | support tickets per hour |

This practical computes each PMF and CDF with SciPy, simulates from it, and checks the
two against each other. The point is not to memorise four formulas but to recognise
which mechanism produces which family — and to know when the Poisson approximation to
the binomial is safe.

## 2. Learning objectives

By the end of this practical you can:

1. Compute and plot a PMF and CDF with `scipy.stats`.
2. Simulate from a distribution and compare empirical with exact probabilities.
3. State the assumptions of the binomial and the Poisson, and when Poisson approximates
   binomial.
4. Compute waiting-time probabilities for the geometric distribution.
5. Choose the right family for a described data-generating process.

## 3. Required libraries

| Library | Used for |
|---|---|
| `scipy.stats` | `bernoulli`, `binom`, `geom`, `poisson` |
| `numpy` | simulation |
| `matplotlib` | PMF bars, CDF steps |

## 4. Concepts

### 4.1 Bernoulli: one trial

\(X\sim\text{Bernoulli}(p)\): \(X=1\) with probability \(p\), \(0\) with \(1-p\).
\(\E[X]=p\), \(\Var(X)=p(1-p)\). Every binary outcome in analytics — click, churn,
fraud — is a Bernoulli trial.

### 4.2 Binomial: \(n\) independent trials

\(X\sim\text{Binomial}(n,p)\) counts successes in \(n\) independent trials with the same
\(p\):

\[ \Pr(X=k)=\binom{n}{k}p^{k}(1-p)^{n-k},\qquad
   \E[X]=np,\qquad \Var(X)=np(1-p). \]

Assumptions: fixed \(n\), constant \(p\), independent trials. Sampling without
replacement from a small population violates independence — then the hypergeometric
distribution applies.

### 4.3 Geometric: waiting for the first success

\[ \Pr(X=k)=(1-p)^{k-1}p,\quad k=1,2,\dots,\qquad
   \E[X]=\frac1p,\qquad \Var(X)=\frac{1-p}{p^{2}}. \]

The distribution is **memoryless**: having waited 10 trials does not change the
distribution of the remaining wait. That property is what makes it the discrete
analogue of the exponential.

### 4.4 Poisson: counts in an interval

\[ \Pr(X=k)=\frac{\lambda^{k}e^{-\lambda}}{k!},\quad k=0,1,2,\dots,\qquad
   \E[X]=\Var(X)=\lambda. \]

Assumptions: events occur independently, at a constant rate, and two events cannot
occur at exactly the same time. Poisson is the limit of Binomial\((n,p)\) when \(n\) is
large, \(p\) small and \(np=\lambda\) stays fixed — the "law of rare events".

## 5. Formulas

\[ \Pr(X=k)=\binom{n}{k}p^{k}(1-p)^{n-k},\qquad
   \Pr(X\le k)=\sum_{j=0}^{k}\Pr(X=j) \]

\[ \Pr(X\ge1)=1-(1-p)^{n}\quad\text{(binomial, at least one)} \]

\[ \Pr(X>k)=(1-p)^{k}\quad\text{(geometric, still waiting after }k\text{ trials)} \]

Poisson approximation: \(\text{Binomial}(n,p)\approx\text{Poisson}(np)\) when
\(n\ge20\) and \(p\le0.05\) is a common rule of thumb.

## 6. Implementation

### 6.1 Binomial: exact, then simulated

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

n, p = 10, 0.5
X = stats.binom(n, p)

print(f"mean = {X.mean():.3f}, variance = {X.var():.3f}")
for k in (0, 5, 8, 10):
    print(f"P(X = {k:2d}) = {X.pmf(k):.4f}   P(X <= {k:2d}) = {X.cdf(k):.4f}")

print(f"P(X >= 6) = {X.sf(5):.4f}  (survival function, 1 - cdf(5))")

rng = np.random.default_rng(2026)
draws = rng.binomial(n, p, size=50_000)
print(f"\nsimulated mean {draws.mean():.3f}, variance {draws.var(ddof=0):.3f}")
print(f"simulated P(X = 5) = {(draws == 5).mean():.4f}  exact {X.pmf(5):.4f}")
```

### 6.2 Geometric: how long until the first success?

```python
p_signup = 0.08
G = stats.geom(p_signup)

print(f"mean sessions to sign-up = {G.mean():.2f}")
print(f"P(first success on trial 1)  = {G.pmf(1):.4f}")
print(f"P(first success on trial 10) = {G.pmf(10):.4f}")
print(f"P(still nothing after 20)    = {G.sf(20):.4f}   (0.92^20 = {0.92**20:.4f})")
print(f"P(success within 20)         = {G.cdf(20):.4f}")

rng = np.random.default_rng(7)
sim = rng.geometric(p_signup, size=200_000)
print(f"\nsimulated mean = {sim.mean():.3f}   exact {1/p_signup:.3f}")
print(f"simulated P(>20) = {(sim > 20).mean():.4f}")
```

### 6.3 Poisson: arrivals

```python
lam = 4.0          # tickets per hour
P = stats.poisson(lam)

print(f"mean = variance = {lam}")
for k in range(0, 9):
    print(f"P(X = {k}) = {P.pmf(k):.4f}   P(X <= {k}) = {P.cdf(k):.4f}")

print(f"\nP(more than 8 tickets) = {P.sf(8):.4f}")
print(f"P(between 2 and 6 inclusive) = {P.cdf(6) - P.cdf(1):.4f}")

rng = np.random.default_rng(11)
arrivals = rng.poisson(lam, size=100_000)
print(f"simulated mean {arrivals.mean():.3f}, variance {arrivals.var(ddof=0):.3f}")
```

### 6.4 Poisson as a limit of the binomial

```python
n_big, p_small = 1000, 0.004
joint = stats.binom(n_big, p_small)
approx = stats.poisson(n_big * p_small)

print(f"{'k':>3} {'binomial':>10} {'Poisson':>10} {'difference':>11}")
for k in range(0, 11):
    b, q = joint.pmf(k), approx.pmf(k)
    print(f"{k:>3} {b:>10.5f} {q:>10.5f} {b-q:>+11.5f}")

ks = np.arange(0, 15)
print(f"\nmaximum absolute difference on k=0..14: "
      f"{np.max(np.abs(joint.pmf(ks) - approx.pmf(ks))):.5f}")
```

### 6.5 Choosing a family from the mechanism

```python
scenarios = [
    ("10 visitors, each converts with p = 0.05; count conversions", "binomial"),
    ("visitors until the first conversion", "geometric"),
    ("emails arriving at a helpdesk in one hour", "poisson"),
    ("one visitor converts or not", "bernoulli"),
    ("20 cards drawn without replacement; count aces", "hypergeometric"),
]
for description, family in scenarios:
    print(f"{family:15s} <- {description}")
```

The last one matters: drawing without replacement from 52 cards, \(p\) changes after
each card, so the binomial does not apply.

### 6.6 Overdispersion: when Poisson is wrong

```python
rng = np.random.default_rng(3)
lam_mixture = rng.gamma(2.0, 3.0, size=100_000)      # rate varies by hour
counts_mix = rng.poisson(lam_mixture)

print(f"mixture mean     = {counts_mix.mean():.3f}")
print(f"mixture variance = {counts_mix.var(ddof=0):.3f}")
print(f"variance / mean  = {counts_mix.var(ddof=0)/counts_mix.mean():.3f}  (Poisson would be 1)")
```

When the rate itself varies (busy hours and quiet hours), counts are **overdispersed**:
the variance exceeds the mean. The negative binomial is the standard model for that
case, and ignoring it produces confidence intervals that are too narrow.

## 7. Output and interpretation

- **Binomial.** With \(n=10\), \(p=0.5\): mean 5, variance 2.5, \(\Pr(X=5)=0.2461\).
  The probability of exactly half the trials being successes is only about a quarter,
  even though 5 is the most likely value — a useful antidote to expecting the mean to be
  the typical outcome.
- **Geometric.** With \(p=0.08\), the expected wait is 12.5 sessions, and 0.92\(^{20}\) =
  0.189, so nearly one visitor in five still has not converted after 20 sessions. The
  distribution has a long right tail: half of all converters arrive within 9 sessions,
  but the mean is 12.5.
- **Poisson.** With \(\lambda=4\), \(\Pr(X=4)=0.1954\) and \(\Pr(X\le4)=0.6288\); the
  mean equals the variance, which is the diagnostic signature of a Poisson process.
- **The limit.** At \(n=1000\), \(p=0.004\), the binomial and Poisson probabilities
  agree to about 0.0005 — invisible on a plot and irrelevant for a decision.
- **Overdispersion.** The mixture has a variance roughly four times its mean, because
  the rate itself varies. A Poisson model fitted to it would report standard errors
  about \(\sqrt{4}=2\) times too small, so intervals would be half as wide as they
  should be.

## 8. Visualisation

```python
fig, axes = plt.subplots(1, 3, figsize=(12.5, 3.4))

ks = np.arange(0, 21)
axes[0].bar(ks, stats.binom(20, 0.3).pmf(ks), color="#4c72b0")
axes[0].set(title="Binomial(20, 0.3)", xlabel="k", ylabel="P(X = k)")

ks = np.arange(1, 26)
axes[1].bar(ks, stats.geom(0.15).pmf(ks), color="#dd8452")
axes[1].set(title="Geometric(0.15): a long right tail", xlabel="k", ylabel="P(X = k)")

ks = np.arange(0, 16)
axes[2].bar(ks, stats.poisson(4).pmf(ks), color="#55a868")
axes[2].set(title="Poisson(4)", xlabel="k", ylabel="P(X = k)")

for ax in axes:
    ax.grid(alpha=0.25, axis="y")
fig.tight_layout()
plt.show()
```

```python
fig, axes = plt.subplots(1, 2, figsize=(11, 3.6))

ks = np.arange(0, 16)
axes[0].step(ks, stats.poisson(4).cdf(ks), where="post", color="#4c72b0", linewidth=2)
axes[0].set(title="Poisson(4) CDF: a step function", xlabel="k", ylabel="P(X <= k)")

draws = rng.poisson(4, size=20_000)
values, counts = np.unique(draws, return_counts=True)
axes[1].bar(values, counts / draws.size, alpha=0.6, color="#4c72b0", label="simulated")
axes[1].plot(ks, stats.poisson(4).pmf(ks), "o", color="#c44e52", label="exact")
axes[1].set(title="Simulation against the PMF", xlabel="k", ylabel="Probability")
axes[1].legend(frameon=False)

fig.tight_layout()
plt.show()
```

**What to look at.** The binomial is symmetric at \(p=0.5\) and skewed at \(p=0.3\);
the geometric decays geometrically, so its bars form a straight line on a log scale;
the Poisson is skewed right for small \(\lambda\) and becomes symmetric as \(\lambda\)
grows. The CDF is a staircase because the variable is discrete: the probability jumps at
each integer and is flat between them.

## 9. Practical scenario

**Capacity planning for a support desk.** Tickets arrive at 4 per hour on average. The
desk can handle 7 per hour. How often is it overwhelmed in a given hour, and how much
does adding one agent (8 per hour) help?

```python
lam = 4.0
for capacity in (7, 8):
    p_over = stats.poisson(lam).sf(capacity)
    print(f"capacity {capacity}: P(more than {capacity} tickets) = {p_over:.4f} "
          f"({p_over*100:.2f}% of hours)")
```

The Poisson model assumes a constant rate, which fails if mornings are busier than
afternoons: the service would be overwhelmed more often than this calculation says. The
fix is to model each period separately (or use a negative binomial), not to add a
fudge factor.

## 10. Exercises

**Exercise 1.** A machine produces a defective item with probability 0.03. For 50 items,
compute the probability of exactly 2 defectives and of at most 2.

**Exercise 2.** Simulate 20,000 binomial samples with \(n=50\), \(p=0.03\) and compare
the proportion of 2s with the exact value from Exercise 1.

**Exercise 3.** With \(p=0.2\), compute the probability that the first success occurs
after trial 5, and the expected number of trials.

**Exercise 4.** A call centre receives 6 calls per minute on average. Compute
\(\Pr(X\le2)\) and compare it with the Poisson approximation using
\(n=600\), \(p=0.01\).

**Exercise 5.** Explain in two sentences why drawing 5 cards from a deck without
replacement is not binomial.

## 11. Solutions

```python
# Solution 1
B = stats.binom(50, 0.03)
print(f"P(X = 2) = {B.pmf(2):.5f}")
print(f"P(X <= 2) = {B.cdf(2):.5f}")
print(f"mean = {B.mean():.3f}, variance = {B.var():.3f}")
```

```python
# Solution 2
rng = np.random.default_rng(21)
draws = rng.binomial(50, 0.03, size=20_000)
exact = stats.binom(50, 0.03).pmf(2)
emp = (draws == 2).mean()
print(f"simulated P(X = 2) = {emp:.5f}  exact {exact:.5f}  diff {emp-exact:+.5f}")
print(f"simulation se      = {np.sqrt(exact*(1-exact)/20_000):.5f}")
```

```python
# Solution 3
G = stats.geom(0.2)
print(f"P(X > 5) = {G.sf(5):.5f}   (0.8^5 = {0.8**5:.5f})")
print(f"E[X] = {G.mean():.3f}")
```

```python
# Solution 4
P6 = stats.poisson(6)
print(f"P(X <= 2) Poisson(6)      = {P6.cdf(2):.5f}")
print(f"P(X <= 2) Binomial(600,.01) = {stats.binom(600, 0.01).cdf(2):.5f}")
print(f"difference = {P6.cdf(2) - stats.binom(600,0.01).cdf(2):+.6f}")
```

```python
# Solution 5 (written)
# Drawing without replacement changes p after every card: if the first card is an ace,
# the chance the second is an ace falls from 4/52 to 3/51. The binomial requires a
# constant p and independent trials, so the correct model is the hypergeometric --
# which matters for small populations even though it is nearly binomial for a full deck.
```

## 12. Summary

- Bernoulli is one trial; binomial is \(n\) independent trials with fixed \(p\).
- Geometric counts trials until the first success, is memoryless, and has a long right
  tail; its mean is \(1/p\).
- Poisson counts events in an interval with mean equal to variance; it approximates the
  binomial when \(n\) is large and \(p\) small.
- Sampling without replacement breaks independence — use the hypergeometric.
- Variance greater than the mean signals overdispersion; the negative binomial is the
  usual remedy.
- Every PMF here can be checked against a simulation with a fixed seed, and the check is
  the best defence against picking the wrong family.

Next: [Practical 10](10-continuous-distributions.ipynb) covers densities and the normal
distribution.
