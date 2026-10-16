# Card

## Scope

A card groups a bounded object, choice, or summary whose contents belong together. It should clarify repeated information, not turn every section into a floating container.

## Decisions

Define the represented object, hierarchy, action model, selection state, media behavior, and whether the entire card or only explicit controls are interactive.

## Constraints

- Click targets remain distinct; a whole-card link cannot contain competing interactive controls.
- Keep repeated cards structurally comparable without forcing equal content length.
- Use semantic elements that match the content and action.
- Do not use cards merely to decorate unrelated page sections.

## Acceptance criteria

Long titles, absent media, responsive grids, and repeated actions preserve hierarchy. Keyboard order, hover/focus treatment, selected or disabled states, and whole-card links have unambiguous targets.
