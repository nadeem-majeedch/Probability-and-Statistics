/* ==========================================================================
   viz.js — minimal SVG charting helper for the course labs
   --------------------------------------------------------------------------
   Deliberately small. Supports exactly what the labs need: linear scales,
   histograms, a normal density, axes, paths and a few marks. It is not a
   general charting library and must not become one.

   No dependencies. No network access. Works offline.
   ========================================================================== */

(function (global) {
  "use strict";

  var NS = "http://www.w3.org/2000/svg";

  /** Create an SVG element with attributes, optionally appended to a parent. */
  function svgEl(tag, attrs, parent) {
    var node = document.createElementNS(NS, tag);
    if (attrs) {
      for (var key in attrs) {
        if (Object.prototype.hasOwnProperty.call(attrs, key)) {
          node.setAttribute(key, attrs[key]);
        }
      }
    }
    if (parent) parent.appendChild(node);
    return node;
  }

  /** Remove all children of a node. */
  function clear(node) {
    while (node && node.firstChild) node.removeChild(node.firstChild);
  }

  /** Linear scale: maps [d0, d1] onto [r0, r1] (invertible). */
  function linear(d0, d1, r0, r1) {
    var span = d1 - d0 || 1;
    var f = function (v) {
      return r0 + ((v - d0) * (r1 - r0)) / span;
    };
    f.invert = function (p) {
      return d0 + ((p - r0) * span) / (r1 - r0 || 1);
    };
    f.domain = [d0, d1];
    f.range = [r0, r1];
    return f;
  }

  /** Deterministic PRNG (mulberry32) so every lab run is reproducible. */
  function rng(seed) {
    var a = seed >>> 0;
    return function () {
      a = (a + 0x6d2b79f5) >>> 0;
      var t = a;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  /** Histogram of values into `bins` equal-width bins over [lo, hi]. */
  function histogram(values, bins, lo, hi) {
    var width = (hi - lo) / bins;
    var counts = new Array(bins);
    for (var b = 0; b < bins; b++) counts[b] = 0;

    for (var i = 0; i < values.length; i++) {
      var idx = Math.floor((values[i] - lo) / width);
      if (idx === bins) idx = bins - 1; // include the right edge
      if (idx >= 0 && idx < bins) counts[idx] += 1;
    }

    var n = values.length || 1;
    var density = counts.map(function (c) {
      return c / (n * width);
    });

    return {
      counts: counts,
      density: density,
      width: width,
      lo: lo,
      hi: hi,
      binCenter: function (b) {
        return lo + (b + 0.5) * width;
      }
    };
  }

  /** Standard normal probability density. */
  function normalPdf(x, mu, sd) {
    mu = mu === undefined ? 0 : mu;
    sd = sd === undefined ? 1 : sd;
    var z = (x - mu) / sd;
    return Math.exp(-0.5 * z * z) / (sd * Math.sqrt(2 * Math.PI));
  }

  /** "M x,y L x,y ..." path string from [[x, y], ...]. */
  function pathFrom(points) {
    if (!points.length) return "";
    var d = "M" + points[0][0].toFixed(2) + "," + points[0][1].toFixed(2);
    for (var i = 1; i < points.length; i++) {
      d += "L" + points[i][0].toFixed(2) + "," + points[i][1].toFixed(2);
    }
    return d;
  }

  /** Round tick values across [lo, hi]. */
  function ticks(lo, hi, count) {
    var span = hi - lo;
    if (span <= 0) return [lo];
    var raw = span / count;
    var mag = Math.pow(10, Math.floor(Math.log10(raw)));
    var norm = raw / mag;
    var step = (norm >= 5 ? 10 : norm >= 2 ? 5 : norm >= 1 ? 2 : 1) * mag;
    var out = [];
    var start = Math.ceil(lo / step) * step;
    for (var v = start; v <= hi + 1e-9; v += step) {
      out.push(Math.abs(v) < 1e-9 ? 0 : v);
    }
    return out;
  }

  /** Draw a filled bar for a histogram bin. */
  function bar(parent, x, y, w, h, cls) {
    return svgEl(
      "rect",
      { x: x.toFixed(2), y: y.toFixed(2), width: Math.max(0, w - 0.6).toFixed(2), height: Math.max(0, h).toFixed(2), class: cls || "bar" },
      parent
    );
  }

  /**
   * Compact default tick label: tick values are computed by division, so they
   * carry floating-point noise (0.6000000000000001). Round and trim instead of
   * printing that noise next to the axis.
   */
  function fmtTick(v) {
    if (!isFinite(v)) return "";
    if (Math.abs(v) >= 1000) return Math.round(v).toLocaleString();
    var s = v.toFixed(Math.abs(v) < 10 ? 2 : 0).replace(/\.?0+$/, "");
    return s === "-0" ? "0" : s;
  }

  /**
   * Draw a standard frame: plot area, horizontal grid, axes and tick labels.
   * Returns the inner group and the scales, so callers can draw marks.
   */
  function frame(svg, opts) {
    var width = opts.width;
    var height = opts.height;
    var margin = opts.margin || { top: 12, right: 12, bottom: 30, left: 42 };
    var plotW = width - margin.left - margin.right;
    var plotH = height - margin.top - margin.bottom;

    svg.setAttribute("viewBox", "0 0 " + width + " " + height);
    svg.setAttribute("class", "psds-chart");
    svg.setAttribute("preserveAspectRatio", "xMidYMid meet");

    var x = linear(opts.xDomain[0], opts.xDomain[1], margin.left, margin.left + plotW);
    var y = linear(opts.yDomain[0], opts.yDomain[1], margin.top + plotH, margin.top);

    var gridG = svgEl("g", { class: "grid" }, svg);
    var axisG = svgEl("g", { class: "axis" }, svg);
    var marksG = svgEl("g", {}, svg);

    ticks(opts.yDomain[0], opts.yDomain[1], 4).forEach(function (v) {
      var py = y(v);
      svgEl("line", { x1: margin.left, x2: margin.left + plotW, y1: py, y2: py }, gridG);
      var t = svgEl("text", { x: margin.left - 6, y: py + 3, "text-anchor": "end" }, axisG);
      t.textContent = opts.yFormat ? opts.yFormat(v) : fmtTick(v);
    });

    ticks(opts.xDomain[0], opts.xDomain[1], 6).forEach(function (v) {
      var px = x(v);
      svgEl("line", { x1: px, x2: px, y1: margin.top, y2: margin.top + plotH }, gridG);
      var t = svgEl("text", { x: px, y: margin.top + plotH + 15, "text-anchor": "middle" }, axisG);
      t.textContent = opts.xFormat ? opts.xFormat(v) : fmtTick(v);
    });

    // Axis lines
    svgEl(
      "line",
      { x1: margin.left, x2: margin.left + plotW, y1: margin.top + plotH, y2: margin.top + plotH },
      axisG
    );

    if (opts.xLabel) {
      var xl = svgEl(
        "text",
        { x: margin.left + plotW / 2, y: height - 4, "text-anchor": "middle", class: "label" },
        svg
      );
      xl.textContent = opts.xLabel;
    }

    return { x: x, y: y, marks: marksG, margin: margin, plotW: plotW, plotH: plotH };
  }

  global.PSDSViz = {
    svgEl: svgEl,
    clear: clear,
    linear: linear,
    rng: rng,
    histogram: histogram,
    normalPdf: normalPdf,
    pathFrom: pathFrom,
    ticks: ticks,
    bar: bar,
    frame: frame
  };
})(window);
