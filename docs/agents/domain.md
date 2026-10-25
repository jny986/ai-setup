# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring the codebase.

## Before exploring, read these

- **`GLOSSARY.md`** at the repo root.
- **`docs/adr/`**: read ADRs that touch the area you're about to work in.

If any of these files don't exist, **proceed silently**. Don't flag their absence; don't suggest creating them upfront. `/plan docs` uses setup's active modeling reference to create them lazily when terms or decisions are resolved. If that reference is unavailable, it reports the modeling dependency while continuing the plan and interview.

Ignore the submodules under `source-skills/` (named `<owner>-<repo>/`; see `.gitmodules`). They're upstream repos, not part of this repo's domain: don't read their docs as this repo's context, and don't edit them. The index files beside them (`source-skills/SKILLS.md`, `source-skills/skills.html`) belong to this repo.

## File structure

```
/
├── GLOSSARY.md
├── docs/adr/
│   ├── 0001-example-decision.md
│   └── 0002-another-decision.md
├── skills/                            ← this repo's skills
└── source-skills/
    ├── <submodule>/                   ← upstream, ignore
    ├── SKILLS.md
    └── skills.html
```

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal, a hypothesis, a test name), use the term as defined in `GLOSSARY.md`. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, that's a signal: either you're inventing language the project doesn't use (reconsider) or there's a real gap (record the unresolved term in the current plan).

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding:

> _Contradicts ADR-0007 (event-sourced orders), but worth reopening because…_
