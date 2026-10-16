# Settings Page

## Scope

A settings page changes preferences, integrations, identity-adjacent configuration, and product behavior whose effects persist beyond the current task. It is not an object editor, dashboard, or dumping ground for unrelated administration.

## Contract

Define setting ownership, scope, defaults, dependencies, permissions, save behavior, propagation delay, reversibility, audit requirements, and destructive or security-sensitive actions.

## Content

- **Core:** navigable setting groups, current values, clear save or immediate-apply behavior.
- **Common:** account or workspace scope, integrations, notifications, appearance, data controls.
- **Conditional:** API keys, members and roles, security, domains, import/export, danger zone.

## Product Adaptation

Developer tools emphasize credentials, environments, webhooks, and integrations. Collaboration products emphasize members, roles, notifications, and workspace policy. Analytics products emphasize data sources, attribution, retention, and reporting defaults. Simple products should not expose empty categories merely to resemble enterprise software.

## Composition

Configuration groups follow task and scope; promotional regions interfere with repeated configuration work.

## Component candidates

- **Primary candidates:** [Navigation Menu](../../components/navigation/navigation-menu.md)
- **Common:** [Sidebar](../../components/navigation/sidebar.md), [Tabs](../../components/content/tabs.md), [Accordion](../../components/content/accordion.md)
- **Conditional:** [Modal](../../components/conversion/popup.md), [Announcement Banner](../../components/utility/top-banner.md)
- **Discouraged:** [Hero](../../components/branding/hero.md), [Carousel](../../components/layout/carousel.md), [Testimonials](../../components/conversion/testimonials.md)

## Acceptance coverage

Permissions, inherited and overridden values, immediate and deferred saves, server errors, secrets, reauthentication, destructive confirmation, keyboard navigation, deep links, long labels, responsive grouping, audit events, and whether changes take effect where promised.
