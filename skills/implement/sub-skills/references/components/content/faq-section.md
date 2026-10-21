---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/bricks
  based_on_version: main(fa7e1e0)
  based_on_skill: faq-section
---

# FAQ Section

## Scope

An FAQ section organizes real questions and direct answers within another page. It resolves recurring uncertainty at the point where it matters; it is not a container for unrelated keywords or a substitute for missing primary content.

## Content Contract

Each item needs a stable identifier, a user-centered question, and an answer whose first sentence gives the conclusion. Category and anchor fields are useful only when the page genuinely needs grouping or direct links. Keep visible content as the source for any derived structured data.

## Presentation

- Use expanded answers when the set is short or immediate visibility matters.
- Use accessible disclosure or accordion behavior when space and scanning justify it.
- Use groups or an anchor index for distinct topics; consider a dedicated FAQ page when the section becomes a knowledge base.

Presentation is a variant choice. Accordion is not part of the FAQ Section identity.

## Constraints

- Questions reflect real uncertainty, have substantive answers, and remain available through the chosen disclosure behavior.
- Important product, pricing, legal, or safety information must not exist only inside a collapsed FAQ.
- If multiple FAQ sections exist on one page, page-level structured data ownership must prevent contradictory or duplicate output.
- FAQ structured data needs a confirmed consumer requirement. Search appearance claims require verification against current eligibility rules; structured output alone does not establish eligibility.

## Acceptance criteria

Keyboard disclosure, heading order, and supported direct links work for long answers, missing items, and multiple sections. Answers remain available in the rendered document; any structured output agrees with the visible content.
