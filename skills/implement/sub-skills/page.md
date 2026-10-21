---
name: page
description: Build or change a page and verify its page-level contract.
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: kostja94/pagina
  based_on_version: main(239cb67)
  based_on_skill: page-builder
---

Build or change a page within the coordinating workflow's requirements. For an existing page, preserve its established responsibilities outside the requested change; the page contract defines coverage, not a requirement to replace the page.

## Steps

1. **Contract.** Reuse the supplied requirements and context; inspect the route, neighboring pages, real content and data sources, existing components, and delivery model to fill remaining gaps. Resolve each applicable field in the [page contract](references/pages/references/contract.md). Ask for missing facts when they block the page's primary task or truthful content.
2. **References.** Reuse a supplied type/reference; otherwise select the page type from the [catalog](references/pages.md), or use the shared contract when no type matches. Read [delivery and localization](references/pages/references/delivery-localization.md) when origins, deployments, locales, or markets affect the route. For a reference with several modes, select the mode matching this page. Keep the reference set limited to the page's actual responsibilities.
3. **Build.** Establish content hierarchy, then implement through the project's layout, tokens, routing, data, and metadata conventions. Reuse existing components; follow [component](component.md) when a child component needs construction or a behavior change. Supporting capability stays within the page-local boundary in the page contract.
4. **Verify.** For a targeted change, select cases affected by the change and its dependencies; for a new surface, cover all supported behavior. Exercise the actual route, every applicable case in the selected page reference, and the [page quality gates](references/pages/references/quality-gates.md). Run relevant project checks and inspect screenshots for visually significant changes. Resolve failures introduced by the change; report pre-existing failures and unavailable checks with their effect on confidence.
5. **Report.** Return the route changed, requirements satisfied, behavior verified, remaining dependencies, and durable product facts discovered to the coordinator. Maintained code and project documents remain authoritative; record durable decisions through the project's existing documentation workflow.
