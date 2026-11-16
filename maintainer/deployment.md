# Deploying the course website

Maintainer documentation. Nothing here is needed by students, and nothing here belongs in the
student-facing `README.md`.

The site is built by **MkDocs Material** and published by **GitHub Actions** to **GitHub Pages**.
No branch contains the built HTML: `site/` is generated in the runner and uploaded as an artifact,
which is the approach GitHub recommends for Pages.

---

## 1. The URL, and why it looks like that

| Repository | Owner type | Published URL |
|---|---|---|
| `nadeem-majeedch/Probability-and-Statistics` | user | `https://nadeem-majeedch.github.io/Probability-and-Statistics/` |

GitHub Pages distinguishes two cases:

- **User/organisation site** — the repository must be named `<owner>.github.io`, and the site is
  served from the domain root: `https://<owner>.github.io/`.
- **Project site** — any other repository name, served from a subpath:
  `https://<owner>.github.io/<repository>/`.

This repository is a project site, so the base path is `/Probability-and-Statistics/`. That is
already correct in `mkdocs.yml`:

```yaml
site_url: https://nadeem-majeedch.github.io/Probability-and-Statistics/
```

`site_url` must be absolute, must end in `/`, and must match the repository name **exactly** —
GitHub Pages paths are case-sensitive. If the repository is ever renamed, `site_url` and the
`repo_url` must change in the same commit, or every link and asset in the generated site breaks.

**Relative paths.** MkDocs links pages relatively (`../modules/...`), so the site works under the
subpath with no further configuration. Do not add a `base`/`basePath` option and do not switch to
absolute-root links: those work at the domain root and fail on a project site. The one place
absolute URLs appear is the 404 page, which MkDocs emits with `site_url` already applied.

**Trailing slash.** The published entry point is
`https://nadeem-majeedch.github.io/Probability-and-Statistics/` (with the slash). Navigating to the
path without it redirects.

---

## 2. One-time setup in the repository

These steps are done once, in the GitHub web interface, by the repository owner.

1. **Push the workflow first.** The workflow file is `.github/workflows/deploy.yml`. It must exist
   on the default branch before Pages can be configured to use it.
2. Open the repository → **Settings** → **Pages**.
3. Under **Build and deployment → Source**, choose **GitHub Actions**.
   Do **not** choose "Deploy from a branch". Branch mode expects committed HTML and would publish
   the repository root or `gh-pages`, neither of which exists here.
4. Leave **Custom domain** empty unless a domain is being attached (see §8).
5. Confirm **Enforce HTTPS** is ticked once the certificate is issued; GitHub normally issues it
   automatically within a few minutes of the first successful deployment.
6. Under **Settings → Actions → General → Workflow permissions**, leave the default
   *Read repository contents* setting. The workflow requests only what it needs at job level.
7. If the organisation enforces environment rules, check **Settings → Environments →
   `github-pages`**. The `github-pages` environment is created automatically by the first
   deployment; adding required reviewers there would make every publish wait for approval.

Nothing else is required: no `gh-pages` branch, no deploy key, no personal access token. The
workflow authenticates to Pages with a short-lived OIDC token (`id-token: write`).

### Required settings, in one table

| Setting | Value | Where |
|---|---|---|
| Pages source | **GitHub Actions** | Settings → Pages |
| Custom domain | empty (unless configured) | Settings → Pages |
| Enforce HTTPS | on | Settings → Pages |
| Workflow permissions | read repository contents | Settings → Actions → General |
| `github-pages` environment | exists, no required reviewers | Settings → Environments |
| Default branch | `main` | Settings → Branches |

---

## 3. What happens after the owner pushes

1. A push to `main` matches `on: push: branches: [main]`.
2. Previous runs for the same ref are cancelled by
   `concurrency: pages-build-${{ github.ref }}` with `cancel-in-progress: true`; a superseded build
   never wastes time finishing.
3. The **build** job installs `requirements.txt` (which defers to `requirements-docs.txt`) and runs,
   in order:
   - a configuration check of `mkdocs.yml` (site URL, docs dir, nav size, plugins, MathJax),
   - `tools/check_math.py` — `\(...\)`/`\[...\]` delimiters balanced, no stray `$` maths,
   - `tools/check_assets.py` — every referenced asset exists and nothing is oversized,
   - `mkdocs build --strict` — warnings become errors, so broken internal links, missing nav
     targets and malformed Markdown all fail the job,
   - `tools/check_site.py` — validates the generated `site/`: core artefacts, all 77 notebook
     downloads present at their published paths, MathJax spans rendered, and ~24,000 internal
     `href`/`src` targets resolving.
4. On success the build job uploads `site/` as the Pages artifact.
5. The **deploy** job starts, serialised on the `pages` concurrency group with
   `cancel-in-progress: false`. It deploys the artifact and exposes the URL as the environment URL.
6. The published site updates within about a minute. GitHub Pages serves from a CDN, so a changed
   page can take a few minutes to appear everywhere; a hard refresh usually settles it.

Any failing check stops the workflow before the artifact is uploaded, so a broken page never
replaces a working deployment: the previously published version stays live.

---

## 4. Monitoring a deployment

- **Actions tab → “Deploy course website”** lists every run with its trigger, duration and status.
- Inside a run, the **build** job shows each validation step; the first red step is the cause.
- The **deploy** job's summary contains the published URL.
- **Settings → Pages** shows the current deployment, its commit, and the “Your site is live at …”
  banner.
- **Settings → Deployments** (or the repository's *Environments* page) shows the `github-pages`
  environment history, which is the authoritative record of what was published and when.
- Email notifications for failed runs are on by default for the actor who pushed.

Useful CLI equivalents, if `gh` is authenticated:

```bash
gh run list --workflow deploy.yml
gh run watch
gh run view --log-failed
```

---

## 5. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `Get Pages site failed` / `Not Found` in *Configure Pages* | Pages is not enabled, or the source is still “Deploy from a branch” | Settings → Pages → Source: **GitHub Actions** |
| `Resource not accessible by integration` on deploy | `pages: write` or `id-token: write` missing | Keep the job-level `permissions` block exactly as in the workflow |
| Deploy fails with `environment protection rules` | reviewers required on `github-pages` | Remove the protection rule, or approve the deployment |
| Build fails at `mkdocs build --strict` | A warning treated as an error: broken link, page missing from nav, bad Markdown | Read the first `WARNING` line in the log; fix the source page |
| `check_math.py` fails | Unbalanced `\(`/`\[` or a stray `$` delimiter | Fix the delimiters; never use `$…$` outside code blocks |
| `check_site.py` reports broken references | A raw-HTML link pointing at `something.md`, which is not rewritten | Use the published path (`something/`) or a Markdown link |
| `check_site.py` reports missing notebooks | A `.ipynb` is linked but absent, or excluded from the build | Add the file under `docs/` or fix the link |
| Site loads without styling or maths | `site_url` does not match the repository name, or the site was opened as a local file | Correct `site_url`; verify over HTTPS, not `file://` |
| 404 on every page except the home page | Pages source is a branch instead of Actions, so `site/` was never published | Switch the source to GitHub Actions and re-run |
| Deployment succeeds but content is stale | Browser or CDN cache | Hard refresh; check the commit SHA in Settings → Pages |
| `Artifact too large` | An unexpected binary landed in `docs/` | Remove it; `check_assets.py` enforces a 2 MB per-file budget |
| Run cancelled immediately | A newer push to `main` superseded it | Expected; the newer run publishes |
| `deploy-pages` waits on a lock | An earlier deployment is still in flight | Wait for it; the `pages` group is deliberately not cancellable |

### Reproducing a CI failure locally

```bash
python -m venv .venv-docs
.venv-docs/Scripts/activate          # Windows
pip install -r requirements.txt
python tools/check_math.py
python tools/check_assets.py
mkdocs build --strict
python tools/check_site.py
```

If all five pass locally and the workflow fails, compare the Python version: CI pins 3.12, and a
much newer local interpreter can resolve different wheels.

---

## 6. Updating the published website

Normal content work needs no deployment knowledge:

1. Edit Markdown under `docs/`, or configuration in `mkdocs.yml`.
2. Run the five local checks above.
3. Commit and push to `main`.

The push builds and publishes. A manual run is available under **Actions → Deploy course
website → Run workflow** (the `workflow_dispatch` trigger) for cases where the site must be
republished without a code change — for example after changing a Pages setting.

**Rolling back.** GitHub Pages publishes the artifact from the latest successful run. To restore an
earlier version, revert the offending commit on `main` and push; the workflow republishes the
reverted content. Re-running an old workflow run republishes that run's artifact, but only if the
artifact is still within its retention window (90 days by default).

**Changing the workflow itself.** Edits to `.github/workflows/deploy.yml` take effect on the next
push to `main`. A workflow file that is syntactically invalid will not run at all; validate with:

```bash
python -c "import yaml; yaml.safe_load(open('.github/workflows/deploy.yml'))"
```

---

## 7. What this workflow deliberately does not do

- It does not build on pull requests. A PR from a fork cannot upload a Pages artifact, and running
  the full publish path on every PR would consume deployment quota for no benefit. Add a separate
  read-only validation workflow if PR checks are wanted.
- It does not commit `site/` anywhere. `site/` is git-ignored, and the artifact is the only copy.
- It does not run the course notebooks. `tools/check_notebooks.py` executes them locally with the
  course environment; CI installs only the documentation stack, so a notebook dependency change
  cannot break a site build.
- It does not deploy to a custom domain automatically. That requires the repository's Pages
  settings and DNS, which are owner actions (§8).

---

## 8. Custom domain (optional, owner action)

1. Settings → Pages → **Custom domain**: enter the domain, e.g. `stats.example.edu`.
2. At the DNS provider, add a `CNAME` record for the host pointing to
   `nadeem-majeedch.github.io`, or `A`/`AAAA` records for an apex domain.
3. Wait for the DNS check to pass, then tick **Enforce HTTPS**.
4. Change `site_url` in `mkdocs.yml` to the new absolute URL ending in `/`, and push. This is
   required: sitemap entries, canonical URLs and the 404 page all use `site_url`.
5. Do not create a `CNAME` file in `docs/` — Pages manages the domain through settings, and a stale
   file in the build output causes redirect loops.

---

## 9. Files involved

| Path | Role |
|---|---|
| `.github/workflows/deploy.yml` | build, validate, upload artifact, deploy |
| `requirements.txt` | the single entry point CI installs; defers to `requirements-docs.txt` |
| `requirements-docs.txt` | pinned MkDocs stack (Material, pymdown-extensions, minify) |
| `mkdocs.yml` | site configuration, including `site_url` and the MathJax setup |
| `hooks/quiz.py` | build-time hook; must stay importable with no extra dependencies |
| `tools/check_math.py` | maths delimiter validation |
| `tools/check_assets.py` | asset existence and size validation |
| `tools/check_site.py` | generated-site validation (artefacts, notebooks, maths, links) |
| `site/` | build output, git-ignored, never committed |
