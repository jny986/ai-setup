---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/pagina
  based_on_version: main(239cb67)
  based_on_skill: contact
---

# Contact Page

## Scope

A Contact page routes a user's intent to the right channel and sets expectations for what happens next. It is not one undifferentiated form for sales, support, privacy, press, partnerships, and abuse reports.

## Content

- **Core:** contact purposes, appropriate channels, required information, response expectation.
- **Common:** sales, support, general inquiry, press, partnerships.
- **Conditional:** office or legal address, security, privacy, abuse, emergency guidance, status link.

Use real inboxes, forms, SLAs, regions, and support boundaries. Add the smallest submission endpoint needed when no form path exists, with validation, spam protection, consent, success, retry, and failure behavior.

## Component candidates

- **Common:** [Card](../../components/layout/card.md), [Call to Action Section](../../components/conversion/cta.md)
- **Conditional:** [Tabs](../../components/content/tabs.md), [Accordion](../../components/content/accordion.md), [Trust Signals](../../components/conversion/trust-badges.md)

## Acceptance coverage

Delivery, recipient routing, keyboard and screen-reader labels, privacy disclosure, attachments, rate limits, confirmation, localization, and that unavailable support is not promised.
