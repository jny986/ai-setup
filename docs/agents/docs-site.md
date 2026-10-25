# Documentation site

The public reference site lives in `site/` and is published at
<https://ai.jny986.com/>. VitePress renders five pages with a custom
Vue theme and compiled Tailwind CSS. Vite+ runs the project tasks. Internal
`docs/` files and upstream `source-skills/` checkouts are outside the site input.

## Develop and verify

Use Node.js LTS and pnpm (pinned in `package.json`), Python 3,
and a checkout of this repository.
Upstream submodules are unnecessary for building the site.

The locked toolchain uses VitePress 2.0.0-alpha.20, Vite+ 1.3.0 and Tailwind
4.3.3. VitePress 2 is a prerelease, selected to use its supported Vite 8 build
dependencies. Vite+ runs the tasks; each build calls VitePress's own build
command. Production builds and browser tests verify the combined toolchain.

```sh
pnpm install --frozen-lockfile
pnpm exec vp run site:dev
```

For a production build and preview:

```sh
pnpm exec vp run site:build
pnpm exec vp run site:check
pnpm exec vp run site:lint
pnpm exec vp run site:preview
```

Open the development or preview server URL at `/`. The production base is `/`
because Pages serves the custom domain at its root. Check direct page loads,
asset requests and internal links at the root when changing routes or assets.

Browser acceptance tests require Chromium:

```sh
pnpm exec playwright install chromium
pnpm exec vp run site:test
```

CI installs Chromium with its Linux system dependencies. Run the existing
repository checks too when changing source files or catalogue generation; see
`scripts/check-all.sh` and `.github/workflows/ci.yml`. Commit `pnpm-lock.yaml`
when changing dependencies. Generated catalogue data, caches and build output
are ignored.

## Edit content

- Edit the introductions and setup guidance in the five `site/*.md` pages.
- Change shared layout, catalogue interactions and styling in
  `site/.vitepress/theme/`; keep appearance separate from generated data.
- Edit skills, agents and templates in their existing repository locations.
  The site generates its catalogue from those files during development/build.
  Preserve the primary instructions and configuration when changing site copy.
- Record website source material in `site/data/website-sources.json`, with a
  descriptive title, URL and names of shipped skills that use it. Add articles
  or websites explicitly used as source material; ordinary outbound links and
  author homepages are not evidence of provenance. Repository provenance comes
  from `based_on_repo` across shipped skills and their nested documents.
- The skills page (`/skills.html`) is the public reference for skills, their
  sub-skills and how to invoke them. It generates from `skills/` frontmatter
  and each router's sub-skill table (`scripts/skilltree.py`); agent invocability
  comes from `disable-model-invocation`. Update the site whenever a skill or
  sub-skill is added, moved, renamed, re-described or re-versioned, and
  rebuild to confirm the change renders.

Rebuild and check that modified items, source mappings and repository links
appear correctly. The catalogue checks validate generated content and mappings;
browser tests cover search, accordion anchors, routing and readable static
content.

## Publish

The `CI` workflow builds and checks the site on pull requests without publishing.
Pushes to `main` upload a Pages artifact; deployment waits for the repository
checks, checker tests and site job to pass. Deployment uses GitHub's Pages
actions and the `github-pages` environment. The public site follows the latest
passing `main` content.

Repository Settings → Pages → Build and deployment must select **GitHub
Actions** as the source. The Pages API was checked during implementation on
2026-10-23: `build_type` was already `workflow`, HTTPS was enabled, the URL was
`https://ai.jny986.com/`, and the custom domain was `ai.jny986.com`. No
settings change is currently needed. If environment protection rules require
approval, complete that approval in the workflow's deployment job.

A successful local build verifies the artifact; publication and the live URL
must be verified after the workflow runs on `main`.
