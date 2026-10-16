# Collection Page

## Scope

A collection page lets users find, filter, sort, compare, select, and act on many objects of the same domain. It is not merely a visual list and should not absorb the responsibilities of an individual object's detail page.

## Contract

Define object identity, visible fields, default ordering, filters, search, pagination or virtualization, selection, bulk actions, saved views, permissions, and empty or error behavior.

## Content

- **Core:** collection identity, discovery controls, object results.
- **Common:** filters, sort, count, create action, pagination, selection.
- **Conditional:** bulk actions, saved views, import/export, alternate list/grid views, summaries.

## Product Adaptation

CRM collections emphasize ownership, stage, recency, and bulk updates. CMS collections emphasize status, author, publication dates, and review. Ecommerce collections emphasize inventory, price, variants, and fulfillment. Marketplaces may prioritize media and comparison over dense operational columns.

## Composition

A proven data-grid library is appropriate when selection, virtualization, pinning, resizing, or complex keyboard interaction is required.

## Component candidates

- **Primary candidates:** [List](../../components/layout/list.md)
- **Common:** [Grid](../../components/layout/grid.md), [Card](../../components/layout/card.md), [Sidebar](../../components/navigation/sidebar.md)
- **Conditional:** [Tabs](../../components/content/tabs.md), [Accordion](../../components/content/accordion.md), [Announcement Banner](../../components/utility/top-banner.md)
- **Discouraged:** [Hero](../../components/branding/hero.md)

## Acceptance coverage

Large and empty datasets, loading and errors, query persistence, deep links, long values, permissions, bulk actions, destructive confirmation, keyboard use, responsive alternatives, pagination, and return-state restoration from detail pages.
