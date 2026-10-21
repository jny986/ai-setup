---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/bricks
  based_on_version: main(fa7e1e0)
  based_on_skill: comparison-table
---

# Comparison Table

## Scope

A comparison table helps users evaluate alternatives against shared criteria. It must make differences inspectable without turning nuanced claims into unsupported checkmarks.

## Decisions

Define the compared entities, decision criteria, evidence source, priority order, and mobile presentation before choosing a table, cards, or hybrid layout. Keep the same criteria across columns.

## Constraints

- Use factual, current, and consistently scoped claims.
- Explain partial support, limits, and plan-dependent features.
- Preserve row and column associations for assistive technology.
- On narrow screens, prefer meaningful reflow or controlled horizontal scrolling over unreadable compression.

## Acceptance criteria

Claims have attributable sources and comparable scope. Long labels, narrow-screen comparison, sticky headers where used, keyboard access, and row/column associations preserve the same criteria; recommendation styling does not conceal differences.
