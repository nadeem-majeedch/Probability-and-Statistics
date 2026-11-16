/* ==========================================================================
   mermaid-init.js — render ```mermaid diagrams without losing them
   --------------------------------------------------------------------------
   Why this exists. Mermaid's own "render on load" hook consumes
   <pre class="mermaid"><code>…</code></pre> and, when it runs against a
   document that Material has already built, it empties the block and leaves a
   blank <div class="mermaid"> behind — which is what every diagram page did
   before this file. Own the rendering instead:

     1. before Mermaid is even requested, take a copy of each diagram's source
        and remove the `mermaid` class, so the library's auto-run has nothing
        to touch;
     2. wait for window.mermaid.render to exist, then draw each saved diagram;
     3. put the finished <svg> where the fence was.

   Degradation: if Mermaid cannot be fetched, the source block is shown again
   as plain text, so a reader still sees the diagram's structure. Nothing here
   is required for the text of a chapter to be readable.
   ========================================================================== */

(function () {
  "use strict";

  var captured = [];
  var drawn = false;

  function mermaidReady() {
    return !!(window.mermaid && typeof window.mermaid.render === "function");
  }

  /* Move each diagram's source out of the DOM's own way, behind a comment
     marker that survives whatever the diagram library does to the element. */
  function capture() {
    var nodes = [].slice.call(document.querySelectorAll(".mermaid"));
    nodes.forEach(function (node) {
      if (node.getAttribute("data-psds-captured")) return;
      node.setAttribute("data-psds-captured", "1");

      var source = node.textContent.replace(/^\s+|\s+$/g, "");
      if (!source) return;

      var marker = document.createComment(" psds-diagram ");
      if (node.parentNode) node.parentNode.insertBefore(marker, node);

      captured.push({ marker: marker, source: source, node: node });
    });

    // Hide the source block (and take it out of Mermaid's selector range) as
    // soon as every banner has been captured.
    captured.forEach(function (item) {
      if (!item.node || !item.node.isConnected) return;
      item.node.removeAttribute("class");
      item.node.hidden = true;
    });
  }

  function reveal(item) {
    if (item.node && item.node.isConnected) item.node.hidden = false;
  }

  function render() {
    if (!mermaidReady()) return;
    drawn = true;

    captured.forEach(function (item, index) {
      if (item.done || !item.marker || !item.marker.isConnected) return;
      item.done = true;

      Promise.resolve(window.mermaid.render("psds-diagram-" + index, item.source)).then(
        function (out) {
          if (!out || !out.svg) {
            reveal(item);
            return;
          }
          var holder = document.createElement("div");
          holder.innerHTML = out.svg;
          var svg = holder.firstElementChild;
          if (!svg || !item.marker.parentNode) {
            reveal(item);
            return;
          }
          item.marker.parentNode.insertBefore(svg, item.marker.nextSibling);
          if (item.node && item.node.isConnected) item.node.remove();
          if (typeof out.bindFunctions === "function") out.bindFunctions(svg);
        },
        function (e) {
          item.done = false;
          reveal(item);
          if (window.console && console.warn) {
            console.warn("Mermaid could not draw a diagram:", e && e.message);
          }
        }
      );
    });
  }

  /* Mermaid's own auto-run may still leave an empty <div class="mermaid">
     behind. Remove those: they are invisible, but they pollute the DOM and
     would be picked up again by the next capture pass. */
  function tidy() {
    [].slice.call(document.querySelectorAll(".mermaid")).forEach(function (node) {
      if (!node.textContent.trim() && !node.querySelector("svg")) node.remove();
    });
  }

  function run() {
    capture();
    loadMermaid();
    if (drawn) render();
    window.setTimeout(tidy, 1500);
  }

  /* Mermaid is ~0.7 MB. It is only requested on the pages that actually hold a
     diagram: capture() has already taken the sources and hidden the blocks, so
     nothing is lost while the library travels. */
  function loadMermaid() {
    if (!captured.length) return;
    if (document.querySelector('script[src*="mermaid.min.js"]')) return;
    var tag = document.createElement("script");
    tag.src = "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js";
    tag.async = true;
    tag.setAttribute("data-psds-mermaid", "1");
    document.head.appendChild(tag);
  }

  // Mermaid arrives from a CDN: wait for it, but never block the page on it.
  var waited = 0;
  var timer = window.setInterval(function () {
    waited += 250;
    if (mermaidReady()) {
      window.clearInterval(timer);
      render();
    } else if (waited > 20000) {
      window.clearInterval(timer);
      captured.forEach(reveal);
    }
  }, 250);

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(run);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
})();
