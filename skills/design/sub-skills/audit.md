---
name: audit
description: "Audit an existing website or app interface for UX and visual quality, accessibility, performance, theming, responsive behavior, and implementation consistency. Deliver verified, prioritized findings."
license: Apache-2.0
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: pbakaus/impeccable, pbakaus/impeccable
  based_on_version: main(2f98774), main(2f98774)
  based_on_skill: audit, critique
---

# Design audit

Review an existing interface and deliver a prioritized diagnosis. Inspect the design before reading automated findings so tool output does not anchor the visual judgment. Then verify technical issues and merge both passes into one report. Apply fixes when the user also requests them.

## Steps

1. **Resolve the target.** Name the exact page, flow, component, or set of surfaces and its primary user task. Read `PRODUCT.md` for the user's job and constraints, `DESIGN.md` for the UI system, and the project brand kit for applicable identity rules when those files exist; use [design-context](references/design-context.md) to discover missing decisions. For a native app, load [native-audit](references/native-audit.md) and use its platform pass in place of browser checks. List the relevant viewport, theme, interaction, error, and empty states. Finish when each surface has a concrete target and success action.
2. **Inspect visual evidence.** For web UI, view desktop and narrow widths, including the first viewport and full scroll; for native UI, use the shipped device classes from [native-audit](references/native-audit.md). Exercise the primary flow and relevant states. Record what draws attention first and what action the screen invites, then inspect product specificity, hierarchy, information order, cognitive load, copy, and visual coherence using [design-critique](references/design-critique.md). If the app cannot run, use current screenshots or visual fixtures and check them against the source; if none exist, limit visual claims to what the source proves. Finish with location-specific observations and any evidenced strengths, recorded before automated findings are read.
3. **Verify implementation quality.** Inspect relevant code and run available accessibility, performance, and browser checks. Check semantics, labels, focus, contrast, reduced motion, responsive overflow and touch gestures, asset weight, animation cost, token use, theme switching, and repeated implementation drift. Exercise interactions when a screenshot cannot prove them. For each measured claim, record the method, viewport or state, and result; verify automated flags against the UI or code. Finish when every applicable review lens below has evidence or a named verification limit.
4. **Synthesize findings.** Merge duplicate symptoms under shared causes. Distinguish observed defects, verified code risks, and unverified tool flags; report the last group as limits rather than defects. Assign P0 to a blocked primary task, P1 to major user difficulty or a material accessibility barrier, P2 to friction with a workable path, and P3 to low-impact polish. Each finding names its location or state, evidence, user impact, and a specific fix. Finish when every reported issue is supported and the highest-impact findings are ordered, without filling a quota.
5. **Deliver and, if requested, fix.** Report the target, inspected states and methods, supported strengths, priority issues, systemic patterns, fix order, and verification limits. Give counts by severity only when useful; do not invent a score without an agreed rubric. If fixes were requested, implement them and recheck the affected states before reporting completion.

The audit is complete when the user can locate each priority issue, understand its effect, and act on its recommendation, and every applicable lens has evidence or a stated verification limit.

## Review lenses

| Lens | Questions to answer |
|---|---|
| Design specificity | Does the composition and interaction express this product's purpose, or could an unrelated product use it unchanged? |
| Usability | Is system status visible? Can users recognize actions, prevent and recover from errors, and leave unwanted states? Does the interface use their language? |
| Cognitive load | Are related choices grouped? Does a user need to remember earlier information or weigh too many options at once? |
| Visual system | Do hierarchy, type, color, spacing, imagery, and states follow a coherent brand system? |
| Accessibility | Can the primary flow be used by keyboard and assistive technology? Are labels, focus, contrast, and motion alternatives sufficient? |
| Performance | Do images, scripts, rendering, and motion support the task at realistic device and network conditions? |
| Responsive behavior | Does content reflow, remain readable, and support touch across the relevant widths and orientations? |
| Implementation integrity | Are tokens and components used consistently, and do visible controls perform the actions they promise? |

Walk the primary task from the perspectives relevant to the surface, such as a first-time user, frequent user, or keyboard user. Report the exact step that failed or slowed them rather than a generic persona prediction.

## Report shape

```text
Target and scope: [surface, user task, inspected states]
Evidence: [renders, viewports, interactions, checks, source files]
What works: [specific supported strengths, if any]
Priority issues:
  [P1] [problem] — [location/state]; [observed evidence]; [user impact]; [specific fix]
  ...
Systemic patterns: [shared causes, if any]
Fix order: [smallest ordered set of changes that addresses the priority issues]
Limits: [untested states, unavailable tools, unverified flags]
```
