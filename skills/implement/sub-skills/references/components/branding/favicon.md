---
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: kostja94/marketing-skills
  based_on_version: v1.0.0(8dd89c5)
  based_on_skill: favicon-generator
---

# Favicon and app icons

Favicons identify a site in browser tabs and bookmarks; touch and installed-app icons serve distinct platform surfaces. A [logo](logo.md) supplies the approved mark, while this reference covers asset and delivery decisions.

## Asset choices

| Surface | Common asset | Constraint |
|---|---|---|
| Browser tab | SVG or small PNG; ICO where fallback support requires it | Recognizable at small sizes, including 16px and 32px previews |
| Apple home screen | Commonly a 180px PNG | Platform-specific appearance and background treatment |
| Installed web app | Commonly 192px and 512px manifest entries | Dimensions and purpose match the targeted install surfaces |
| Maskable launcher | Dedicated maskable artwork | Safe area and background are designed for cropping; a square icon is not automatically maskable |

These are common export targets, not a universal required set. The supported platforms determine the delivered files. Approved aspect ratio, colors, clear space, and simplification policy come from the brand source.

## Delivery contract

- The project's framework owns asset placement and generated head tags. Explicit HTML declarations are appropriate when that mechanism is absent.
- Icon declarations, MIME types, dimensions, manifest entries, and served files agree.
- Browser, touch, and installed-app declarations point to their intended assets rather than an arbitrary shared export.
- Stable asset URLs and the project's cache invalidation policy govern replacement; cached icons may outlive a page reload.
- Search-specific requirements come from [Google's favicon documentation](https://developers.google.com/search/docs/appearance/favicon-in-search) when search appearance is in scope. Valid assets do not guarantee inclusion or immediate recrawling.

## Acceptance criteria

- Every declared asset loads at the intended deployment base path with the expected content type.
- Small-size previews remain recognizable on supported light and dark browser surfaces.
- Touch icons and install flows use the intended artwork on supported devices.
- Manifest purposes and maskable crops preserve the mark where installed-app support is required.
- Replacement behavior respects the project's caching strategy; search crawlability and hostname ownership are checked when search appearance is in scope.

## Related references

[Press and media](../../pages/marketing/press.md) covers distribution of approved brand assets. The marketing router's `brand-visual` and `indexing` sub-skills cover visual identity and crawlability when those tasks are requested.
