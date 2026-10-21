---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/pagina
  based_on_version: main(239cb67)
  based_on_skill: pricing
---

# Pricing Page

## Scope

A pricing page helps a qualified visitor understand how the product is charged, compare meaningful options, estimate commitment, and choose a next step. It does not decide the company's pricing strategy or conceal material limitations behind decorative comparison UI.

## Contract

Use the approved plans, currencies, billing periods, limits, taxes, trials, refund terms, and enterprise path. Price, entitlement, and checkout data must agree with the product and billing system.

## Content

- **Core:** pricing model explanation, purchasable options, meaningful differences, next action.
- **Common:** billing toggle, limits and inclusions, FAQ, enterprise or contact path, trust.
- **Conditional:** usage calculator, regional pricing, add-ons, overages, nonprofit or startup programs.

## Product Adaptation

SaaS commonly compares subscriptions; AI tools often require credits, generation limits, or model access; developer tools may price by seats, requests, or infrastructure usage. Ecommerce usually exposes prices on products rather than creating a standalone pricing page.

## Composition

Dense detail needs accessible disclosure and a mobile comparison that retains decisive differences. Candidate components do not prescribe source-code boundaries.

## Component candidates

- **Primary candidates:** [Comparison Table](../../components/content/comparison-table.md), [Call to Action Section](../../components/conversion/cta.md)
- **Common:** [FAQ Section](../../components/content/faq-section.md), [Trust Signals](../../components/conversion/trust-badges.md)
- **Conditional:** [Tabs](../../components/content/tabs.md), [Accordion](../../components/content/accordion.md), [Testimonials](../../components/conversion/testimonials.md), [Announcement Banner](../../components/utility/top-banner.md)
- **Discouraged:** [Carousel](../../components/layout/carousel.md)

## Acceptance coverage

Billing periods, currencies, plan availability, long feature names, mobile comparison, keyboard controls, checkout links, contact-sales behavior, legal qualifiers, analytics, and agreement with the live billing configuration.
