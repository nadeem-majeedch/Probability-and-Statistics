/* ==========================================================================
   mathjax.js — MathJax 3 configuration
   --------------------------------------------------------------------------
   Two jobs:

   1. Define the course-wide notation macros, so a symbol cannot drift between
      modules. Every macro here is documented in docs/reference/notation.md.

   2. Re-typeset after Material's instant navigation replaces the document.
      Forgetting this is the classic bug where equations render on first load
      and then vanish on the second page.

   MathJax itself is fetched from jsDelivr. If that request fails (offline
   reader, blocked CDN), everything here must stay quiet: the raw TeX is still
   in the page, and body.psds-no-mathjax styles it so the mathematics stays
   legible instead of throwing on every navigation.
   ========================================================================== */

window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    tags: "none",
    macros: {
      E: "\\operatorname{E}",
      Var: "\\operatorname{Var}",
      Cov: "\\operatorname{Cov}",
      sd: "\\operatorname{sd}",
      se: "\\operatorname{se}",
      iid: "\\overset{\\text{iid}}{\\sim}",
      indep: "\\perp\\!\\!\\!\\perp",
      R: "\\mathbb{R}",
      P: "\\Pr"
    }
  },
  options: {
    // Process the whole document, not just pymdownx's <span class="arithmatex">
    // wrappers: the assessment pages build their quiz options from raw HTML, so
    // \(...\) written there is never wrapped and used to print as literal TeX.
    // MathJax still skips <pre>, <code>, <script> and <style> by default.
    ignoreHtmlClass: "psds-math-off"
  }
};

(function () {
  "use strict";

  function ready() {
    return !!(window.MathJax && window.MathJax.startup && window.MathJax.startup.output);
  }

  function typeset() {
    if (!ready()) return;
    MathJax.startup.output.clearCache();
    MathJax.typesetClear();
    MathJax.texReset();
    MathJax.typesetPromise();
  }

  // Re-typeset on every client-side navigation.
  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(typeset);
  }

  // Graceful degradation: mark the page when the CDN script never arrives, so
  // the stylesheet can present the raw TeX readably.
  window.setTimeout(function () {
    if (!ready() && document.body) {
      document.body.classList.add("psds-no-mathjax");
    }
  }, 8000);
})();
