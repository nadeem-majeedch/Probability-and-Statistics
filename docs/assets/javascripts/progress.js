/* ==========================================================================
   progress.js — local, private progress tracking
   --------------------------------------------------------------------------
   Stores completion in localStorage only. No account, no server, no analytics,
   no cookies, nothing transmitted.

   Contract:
     - A page with  <body data-psds-module="14">  (or any element carrying
       data-psds-module) gets a "Mark this module complete" control inserted
       under the page title.
     - A page with  <div data-psds-progress></div>  gets a progress summary.

   Module pages are delivered from Phase 2 onward; the runtime is installed now
   so that the pattern is fixed before 30 pages depend on it.
   ========================================================================== */

(function () {
  "use strict";

  var KEY = "psds.progress.v1";

  function load() {
    try {
      var raw = window.localStorage.getItem(KEY);
      return raw ? JSON.parse(raw) : {};
    } catch (e) {
      return {};
    }
  }

  function save(state) {
    try {
      window.localStorage.setItem(KEY, JSON.stringify(state));
    } catch (e) {
      /* storage full or disabled: degrade silently, never break the page */
    }
  }

  function buildControl(moduleId, state, onChange) {
    var wrap = document.createElement("div");
    wrap.className = "psds-progress";

    var label = document.createElement("label");
    label.className = "psds-progress__label";

    var box = document.createElement("input");
    box.type = "checkbox";
    box.checked = Boolean(state[moduleId]);
    box.id = "psds-complete-" + moduleId;

    var text = document.createElement("span");
    text.textContent = "Mark this module complete";

    label.appendChild(box);
    label.appendChild(text);
    wrap.appendChild(label);

    box.addEventListener("change", function () {
      if (box.checked) {
        state[moduleId] = new Date().toISOString().slice(0, 10);
      } else {
        delete state[moduleId];
      }
      save(state);
      onChange();
    });

    return wrap;
  }

  function init() {
    var host = document.querySelector("[data-psds-module]");
    if (!host || host.getAttribute("data-psds-ready")) return;

    var moduleId = host.getAttribute("data-psds-module");
    var state = load();

    var control = buildControl(moduleId, state, function () {
      document.dispatchEvent(new CustomEvent("psds:progress"));
    });

    var title = document.querySelector(".md-content h1");
    if (title && title.parentNode) {
      title.parentNode.insertBefore(control, title.nextSibling);
    }
    host.setAttribute("data-psds-ready", "1");
  }

  function initSummary() {
    var hosts = document.querySelectorAll("[data-psds-progress]");
    if (!hosts.length) return;
    var state = load();
    var done = Object.keys(state).length;
    for (var i = 0; i < hosts.length; i++) {
      hosts[i].textContent =
        done === 0
          ? "No modules marked complete yet."
          : done + (done === 1 ? " module marked complete." : " modules marked complete.");
    }
  }

  function run() {
    init();
    initSummary();
  }

  document.addEventListener("psds:progress", initSummary);

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(run);
  } else {
    document.addEventListener("DOMContentLoaded", run);
  }
})();
