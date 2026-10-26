# Skills

What a skill in `skills/` contains, and how to add, modify or re-sync one. For routers and their sub-skills, see [router-skills.md](router-skills.md). The skills page of the docs site is generated from `skills/`; see [docs-site.md](docs-site.md).

## Anatomy

| Part | Path | Required |
|---|---|---|
| Skill | `skills/<name>/SKILL.md`, folder name equals frontmatter `name` | Yes |
| Agent metadata | `skills/<name>/agents/openai.yaml` | Yes, on every `SKILL.md` |
| Sub-skill | `skills/<router>/sub-skills/<sub-skill>.md`, a plain file, not a skill | Routers only |
| References | `references/` beside the file that uses them, relative links | No |
| README | `skills/<name>/README.md` with install, usage, resources | Routers |

## Frontmatter

Allowed top-level keys: `name`, `description`, `license`, `metadata`, `disable-model-invocation`, `argument-hint`. Any other key fails `check-skills.py`.

- `description`: max 1024 chars. A model-invoked skill needs a trigger phrase (`use`, `when`, `for`); a user-only skill does not.
- `disable-model-invocation: true` makes the skill user-only. Its `agents/openai.yaml` must set `policy.allow_implicit_invocation: false`; every other skill must set `true`.
- For `author: jny986`, `version` must equal the repo's latest git tag (`1.0.0` while there are no tags) and changes only when the tag changes.
- `metadata` allowed keys: `version`, `author` (required), `author-url`, the three `based_on_*` keys below, and optional `based_on_url`.
- Sub-skill files (`skills/*/sub-skills/**/*.md` outside `references/`, except `name-table.md`) need frontmatter with `name` and `description`. Allowed top-level keys are the list above minus `disable-model-invocation`. `license` and `metadata.author` are optional because the router supplies them; `name` may differ from the file name (the marketing name table aliases old names). `check-skills.py` validates them.

## based_on provenance

Add all three keys when a skill is adapted from an upstream skill; omit all three when it is original. Partial sets fail.

| Key | Value |
|---|---|
| `based_on_repo` | Upstream `owner/name`, as in `.gitmodules` |
| `based_on_version` | `<ref>(<short commit hash>)`: latest tag, or the branch name when the repo has no tags |
| `based_on_skill` | The upstream skill's name |

Rules:

- `based_on_url` is optional: a comma-separated list of web pages the skill draws on that have no repo to pin, such as a Wikipedia article. Write each as `https://… (YYYY-MM-DD)`, the date you last viewed the page. It does not replace the three keys above and is not checked against `.gitmodules`.
- The hash is the commit the submodule in `source-skills/` is pinned at. Get it with `git -C source-skills/<owner>-<repo> rev-parse --short HEAD`, and the ref with `git -C source-skills/<owner>-<repo> describe --tags --always`.
- Several sources: comma-separate each key. `based_on_repo` and `based_on_version` align by position, one version per repo; `based_on_skill` names at least one skill per repo and may name several from the same repo. `skills/security/sub-skills/release-gate.md` is the worked example.
- `check-skills.py` requires `based_on_version` in a `SKILL.md` to match `vX.Y.Z(hash)`. In a sub-skill it accepts `<ref>(hash)`, so a branch such as `main(d18b7aa)` passes. The hash is required in both.
- The legacy single key `based_on: owner/repo@hash` is unknown and fails the check.
- Every file in a `references/` folder records provenance so it can be re-synced on its own. For repository sources, use `metadata` frontmatter with `version` and the three `based_on_*` keys. For website-only sources, use `version` and dated `based_on_url` instead. A reference needs no `name` or `description`. Only a reference written here with no upstream may omit provenance, and it must be listed in `ORIGINAL_REFERENCES` in `scripts/check-skills.py` (today `git/sub-skills/references/gh-review.md`).
- For a build guide in `implement`, take the repo and skill from `sub-skills/name-table.md`.
- Every `based_on_repo` needs a submodule in `.gitmodules`; `check-provenance.py` fails without one.
- Content merged from several upstream files keeps `based_on_*` on each adapted file, including references.

## Add a skill

1. **Upstream source.** When adapting, add the repo as a submodule at `source-skills/<owner>-<repo>`: `git submodule add <url> source-skills/<owner>-<repo>`. Then add it to the `source-skills/` tree in `README.md`.
2. **Write the skill.** Read the [writing agents guide](../../skills/writing/sub-skills/agents.md). Create `SKILL.md` (or `sub-skills/<name>.md` under a router) with frontmatter as above.
3. **Provenance.** Fill in `based_on_*` from the pinned submodule.
4. **Agent metadata.** Add `agents/openai.yaml` with `interface.display_name`, `interface.short_description` and `policy.allow_implicit_invocation`.
5. **Router entry.** For a sub-skill, add a row to the router's table and its description, plus a line in the router's `README.md`.
6. **Docs site.** The public skills page generates from `skills/`. Run `pnpm exec vp run site:build` and `pnpm exec vp run site:check`, then confirm the skill, its description and sub-skills render on the skills page. Update `site/*.md` copy if the change affects setup or usage guidance.
7. **Check.** `scripts/check-all.sh` exits 0.

## Modify a skill

1. Edit the file. Change behaviour in one place; if a meaning lives in two files, fix both.
2. Version: when `metadata.author` is `jny986`, `metadata.version` is always the latest git tag on this repo (`git describe --tags --abbrev=0`; a leading `v` is ignored when comparing). Never bump it for an edit; it changes only when a new tag is created. Other authors bump `metadata.version` for behaviour changes. The indexes read it, so rebuild them.
3. Renaming or moving: update the folder or file name, `name`, router table rows, links, and any `/<skill>` mentions; `grep` the repo for the old name.
4. Adding content from another upstream: append to each `based_on_*` key, keeping the lists aligned.
5. Run the rebuild and `scripts/check-all.sh` as above.

## Re-sync with upstream

1. Update the submodule: `git -C source-skills/<owner>-<repo> pull`, then `git add source-skills/<owner>-<repo>`.
2. Diff the upstream skill against the adapted file. Port what is worth keeping.
3. Set `based_on_version` to the new `<ref>(<hash>)` on each file you re-synced.
4. `python3 scripts/check-provenance.py` lists, per upstream version, how many skill, sub-skill and reference files are behind the pin; `--fail-on-drift` turns that into a failure; `--remote` also compares the pin to upstream HEAD (network).

## Checks

| Check | Covers |
|---|---|
| `scripts/check-skills.py` | `SKILL.md` and sub-skill frontmatter, `based_on_*` format, relative links, chained `git`/`gh` commands in code |
| `scripts/check-provenance.py` | `based_on_repo` has a submodule; `--fail-on-drift` hash matches the pin |
| `scripts/check-agent-yaml.py` | `openai.yaml` keys and invocation policy agree with the skill |
| `scripts/check-readme.py` | Every submodule in `.gitmodules` appears in the README structure tree |
| `scripts/check-references.py`, `check-assets.py`, `check-marketing-structure.py` | References, assets and router layout |
| `scripts/check-all.sh` | All of the above in CI order, plus lint and tests |
