# Delivery and localization

A page operates within the product's chosen delivery topology and release scope. Site-wide architecture remains a project-level decision.

## Delivery topology

| Dimension | Values to resolve |
|---|---|
| Surface | Marketing, app, dashboard, docs, status, community, developer, or human-facing API entry |
| Placement | Path, subdomain, or separate origin |
| Ownership | First-party application, separate first-party deployment, or an explicitly selected third-party service |

Machine API endpoints are supporting capability rather than pages. A subdomain alone does not establish third-party ownership. First-party construction is the default; adopting an external operational service requires the user's choice.

## Cross-origin contract

Canonical origin, base and asset paths, authentication, cookies, analytics, consent, internal links, return paths, sitemap ownership, and visual chrome must agree across the deployments the page spans.

Supporting handlers and adapters follow the [page-local capability boundary](contract.md#supporting-capability). A missing operational system remains an explicit dependency.

## Locale and market

| Concept | Ownership |
|---|---|
| Language | Content language |
| Locale | Language and presentation formats |
| Market | Price, plans, tax, availability, legal text, and fulfillment where they differ |

The project's existing path, subdomain, or domain model determines locale routing. Published switcher links and `hreflang` entries target available pages in the current release. Another market's price, terms, or availability cannot stand in for missing commercial data.

Shared page behavior and components support localized copy and market-owned data. Acceptance includes translated metadata and social previews, structured data, dates, numbers, currencies, units, text expansion, line breaking, and corresponding-locale navigation for every released locale and market.
