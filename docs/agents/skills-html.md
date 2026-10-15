# skills.html

Root `skills.html` is generated. Never hand-edit it; the next build overwrites the change.

## Update

```sh
python3 scripts/build-marketing-index.py
```

Run after adding, moving, renaming or re-describing a skill, or after changing a guide row in the marketing or git router. The same run rewrites the marked spans in `SKILLS.md`.

## Sources

| Source | Feeds |
|---|---|
| `SKILLS.md` skills table (rows starting `\| [`) | One accordion per row: name, "Agent invokable", description, "Based on" links (or "Original") |
| `skills/marketing/SKILL.md` router table | Marketing guide tree, built from `` | `name` | `references/…md` | use | `` rows |
| `skills/git/SKILL.md` Guides table | Git guide table, built from `` | [`name`](references/x.md) | use | `` rows |

Version and Author come from the `metadata:` frontmatter (`version`, `author`) of each `SKILL.md` and each guide file, and show as "—" where a file has no such key. The build rewrites the Version and Author cells of the `SKILLS.md` skills table, so bump the frontmatter, not the table.

Row order in `SKILLS.md` is page order; keep the table alphabetical by name.

## Structure

- One top-level `<details>` per skill. The summary is the skill link plus a green/red invokable badge; the body shows description, version and author, and "Based on".
- Router skills list their guides as references directly inside the skill's `<details>`, with no extra "Guides" wrapper.
- A router with subfolders under `references/` nests one `<details>` per folder, with the guide count in the summary. Each leaf folder holds a `Guide | Version | Author | Use when` table.
- A router with no subfolders is a single `Guide | Version | Author | Use when` table.
- Guide links point at the files under `skills/<skill>/references/`.

## SKILLS.md spans

The script rewrites only the text between these markers, so don't edit between them:

- `<!-- marketing-references:start -->` … `<!-- marketing-references:end -->`
- `<!-- git-references:start -->` … `<!-- git-references:end -->`

The script exits with "markers missing" if either pair is gone.

## Give another skill guides

1. Add a router-table parser beside `guides()` / `git_guides()` in `scripts/build-marketing-index.py`.
2. Build its tree with `tree(rows, "<skill>")`.
3. Add it to the `trees` dict passed to `skills_page`, and add a `splice(...)` call plus a new marker pair in `SKILLS.md`.

## Check

`python3 scripts/check-marketing-structure.py` and `python3 scripts/check-skills.py` validate guide layout and `SKILL.md` links. Neither checks that `skills.html` is current: rerun the build and look at `git diff skills.html SKILLS.md`.
