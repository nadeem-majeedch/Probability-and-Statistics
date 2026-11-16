/* ==========================================================================
   labs.js — interactive lab runtime
   --------------------------------------------------------------------------
   Finds every <div data-lab="..."> on the page and builds a complete,
   accessible, keyboard-operable experiment inside it.

   Design rules enforced here (planning/10-interactive-simulate-spec.md):
     - no backend, no network, no keys, no storage of inputs
     - accessible SVG with a state-dependent aria-label
     - a plain-language readout that restates the figure in words
     - a "what changed" hint after every interaction
     - deterministic: each lab seeds its PRNG from data-seed

   Labs: clt (L-04), ci (L-05)
   ========================================================================== */

(function () {
  "use strict";

  var V = window.PSDSViz;
  if (!V) return;

  // Registry shared with the lab modules that load after this file.
  var REG = (window.PSDSLabs = window.PSDSLabs || { builders: {} });
  REG.builders = REG.builders || {};

  /* ---------------------------------------------------------------- utils */

  function el(tag, cls, parent) {
    var node = document.createElement(tag);
    if (cls) node.className = cls;
    if (parent) parent.appendChild(node);
    return node;
  }

  function fmt(x, digits) {
    var d = digits === undefined ? 3 : digits;
    if (!isFinite(x)) return "—";
    return x.toFixed(d);
  }

  function gauss(r) {
    var u1 = Math.max(r(), 1e-12);
    var u2 = r();
    return Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2);
  }

  function mean(a) {
    var s = 0;
    for (var i = 0; i < a.length; i++) s += a[i];
    return s / a.length;
  }

  function sd(a) {
    var m = mean(a);
    var s = 0;
    for (var i = 0; i < a.length; i++) s += (a[i] - m) * (a[i] - m);
    return Math.sqrt(s / (a.length - 1));
  }

  function skewness(a) {
    var n = a.length;
    var m = mean(a);
    var s2 = 0;
    var s3 = 0;
    for (var i = 0; i < n; i++) {
      var d = a[i] - m;
      s2 += d * d;
      s3 += d * d * d;
    }
    var s = Math.sqrt(s2 / n);
    return s === 0 ? 0 : s3 / n / (s * s * s);
  }

  /* Build a labelled slider field. */
  function slider(parent, opts) {
    var wrap = el("label", "psds-field", parent);
    var label = el("span", "psds-field__label", wrap);
    var name = el("span", null, label);
    name.textContent = opts.label;
    var value = el("span", "psds-field__value", label);
    value.textContent = opts.format ? opts.format(opts.value) : String(opts.value);

    var input = document.createElement("input");
    input.type = "range";
    input.min = opts.min;
    input.max = opts.max;
    input.step = opts.step || 1;
    input.value = opts.value;
    input.id = "psds-" + opts.id;
    // The visible caption is a <label>, but it also carries the live value
    // span, which would be read out as part of the control name. An explicit
    // aria-label gives screen readers a stable name ("Sample size n") and lets
    // them announce the value themselves as the slider moves.
    input.setAttribute("aria-label", opts.label);
    wrap.appendChild(input);

    input.addEventListener("input", function () {
      value.textContent = opts.format ? opts.format(Number(input.value)) : input.value;
      if (opts.onInput) opts.onInput(Number(input.value));
    });

    return {
      input: input,
      set: function (v) {
        input.value = v;
        value.textContent = opts.format ? opts.format(v) : String(v);
      }
    };
  }

  /* Build a labelled select field. */
  function select(parent, opts) {
    var wrap = el("label", "psds-field", parent);
    var label = el("span", "psds-field__label", wrap);
    var name = el("span", null, label);
    name.textContent = opts.label;

    var box = document.createElement("select");
    box.setAttribute("aria-label", opts.label);
    opts.options.forEach(function (o) {
      var opt = document.createElement("option");
      opt.value = o.value;
      opt.textContent = o.label;
      if (o.value === opts.value) opt.selected = true;
      box.appendChild(opt);
    });
    wrap.appendChild(box);

    box.addEventListener("change", function () {
      if (opts.onChange) opts.onChange(box.value);
    });

    return {
      input: box,
      set: function (v) {
        box.value = v;
      }
    };
  }

  function button(parent, text, variant, onClick) {
    var b = el("button", variant ? "psds-btn " + variant : "psds-btn", parent);
    b.type = "button";
    b.textContent = text;
    b.addEventListener("click", onClick);
    return b;
  }

  function setAria(svg, text) {
    svg.setAttribute("role", "img");
    svg.setAttribute("aria-label", text);
  }

  /* ------------------------------------------------------------------ CLT */

  var POP = {
    normal: {
      label: "Normal",
      mu: 0,
      sd: 1,
      finite: true,
      draw: function (r) {
        return gauss(r);
      }
    },
    uniform: {
      label: "Uniform (flat)",
      mu: 0,
      sd: 1 / Math.sqrt(3),
      finite: true,
      draw: function (r) {
        return r() * 2 - 1;
      }
    },
    exponential: {
      label: "Exponential (skewed)",
      mu: 1,
      sd: 1,
      finite: true,
      draw: function (r) {
        return -Math.log(Math.max(1e-12, 1 - r()));
      }
    },
    bimodal: {
      label: "Bimodal (two peaks)",
      mu: 0,
      sd: Math.sqrt(0.36 + 2.25),
      finite: true,
      draw: function (r) {
        var centre = r() < 0.5 ? -1.5 : 1.5;
        return centre + 0.6 * gauss(r);
      }
    },
    cauchy: {
      label: "Cauchy (heavy tailed)",
      mu: 0,
      sd: 1,
      finite: false,
      draw: function (r) {
        return Math.tan(Math.PI * (r() - 0.5));
      }
    }
  };

  function buildClt(root) {
    var seed = Number(root.getAttribute("data-seed") || 2026);
    var controls = root.querySelector('[data-role="controls"]');
    var chartHost = root.querySelector('[data-role="chart"]');
    var readout = root.querySelector('[data-role="readout"]');
    var hint = root.querySelector('[data-role="hint"]');
    if (!controls || !chartHost) return;

    V.clear(controls);
    V.clear(chartHost);

    var svg = V.svgEl("svg", { width: 640, height: 340 }, chartHost);

    var state = { pop: "exponential", n: 5, B: 2000 };

    var popSel = select(controls, {
      label: "Population",
      value: state.pop,
      options: Object.keys(POP).map(function (k) {
        return { value: k, label: POP[k].label };
      }),
      onChange: function (v) {
        state.pop = v;
        dirty();
      }
    });

    var nSlider = slider(controls, {
      id: "clt-n",
      label: "Sample size n",
      min: 1,
      max: 200,
      step: 1,
      value: state.n,
      onInput: function (v) {
        state.n = v;
        dirty();
      }
    });

    var bSlider = slider(controls, {
      id: "clt-b",
      label: "Replications B",
      min: 500,
      max: 5000,
      step: 500,
      value: state.B,
      onInput: function (v) {
        state.B = v;
        dirty();
      }
    });

    var buttons = el("div", "psds-lab__buttons", controls);
    button(buttons, "Run simulation", null, draw);
    button(
      buttons,
      "Reset",
      "psds-btn--ghost",
      function () {
        state = { pop: "exponential", n: 5, B: 2000 };
        popSel.set(state.pop);
        nSlider.set(state.n);
        bSlider.set(state.B);
        draw();
      }
    );

    function dirty() {
      hint.textContent = "Settings changed — press Run simulation to resample.";
    }

    function draw() {
      var p = POP[state.pop];
      var r = V.rng(seed);
      var n = state.n;
      var B = state.B;

      var z = new Array(B);
      var means = new Array(B);
      var sigmaOverRootN = p.sd / Math.sqrt(n);

      for (var b = 0; b < B; b++) {
        var sum = 0;
        for (var i = 0; i < n; i++) sum += p.draw(r);
        var m = sum / n;
        means[b] = m;
        // For infinite-variance populations there is no meaningful
        // standardisation, so the means are shown on their own scale.
        z[b] = p.finite ? (m - p.mu) / sigmaOverRootN : m - p.mu;
      }

      var mid = mean(means);
      var spread = sd(means);
      var sk = p.finite ? skewness(z) : NaN;

      var inside = 0;
      for (var j = 0; j < B; j++) if (Math.abs(z[j]) <= 1.96) inside += 1;
      var share = (100 * inside) / B;

      var lo = -4.5;
      var hi = 4.5;
      var hist = V.histogram(z, 45, lo, hi);

      var peak = 0;
      for (var k = 0; k < hist.density.length; k++) peak = Math.max(peak, hist.density[k]);
      peak = Math.max(peak, V.normalPdf(0));

      V.clear(svg);
      var f = V.frame(svg, {
        width: 640,
        height: 340,
        xDomain: [lo, hi],
        yDomain: [0, peak * 1.12],
        xLabel: p.finite ? "standardised sample mean  z = (x̄ − μ) / (σ/√n)" : "sample mean (own scale)",
        yFormat: function (v) {
          return v.toFixed(2);
        }
      });

      for (var bi = 0; bi < hist.density.length; bi++) {
        var x0 = f.x(hist.lo + bi * hist.width);
        var x1 = f.x(hist.lo + (bi + 1) * hist.width);
        V.bar(f.marks, x0, f.y(hist.density[bi]), x1 - x0, f.y(0) - f.y(hist.density[bi]));
      }

      // Standard normal reference curve
      var pts = [];
      for (var t = lo; t <= hi + 1e-9; t += 0.05) {
        pts.push([f.x(t), f.y(V.normalPdf(t))]);
      }
      V.svgEl("path", { d: V.pathFrom(pts), class: "curve" }, f.marks);

      setAria(
        svg,
        "Histogram of " +
          B +
          " sample means of size " +
          n +
          " from a " +
          p.label +
          " population, standardised against the standard normal curve. Mean of the means " +
          fmt(mid, 2) +
          ", standard deviation of the means " +
          fmt(spread, 3) +
          ", " +
          fmt(share, 1) +
          " percent of values within plus or minus 1.96."
      );

      readout.textContent =
        "B = " +
        B.toLocaleString() +
        "  ·  n = " +
        n +
        "  ·  mean of means = " +
        fmt(mid, 3) +
        "  ·  SD of means = " +
        fmt(spread, 3) +
        (p.finite ? "  ·  σ/√n = " + fmt(sigmaOverRootN, 3) : "  ·  σ/√n undefined") +
        "  ·  skew(z) = " +
        (p.finite ? fmt(sk, 2) : "—") +
        "  ·  within ±1.96: " +
        fmt(share, 1) +
        "%";

      var msg;
      if (!p.finite) {
        msg =
          "The Cauchy population has no finite variance, so the theorem's premise is false. The means are plotted on their own scale; increasing n will not produce a normal shape.";
      } else if (Math.abs(sk) > 0.5) {
        msg =
          "The sampling distribution is still clearly skewed (skew " +
          fmt(sk, 2) +
          "), so the normal curve fits poorly. Increase n — not B — to improve the approximation.";
      } else if (Math.abs(sk) > 0.25) {
        msg =
          "Approaching normality but still visibly skewed (skew " +
          fmt(sk, 2) +
          "). A normal approximation is borderline here.";
      } else {
        msg =
          "Close to normal (skew " +
          fmt(sk, 2) +
          "); the standard error is " +
          fmt(sigmaOverRootN, 3) +
          ". This is the regime where the CLT justifies z and t procedures.";
      }
      hint.textContent = msg;
    }

    draw();
  }

  /* ------------------------------------------------------- CI coverage */

  var Z = { "80": 1.2816, "90": 1.6449, "95": 1.96, "99": 2.5758 };

  function buildCi(root) {
    var seed = Number(root.getAttribute("data-seed") || 2026);
    var controls = root.querySelector('[data-role="controls"]');
    var chartHost = root.querySelector('[data-role="chart"]');
    var readout = root.querySelector('[data-role="readout"]');
    var hint = root.querySelector('[data-role="hint"]');
    if (!controls || !chartHost) return;

    V.clear(controls);
    V.clear(chartHost);

    var svg = V.svgEl("svg", { width: 640, height: 380 }, chartHost);

    var MU = 100;
    var SIGMA = 15;
    var state = { level: "95", n: 30, B: 100 };

    var levelSel = select(controls, {
      label: "Confidence level",
      value: state.level,
      options: [
        { value: "80", label: "80%" },
        { value: "90", label: "90%" },
        { value: "95", label: "95%" },
        { value: "99", label: "99%" }
      ],
      onChange: function (v) {
        state.level = v;
        dirty();
      }
    });

    var nSlider = slider(controls, {
      id: "ci-n",
      label: "Sample size n",
      min: 5,
      max: 100,
      step: 5,
      value: state.n,
      onInput: function (v) {
        state.n = v;
        dirty();
      }
    });

    var bSlider = slider(controls, {
      id: "ci-b",
      label: "Intervals drawn B",
      min: 20,
      max: 200,
      step: 20,
      value: state.B,
      onInput: function (v) {
        state.B = v;
        dirty();
      }
    });

    var buttons = el("div", "psds-lab__buttons", controls);
    button(buttons, "Run", null, draw);
    button(
      buttons,
      "Reset",
      "psds-btn--ghost",
      function () {
        state = { level: "95", n: 30, B: 100 };
        levelSel.set(state.level);
        nSlider.set(state.n);
        bSlider.set(state.B);
        draw();
      }
    );

    function dirty() {
      hint.textContent = "Settings changed — press Run to draw new intervals.";
    }

    function draw() {
      var r = V.rng(seed);
      var n = state.n;
      var B = state.B;
      var z = Z[state.level];
      var se = SIGMA / Math.sqrt(n);
      var half = z * se;

      var los = new Array(B);
      var his = new Array(B);
      var captured = 0;
      var minLo = Infinity;
      var maxHi = -Infinity;

      for (var b = 0; b < B; b++) {
        var sum = 0;
        for (var i = 0; i < n; i++) sum += MU + SIGMA * gauss(r);
        var xbar = sum / n;
        los[b] = xbar - half;
        his[b] = xbar + half;
        if (los[b] <= MU && MU <= his[b]) captured += 1;
        minLo = Math.min(minLo, los[b]);
        maxHi = Math.max(maxHi, his[b]);
      }

      var nominal = Number(state.level) / 100;
      var pct = (100 * captured) / B;
      var mcse = (100 * Math.sqrt((nominal * (1 - nominal)) / B));

      var pad = Math.max(0.6, (maxHi - minLo) * 0.04);
      var lo = Math.min(minLo, MU) - pad;
      var hi = Math.max(maxHi, MU) + pad;

      V.clear(svg);
      var f = V.frame(svg, {
        width: 640,
        height: 380,
        xDomain: [lo, hi],
        yDomain: [0, B],
        margin: { top: 14, right: 14, bottom: 34, left: 42 },
        xLabel: "interval for the population mean μ (true value = " + MU + ")",
        yFormat: function () {
          return "";
        }
      });

      // Intervals
      for (var k = 0; k < B; k++) {
        var y = f.margin.top + (f.plotH * (k + 0.5)) / B;
        var miss = !(los[k] <= MU && MU <= his[k]);
        V.svgEl(
          "line",
          {
            x1: f.x(los[k]),
            x2: f.x(his[k]),
            y1: y,
            y2: y,
            class: miss ? "interval interval--miss" : "interval"
          },
          f.marks
        );
      }

      // True mean
      V.svgEl(
        "line",
        {
          x1: f.x(MU),
          x2: f.x(MU),
          y1: f.margin.top,
          y2: f.margin.top + f.plotH,
          class: "reference"
        },
        f.marks
      );
      var label = V.svgEl(
        "text",
        { x: f.x(MU) + 4, y: f.margin.top + 10, class: "label" },
        f.marks
      );
      label.textContent = "μ = " + MU;

      setAria(
        svg,
        B +
          " confidence intervals at the " +
          state.level +
          " percent level from samples of size " +
          n +
          ". A vertical line marks the true mean at " +
          MU +
          ". " +
          captured +
          " intervals contain the true mean; " +
          (B - captured) +
          " miss."
      );

      readout.textContent =
        state.level +
        "% level  ·  n = " +
        n +
        "  ·  B = " +
        B +
        " intervals  ·  captured " +
        captured +
        "/" +
        B +
        " (" +
        fmt(pct, 1) +
        "%)  ·  expected " +
        (nominal * 100).toFixed(0) +
        "% ± " +
        fmt(mcse, 1) +
        "  ·  mean width " +
        fmt(2 * half, 2) +
        "  ·  SE = " +
        fmt(se, 3);

      var diff = Math.abs(pct - nominal * 100);
      var msg;
      if (diff <= 2 * mcse) {
        msg =
          "Observed coverage (" +
          fmt(pct, 1) +
          "%) is within Monte Carlo noise of the nominal " +
          (nominal * 100).toFixed(0) +
          "%. Run again: the count will move, but it should stay in this band.";
      } else {
        msg =
          "Observed coverage (" +
          fmt(pct, 1) +
          "%) is more than two Monte Carlo standard errors (" +
          fmt(mcse, 1) +
          " points) from the nominal level. Rerun with a larger B before drawing conclusions.";
      }
      hint.textContent = msg;
    }

    draw();
  }

  /* ------------------------------------------------ shared with lab modules */

  REG.utils = {
    V: V,
    el: el,
    fmt: fmt,
    gauss: gauss,
    mean: mean,
    sd: sd,
    skewness: skewness,
    slider: slider,
    select: select,
    button: button,
    setAria: setAria
  };

  REG.builders.clt = buildClt;
  REG.builders.ci = buildCi;

  /* Exposed so labs-loader.js can start the runtime as soon as the scripts it
     requested have arrived, including after an instant-navigation swap. */
  REG.init = init;

  /* ---------------------------------------------------------------- boot */

  function init() {
    var nodes = document.querySelectorAll("[data-lab]");
    for (var i = 0; i < nodes.length; i++) {
      var node = nodes[i];
      if (node.getAttribute("data-psds-ready")) continue;
      var builder = REG.builders[node.getAttribute("data-lab")];
      if (!builder) continue;
      node.setAttribute("data-psds-ready", "1");
      try {
        builder(node);
      } catch (e) {
        node.setAttribute("data-psds-ready", "error");
        if (window.console && console.error) {
          console.error("Lab failed to initialise:", node.getAttribute("data-lab"), e);
        }
      }
    }
  }

  // Material's instant navigation swaps the document; re-run on every swap.
  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(init);
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
