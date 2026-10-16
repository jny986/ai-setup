# Page versus component

| Boundary | Page | Component |
|---|---|---|
| Deliverable | One route with a page-level user task | One interface object or bounded composition |
| Ownership | Content hierarchy, metadata, routing, page states, and continuation | Local inputs, outputs, behavior, state, and semantics |
| Typical scope | Homepage, pricing, article, dashboard, settings, or 404 | Task input, article layout, navigation, or an editor workspace |
| Composition | Coordinates sections around one primary task | Coordinates child primitives without owning the complete page |

A large component can remain bounded; visual size alone does not establish page ownership. Page references link their component candidates, while the component references own each child's behavior.

Page construction and changes follow [page](../../../page.md) and the [page catalog](../../pages.md). Component construction and changes follow [component](../../../component.md). Requested audits or visual direction use the `design` router; its findings can feed the implementation workflow.
