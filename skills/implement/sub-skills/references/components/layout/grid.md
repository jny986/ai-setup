---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/bricks
  based_on_version: main(fa7e1e0)
  based_on_skill: grid
---

# Grid

## Scope

A grid arranges peer items across rows and columns for scanning or comparison. Visual grid layout does not automatically require ARIA grid interaction.

## Decisions

Choose column behavior, minimum item width, alignment, ordering, density, and whether items remain peers at every breakpoint. Use semantic lists or ordinary containers unless spreadsheet-like keyboard navigation is actually required.

## Constraints

- Preserve source order and reading order.
- Tracks must accommodate content at supported widths and zoom levels.
- Let long content reflow rather than overlap adjacent cells.
- Do not force equal heights when doing so creates empty or misleading space.

## Acceptance criteria

Minimum and maximum widths, longest content, missing items, zoom, and localization preserve readable tracks. Keyboard and source order remain coherent across column-count changes.
