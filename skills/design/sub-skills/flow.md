---
name: flow
description: "Design or improve a user task journey: entry points, steps, forms, onboarding, interface copy, feedback, errors, recovery, and completion."
license: Apache-2.0
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: pbakaus/impeccable, pbakaus/impeccable, pbakaus/impeccable
  based_on_version: main(2f98774), main(2f98774), main(2f98774)
  based_on_skill: onboard, clarify, distill
---

# Design a task flow

Help users complete a particular job through a coherent sequence of actions and states. Apply this to creation, editing, search, permissions, onboarding, checkout, or recovery. Match the deliverable to the request: a flow specification for planning, working changes for implementation. For visual treatment within settled behavior, use [refine](refine.md); for the wider design brief, use [shape](shape.md).

## Workflow

1. **Define the journey.** Read relevant `PRODUCT.md`, domain terminology, `DESIGN.md`, existing routes, forms, and service behavior. Identify the user's starting knowledge, entry point, desired result, prerequisites, and supported roles. In onboarding, name the first useful outcome the product can actually deliver. Resolve missing facts that change behavior. Finish with a bounded task and observable completion, distinguishing confirmed behavior from proposals.
2. **Walk and map it.** Exercise an existing journey with realistic data, or map a proposed one from the evidence. For each step record the information needed, action, resulting state, and available way back or forward. Include the relevant cases below. Identify repeated entry, unnecessary decisions, hidden prerequisites, unclear consequences, and dead ends. Finish when every mapped branch reaches a useful outcome or an explicit recovery or exit.
3. **Design the path.** Put prerequisites before the action that needs them; reuse known data and appropriate defaults. Collect information when it becomes necessary, group related choices, and expose uncommon detail progressively. Preserve required capabilities and domain distinctions. For first use, guide people through real work with examples where useful, and make optional instruction dismissible and replayable. Finish with an explicit proposed sequence and any behavior or service changes it requires.
4. **Write copy in context.** Use the copy guidance below across the affected journey. Keep product terms and factual meaning consistent. Finish when each decision explains its consequence and each failure offers a truthful next step.
5. **Deliver or implement.** For planning, return the proposed journey, state transitions, copy, and unresolved dependencies. For implementation, follow the existing state and component conventions; align visible feedback with actual service outcomes and preserve input through recoverable failures. Reuse the surface guidance linked by the router. Finish when the requested artifact covers the mapped branches, with unsupported backend behavior named as a dependency.
6. **Verify the journey.** Walk the primary path and selected alternatives with realistic content, relevant widths, keyboard or platform input, and assistive technology where available. Check returning users, retries, cancellation, refresh, and duplicate actions where applicable; use [harden](references/harden.md) for deeper stress coverage. Verify dismissals and completion persist at the appropriate user and device scope. Report observed outcomes and gaps; use measured analytics or user testing to support claims about activation or completion rates.

## States to consider

Select the states that the task can actually encounter.

| State | Design question |
|---|---|
| First use or missing prerequisites | Can the user reach useful work, understand what is required, and skip optional teaching? |
| Loading or submission | Does feedback describe the real operation, with honest progress and protection against unintended duplicate work? |
| Empty or no results | Is this first use, a cleared collection, a filter result, unavailable data, or a failure? What action fits that cause? |
| Invalid input | Are requirements available before submission, errors associated with fields, and valid input preserved? |
| Permissions or service failure | What can the user retry, change, request, or safely leave? |
| Interruption or cancellation | What happens to progress on navigation, refresh, session expiry, or return? |
| Success or repeat use | Is completion confirmed, the consequence clear, and unnecessary teaching absent on subsequent visits? |

## Copy and feedback

- Name actions by their outcome, with specific verbs and objects where needed. Use the same term for the same domain concept throughout the journey.
- Give forms persistent labels and relevant format requirements. Place correction guidance near the field and announce dynamic errors accessibly.
- Explain what failed, why when known and useful, and how to recover. Preserve uncertainty when the system cannot know whether an operation completed.
- State consequential outcomes before destructive, payment, privacy, or access changes. Support safe undo where the product can guarantee recovery; use explicit confirmation when needed.
- Keep placeholders as examples, helper text informative, and success messages proportional to the result. Match tone to the user's situation and the action's stakes.
- Use complete translatable messages, accommodate text expansion, align accessible names with visible labels, and communicate state through more than color or icons.

For activation strategy, funnel measurement, and experiments, consult [marketing onboarding](../../marketing/sub-skills/strategies/conversion/onboarding.md). Keep this sub-skill focused on the journey and its implementation; quantitative improvement requires measured evidence.

Completion: a user can follow the supported journey to its real outcome, understand the state at each decision, and recover or exit from the applicable failure paths. A specification identifies any unimplemented or undecided branches explicitly.
