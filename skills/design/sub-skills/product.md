---
name: product
description: "Capture or update durable product context in a project's root PRODUCT.md: users, jobs, workflows, positioning, constraints, and confirmed commitments."
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: pbakaus/impeccable
  based_on_version: main(2f98774)
  based_on_skill: init
---

# Product context

Write `PRODUCT.md` at the project root unless the user specifies another location. It records durable product truth for future design work. Keep a domain glossary such as `GLOSSARY.md` in its existing role; link to it for shared terminology rather than copying it.

## Workflow

1. **Inspect evidence.** Read an existing `PRODUCT.md`, project brief, product copy, routes, workflows, roles, assets, and applicable domain docs. Separate explicit commitments from inferences and open questions. Preserve useful existing sections.
2. **Resolve material gaps.** Ask only for facts that would change future product decisions and cannot be established from the request or project. Confirm uncertain inferences before stating them as facts. An unanswered question remains undecided.
3. **Write or update.** Capture the primary users and their jobs; purpose and success; differentiating mechanism or positioning; operating workflows; capabilities and constraints; platform and accessibility needs; confirmed voice, assets, and other brand commitments; and evidence available for future work. Include only supported sections. Record open decisions explicitly. When updating, edit affected sections rather than replacing the file.
4. **Check the boundary.** Keep palettes, fonts, components, visual direction, and page concepts in `DESIGN.md` or `BRANDKIT.md`. Link to those files if a confirmed product commitment constrains them. Check each factual claim against its source and report remaining open decisions.

Completion: `PRODUCT.md` contains the durable facts established by the task, labels unresolved material decisions, and preserves confirmed prior facts outside the requested change.

## Suggested headings

Use headings that fit the project; omit empty sections.

```markdown
# Product

## Users and Jobs
## Product Purpose
## Positioning
## Operating Context
## Capabilities and Constraints
## Platform and Accessibility
## Brand Commitments
## Evidence on Hand
## Open Decisions
```

This adapts Impeccable's product-context flow without requiring its CLI, live mode, or schema marker.
