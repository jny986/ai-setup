---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/bricks
  based_on_version: main(fa7e1e0)
  based_on_skill: sidebar
---

# Sidebar

## Scope

A sidebar contains secondary navigation, filtering, context, or tools adjacent to a primary work area. It should improve repeated access without stealing space from the main task.

## Decisions

Define purpose, persistence, width, collapse behavior, mobile replacement, active state, scroll ownership, and whether content belongs globally or only to the current section.

## Constraints

- Collapsed states need recognizable controls and accessible names.
- On narrow screens, use an intentional drawer, sheet, or separate view rather than squeezing both regions.
- Avoid multiple competing vertical scroll containers.
- Keep critical content available when the sidebar is hidden.

## Acceptance criteria

Expanded/collapsed states, long labels, independent scrolling, mobile dismissal, and persistence across routes follow the contract. Keyboard navigation and focus restoration preserve access when the primary work area changes.
