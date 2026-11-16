/*
 * Automated tests for the interactive-lab mathematics.
 *
 * Run:  node --test tests/
 *
 * Reference values were computed independently with SciPy 1.x
 * (scipy.stats and scipy.special) and are pasted in as constants, so the
 * tests do not depend on Python being installed. Tolerances are stated per
 * test and are far tighter than any difference a student could see.
 */

"use strict";

const test = require("node:test");
const assert = require("node:assert");
const S = require("../docs/assets/javascripts/stats.js");

const close = (a, b, tol, label) =>
  assert.ok(Math.abs(a - b) <= tol, `${label}: got ${a}, expected ${b} ±${tol}`);

/* ---------------------------------------------------------------- normal */

test("normal CDF matches SciPy", () => {
  close(S.normCdf(-2.5), 0.006209665325776132, 1e-14, "Φ(-2.5)");
  close(S.normCdf(0), 0.5, 1e-15, "Φ(0)");
  close(S.normCdf(1.645), 0.9500150944608786, 1e-14, "Φ(1.645)");
  close(S.normCdf(1.96), 0.9750021048517795, 1e-14, "Φ(1.96)");
});

test("normal quantile inverts the CDF to 1e-10", () => {
  close(S.normInv(0.025), -1.9599639845400545, 1e-9, "Φ⁻¹(0.025)");
  close(S.normInv(0.5), 0, 1e-12, "Φ⁻¹(0.5)");
  close(S.normInv(0.975), 1.959963984540054, 1e-9, "Φ⁻¹(0.975)");
  [0.001, 0.01, 0.2, 0.5, 0.8, 0.99, 0.999].forEach((p) => {
    close(S.normCdf(S.normInv(p)), p, 1e-10, `round trip at p=${p}`);
  });
});

test("normal density integrates to one (Simpson rule)", () => {
  let sum = 0;
  const a = -9;
  const b = 9;
  const n = 3600;
  const h = (b - a) / n;
  for (let i = 0; i <= n; i++) {
    const w = i === 0 || i === n ? 1 : i % 2 ? 4 : 2;
    sum += w * S.normPdf(a + i * h);
  }
  close((sum * h) / 3, 1, 1e-12, "∫φ");
});

/* -------------------------------------------------------------- discrete */

test("binomial PMF matches SciPy", () => {
  close(S.binomPmf(0, 20, 0.3), 0.0007979226629761171, 1e-15, "P(X=0)");
  close(S.binomPmf(5, 20, 0.3), 0.17886305056987964, 1e-13, "P(X=5)");
  close(S.binomPmf(20, 20, 0.9), 0.12157665459056935, 1e-13, "P(X=20)");
  close(S.binomPmf(10, 20, 0.5), 0.17619705200195296, 1e-15, "P(X=10)");
});

test("binomial PMF sums to one and obeys the trivial boundaries", () => {
  let total = 0;
  for (let k = 0; k <= 40; k++) total += S.binomPmf(k, 40, 0.35);
  close(total, 1, 1e-12, "Σ pmf");
  assert.strictEqual(S.binomPmf(-1, 10, 0.5), 0, "negative k");
  assert.strictEqual(S.binomPmf(11, 10, 0.5), 0, "k > n");
  assert.strictEqual(S.binomPmf(0, 10, 0), 1, "p = 0, k = 0");
  assert.strictEqual(S.binomPmf(3, 10, 0), 0, "p = 0, k > 0");
  assert.strictEqual(S.binomPmf(10, 10, 1), 1, "p = 1, k = n");
});

test("binomial CDF is monotone, bounded and agrees with the PMF", () => {
  let prev = 0;
  for (let k = 0; k <= 25; k++) {
    const c = S.binomCdf(k, 25, 0.4);
    assert.ok(c >= prev - 1e-15, "CDF is non-decreasing");
    assert.ok(c >= 0 && c <= 1, "CDF stays in [0, 1]");
    prev = c;
  }
  close(prev, 1, 1e-12, "CDF at n");
  close(
    S.binomCdf(6, 25, 0.4) - S.binomCdf(5, 25, 0.4),
    S.binomPmf(6, 25, 0.4),
    1e-15,
    "CDF difference"
  );
});

test("Poisson PMF matches SciPy and sums to one", () => {
  close(S.poissonPmf(0, 3.5), 0.0301973834223185, 1e-16, "P(0)");
  close(S.poissonPmf(7, 3.5), 0.038549174937634004, 1e-15, "P(7)");
  close(S.poissonPmf(12, 3.5), 0.0002130339801586227, 1e-16, "P(12)");
  let total = 0;
  for (let k = 0; k <= 200; k++) total += S.poissonPmf(k, 12);
  close(total, 1, 1e-12, "Σ pmf at λ = 12");
  assert.strictEqual(S.poissonPmf(-2, 3.5), 0, "negative k");
});

/* ------------------------------------------------------------ continuous */

test("exponential CDF matches SciPy", () => {
  close(S.exponCdf(1, 0.8), 0.5506710358827784, 1e-15, "F(1)");
  close(S.exponCdf(3, 0.8), 0.9092820467105875, 1e-15, "F(3)");
  assert.strictEqual(S.exponCdf(-1, 0.8), 0, "no mass below zero");
});

test("gamma density matches SciPy and integrates to one", () => {
  close(S.gammaPdf(0.5, 2, 0.5), 0.09735009788392561, 1e-15, "gamma pdf at 0.5");
  close(S.gammaPdf(2, 2, 0.5), 0.18393972058572117, 1e-15, "gamma pdf at 2");
  let sum = 0;
  const n = 4000;
  const hi = 60;
  for (let i = 0; i <= n; i++) sum += S.gammaPdf((i * hi) / n, 3, 0.7);
  close((sum * hi) / n, 1, 2e-3, "∫ gamma pdf (rectangle rule)");
});

test("uniform density and CDF are exact", () => {
  assert.strictEqual(S.uniformPdf(0.4, 0, 2), 0.5, "pdf inside");
  assert.strictEqual(S.uniformPdf(2.5, 0, 2), 0, "pdf outside");
  close(S.uniformCdf(0.5, 0, 2), 0.25, 1e-15, "CDF");
  assert.strictEqual(S.uniformCdf(-1, 0, 2), 0, "CDF below support");
  assert.strictEqual(S.uniformCdf(5, 0, 2), 1, "CDF above support");
});

/* --------------------------------------------------------------- t and F */

test("Student t CDF and two-sided p match SciPy", () => {
  close(S.tCdf(1.5, 10), 0.9177463367772799, 1e-13, "t CDF");
  close(S.tCdf(-2, 7), 0.042809664281488025, 1e-13, "t CDF negative");
  close(S.tTwoSidedP(2, 19), 0.06000203638609834, 1e-13, "two-sided p, t = 2");
  close(S.tTwoSidedP(0.5, 4), 0.6433299631818633, 1e-13, "two-sided p, t = 0.5");
  close(S.tTwoSidedP(3.5, 99), 0.0006990646483687958, 1e-13, "two-sided p, t = 3.5");
});

test("t distribution is symmetric and its quantiles invert the CDF", () => {
  close(S.tCdf(0, 12), 0.5, 1e-14, "median at zero");
  close(S.tCdf(1.2, 12) + S.tCdf(-1.2, 12), 1, 1e-14, "symmetry");
  close(S.tCdf(S.tInv(0.975, 10), 10), 0.975, 1e-9, "quantile round trip");
  close(S.tInv(0.975, 10), 2.2281388519862744, 1e-9, "t 0.975, df 10");
  assert.ok(S.tTwoSidedP(0, 5) === 1, "p = 1 at t = 0");
});

test("F tail matches SciPy and is monotone", () => {
  close(S.fSf(2.5, 3, 44), 0.07182821239833596, 1e-13, "F tail");
  close(S.fSf(0.8, 4, 55), 0.5304155787681264, 1e-13, "F tail below 1");
  let prev = 1;
  for (let f = 0.2; f <= 8; f += 0.2) {
    const v = S.fSf(f, 3, 20);
    assert.ok(v <= prev + 1e-14, "tail is non-increasing");
    assert.ok(v >= 0 && v <= 1, "tail in [0, 1]");
    prev = v;
  }
});

/* --------------------------------------------------- summaries and models */

test("summary statistics use n − 1 for the sample SD", () => {
  const a = [1, 2, 3, 4, 5];
  assert.strictEqual(S.mean(a), 3);
  close(S.sd(a), Math.sqrt(2.5), 1e-15, "sample SD");
  close(S.sd(a, 0), Math.sqrt(2), 1e-15, "population SD");
  assert.strictEqual(S.median([5, 1, 9, 3]), 4);
  assert.strictEqual(S.median([4, 1, 9]), 4);
});

test("correlation and least squares match numpy", () => {
  const x = [1, 2, 3, 4, 5];
  const y = [2, 4, 5, 4, 5];
  close(S.correlation(x, y), 0.7745966692414834, 1e-14, "r");
  const fit = S.ols(x, y);
  close(fit.slope, 0.6, 1e-14, "slope");
  close(fit.intercept, 2.2, 1e-14, "intercept");
  close(fit.r2, 0.6, 1e-13, "R²");
});

test("correlation is undefined for a constant variable", () => {
  const r = S.correlation([1, 1, 1, 1], [1, 2, 3, 4]);
  assert.ok(Number.isNaN(r) || !isFinite(r), "constant x gives NaN or 0/0");
});

test("one-way ANOVA matches scipy.stats.f_oneway", () => {
  const res = S.anova([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);
  close(res.F, 27, 1e-12, "F");
  close(res.p, 0.0010000000000000002, 1e-12, "p");
  assert.strictEqual(res.dfb, 2);
  assert.strictEqual(res.dfw, 6);
  close(res.eta2, 54 / 60, 1e-14, "η²");
  close(res.ssb + res.ssw, res.sst, 1e-14, "SS partition");
});

test("ANOVA reports the degenerate all-identical case instead of NaN", () => {
  const res = S.anova([[2, 2, 2], [2, 2, 2]]);
  assert.strictEqual(res.degenerate, true, "flagged as degenerate");
  assert.strictEqual(res.F, 0, "F is reported as 0");
  assert.strictEqual(res.p, 1, "p is reported as 1");
  assert.strictEqual(res.eta2, 0, "eta squared is 0");
  const normal = S.anova([[1, 2, 3], [4, 5, 6]]);
  assert.strictEqual(normal.degenerate, false, "ordinary data is not flagged");
});

/* --------------------------------------------------------- power, Wilson */

test("power of the two-sided z test matches the standard formula", () => {
  const d = 0.5, n = 30, alpha = 0.05;
  const zc = S.zCrit(alpha);
  const power = S.normCdf(d * Math.sqrt(n) - zc) + S.normCdf(-d * Math.sqrt(n) - zc);
  close(power, 0.7819079987319799, 1e-13, "power");
  close(S.zCrit(0.05), 1.959963984540054, 1e-9, "z crit");
});

test("power rises with n and equals alpha at zero effect", () => {
  const power = (d, n) => {
    const zc = S.zCrit(0.05);
    return S.normCdf(d * Math.sqrt(n) - zc) + S.normCdf(-d * Math.sqrt(n) - zc);
  };
  close(power(0, 50), 0.05, 1e-9, "no effect → power = α");
  assert.ok(power(0.4, 20) < power(0.4, 80), "power increases with n");
  assert.ok(power(0.2, 60) < power(0.6, 60), "power increases with effect size");
});

test("Wilson interval stays inside [0, 1] at the extremes", () => {
  const a = S.wilson(0, 10, 1.96);
  const b = S.wilson(10, 10, 1.96);
  assert.ok(a.lo >= 0 && a.hi <= 1, "no successes");
  assert.ok(b.lo >= 0 && b.hi <= 1, "all successes");
  assert.ok(a.lo < a.hi && b.lo < b.hi, "non-degenerate");
});

/* ------------------------------------------------------- robustness sweep */

test("no density, CDF or p-value ever leaves its legal range", () => {
  const params = [0.001, 0.01, 0.1, 0.3, 0.5, 0.9, 0.99];
  params.forEach((p) => {
    assert.ok(S.normCdf(p) > 0 && S.normCdf(p) < 1, "normal CDF open interval");
    assert.ok(S.tCdf(p, 3) > 0 && S.tCdf(p, 3) < 1, "t CDF open interval");
    assert.ok(S.binomPmf(3, 10, p) >= 0, "PMF ≥ 0");
    assert.ok(S.poissonPmf(3, 10 * p) >= 0, "PMF ≥ 0");
    assert.ok(S.fSf(p, 2, 9) >= 0 && S.fSf(p, 2, 9) <= 1, "F tail in range");
  });
});

test("extreme inputs stay finite rather than exploding", () => {
  assert.ok(isFinite(S.tTwoSidedP(1e6, 3)), "huge t");
  assert.ok(S.tTwoSidedP(1e6, 3) < 1e-10, "huge t gives a tiny p");
  assert.ok(isFinite(S.normCdf(-30)), "deep lower tail");
  assert.ok(S.normCdf(-30) < 1e-100, "deep tail is tiny, not negative");
  assert.ok(S.binomPmf(0, 2000, 1e-4) > 0, "tiny p does not underflow to NaN");
  assert.ok(isFinite(S.poissonPmf(500, 500)), "large λ stays finite");
});
