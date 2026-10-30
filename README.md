# JNY986 AI Setup

My personal setup for AI coding agents. It's mostly [Agent Skills](https://agentskills.io) for now, and will grow to include mods, rules and other agent configuration. It's built for my own use, but you're welcome to use any of it.

Read the [documentation site](https://ai.jny986.com/) for setup guidance and searchable references for skills, agents, templates and their sources. Maintainers can [build and preview the site locally](docs/agents/docs-site.md).

## Install

Install the skills with [`npx skills`](https://github.com/vercel-labs/skills):

```sh
# Pick skills interactively
npx skills add jny986/ai-setup

# List available skills without installing
npx skills add jny986/ai-setup --list

# Install specific skills globally
npx skills add jny986/ai-setup -g --skill tdd --skill git

# Update installed skills
npx skills update
```

To install the included agent definitions and personal configuration templates,
download and run the installer (requires Bash, curl and Git; config templates
also require Python 3):

```sh
curl -fsSL https://raw.githubusercontent.com/jny986/ai-setup/main/install.sh | bash
```

The downloaded script fetches the agents and templates from GitHub. From a
repository checkout, run the local copy instead:

```sh
./install.sh
```

The installer detects `~/.agents`, `~/.claude` and `~/.codex`, offers each
existing client, and lets you choose agents, configuration templates, or both.
It asks before replacing changed agent definitions. Template updates preserve
existing instructions outside a managed section and save numbered backups.
Settings merge recursively: template values replace matching values, while
lists retain unrelated entries and add template entries. A local template
history tracks entries added by the installer for later updates. On the first
merge, existing entries are retained because their origin is unknown. Claude's
settings template is optional: review its personal paths, hooks, permissions and
plugins before applying it. Adjust agent models and installed configuration to
suit your setup.

## Set up a project

Install the setup skill for your agent:

```sh
npx skills add jny986/ai-setup --skill setup
```

In the target project, run `/setup` to configure project instructions and engineering workflows for the skills already available, migrate domain glossaries, and check readiness. Describe any narrower setup request in plain language, or ask for a read-only readiness check. Setup asks for unresolved project details and shows proposed file changes for approval before applying them. Existing conventions and configuration are preserved on repeat runs.

The skill configures the issue tracker, optional triage labels, domain doc rules and a coding standards guide (Laravel/PHP, JavaScript and security, picked from the project's languages).

## Structure

```
.
├── skills/            # My skills — one folder per skill, each with a SKILL.md
│   ├── marketing/     # Router skill: nested sub-skills by category under sub-skills/, plus sub-skills/name-table.md
│   ├── design/        # Router skill: eight design workflows plus references by surface
│   ├── security/      # Router skill: five sub-skills (review-code, build-securely, harden-deployment, release-gate, skills-check) over sub-skills/references/
│   ├── git/           # Router: commit, create-pr, code-review, pr-review, review-prs, pr-fixes, ci-fix, resolving-merge-conflicts
│   ├── grill/         # Router: me, docs, spec, tickets
│   ├── writing/       # Router: fragments, shape, beats, edit, humanize, technical, agents, review
│   └── implement/     # Router: direct changes, tickets, specs, plus page and component build guides
├── site/              # Public documentation source; VitePress custom theme and generated catalogues
├── GLOSSARY.md         # Glossary of this repo's terms
├── docs/              # Agent config docs (agents/) and the router-skill guide
├── scripts/           # Repo checks run in CI; `scripts/check-all.sh` runs them all locally
├── tests/             # pytest fixtures for the checks (`pip install -r tests/requirements.txt`)
├── templates/         # Client-specific instruction and settings templates
└── source-skills/     # Upstream skill repos, as git submodules
    ├── pbakaus-impeccable/
    ├── coreyhaines31-marketingskills/
    ├── mattpocock-skills/
    ├── Leonxlnx-taste-skill/
    ├── kostja94-marketing-skills/
    ├── kostja94-pagina/
    ├── kostja94-bricks/
    ├── getsentry-skills/
    ├── addyosmani-agent-skills/
    ├── affaan-m-ECC/
    ├── ArnavPuri-designskills/
    ├── jamditis-claude-skills-journalism/
    ├── CosmoBlk-email-design/
    ├── vercel-labs-web-interface-guidelines/
    ├── blader-humanizer/
    ├── UseAI-pro-openclaw-skills-security/
    ├── OWASP-www-project-agentic-skills-top-10/
    ├── spatie-guidelines-skills/
    ├── claude-dev-suite-claude-dev-suite/
    ├── SKILLS.md      # Index of every upstream skill
    └── skills.html    # The same index, grouped by repo
```

### `skills/`

These are the skills that `npx skills` installs. Each one's `SKILL.md` frontmatter records where it came from:

```yaml
metadata:
  author: jny986
  author-url: https://jny986.com
  # Only on skills adapted from an upstream skill; multiple sources are comma-separated, aligned by position
  based_on_repo: mattpocock/skills
  based_on_version: v1.2.3(6acc160)  # latest tag(short commit hash)
  based_on_skill: implement
```

#### Marketing and implementation routers

`skills/marketing/SKILL.md` is one router over every marketing sub-skill. Sub-skills are nested as `sub-skills/<category>/[<group>/]<name>.md`, and [`sub-skills/name-table.md`](skills/marketing/sub-skills/name-table.md) maps each final name to its path, source and the old flat names that alias to it. Run `/marketing <sub-skill>` with a final name or an old one.

`skills/implement/sub-skills/references/` holds the page and component build guides (`pages/`, `components/`). The implement router selects a direct-change, single-ticket, or whole-spec workflow, then uses page and component workflows for new or existing UI alongside required non-UI changes. `/implement <feature or change>` selects the relevant context and references automatically. Use `/implement ticket`, `/implement spec`, `/implement page`, `/implement component`, or a build-guide name from its [name table](skills/implement/sub-skills/name-table.md). Marketing sub-skills hand off to the build guides by path, for example `implement/sub-skills/references/pages/marketing/pricing.md`. Marketing is based on [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills), [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills), [kostja94/pagina](https://github.com/kostja94/pagina) and [kostja94/bricks](https://github.com/kostja94/bricks) (all MIT).

#### Security router

`skills/security/SKILL.md` routes to five sub-skills by situation: `review-code`, `build-securely`, `harden-deployment`, `release-gate` and `skills-check`. Their depth lives in `sub-skills/references/` (topic guides, `languages/`, `infrastructure/`, review rules and report template, hardening controls, privacy, LLM, dependency and Solana guides). The content is adapted from [getsentry/skills](https://github.com/getsentry/skills) (Apache-2.0), [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) and [affaan-m/ECC](https://github.com/affaan-m/ECC) (MIT); each adapted file's `based_on_*` metadata records its source, and nothing in `skills/security/` links into `source-skills/`.

Check the layout with `python3 scripts/check-marketing-structure.py`: it fails on flat sub-skills, unlisted sub-skills, broken links and unresolved dev hand-offs. `python3 scripts/check-skills.py` validates every `SKILL.md`'s frontmatter and relative links. CI runs both plus markdownlint. After adding, moving or renaming a marketing sub-skill, rebuild the docs site (`pnpm exec vp run site:build`): its skills page at <https://ai.jny986.com/skills.html> is the public reference and generates from `skills/`.

#### Design router

`skills/design/SKILL.md` routes product context, design briefs, visual-system documentation, brand kits, interface audits, task flows, UI consolidation, and refinement through eight sub-skills. Its 37 references cover design surfaces, native platforms, adaptation, visual-reference implementation, and verification. Content is adapted from [ArnavPuri/designskills](https://github.com/ArnavPuri/designskills), [CosmoBlk/email-design](https://github.com/CosmoBlk/email-design), [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) (MIT), and [pbakaus/impeccable](https://github.com/pbakaus/impeccable) (Apache-2.0). Each adapted document records its source in frontmatter.

#### Writing router

[`skills/writing/SKILL.md`](skills/writing/SKILL.md) routes six writing workflows: `fragments`, `shape`, `beats`, `edit`, `humanize` and `agents`. Invoke `/writing <sub-skill>` explicitly. It consolidates the former standalone writing workflows and their supporting guidance; `edit` adds structural and prose editing. See the [writing usage guide](skills/writing/README.md) for installation and examples.

### `source-skills/`

The upstream repos my skills are based on or sit alongside. They're kept as submodules for reference and so I can diff against them, and `npx skills` doesn't install them from this repo. To install one directly, run something like `npx skills add mattpocock/skills`.

| Submodule | Repo | Author |
|-----------|------|--------|
| `pbakaus-impeccable` | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Paul Bakaus |
| `coreyhaines31-marketingskills` | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | Corey Haines |
| `mattpocock-skills` | [mattpocock/skills](https://github.com/mattpocock/skills) | Matt Pocock |
| `Leonxlnx-taste-skill` | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Leonxlnx |
| `kostja94-marketing-skills` | [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) | kostja94 |
| `kostja94-pagina` | [kostja94/pagina](https://github.com/kostja94/pagina) | kostja94 |
| `kostja94-bricks` | [kostja94/bricks](https://github.com/kostja94/bricks) | kostja94 |
| `getsentry-skills` | [getsentry/skills](https://github.com/getsentry/skills) | Sentry |
| `addyosmani-agent-skills` | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Addy Osmani |
| `affaan-m-ECC` | [affaan-m/ECC](https://github.com/affaan-m/ECC) | affaan-m |
| `ArnavPuri-designskills` | [ArnavPuri/designskills](https://github.com/ArnavPuri/designskills) | Arnav Puri |
| `jamditis-claude-skills-journalism` | [jamditis/claude-skills-journalism](https://github.com/jamditis/claude-skills-journalism) | Joe Amditis |
| `CosmoBlk-email-design` | [CosmoBlk/email-design](https://github.com/CosmoBlk/email-design) | George Hartley |
| `vercel-labs-web-interface-guidelines` | [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | Vercel |
| `blader-humanizer` | [blader/humanizer](https://github.com/blader/humanizer) | blader |
| `UseAI-pro-openclaw-skills-security` | [UseAI-pro/openclaw-skills-security](https://github.com/UseAI-pro/openclaw-skills-security) | UseAI-pro |
| `OWASP-www-project-agentic-skills-top-10` | [OWASP/www-project-agentic-skills-top-10](https://github.com/OWASP/www-project-agentic-skills-top-10) | OWASP |
| `spatie-guidelines-skills` | [spatie/guidelines-skills](https://github.com/spatie/guidelines-skills) | Spatie |
| `claude-dev-suite-claude-dev-suite` | [claude-dev-suite/claude-dev-suite](https://github.com/claude-dev-suite/claude-dev-suite) | claude-dev-suite |

Fetch or update the submodules:

```sh
git clone --recurse-submodules https://github.com/jny986/ai-setup.git

# In an existing clone
git submodule update --init

# Pull the latest upstream changes
git submodule update --remote
```

## License

[Apache 2.0](LICENSE). Skills adapted from upstream repos keep their original licence. The source is recorded in each skill's `based_on_repo`, `based_on_version` and `based_on_skill` fields.
