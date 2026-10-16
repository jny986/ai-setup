---
name: generate
description: "Build comparable, viewable UI variants and apply the selected option within the existing project identity."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: pbakaus/impeccable
  based_on_version: main(2f98774)
  based_on_skill: generate
---

# Generate UI variants

Use when the user wants several design options for a named element or section of an existing web interface. Produce viewable alternatives within the project's framework, then let the user choose one. For a new page or identity, use the relevant surface guide first; for image or graphic variants, use [image-generation](image-generation.md). This reference needs no Impeccable live helper, overlay, session IDs, or project-specific Impeccable files.

## Procedure

1. **Resolve the target and brief.** Locate the element's source, the route or story that renders it, and the user's direction. Use the requested count, or three by default; keep the set small enough to compare (at most eight). If a direction is vague, infer three useful, distinct options from the element's purpose and surrounding design. Ask only when the named element cannot be located or a material constraint is genuinely unclear. Finish when one target, count, and shared constraints are recorded.
2. **Lock the identity.** Read `DESIGN.md` and the project brand kit when present; use [design-context](design-context.md) to discover missing decisions. Inspect actual tokens, loaded fonts, neighboring components, and the rendered element. Write one short identity sentence covering palette roles, type character, layout rhythm, surface treatment, and voice. Preserve content, behavior, accessibility, and existing brand commitments unless the user explicitly asks to change them. Finish when every planned option can be checked against the same identity sentence.
3. **Plan distinct options.** Give each variant a different primary axis: hierarchy, layout, type scale, use of existing color roles, density, or grouping. For a requested direction such as “bolder” or “quieter,” vary how that direction is achieved rather than changing the same property three times. Name the axis and the intended user effect for each variant. Finish when the options differ at a glance while remaining coherent side by side.
4. **Build a comparison.** Use the project's existing component preview, Storybook, or a temporary app route so all variants render with the real CSS, fonts, assets, and content. Keep draft styles scoped and avoid changing the shipped default while the choice is open. Reuse shared logic and props; vary presentation at the component boundary. If no app preview can run, create a local HTML comparison using the same assets and tokens and state the fidelity limit. Finish when every option is visible at the same viewport and clearly labeled by its design axis.
5. **Inspect and present.** View the comparison at desktop and narrow widths; exercise focus, hover, touch, and relevant states. Check copy, contrast, overflow, and consistency with the identity lock. Fix broken options before showing them. Present the variants with a brief difference and a link or screenshot for each, then ask the user to select one or request a specific revision. Finish when the user can compare complete, usable options rather than source snippets.
6. **Apply the choice.** Once selected, move the chosen design into the production component, remove the comparison route and unused draft styles, and recheck the affected states and build. Preserve the other options only if the user asks to keep them. Finish when the shipped element matches the selected preview and no temporary preview code remains.

If the request is to explore ideas only, the comparison is the deliverable; wait for a choice before step 6. If the user has already specified which option to implement, proceed through step 6 in the same task.
