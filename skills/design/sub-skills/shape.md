---
name: shape
description: "Plan a UI surface or feature before implementation: user task, hierarchy, interactions, states, visual direction, and constraints. Deliver a design brief."
license: Apache-2.0
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: pbakaus/impeccable, pbakaus/impeccable
  based_on_version: main(2f98774), main(2f98774)
  based_on_skill: shape, new-work
---

# Shape a design

Turn a feature or surface request into a brief a builder can use. Shape owns decisions for this task; [product](product.md) records durable product facts and [document](document.md) records the reusable visual system.

## Workflow

1. **Establish the task.** Read the request, existing `PRODUCT.md`, `DESIGN.md`, applicable brand guidance, and the target's code or visual evidence. Identify who arrives, their situation, the job they need to complete, and the evidence of success. Name the surface, fidelity, implementation scope, and binding constraints. Finish with a concrete user outcome and an explicit account of what is established versus unresolved.
2. **Resolve material gaps.** Ask a small group of related questions only where the answer changes the design: real content and assets, data ranges, permissions, platform, accessibility, localization, or delivery constraints. Reuse answers already given. Keep unanswered choices visible as open decisions; label working assumptions. Finish when the brief can proceed with supported facts and clearly bounded uncertainty.
3. **Choose structure and direction.** Decide whether the task extends the current visual system or establishes a new direction. An existing interface remains evidence even when `DESIGN.md` is missing; use [design-context](references/design-context.md) to discover its rules. For an extension, work within those rules. For a requested redesign or a new system, explain the proposed direction and its consequences; seek a choice when materially different directions remain open. Read the router's reference for the surface. Finish with a hierarchy, interaction approach, and visual direction whose relationship to the existing system is explicit.
4. **Specify the experience.** Map the entry point, information order, primary action, feedback, and completion. Include relevant loading, empty, error, success, permission, and interrupted states, plus realistic content extremes. State how layout and interaction adapt to the target devices and input methods. Use [flow](flow.md) for detailed journey work when needed. Finish when the builder can implement the important states without inventing product behavior.
5. **Deliver the brief.** Use the smallest useful form below, linking evidence and existing components where they settle a decision. Record unresolved decisions and what depends on them. For a planning-only request, return the brief as the deliverable. When implementation is already requested, continue once material decisions are resolved; request a choice only for consequential open alternatives.

## Brief

- **Job and success:** audience, arrival context, primary task, and observable outcome.
- **Scope:** target surfaces, fidelity, existing behavior to preserve, and delivery constraints.
- **Structure and direction:** reading order, grouping, primary action, visual authority, and any proposed departure.
- **Behavior and content:** states, transitions, realistic ranges, responsive behavior, and accessibility needs.
- **Build guidance:** existing components and assets, necessary changes, assumptions, and open decisions.

Scale detail to the task: a settled component may need a few bullets; a multi-screen flow may need a state table or diagram. When purpose affects hierarchy, density, or expression, read [surface-purpose](references/surface-purpose.md). For an approved screenshot or mockup, use [reference-to-ui](references/reference-to-ui.md); for a device or platform change, use [adapt](references/adapt.md).

Completion: the brief defines a coherent, feasible experience and makes every unresolved decision that could change implementation visible.
