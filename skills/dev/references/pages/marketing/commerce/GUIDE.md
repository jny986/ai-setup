# Commerce Pages

## Shared Responsibility

Commerce pages help shoppers discover, evaluate, purchase, and follow the fulfillment of real products. Price, availability, variants, shipping, tax, returns, and payment states must come from authoritative commerce systems.

## Modes

- **Catalog:** support category-aware browse, search, filters, sorting, merchandising, pagination, and useful empty states.
- **Product detail:** present one purchasable product with media, variants, current price, availability, delivery expectations, policies, evidence, and purchase actions.
- **Cart:** preserve selected items and variants, expose editable quantities and costs, explain promotions, and provide a reliable route to checkout.
- **Checkout:** collect only required identity, delivery, billing, and payment information through recoverable steps with an explicit final commitment.
- **Order confirmation:** confirm the completed transaction once, identify what happens next, and avoid accidental duplicate submission.
- **Order tracking:** show current fulfillment state, shipment events, support paths, and permitted order actions without exposing another customer's data.
- **Wishlist:** preserve intentional saved products and clearly communicate authentication, availability, price changes, and move-to-cart behavior.

## Components And Verification

Navigation, Task Input, Grid, Card, Carousel, Tabs, Trust Signals, FAQ, Announcement Banner, Modal, and CTA Section may apply. Verify variant and inventory races, price and currency, tax, shipping, discounts, payment retries, idempotency, address validation, fraud and privacy boundaries, receipts, cancellation and returns, unavailable items, localization, structured data, accessibility, and small-screen purchase flow.

## Bricks Components

Catalog recommendations; links go to the component guides in this tree.

- Commerce Catalog (`commerce-catalog`): **Core:** [Task Input](../../../components/utility/task-input/GUIDE.md); **Common:** [Navigation Menu](../../../components/navigation/navigation-menu/GUIDE.md), [Grid](../../../components/layout/grid/GUIDE.md), [Card](../../../components/layout/card/GUIDE.md), [Sidebar](../../../components/navigation/sidebar/GUIDE.md); **Conditional:** [Tabs](../../../components/content/tabs/GUIDE.md), [Accordion](../../../components/content/accordion/GUIDE.md), [Announcement Banner](../../../components/utility/top-banner/GUIDE.md)
- Commerce Product Detail (`commerce-product`): **Core:** [Call to Action Section](../../../components/conversion/cta/GUIDE.md); **Common:** [Carousel](../../../components/layout/carousel/GUIDE.md), [Tabs](../../../components/content/tabs/GUIDE.md), [Accordion](../../../components/content/accordion/GUIDE.md), [Trust Signals](../../../components/conversion/trust-badges/GUIDE.md); **Conditional:** [FAQ Section](../../../components/content/faq-section/GUIDE.md), [Testimonials](../../../components/conversion/testimonials/GUIDE.md), [Breadcrumb](../../../components/navigation/breadcrumb/GUIDE.md)
- Shopping Cart (`cart`): **Core:** [Call to Action Section](../../../components/conversion/cta/GUIDE.md); **Common:** [List](../../../components/layout/list/GUIDE.md), [Trust Signals](../../../components/conversion/trust-badges/GUIDE.md); **Conditional:** [Announcement Banner](../../../components/utility/top-banner/GUIDE.md), [Modal](../../../components/conversion/popup/GUIDE.md), [FAQ Section](../../../components/content/faq-section/GUIDE.md); **Discouraged:** [Carousel](../../../components/layout/carousel/GUIDE.md)
- Checkout (`checkout`): **Core:** [Call to Action Section](../../../components/conversion/cta/GUIDE.md); **Common:** [List](../../../components/layout/list/GUIDE.md), [Trust Signals](../../../components/conversion/trust-badges/GUIDE.md); **Conditional:** [Announcement Banner](../../../components/utility/top-banner/GUIDE.md), [Modal](../../../components/conversion/popup/GUIDE.md), [FAQ Section](../../../components/content/faq-section/GUIDE.md); **Discouraged:** [Carousel](../../../components/layout/carousel/GUIDE.md)
- Order Confirmation (`order-confirmation`): **Common:** [List](../../../components/layout/list/GUIDE.md), [Announcement Banner](../../../components/utility/top-banner/GUIDE.md); **Conditional:** [How-to Section](../../../components/content/howto-section/GUIDE.md), [FAQ Section](../../../components/content/faq-section/GUIDE.md), [Call to Action Section](../../../components/conversion/cta/GUIDE.md); **Discouraged:** [Hero](../../../components/branding/hero/GUIDE.md)
- Order Tracking (`order-tracking`): **Common:** [List](../../../components/layout/list/GUIDE.md), [Announcement Banner](../../../components/utility/top-banner/GUIDE.md); **Conditional:** [How-to Section](../../../components/content/howto-section/GUIDE.md), [FAQ Section](../../../components/content/faq-section/GUIDE.md), [Call to Action Section](../../../components/conversion/cta/GUIDE.md); **Discouraged:** [Hero](../../../components/branding/hero/GUIDE.md)
- Wishlist (`wishlist`): **Core:** [Task Input](../../../components/utility/task-input/GUIDE.md); **Common:** [Navigation Menu](../../../components/navigation/navigation-menu/GUIDE.md), [Grid](../../../components/layout/grid/GUIDE.md), [Card](../../../components/layout/card/GUIDE.md), [Sidebar](../../../components/navigation/sidebar/GUIDE.md); **Conditional:** [Tabs](../../../components/content/tabs/GUIDE.md), [Accordion](../../../components/content/accordion/GUIDE.md), [Announcement Banner](../../../components/utility/top-banner/GUIDE.md)
