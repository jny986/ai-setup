---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/bricks
  based_on_version: main(fa7e1e0)
  based_on_skill: post-collection
---

# Post Collection

## Scope

A post collection presents a bounded set of publication entries for scanning and discovery. It can be used inside a blog index, topic page, author page, resource page, or related-content region; it does not own the complete page.

## Composition

Use the host project's card, list, grid, pagination, filter, and metadata components. Choose chronological, curated, taxonomy-led, or search-led ordering from the parent context and real content model.

## Constraints

- Preserve stable entry links and expose only metadata that helps selection.
- Handle long titles, absent media, sparse results, no results, and large collections.
- Keep filtering, pagination, canonical behavior, and indexability aligned with the parent page.
- Do not create alternate versions of every child component.

## Acceptance criteria

Each rendered entry has a valid destination and a coherent scanning and keyboard order. Narrow layouts, missing fields, loading, empty or error results, and filtering or pagination preserve discovery.
