---
name: update-from-source
description: Pull upstream changes from the source-skills submodules into the adapted skills in skills/.
disable-model-invocation: true
---

# Update from source

Port upstream changes into adapted skills, keeping local adaptations. Scope is the repos or skills named in the request; with none named, every drifted skill.

## 1. Find drift

```sh
git submodule update --remote source-skills/<owner>-<repo>
python3 scripts/check-provenance.py --fail-on-drift
```

Each failure names a skill whose `based_on_version` commit differs from the new submodule pin. The recorded commit is the **base**, the new pin is the **target**. Drift on a skill's source files is the only change that matters; skip skills whose upstream files are untouched between base and target.

Marketing sub-skills record their source in `skills/marketing/sub-skills/name-table.md` rather than frontmatter. Treat each row's source path as that sub-skill's upstream.

## 2. Diff per skill

For each drifted skill, diff its upstream path between base and target:

```sh
git -C source-skills/<owner>-<repo> diff <base>..<target> -- <upstream skill path>
```

Read `CHANGELOG.md` in the upstream repo when present, for the reason behind each change. Renamed, moved or deleted upstream skills get surfaced to the user, not silently followed.

## 3. Port

Three-way: base is upstream before, the local skill is upstream plus our adaptations, target is upstream after. Apply each upstream change unless it conflicts with an adaptation (house style, renamed terms from `GLOSSARY.md`, router structure). Ask the user on any conflict where intent is unclear.

Done when every hunk in the upstream diff is ported, deliberately skipped, or raised with the user, and you can list which.

## 4. Record

- Set `based_on_version` to `<tag>(<short hash>)` of the target: `git -C source-skills/<owner>-<repo> describe --tags --always`, with the hash in parentheses.
- Bump the skill's own `metadata.version`.
- Run `pnpm exec vp run site:build` and `site:check` when a description or router row changed; the docs site skills page generates from `skills/`.
- Run `scripts/check-all.sh`; done when it is green with `check-provenance.py --fail-on-drift` clean for the touched skills.

Leave the submodule bump and skill edits uncommitted for the user to review.
