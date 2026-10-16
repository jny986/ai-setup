# Tabs

## Scope

Tabs switch among a small, stable set of peer panels within one context. They are not navigation by default and are not a compact substitute for ordinary headings.

## Constraints

- Implement the tablist keyboard and focus model or reuse a maintained accessible primitive.
- Keep labels short enough to remain usable on narrow screens.
- Do not hide critical safety, pricing, or task information by default.
- Use links instead when selecting an item changes the route and represents navigation.

## Acceptance criteria

Arrow keys, focus, selected state, and panel associations agree. Long labels, changing panel height, mobile overflow, and supported direct links preserve access to every panel.
