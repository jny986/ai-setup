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
├── SKILLS.md          # Index of my skills
├── skills.html        # The same index, grouped by upstream source
└── original-skills/   # Upstream skill repos, as git submodules
    ├── impeccable/
    ├── marketingskills/
    ├── matt-pocock-skills/
    ├── taste-skill/
    ├── SKILLS.md      # Index of every upstream skill
    └── skills.html    # The same index, grouped by repo
```

### `skills/`

These are the skills that `npx skills` installs. Each one's `SKILL.md` frontmatter records where it came from:

```yaml
metadata:
  author: jny986
  author-url: https://jny986.com
  based_on: mattpocock/skills@v1.2.3 (MIT)  # Only on skills adapted from an upstream skill
```

### `original-skills/`

The upstream repos my skills are based on or sit alongside. They're kept as submodules for reference and so I can diff against them, and `npx skills` doesn't install them from this repo. To install one directly, run something like `npx skills add mattpocock/skills`.

| Repo | Author |
|------|--------|
| [impeccable](https://github.com/pbakaus/impeccable) | Paul Bakaus |
| [marketingskills](https://github.com/coreyhaines31/marketingskills) | Corey Haines |
| [skills](https://github.com/mattpocock/skills) | Matt Pocock |
| [taste-skill](https://github.com/Leonxlnx/taste-skill) | Leonxlnx |

Fetch or update the submodules:

```sh
git clone --recurse-submodules https://github.com/jny986/ai-setup.git

# In an existing clone
git submodule update --init

# Pull the latest upstream changes
git submodule update --remote
```

## License

[Apache 2.0](LICENSE). Skills adapted from upstream repos keep their original licence, which is noted in each skill's `based_on` field.
