# Authentication Page

## Scope

An Authentication page establishes, verifies, restores, or resumes identity. Login, signup, password recovery, verification, and invitation acceptance are modes of one identity journey, not marketing forms.

## Content

- **Core:** identity method, credential or provider controls, validation, security and recovery paths.
- **Common:** login/signup switching, SSO, verification, password reset, terms acknowledgement.
- **Conditional:** invitation context, MFA, passkeys, organization selection, regional eligibility.

Use the project's real identity provider, redirect contract, session model, and account rules. Keep product explanation concise and never expose whether a sensitive account exists beyond the provider's security policy.

## Component candidates
- **Conditional:** [Modal](../../components/conversion/popup.md), [Trust Signals](../../components/conversion/trust-badges.md)
- **Discouraged:** [Hero](../../components/branding/hero.md), [Carousel](../../components/layout/carousel.md)

## Acceptance coverage

Keyboard and password-manager behavior, autofill, error privacy, rate limits, OAuth cancellation, redirects, invitation expiry, localization, and narrow screens.
