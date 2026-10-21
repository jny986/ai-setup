---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/pagina
  based_on_version: main(239cb67)
  based_on_skill: commerce
---

# Commerce Pages

## Scope

Commerce pages help shoppers discover, evaluate, purchase, and follow the fulfillment of real products. Price, availability, variants, shipping, tax, returns, and payment states must come from authoritative commerce systems.

## Modes

- **Catalog:** support category-aware browse, search, filters, sorting, merchandising, pagination, and useful empty states.
- **Product detail:** present one purchasable product with media, variants, current price, availability, delivery expectations, policies, evidence, and purchase actions.
- **Cart:** preserve selected items and variants, expose editable quantities and costs, explain promotions, and provide a reliable route to checkout.
- **Checkout:** collect only required identity, delivery, billing, and payment information through recoverable steps with an explicit final commitment.
- **Order confirmation:** confirm the completed transaction once, identify what happens next, and avoid accidental duplicate submission.
- **Order tracking:** show current fulfillment state, shipment events, support paths, and permitted order actions without exposing another customer's data.
- **Wishlist:** preserve intentional saved products and clearly communicate authentication, availability, price changes, and move-to-cart behavior.

## Component candidates

**Commerce Catalog, Wishlist:**

- **Primary candidates:** [Task Input](../../components/utility/task-input.md)
- **Common:** [Navigation Menu](../../components/navigation/navigation-menu.md), [Grid](../../components/layout/grid.md), [Card](../../components/layout/card.md), [Sidebar](../../components/navigation/sidebar.md)
- **Conditional:** [Tabs](../../components/content/tabs.md), [Accordion](../../components/content/accordion.md), [Announcement Banner](../../components/utility/top-banner.md)

**Commerce Product Detail:**

- **Primary candidates:** [Call to Action Section](../../components/conversion/cta.md)
- **Common:** [Carousel](../../components/layout/carousel.md), [Tabs](../../components/content/tabs.md), [Accordion](../../components/content/accordion.md), [Trust Signals](../../components/conversion/trust-badges.md)
- **Conditional:** [FAQ Section](../../components/content/faq-section.md), [Testimonials](../../components/conversion/testimonials.md), [Breadcrumb](../../components/navigation/breadcrumb.md)

**Shopping Cart, Checkout:**

- **Primary candidates:** [Call to Action Section](../../components/conversion/cta.md)
- **Common:** [List](../../components/layout/list.md), [Trust Signals](../../components/conversion/trust-badges.md)
- **Conditional:** [Announcement Banner](../../components/utility/top-banner.md), [Modal](../../components/conversion/popup.md), [FAQ Section](../../components/content/faq-section.md)
- **Discouraged:** [Carousel](../../components/layout/carousel.md)

**Order Confirmation, Order Tracking:**

- **Common:** [List](../../components/layout/list.md), [Announcement Banner](../../components/utility/top-banner.md)
- **Conditional:** [How-to Section](../../components/content/howto-section.md), [FAQ Section](../../components/content/faq-section.md), [Call to Action Section](../../components/conversion/cta.md)
- **Discouraged:** [Hero](../../components/branding/hero.md)

## Acceptance coverage

Variant and inventory races, price and currency, tax, shipping, discounts, payment retries, idempotency, address validation, fraud and privacy boundaries, receipts, cancellation and returns, unavailable items, localization, structured data, accessibility, and small-screen purchase flow.
