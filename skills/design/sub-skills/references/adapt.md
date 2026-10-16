---
name: adapt
description: "Adapt an existing interface to another device, window size, input method, or platform while preserving the user task."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: pbakaus/impeccable, pbakaus/impeccable
  based_on_version: main(2f98774), main(2f98774)
  based_on_skill: adapt, adapt.native
---

# Adapt an interface

Use when an existing experience must work in a different window size, device class, input method, or platform. Preserve the user task and required capabilities while changing the structure and interaction for the target context. [Mobile UI design](mobile-ui-design.md) covers mobile web details; [native-platforms](native-platforms.md) covers native conventions.

## Workflow

1. **Compare contexts.** Inspect the current interface, `DESIGN.md`, and relevant product facts. Name the source assumptions and target constraints: available window space, orientation, input, text scaling, connection, and usage posture. Identify what currently fails or becomes awkward. Finish with a bounded target and observable task success.
2. **Plan structural changes.** Choose from the table below based on the actual task. Reuse established identity and content; translate controls and navigation into the target platform's vocabulary. Specify how state, selection, progress, and focus survive a layout change. Finish with mappings for affected navigation, content, controls, and states.
3. **Implement to available space and capability.** Use content-driven breakpoints or container queries on the web and the framework's adaptive layout facilities on native. Account for keyboard, system bars, safe areas, and foldable hinges where relevant. Detect input capabilities independently of viewport width. Finish when the same task works in each supported structure.
4. **Verify transitions and interaction.** Test the target sizes and the intermediate widths where structure changes, plus relevant orientation, split-screen, text-size, and input combinations. Exercise controls and recovery paths, not only screenshots. Report the engine, simulator, emulator, or device used and what remains untested. Completion requires a usable target experience and preserved task state through supported configuration changes.

## Structural choices

| Change | Decisions to make |
|---|---|
| Wide to narrow | Reorder by task priority; collapse secondary panes deliberately; retain access to essential fields, actions, and data. |
| Narrow to wide | Use extra space for relevant simultaneous context, such as list/detail or editing/preview, rather than stretching controls. |
| Pointer to touch or mixed input | Replace hover-only discovery; provide visible alternatives to gestures; account for hit area, scrolling, keyboard access, and focus. |
| Phone to tablet or resizable window | Adapt panes and navigation to window space, including a narrow window on a large device; preserve selection across structure changes. |
| Web to native or between native platforms | Preserve product meaning and brand while adopting the target's navigation, Back behavior, controls, text scaling, and system feedback. |
| Print or email | Read [poster-design](poster-design.md) for print delivery or [email-design](email-design.md) for email; translate interactions into readable content and useful destinations. |

## Gesture evidence

For a slider, drag surface, swipe action, or scrollable strip, verify the primary gesture completes, scrolling across it still works as intended, cancellation releases interaction state, and the next attempt succeeds. Check keyboard or single-action alternatives where needed. A resized browser viewport proves layout; synthesized touch proves behavior only in the tested engine. Record hardware and other-engine gaps without claiming they passed.

For broad stress conditions use [harden](harden.md); for a changed task sequence use [flow](../flow.md).
