# Product Interface Pages

## Scope

Product Interface pages explain one way to access or operate the product and lead the user to a first successful use. API, desktop, mobile, browser extension, MCP, and CLI pages share this goal but have different installation, permission, and runtime contracts.

## Variants

- **API:** capabilities, authentication, SDK or request example, limits, key or docs path; not endpoint reference.
- **Desktop app:** operating systems, architecture, signed download, requirements, install and update behavior.
- **Mobile app:** stores, device and region support, QR handoff, permissions, account continuity.
- **Browser extension:** supported browsers, store or enterprise install, permissions, current-page access, update and removal.
- **MCP:** server type, transport, client configuration, exposed tools, authentication, scope and trust boundary.
- **CLI:** package or binary, shell and platform support, authentication, first command, update and uninstall.

## Content

Core regions cover interface identity, supported environment, capabilities, acquisition or connection, first success, and help.

## Component candidates

**API Page, Desktop App Page, Browser Extension Page, MCP Page, CLI Page:**

- **Common:** [Hero](../../components/branding/hero.md), [Call to Action Section](../../components/conversion/cta.md), [How-to Section](../../components/content/howto-section.md)
- **Conditional:** [Tabs](../../components/content/tabs.md), [Accordion](../../components/content/accordion.md), [FAQ Section](../../components/content/faq-section.md), [Trust Signals](../../components/conversion/trust-badges.md)

**Mobile App Page:**

- **Common:** [Hero](../../components/branding/hero.md), [Call to Action Section](../../components/conversion/cta.md), [How-to Section](../../components/content/howto-section.md)
- **Conditional:** [FAQ Section](../../components/content/faq-section.md), [Trust Signals](../../components/conversion/trust-badges.md)

## Acceptance coverage

Real versions, links, package names, signatures, permissions, commands, code examples, regional availability, installation failure, authentication, update paths, uninstall or revocation, metadata, and handoff to documentation or the product.
