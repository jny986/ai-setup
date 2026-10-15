---
name: page-builder
description: Build a new individual page inside an existing product or application. Use for page types such as home, product, feature, landing, pricing, tool, documentation, campaign, article, dashboard, settings, and error pages when the task includes page purpose, structure, content, components, implementation, and verification. Do not use for whole-site information architecture, site-wide navigation planning, or isolated component construction.
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on: kostja94/pagina@239cb67 (MIT)
---

# Page Builder

Build a page that belongs in the target product instead of producing a generic template.

## Start With The Product

Inspect the target route, neighboring pages, product and audience, source content, design system, reusable components, data contracts, framework, rendering model, responsive conventions, metadata, and tests.

Determine:

- the page type and the user task it must complete;
- how users arrive, what they need to understand or do, and where they continue;
- which claims, data, assets, and states are real;
- which existing components and project conventions should be reused;
- the boundary between this page and site-wide decisions.

Ask one concise question when missing information would materially change the page's responsibility, content, data, or primary action. Do not delete the affected section or replace the missing fact with generic copy.

## Load Only Relevant Guidance

Read [references/workflow.md](references/workflow.md) for construction and [references/quality-gates.md](references/quality-gates.md) before final verification. Read [references/delivery-localization.md](references/delivery-localization.md) when routes, deployments, locales, markets, or supporting data capabilities affect the page.

When a matching page guide exists in [Page Guides](#page-guides), load only that guide. If the page type is absent, use the shared workflow and do not create a permanent page guide unless repository maintenance is part of the task.

Use the page's product contexts to adapt priorities without inventing a new page identity. Each page guide links its recommended components to the component guides under [../components](../components/GUIDE.md). Reuse components already present in the target project first; use the component guides only when a required component must be created.

## Build

1. Define the page contract: purpose, audience, primary task, required truth, inputs, outputs, and exclusions.
2. Establish information hierarchy and content before selecting visual composition.
3. Reuse the target project's components, tokens, layouts, icons, content models, and routing conventions.
4. Implement real states, responsive behavior, accessibility, metadata, and failure handling.
5. Report durable user-confirmed facts and agent-discovered candidates without creating a parallel context system.
6. Verify the page in its actual route and product context.

## Boundaries

- The page guides own one page at a time, including its content structure and component composition.
- Build only new pages. Do not use this skill to audit, optimize, patch, or reconstruct an existing page.
- Page references express durable decisions and acceptance criteria, not fixed visual templates.
- Reusable component behavior belongs in the target design system or a [component guide](../components/GUIDE.md).
- Site maps, global navigation, URL architecture, cross-page journeys, and complete website planning remain outside this skill.
- Do not invent product claims, customer evidence, prices, legal terms, or operational capabilities.
- Do not replace an established stack or design system without a concrete requirement.

## Completion

Report the page created, the existing conventions and components reused, the route and states verified, durable context updates or candidates, and any material dependency or product decision that remains.

## Page Guides

**Brand:**

- [About Page](brand/about/GUIDE.md)
- [Community Pages](brand/community/GUIDE.md)
- [Contact Page](brand/contact/GUIDE.md)
- [Homepage](brand/home/GUIDE.md)
- [Portfolio Pages](brand/portfolio/GUIDE.md)

**Content:**

- [Article Page](content/article/GUIDE.md)
- [Blog Index](content/blog/GUIDE.md)
- [Collection Page](content/collection/GUIDE.md)
- [Detail Page](content/detail/GUIDE.md)
- [Documentation And Glossary Pages](content/documentation/GUIDE.md)
- [FAQ Page](content/faq/GUIDE.md)
- [Product And Capability Pages](content/features/GUIDE.md)
- [Learning Pages](content/learning/GUIDE.md)
- [Product Interface Pages](content/product-interface/GUIDE.md)
- [Publication And News Pages](content/publication/GUIDE.md)
- [Resource Pages](content/resources/GUIDE.md)
- [Template Pages](content/template-page/GUIDE.md)
- [Tool Pages](content/tools/GUIDE.md)

**Legal:**

- [Legal Policy Page](legal/legal-policy/GUIDE.md)
- [Trust, Security, And Compliance Pages](legal/trust-security-compliance/GUIDE.md)

**Marketing:**

- [Comparison Page](marketing/alternatives/GUIDE.md)
- [Commerce Pages](marketing/commerce/GUIDE.md)
- [Campaign Pages](marketing/contest/GUIDE.md)
- [Case Study Pages](marketing/customer-stories/GUIDE.md)
- [Integration, Plugin And Connector Pages](marketing/integrations/GUIDE.md)
- [Landing Page](marketing/landing-page/GUIDE.md)
- [Marketplace And Directory Pages](marketing/marketplace-directory/GUIDE.md)
- [Migration Pages](marketing/migration/GUIDE.md)
- [Press And Media Pages](marketing/press/GUIDE.md)
- [Pricing Page](marketing/pricing/GUIDE.md)
- [Program Pages](marketing/program/GUIDE.md)
- [Service And Solution Pages](marketing/service-solution/GUIDE.md)
- [Showcase Pages](marketing/showcase/GUIDE.md)
- [Use Case Pages](marketing/use-cases/GUIDE.md)

**Utility:**

- [404 Page](utility/404/GUIDE.md)
- [Careers Pages](utility/careers/GUIDE.md)
- [Changelog Pages](utility/changelog/GUIDE.md)
- [Create And Edit Page](utility/create-edit/GUIDE.md)
- [Dashboard](utility/dashboard/GUIDE.md)
- [Feedback And Disclosure Pages](utility/feedback-disclosure/GUIDE.md)
- [Roadmap Page](utility/roadmap/GUIDE.md)
- [Settings Page](utility/settings/GUIDE.md)
- [Authentication Page](utility/signup-login/GUIDE.md)
- [Status Page](utility/status/GUIDE.md)
