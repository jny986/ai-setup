---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/pagina
  based_on_version: main(239cb67)
  based_on_skill: status
---

# Status Page

## Scope

A Status page communicates current service health, affected components, incidents, maintenance, and history from a real operational source. It must never use static green indicators to imply live availability.

## Content

- **Core:** overall state, service components, active incidents, last update.
- **Common:** incident history, maintenance, timestamps, subscription or contact path.
- **Conditional:** regions, dependencies, uptime history, postmortems, authenticated detail.

Build first-party by default and consume existing monitoring or incident data. A page-local adapter is allowed; a complete monitoring and notification platform is not silently created.

## Component candidates

- **Common:** [Announcement Banner](../../components/utility/top-banner.md), [List](../../components/layout/list.md)
- **Conditional:** [Card](../../components/layout/card.md), [Tabs](../../components/content/tabs.md), [Accordion](../../components/content/accordion.md), [Navigation Menu](../../components/navigation/navigation-menu.md)

## Acceptance coverage

Stale and unavailable data, partial outage, maintenance, time zones, refresh behavior, accessible non-color status, canonical origin, subscription truth, and failure of the status source itself.
