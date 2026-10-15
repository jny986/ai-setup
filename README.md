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
│   ├── marketing/     # Router skill: nested guides by category under references/, plus references/name-table.md
│   └── dev/           # Page and component build references (no SKILL.md), reached from marketing hand-offs
├── SKILLS.md          # Index of my skills
├── skills.html        # The same index, grouped by upstream source
├── CONTEXT.md         # Glossary of this repo's terms
├── docs/              # Agent config docs (agents/) and the router-skill guide
├── scripts/           # Structure and frontmatter checks, run in CI
├── templates/         # Starter AGENTS.md and CLAUDE.md
└── original-skills/   # Upstream skill repos, as git submodules
    ├── impeccable/
    ├── marketingskills/
    ├── matt-pocock-skills/
    ├── taste-skill/
    ├── marketing-skills/
    ├── pagina/
    ├── bricks/
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

`skills/marketing/SKILL.md` is one router over every marketing guide. Guides are nested as `references/<category>/[<group>/]<name>.md`, and [`references/name-table.md`](skills/marketing/references/name-table.md) maps each final name to its path, source and the old flat names that alias to it. Run `/marketing <guide>` with a final name or an old one.

`skills/dev/references/` holds the page and component build guides (`pages/`, `components/`). It is not a skill: marketing guides hand off to it by path, for example `dev/references/pages/marketing/pricing`. Marketing is based on [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills), [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills), [kostja94/pagina](https://github.com/kostja94/pagina) and [kostja94/bricks](https://github.com/kostja94/bricks) (all MIT).

Check the layout with `python3 scripts/check-marketing-structure.py`: it fails on flat guides, unlisted guides, broken links and unresolved dev hand-offs. `python3 scripts/check-skills.py` validates every `SKILL.md`'s frontmatter and relative links. CI runs both plus markdownlint. After adding, moving or renaming a marketing guide, run `python3 scripts/build-marketing-index.py` to rebuild `skills.html` from the `SKILLS.md` table and refresh the guide tree in `SKILLS.md`.

### `original-skills/`

The upstream repos my skills are based on or sit alongside. They're kept as submodules for reference and so I can diff against them, and `npx skills` doesn't install them from this repo. To install one directly, run something like `npx skills add mattpocock/skills`.

| Repo | Author |
|------|--------|
| [impeccable](https://github.com/pbakaus/impeccable) | Paul Bakaus |
| [marketingskills](https://github.com/coreyhaines31/marketingskills) | Corey Haines |
| [skills](https://github.com/mattpocock/skills) | Matt Pocock |
| [taste-skill](https://github.com/Leonxlnx/taste-skill) | Leonxlnx |
| [marketing-skills](https://github.com/kostja94/marketing-skills) | kostja94 |
| [pagina](https://github.com/kostja94/pagina) | kostja94 |
| [bricks](https://github.com/kostja94/bricks) | kostja94 |

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
