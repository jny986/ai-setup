---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/bricks
  based_on_version: main(fa7e1e0)
  based_on_skill: logo
---

# Logo

## Scope

A logo component presents the product or organization mark consistently and links it appropriately for the current surface. It may combine a symbol and wordmark, but it does not own the complete visual identity.

## Decisions

Choose the approved asset, lockup, contrast variant, responsive treatment, and link behavior from the target project's brand source. Navigation commonly links the logo to the product home; authenticated products may use a compact mark when space is constrained.

## Constraints

- Preserve aspect ratio, clear space, and approved colors.
- Do not redraw, recolor, stretch, animate, or crop the mark without brand authorization.
- Use meaningful accessible text for linked marks; decorative duplicates should not repeat the brand name.
- Avoid downloading an unverified logo when the repository already contains approved assets.

## Acceptance criteria

The approved mark renders clearly on light and dark surfaces, narrow navigation, and high-density displays. Image failure preserves accessible identification; the link has the correct name, keyboard focus, and destination.
