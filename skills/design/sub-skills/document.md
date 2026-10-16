---
name: document
description: "Create or update a project's root DESIGN.md from its implemented UI or an approved pre-implementation direction."
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: pbakaus/impeccable
  based_on_version: main(2f98774)
  based_on_skill: document
---

# Document the visual system

Create or update project-root `DESIGN.md`, the authoritative record of applied UI tokens and reusable visual rules. Use the [DESIGN.md format](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md): optional YAML token frontmatter, followed by the canonical sections below in order. Tokens are normative; prose explains where and why to use them. Keep the file useful without Impeccable's CLI or `.impeccable/design.json` sidecar.

## Workflow

1. **Identify the source.** Read an existing `DESIGN.md`, `PRODUCT.md`, the brand kit in the project reference directory, and relevant code. If `.agents/design-context.md` exists, import its decisions as evidence and resolve conflicts against current code and approved brand guidance. See [design-context](references/design-context.md) for discovery and migration.
2. **Choose the path.** With an implemented UI, scan its tokens, theme files, global styles, common components, and representative rendered screens where available. With no implemented system, document only an approved direction as a seed. If neither evidence nor a chosen direction exists, resolve that gap before assigning visual values.
3. **Draft or update `DESIGN.md`.** In scan mode, record reused tokens and observed component behavior, citing source paths where useful. In seed mode, record durable direction and mark unresolved values; omit unimplemented components and token frontmatter beyond established values. Preserve existing decisions outside the task scope. When existing documentation conflicts with implementation, determine whether the code drifted or the document is stale before changing either.
4. **Reconcile.** Match approved brand primitives to the brand kit; explain intentional UI adaptations. Keep product facts in `PRODUCT.md`. Check frontmatter syntax, token references, component descriptions, and representative rendered states against the implementation. Report decisions still awaiting approval and any mismatch left unresolved.

Completion: the document distinguishes implemented facts from proposed direction, its token values agree with the chosen source, and it gives a future designer enough guidance to apply the same system.

## Document shape

Include only sections that have useful content, in this order:

1. `## Overview` — visual thesis and durable principles.
2. `## Colors` — roles, combinations, and contrast behavior.
3. `## Typography` — families, hierarchy, sizing, and usage.
4. `## Layout` — spacing, grids, containers, and responsive behavior.
5. `## Elevation & Depth` — borders, shadows, and layering.
6. `## Shapes` — radius, geometry, and clipping.
7. `## Components` — recurring variants and interaction states.
8. `## Do's and Don'ts` — concrete system rules.

Frontmatter may contain established `colors`, `typography`, `rounded`, `spacing`, and `components` tokens. Follow the linked format for token keys and `{path.to.token}` references. For example, `backgroundColor: "{colors.primary}"` can refer to an established `colors.primary` token. Preserve the project's normative color notation rather than converting values solely for this file. Put motion, breakpoints, and other guidance in the relevant prose sections when the frontmatter schema cannot represent them. In seed mode, label the file as a pre-implementation direction and leave unknown values out of the token frontmatter.

This adapts Impeccable's documentation flow; its sidecar and live-panel instructions apply only to Impeccable's runtime.
