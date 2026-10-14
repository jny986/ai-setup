# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring the codebase.

## Before exploring, read these

- **`CONTEXT.md`** at the repo root.
- **`docs/adr/`**: read ADRs that touch the area you're about to work in.

If any of these files don't exist, **proceed silently**. Don't flag their absence; don't suggest creating them upfront. The `/domain-modeling` skill (reached via `/grill-with-docs` and `/improve-codebase-architecture`) creates them lazily when terms or decisions actually get resolved.

Ignore the submodules under `original-skills/` (`impeccable/`, `marketingskills/`, `matt-pocock-skills/`, `taste-skill/`; see `.gitmodules`). They're upstream repos, not part of this repo's domain: don't read their docs as this repo's context, and don't edit them. The index files beside them (`original-skills/SKILLS.md`, `original-skills/skills.html`) belong to this repo.

## File structure

```
/
├── CONTEXT.md
├── docs/adr/
│   ├── 0001-example-decision.md
│   └── 0002-another-decision.md
├── skills/                            ← this repo's skills
└── original-skills/
    ├── <submodule>/                   ← upstream, ignore
    ├── SKILLS.md
    └── skills.html
```

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal, a hypothesis, a test name), use the term as defined in `CONTEXT.md`. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, that's a signal: either you're inventing language the project doesn't use (reconsider) or there's a real gap (note it for `/domain-modeling`).

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding:

> _Contradicts ADR-0007 (event-sourced orders), but worth reopening because…_
