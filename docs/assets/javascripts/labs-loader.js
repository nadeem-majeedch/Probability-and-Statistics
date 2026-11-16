/* ==========================================================================
   labs-loader.js — load the laboratory runtime only where a page needs it
   --------------------------------------------------------------------------
   The 14 laboratory pages need ~137 KB of JavaScript (stats, viz, the lab
   runtime, the kit and one lab module). The other 148 pages need none of it,
   so nothing here is requested until a page actually contains
   <div data-lab="...">.

   Rules:
     - dependency order is fixed: stats → viz → labs → labs-kit → lab module
     - every file is requested at most once per visit (promise cache)
     - the runtime is initialised after the scripts arrive, and again on every
       Material instant-navigation swap, so a lab page reached by an in-site
       link behaves exactly like a freshly loaded one
     - no build step, no bundler, no module loader: plain <script> tags, so
       GitHub Pages serves it as-is
   ========================================================================== */

(function () {
  "use strict";

  var here = (function () {
    var tag = document.querySelector('script[src$="labs-loader.js"]');
    return tag ? tag.src.replace(/[^/]*$/, "") : "assets/javascripts/";
  })();

  var promises = {};

  function load(file) {
    if (promises[file]) return promises[file];
    promises[file] = new Promise(function (resolve) {
      var s = document.createElement("script");
      s.src = file.indexOf("://") === -1 ? here + file : file;
      s.async = false;
      s.onload = resolve;
      // A missing or blocked file must not stop the page: resolve anyway and
      // let the lab runtime report what it could not build.
      s.onerror = function () {
        if (window.console && console.warn) {
          console.warn("Could not load " + file);
        }
        resolve();
      };
      document.head.appendChild(s);
    });
    return promises[file];
  }

  function chain(files) {
    return files.reduce(function (p, file) {
      return p.then(function () {
        return load(file);
      });
    }, Promise.resolve());
  }

  /* Lab id → the single module file that registers it. clt and ci live in the
     runtime itself, so they need no module. */
  var MODULE = {
    probability: "labs-probability.js",
    conditional: "labs-probability.js",
    discrete: "labs-probability.js",
    continuous: "labs-probability.js",
    normal: "labs-inference.js",
    lln: "labs-inference.js",
    sampling: "labs-inference.js",
    pvalues: "labs-inference.js",
    regression: "labs-modelling.js",
    bayes: "labs-modelling.js",
    power: "labs-modelling.js",
    anova: "labs-modelling.js"
  };

  var labsReady = null;

  function initLabs() {
    if (window.PSDSLabs && typeof window.PSDSLabs.init === "function") {
      window.PSDSLabs.init();
    }
  }

  function bootLabs() {
    var nodes = document.querySelectorAll("[data-lab]");
    if (!nodes.length) return;

    if (labsReady) {
      initLabs();
      return;
    }

    var files = ["stats.js", "viz.js", "labs.js", "labs-kit.js"];
    for (var i = 0; i < nodes.length; i++) {
      var module = MODULE[nodes[i].getAttribute("data-lab")];
      if (module && files.indexOf(module) === -1) files.push(module);
    }

    labsReady = chain(files).then(initLabs);
  }

  function boot() {
    bootLabs();
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(boot);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
