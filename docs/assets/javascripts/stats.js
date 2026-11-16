/* ==========================================================================
   stats.js — the numerical core shared by every interactive lab
   --------------------------------------------------------------------------
   Pure functions only: no DOM, no globals beyond window.PSDSStats (and
   module.exports when loaded by Node for the test suite).

   Everything here is either exact in closed form or a converged special
   function; the only intentional approximations are:
     - the normal quantile, obtained by bisection on the CDF to 1e-12
       (so it is as accurate as the CDF itself, not a rational shortcut)
     - the power of the two-sample z-test, which is exact when sigma is known
       and is labelled as a z approximation when it is used for a t-test
   Each function is validated against SciPy in tests/labs.test.js.
   ========================================================================== */

(function (global) {
  "use strict";

  var LN_SQRT_2PI = 0.5 * Math.log(2 * Math.PI);

  /* ------------------------------------------------------------ special */

  /** Lanczos log-gamma (g = 7, n = 9), accurate to about 1e-15. */
  var LANCZOS = [
    0.99999999999980993, 676.5203681218851, -1259.1392167224028,
    771.32342877765313, -176.61502916214059, 12.507343278686905,
    -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7
  ];

  function lnGamma(x) {
    if (x < 0.5) {
      // Reflection: Gamma(x)Gamma(1-x) = pi / sin(pi x)
      return Math.log(Math.PI / Math.sin(Math.PI * x)) - lnGamma(1 - x);
    }
    x -= 1;
    var a = LANCZOS[0];
    var t = x + 7.5;
    for (var i = 1; i < 9; i++) a += LANCZOS[i] / (x + i);
    return 0.5 * Math.log(2 * Math.PI) + (x + 0.5) * Math.log(t) - t + Math.log(a);
  }

  function gammaQ(a, x) {
    return 1 - gammaP(a, x);
  }

  /** Regularised lower incomplete gamma P(a, x) (series + continued fraction). */
  function gammaP(a, x) {
    if (x <= 0) return 0;
    if (a <= 0) return NaN;
    if (x < a + 1) {
      // Series
      var ap = a;
      var sum = 1 / a;
      var del = sum;
      for (var n = 0; n < 1000; n++) {
        ap += 1;
        del *= x / ap;
        sum += del;
        if (Math.abs(del) < Math.abs(sum) * 1e-16) break;
      }
      return sum * Math.exp(-x + a * Math.log(x) - lnGamma(a));
    }
    return 1 - gammaQcf(a, x);
  }

  function gammaQcf(a, x) {
    var tiny = 1e-300;
    var b = x + 1 - a;
    var c = 1 / tiny;
    var d = 1 / b;
    var h = d;
    for (var i = 1; i <= 1000; i++) {
      var an = -i * (i - a);
      b += 2;
      d = an * d + b;
      if (Math.abs(d) < tiny) d = tiny;
      c = b + an / c;
      if (Math.abs(c) < tiny) c = tiny;
      d = 1 / d;
      var del = d * c;
      h *= del;
      if (Math.abs(del - 1) < 1e-16) break;
    }
    return Math.exp(-x + a * Math.log(x) - lnGamma(a)) * h;
  }

  function betaCf(a, b, x) {
    var tiny = 1e-300;
    var qab = a + b;
    var qap = a + 1;
    var qam = a - 1;
    var c = 1;
    var d = 1 - (qab * x) / qap;
    if (Math.abs(d) < tiny) d = tiny;
    d = 1 / d;
    var h = d;
    for (var m = 1; m <= 500; m++) {
      var m2 = 2 * m;
      var aa = (m * (b - m) * x) / ((qam + m2) * (a + m2));
      d = 1 + aa * d;
      if (Math.abs(d) < tiny) d = tiny;
      c = 1 + aa / c;
      if (Math.abs(c) < tiny) c = tiny;
      d = 1 / d;
      h *= d * c;
      aa = (-(a + m) * (qab + m) * x) / ((a + m2) * (qap + m2));
      d = 1 + aa * d;
      if (Math.abs(d) < tiny) d = tiny;
      c = 1 + aa / c;
      if (Math.abs(c) < tiny) c = tiny;
      d = 1 / d;
      var del = d * c;
      h *= del;
      if (Math.abs(del - 1) < 1e-16) break;
    }
    return h;
  }

  /** Regularised incomplete beta I_x(a, b). */
  function betaI(a, b, x) {
    if (x <= 0) return 0;
    if (x >= 1) return 1;
    var bt = Math.exp(
      lnGamma(a + b) - lnGamma(a) - lnGamma(b) + a * Math.log(x) + b * Math.log(1 - x)
    );
    if (x < (a + 1) / (a + b + 2)) return (bt * betaCf(a, b, x)) / a;
    return 1 - (bt * betaCf(b, a, 1 - x)) / b;
  }

  /* ------------------------------------------------------------- normal */

  function erf(x) {
    if (x < 0) return -gammaP(0.5, x * x);
    return gammaP(0.5, x * x);
  }

  function erfc(x) {
    if (x < 0) return 1 + gammaP(0.5, x * x);
    return gammaQ(0.5, x * x);
  }

  function normPdf(x, mu, sd) {
    mu = mu === undefined ? 0 : mu;
    sd = sd === undefined ? 1 : sd;
    var z = (x - mu) / sd;
    return Math.exp(-0.5 * z * z - LN_SQRT_2PI) / sd;
  }

  function normCdf(x, mu, sd) {
    mu = mu === undefined ? 0 : mu;
    sd = sd === undefined ? 1 : sd;
    return 0.5 * erfc(-(x - mu) / (sd * Math.SQRT2));
  }

  /** Upper tail P(Z > z). */
  function normSf(z) {
    return 0.5 * erfc(z / Math.SQRT2);
  }

  /** Quantile of N(0,1) by bisection on normCdf (accuracy 1e-12 in p). */
  function normInv(p) {
    if (!(p > 0 && p < 1)) {
      if (p === 0) return -Infinity;
      if (p === 1) return Infinity;
      return NaN;
    }
    var lo = -40;
    var hi = 40;
    for (var i = 0; i < 240; i++) {
      var mid = 0.5 * (lo + hi);
      if (normCdf(mid) < p) lo = mid;
      else hi = mid;
    }
    return 0.5 * (lo + hi);
  }

  /** Two-sided critical value for level (1 - alpha). */
  function zCrit(alpha) {
    return normInv(1 - alpha / 2);
  }

  /* --------------------------------------------------------- discrete */

  function lnChoose(n, k) {
    if (k < 0 || k > n) return -Infinity;
    return lnGamma(n + 1) - lnGamma(k + 1) - lnGamma(n - k + 1);
  }

  function choose(n, k) {
    if (k < 0 || k > n) return 0;
    k = Math.min(k, n - k);
    var out = 1;
    for (var i = 1; i <= k; i++) out = (out * (n - k + i)) / i;
    return Math.round(out);
  }

  function binomPmf(k, n, p) {
    if (k < 0 || k > n) return 0;
    if (p === 0) return k === 0 ? 1 : 0;
    if (p === 1) return k === n ? 1 : 0;
    return Math.exp(lnChoose(n, k) + k * Math.log(p) + (n - k) * Math.log(1 - p));
  }

  function binomCdf(k, n, p) {
    var out = 0;
    for (var j = 0; j <= k; j++) out += binomPmf(j, n, p);
    return Math.min(1, Math.max(0, out));
  }

  function poissonPmf(k, lambda) {
    if (k < 0) return 0;
    return Math.exp(-lambda + k * Math.log(lambda) - lnGamma(k + 1));
  }

  function poissonCdf(k, lambda) {
    var out = 0;
    for (var j = 0; j <= k; j++) out += poissonPmf(j, lambda);
    return Math.min(1, Math.max(0, out));
  }

  /* -------------------------------------------------------- continuous */

  function exponPdf(x, rate) {
    return x < 0 ? 0 : rate * Math.exp(-rate * x);
  }

  function exponCdf(x, rate) {
    return x < 0 ? 0 : 1 - Math.exp(-rate * x);
  }

  function gammaPdf(x, shape, rate) {
    if (x <= 0) return shape === 1 && x === 0 ? rate : 0;
    return Math.exp(
      shape * Math.log(rate) + (shape - 1) * Math.log(x) - rate * x - lnGamma(shape)
    );
  }

  function gammaCdf(x, shape, rate) {
    if (x <= 0) return 0;
    return gammaP(shape, rate * x);
  }

  function uniformPdf(x, a, b) {
    return x < a || x > b ? 0 : 1 / (b - a);
  }

  function uniformCdf(x, a, b) {
    if (x < a) return 0;
    if (x > b) return 1;
    return (x - a) / (b - a);
  }

  /* --------------------------------------------------------------- t, F */

  /** CDF of Student's t with df degrees of freedom. */
  function tCdf(t, df) {
    if (df <= 0) return NaN;
    var x = df / (df + t * t);
    var tail = 0.5 * betaI(df / 2, 0.5, x);
    return t >= 0 ? 1 - tail : tail;
  }

  function tSf(t, df) {
    return 1 - tCdf(t, df);
  }

  /** Two-sided p-value for a t statistic. */
  function tTwoSidedP(t, df) {
    return 2 * tSf(Math.abs(t), df);
  }

  /** Quantile of Student's t by bisection. */
  function tInv(p, df) {
    if (!(p > 0 && p < 1)) return NaN;
    var lo = -1e6;
    var hi = 1e6;
    for (var i = 0; i < 200; i++) {
      var mid = 0.5 * (lo + hi);
      if (tCdf(mid, df) < p) lo = mid;
      else hi = mid;
    }
    return 0.5 * (lo + hi);
  }

  function fCdf(f, d1, d2) {
    if (f <= 0) return 0;
    return betaI(d1 / 2, d2 / 2, (d1 * f) / (d1 * f + d2));
  }

  function fSf(f, d1, d2) {
    return 1 - fCdf(f, d1, d2);
  }

  /* --------------------------------------------------------- summaries */

  function mean(a) {
    if (!a.length) return NaN;
    var s = 0;
    for (var i = 0; i < a.length; i++) s += a[i];
    return s / a.length;
  }

  function sd(a, ddof) {
    var d = ddof === undefined ? 1 : ddof;
    var n = a.length;
    if (n - d <= 0) return NaN;
    var m = mean(a);
    var s = 0;
    for (var i = 0; i < n; i++) s += (a[i] - m) * (a[i] - m);
    return Math.sqrt(s / (n - d));
  }

  function variance(a, ddof) {
    var s = sd(a, ddof);
    return s * s;
  }

  function quantileSorted(sorted, q) {
    var n = sorted.length;
    if (!n) return NaN;
    if (n === 1) return sorted[0];
    var pos = (n - 1) * q;
    var lo = Math.floor(pos);
    var hi = Math.ceil(pos);
    return sorted[lo] + (pos - lo) * (sorted[hi] - sorted[lo]);
  }

  function median(a) {
    var s = a.slice().sort(function (x, y) {
      return x - y;
    });
    return quantileSorted(s, 0.5);
  }

  function correlation(x, y) {
    var n = Math.min(x.length, y.length);
    if (n < 2) return NaN;
    var mx = mean(x);
    var my = mean(y);
    var sxy = 0;
    var sxx = 0;
    var syy = 0;
    for (var i = 0; i < n; i++) {
      var dx = x[i] - mx;
      var dy = y[i] - my;
      sxy += dx * dy;
      sxx += dx * dx;
      syy += dy * dy;
    }
    return sxy / Math.sqrt(sxx * syy);
  }

  /** Ordinary least squares on (x, y). Returns slope, intercept, r, r2. */
  function ols(x, y) {
    var n = Math.min(x.length, y.length);
    var mx = mean(x);
    var my = mean(y);
    var sxy = 0;
    var sxx = 0;
    for (var i = 0; i < n; i++) {
      sxy += (x[i] - mx) * (y[i] - my);
      sxx += (x[i] - mx) * (x[i] - mx);
    }
    var slope = sxy / sxx;
    var intercept = my - slope * mx;
    var r = correlation(x, y);
    return { slope: slope, intercept: intercept, r: r, r2: r * r, n: n };
  }

  /** One-way ANOVA from an array of group arrays. */
  function anova(groups) {
    var k = groups.length;
    var N = 0;
    var grandSum = 0;
    groups.forEach(function (g) {
      N += g.length;
      g.forEach(function (v) {
        grandSum += v;
      });
    });
    var grand = grandSum / N;
    var ssb = 0;
    var ssw = 0;
    groups.forEach(function (g) {
      var m = mean(g);
      ssb += g.length * (m - grand) * (m - grand);
      g.forEach(function (v) {
        ssw += (v - m) * (v - m);
      });
    });
    var dfb = k - 1;
    var dfw = N - k;
    var msb = ssb / dfb;
    var msw = ssw / dfw;
    // Degenerate case: every observation identical. F is 0/0, which the
    // distribution theory leaves undefined; we report F = 0, p = 1 and flag it
    // so a caller can say so rather than printing NaN.
    var degenerate = msw === 0;
    var F = degenerate ? 0 : msb / msw;
    var p = degenerate ? 1 : fSf(F, dfb, dfw);
    return {
      k: k,
      N: N,
      grand: grand,
      ssb: ssb,
      ssw: ssw,
      sst: ssb + ssw,
      dfb: dfb,
      dfw: dfw,
      msb: msb,
      msw: msw,
      F: F,
      p: p,
      eta2: ssb + ssw === 0 ? 0 : ssb / (ssb + ssw),
      degenerate: degenerate
    };
  }

  /** Wilson score interval for a binomial proportion. */
  function wilson(k, n, z) {
    if (!n) return { lo: 0, hi: 1, centre: 0 };
    var p = k / n;
    var denom = 1 + (z * z) / n;
    var centre = (p + (z * z) / (2 * n)) / denom;
    var half =
      (z * Math.sqrt((p * (1 - p)) / n + (z * z) / (4 * n * n))) / denom;
    return { lo: Math.max(0, centre - half), hi: Math.min(1, centre + half), centre: centre };
  }

  global.PSDSStats = {
    lnGamma: lnGamma,
    gammaP: gammaP,
    gammaQ: gammaQ,
    betaI: betaI,
    erf: erf,
    erfc: erfc,
    normPdf: normPdf,
    normCdf: normCdf,
    normSf: normSf,
    normInv: normInv,
    zCrit: zCrit,
    choose: choose,
    lnChoose: lnChoose,
    binomPmf: binomPmf,
    binomCdf: binomCdf,
    poissonPmf: poissonPmf,
    poissonCdf: poissonCdf,
    exponPdf: exponPdf,
    exponCdf: exponCdf,
    gammaPdf: gammaPdf,
    gammaCdf: gammaCdf,
    uniformPdf: uniformPdf,
    uniformCdf: uniformCdf,
    tCdf: tCdf,
    tSf: tSf,
    tTwoSidedP: tTwoSidedP,
    tInv: tInv,
    fCdf: fCdf,
    fSf: fSf,
    mean: mean,
    sd: sd,
    variance: variance,
    median: median,
    quantileSorted: quantileSorted,
    correlation: correlation,
    ols: ols,
    anova: anova,
    wilson: wilson
  };

  if (typeof module !== "undefined" && module.exports) module.exports = global.PSDSStats;
})(typeof window !== "undefined" ? window : globalThis);
