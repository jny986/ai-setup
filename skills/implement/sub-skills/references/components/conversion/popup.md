---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/bricks
  based_on_version: main(fa7e1e0)
  based_on_skill: modal
---

# Modal

## Scope

A modal interrupts the current surface for a focused decision or short task that must be resolved or dismissed before normal interaction continues. Popup, dialog, and lightbox are context-dependent names, not automatic synonyms.

## Decisions

Confirm that interruption is necessary, define the opening trigger, dismissal rules, initial focus, destructive action treatment, and return focus target. Use a non-modal surface when users need the background for context or comparison.

## Constraints

- Use a maintained dialog primitive or implement focus containment and restoration correctly.
- Provide an accessible name and a visible dismissal path unless dismissal would invalidate a required system decision.
- Escape and backdrop behavior must match consequence and data-loss risk.
- Prevent background interaction and incoherent scrolling while open.

## Acceptance criteria

Opening, keyboard traversal, Escape, backdrop interaction, nested controls, and dismissal follow the declared rules. The dialog has an accessible name, restores focus, preserves unsaved work where required, and remains usable with mobile viewports and virtual keyboards.
