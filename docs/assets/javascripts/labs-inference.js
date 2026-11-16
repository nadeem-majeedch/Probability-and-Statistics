/* ==========================================================================
   labs-inference.js — Labs L-05, L-06, L-08 and L-10
   --------------------------------------------------------------------------
   normal                 normal distribution, z-scores and the empirical rule
   lln                    the law of large numbers, including a failure case
   sampling               sampling distributions and the standard error
   pvalues                hypothesis tests, p-values and rejection rates
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

  /* ------------------------------------------------------- L-05 normal */

  function buildNormal(root) {
    var s = slots(root);
    if (!s.controls || !s.chart) return;
    V.clear(s.controls);
    V.clear(s.chart);

    var DEFAULTS = { mu: 70, sigma: 8, x: 82, draws: 2000, run: 0 };
    var state = Object.assign({}, DEFAULTS);
    var svg = V.svgEl("svg", { width: 640, height: 300 }, s.chart);
    var table = K.table(s.results);

    var muField = U.slider(s.controls, {
      id: "norm-mu", label: "Population mean μ", min: 40, max: 100, step: 1, value: state.mu,
      onInput: function (v) { state.mu = v; changed(); }
    });
    var sdField = U.slider(s.controls, {
      id: "norm-sd", label: "Population SD σ", min: 2, max: 20, step: 1, value: state.sigma,
      onInput: function (v) { state.sigma = v; changed(); }
    });
    var xField = U.slider(s.controls, {
      id: "norm-x", label: "Observed value x", min: 30, max: 110, step: 1, value: state.x,
      onInput: function (v) { state.x = v; changed(); }
    });
    var dField = U.slider(s.controls, {
      id: "norm-draws", label: "Check with draws", min: 500, max: 5000, step: 500, value: state.draws,
      onInput: function (v) { state.draws = v; changed(); }
    });

    buttons(s.controls, function () { state.run += 1; draw(); }, function () {
      state = Object.assign({}, DEFAULTS);
      muField.set(state.mu); sdField.set(state.sigma); xField.set(state.x); dField.set(state.draws);
      draw();
    });

    K.legend(s.legend, [
      { label: "shaded: P(X ≤ x)", colour: "band", kind: "bar" },
      { label: "density", colour: "teal", kind: "line" },
      { label: "μ and x", colour: "accent", kind: "line" }
    ]);

    function changed() {
      s.hint.textContent = "Settings changed — press New run to recheck the empirical rule.";
    }

    function draw() {
      var mu = state.mu;
      var sd = state.sigma;
      var x = state.x;
      var z = (x - mu) / sd;
      var pBelow = S.normCdf(z);

      var r = V.rng(seedOf(root, state.run));
      var draws = state.draws;
      var within1 = 0, within2 = 0, within3 = 0;
      for (var i = 0; i < draws; i++) {
        var v = mu + sd * U.gauss(r);
        var d = Math.abs(v - mu);
        if (d <= sd) within1 += 1;
        if (d <= 2 * sd) within2 += 1;
        if (d <= 3 * sd) within3 += 1;
      }

      var lo = mu - 4 * sd;
      var hi = mu + 4 * sd;
      V.clear(svg);
      var f = V.frame(svg, {
        width: 640, height: 300,
        xDomain: [lo, hi],
        yDomain: [0, S.normPdf(mu, mu, sd) * 1.22],
        xLabel: "x   (z = (x − μ)/σ, so the same curve has μ = 0 and σ = 1 on the z axis)",
        yFormat: function (v) { return v.toFixed(3); }
      });
      K.area(f.marks, f, function (t) { return S.normPdf(t, mu, sd); }, lo, x, "area");
      K.curve(f.marks, f, function (t) { return S.normPdf(t, mu, sd); }, lo, hi, "curve", 240);
      K.vline(f.marks, f, mu, "reference");
      V.svgEl("line", {
        x1: f.x(x), x2: f.x(x), y1: f.margin.top,
        y2: f.margin.top + f.plotH, class: "reference reference--accent"
      }, f.marks);
      K.text(f.marks, f, mu, 0, "μ = " + mu, "label", "middle");
      K.text(f.marks, f, x, S.normPdf(x, mu, sd) * 0.72, "x = " + x, "label label--strong", "middle");
      K.text(f.marks, f, lo + 0.12 * (hi - lo), S.normPdf(mu, mu, sd) * 1.06,
             "z = " + K.num(z, 2) + "   percentile " + K.num(100 * pBelow, 1), "label label--strong");

      U.setAria(
        svg,
        "Normal curve with mean " + mu + " and standard deviation " + sd +
          ". The area to the left of x = " + x + " is " + K.num(pBelow, 3) +
          ", which corresponds to z = " + K.num(z, 2) + "."
      );

      var e1 = within1 / draws, e2 = within2 / draws, e3 = within3 / draws;
      s.readout.textContent =
        "μ = " + mu + "  ·  σ = " + sd + "  ·  x = " + x + "  ·  z = " + K.num(z, 3) +
        "  ·  P(X ≤ x) = " + K.num(pBelow, 4) +
        "  ·  empirical 68/95/99.7: " + K.pct(e1) + " / " + K.pct(e2) + " / " + K.pct(e3);

      table && table.set([
        ["z-score", K.num(z, 4)],
        ["percentile from z", K.num(100 * pBelow, 2) + "%"],
        ["P(X ≤ x)", K.num(pBelow, 4)],
        ["P(X > x)", K.num(1 - pBelow, 4)],
        ["P(|X − μ| ≤ σ)", "0.6827 · observed " + K.pct(e1)],
        ["P(|X − μ| ≤ 2σ)", "0.9545 · observed " + K.pct(e2)],
        ["P(|X − μ| ≤ 3σ)", "0.9973 · observed " + K.pct(e3)],
        ["draws used", draws.toLocaleString()]
      ]);

      s.hint.textContent =
        "A z-score is a change of units, not a change of shape: moving μ slides the curve and " +
        "changing σ stretches it, while z = " + K.num(z, 2) + " stays the position in standard " +
        "deviations. The empirical counts land near 68 / 95 / 99.7 %; the gap is sampling error " +
        "of about " + K.num(100 * Math.sqrt(0.68 * 0.32 / draws), 2) + " percentage points.";
    }

    draw();
  }

  /* ---------------------------------------------------------- L-06 LLN */

  function buildLln(root) {
    var s = slots(root);
    if (!s.controls || !s.chart) return;
    V.clear(s.controls);
    V.clear(s.chart);

    var POPS = {
      uniform: {
        label: "Uniform on [0, 2]",
        mean: 1,
        sd: 1 / Math.sqrt(3),
        draw: function (r) { return 2 * r(); }
      },
      exponential: {
        label: "Exponential, rate 1",
        mean: 1,
        sd: 1,
        draw: function (r) { return -Math.log(Math.max(1e-12, 1 - r())); }
      },
      cauchy: {
        label: "Cauchy (no mean)",
        mean: NaN,
        sd: NaN,
        draw: function (r) { return Math.tan(Math.PI * (r() - 0.5)); }
      }
    };

    var DEFAULTS = { pop: "exponential", trials: 5000, run: 0 };
    var state = Object.assign({}, DEFAULTS);
    var svg = V.svgEl("svg", { width: 640, height: 320 }, s.chart);
    var table = K.table(s.results);

    var popSel = U.select(s.controls, {
      label: "Population",
      value: state.pop,
      options: Object.keys(POPS).map(function (k) {
        return { value: k, label: POPS[k].label };
      }),
      onChange: function (v) { state.pop = v; draw(); }
    });
    var tField = U.slider(s.controls, {
      id: "lln-trials", label: "Trials", min: 200, max: 20000, step: 200, value: state.trials,
      onInput: function (v) { state.trials = v; draw(); }
    });

    buttons(s.controls, function () { state.run += 1; draw(); }, function () {
      state = Object.assign({}, DEFAULTS);
      popSel.set(state.pop); tField.set(state.trials);
      draw();
    });

    K.legend(s.legend, [
      { label: "running average x̄ₙ", colour: "teal", kind: "line" },
      { label: "population mean μ (when it exists)", colour: "accent", kind: "line" }
    ]);

    function draw() {
      var pop = POPS[state.pop];
      var r = V.rng(seedOf(root, state.run));
      var n = state.trials;
      var running = new Array(n);
      var sum = 0;
      for (var i = 0; i < n; i++) {
        sum += pop.draw(r);
        running[i] = sum / (i + 1);
      }
      var final = running[n - 1];
      var finite = isFinite(pop.mean);

      var lo = 0;
      var hi = n;
      var vals = running.slice(Math.max(0, Math.floor(n / 20)));
      var vmin = Math.min.apply(null, vals);
      var vmax = Math.max.apply(null, vals);
      if (finite) {
        vmin = Math.min(vmin, pop.mean - 0.6 * pop.sd);
        vmax = Math.max(vmax, pop.mean + 0.6 * pop.sd);
      }
      if (!isFinite(vmin) || !isFinite(vmax) || vmax === vmin) {
        vmin = -2;
        vmax = 2;
      }
      var pad = 0.12 * (vmax - vmin);

      V.clear(svg);
      var f = V.frame(svg, {
        width: 640, height: 320,
        xDomain: [lo, hi],
        yDomain: [vmin - pad, vmax + pad],
        xLabel: "number of observations n (log axis to the eye: early wobble, later calm)",
        yFormat: function (v) { return v.toFixed(2); }
      });
      if (finite) K.hline(f.marks, f, pop.mean, "reference reference--accent");
      var pts = [];
      var stride = Math.max(1, Math.floor(n / 600));
      for (var j = 0; j < n; j += stride) pts.push([f.x(j + 1), f.y(running[j])]);
      pts.push([f.x(n), f.y(final)]);
      V.svgEl("path", { d: V.pathFrom(pts), class: "curve" }, f.marks);
      if (finite) {
        K.text(f.marks, f, n * 0.02, pop.mean + 0.5 * pad, "μ = " + K.num(pop.mean, 2), "label");
      }

      U.setAria(
        svg,
        "Running average of " + n + " draws from a " + pop.label + " population. The final average is " +
          K.num(final, 3) + (finite ? ", compared with the population mean " + K.num(pop.mean, 3) + "." :
          ". This population has no finite mean, so the average does not settle.")
      );

      s.readout.textContent =
        pop.label + "  ·  n = " + n.toLocaleString() +
        "  ·  running average " + K.num(final, 3) +
        (finite ? "  ·  μ = " + K.num(pop.mean, 3) + "  ·  SE at n = " + K.num(pop.sd / Math.sqrt(n), 4) : "  ·  μ undefined");

      table && table.set([
        ["population", pop.label],
        ["theoretical mean μ", finite ? K.num(pop.mean, 3) : "does not exist"],
        ["theoretical SD σ", finite ? K.num(pop.sd, 3) : "does not exist"],
        ["running average at n", K.num(final, 3)],
        [finite ? "distance from μ" : "the average keeps jumping", finite ? K.num(Math.abs(final - pop.mean), 3) : "—"],
        ["±2 SE around μ at this n", finite ? "±" + K.num(2 * pop.sd / Math.sqrt(n), 3) : "no SE exists"]
      ]);

      s.hint.textContent = finite
        ? "The average settles towards μ but never locks onto it: at n = " + n.toLocaleString() +
          " the standard error is still " + K.num(pop.sd / Math.sqrt(n), 4) +
          ". Press New run and the path changes completely — the destination does not."
        : "The Cauchy distribution has no mean, so the running average has no limit. It makes " +
          "occasional enormous jumps that undo thousands of observations. This is the counter-example " +
          "that shows why the law of large numbers needs a finite mean.";
    }

    draw();
  }

  /* ----------------------------------------------------- L-08 sampling */

  function buildSampling(root) {
    var s = slots(root);
    if (!s.controls || !s.chart) return;
    V.clear(s.controls);
    V.clear(s.chart);

    var DEFAULTS = { mu: 100, sigma: 15, n: 10, B: 1000, run: 0 };
    var state = Object.assign({}, DEFAULTS);
    var svg = V.svgEl("svg", { width: 640, height: 320 }, s.chart);
    var table = K.table(s.results);

    var muField = U.slider(s.controls, {
      id: "samp-mu", label: "Population mean μ", min: 50, max: 150, step: 5, value: state.mu,
      onInput: function (v) { state.mu = v; changed(); }
    });
    var sdField = U.slider(s.controls, {
      id: "samp-sd", label: "Population SD σ", min: 5, max: 30, step: 1, value: state.sigma,
      onInput: function (v) { state.sigma = v; changed(); }
    });
    var nField = U.slider(s.controls, {
      id: "samp-n", label: "Sample size n", min: 2, max: 100, step: 1, value: state.n,
      onInput: function (v) { state.n = v; changed(); }
    });
    var bField = U.slider(s.controls, {
      id: "samp-b", label: "Samples B", min: 200, max: 3000, step: 100, value: state.B,
      onInput: function (v) { state.B = v; changed(); }
    });

    buttons(s.controls, function () { state.run += 1; draw(); }, function () {
      state = Object.assign({}, DEFAULTS);
      muField.set(state.mu); sdField.set(state.sigma); nField.set(state.n); bField.set(state.B);
      draw();
    });

    K.legend(s.legend, [
      { label: "one sample at a time", colour: "accent", kind: "dot" },
      { label: "sampling distribution of x̄", colour: "teal", kind: "bar" },
      { label: "σ/√n around μ", colour: "accent", kind: "line" }
    ]);

    function changed() {
      s.hint.textContent = "Settings changed — press New run to resample.";
    }

    function draw() {
      var r = V.rng(seedOf(root, state.run));
      var mu = state.mu, sigma = state.sigma, n = state.n, B = state.B;
      var se = sigma / Math.sqrt(n);
      var means = new Array(B);
      for (var b = 0; b < B; b++) {
        var sum = 0;
        for (var i = 0; i < n; i++) sum += mu + sigma * U.gauss(r);
        means[b] = sum / n;
      }
      var empMean = S.mean(means);
      var empSd = S.sd(means);
      var share = 0;
      for (var j = 0; j < B; j++) if (Math.abs(means[j] - mu) <= 1.96 * se) share += 1;
      share /= B;

      var lo = mu - 3.6 * Math.max(se, sigma / Math.sqrt(4));
      var hi = mu + 3.6 * Math.max(se, sigma / Math.sqrt(4));
      var h = V.histogram(means, 44, lo, hi);

      V.clear(svg);
      var f = V.frame(svg, {
        width: 640, height: 320,
        xDomain: [lo, hi],
        yDomain: [0, Math.max(0.02, Math.max.apply(null, h.density)) * 1.3],
        xLabel: "sample mean x̄, and the population spread for comparison",
        yFormat: function (v) { return v.toFixed(3); }
      });
      for (var k = 0; k < h.density.length; k++) {
        var x0 = f.x(h.lo + k * h.width);
        var x1 = f.x(h.lo + (k + 1) * h.width);
        V.bar(f.marks, x0, f.y(h.density[k]), x1 - x0, f.y(0) - f.y(h.density[k]), "bar");
      }
      K.curve(f.marks, f, function (t) { return S.normPdf(t, mu, se); }, lo, hi, "curve", 200);
      K.hline(f.marks, f, 0, "reference");
      K.area(f.marks, f, function (t) { return S.normPdf(t, mu, se); }, mu - sigma, mu + sigma,
             "area area--faint");
      K.vline(f.marks, f, mu, "reference reference--accent");
      K.text(f.marks, f, mu, S.normPdf(mu, mu, se) * 0.55,
             "σ/√n = " + K.num(se, 2), "label label--strong", "middle");

      U.setAria(
        svg,
        "Histogram of " + B + " sample means from samples of size " + n + " taken from a normal " +
          "population with mean " + mu + " and standard deviation " + sigma + ". The standard deviation " +
          "of the means is " + K.num(empSd, 2) + " against a theoretical standard error of " + K.num(se, 2) + "."
      );

      s.readout.textContent =
        "n = " + n + "  ·  B = " + B + "  ·  mean of means = " + K.num(empMean, 2) +
        "  ·  SD of means = " + K.num(empSd, 2) + "  ·  σ/√n = " + K.num(se, 2) +
        "  ·  within ±1.96 SE: " + K.pct(share);

      table && table.set([
        ["standard error σ/√n", K.num(se, 3)],
        ["observed SD of the means", K.num(empSd, 3)],
        ["ratio observed / theory", K.num(empSd / se, 3)],
        ["mean of the means", K.num(empMean, 3) + " (μ = " + mu + ")"],
        ["within ±1.96 SE", K.pct(share) + " (theory 95 %)"],
        ["quadruple n → SE", "halves: " + K.num(sigma / Math.sqrt(4 * n), 3)],
        ["B samples of size n", B + " × " + n + " = " + (B * n).toLocaleString() + " draws"]
      ]);

      s.hint.textContent =
        "One observation is highly variable (σ = " + sigma + "), but an average of " + n +
        " is much less so (SE = " + K.num(se, 2) + "). The histogram is the distribution of the " +
        "statistic, not of the data — a distinction students routinely blur. Quadruple n and the " +
        "spread halves; that 1/√n law is why precision is expensive.";
    }

    draw();
  }

  /* ------------------------------------------------------ L-10 p-values */

  function buildPvalues(root) {
    var s = slots(root);
    if (!s.controls || !s.chart) return;
    V.clear(s.controls);
    V.clear(s.chart);

    var DEFAULTS = { delta: 0, n: 30, alpha: 0.05, side: "two", B: 1000, run: 0 };
    var state = Object.assign({}, DEFAULTS);
    var svg = V.svgEl("svg", { width: 640, height: 290 }, s.chart);
    var hist = V.svgEl("svg", { width: 640, height: 190 }, s.chart);
    var table = K.table(s.results);

    var deltaField = U.slider(s.controls, {
      id: "pval-delta", label: "True effect δ (in SD units)", min: 0, max: 1.5, step: 0.05,
      value: state.delta, format: function (v) { return v.toFixed(2); },
      onInput: function (v) { state.delta = v; changed(); }
    });
    var nField = U.slider(s.controls, {
      id: "pval-n", label: "Sample size n", min: 5, max: 200, step: 5, value: state.n,
      onInput: function (v) { state.n = v; changed(); }
    });
    var alphaField = U.select(s.controls, {
      label: "Significance level α", value: String(state.alpha),
      options: [{ value: "0.01", label: "0.01" }, { value: "0.05", label: "0.05" }, { value: "0.10", label: "0.10" }],
      onChange: function (v) { state.alpha = Number(v); changed(); }
    });
    var sideField = U.select(s.controls, {
      label: "Alternative hypothesis", value: state.side,
      options: [
        { value: "two", label: "two-sided μ ≠ 0" },
        { value: "greater", label: "one-sided μ > 0" },
        { value: "less", label: "one-sided μ < 0" }
      ],
      onChange: function (v) { state.side = v; changed(); }
    });
    var bField = U.slider(s.controls, {
      id: "pval-b", label: "Simulated studies B", min: 200, max: 3000, step: 100, value: state.B,
      onInput: function (v) { state.B = v; changed(); }
    });

    buttons(s.controls, function () { state.run += 1; draw(); }, function () {
      state = Object.assign({}, DEFAULTS);
      deltaField.set(state.delta); nField.set(state.n); alphaField.set(String(state.alpha));
      sideField.set(state.side); bField.set(state.B);
      draw();
    });

    K.legend(s.legend, [
      { label: "null distribution t(n−1)", colour: "teal", kind: "line" },
      { label: "rejection region (α)", colour: "accent", kind: "bar" },
      { label: "simulated p-values", colour: "accent", kind: "bar" }
    ]);

    function changed() {
      s.hint.textContent = "Settings changed — press New run to resimulate the studies.";
    }

    function pOf(t, df) {
      if (state.side === "two") return S.tTwoSidedP(t, df);
      if (state.side === "greater") return S.tSf(t, df);
      return S.tCdf(t, df);
    }

    function draw() {
      var r = V.rng(seedOf(root, state.run));
      var n = state.n, B = state.B, delta = state.delta, df = n - 1;
      var tCrit = state.side === "two" ? S.tInv(1 - state.alpha / 2, df) : S.tInv(1 - state.alpha, df);

      var ps = new Array(B);
      var ts = new Array(B);
      var rejects = 0;
      var firstT = NaN, firstP = NaN;
      for (var b = 0; b < B; b++) {
        var sum = 0, sumSq = 0;
        for (var i = 0; i < n; i++) {
          var x = delta + U.gauss(r);
          sum += x;
          sumSq += x * x;
        }
        var xbar = sum / n;
        var sdv = Math.sqrt(Math.max(1e-12, (sumSq - n * xbar * xbar) / (n - 1)));
        var t = xbar / (sdv / Math.sqrt(n));
        var p = pOf(t, df);
        ts[b] = t; ps[b] = p;
        if (b === 0) { firstT = t; firstP = p; }
        var reject = state.side === "two" ? Math.abs(t) >= tCrit :
                     state.side === "greater" ? t >= tCrit : t <= -tCrit;
        if (reject) rejects += 1;
      }

      // Analytic power by the z approximation (exact for known sigma).
      var zc = S.zCrit(state.alpha);
      var shift = delta * Math.sqrt(n);
      var power = state.side === "two"
        ? S.normCdf(shift - zc) + S.normCdf(-shift - zc)
        : state.side === "greater" ? S.normCdf(shift - zc) : S.normCdf(-shift - zc);

      // Null t density
      var lo = -4.2, hi = 4.2;
      V.clear(svg);
      var f = V.frame(svg, {
        width: 640, height: 290,
        xDomain: [lo, hi],
        yDomain: [0, 0.46],
        xLabel: "t statistic under H₀: μ = 0",
        yFormat: function () { return ""; }
      });
      K.curve(f.marks, f, function (t) {
        var lg = S.lnGamma((df + 1) / 2) - S.lnGamma(df / 2) - 0.5 * Math.log(df * Math.PI);
        return Math.exp(lg - ((df + 1) / 2) * Math.log(1 + (t * t) / df));
      }, lo, hi, "curve", 260);
      if (state.side === "two") {
        K.area(f.marks, f, function (t) { return S.tCdf(-t, df) * 0 + pdf(t); }, tCrit, hi, "area area--accent");
        K.area(f.marks, f, pdf, lo, -tCrit, "area area--accent");
      } else if (state.side === "greater") {
        K.area(f.marks, f, pdf, tCrit, hi, "area area--accent");
      } else {
        K.area(f.marks, f, pdf, lo, -tCrit, "area area--accent");
      }
      K.vline(f.marks, f, tCrit, "reference");
      if (state.side !== "greater") K.vline(f.marks, f, -tCrit, "reference");
      K.text(f.marks, f, tCrit, 0.40, "|t| = " + K.num(tCrit, 2), "label", "middle");
      K.text(f.marks, f, -3.6, 0.30, "α = " + state.alpha, "label label--strong");

      function pdf(t) {
        var lg = S.lnGamma((df + 1) / 2) - S.lnGamma(df / 2) - 0.5 * Math.log(df * Math.PI);
        return Math.exp(lg - ((df + 1) / 2) * Math.log(1 + (t * t) / df));
      }

      // p-value histogram
      V.clear(hist);
      var hb = 20;
      var counts = new Array(hb);
      for (var c = 0; c < hb; c++) counts[c] = 0;
      for (var q = 0; q < B; q++) {
        var idx = Math.min(hb - 1, Math.floor(ps[q] * hb));
        counts[idx] += 1;
      }
      var hf = V.frame(hist, {
        width: 640, height: 190,
        xDomain: [0, 1],
        yDomain: [0, Math.max(1, Math.max.apply(null, counts)) * 1.15 / B * 2.4],
        xLabel: "p-value from each simulated study (B = " + B + ")",
        yFormat: function (v) { return v.toFixed(2); }
      });
      for (var k = 0; k < hb; k++) {
        var x0 = hf.x(k / hb);
        var x1 = hf.x((k + 1) / hb);
        var height = counts[k] / B / (1 / hb);
        V.bar(hf.marks, x0, hf.y(height), x1 - x0, hf.y(0) - hf.y(height), "bar");
      }
      K.hline(hf.marks, hf, 1, "reference reference--accent");
      K.text(hf.marks, hf, 0.52, 1.05, "uniform when H₀ is true", "label");

      U.setAria(
        svg,
        "Null t distribution with degrees of freedom " + df + " and the rejection region for alpha " +
          state.alpha + ". In " + B + " simulated studies with true effect " + K.num(delta, 2) +
          ", " + rejects + " were significant, an observed rejection rate of " + K.pct(rejects / B) +
          ". The analytic power is " + K.num(power, 3) + "."
      );

      s.readout.textContent =
        "δ = " + K.num(delta, 2) + "  ·  n = " + n + "  ·  α = " + state.alpha +
        "  ·  critical |t| = " + K.num(tCrit, 3) +
        "  ·  rejection rate = " + K.pct(rejects / B) +
        "  ·  analytic power (z approx.) = " + K.num(power, 3) +
        "  ·  first study: t = " + K.num(firstT, 2) + ", p = " + K.num(firstP, 3);

      table && table.set([
        ["hypotheses", "H₀: μ = 0 against " + (state.side === "two" ? "μ ≠ 0" :
          state.side === "greater" ? "μ > 0" : "μ < 0")],
        ["critical value", "|t| = " + K.num(tCrit, 3) + " (df = " + df + ")"],
        ["observed rejection rate", K.pct(rejects / B) + " of " + B + " studies"],
        ["analytic power (z approximation)", K.num(power, 3)],
        ["probability of a false positive", "α = " + state.alpha + " by construction"],
        ["mean p-value", K.num(S.mean(ps), 3)],
        ["share of p < α", K.pct(ps.filter(function (p) { return p < state.alpha; }).length / B)]
      ]);

      var observed = rejects / B;
      s.hint.textContent = delta === 0
        ? "With no true effect, every significant result is a false positive. The rejection rate is " +
          K.pct(observed) + ", close to α = " + state.alpha + ", and the p-values are spread uniformly: " +
          "a p of 0.04 is no more surprising than a p of 0.87. That is why a single p-value is not evidence " +
          "of a real effect on its own."
        : "The true effect is " + K.num(delta, 2) + " SD. Power here is about " + K.pct(observed) +
          " — the share of studies that correctly reject H₀. Raise n and power climbs: significance " +
          "depends on the effect size and the sample size together, never on the p-value alone.";
    }

    draw();
  }

  REG.builders.normal = buildNormal;
  REG.builders.lln = buildLln;
  REG.builders.sampling = buildSampling;
  REG.builders.pvalues = buildPvalues;
})();
