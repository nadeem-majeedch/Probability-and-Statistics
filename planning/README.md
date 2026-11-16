# Architecture and Implementation Plan

**Probability and Statistics for Data Science**
Department of Data Science (PUCIT), University of the Punjab, Lahore

This folder is the **instructor-facing planning record** for the course. It is
deliberately kept outside `docs/`, because `docs/` becomes the published student
website. Nothing here is student learning material, and nothing here should
appear in the site navigation.

| # | Document | Covers |
|---|---|---|
| 1 | [01 — Repository Audit](01-repository-audit.md) | What exists today: git state, remote, files, toolchain, gaps |
| 2 | [02 — Curriculum](02-curriculum.md) | **Superseded** — historical 30-module draft: sequencing rationale, coverage matrix, assessment design |
| 3 | [03 — Repository Structure](03-repository-structure.md) | Target directory layout, naming conventions, asset and notebook policy |
| 4 | [04 — Module Learning Objectives](04-module-learning-objectives.md) | **Superseded** — historical objectives for the 30-module draft; live objectives are in `docs/modules/` |
| 5 | [05 — Tools and Libraries](05-tools-and-libraries.md) | Python stack, documentation stack, quality tooling, version policy |
| 6 | [06 — Website Architecture](06-website-architecture.md) | MkDocs Material configuration, navigation, plugins, deployment plan (deferred) |
| 7 | [07 — Design Specification](07-design-specification.md) | Typography, palette, page templates, components, accessibility, dark mode |
| 8 | [08 — Implementation Roadmap](08-implementation-roadmap.md) | Phased delivery plan with exit criteria and effort estimates |
| 9 | [09 — Risks and Quality](09-risks-and-quality.md) | Risk register, quality requirements, QA checklists, governance |
| 10 | [10 — Interactive and Simulation Spec](10-interactive-simulation-spec.md) | **Binding**: lab technology, widget standards, simulation protocol, theory→Python map, academic integrity rules, nine phase gates |
| 11 | [11 — Module Framework (18 modules)](11-module-framework.md) | **Authoritative**: the approved 18-module curriculum, hours, and the mapping from the 30-module draft |

**Reading order for anyone implementing content:** 11 (what to write) → 08 (in what
order) → 10 (to what standard) → 03 (where it goes). Documents 02 and 04 remain for
their reasoning but their module numbering is historical.

---

## Executive summary

### Where the project stands

The repository is **empty of content but correctly configured**. It is a git
repository on branch `main`, with `origin` pointing at
`https://github.com/nadeem-majeedch/Probability-and-Statistics.git`, and **no
commits**. The GitHub repository is public, zero bytes, with no licence, no
description, no workflows and GitHub Pages disabled. The only files in the
working tree are two metadata files created by the coding assistant. There was
therefore **no existing educational material to inspect, preserve, or delete** —
the "do not delete content" rule is satisfied by there being nothing to delete,
and this is recorded in the audit rather than assumed.

### What this plan delivers

1. A **30-module, eight-part curriculum** that runs beginner → advanced across two
   semesters (or a documented one-semester core track), covering every topic
   requested plus the additions that are educationally necessary: statistical
   thinking and study design (M02), convergence and the delta method (M16),
   multiple regression diagnostics (M23), experimental design and A/B testing
   (M29), and a capstone (M30).
2. A **self-study contract**: a fixed twelve-section anatomy for every module, so
   a student never needs an instructor to explain a step, plus a seven-step study
   protocol and self-marking scheme.
3. A **repository architecture** with a hard separation between the published
   student site (`docs/`) and instructor infrastructure (`planning/`, `tools/`,
   `.github/`), so deployment documentation cannot leak into learning material.
4. A **MkDocs Material configuration** — given in full, ready to instantiate in
   Phase 1 — with MathJax equation rendering, Pygments code highlighting, Mermaid
   diagrams, notebook embedding, tuned search, light/dark palettes and
   progress-oriented navigation.
5. A **design specification**: two-font academic typography, an indigo/teal
   palette verified for both modes, page templates, a component vocabulary and an
   accessibility baseline.
6. A **nine-phase roadmap** with explicit exit criteria, and a **risk register**
   whose most consequential entry is external.

### The one decision that needs the instructor's attention now

**Material for MkDocs reaches end of life on 5 May 2027.** It remains the correct
choice for this build — it is mature, it renders the mathematics, code and
diagrams this course needs, and it is what the brief asks for — but a course
repository is expected to outlive a theme. The plan therefore:

- keeps configuration in **standard `mkdocs.yml`** and avoids Insiders-only
  features, so the site stays portable;
- isolates all visual customisation in `docs/assets/stylesheets/extra.css`, which
  the successor project (**Zensical**, MIT-licensed, by the same team, and able to
  read an existing `mkdocs.yml`) can inherit;
- schedules a **migration checkpoint in Phase 9** (before May 2027) rather than
  discovering the problem after the deadline.

This is a scheduling consequence, not a reason to change framework now. Details
are in [06 — Website Architecture](06-website-architecture.md) and risk **R03** in
[09 — Risks and Quality](09-risks-and-quality.md).

### Scope discipline of this plan

**No course content has been written**, as instructed. The only student-facing
file created is `README.md`, which is the repository's front page and course
overview. No `mkdocs.yml`, no `requirements.txt`, no workflow, no module page and
no notebook exists yet; every such artifact is specified here and produced in its
own phase. Nothing was committed, pushed, pulled or published, and the remote URL
was not touched.
