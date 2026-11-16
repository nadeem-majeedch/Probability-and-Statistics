# 01 — Repository Audit Report

**Audit date:** 13 November 2026
**Local path:** `E:\Probability and Statistics` (Windows, Git Bash)
**Remote:** `https://github.com/nadeem-majeedch/Probability-and-Statistics.git`

---

## 1. Method

The audit combined four independent sources, so that no conclusion rests on a
single observation:

1. **Working-tree inspection** — full recursive file listing.
2. **Git inspection** — `status`, `remote -v`, `log --all`, `config --local`,
   `.git/HEAD`, repository size.
3. **Remote inspection** — the GitHub repository page and the GitHub REST API
   record for the repository (visibility, size, branch, licence, Pages status,
   timestamps). No clone, fetch or pull was performed.
4. **Toolchain inspection** — `git --version`, `python --version`, installed
   Python packages relevant to the course.

## 2. Findings

### 2.1 Git configuration

| Property | Observed value | Assessment |
|---|---|---|
| Repository present | Yes — `.git/` created 13 Nov 2026, 61 KB | Initialised, empty |
| Current branch | `main` (`HEAD → refs/heads/main`) | Matches remote default branch |
| Commits | **None** (`No commits yet on main`) | Nothing has ever been committed |
| Remote `origin` (fetch) | `https://github.com/nadeem-majeedch/Probability-and-Statistics.git` | Correct; **left unchanged** |
| Remote `origin` (push) | Same URL | Correct; **left unchanged** |
| Other remotes | None | Clean |
| `core.filemode` | `false` | Expected on Windows |
| `core.ignorecase` | `true` | Expected on Windows (see risk R11) |
| `core.symlinks` | `false` | Expected on Windows; avoid symlinks in the repo |
| Branches / tags | None | — |
| Stash | None | — |
| Submodules / LFS | None | — |

The remote URL matches the brief exactly and was **not** modified, re-pointed or
re-added at any point during this audit.

### 2.2 Working tree contents

Complete listing, excluding `.git/`:

```
.freebuff/.gitignore
.freebuff/project-id
```

Two files, both created by the coding assistant as session metadata. **Neither is
course material**, neither is tracked, and neither should be committed. No other
files or directories exist — no hidden configuration, no stray drafts, no
archives.

### 2.3 Remote repository (GitHub)

| Property | Value | Assessment |
|---|---|---|
| Visibility | `public` | Site will be public when published |
| Size | `0` KB | No content |
| Created | 2026-11-13T15:39:59Z | Created the same day as this audit |
| Pushed | 2026-11-13T15:40:00Z | Initial creation only |
| Default branch | `main` | Consistent with local |
| Description | `null` | Should be set when the site goes live |
| Topics | none | Recommend `statistics`, `probability`, `data-science`, `python`, `education`, `mkdocs` |
| Licence | `null` | Must be chosen before publishing (see 09) |
| GitHub Pages | `has_pages: false` | Not enabled; enabling is the instructor's action |
| Actions / workflows | None (empty repository) | No CI, no deployment automation |
| Issues / PRs / Discussions / Wiki | enabled / none open / disabled / enabled | Issues usable for errata |
| `fork`, `archived`, `disabled` | false | Active |

### 2.4 Documentation framework

**None.** There is no `mkdocs.yml`, `mkdocs.yaml`, `docusaurus.config.*`,
`book.toml`, `_config.yml`, `conf.py`, `package.json`, `quartz.config.*` or any
other static-site configuration. No `requirements.txt`, `pyproject.toml`,
`environment.yml`, `Pipfile` or lockfile. No theme overrides, no custom CSS, no
JavaScript.

### 2.5 GitHub Actions workflows

**None.** `.github/` does not exist. There is no CI, no link checking, no
notebook execution, no Pages deployment workflow. Nothing in this plan creates
one; the deployment workflow is specified but **not installed**, because the
brief forbids starting deployment.

### 2.6 Licences and legal configuration

**None.** No `LICENSE`, `COPYING`, `NOTICE`, `CITATION.cff`, `CODE_OF_CONDUCT.md`
or `CONTRIBUTING.md`. The GitHub API confirms `license: null`. Because third-party
datasets and figures will be used, licence selection is a *prerequisite* for
publishing, not a finishing touch — see the recommendation in
[09 — Risks and Quality](09-risks-and-quality.md).

### 2.7 Existing educational material and student-facing content

**None.** No Markdown pages, no notebooks (`.ipynb`), no datasets (`.csv`,
`.parquet`, `.json`), no figures, no slides, no PDFs, no exercise sets, no quiz
banks, no glossary, no formula sheets. The repository contains zero words of
course content.

Consequence: **nothing can be lost by building here**, and equally, **nothing can
be reused**. The curriculum is designed from first principles in
[02 — Curriculum](02-curriculum.md) rather than assembled from existing drafts.

### 2.8 Toolchain available on the machine

| Tool | Version | Note for this project |
|---|---|---|
| Git | 2.56.0 (windows.2) | Sufficient; supports worktrees, `core.longpaths` |
| Python | 3.14.10 (`python`, also `py`) | **Too new for parts of the scientific stack** — see below |
| JupyterLab | 4.6.6 | Notebook authoring available |
| numpy / scipy / pandas / matplotlib / seaborn / statsmodels | **not installed** in the active interpreter | Must be installed into a project virtual environment |
| MkDocs / Material | **not installed** | Installed in Phase 1 |

**Python version risk.** The default interpreter is Python 3.14. MkDocs Material
9.8.1 requires ≥ 3.11 and will run, but a course whose *content* is Python
execution depends on wheels for numpy, scipy, statsmodels, seaborn and (optionally)
PyMC. Wheel availability for 3.14 lags the release for some of these, and PyMC in
particular has historically trailed by several months. The plan therefore pins a
**Python 3.12 or 3.13 virtual environment** for all content and notebook
execution, and documents the check as a Phase-1 gate rather than discovering a
build failure in Phase 3. Recorded as risk **R07**.

Windows specifics that affect authoring: `core.filemode=false` and
`core.symlinks=false` mean POSIX executable bits and symlinks do not survive a
clone. No part of the design may depend on either.

## 3. Gap analysis against the brief

| # | Required capability | Present | Gap to close | Phase |
|---|---|---|---|---|
| 1 | Git repo with correct remote | Yes | None | — |
| 2 | `.gitignore` | No | Added by this plan | 0 |
| 3 | Student-facing `README.md` | No | Added by this plan | 0 |
| 4 | Licence + citation metadata | No | Choose and add `LICENSE`, `CITATION.cff` | 1 |
| 5 | MkDocs Material site config | No | `mkdocs.yml`, `requirements-docs.txt` | 1 |
| 6 | Site skeleton (home, syllabus, how-to-study, glossary, formula sheet) | No | 6–8 orientation pages | 1 |
| 7 | 30 module pages | No | Part-by-part content build | 2–6 |
| 8 | Practice notebooks + datasets | No | 1 notebook per 2 modules + curated data | 2–7 |
| 9 | Projects, assessments, capstone | No | 3 projects + capstone brief | 7 |
| 10 | Quality automation (links, notebooks, prose) | No | `tools/` scripts + pre-commit | 1, 8 |
| 11 | CI for build validation | No | Workflow — **deferred**, needs authorisation | 8 |
| 12 | Pages deployment | No | Workflow + Pages enablement — **deferred** | 9 |

## 4. Rules compliance record

| Rule from the brief | Compliance |
|---|---|
| Instructor commits and pushes personally | No commit, push, pull, fetch, tag or branch operation was run. `git log` confirms zero commits. |
| Never publish or deploy | No Pages enablement, no workflow, no `sites_*` operation, no hosting action taken. |
| Never change the remote URL | `git remote -v` before and after: identical. |
| Never delete content without inspection | Nothing existed; a full listing is recorded above as evidence. No deletion performed at any point. |
| Work locally in the repository | All writes are inside `E:\Probability and Statistics`. |
| Student-facing `README.md` | Written as a course homepage: outcomes, module map, study protocol, assessment, FAQ. Contains no deployment or maintenance instructions. |

## 5. Audit conclusion

The repository is a **greenfield project with correct plumbing**: right remote,
right default branch, no conflicting history, and no legacy content to
accommodate. There is no technical debt and no migration work. Every constraint in
the brief can be satisfied without touching what exists, and the entire effort can
go into curriculum and content.

Two facts drive the plan and should be settled early:

1. **Licence and attribution must be decided before content is published**, because
   datasets and figures carry their own terms.
2. **The Python environment must be pinned below the system 3.14** so that every
   notebook in the course is guaranteed executable and reproducible.

Neither is a blocker for Phase 1.
