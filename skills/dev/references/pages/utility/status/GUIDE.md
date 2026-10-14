# Status Page

## Responsibility

A Status page communicates current service health, affected components, incidents, maintenance, and history from a real operational source. It must never use static green indicators to imply live availability.

## Sections

- **Core:** overall state, service components, active incidents, last update.
- **Common:** incident history, maintenance, timestamps, subscription or contact path.
- **Conditional:** regions, dependencies, uptime history, postmortems, authenticated detail.

Build first-party by default and consume existing monitoring or incident data. A page-local adapter is allowed; a complete monitoring and notification platform is not silently created.

## Components And Verification

Announcement Banner, List, Card, Tabs, and Navigation may apply. Verify stale and unavailable data, partial outage, maintenance, time zones, refresh behavior, accessible non-color status, canonical origin, subscription truth, and failure of the status source itself.

## Components

Catalog recommendations; links go to the component guides in this tree.

- **Common:** [Announcement Banner](../../../components/utility/top-banner/GUIDE.md), [List](../../../components/layout/list/GUIDE.md)
- **Conditional:** [Card](../../../components/layout/card/GUIDE.md), [Tabs](../../../components/content/tabs/GUIDE.md), [Accordion](../../../components/content/accordion/GUIDE.md), [Navigation Menu](../../../components/navigation/navigation-menu/GUIDE.md)
