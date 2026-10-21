---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/bricks
  based_on_version: main(fa7e1e0)
  based_on_skill: newsletter-signup
---

# Newsletter Signup

## Scope

A newsletter signup collects consent and the minimum information needed to subscribe a person to a defined publication.

## Decisions

Specify the publication promise, frequency where material, fields, consent model, provider, confirmation flow, existing-subscriber behavior, and success destination.

## Constraints

- Explain what the person is subscribing to near the form.
- Collect only necessary fields and follow the applicable consent policy.
- Do not treat a network request as success until the provider accepts it.
- Keep API credentials and privileged provider calls on the server.
- Preserve entered data on recoverable errors.

## Acceptance criteria

Valid subscriptions, invalid input, duplicate subscribers, rate limits, and provider failure produce accurate feedback. Keyboard labels, consent text, mobile input, and confirmation delivery work; analytics exclude personal data.
