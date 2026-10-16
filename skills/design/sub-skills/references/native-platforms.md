---
name: native-platforms
description: "Build native iOS, iPadOS, and Android interfaces using platform navigation, controls, text scaling, themes, and accessibility."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: pbakaus/impeccable, pbakaus/impeccable, pbakaus/impeccable
  based_on_version: main(2f98774), main(2f98774), main(2f98774)
  based_on_skill: ios, android, adapt.native
---

# Native platform design

Use when building or changing native iOS, iPadOS, or Android UI, including React Native, Expo, and Flutter apps. Apply the shipped OS's interaction and accessibility conventions through the framework in use. Mobile web and PWAs use [mobile-ui-design](mobile-ui-design.md). For implementation APIs, check current official platform and framework documentation against the project's supported versions.

Read existing `DESIGN.md`, product constraints, and the actual navigation and theme setup. Preserve an intentional cross-platform design while honoring each OS's Back behavior, insets, accessibility settings, and text scaling. Brand can shape typography, color, content, and motion within those constraints.

## Platform decisions

| Area | iOS / iPadOS | Android |
|---|---|---|
| Navigation | Platform tabs for peer destinations, stacks for hierarchy, sheets for focused subtasks; retain the expected interactive Back gesture. | Navigation suited to window size; honor system Back and predictive Back where supported by the app and framework. |
| Adaptive layout | Recompose for available window space, iPad multitasking, and orientation; keep list/detail selection coherent. | Recompose for available window space, multi-window, and supported foldable postures; consider rail or pane layouts where useful. |
| Insets | Respect safe areas, system bars, keyboard, and dismissal behavior; keep controls reachable. | Handle system bars, display cutouts, keyboard/IME, and hinges; preserve useful edge-to-edge content without obscuring actions. |
| Typography | Use Dynamic Type-aware text styles; ensure custom fonts scale with the user's preferences. | Use scalable text roles through the theme; respect system font scaling and wrapping. |
| Touch | Use comfortably sized hit areas, ordinarily at least 44 pt, distinct from visual icon size. | Use comfortably sized hit areas, ordinarily at least 48 dp, distinct from visual icon size. |
| Theme | Semantic colors and platform materials or app tokens that cover supported appearances and contrast settings. | Semantic theme roles covering supported appearances and contrast; use dynamic color when it fits the product. |
| Controls | Prefer native controls and expected picker, menu, list, and sheet behavior where they fit. | Prefer established Material or project component behavior; keep system interaction guarantees. |
| Icons | Use a coherent family; platform symbols can supply text-aware weights and scaling. | Use a coherent family aligned with the app's component system and theme. |
| Motion | Preserve navigation continuity and the platform's Reduce Motion alternative. | Preserve navigation continuity and respect system animation preferences. |

Point, dp, and CSS px are distinct implementation units; use the target framework's logical sizing rather than copying CSS measurements. Give custom controls accessible roles, names, values, actions, and focus order. Explain state changes through platform accessibility APIs.

## Implementation checks

- Keep user input and task state through supported resize, orientation, keyboard, background/return, and navigation changes.
- Use platform modality intentionally. Provide a clear completion or exit; protect unsaved work where dismissal could lose it.
- Make text and controls expand for larger text and localization; allow scrolling when content exceeds the window.
- Make gestures interruptible, preserve system navigation gestures, and offer an accessible way to perform required actions.
- Choose system components or proven project components before adding custom interaction machinery.

## Verify on the native runtime

Build and run the actual app; browser previews of cross-platform code supply web evidence only. Capture the shipped device classes from a simulator, emulator, or device. Exercise the primary task, Back and dismiss, keyboard insets, large text, supported appearances, and relevant assistive technology. Use [native-audit](native-audit.md) for the review pass and [adapt](adapt.md) for configuration changes.

Record device or emulator identity, OS, appearance, text size, and input method. Preserve original simulator/device settings when changing them for inspection and restore those values afterward. Distinguish simulator coverage from hardware evidence for gestures, haptics, and performance. Unavailable environments are verification limits.
