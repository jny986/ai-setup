---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/bricks
  based_on_version: main(fa7e1e0)
  based_on_skill: table-of-contents
---

# Table Of Contents

## Scope

A table of contents exposes the structure of a long document or page and links to meaningful sections. It helps orientation; it does not replace a coherent heading hierarchy.

## Decisions

Choose included heading levels, label shortening policy, active-section behavior, sticky placement, collapse behavior, and whether the page is long enough to benefit.

## Constraints

- Generate links from stable unique IDs and valid heading order.
- Do not include every minor heading when it harms scanning.
- Account for fixed headers when scrolling to anchors.
- Active-section tracking must not create constant noisy updates for assistive technology.

## Acceptance criteria

Every anchor targets a unique heading and works with keyboard and history navigation. Duplicate headings, fixed headers, sticky boundaries, mobile collapse, reduced motion, and short or long outlines retain orientation.
