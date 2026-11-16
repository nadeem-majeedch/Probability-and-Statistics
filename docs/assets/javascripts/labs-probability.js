/* ==========================================================================
   labs-probability.js — Labs L-01 to L-04
   --------------------------------------------------------------------------
   probability            random events and long-run frequency
   conditional            conditional probability and Bayes' theorem
   discrete               binomial, Poisson and geometric distributions
   continuous             normal, exponential, gamma and uniform densities

   Every builder follows the same contract: read [data-role] slots from the
   root, build controls, draw an SVG that carries an aria-label, and report a
   numeric readout plus a plain-language interpretation in [data-role=hint].
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

  function buttonRow(parent, handlers) {
    var box = el("div", "psds-lab__buttons", parent);
    var restart = U.button(box, "New run", null, handlers.run);
    U.button(box, "Reset", "psds-btn--ghost", handlers.reset);
    return restart;
  }

  /* --------------------------------------------------------- L-01 events */

  function buildProbability(root) {
    var s = slots(root);
    if (!s.controls || !s.chart) return;
    V.clear(s.controls);
    V.clear(s.chart);

    var DEFAULTS = { n: 1000, p: 0.5, k: 3 };
    var state = { n: DEFAULTS.n, p: DEFAULTS.p, k: DEFAULTS.k, run: 0 };

    var bars = V.svgEl("svg", { width: 640, height: 250 }, s.chart);
    var line = V.svgEl("svg", { width: 640, height: 150 }, s.chart);
    var table = K.table(s.results);

    var nSlider, pSlider, kSlider;

    function changed() {
      s.hint.textContent = "Settings changed — press New run to resample.";
    }

    nSlider = U.slider(s.controls, {
      id: "prob-n",
      label: "Trials n",
      min: 100,
      max: 5000,
      step: 100,
      value: state.n,
      onInput: function (v) {
        state.n = v;
        changed();
      }
    });
    pSlider = U.slider(s.controls, {
      id: "prob-p",
      label: "P(A) = p",
      min: 0.05,
      max: 0.95,
      step: 0.05,
      value: state.p,
      format: function (v) {
        return v.toFixed(2);
      },
      onInput: function (v) {
        state.p = v;
        changed();
      }
    });
    kSlider = U.slider(s.controls, {
      id: "prob-k",
      label: "Outcomes k",
      min: 2,
      max: 5,
      step: 1,
      value: state.k,
      onInput: function (v) {
        state.k = v;
        changed();
      }
    });

    buttonRow(s.controls, {
      run: function () {
        state.run += 1;
        draw();
      },
      reset: function () {
        state = { n: DEFAULTS.n, p: DEFAULTS.p, k: DEFAULTS.k, run: 0 };
        nSlider.set(state.n);
        pSlider.set(state.p);
        kSlider.set(state.k);
        draw();
      }
    });

    K.legend(s.legend, [
      { label: "observed relative frequency", colour: "teal", kind: "bar" },
      { label: "theoretical probability", colour: "accent", kind: "line" }
    ]);

    function theory(k, p) {
      // Outcome 1 has probability p; the remaining k-1 share 1-p equally.
      var out = [p];
      for (var i = 1; i < k; i++) out.push((1 - p) / (k - 1));
      return out;
    }

    function draw() {
      var r = V.rng(seedOf(root, state.run));
      var n = state.n;
      var k = state.k;
      var th = theory(k, state.p);

      var counts = new Array(k);
      for (var c = 0; c < k; c++) counts[c] = 0;
      var running = [];
      var hitA = 0;
      for (var t = 0; t < n; t++) {
        var u = r();
        var cum = 0;
        var pick = k - 1;
        for (var j = 0; j < k; j++) {
          cum += th[j];
          if (u <= cum) {
            pick = j;
            break;
          }
        }
        counts[pick] += 1;
        if (pick === 0) hitA += 1;
        if ((t + 1) % Math.max(1, Math.floor(n / 200)) === 0 || t === n - 1) {
          running.push([(t + 1) / n, hitA / (t + 1)]);
        }
      }

      var pA = hitA / n;
      var pB = (counts[0] + counts[1]) / n;
      var thB = th[0] + th[1];
      var seA = Math.sqrt((state.p * (1 - state.p)) / n);

      V.clear(bars);
      var peak = 1.15 * Math.max(
        0.15,
        Math.max.apply(null, th),
        Math.max.apply(null, counts.map(function (x) { return x / n; }))
      );
      var f = V.frame(bars, {
        width: 640,
        height: 250,
        xDomain: [0, k + 1],
        yDomain: [0, peak],
        xLabel: "outcome",
        xFormat: function (v) { return Number.isInteger(v) ? String(v) : ""; }
      });
      for (var i = 0; i < k; i++) {
        var x0 = f.x(i + 0.62);
        var x1 = f.x(i + 1.38);
        V.bar(f.marks, x0, f.y(counts[i] / n), x1 - x0, f.y(0) - f.y(counts[i] / n), "bar");
        V.svgEl("line", {
          x1: f.x(i + 0.55), x2: f.x(i + 1.45),
          y1: f.y(th[i]), y2: f.y(th[i]),
          class: "reference"
        }, f.marks);
        K.text(f.marks, f, i + 1, counts[i] / n + peak * 0.04,
               (100 * counts[i] / n).toFixed(1) + "%", "label", "middle");
      }

      V.clear(line);
      var lf = V.frame(line, {
        width: 640,
        height: 150,
        yDomain: [0, 1],
        xDomain: [0, 1],
        xLabel: "fraction of the n trials completed",
        yFormat: function (v) { return v.toFixed(2); }
      });
      K.hline(lf.marks, lf, state.p, "reference");
      K.curve(lf.marks, lf, function () { return state.p; }, 0, 1, "reference", 2);
      var pts = running.map(function (d) {
        return [lf.x(d[0]), lf.y(d[1])];
      });
      if (pts.length > 1) V.svgEl("path", { d: V.pathFrom(pts), class: "curve" }, lf.marks);
      K.text(lf.marks, lf, 0.02, state.p + 0.06, "p = " + state.p.toFixed(2), "label");

      U.setAria(
        bars,
        "Bar chart of " + k + " outcome frequencies from " + n + " simulated trials. " +
          "P(outcome 1) was estimated as " + K.num(pA, 3) + ", theoretical " + K.num(th[0], 3) +
          ". The second chart traces that estimate as the trials accumulate."
      );

      s.readout.textContent =
        "n = " + n + "  ·  k = " + k + "  ·  p = " + state.p.toFixed(2) +
        "  ·  observed P(A) = " + K.num(pA, 3) + " (theory " + K.num(th[0], 3) + ")" +
        "  ·  observed P(A or B) = " + K.num(pB, 3) + " (theory " + K.num(thB, 3) + ")" +
        "  ·  standard error of P(A) = " + K.num(seA, 4);

      table && table.set([
        ["P(A)", K.num(th[0], 4) + " theory · " + K.num(pA, 4) + " observed"],
        ["P(A or B)", K.num(thB, 4) + " theory · " + K.num(pB, 4) + " observed"],
        ["P(not A)", K.num(1 - th[0], 4) + " theory · " + K.num(1 - pA, 4) + " observed"],
        ["standard error √(p(1−p)/n)", K.num(seA, 4)],
        ["two standard errors", K.num(2 * seA, 4)],
        ["observed within ±2 SE?", Math.abs(pA - th[0]) <= 2 * seA ? "yes" : "no — resample"]
      ]);

      s.hint.textContent =
        "The gap between the bars and the red ticks is sampling error, not a mistake: " +
        "with n = " + n + " the standard error is " + K.num(seA, 3) +
        ", so estimates typically land within ±" + K.num(2 * seA, 3) + " of the truth. " +
        "Press New run: the bars move, the ticks do not. That difference is the whole subject.";
    }

    draw();
  }

  /* --------------------------------------------------- L-02 conditional */

  function buildConditional(root) {
    var s = slots(root);
    if (!s.controls || !s.chart) return;
    V.clear(s.controls);
    V.clear(s.chart);

    var DEFAULTS = { prev: 0.10, sens: 0.90, fpr: 0.05, n: 2000 };
    var state = { prev: DEFAULTS.prev, sens: DEFAULTS.sens, fpr: DEFAULTS.fpr, n: DEFAULTS.n, run: 0 };
    var svg = V.svgEl("svg", { width: 640, height: 330 }, s.chart);
    var table = K.table(s.results);

    var prevSlider = U.slider(s.controls, {
      id: "cond-prev",
      label: "Prevalence P(A)",
      min: 0.01, max: 0.5, step: 0.01, value: state.prev,
      format: function (v) { return v.toFixed(2); },
      onInput: function (v) { state.prev = v; changed(); }
    });
    var sensSlider = U.slider(s.controls, {
      id: "cond-sens",
      label: "Sensitivity P(B|A)",
      min: 0.5, max: 1, step: 0.01, value: state.sens,
      format: function (v) { return v.toFixed(2); },
      onInput: function (v) { state.sens = v; changed(); }
    });
    var fprSlider = U.slider(s.controls, {
      id: "cond-fpr",
      label: "False positive P(B|¬A)",
      min: 0, max: 0.3, step: 0.01, value: state.fpr,
      format: function (v) { return v.toFixed(2); },
      onInput: function (v) { state.fpr = v; changed(); }
    });
    var nSlider = U.slider(s.controls, {
      id: "cond-n",
      label: "Simulated people n",
      min: 500, max: 5000, step: 500, value: state.n,
      onInput: function (v) { state.n = v; changed(); }
    });

    buttonRow(s.controls, {
      run: function () { state.run += 1; draw(); },
      reset: function () {
        state = { prev: DEFAULTS.prev, sens: DEFAULTS.sens, fpr: DEFAULTS.fpr, n: DEFAULTS.n, run: 0 };
        prevSlider.set(state.prev);
        sensSlider.set(state.sens);
        fprSlider.set(state.fpr);
        nSlider.set(state.n);
        draw();
      }
    });

    K.legend(s.legend, [
      { label: "has the condition (A)", colour: "accent", kind: "bar" },
      { label: "does not have it (¬A)", colour: "teal", kind: "bar" }
    ]);

    function changed() {
      s.hint.textContent = "Settings changed — press New run to resample.";
    }

    function draw() {
      var prev = state.prev;
      var sens = state.sens;
      var fpr = state.fpr;
      var pB = sens * prev + fpr * (1 - prev);
      var post = (sens * prev) / pB;                 // P(A|B)
      var npv = ((1 - fpr) * (1 - prev)) / (1 - pB); // P(¬A|¬B)

      // Simulated table
      var r = V.rng(seedOf(root, state.run));
      var n = state.n;
      var cell = { aB: 0, aNb: 0, naB: 0, naNb: 0 };
      for (var i = 0; i < n; i++) {
        var has = r() < prev;
        var tests = r() < (has ? sens : fpr);
        if (has && tests) cell.aB += 1;
        else if (has) cell.aNb += 1;
        else if (tests) cell.naB += 1;
        else cell.naNb += 1;
      }
      var empPost = cell.aB / Math.max(1, cell.aB + cell.naB);

      V.clear(svg);
      var f = V.frame(svg, {
        width: 640, height: 330,
        xDomain: [0, 1], yDomain: [0, 1],
        xLabel: "column width ∝ number of people",
        yFormat: function () { return ""; }
      });
      // Mosaic: left column A, right column ¬A; top row test positive.
      var wA = f.plotW * prev;
      var wN = f.plotW * (1 - prev);
      var hAB = f.plotH * sens;
      var hNB = f.plotH * fpr;
      var x = f.margin.left;
      var top = f.margin.top;
      var heights = [hAB, f.plotH - hAB, hNB, f.plotH - hNB];
      var widths = [wA, wA, wN, wN];
      var xs = [x, x, x + wA, x + wA];
      var ys = [top, top + hAB, top, top + hNB];
      var labels = [
        ["true positive", cell.aB, "accent"],
        ["false negative", cell.aNb, "accent-soft"],
        ["false positive", cell.naB, "teal"],
        ["true negative", cell.naNb, "teal-soft"]
      ];
      for (var b = 0; b < 4; b++) {
        var rect = V.svgEl(
          "rect",
          {
            x: xs[b].toFixed(2),
            y: ys[b].toFixed(2),
            width: Math.max(0, widths[b] - 2).toFixed(2),
            height: Math.max(0, heights[b] - 2).toFixed(2),
            class: "mosaic mosaic--" + labels[b][2]
          },
          f.marks
        );
        if (widths[b] > 46 && heights[b] > 26) {
          var t1 = V.svgEl("text", {
            x: (xs[b] + widths[b] / 2).toFixed(2),
            y: (ys[b] + heights[b] / 2 - 4).toFixed(2),
            "text-anchor": "middle", class: "label"
          }, f.marks);
          t1.textContent = labels[b][0];
          var t2 = V.svgEl("text", {
            x: (xs[b] + widths[b] / 2).toFixed(2),
            y: (ys[b] + heights[b] / 2 + 12).toFixed(2),
            "text-anchor": "middle", class: "label label--strong"
          }, f.marks);
          t2.textContent = labels[b][1].toLocaleString();
        } else {
          rect.setAttribute("opacity", "0.85");
        }
      }
      V.svgEl("line", {
        x1: x, x2: x, y1: top, y2: top + f.plotH, class: "reference"
      }, f.marks);
      var headline = V.svgEl("text", {
        x: x + 6, y: top + 16, class: "label label--strong"
      }, f.marks);
      headline.textContent = "P(A | B) = " + K.num(post, 3) + "   (observed " + K.num(empPost, 3) + ")";

      U.setAria(
        svg,
        "Mosaic of " + n + " simulated people. " + cell.aB + " test positive and truly have the " +
          "condition, " + cell.naB + " test positive without it. The posterior probability of the " +
          "condition given a positive test is " + K.num(post, 3) + "."
      );

      s.readout.textContent =
        "P(A) = " + K.num(prev, 2) + "  ·  P(B|A) = " + K.num(sens, 2) +
        "  ·  P(B|¬A) = " + K.num(fpr, 2) + "  ·  P(B) = " + K.num(pB, 3) +
        "  ·  P(A|B) = " + K.num(post, 3) + "  ·  P(¬A|¬B) = " + K.num(npv, 3);

      table && table.set([
        ["P(B), any positive", K.num(pB, 4)],
        ["P(A | B), posterior", K.num(post, 4) + " theory · " + K.num(empPost, 4) + " observed"],
        ["P(¬A | B), false discovery", K.num(1 - post, 4)],
        ["P(¬A | ¬B), negative predictive value", K.num(npv, 4)],
        ["odds form", K.num(post / (1 - post), 3) + " : 1"],
        ["people tested", n.toLocaleString() + " simulated"]
      ]);

      s.hint.textContent =
        "P(A|B) is not P(B|A). A sensitive test on a rare condition still produces mostly false " +
        "positives: here " + cell.naB + " of " + (cell.aB + cell.naB) + " positives are false. " +
        "Lower the prevalence and watch the posterior collapse towards zero — that is the base-rate trap.";
    }

    draw();
  }

  /* ------------------------------------------------------ L-03 discrete */

  function buildDiscrete(root) {
    var s = slots(root);
    if (!s.controls || !s.chart) return;
    V.clear(s.controls);
    V.clear(s.chart);

    var DEFAULTS = { family: "binomial", n: 10, p: 0.3, lambda: 4, draws: 2000, k: 3 };
    var state = { family: DEFAULTS.family, n: DEFAULTS.n, p: DEFAULTS.p,
                  lambda: DEFAULTS.lambda, draws: DEFAULTS.draws, k: DEFAULTS.k, run: 0 };
    var svg = V.svgEl("svg", { width: 640, height: 320 }, s.chart);
    var table = K.table(s.results);

    var familySel = U.select(s.controls, {
      label: "Distribution",
      value: state.family,
      options: [
        { value: "binomial", label: "Binomial(n, p)" },
        { value: "poisson", label: "Poisson(λ)" },
        { value: "geometric", label: "Geometric(p)" }
      ],
      onChange: function (v) { state.family = v; sync(); }
    });

    var nField = U.slider(s.controls, {
      id: "disc-n", label: "Trials n (binomial)", min: 5, max: 40, step: 1, value: state.n,
      onInput: function (v) { state.n = v; changed(); }
    });
    var pField = U.slider(s.controls, {
      id: "disc-p", label: "Success probability p", min: 0.05, max: 0.9, step: 0.05, value: state.p,
      format: function (v) { return v.toFixed(2); },
      onInput: function (v) { state.p = v; changed(); }
    });
    var lField = U.slider(s.controls, {
      id: "disc-lambda", label: "Rate λ (Poisson)", min: 0.5, max: 10, step: 0.5, value: state.lambda,
      format: function (v) { return v.toFixed(1); },
      onInput: function (v) { state.lambda = v; changed(); }
    });
    var dField = U.slider(s.controls, {
      id: "disc-draws", label: "Simulated draws", min: 500, max: 5000, step: 500, value: state.draws,
      onInput: function (v) { state.draws = v; changed(); }
    });
    var kField = U.slider(s.controls, {
      id: "disc-k", label: "Threshold k: P(X ≤ k)", min: 0, max: 30, step: 1, value: state.k,
      onInput: function (v) { state.k = v; changed(); }
    });

    buttonRow(s.controls, {
      run: function () { state.run += 1; draw(); },
      reset: function () {
        state = { family: DEFAULTS.family, n: DEFAULTS.n, p: DEFAULTS.p, lambda: DEFAULTS.lambda,
                  draws: DEFAULTS.draws, k: DEFAULTS.k, run: 0 };
        familySel.set(state.family);
        nField.set(state.n); pField.set(state.p); lField.set(state.lambda);
        dField.set(state.draws); kField.set(state.k);
        sync();
      }
    });

    K.legend(s.legend, [
      { label: "exact PMF", colour: "teal", kind: "bar" },
      { label: "simulated relative frequency", colour: "accent", kind: "dot" },
      { label: "shaded: P(X ≤ k)", colour: "band", kind: "bar" }
    ]);

    function sync() {
      nField.input.parentNode.style.display = state.family === "binomial" ? "" : "none";
      lField.input.parentNode.style.display = state.family === "poisson" ? "" : "none";
      pField.input.parentNode.style.display = state.family === "poisson" ? "none" : "";
      draw();
    }

    function changed() {
      s.hint.textContent = "Settings changed — press New run to redraw and resample.";
    }

    function model() {
      var max, pmf, mean, variance;
      if (state.family === "binomial") {
        max = state.n;
        pmf = function (k) { return S.binomPmf(k, state.n, state.p); };
        mean = state.n * state.p;
        variance = state.n * state.p * (1 - state.p);
      } else if (state.family === "poisson") {
        max = Math.ceil(state.lambda + 5 * Math.sqrt(state.lambda) + 4);
        pmf = function (k) { return S.poissonPmf(k, state.lambda); };
        mean = state.lambda;
        variance = state.lambda;
      } else {
        max = Math.ceil(Math.log(0.0005) / Math.log(1 - state.p));
        pmf = function (k) {
          return k >= 1 ? Math.pow(1 - state.p, k - 1) * state.p : 0;
        };
        mean = 1 / state.p;
        variance = (1 - state.p) / (state.p * state.p);
      }
      return { max: max, pmf: pmf, mean: mean, variance: variance };
    }

    function sample(r) {
      if (state.family === "poisson") {
        // Knuth's method; lambda is small here so it is efficient and exact.
        var L = Math.exp(-state.lambda);
        var k = 0;
        var prod = 1;
        do {
          k += 1;
          prod *= r();
        } while (prod > L);
        return k - 1;
      }
      if (state.family === "geometric") {
        return Math.floor(Math.log(1 - r()) / Math.log(1 - state.p)) + 1;
      }
      var hits = 0;
      for (var i = 0; i < state.n; i++) if (r() < state.p) hits += 1;
      return hits;
    }

    function draw() {
      var m = model();
      var kMax = Math.min(m.max, Math.max(8, Math.ceil(m.mean + 4 * Math.sqrt(m.variance))));
      var k = Math.min(state.k, kMax);
      kField.input.max = String(kMax);

      var r = V.rng(seedOf(root, state.run));
      var draws = state.draws;
      var counts = new Array(kMax + 1);
      for (var c = 0; c <= kMax; c++) counts[c] = 0;
      var sum = 0;
      var sumSq = 0;
      for (var t = 0; t < draws; t++) {
        var x = sample(r);
        sum += x;
        sumSq += x * x;
        if (x <= kMax) counts[x] += 1;
      }
      var empMean = sum / draws;
      var empVar = sumSq / draws - empMean * empMean;

      var theoryCdf = 0;
      for (var j = 0; j <= k; j++) theoryCdf += m.pmf(j);
      var empCdf = 0;
      for (var j2 = 0; j2 <= k; j2++) empCdf += counts[j2] / draws;

      V.clear(svg);
      var peak = 0;
      for (var p = 0; p <= kMax; p++) peak = Math.max(peak, m.pmf(p), counts[p] / draws);
      var f = V.frame(svg, {
        width: 640, height: 320,
        xDomain: [-0.7, kMax + 0.7],
        yDomain: [0, peak * 1.2],
        xLabel: "x",
        yFormat: function (v) { return v.toFixed(2); },
        xFormat: function (v) { return Number.isInteger(v) ? String(v) : ""; }
      });

      for (var i = 0; i <= kMax; i++) {
        var x0 = f.x(i - 0.32);
        var x1 = f.x(i + 0.32);
        V.bar(f.marks, x0, f.y(m.pmf(i)), x1 - x0, f.y(0) - f.y(m.pmf(i)),
              i <= k ? "bar bar--band" : "bar");
        V.svgEl("circle", {
          cx: f.x(i), cy: f.y(counts[i] / draws), r: 3,
          class: "dot dot--accent"
        }, f.marks);
      }
      K.vline(f.marks, f, k + 0.5, "reference");

      U.setAria(
        svg,
        "Probability mass function of a " + state.family + " variable with the simulated " +
          "frequencies overlaid. P(X ≤ " + k + ") is " + K.num(theoryCdf, 3) +
          " in theory and " + K.num(empCdf, 3) + " in the simulation."
      );

      s.readout.textContent =
        state.family + "  ·  mean = " + K.num(m.mean, 3) + " (observed " + K.num(empMean, 3) + ")" +
        "  ·  variance = " + K.num(m.variance, 3) + " (observed " + K.num(empVar, 3) + ")" +
        "  ·  SD = " + K.num(Math.sqrt(m.variance), 3) +
        "  ·  P(X ≤ " + k + ") = " + K.num(theoryCdf, 3) + " (observed " + K.num(empCdf, 3) + ")";

      table && table.set([
        ["theory mean E[X]", K.num(m.mean, 3)],
        ["theory variance Var(X)", K.num(m.variance, 3)],
        ["simulated mean x̄", K.num(empMean, 3)],
        ["simulated variance s²", K.num(empVar, 3)],
        ["P(X = " + k + ")", K.num(m.pmf(k), 4)],
        ["P(X ≤ " + k + ")", K.num(theoryCdf, 4) + " · observed " + K.num(empCdf, 4)],
        ["mean / variance", K.num(m.mean / m.variance, 3) + " (1 for Poisson)"]
      ]);

      s.hint.textContent =
        state.family === "binomial"
          ? "The binomial variance n·p·(1−p) peaks at p = 0.5 and vanishes at the ends. " +
            "Compare the simulated dots with the bars: they should agree to within about " +
            K.num(2 * Math.sqrt((Math.max.apply(null, counts.map(function (c) { return c / draws; })) * (1 - 0.5)) / draws), 3) +
            " in relative frequency."
          : state.family === "poisson"
          ? "For a Poisson variable the mean and the variance both equal λ, so the bars spread as λ grows. " +
            "The simulation reproduces that equality; a real dataset rarely does, which is a diagnostic."
          : "The geometric distribution counts trials up to and including the first success, so its mean is 1/p " +
            "and its variance is (1−p)/p². Integer outcomes mean P(X ≤ k) is a sum, not an integral.";
    }

    sync();
  }

  /* ---------------------------------------------------- L-04 continuous */

  function buildContinuous(root) {
    var s = slots(root);
    if (!s.controls || !s.chart) return;
    V.clear(s.controls);
    V.clear(s.chart);

    var DEFAULTS = { family: "normal", mu: 0, sigma: 1, rate: 1, shape: 2,
                     a: 0, b: 1, lo: -1, hi: 1, draws: 2000, run: 0 };
    var state = Object.assign({}, DEFAULTS);
    var svg = V.svgEl("svg", { width: 640, height: 320 }, s.chart);
    var table = K.table(s.results);

    function familyPdf(x) {
      if (state.family === "normal") return S.normPdf(x, state.mu, state.sigma);
      if (state.family === "exponential") return S.exponPdf(x, state.rate);
      if (state.family === "gamma") return S.gammaPdf(x, state.shape, state.rate);
      return S.uniformPdf(x, state.a, state.b);
    }
    function familyCdf(x) {
      if (state.family === "normal") return S.normCdf(x, state.mu, state.sigma);
      if (state.family === "exponential") return S.exponCdf(x, state.rate);
      if (state.family === "gamma") return S.gammaCdf(x, state.shape, state.rate);
      return S.uniformCdf(x, state.a, state.b);
    }
    function familyDraw(r) {
      if (state.family === "normal") return state.mu + state.sigma * U.gauss(r);
      if (state.family === "exponential") return -Math.log(Math.max(1e-12, 1 - r())) / state.rate;
      if (state.family === "gamma") {
        // Marsaglia–Tsang for shape >= 1 (all defaults satisfy this).
        var shape = state.shape;
        if (shape < 1) {
          var u0 = Math.max(1e-12, r());
          return familyDraw(r) * Math.pow(u0, 1 / shape);
        }
        var d = shape - 1 / 3;
        var c = 1 / Math.sqrt(9 * d);
        for (;;) {
          var x = U.gauss(r);
          var v = 1 + c * x;
          if (v <= 0) continue;
          v = v * v * v;
          var u = r();
          if (u < 1 - 0.0331 * x * x * x * x) return (d * v) / state.rate;
          if (Math.log(u) < 0.5 * x * x + d * (1 - v + Math.log(v))) return (d * v) / state.rate;
        }
      }
      return state.a + (state.b - state.a) * r();
    }
    function familySupport() {
      if (state.family === "normal") return [state.mu - 4 * state.sigma, state.mu + 4 * state.sigma];
      if (state.family === "exponential") return [0, 5 / state.rate];
      if (state.family === "gamma") {
        var mean = state.shape / state.rate;
        var sd = Math.sqrt(state.shape) / state.rate;
        return [0, Math.max(mean + 5 * sd, 0.1)];
      }
      return [state.a - 0.2 * (state.b - state.a), state.b + 0.2 * (state.b - state.a)];
    }

    var familySel = U.select(s.controls, {
      label: "Distribution",
      value: state.family,
      options: [
        { value: "normal", label: "Normal(μ, σ)" },
        { value: "exponential", label: "Exponential(λ)" },
        { value: "gamma", label: "Gamma(shape, λ)" },
        { value: "uniform", label: "Uniform(a, b)" }
      ],
      onChange: function (v) { state.family = v; sync(); }
    });
    var muField = U.slider(s.controls, { id: "cont-mu", label: "Mean μ", min: -3, max: 3, step: 0.5, value: state.mu,
      onInput: function (v) { state.mu = v; changed(); } });
    var sigmaField = U.slider(s.controls, { id: "cont-sigma", label: "SD σ", min: 0.5, max: 3, step: 0.5, value: state.sigma,
      onInput: function (v) { state.sigma = v; changed(); } });
    var rateField = U.slider(s.controls, { id: "cont-rate", label: "Rate λ", min: 0.5, max: 3, step: 0.5, value: state.rate,
      format: function (v) { return v.toFixed(1); },
      onInput: function (v) { state.rate = v; changed(); } });
    var shapeField = U.slider(s.controls, { id: "cont-shape", label: "Shape k (gamma)", min: 1, max: 6, step: 0.5, value: state.shape,
      format: function (v) { return v.toFixed(1); },
      onInput: function (v) { state.shape = v; changed(); } });
    var aField = U.slider(s.controls, { id: "cont-a", label: "Lower bound a", min: -2, max: 1, step: 0.5, value: state.a,
      onInput: function (v) { state.a = v; changed(); } });
    var bField = U.slider(s.controls, { id: "cont-b", label: "Upper bound b", min: 0.5, max: 3, step: 0.5, value: state.b,
      onInput: function (v) { state.b = v; changed(); } });
    var loField = U.slider(s.controls, { id: "cont-lo", label: "Interval low", min: -4, max: 4, step: 0.25, value: state.lo,
      onInput: function (v) { state.lo = v; changed(); } });
    var hiField = U.slider(s.controls, { id: "cont-hi", label: "Interval high", min: -4, max: 6, step: 0.25, value: state.hi,
      onInput: function (v) { state.hi = v; changed(); } });
    var dField = U.slider(s.controls, { id: "cont-draws", label: "Simulated draws", min: 500, max: 5000, step: 500, value: state.draws,
      onInput: function (v) { state.draws = v; changed(); } });

    buttonRow(s.controls, {
      run: function () { state.run += 1; draw(); },
      reset: function () {
        Object.keys(DEFAULTS).forEach(function (k) { state[k] = DEFAULTS[k]; });
        familySel.set(state.family);
        muField.set(state.mu); sigmaField.set(state.sigma); rateField.set(state.rate);
        shapeField.set(state.shape); aField.set(state.a); bField.set(state.b);
        loField.set(state.lo); hiField.set(state.hi); dField.set(state.draws);
        sync();
      }
    });

    K.legend(s.legend, [
      { label: "density f(x) — area, not height, is probability", colour: "teal", kind: "line" },
      { label: "shaded: P(lo < X ≤ hi)", colour: "band", kind: "bar" },
      { label: "simulated draws", colour: "accent", kind: "bar" }
    ]);

    function sync() {
      var f = state.family;
      muField.input.parentNode.style.display = f === "normal" ? "" : "none";
      sigmaField.input.parentNode.style.display = f === "normal" ? "" : "none";
      rateField.input.parentNode.style.display = f === "gamma" || f === "exponential" ? "" : "none";
      shapeField.input.parentNode.style.display = f === "gamma" ? "" : "none";
      aField.input.parentNode.style.display = f === "uniform" ? "" : "none";
      bField.input.parentNode.style.display = f === "uniform" ? "" : "none";
      draw();
    }

    function changed() {
      s.hint.textContent = "Settings changed — press New run to resample the simulated draws.";
    }

    function draw() {
      var range = familySupport();
      var lo = range[0];
      var hi = range[1];
      var a = Math.max(state.lo, lo);
      var b = Math.min(state.hi, hi);
      if (b <= a) b = a;
      var pInterval = Math.max(0, familyCdf(b) - familyCdf(a));
      var mid = 0.5 * (a + b);
      var densityAtMid = familyPdf(mid);

      var r = V.rng(seedOf(root, state.run));
      var draws = state.draws;
      var values = new Array(draws);
      var inside = 0;
      for (var i = 0; i < draws; i++) {
        values[i] = familyDraw(r);
        if (values[i] > a && values[i] <= b) inside += 1;
      }
      var emp = inside / draws;
      var empMean = S.mean(values);
      var empSd = S.sd(values);

      var peak = 0;
      for (var t = lo; t <= hi; t += (hi - lo) / 180) peak = Math.max(peak, familyPdf(t));

      V.clear(svg);
      var f = V.frame(svg, {
        width: 640, height: 320,
        xDomain: [lo, hi],
        yDomain: [0, peak * 1.25],
        xLabel: "x",
        yFormat: function (v) { return v.toFixed(2); }
      });
      K.histBars(f.marks, f, values, 48, lo, hi, "bar bar--faint");
      K.area(f.marks, f, familyPdf, a, b, "area");
      K.curve(f.marks, f, familyPdf, lo, hi, "curve", 240);
      K.vline(f.marks, f, a, "reference");
      K.vline(f.marks, f, b, "reference");
      K.text(f.marks, f, mid, familyPdf(mid) * 0.55,
             "P = " + K.num(pInterval, 3), "label label--strong", "middle");

      U.setAria(
        svg,
        "Density curve of a " + state.family + " random variable with the simulated draws as a " +
          "histogram. The shaded area between " + K.num(a, 2) + " and " + K.num(b, 2) + " is " +
          K.num(pInterval, 3) + " in theory and " + K.num(emp, 3) + " in the simulation."
      );

      s.readout.textContent =
        state.family + "  ·  P(" + K.num(a, 2) + " < X ≤ " + K.num(b, 2) + ") = " +
        K.num(pInterval, 4) + " (observed " + K.num(emp, 3) + ")" +
        "  ·  f(" + K.num(mid, 2) + ") = " + K.num(densityAtMid, 4) + " — a density, not a probability" +
        "  ·  simulated mean " + K.num(empMean, 3) + ", SD " + K.num(empSd, 3);

      table && table.set([
        ["density at the interval midpoint", K.num(densityAtMid, 4)],
        ["P(interval) as an integral", K.num(pInterval, 4)],
        ["P(interval) observed", K.num(emp, 3)],
        ["P(X = a single point)", "0 — continuous variables have no point mass"],
        ["mean of the draws", K.num(empMean, 3)],
        ["SD of the draws", K.num(empSd, 3)],
        ["draws inside the interval", inside.toLocaleString() + " of " + draws]
      ]);

      s.hint.textContent =
        "The curve's height at the midpoint is " + K.num(densityAtMid, 3) +
        ", which is not the probability of anything: the probability is the shaded area, " +
        K.num(pInterval, 3) + ". Widen the interval and the area grows even though the peak " +
        "does not; narrow it to a point and the area goes to zero while the density stays finite.";
    }

    sync();
  }

  REG.builders.probability = buildProbability;
  REG.builders.conditional = buildConditional;
  REG.builders.discrete = buildDiscrete;
  REG.builders.continuous = buildContinuous;
})();
