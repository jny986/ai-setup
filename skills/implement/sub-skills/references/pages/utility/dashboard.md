# Dashboard

## Scope

A dashboard summarizes current state, exposes priorities and exceptions, and routes users into detailed work. It is not a decorative collection of metrics or a substitute for a sustained analytics, operations, or editing workspace.

## Contract

Define the decisions users make from this page, the freshness and ownership of each signal, actionable exceptions, next tasks, permissions, and destination pages. Every metric needs a stable meaning and time context.

## Content

- **Core:** current state; priorities or exceptions; next actions.
- **Common:** recent activity, progress, saved views, guidance.
- **Conditional:** onboarding, alerts, usage, plan state, team activity, upgrade notice.

## Product Adaptation

SaaS may emphasize activation, usage, account health, and recent work. Analytics products emphasize selected metrics and trends but should route deep analysis to an analytics workspace. Ecommerce emphasizes orders, inventory, fulfillment, and revenue exceptions. AI tools emphasize task entry, running jobs, recent outputs, and credits.

## Composition

Compact hierarchy and stable dimensions support repeated use.

## Component candidates

- **Primary candidates:** [Grid](../../components/layout/grid.md)
- **Common:** [Card](../../components/layout/card.md), [Sidebar](../../components/navigation/sidebar.md), [Navigation Menu](../../components/navigation/navigation-menu.md)
- **Conditional:** [Announcement Banner](../../components/utility/top-banner.md), [List](../../components/layout/list.md), [Comparison Table](../../components/content/comparison-table.md)
- **Discouraged:** [Hero](../../components/branding/hero.md), [Carousel](../../components/layout/carousel.md)

## Acceptance coverage

Fresh, stale, loading, empty, partial, error, and permission-restricted data; metric definitions; time zones; alerts; keyboard navigation; responsive layout; drill-down links; and whether users can identify the next action without scanning every panel.
