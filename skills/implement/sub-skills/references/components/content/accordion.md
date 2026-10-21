---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/bricks
  based_on_version: main(fa7e1e0)
  based_on_skill: accordion
---

# Accordion

## Scope

An accordion expands and collapses independently named content sections in a vertical flow. It preserves heading-level scanning while allowing secondary detail to remain compact.

## Constraints

- Use buttons with explicit expanded state and correctly associated panels.
- Decide whether one or multiple sections may be open.
- Disclosure is justified when scanning section titles before opening details serves the task; primary task content remains directly available.

## Acceptance criteria

Keyboard activation updates the associated panel and expanded state. Focus, heading hierarchy, long or dynamically updated content, narrow screens, and print output where supported remain coherent.
