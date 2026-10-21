---
name: implement
description: "Implement a feature, change, spec, or ticket. Select the scope workflow, relevant project context, and page or component workflows for new or existing UI, alongside any required non-UI work. Sub-skills: ticket, spec, page, component."
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: mattpocock/skills
  based_on_version: v1.3.1(49dd158)
  based_on_skill: implement
---

Read the project’s agent instructions before resolving tracker references or changing code.

Implement the user's desired outcome. **Scope** chooses the coordinating workflow; **surface** chooses the implementation guidance used within it.

## Routing

1. **Resolve scope.** Resolve references from the request or conversation far enough to distinguish one ticket from a whole spec. An explicit `ticket` or `spec` argument selects that scope; a direct feature or change uses the implementation steps below. A linked parent spec supplies context for a ticket; completing its other tickets requires that wider scope. Ask only when unresolved scope would change what gets built.
2. **Carry surface requests.** An explicit `page`, `component`, or type name from the [name table](sub-skills/name-table.md) selects surface guidance within the resolved scope. A feature may need several pages, components, and non-UI changes.
3. **Coordinate.** For a ticket, follow [ticket](sub-skills/ticket.md); for a whole spec, follow [spec](sub-skills/spec.md), carrying the requested surfaces and fetched requirements. These workflows return scoped work to [Implementation](#implementation) below. For direct work, continue there immediately. When returning with resolved requirements, start at Implementation without repeating routing.

## Implementation

Build the complete feature or change within the resolved scope. Keep that scope through surface hand-offs.

1. **Outcome.** Read the request or supplied requirements and affected code until you can name the required behavior, current behavior, acceptance criteria, and exclusions. Keep supplied ticket or spec identifiers attached to these requirements. For an existing feature, identify behavior that must continue to work.
2. **Context.** Select the information below for the affected work. Reuse context already gathered. Resolve missing facts that block correctness; infer routine implementation choices from the project.

   | Work | Information to read |
   |---|---|
   | Any change | Relevant code, callers, data contracts, project checks, and existing tests |
   | Product behavior or domain rules | Maintained product/domain context, linked spec constraints, and relevant decisions |
   | UI work | Existing design system, tokens, layouts, and reusable components; `DESIGN.md` and relevant product/brand context where present |
   | Route, deployment, locale, or market changes | Existing routing and delivery configuration; [delivery and localization](sub-skills/references/pages/references/delivery-localization.md) |

3. **Surfaces.** Identify every page-level, component-level, and non-UI responsibility needed for the outcome. Honor an explicitly requested surface or reference type. Select guidance by responsibility:

   - **Page:** select [page](sub-skills/page.md) for route-level hierarchy, content, data, metadata, or page states, whether new or existing.
   - **Component:** select [component](sub-skills/component.md) for a bounded interface object or composition. A change confined to a component uses this workflow without a page-wide rebuild.
   - **Non-UI:** implement through the project's existing modules and contracts. Complete required server, data, permission, or integration work alongside the UI.

   For an explicit type name, resolve its reference through the [name table](sub-skills/name-table.md). Otherwise use the selected surface’s catalog. Match the user task, not a keyword: implementing a software feature does not imply building a product-feature marketing page. Reuse resolved references and read only those matching the affected responsibilities. Existing components satisfy the contract when reusable; their presence does not require constructing replacements. An uncatalogued feature uses the applicable shared contracts.
4. **Implement.** Run the selected page/component workflows once for their assigned responsibilities and implement non-UI work through the project’s established seams. Use `tdd` for behavior suited to test-first development. When visual direction, a user journey, or audit findings need design work, use the applicable `design` guidance, then continue implementation within the same requirements. Carry requirements, relevant context paths, and verification results across hand-offs instead of restarting discovery.
5. **Verify.** Account for every acceptance criterion across the affected layers. Run relevant project checks and the selected surface workflows' acceptance checks, including UI-to-server integration and preserved behavior where affected. Fix failures caused by the change. An unmet requirement or unverified dependency remains an explicit completion blocker for the coordinating workflow.
6. **Report.** State what changed, verification evidence, and remaining requirements or blockers. Distinguish checks that passed from checks unavailable in this environment. Return results to the ticket or spec coordinator when nested; a finished UI surface alone does not complete the feature.

## Sub-skills

| Sub-skill | Use when |
|---|---|
| [`ticket`](sub-skills/ticket.md) | Resolve and implement one ticket against its acceptance criteria and parent-spec constraints |
| [`spec`](sub-skills/spec.md) | Complete a spec, coordinating its ticket graph when tickets exist |
| [`page`](sub-skills/page.md) | Build or change page-level hierarchy, routing, content, data, metadata, or states |
| [`component`](sub-skills/component.md) | Build or change a bounded interface component or composition and its behavior |
