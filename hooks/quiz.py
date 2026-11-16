"""MkDocs hook: compile ```quiz blocks into interactive multiple-choice questions.

Authoring format (one fence may hold many questions):

    ```quiz
    Q1. Stem text, with \\(inline\\) maths allowed.
    A) first option
    B) second option
    C) third option
    D) fourth option
    * B
    Why: why B is right; why the others mislead.
    ```

Rules
-----
* ``Q<number>.`` starts a question.
* ``A)`` … ``E)`` are options.
* ``* X`` names the correct option (exactly one per question).
* ``Why:`` starts the explanation; following plain lines continue it until the
  next question marker.

The output is semantic HTML with real radio inputs, a per-question answer
``<details>`` block (so the page still works with JavaScript disabled and
prints as a question sheet plus answer key), and data attributes that
``assets/javascripts/quiz.js`` upgrades into immediate feedback.
"""

from __future__ import annotations

import html
import re

QUIZ_BLOCK = re.compile(r"^```quiz[ \t]*\n(.*?)^```[ \t]*$", re.MULTILINE | re.DOTALL)
QUESTION = re.compile(r"^Q(\d+)[.)]\s*(.*)$")
OPTION = re.compile(r"^([A-E])\)\s*(.*)$")
ANSWER = re.compile(r"^\*\s*([A-E])\s*$")
WHY = re.compile(r"^Why:\s*(.*)$")

PAGE_COUNTERS: dict[str, int] = {}


def _parse(block: str) -> list[dict]:
    questions: list[dict] = []
    current: dict | None = None
    mode = None
    for raw in block.splitlines():
        line = raw.rstrip()
        if not line.strip():
            if mode == "why" and current is not None:
                current["why"].append("")
            continue
        match = QUESTION.match(line)
        if match:
            current = {"number": match.group(1), "stem": match.group(2).strip(),
                       "options": [], "answer": None, "why": []}
            questions.append(current)
            mode = "stem"
            continue
        if current is None:
            continue
        match = OPTION.match(line)
        if match and mode in ("stem", "option", "why"):
            current["options"].append((match.group(1), match.group(2).strip()))
            mode = "option"
            continue
        match = ANSWER.match(line)
        if match:
            current["answer"] = match.group(1)
            mode = "answer"
            continue
        match = WHY.match(line)
        if match:
            current["why"].append(match.group(1).strip())
            mode = "why"
            continue
        if mode == "why":
            current["why"].append(line.strip())
        elif mode == "option" and current["options"]:
            label, text = current["options"][-1]
            current["options"][-1] = (label, text + " " + line.strip())
    for item in questions:
        if len(item["options"]) < 2 or item["answer"] is None:
            raise ValueError(f"malformed quiz question Q{item['number']}: {item['stem'][:60]}")
    return questions


def _render(questions: list[dict], page_key: str) -> str:
    index = PAGE_COUNTERS.get(page_key, 0) + 1
    PAGE_COUNTERS[page_key] = index
    block_id = f"{page_key}-quiz{index}"
    parts = [f'<div class="quiz" data-quiz id="{block_id}">']
    for q_index, item in enumerate(questions, start=1):
        radio = f"{block_id}-q{q_index}"
        why = " ".join(item["why"]).strip()
        parts.append(
            f'<div class="quiz-q" data-answer="{html.escape(item["answer"])}" '
            f'data-number="{html.escape(item["number"])}">'
        )
        parts.append(f'<p class="quiz-stem"><span class="quiz-num">Q{item["number"]}.</span> '
                     f'{item["stem"]}</p>')
        parts.append('<ul class="quiz-options">')
        for label, text in item["options"]:
            parts.append(
                f'<li><label><input type="radio" name="{radio}" value="{label}">'
                f'<span class="quiz-label">{label}.</span> {text}</label></li>'
            )
        parts.append("</ul>")
        parts.append(
            '<p class="quiz-controls">'
            '<button type="button" class="quiz-check">Check answer</button>'
            '<span class="quiz-feedback" role="status" aria-live="polite"></span>'
            "</p>"
        )
        parts.append(
            '<details class="quiz-answer"><summary>Answer and explanation</summary>'
            f'<p><strong>Correct answer: {item["answer"]}.</strong> {why}</p></details>'
        )
        parts.append("</div>")
    parts.append(
        '<p class="quiz-toolbar"><button type="button" class="quiz-check-all">'
        "Check all</button>"
        '<button type="button" class="quiz-reveal">Show all answers</button>'
        '<span class="quiz-score" role="status" aria-live="polite"></span></p>'
    )
    parts.append("</div>")
    return "\n".join(parts)


def on_page_markdown(markdown, page=None, config=None, files=None, **kwargs):
    page_key = "page"
    if page is not None:
        page_key = str(page.file.src_path).replace("/", "-").replace(".md", "")
        PAGE_COUNTERS.pop(page_key, None)

    def replace(match: re.Match) -> str:
        return _render(_parse(match.group(1)), page_key)

    return QUIZ_BLOCK.sub(replace, markdown)
