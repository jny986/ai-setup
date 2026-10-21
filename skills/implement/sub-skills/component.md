---
name: component
description: Build or change a component or bounded composition in its host interface.
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: kostja94/bricks
  based_on_version: main(fa7e1e0)
  based_on_skill: component-builder
---

Build or change a component or bounded composition within the coordinating workflow's requirements. Page-level hierarchy, routing, and metadata belong to [page](page.md). Existing component contracts remain authoritative outside the requested change.

## Steps

1. **Contract.** Reuse the supplied requirements and context; inspect the host page, nearby components, data model, design system, and stack to fill remaining gaps. Resolve responsibility, ownership, inputs, outputs, and reachable states using the [component contract](references/components/references/contract.md). Ask when missing facts change responsibility or data behavior.
2. **References.** Reuse a supplied type/reference; otherwise select the concept from the [catalog](references/components.md), or use the shared contract for an uncatalogued concept. Read [foundational controls](references/components/references/foundational-controls.md) for inputs and actions. When the boundary is unclear, use [page versus component](references/components/references/pagina.md).
3. **Build.** Choose the variant from content, placement, and interaction needs. Reuse project primitives, tokens, icons, state ownership, and data access. Integrate the component where users encounter it; a separate showcase suffices only when the project is itself a component library.
4. **Verify.** For a targeted change, select cases affected by the change and its dependencies; for a new surface, cover all supported behavior. Exercise every applicable acceptance case in the selected reference and the [component quality gates](references/components/references/quality-gates.md) in the host page. Run relevant project checks and inspect screenshots for visually significant changes. Resolve failures introduced by the change; report pre-existing failures and unavailable checks with their effect on confidence.
5. **Report.** Return requirements satisfied, integration and verification results, and remaining constraints to the coordinator. For an uncatalogued component, name the inferred concept; add a permanent reference only when repository maintenance is part of the task.
