/* ==========================================================================
   labs-kit.js — small drawing and reporting helpers shared by every lab
   --------------------------------------------------------------------------
   Loaded after labs.js (which owns the registry and the form widgets) and
   before any lab module. Adds no dependencies and no global state of its own.
   ========================================================================== */

(function () {
  "use strict";

  var REG = (window.PSDSLabs = window.PSDSLabs || { builders: {} });
  if (!REG.utils) return;

  var U = REG.utils;
  var V = U.V;

  /** A results panel: an accessible description list of label/value pairs. */
  function table(host) {
    if (!host) return null;
    V.clear(host);
    var dl = document.createElement("dl");
    dl.className = "psds-results";
    host.appendChild(dl);
    return {
      set: function (rows) {
        V.clear(dl);
        rows.forEach(function (row) {
          var dt = document.createElement("dt");
          dt.textContent = row[0];
          var dd = document.createElement("dd");
          dd.textContent = row[1];
          if (row[2]) {
            var note = document.createElement("span");
            note.className = "psds-results__note";
            note.textContent = " " + row[2];
            dd.appendChild(note);
          }
          dl.appendChild(dt);
          dl.appendChild(dd);
        });
      }
    };
  }

  /** Legend of coloured keys below a chart. */
  function legend(host, items) {
    if (!host) return;
    V.clear(host);
    var box = document.createElement("p");
    box.className = "psds-legend";
    items.forEach(function (item) {
      var key = document.createElement("span");
      key.className = "psds-legend__item psds-legend__item--" + (item.kind || "line");
      var swatch = document.createElement("span");
      swatch.className = "psds-legend__swatch psds-legend__swatch--" + (item.colour || "ink");
      key.appendChild(swatch);
      key.appendChild(document.createTextNode(item.label));
      box.appendChild(key);
    });
    host.appendChild(box);
  }

  /** Sample a function on [a, b] and draw it as a polyline inside a frame. */
  function curve(parent, f, fn, a, b, cls, steps) {
    var n = steps || 200;
    var pts = [];
    for (var i = 0; i <= n; i++) {
      var x = a + ((b - a) * i) / n;
      pts.push([f.x(x), f.y(fn(x))]);
    }
    return V.svgEl("path", { d: V.pathFrom(pts), class: cls || "curve" }, parent);
  }

  /** Filled area under fn between a and b. */
  function area(parent, f, fn, a, b, cls, steps) {
    var n = steps || 120;
    var pts = [[f.x(a), f.y(0)]];
    for (var i = 0; i <= n; i++) {
      var x = a + ((b - a) * i) / n;
      pts.push([f.x(x), f.y(fn(x))]);
    }
    pts.push([f.x(b), f.y(0)]);
    return V.svgEl(
      "path",
      { d: V.pathFrom(pts) + "Z", class: cls || "area" },
      parent
    );
  }

  function text(parent, f, x, y, label, cls, anchor) {
    var t = V.svgEl(
      "text",
      {
        x: f.x(x),
        y: f.y(y),
        "text-anchor": anchor || "start",
        class: cls || "label"
      },
      parent
    );
    t.textContent = label;
    return t;
  }

  function vline(parent, f, x, cls) {
    return V.svgEl(
      "line",
      {
        x1: f.x(x),
        x2: f.x(x),
        y1: f.margin.top,
        y2: f.margin.top + f.plotH,
        class: cls || "reference"
      },
      parent
    );
  }

  function hline(parent, f, y, cls) {
    return V.svgEl(
      "line",
      {
        x1: f.margin.left,
        x2: f.margin.left + f.plotW,
        y1: f.y(y),
        y2: f.y(y),
        class: cls || "reference"
      },
      parent
    );
  }

  /** Empirical histogram bars drawn inside a frame, in density units. */
  function histBars(parent, f, values, bins, lo, hi, cls) {
    var h = V.histogram(values, bins, lo, hi);
    for (var i = 0; i < h.density.length; i++) {
      var x0 = f.x(h.lo + i * h.width);
      var x1 = f.x(h.lo + (i + 1) * h.width);
      V.bar(f.marks, x0, f.y(h.density[i]), x1 - x0, f.y(0) - f.y(h.density[i]), cls);
    }
    return h;
  }

  /** Count how many values fall inside [a, b]. */
  function shareInside(values, a, b) {
    var n = 0;
    for (var i = 0; i < values.length; i++) if (values[i] >= a && values[i] <= b) n += 1;
    return values.length ? n / values.length : NaN;
  }

  function num(x, d) {
    if (x === null || x === undefined || !isFinite(x)) return "—";
    return x.toFixed(d === undefined ? 3 : d);
  }

  function pct(x, d) {
    if (!isFinite(x)) return "—";
    return (100 * x).toFixed(d === undefined ? 1 : d) + "%";
  }

  /** A polite announcement element inside a lab (screen readers). */
  function announce(host, message) {
    if (!host) return;
    host.textContent = message;
  }

  REG.kit = {
    table: table,
    legend: legend,
    curve: curve,
    area: area,
    text: text,
    vline: vline,
    hline: hline,
    histBars: histBars,
    shareInside: shareInside,
    num: num,
    pct: pct,
    announce: announce
  };
})();
