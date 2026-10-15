# JNY986 AI Setup

My personal setup for AI coding agents. It's mostly [Agent Skills](https://agentskills.io) for now, and will grow to include mods, rules and other agent configuration. It's built for my own use, but you're welcome to use any of it.

## Install

Install the skills with [`npx skills`](https://github.com/vercel-labs/skills):

```sh
# Pick skills interactively
npx skills add jny986/ai-setup

# List available skills without installing
npx skills add jny986/ai-setup --list

# Install specific skills globally
npx skills add jny986/ai-setup -g --skill tdd --skill code-review

# Update installed skills
npx skills update
```

## Structure

```
.
├── skills/            # My skills — one folder per skill, each with a SKILL.md
│   ├── marketing/     # Router skill: nested sub-skills by category under sub-skills/, plus sub-skills/name-table.md
│   ├── design/        # Router skill: sub-skills being curated
│   ├── security/      # Router skill: four sub-skills (review-code, build-securely, harden-deployment, release-gate) over sub-skills/references/
│   └── dev/           # Page and component build guides (no SKILL.md), reached from marketing hand-offs
├── SKILLS.md          # Index of my skills
├── skills.html        # The same index, grouped by upstream source
├── CONTEXT.md         # Glossary of this repo's terms
├── docs/              # Agent config docs (agents/) and the router-skill guide
├── scripts/           # Repo checks run in CI; `scripts/check-all.sh` runs them all locally
├── tests/             # pytest fixtures for the checks (`pip install -r tests/requirements.txt`)
├── templates/         # Starter AGENTS.md and CLAUDE.md
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

#### Marketing router and dev references

`skills/marketing/SKILL.md` is one router over every marketing sub-skill. Sub-skills are nested as `sub-skills/<category>/[<group>/]<name>.md`, and [`sub-skills/name-table.md`](skills/marketing/sub-skills/name-table.md) maps each final name to its path, source and the old flat names that alias to it. Run `/marketing <sub-skill>` with a final name or an old one.

`skills/dev/references/` holds the page and component build guides (`pages/`, `components/`). It is not a skill: marketing sub-skills hand off to it by path, for example `dev/references/pages/marketing/pricing`. Marketing is based on [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills), [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills), [kostja94/pagina](https://github.com/kostja94/pagina) and [kostja94/bricks](https://github.com/kostja94/bricks) (all MIT).

#### Security router

`skills/security/SKILL.md` routes to four sub-skills by situation: `review-code`, `build-securely`, `harden-deployment` and `release-gate`. Their depth lives in `sub-skills/references/` (topic guides, `languages/`, `infrastructure/`, review rules and report template, hardening controls, privacy, LLM, dependency and Solana guides). The content is adapted from [getsentry/skills](https://github.com/getsentry/skills) (Apache-2.0), [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) and [affaan-m/ECC](https://github.com/affaan-m/ECC) (MIT); each adapted file's `based_on_*` metadata records its source, and nothing in `skills/security/` links into `source-skills/`.

Check the layout with `python3 scripts/check-marketing-structure.py`: it fails on flat sub-skills, unlisted sub-skills, broken links and unresolved dev hand-offs. `python3 scripts/check-skills.py` validates every `SKILL.md`'s frontmatter and relative links. CI runs both plus markdownlint. After adding, moving or renaming a marketing sub-skill, run `python3 scripts/build-marketing-index.py` to rebuild `skills.html` from the `SKILLS.md` table and refresh the marketing, git, security and design sub-skill lists in `SKILLS.md`.

#### Design router

`skills/design/SKILL.md` is a router whose sub-skills are still being curated. Candidate sources: [ArnavPuri/designskills](https://github.com/ArnavPuri/designskills), [CosmoBlk/email-design](https://github.com/CosmoBlk/email-design) and [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) (all MIT).

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
