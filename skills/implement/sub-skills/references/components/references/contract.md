---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/bricks
  based_on_version: main(fa7e1e0)
  based_on_skill: component-builder
---

# Component contract

A component owns a bounded interface responsibility within its host page. Role, placement, visual variant, and runtime state usually vary one concept rather than create separate component identities. Independent terminology and interaction contracts can justify separate references, as with Grid, List, and Masonry.

## Contract fields

| Concern | Required decision |
|---|---|
| Responsibility | User task, semantic boundary, host surface, and exclusions |
| Data | Authoritative inputs, outputs, content source, and data/error ownership |
| State | Reachable transitions, pending and failure behavior, recovery, and permissions |
| Interaction | Actions, navigation, keyboard behavior, focus ownership, and accessible semantics |
| Variant | Content volume, hierarchy, available space, interaction frequency, and host-page conventions |
| Integration | Existing primitives, tokens, icons, data access, file organization, and compatible dependencies |

Potential states include default, hover, focus, active, disabled, loading, empty, error, success, expanded, collapsed, and permission restricted. Only reachable states belong to the contract.

## Ownership

The host page owns page-level hierarchy, routing, and metadata. Bounded compositions may coordinate child components while each child's behavior keeps one maintained source. [Page versus component](pagina.md) distinguishes complete page construction.

Complex editors, tables, charts, calendars, accessible primitives, and agent runtimes benefit from maintained domain libraries. A dependency needs a concrete contract benefit and compatibility with the project's stack.

## Reference selection

Use the reference for the component's semantic responsibility. Visual variants and host-page placement do not require reading every neighboring reference. Page component lists are suggestions; an existing primitive may satisfy the same contract. For a targeted change, cover changed behavior and affected dependencies; for new components, cover all supported states.

## Acceptance

The component works in its host page with real data and reachable states. Its reference's acceptance cases and [shared quality gates](quality-gates.md) define the evidence needed; a static isolated preview does not establish interaction correctness.
