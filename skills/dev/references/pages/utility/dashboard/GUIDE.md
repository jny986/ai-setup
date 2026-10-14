# Dashboard

## Responsibility

A dashboard summarizes current state, exposes priorities and exceptions, and routes users into detailed work. It is not a decorative collection of metrics or a substitute for a sustained analytics, operations, or editing workspace.

## Page Contract

Define the decisions users make from this page, the freshness and ownership of each signal, actionable exceptions, next tasks, permissions, and destination pages. Every metric needs a stable meaning and time context.

## Sections

- **Core:** current state; priorities or exceptions; next actions.
- **Common:** recent activity, progress, saved views, guidance.
- **Conditional:** onboarding, alerts, usage, plan state, team activity, upgrade notice.

## Product Adaptation

SaaS may emphasize activation, usage, account health, and recent work. Analytics products emphasize selected metrics and trends but should route deep analysis to an analytics workspace. Ecommerce emphasizes orders, inventory, fulfillment, and revenue exceptions. AI tools emphasize task entry, running jobs, recent outputs, and credits.

## Components

Grid, Card, List, Sidebar, Navigation, and Announcement Banner are candidates. Compact hierarchy and stable dimensions matter more than marketing-style presentation; Hero and Carousel are generally poor fits.

## Verify

Test fresh, stale, loading, empty, partial, error, and permission-restricted data; metric definitions; time zones; alerts; keyboard navigation; responsive layout; drill-down links; and whether users can identify the next action without scanning every panel.

## Bricks Components

Catalog recommendations; links go to the component guides in this tree.

- **Core:** [Grid](../../../components/layout/grid/GUIDE.md)
- **Common:** [Card](../../../components/layout/card/GUIDE.md), [Sidebar](../../../components/navigation/sidebar/GUIDE.md), [Navigation Menu](../../../components/navigation/navigation-menu/GUIDE.md)
- **Conditional:** [Announcement Banner](../../../components/utility/top-banner/GUIDE.md), [List](../../../components/layout/list/GUIDE.md), [Comparison Table](../../../components/content/comparison-table/GUIDE.md)
- **Discouraged:** [Hero](../../../components/branding/hero/GUIDE.md), [Carousel](../../../components/layout/carousel/GUIDE.md)
