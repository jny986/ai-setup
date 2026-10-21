---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/bricks
  based_on_version: main(fa7e1e0)
  based_on_skill: list
---

# List

## Scope

A list presents related items in a linear order. It is the default repeated-content pattern when sequence, scanning, or narrow layouts matter more than two-dimensional comparison.

## Decisions

Define ordering, item identity, density, dividers, metadata, actions, selection, pagination or virtualization, and empty behavior. Use ordered semantics only when order carries meaning.

## Constraints

- Keep item actions distinguishable from item navigation.
- Preserve stable keys and selection across data updates.
- Virtualize only when scale justifies the accessibility and state complexity.
- Do not encode important hierarchy through indentation alone.

## Acceptance criteria

Empty and large datasets, long labels, loading more items, and responsive metadata preserve scanning and action access. Selection and keyboard actions survive updates; screen-reader item counts are accurate where exposed.
