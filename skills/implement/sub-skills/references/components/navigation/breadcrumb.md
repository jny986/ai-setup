# Breadcrumb

## Scope

A breadcrumb shows the current page's position in a meaningful hierarchy and provides navigation to ancestors. It is not a history trail.

## Decisions

Derive items from stable information architecture, not arbitrary URL segments. Decide whether the current page is text or a link and how long labels collapse on small screens.

## Constraints

- Use navigation semantics with an accessible label and an ordered list.
- Separators should not be announced as item content.
- Do not invent ancestors that have no useful destination.
- Visible breadcrumb and any structured data must describe the same hierarchy.

## Acceptance criteria

Ancestor destinations and current-page state match the real hierarchy. Deep paths, long labels, mobile truncation, keyboard links, and any structured data retain that meaning.
