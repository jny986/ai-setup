# skills.html

Root `skills.html` is generated. Never hand-edit it; the next build overwrites the change.

This is the usage guide for the skills shipped in this repo: what each does, when to use it, how to ask for it, and which sub-skills it offers. `source-skills/skills.html` is the separate index of upstream collections, grouped by source.

## Update

```sh
python3 scripts/build-index.py
```

Run after adding, moving, renaming or re-describing a skill, or after changing a sub-skill row in the marketing, git, security, design, implement or plan router. The same run rewrites the marked spans in `SKILLS.md`.

## Sources

| Source | Feeds |
|---|---|
| `SKILLS.md` skills table (rows starting with `\| [`) | One entry per package skill: name, description, invocation and automatic/explicit selection label |
| `skills/marketing/SKILL.md` router table | Marketing sub-skill tree, built from the table rows that point at `sub-skills/…md` |
| `skills/git/SKILL.md` Sub-skills table | Git sub-skill table, built from the rows linking `sub-skills/x.md` |
| `skills/plan/SKILL.md` Sub-skills table | Plan sub-skill table, built from the rows linking `sub-skills/x.md` |
| `skills/implement/SKILL.md` Sub-skills table | Implement sub-skill table, built from the rows linking `sub-skills/x.md` |
| `skills/design/SKILL.md` Sub-skills table | Design sub-skill table, parsed from situation rows linking `sub-skills/x.md`; reference bullets stay outside the sub-skill index |
| `skills/security/SKILL.md` Sub-skills table | Security sub-skill table, built from `\| situation \| [`name`](sub-skills/x.md) \|` rows |

Version and Author come from the `metadata:` frontmatter (`version`, `author`) of each `SKILL.md` and each sub-skill file, and show as "—" where a file has no such key. The build rewrites the Version and Author cells of the `SKILLS.md` skills table, so bump the frontmatter, not the table.

Skills appear alphabetically by name, regardless of upstream source. Keep the `SKILLS.md` table alphabetical too.

## Required structure

- Root `skills.html` must show every package skill, with its sub-skills nested directly beneath that skill before the next skill appears.
- Introduce how to ask for skills and sub-skills, and explain automatic selection versus explicit requests. Slash-command examples are for clients supporting that syntax; naming the skill in a request is the general alternative.
- Each skill is an `<article class="skill">` with a stable anchor, `data-skill`, `data-invokable` (`yes` or `no`) and `data-search`. Show its name, description/when to use it, invocation, and link to its `SKILL.md`. Label agent-invokable skills "Automatic or explicit" and user-only skills "Explicit request".
- The main catalogue's `data-skill-count` counts package skills. Upstream grouping, version and author columns belong outside this usage guide; link to the source index for upstream browsing.
- Under each router (marketing, git, security, design, implement and docs), show its sub-skill tree. Skills without sub-skills show only the skill entry.
- A router with subfolders under `sub-skills/` nests one `<details>` per folder beneath its skill entry, with the sub-skill count in `<span class="count">`. Each sub-skill shows its name, when to use it, an invocation through its parent, and a link to the full instructions.
- A router with no subfolders shows a single sub-skill list directly beneath its skill entry.
- Sub-skill links point at the files under `skills/<skill>/sub-skills/`.
- Search matches names and descriptions for skills and sub-skills, exposes matching children with their parent, and offers a clear action and empty state. Keep all content accessible when JavaScript is unavailable and at narrow screen widths.
- `scripts/check-indexes.py` reads the skill article attributes and catalogue count. It also supports the older table/group format used by check fixtures.

## SKILLS.md spans

The script rewrites only the text between these markers, so don't edit between them:

- `<!-- marketing-sub-skills:start -->` … `<!-- marketing-sub-skills:end -->`
- `<!-- git-sub-skills:start -->` … `<!-- git-sub-skills:end -->`
- `<!-- security-sub-skills:start -->` … `<!-- security-sub-skills:end -->`
- `<!-- design-sub-skills:start -->` … `<!-- design-sub-skills:end -->`
- `<!-- implement-sub-skills:start -->` … `<!-- implement-sub-skills:end -->`
- `<!-- docs-sub-skills:start -->` … `<!-- docs-sub-skills:end -->`

The script exits with "markers missing" if any pair is gone.

## Give another skill sub-skills

1. Add a router-table parser beside `sub_skills()`, `linked_sub_skills()` and `situation_sub_skills()` in `scripts/build-index.py`.
2. Build its tree with `tree(rows, "<skill>")`.
3. Add it to the `trees` dict passed to `skills_page`, and add a `splice(...)` call plus a new marker pair in `SKILLS.md`. Render its tree directly beneath the parent skill in root `skills.html`, following the required structure above.

## Check

`python3 scripts/check-marketing-structure.py` and `python3 scripts/check-skills.py` validate sub-skill layout and `SKILL.md` links. `scripts/check-indexes.py` checks that `SKILLS.md` and `skills.html` list the same skills. These checks do not verify that the sub-skill trees are current or nested beneath their parents: rerun the build and look at `git diff skills.html SKILLS.md`. In root `skills.html`, verify that every skill appears once, each router's sub-skills appear beneath it before the next skill, and folder nesting is preserved.
