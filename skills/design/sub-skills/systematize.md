---
name: systematize
description: "Consolidate repeated UI patterns into shared tokens, components, and variants; migrate existing uses and verify visual and behavioral parity."
license: Apache-2.0
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: pbakaus/impeccable
  based_on_version: main(2f98774)
  based_on_skill: extract
---

# Systematize an interface

Extract shared UI behavior and visual rules from an implemented interface. [Design-system](references/design-system.md) supplies token and component architecture; [document](document.md) records the resulting system. This workflow changes code and migrates consumers.

## Workflow

1. **Find the existing system.** Read `DESIGN.md`, relevant brand guidance, theme files, shared components, their consumers, and any component catalog. Use [design-context](references/design-context.md) for discovery. Establish naming, exports, styling, state ownership, and accessibility conventions. Finish with a target area and the existing home for shared patterns, or a proposed location consistent with the repository.
2. **Identify meaningful repetition.** Compare repeated markup, interactions, type roles, spacing, colors, and motion. Group by intent and behavior as well as appearance. Distinguish accidental drift from legitimate variation. Choose candidates whose consolidation reduces maintenance or fixes a repeated defect; keep isolated patterns local when sharing adds more configuration than it removes. Finish with actual consumers, intended variants, and the benefit of each extraction.
3. **Define the migration.** Choose the authoritative behavior and appearance from approved guidance and current uses. Resolve consequential differences before unifying them. Specify the component boundary, minimal API, token roles, consumers to change, and expected parity. Preserve useful domain distinctions. Finish when every selected consumer maps to a supported variant or an explicitly retained local implementation.
4. **Extract and migrate.** Build in the project's existing system, reuse its dependencies, and move shared behavior with its accessible semantics and interaction states. Introduce semantic tokens for stable roles; preserve deliberate exceptions. Migrate the scoped consumers and remove their superseded code once references are gone. Finish when those consumers use the shared implementation and the public API covers their real requirements.
5. **Verify parity.** Compare representative before/after renders, themes, responsive layouts, content extremes, keyboard or native input, and relevant states. Exercise every changed behavior and run the project's applicable checks; use meaningful behavioral regressions for interaction changes. Inspect consumers outside the migration scope when shared dependencies changed. Finish when each migrated variant has evidence of parity or an intentional, authorized difference.
6. **Record the system.** Update the existing component catalog or usage documentation and use [document](document.md) for changed durable tokens and rules. Report migrated uses, intentional exceptions, and verification limits. Completion requires both the reusable implementation and its scoped migration; a new unused component alone is incomplete.

Prefer composition and domain-specific variants over an API that exposes every style property. Repetition is evidence to investigate, not a numerical threshold for extraction. Record genuine behavior or identity changes separately from consolidation so parity can be assessed.
