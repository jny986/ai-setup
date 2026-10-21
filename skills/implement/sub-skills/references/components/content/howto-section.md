---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/bricks
  based_on_version: main(fa7e1e0)
  based_on_skill: howto-section
---

# How-to Section

## Scope

A how-to section presents an ordered procedure that a user can complete. It belongs inside a page when the procedure supports that page's primary subject.

## Decisions

Define the starting condition, required materials or permissions, ordered steps, expected result, and recovery points. Use an ordered list when sequence matters; add media only where it clarifies an action.

## Constraints

- Each step should contain one primary action and an observable result.
- Do not omit prerequisites, destructive consequences, or required waiting states.
- Keep structured data aligned with visible steps when the project has a concrete consumer for it.
- Do not manufacture steps to target search terms.

## Acceptance criteria

The visible procedure can reach its stated final condition from its stated prerequisites. Numbering, anchors, narrow layouts, and media alternatives preserve the order and observable results.
