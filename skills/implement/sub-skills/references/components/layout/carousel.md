---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/bricks
  based_on_version: main(fa7e1e0)
  based_on_skill: carousel
---

# Carousel

## Scope

A carousel lets users browse an ordered set within constrained space. Use it only when sequential browsing is acceptable and hidden items do not need simultaneous comparison.

## Decisions

Define item order, visible count, navigation controls, looping, autoplay policy, pagination, and fallback layout. Prefer a grid or list when users need scanning or comparison.

## Constraints

- Autoplay must be justified, pausable, and respectful of reduced motion.
- Controls need accessible names, disabled states, and predictable keyboard behavior.
- Do not trap horizontal gestures or hide essential content.
- Preserve meaningful reading order independent of visual cloning used for loops.

## Acceptance criteria

Keyboard, pointer, and touch controls work at the first and last items and after resize. Long content, reduced motion, assistive reading order, and operation without autoplay retain access to every item.
