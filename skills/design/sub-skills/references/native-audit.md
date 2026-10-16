---
name: native-audit
description: "Audit native UI behavior, accessibility, performance, appearance, and adaptivity using platform runtime evidence."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: pbakaus/impeccable
  based_on_version: main(2f98774)
  based_on_skill: audit.native
---

# Native UI audit

Use with [audit](../audit.md) for iOS, Android, React Native, or Flutter apps. Replace its browser checks with source inspection and captures from the simulator, emulator, or a device. Inspect the supported device classes, orientations, appearance modes, and input methods; identify anything not exercised. [Mobile UI design](mobile-ui-design.md) covers touch-first design patterns, while this reference checks the implemented result.

## Platform pass

For implementation decisions use [native-platforms](native-platforms.md); for device or window changes use [adapt](adapt.md).

| Area | Verify |
|---|---|
| Accessibility | VoiceOver or TalkBack names, roles, state announcements, focus and reading order; text scaling; visible focus; 44 pt iOS and 48 dp Android touch targets; Reduce Motion; contrast in each appearance. |
| Performance | Launch and first usable frame; long-list recycling; scroll and gesture frame stability; main-thread work; image decoding and caching; wasted recomposition or re-rendering. |
| Appearance | Semantic platform colors or design tokens; light and dark appearances; native materials and elevation; consistent icon family. |
| Platform behavior | iOS edge-swipe back and Android system or predictive Back; safe areas, status bars, keyboard insets; native navigation and controls. |
| Adaptivity | Phone and tablet layouts, landscape, split-screen or multi-window, keyboard or IME, and foldable posture where supported. |

Run the primary task with assistive technology and large text where tools allow. Record the device, OS version, appearance, text size, and input method for each finding. Source code can identify a likely problem; a claimed runtime failure needs a capture, reproduced interaction, or platform test. Keep platform conventions specific to the shipped OS instead of grading every app against both.

In the combined audit report, use the same P0–P3 severity and evidence format as [audit](../audit.md). Mark device or OS combinations that were not tested as limits rather than defects. A native audit is complete when each applicable area above has a verified result or a named verification limit.
