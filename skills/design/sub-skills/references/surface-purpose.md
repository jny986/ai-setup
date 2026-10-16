---
name: surface-purpose
description: "Choose UI hierarchy, density, and expression according to whether users need to work, read, decide, or explore."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: pbakaus/impeccable, pbakaus/impeccable, pbakaus/impeccable, pbakaus/impeccable, pbakaus/impeccable
  based_on_version: main(2f98774), main(2f98774), main(2f98774), main(2f98774), main(2f98774)
  based_on_skill: new-work, operate, mode-operate, mode-read, mode-persuade
---

# Design for the surface's purpose

Read when shaping a new surface or deciding how hierarchy, density, and expression should serve its audience. Choose by the surface's user outcome: one product can have a persuasive landing page, a working dashboard, and readable documentation. Keep approved brand and platform constraints across them.

| Purpose | Prioritize | Where expression helps | Evidence to inspect |
|---|---|---|---|
| Complete a task | Familiar affordances, clear state, scanability, useful density, efficient repeated use. | Type, palette, grouping, and precise feedback; distinctive details that help people understand the work. | Can users locate information, act, and recover without learning decorative controls? |
| Understand material | Reading hierarchy, comfortable prose, navigation, examples, and findable answers. | The frame, typography, section openers, figures, and coherent treatment of code or tables. | Can readers find the answer, follow its context, and continue comfortably? |
| Decide and act | A comprehensible offer, relevant evidence, consequence, and clear action. | Composition, imagery, type, and motion that make the actual subject intelligible and memorable. | Can visitors explain what is offered, why it matters, and what action is available? |
| Explore the work | The artifact itself, context, discovery, and continuity. | Composition and interaction that reveal the work and support exploration. | Is the work visible early, usable across input methods, and able to hold attention without obstructive chrome? |

## Apply the distinction

- **Hierarchy and density:** keep frequent task controls stable; give reading a calm column; give persuasion a clear argument; let showcases lead with the artifact. A dense professional tool can be appropriate when grouping and state are legible.
- **Typography:** use predictable text roles for controls and data, readable measure for prose, and expressive display type where the composition warrants it. One family can carry a complete product UI.
- **Color and motion:** preserve semantic meaning and immediate feedback. Larger expressive treatments can serve a campaign or showcase; repeated tasks need speed and predictable behavior.
- **Navigation and controls:** preserve discoverability and platform expectations across all purposes. Identity does not require users to relearn basic interactions.

Use these as decision criteria rather than fixed visual presets. Record task-specific reasoning in the brief; put reusable, approved system decisions in `DESIGN.md`. Read the router's reference for the actual surface for implementation details.
