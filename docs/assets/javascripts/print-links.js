/* ==========================================================================
   print-links.js — mark links that leave the site, and mute code-line anchors
   --------------------------------------------------------------------------
   Printed pages show a link's destination after the link text, which is useful
   for a reader holding paper. Internal links are absolute in this build, so CSS
   cannot tell them apart from external ones — this adds data-psds-external to
   cross-origin links only, and the print stylesheet keys off that attribute.

   MkDocs also drops one empty <a href="#__codelineno-…"> before every line of
   every code block — 1,800 of them across 47 pages. They are scroll targets,
   but they are focusable and announced as links, so a keyboard user tabbing
   through a code listing stops on nothing, 1,800 times. Hide them from the tab
   order and from assistive technology; the line-number permalinks Material
   draws stay clickable.
   ========================================================================== */

(function () {
  "use strict";

  function mark() {
    var links = document.querySelectorAll(".md-typeset a[href]");
    for (var i = 0; i < links.length; i++) {
      var link = links[i];
      if (link.getAttribute("data-psds-external") !== null) continue;
      var host = "";
      try {
        host = new URL(link.href, location.href).host;
      } catch (e) {
        continue;
      }
      if (host && host !== location.host) {
        link.setAttribute("data-psds-external", "1");
      }
    }
  }

  function muteCodeAnchors() {
    var anchors = document.querySelectorAll('a[id^="__codelineno"]');
    for (var i = 0; i < anchors.length; i++) {
      anchors[i].setAttribute("aria-hidden", "true");
      anchors[i].setAttribute("tabindex", "-1");
    }
  }

  function run() {
    mark();
    muteCodeAnchors();
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(run);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
})();
