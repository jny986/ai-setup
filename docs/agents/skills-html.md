# skills.html

Root `skills.html` is generated. Never hand-edit it; the next build overwrites the change.

## Update

```sh
python3 scripts/build-marketing-index.py
```

Run after adding, moving, renaming or re-describing a skill, or after changing a sub-skill row in the marketing or git router. The same run rewrites the marked spans in `SKILLS.md`.

## Sources

| Source | Feeds |
|---|---|
| `SKILLS.md` skills table (rows starting with `\| [`) | One table row per skill, grouped by upstream: name, "Agent invokable", version, author, description |
| `skills/marketing/SKILL.md` router table | Marketing sub-skill tree, built from the table rows that point at `sub-skills/…md` |
| `skills/git/SKILL.md` Sub-skills table | Git sub-skill table, built from the rows linking `sub-skills/x.md` |

Version and Author come from the `metadata:` frontmatter (`version`, `author`) of each `SKILL.md` and each sub-skill file, and show as "—" where a file has no such key. The build rewrites the Version and Author cells of the `SKILLS.md` skills table, so bump the frontmatter, not the table.

Row order in `SKILLS.md` is page order; keep the table alphabetical by name.

## Structure

- Skills sit in one `<details>` group per upstream, `Original` first: a `Name | Agent invokable | Version | Author | Description` table whose summary carries the count, e.g. `<span>(29)</span>`.
- After the groups, one top-level `<details>` per router lists its sub-skills ("Marketing sub-skills", "Git sub-skills").
- A router with subfolders under `sub-skills/` nests one `<details>` per folder, with the sub-skill count in `<span class="count">`. Each leaf folder holds a `Sub-skill | Version | Author | Use when` table.
- A router with no subfolders is a single sub-skill table.
- Sub-skill links point at the files under `skills/<skill>/sub-skills/`.
- `scripts/check-indexes.py` reads the skill rows and the plain `<span>(N)</span>` group counts. Keep sub-skill counts in `<span class="count">` so the check ignores them.

## SKILLS.md spans

The script rewrites only the text between these markers, so don't edit between them:

- `<!-- marketing-sub-skills:start -->` … `<!-- marketing-sub-skills:end -->`
- `<!-- git-sub-skills:start -->` … `<!-- git-sub-skills:end -->`

The script exits with "markers missing" if either pair is gone.

## Give another skill sub-skills

1. Add a router-table parser beside `sub-skills()` / `git_guides()` in `scripts/build-marketing-index.py`.
2. Build its tree with `tree(rows, "<skill>")`.
3. Add it to the `trees` dict passed to `skills_page`, and add a `splice(...)` call plus a new marker pair in `SKILLS.md`.

## Check

`python3 scripts/check-marketing-structure.py` and `python3 scripts/check-skills.py` validate sub-skill layout and `SKILL.md` links. `scripts/check-indexes.py` checks that `SKILLS.md` and `skills.html` list the same skills. Neither checks that the sub-skill trees are current: rerun the build and look at `git diff skills.html SKILLS.md`.
