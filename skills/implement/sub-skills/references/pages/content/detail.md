# Detail Page

## Scope

A detail page presents one domain object, its current state, related information, and context-appropriate actions. It is distinct from the collection used to find the object and from the dedicated editor used to make substantial changes.

## Contract

Define object identity, authoritative fields, status, ownership, relationships, activity, permissions, available actions, edit path, deletion behavior, and return destination.

## Content

- **Core:** identity, status, primary information, contextual actions.
- **Common:** related records, activity, metadata, ownership, navigation back to the collection.
- **Conditional:** tabs, side panel, audit history, comments, attachments, destructive actions.

## Product Adaptation

CRM details emphasize relationship history and next actions. Ecommerce details in an admin context emphasize variants, inventory, pricing, and fulfillment. Operations products emphasize live state, events, ownership, and intervention. CMS details may be read-only review surfaces leading to an editor.

## Composition

Object identity uses a compact header; a marketing hero would displace repeated operational work.

## Component candidates

- **Primary candidates:** [Breadcrumb](../../components/navigation/breadcrumb.md)
- **Common:** [Tabs](../../components/content/tabs.md), [Accordion](../../components/content/accordion.md), [Sidebar](../../components/navigation/sidebar.md), [Card](../../components/layout/card.md)
- **Conditional:** [Modal](../../components/conversion/popup.md), [Announcement Banner](../../components/utility/top-banner.md), [List](../../components/layout/list.md)
- **Discouraged:** [Hero](../../components/branding/hero.md), [Carousel](../../components/layout/carousel.md)

## Acceptance coverage

Missing or deleted objects, stale data, permissions, long values, related-record failures, deep links to sections or tabs, actions and confirmations, unsaved transitions, keyboard operation, responsive hierarchy, and return navigation.
