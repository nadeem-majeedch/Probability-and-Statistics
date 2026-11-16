/* ==========================================================================
   labs-modelling.js — Labs L-11, L-12, L-13 and L-14
   --------------------------------------------------------------------------
   regression             correlation, least squares and inference on a slope
   bayes                  conjugate Beta–Binomial updating
   power                  Type I error, Type II error and statistical power
   anova                  one-way ANOVA across two to five groups
   ========================================================================== */

(function () {
  "use strict";

  var REG = window.PSDSLabs;
  if (!REG || !REG.utils) return;

  var U = REG.utils;
  var V = U.V;
  var S = window.PSDSStats;
  var K = REG.kit;
  var el = U.el;

  function slots(root) {
    return {
      controls: root.querySelector('[data-role="controls"]'),
      chart: root.querySelector('[data-role="chart"]'),
      readout: root.querySelector('[data-role="readout"]'),
      hint: root.querySelector('[data-role="hint"]'),
      results: root.querySelector('[data-role="results"]'),
      legend: root.querySelector('[data-role="legend"]')
    };
  }

  function seedOf(root, run) {
    var base = Number(root.getAttribute("data-seed") || 2026);
    return (base + 7919 * (run || 0)) >>> 0;
  }

  function buttons(parent, run, reset) {
    var box = el("div", "psds-lab__buttons", parent);
    U.button(box, "New run", null, run);
    U.button(box, "Reset", "psds-btn--ghost", reset);
    return box;
  }

  /* --------------------------------------------------- L-11 regression */

  function buildRegression(root) {
    var s = slots(root);
    if (!s.controls || !s.chart) return;
    V.clear(s.controls);
    V.clear(s.chart);

    // The correlation is not a free control: with a standardised predictor it is
    // implied by the slope and the residual SD, rho = b1 / sqrt(b1^2 + sigma^2).
    // The lab reports it rather than pretending the three can be set independently.
    var DEFAULTS = { slope: 1, intercept: 2, noise: 1, n: 40, run: 0 };
    var state = Object.assign({}, DEFAULTS);
    var svg = V.svgEl("svg", { width: 640, height: 340 }, s.chart);
    var table = K.table(s.results);

    var slopeField = U.slider(s.controls, {
      id: "reg-slope", label: "True slope β₁", min: -2, max: 2, step: 0.1, value: state.slope,
      format: function (v) { return v.toFixed(1); },
      onInput: function (v) { state.slope = v; changed(); }
    });
    var interceptField = U.slider(s.controls, {
      id: "reg-intercept", label: "True intercept β₀", min: -3, max: 3, step: 0.5, value: state.intercept,
      format: function (v) { return v.toFixed(1); },
      onInput: function (v) { state.intercept = v; changed(); }
    });
    var noiseField = U.slider(s.controls, {
      id: "reg-noise", label: "Residual SD σ", min: 0.2, max: 3, step: 0.2, value: state.noise,
      format: function (v) { return v.toFixed(1); },
      onInput: function (v) { state.noise = v; changed(); }
    });
    var nField = U.slider(s.controls, {
      id: "reg-n", label: "Sample size n", min: 8, max: 120, step: 2, value: state.n,
      onInput: function (v) { state.n = v; changed(); }
    });

    buttons(s.controls, function () { state.run += 1; draw(); }, function () {
      state = Object.assign({}, DEFAULTS);
      slopeField.set(state.slope); interceptField.set(state.intercept);
      noiseField.set(state.noise); nField.set(state.n);
      draw();
    });

    K.legend(s.legend, [
      { label: "observed data", colour: "ink", kind: "dot" },
      { label: "least-squares fit ŷ = b₀ + b₁x", colour: "accent", kind: "line" },
      { label: "true generating line", colour: "teal", kind: "line" }
    ]);

    function changed() {
      s.hint.textContent = "Settings changed — press New run to draw a new sample.";
    }

    function draw() {
      var r = V.rng(seedOf(root, state.run));
      var n = state.n;
      var sigma = state.noise;
      // The predictor is standard normal, so the population correlation implied
      // by the slope and the residual SD is b1 / sqrt(b1^2 + sigma^2).
      var rho = state.slope / Math.sqrt(state.slope * state.slope + sigma * sigma);
      var xs = new Array(n);
      var ys = new Array(n);
      for (var i = 0; i < n; i++) {
        var x = U.gauss(r);
        xs[i] = x;
        ys[i] = state.intercept + state.slope * x + sigma * U.gauss(r);
      }
      var fit = S.ols(xs, ys);
      var n2 = fit.n;
      var sse = 0;
      var sxx = 0;
      var mx = S.mean(xs);
      for (var j = 0; j < n2; j++) {
        var res = ys[j] - (fit.intercept + fit.slope * xs[j]);
        sse += res * res;
        sxx += (xs[j] - mx) * (xs[j] - mx);
      }
      var df = n2 - 2;
      var seSlope = Math.sqrt(sse / df / sxx);
      var tSlope = fit.slope / seSlope;
      var pSlope = S.tTwoSidedP(tSlope, df);
      var tCrit = S.tInv(0.975, df);

      var xlo = -3.2, xhi = 3.2;
      var ymin = Infinity, ymax = -Infinity;
      for (var k = 0; k < n2; k++) {
        ymin = Math.min(ymin, ys[k]);
        ymax = Math.max(ymax, ys[k]);
      }
      ymin = Math.min(ymin, fit.intercept + fit.slope * xlo);
      ymax = Math.max(ymax, fit.intercept + fit.slope * xhi);
      var pad = 0.1 * (ymax - ymin || 1);

      V.clear(svg);
      var f = V.frame(svg, {
        width: 640, height: 340,
        xDomain: [xlo, xhi],
        yDomain: [ymin - pad, ymax + pad],
        xLabel: "predictor x",
        yFormat: function (v) { return v.toFixed(1); }
      });
      for (var m = 0; m < n2; m++) {
        V.svgEl("circle", {
          cx: f.x(xs[m]), cy: f.y(ys[m]), r: 2.6, class: "dot"
        }, f.marks);
      }
      K.curve(f.marks, f, function (x) {
        return state.intercept + state.slope * x;
      }, xlo, xhi, "curve curve--true", 2);
      K.curve(f.marks, f, function (x) {
        return fit.intercept + fit.slope * x;
      }, xlo, xhi, "curve", 2);

      U.setAria(
        svg,
        "Scatter plot of " + n2 + " points with the least-squares line. The observed correlation is " +
          K.num(fit.r, 3) + ", the fitted slope " + K.num(fit.slope, 3) +
          " with p = " + K.num(pSlope, 4) + ", against a true slope of " + K.num(state.slope, 2) + "."
      );

      s.readout.textContent =
        "n = " + n2 + "  ·  r = " + K.num(fit.r, 3) + " (implied ρ = " + K.num(rho, 2) + ")" +
        "  ·  b₁ = " + K.num(fit.slope, 3) + " (true " + K.num(state.slope, 2) + ")" +
        "  ·  b₀ = " + K.num(fit.intercept, 3) +
        "  ·  R² = " + K.num(fit.r2, 3) + "  ·  p = " + K.num(pSlope, 4);

      table && table.set([
        ["correlation r", K.num(fit.r, 4) + " (implied population ρ = " + K.num(rho, 3) + ")"],
        ["least-squares slope b₁", K.num(fit.slope, 4)],
        ["least-squares intercept b₀", K.num(fit.intercept, 4)],
        ["R²", K.num(fit.r2, 4)],
        ["standard error of b₁", K.num(seSlope, 4)],
        ["95 % CI for β₁", "[" + K.num(fit.slope - tCrit * seSlope, 3) + ", " +
          K.num(fit.slope + tCrit * seSlope, 3) + "]"],
        ["t for H₀: β₁ = 0", K.num(tSlope, 3) + " on " + df + " df"],
        ["two-sided p-value", K.num(pSlope, 4)]
      ]);

      s.hint.textContent =
        "R² = " + K.num(fit.r2, 3) + " is the share of the variation in y explained by x, and the slope " +
        "is " + K.num(fit.slope, 2) + " units of y per unit of x. Raise the residual SD and the slope " +
        "estimate gets noisier even though the true slope has not moved — that is what the standard " +
        "error is measuring. A large R² with n = 8 can still have a p-value above 0.05.";
    }

    draw();
  }

  /* --------------------------------------------------------- L-12 Bayes */

  function buildBayes(root) {
    var s = slots(root);
    if (!s.controls || !s.chart) return;
    V.clear(s.controls);
    V.clear(s.chart);

    var DEFAULTS = { priorMean: 0.3, strength: 4, truth: 0.35, batch: 40 };
    var state = Object.assign({}, DEFAULTS);
    var observed = { successes: 0, trials: 0 };
    var svg = V.svgEl("svg", { width: 640, height: 330 }, s.chart);
    var table = K.table(s.results);

    function betaPdf(x, a, b) {
      if (x <= 0 || x >= 1) return 0;
      var lb = S.lnGamma(a + b) - S.lnGamma(a) - S.lnGamma(b);
      return Math.exp(lb + (a - 1) * Math.log(x) + (b - 1) * Math.log(1 - x));
    }

    var meanField = U.slider(s.controls, {
      id: "bayes-mean", label: "Prior mean", min: 0.05, max: 0.95, step: 0.05,
      value: state.priorMean, format: function (v) { return v.toFixed(2); },
      onInput: function (v) { state.priorMean = v; observed = { successes: 0, trials: 0 }; draw(); }
    });
    var strengthField = U.slider(s.controls, {
      id: "bayes-strength", label: "Prior strength (pseudo-observations)", min: 2, max: 40, step: 2,
      value: state.strength,
      onInput: function (v) { state.strength = v; observed = { successes: 0, trials: 0 }; draw(); }
    });
    var truthField = U.slider(s.controls, {
      id: "bayes-truth", label: "True rate (unknown to the analyst)", min: 0.05, max: 0.9, step: 0.05,
      value: state.truth, format: function (v) { return v.toFixed(2); },
      onInput: function (v) { state.truth = v; observed = { successes: 0, trials: 0 }; draw(); }
    });
    var batchField = U.slider(s.controls, {
      id: "bayes-batch", label: "Observations per update", min: 10, max: 200, step: 10,
      value: state.batch,
      onInput: function (v) { state.batch = v; }
    });

    var box = el("div", "psds-lab__buttons", s.controls);
    U.button(box, "Observe another batch", null, function () {
      var r = V.rng(seedOf(root, observed.trials));
      var k = 0;
      for (var i = 0; i < state.batch; i++) if (r() < state.truth) k += 1;
      observed.successes += k;
      observed.trials += state.batch;
      draw();
    });
    U.button(box, "Reset evidence", "psds-btn--ghost", function () {
      observed = { successes: 0, trials: 0 };
      state = Object.assign({}, DEFAULTS);
      meanField.set(state.priorMean);
      strengthField.set(state.strength);
      truthField.set(state.truth);
      batchField.set(state.batch);
      draw();
    });

    K.legend(s.legend, [
      { label: "prior Beta(a, b)", colour: "teal", kind: "line" },
      { label: "likelihood (scaled to the posterior peak)", colour: "ink", kind: "line" },
      { label: "posterior Beta(a + k, b + n − k)", colour: "accent", kind: "line" }
    ]);

    function draw() {
      var a0 = state.priorMean * state.strength;
      var b0 = state.strength - a0;
      var a = a0 + observed.successes;
      var b = b0 + (observed.trials - observed.successes);
      var postMean = a / (a + b);
      var postSd = Math.sqrt((a * b) / ((a + b) * (a + b) * (a + b + 1)));
      // 95 % credible interval by numeric inversion of the Beta CDF.
      function betaCdf(x) {
        if (x <= 0) return 0;
        if (x >= 1) return 1;
        return S.betaI(a, b, x);
      }
      var lo = 0, hi = 1;
      for (var i = 0; i < 60; i++) {
        var m1 = 0.5 * (lo + hi);
        if (betaCdf(m1) < 0.025) lo = m1; else hi = m1;
      }
      var qLo = 0.5 * (lo + hi);
      lo = 0; hi = 1;
      for (var j = 0; j < 60; j++) {
        var m2 = 0.5 * (lo + hi);
        if (betaCdf(m2) < 0.975) lo = m2; else hi = m2;
      }
      var qHi = 0.5 * (lo + hi);

      var peak = 0;
      [a0, a, 1 + observed.successes, 1 + (observed.trials - observed.successes)].forEach(function () {});
      for (var t = 0.001; t < 1; t += 0.002) {
        peak = Math.max(peak, betaPdf(t, a0, b0), betaPdf(t, a, b));
      }
      peak = Math.max(peak, 1.5);

      V.clear(svg);
      var f = V.frame(svg, {
        width: 640, height: 330,
        xDomain: [0, 1],
        yDomain: [0, peak * 1.35],
        xLabel: "conversion rate θ (unknown parameter)",
        yFormat: function (v) { return v.toFixed(1); }
      });
      K.curve(f.marks, f, function (x) { return betaPdf(x, a0, b0); }, 0.002, 0.998, "curve curve--prior", 300);
      K.area(f.marks, f, function (x) { return betaPdf(x, a, b); }, qLo, qHi, "area area--faint");
      K.curve(f.marks, f, function (x) { return betaPdf(x, a, b); }, 0.002, 0.998, "curve", 300);
      if (observed.trials > 0) {
        var phat = observed.successes / observed.trials;
        var lpeak = betaPdf(Math.min(0.999, Math.max(0.001, phat)), a, b) * 0.55 + 0.15;
        K.vline(f.marks, f, phat, "reference reference--accent");
        K.text(f.marks, f, phat, peak * 1.12, "data: " + K.num(phat, 2), "label", "middle");
      }
      K.vline(f.marks, f, postMean, "reference");
      K.text(f.marks, f, postMean, peak * 1.24,
             "posterior mean " + K.num(postMean, 2), "label label--strong", "middle");

      U.setAria(
        svg,
        "Beta prior and posterior densities for a rate. After " + observed.trials + " observations with " +
          observed.successes + " successes the posterior mean is " + K.num(postMean, 3) +
          " with a 95 percent credible interval from " + K.num(qLo, 3) + " to " + K.num(qHi, 3) + "."
      );

      s.readout.textContent =
        "prior Beta(" + K.num(a0, 1) + ", " + K.num(b0, 1) + ")  ·  evidence " +
        observed.successes + "/" + observed.trials +
        "  ·  posterior Beta(" + K.num(a, 1) + ", " + K.num(b, 1) + ")" +
        "  ·  posterior mean = " + K.num(postMean, 3) +
        "  ·  95 % credible interval [" + K.num(qLo, 3) + ", " + K.num(qHi, 3) + "]" +
        "  ·  P(next success | data) = " + K.num(postMean, 3);

      table && table.set([
        ["prior mean", K.num(a0 / (a0 + b0), 3) + " with strength " + K.num(a0 + b0, 0)],
        ["data", observed.successes + " successes in " + observed.trials + " trials"],
        ["likelihood peak (MLE)", observed.trials ? K.num(observed.successes / observed.trials, 3) : "—"],
        ["posterior mean", K.num(postMean, 4)],
        ["posterior SD", K.num(postSd, 4)],
        ["95 % credible interval", "[" + K.num(qLo, 3) + ", " + K.num(qHi, 3) + "]"],
        ["posterior predictive", K.num(postMean, 3)],
        ["credible interval width", K.num(qHi - qLo, 3)]
      ]);

      s.hint.textContent = observed.trials === 0
        ? "No data yet, so the posterior is the prior. Add a batch and watch the curve move: with a " +
          "weak prior it jumps to the data, with a strong prior it resists."
        : "The posterior is a compromise between the prior and the data, weighted by how much evidence " +
          "there is: the prior counts as " + K.num(a0 + b0, 0) + " pseudo-observations against " +
          observed.trials + " real ones. The interval narrows as evidence accumulates, and the posterior " +
          "mean converges on the true rate " + K.num(state.truth, 2) + " whatever the prior said at the start.";
    }

    draw();
  }

  /* --------------------------------------------------------- L-13 power */

  function buildPower(root) {
    var s = slots(root);
    if (!s.controls || !s.chart) return;
    V.clear(s.controls);
    V.clear(s.chart);

    var DEFAULTS = { d: 0.5, n: 30, alpha: 0.05, side: "two" };
    var state = Object.assign({}, DEFAULTS);
    var svg = V.svgEl("svg", { width: 640, height: 320 }, s.chart);
    var table = K.table(s.results);

    var dField = U.slider(s.controls, {
      id: "power-d", label: "Effect size d = δ/σ", min: 0, max: 1.5, step: 0.05,
      value: state.d, format: function (v) { return v.toFixed(2); },
      onInput: function (v) { state.d = v; draw(); }
    });
    var nField = U.slider(s.controls, {
      id: "power-n", label: "Sample size n", min: 5, max: 300, step: 5, value: state.n,
      onInput: function (v) { state.n = v; draw(); }
    });
    var alphaField = U.select(s.controls, {
      label: "Significance level α", value: String(state.alpha),
      options: [{ value: "0.01", label: "0.01" }, { value: "0.05", label: "0.05" }, { value: "0.10", label: "0.10" }],
      onChange: function (v) { state.alpha = Number(v); draw(); }
    });
    var sideField = U.select(s.controls, {
      label: "Alternative hypothesis", value: state.side,
      options: [
        { value: "two", label: "two-sided μ ≠ 0" },
        { value: "greater", label: "one-sided μ > 0" }
      ],
      onChange: function (v) { state.side = v; draw(); }
    });

    buttons(s.controls, function () { draw(); }, function () {
      state = Object.assign({}, DEFAULTS);
      dField.set(state.d); nField.set(state.n);
      alphaField.set(String(state.alpha)); sideField.set(state.side);
      draw();
    });

    K.legend(s.legend, [
      { label: "H₀ true (μ = 0)", colour: "teal", kind: "line" },
      { label: "H₁ true (μ = δ)", colour: "accent", kind: "line" },
      { label: "α and β are areas, not opinions", colour: "band", kind: "bar" }
    ]);

    function powerFor(d, n, alpha, side) {
      var shift = d * Math.sqrt(n);
      var zc = side === "two" ? S.zCrit(alpha) : S.normInv(1 - alpha);
      var pow = side === "two"
        ? S.normCdf(shift - zc) + S.normCdf(-shift - zc)
        : S.normCdf(shift - zc);
      return { power: pow, zc: zc, shift: shift };
    }

    function draw() {
      var n = state.n;
      var d = state.d;
      var alpha = state.alpha;
      var p = powerFor(d, n, alpha, state.side);
      var se = 1 / Math.sqrt(n);

      var lo = -4 * se - 0.0;
      var hi = d + 4 * se;
      var pad = 0.15 * (hi - lo);
      lo -= pad;
      hi += pad;

      V.clear(svg);
      var f = V.frame(svg, {
        width: 640, height: 320,
        xDomain: [lo, hi],
        yDomain: [0, S.normPdf(0, 0, se) * 1.3],
        xLabel: "sample mean x̄ under H₀ (left curve) and under H₁ (right curve), SE = " + K.num(se, 3),
        yFormat: function () { return ""; }
      });
      var critHigh = p.zc * se;
      var critLow = -p.zc * se;

      K.area(f.marks, f, function (x) { return S.normPdf(x, 0, se); },
             critHigh, hi, "area area--accent");
      if (state.side === "two") {
        K.area(f.marks, f, function (x) { return S.normPdf(x, 0, se); },
               lo, critLow, "area area--accent");
      }
      K.area(f.marks, f, function (x) { return S.normPdf(x, d, se); },
             lo, critHigh, "area area--beta");
      K.curve(f.marks, f, function (x) { return S.normPdf(x, 0, se); }, lo, hi, "curve", 260);
      K.curve(f.marks, f, function (x) { return S.normPdf(x, d, se); }, lo, hi, "curve curve--h1", 260);
      K.vline(f.marks, f, critHigh, "reference");
      K.text(f.marks, f, 0, S.normPdf(0, 0, se) * 1.1, "H₀: μ = 0", "label label--strong", "middle");
      K.text(f.marks, f, d, S.normPdf(d, d, se) * 1.1, "H₁: μ = δ", "label label--strong", "middle");
      K.text(f.marks, f, critHigh, S.normPdf(critHigh, 0, se) * 0.45,
             "critical " + K.num(critHigh, 2), "label", "start");

      U.setAria(
        svg,
        "Two sampling distributions of the sample mean: under the null hypothesis centred at zero and " +
          "under the alternative centred at " + K.num(d, 2) + ". With n = " + n + ", alpha = " + alpha +
          ", the rejection region starts at " + K.num(critHigh, 3) + " and the power is " + K.pct(p.power) + "."
      );

      s.readout.textContent =
        "d = " + K.num(d, 2) + "  ·  n = " + n + "  ·  α = " + alpha +
        "  ·  critical x̄ = " + K.num(critHigh, 3) +
        "  ·  power = " + K.pct(p.power) + "  ·  β = " + K.pct(1 - p.power);

      var n80 = 1;
      for (var k = 1; k <= 5000; k++) {
        if (powerFor(d, k, alpha, state.side).power >= 0.8) { n80 = k; break; }
      }

      table && table.set([
        ["α, Type I error rate", K.num(alpha, 2)],
        ["β, Type II error rate", K.num(1 - p.power, 3)],
        ["power = 1 − β", K.num(p.power, 3)],
        ["standard error σ/√n", K.num(se, 4)],
        ["critical value on the x̄ scale", K.num(critHigh, 4)],
        ["n needed for 80 % power at this d", d > 0 ? n80 : "impossible at d = 0"],
        ["n needed for 90 % power at this d", d > 0 ? (function () {
          for (var k2 = 1; k2 <= 5000; k2++) {
            if (powerFor(d, k2, alpha, state.side).power >= 0.9) return k2;
          }
          return "> 5000";
        })() : "impossible at d = 0"],
        ["note", "z approximation — exact when σ is known"]
      ]);

      s.hint.textContent = d === 0
        ? "With no effect, power equals α and every rejection is a Type I error. There is no sample " +
          "size that fixes this: α is a decision you make, not a property of the data."
        : "A Type I error rejects a true H₀ (rate α = " + alpha + "); a Type II error keeps a false H₀ " +
          "(rate β = " + K.num(1 - p.power, 3) + "). Power is " + K.pct(p.power) +
          ", so this design would miss a real effect of " + K.num(d, 2) + " SD about " +
          K.pct(1 - p.power) + " of the time. Lower α and power falls; raise n and both α and β stay put " +
          "while power climbs — because the curves separate as the standard error shrinks.";
    }

    draw();
  }

  /* --------------------------------------------------------- L-14 ANOVA */

  function buildAnova(root) {
    var s = slots(root);
    if (!s.controls || !s.chart) return;
    V.clear(s.controls);
    V.clear(s.chart);

    var DEFAULTS = { k: 4, gap: 0.6, within: 1, n: 12, run: 0 };
    var state = Object.assign({}, DEFAULTS);
    var svg = V.svgEl("svg", { width: 640, height: 340 }, s.chart);
    var table = K.table(s.results);

    var kField = U.slider(s.controls, {
      id: "anova-k", label: "Number of groups k", min: 2, max: 5, step: 1, value: state.k,
      onInput: function (v) { state.k = v; changed(); }
    });
    var gapField = U.slider(s.controls, {
      id: "anova-gap", label: "Between-group separation", min: 0, max: 2, step: 0.1,
      value: state.gap, format: function (v) { return v.toFixed(1); },
      onInput: function (v) { state.gap = v; changed(); }
    });
    var withinField = U.slider(s.controls, {
      id: "anova-within", label: "Within-group SD σ", min: 0.2, max: 3, step: 0.2,
      value: state.within, format: function (v) { return v.toFixed(1); },
      onInput: function (v) { state.within = v; changed(); }
    });
    var nField = U.slider(s.controls, {
      id: "anova-n", label: "Sample size per group", min: 3, max: 40, step: 1, value: state.n,
      onInput: function (v) { state.n = v; changed(); }
    });

    buttons(s.controls, function () { state.run += 1; draw(); }, function () {
      state = Object.assign({}, DEFAULTS);
      kField.set(state.k); gapField.set(state.gap); withinField.set(state.within); nField.set(state.n);
      draw();
    });

    K.legend(s.legend, [
      { label: "observations", colour: "ink", kind: "dot" },
      { label: "group mean", colour: "accent", kind: "line" },
      { label: "grand mean", colour: "teal", kind: "line" }
    ]);

    function changed() {
      s.hint.textContent = "Settings changed — press New run to draw new samples.";
    }

    function draw() {
      var r = V.rng(seedOf(root, state.run));
      var k = state.k;
      var groups = [];
      var means = [];
      for (var g = 0; g < k; g++) {
        var centre = state.gap * (g - (k - 1) / 2);
        var arr = new Array(state.n);
        for (var i = 0; i < state.n; i++) arr[i] = centre + state.within * U.gauss(r);
        groups.push(arr);
        means.push(S.mean(arr));
      }
      var res = S.anova(groups);
      var fCrit = (function () {
        var lo = 0, hi = 50;
        for (var j = 0; j < 200; j++) {
          var mid = 0.5 * (lo + hi);
          if (S.fCdf(mid, res.dfb, res.dfw) < 0.95) lo = mid; else hi = mid;
        }
        return 0.5 * (lo + hi);
      })();

      var ymin = Infinity, ymax = -Infinity;
      groups.forEach(function (arr) {
        arr.forEach(function (v) {
          ymin = Math.min(ymin, v);
          ymax = Math.max(ymax, v);
        });
      });
      var pad = 0.1 * (ymax - ymin || 1);

      V.clear(svg);
      var f = V.frame(svg, {
        width: 640, height: 340,
        xDomain: [-0.6, k - 0.4],
        yDomain: [ymin - pad, ymax + pad],
        xLabel: "group",
        xFormat: function (v) { return Number.isInteger(v) ? String.fromCharCode(65 + v) : ""; },
        yFormat: function (v) { return v.toFixed(1); }
      });
      K.hline(f.marks, f, res.grand, "reference reference--grand");
      groups.forEach(function (arr, g) {
        arr.forEach(function (v, i) {
          var jitter = ((i % 5) - 2) * 0.055;
          V.svgEl("circle", {
            cx: f.x(g + jitter), cy: f.y(v), r: 2.6, class: "dot"
          }, f.marks);
        });
        V.svgEl("line", {
          x1: f.x(g - 0.28), x2: f.x(g + 0.28),
          y1: f.y(means[g]), y2: f.y(means[g]),
          class: "reference reference--accent"
        }, f.marks);
        K.text(f.marks, f, g + 0.34, means[g], K.num(means[g], 1), "label");
      });
      K.text(f.marks, f, k - 0.45, res.grand, "grand mean", "label", "end");

      U.setAria(
        svg,
        "Dot plot of " + k + " groups with " + state.n + " observations each. Group means are " +
          means.map(function (m) { return K.num(m, 1); }).join(", ") +
          ". The one-way ANOVA gives F = " + K.num(res.F, 3) + " with p = " + K.num(res.p, 4) + "."
      );

      s.readout.textContent =
        "k = " + k + "  ·  n per group = " + state.n + "  ·  F(" + res.dfb + ", " + res.dfw + ") = " +
        K.num(res.F, 3) + "  ·  p = " + K.num(res.p, 4) + "  ·  η² = " + K.num(res.eta2, 3) +
        "  ·  critical F at 5 % = " + K.num(fCrit, 3);

      table && table.set([
        ["group means", means.map(function (m) { return K.num(m, 2); }).join(" · ")],
        ["between-group SS", K.num(res.ssb, 3) + " on " + res.dfb + " df"],
        ["within-group SS", K.num(res.ssw, 3) + " on " + res.dfw + " df"],
        ["MS between / MS within", K.num(res.msb, 3) + " / " + K.num(res.msw, 3)],
        ["F statistic", K.num(res.F, 4)],
        ["p-value", K.num(res.p, 5)],
        ["η² (share of variation explained)", K.num(res.eta2, 4)],
        ["critical F at 5 %", K.num(fCrit, 3)]
      ]);

      s.hint.textContent = res.p < 0.05
        ? "F = " + K.num(res.F, 2) + " is larger than the 5 % critical value " + K.num(fCrit, 2) +
          ": the group means differ by more than within-group noise would explain. But η² = " +
          K.num(res.eta2, 2) + " says how much of the variation that difference accounts for — a small p-value " +
          "with η² = 0.05 is a real but minor effect."
        : "F = " + K.num(res.F, 2) + " is below the 5 % critical value " + K.num(fCrit, 2) +
          ": this sample does not show a difference between the groups. With 5 groups and 3 observations " +
          "each, a real difference of this size is easy to miss — that is a power problem, not evidence " +
          "that the groups are identical.";
    }

    draw();
  }

  REG.builders.regression = buildRegression;
  REG.builders.bayes = buildBayes;
  REG.builders.power = buildPower;
  REG.builders.anova = buildAnova;
})();
