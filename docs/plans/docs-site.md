# Repository docs site

Status: implemented locally on 2026-10-23 following the user's implementation
request. This is a local plan, not a tracker-published spec. The five-page site,
generated catalogues, browser enhancements and gated Pages workflow are in place.
Local build, repository checks and acceptance tests pass; publication remains
to be verified after the workflow runs on `main`.

## Confirmed requirements

- Create a docs site based on the root `skills.html` page.
- Provide a home page with navigation to documentation about skills, agents,
  and templates.
- Build with HTML and Tailwind CSS.
- Host on GitHub Pages for `jny986/ai-setup`.
- Grill the requirements and create durable planning docs before implementation.
- Audience: anyone using the skills, templates and agents who needs to reference
  their details. Prioritize reference use over marketing or acquisition.
- Main catalogue covers this repo's shipped items. Add a separate Sources page
  listing sources used by the skills.
- List every item on its section index, with accordion details similar to
  `skills.html`; do not create individual item detail pages.
- Include a short introduction, setup instructions and details.
- Keep the existing layout and colours initially; a later redesign is expected.
- Use VitePress and Vite+. A content-generation/build step is acceptable.
- Five pages: Home, Skills, Agents, Templates and Sources. Home provides a
  short introduction, shared setup guidance and links to the four indexes.
- Use a VitePress custom theme with Vue components, semantic HTML and Tailwind
  to preserve the current appearance. Vite+ runs project tasks and checks;
  verify compatibility before selecting exact dependency versions.
- Accordion details show setup/usage guidance and formatted full primary
  instructions or template content, with GitHub source links. Router skills
  retain nested sub-skill summaries and source links, without embedding every
  reference document.
- Sources includes upstream repositories actually used by shipped skills,
  including their sub-skills/references, plus website sources. Deduplicate
  sources and show which skills use them. Website inclusion rules remain open.
- Keep section-level filtering, allow multiple accordions open, use stable
  item anchors and open matching accordions during search.
- Agent guidance covers the existing Claude-style definition and Codex TOML;
  template guidance explains placement and customization, identifying
  machine-specific settings rather than recommending blind copying.

## Existing sources and constraints

- [Repository guide](../../README.md): purpose, installation and project setup.
- [Skills guide](../../skills.html): current searchable usage catalogue,
  invocation examples and nested sub-skills.
- [Index contract](../agents/skills-html.md): root `skills.html` is generated;
  changes belong in its generator rather than hand edits.
- [Generator](../../scripts/build-index.py): produces root `skills.html` and
  updates marked sections of `SKILLS.md`.
- [Skills index](../../SKILLS.md) and skill files under `skills/`: existing
  content and metadata sources.
- `agents/explore/agent.md` and `agents/explore/explore.toml`: current agent
  definition and Codex configuration.
- `templates/AGENTS.md`, `templates/CLAUDE.md`, and `templates/settings.json`:
  current templates. Review portability before recommending copying settings;
  the settings file includes machine-specific paths.
- [.github/workflows/ci.yml](../../.github/workflows/ci.yml): existing repository
  checks. No Pages deployment workflow was found during initial discovery.
- Upstream submodules in `source-skills/` are excluded from project discovery.
- [Glossary](../../GLOSSARY.md): existing project terminology.

## Superseded proposals

- The first-round proposal for individual detail pages was rejected in favour
  of section indexes with accordions.
- The proposed primary focus on discovery and installation was refined to
  reference documentation for anyone using the shipped items.

## Confirmed scope and delivery decisions

The user agreed to all six decisions below in Q13–Q18:

1. Website sources mean websites/articles used as source material, not every
   outbound link, author homepage or service mentioned. Maintain a small
   explicit website-source list mapping URLs to skills alongside automatically
   extracted repository provenance. Review existing links to seed that list;
   do not infer that every external link is source material.
2. Search matches item names, summaries and nested sub-skill summaries within
   the current section. Full instruction text search and global search are
   excluded initially.
3. Preserve the current light theme, desktop jump navigation and responsive
   layout. Provide accessible keyboard-operated accordions, visible focus,
   mobile section navigation, and core readable content without JavaScript.
   Direct item links open the relevant accordion when JavaScript is available.
4. Keep site source in `site/`, separate from internal `docs/`. Generate
   catalogue data from repository files; maintain only introductions/setup
   guidance and website-source mappings by hand. Ignore built output and use
   a committed dependency lockfile. Preserve root `skills.html` and its existing
   generator/checks, linking to the new site without hand-editing generated HTML.
5. Publish the latest main-branch content at
   `https://jny986.github.io/ai-setup/`, using a GitHub Actions build/deploy
   workflow after checks pass. PRs build and validate without publishing;
   local dev and production-preview commands are documented. No custom domain,
   hosted PR previews or historical documentation versions initially.
6. Complete a local implementation plan with page/content contracts,
   architecture, acceptance criteria and ordered work; do not publish GitHub
   issues or start building as part of this interview.

## Verified platform guidance

- [VitePress custom themes](https://vitepress.dev/guide/custom-theme) use a
  Vue layout component. The user approved this refinement of the original
  plain-HTML request in Q8.
- [Vite+ guide](https://www.viteplus.dev/guide/) documents `vp run` for project
  tasks. Do not assume `vp build` replaces VitePress's own build command.
- [VitePress deployment](https://vitepress.dev/guide/deploy) supports GitHub
  Pages and requires a repository base path for project sites; propose
  `/ai-setup/` unless a custom domain is requested.
- [VitePress Vite+ support discussion](https://github.com/vuejs/vitepress/issues/5147)
  is context, not proof of compatibility. Exact versions and integration
  remain untested until implementation.

## Page and content contracts

| Page | Required content |
| --- | --- |
| Home | Short description of this personal setup, shared installation/setup instructions, navigation to Skills, Agents, Templates and Sources, and repository link. Keep the focus on reference use. |
| Skills | Introduction and skill setup instructions; alphabetical catalogue of all package skills; names, descriptions and invocation mode visible before expansion; accordions with usage/invocation and formatted full `SKILL.md` body; nested router sub-skill summaries, invocation examples and GitHub links. |
| Agents | Introduction and setup guidance for the existing agent formats; one accordion per logical agent, with its description, instructions and configuration. Group `agent.md` and `explore.toml` as the two formats of Explore rather than two unrelated agents. Explain their respective placement and client use. |
| Templates | Introduction and placement/customization guidance; one accordion per template file with full content, source link and relevant setup notes. Explain the relationship between `CLAUDE.md` and `AGENTS.md` and identify machine-specific settings to replace. |
| Sources | Introduction, deduplicated upstream repositories used by shipped skills, and explicitly recorded website sources; descriptive links and links to the skills using each source. Include section filtering consistent with the other catalogues. |

Each section uses the existing `skills.html` layout and colour palette as its
visual baseline. Shared navigation exposes all five pages and marks the current
page. Desktop jump links navigate items on the current page. Mobile navigation
must retain access to every section without horizontal overflow.

Use primary file frontmatter for metadata and render its Markdown body as
readable documentation. Show TOML and JSON as code. Keep installation commands
and file paths legible on small screens. Source links open the corresponding
files on GitHub; do not publish raw repo-relative Markdown links that become
broken site routes. Resolve in-scope item links to site anchors where practical;
resolve other repository document links to GitHub.

## Interaction contract

- All items are present in the initial page content. Accordions start collapsed
  unless an item anchor or search result requires expansion. Multiple items
  can remain open for comparison.
- Prefer native `details`/`summary` for keyboard operation and no-JavaScript
  access. Provide semantic headings, labels, skip navigation and visible focus.
- Item IDs are deterministic and collision-free. Preserve existing skill IDs
  such as `skill-tdd` on the new Skills page where practical.
- Navigating to an item anchor opens its enclosing accordion and exposes the
  target, including after client-side navigation and browser back/forward.
- Section search matches names/descriptions and, for Skills, nested sub-skill
  names/descriptions. Full instruction bodies are outside the search scope.
- Searching keeps matching sub-skills with their parent and reveals enclosing
  accordions. Provide a clear action, result count and empty state. Clearing
  restores the complete catalogue. Hide inactive search controls without JS.
- Theme remains light initially. Keep styling tokens and shared components
  centralized so a later visual redesign does not require changing source data.

## Proposed implementation architecture

These are implementation choices within the agreed scope; adjust filenames
when necessary without changing the page/content contracts.

```text
site/
  index.md
  skills.md
  agents.md
  templates.md
  sources.md
  data/
    website-sources.json
  .vitepress/
    config.ts
    theme/
      index.ts
      Layout.vue
      components/
      styles.css
scripts/
  build-site-data.*
package.json
<package-manager lockfile>
.github/workflows/pages.yml
```

- Use VitePress for routing and static generation, with a custom Vue theme and
  compiled Tailwind CSS. Use Vite+ for task execution and relevant JS/TS checks.
  Keep VitePress's build command as the site-build entry point inside the task.
- First verify a minimal VitePress + Vite+ + Tailwind production build. Select
  compatible versions, document the runtime/package-manager requirements and
  commit a lockfile. Do not silently drop a requested tool if compatibility
  fails; report the concrete conflict for resolution.
- Generate catalogue data at build time from local repository files. Prefer a
  shared parser/data model with the current index generator where practical;
  do not scrape generated HTML or independently retype skill descriptions.
- Preserve existing skill inclusion, invocation labels and router-table
  semantics described by `docs/agents/skills-html.md`. Reference documents
  contribute provenance, not extra catalogue skills.
- Read agents and templates from their existing directories. Keep editorial
  setup guidance separate from the original file bodies. Do not rewrite the
  shipped settings template as part of site implementation.
- Read `based_on_repo` across shipped skills, sub-skills and references.
  Normalize repository identities and aggregate affected parent skills. Keep
  current provenance fields and validation intact.
- The website-source list records a descriptive title, URL and affected skill
  names. Validate the mapping and deduplicate repeated URLs; review existing
  source statements to populate it without guessing at undocumented origins.
- Escape code and process Markdown appropriately: source instructions containing
  Vue-like syntax must remain readable text, not execute as site components.
- Render all catalogue entries during static generation. Browser code enhances
  filtering, anchor expansion and navigation; content must not depend on a
  runtime GitHub API or network fetch.
- Keep generated data/cache and built output ignored. Limit VitePress input to
  `site/` so internal planning docs and upstream submodules are not published.
- Preserve `scripts/build-index.py`, root `skills.html`, `SKILLS.md` and their
  checks. Add the new site link through maintained sources/generator code where
  relevant, and regenerate rather than hand-edit the HTML.

## Delivery and maintainer workflow

- Configure the production base as `/ai-setup/`. Every route, asset and dynamic
  anchor link must work beneath that base.
- Add documented Vite+ tasks for site development, generation/build, production
  preview and checks. A fresh checkout with documented prerequisites must build
  without initializing upstream submodules solely for site content.
- On PRs, build and validate the site alongside the existing repository checks.
  Do not deploy PR content or create a separate hosted preview service.
- On pushes to `main`, deploy the built site to GitHub Pages only after the
  required checks pass. Avoid relying on an unrelated workflow having happened
  to finish; encode the dependency in the workflow/job arrangement.
- Use GitHub Pages artifact/deployment actions and the `github-pages`
  environment. During implementation, inspect repository Pages settings and
  document any one-time setting required to select GitHub Actions as the source.
- Document where to edit introductions/setup guidance, how generated catalogues
  update, and how to add website sources. Site content follows current `main`;
  historical versions and a custom domain are excluded.

## Acceptance criteria

1. All five pages build as static output and are reachable through shared
   navigation under `/ai-setup/`, including direct page loads.
2. Every shipped package skill appears exactly once on Skills, alphabetical
   by name. Invocation mode and router/sub-skill structure match the existing
   index contract. The catalogue updates from repository changes on rebuild.
3. Each logical agent and every template file is represented with complete
   primary content, source links and accurate setup/customization guidance.
4. Sources includes all recorded repository provenance and explicit website
   sources, with valid mappings to the skills that use them. Unused submodules
   and incidental outbound links are not promoted into sources.
5. Accordions allow multiple open items, work with a keyboard and without JS,
   and expose deep-linked items when enhanced with JS. Search handles matching
   children, clear, result counts and no matches correctly.
6. The current light palette and page layout are retained across the site.
   Desktop and narrow mobile layouts have readable content, usable navigation,
   visible focus and no page-level horizontal overflow.
7. Markdown, code and repository links render correctly; embedded instructions
   do not execute as Vue templates. No runtime API call is required for content.
8. A clean locked install, production build and preview succeed with documented
   commands. VitePress, Vite+ and Tailwind are all present and verified together.
9. Existing index and repo checks pass. Root `skills.html` continues to work and
   is generated according to its contract. Internal docs and upstream checkouts
   are absent from the published routes.
10. PR validation builds without publishing; main-branch deployment waits for
    checks and targets the correct GitHub Pages URL. Any unperformed deployment
    verification is explicitly reported when implementation is delivered.

## Ordered implementation work

1. Establish the locked toolchain and custom theme with a Home → Skills slice;
   render one real skill and prove a production build at `/ai-setup/`.
2. Generate the complete Skills catalogue, retaining router trees, source links
   and existing index compatibility. Add accordions, filtering and deep links.
3. Add Agents and Templates using the shared catalogue layout, complete file
   content and reviewed placement/customization guidance.
4. Add Sources from provenance plus the reviewed website-source list, including
   links back to affected skills and validation of mappings.
5. Complete Home/setup copy and shared navigation; check responsive behaviour,
   keyboard use, no-JS content and production-base navigation.
6. Add PR build checks and main-branch Pages deployment, maintainer instructions
   and repository links. Run existing checks and focused tests for data coverage,
   provenance/mappings, search/deep-link behaviour and production paths.

Each slice should produce reviewable working output. These are local planning
steps, not published GitHub tickets.

## Exclusions and remaining questions

- No per-item routes, full reference-document mirror, global/full-body search,
  dark theme, visual redesign, custom domain, versioned docs or hosted PR previews.
- No upstream catalogue import, source-submodule edits, template configuration
  rewrite, skill instruction changes or provenance-schema migration.
- No implementation, deployment or issue publishing during this planning task.
- No unresolved product questions remain from Q1–Q18. The subsequent explicit
  implementation request authorized the build. Dependency versions, npm
  commands, reviewed website-source entries and inspected Pages settings are
  recorded in [the maintainer guide](../agents/docs-site.md) and the lockfile.

## Modeling dependency

Setup's `references/modeling.md` is restored in the repository. Installed copies of the setup skill may still lack it until updated.
