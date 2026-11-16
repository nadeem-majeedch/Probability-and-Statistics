/* Interactive self-assessment quizzes.
 *
 * Progressive enhancement: every question is already a radio group plus a
 * <details> answer block, so the page is usable (and printable) with
 * JavaScript disabled. This script adds immediate right/wrong feedback, a
 * per-section score, and a "show all answers" control.
 *
 * No accounts, no network calls, no storage.
 */
(function () {
  "use strict";

  function feedbackFor(question, selected) {
    var correct = question.getAttribute("data-answer");
    var box = question.querySelector(".quiz-feedback");
    var details = question.querySelector(".quiz-answer");
    if (!selected) {
      box.textContent = "Choose an option first.";
      box.className = "quiz-feedback quiz-feedback--empty";
      return null;
    }
    if (selected === correct) {
      box.textContent = "Correct.";
      box.className = "quiz-feedback quiz-feedback--ok";
    } else {
      box.textContent = "Not quite — you chose " + selected + ".";
      box.className = "quiz-feedback quiz-feedback--no";
    }
    if (details) {
      details.open = true;
    }
    return selected === correct;
  }

  function selectedValue(question) {
    var checked = question.querySelector("input[type=radio]:checked");
    return checked ? checked.value : null;
  }

  function markOptions(question) {
    var correct = question.getAttribute("data-answer");
    question.querySelectorAll(".quiz-options li").forEach(function (li) {
      var input = li.querySelector("input");
      li.classList.remove("is-correct", "is-wrong");
      if (input && input.checked && input.value !== correct) {
        li.classList.add("is-wrong");
      }
      if (input && input.value === correct) {
        li.classList.add("is-correct");
      }
    });
  }

  function wire(block) {
    var questions = Array.prototype.slice.call(block.querySelectorAll(".quiz-q"));
    if (!questions.length) {
      return;
    }
    var score = block.querySelector(".quiz-score");

    function updateScore() {
      var answered = 0;
      var right = 0;
      questions.forEach(function (question) {
        var value = selectedValue(question);
        if (!value) {
          return;
        }
        answered += 1;
        if (value === question.getAttribute("data-answer")) {
          right += 1;
        }
      });
      if (score) {
        score.textContent = answered
          ? "Score: " + right + " / " + questions.length + " (" + answered + " answered)"
          : "";
      }
    }

    questions.forEach(function (question) {
      var button = question.querySelector(".quiz-check");
      if (button) {
        button.addEventListener("click", function () {
          feedbackFor(question, selectedValue(question));
          markOptions(question);
          updateScore();
        });
      }
      question.querySelectorAll("input[type=radio]").forEach(function (input) {
        input.addEventListener("change", function () {
          question.querySelectorAll(".quiz-options li").forEach(function (li) {
            li.classList.remove("is-correct", "is-wrong");
          });
          var box = question.querySelector(".quiz-feedback");
          box.textContent = "";
          box.className = "quiz-feedback";
        });
      });
    });

    var all = block.querySelector(".quiz-check-all");
    if (all) {
      all.addEventListener("click", function () {
        questions.forEach(function (question) {
          feedbackFor(question, selectedValue(question));
          markOptions(question);
        });
        updateScore();
      });
    }

    var reveal = block.querySelector(".quiz-reveal");
    if (reveal) {
      reveal.addEventListener("click", function () {
        var open = reveal.getAttribute("data-open") !== "true";
        block.querySelectorAll(".quiz-answer").forEach(function (details) {
          details.open = open;
        });
        reveal.setAttribute("data-open", String(open));
        reveal.textContent = open ? "Hide all answers" : "Show all answers";
      });
    }
  }

  function init() {
    document.querySelectorAll("[data-quiz]").forEach(wire);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  // Material's instant navigation replaces the page body; re-wire on change.
  if (typeof document !== "undefined" && window.document$) {
    window.document$.subscribe(init);
  }
})();
