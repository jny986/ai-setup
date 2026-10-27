---
name: ticket
description: Implement one tracked ticket and verify its acceptance criteria.
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: mattpocock/skills
  based_on_version: v1.3.1(49dd158)
  based_on_skill: implement
---

Implement one ticket against its acceptance criteria and parent-spec constraints.

1. **Resolve.** Read the ticket's current requirements, acceptance criteria, blockers, and linked spec from the project's configured tracker or supplied artifact. Reuse prior lookups and state its title. Ask when the reference remains ambiguous.
2. **Readiness.** Confirm that prerequisites are satisfied in the implementation base. If a dependency prevents progress, report its missing behavior and ticket reference. Sibling tickets bound the scope; the parent spec supplies constraints.
3. **Implement.** Follow the [root Implementation steps](../SKILL.md#implementation) with the resolved requirements, relevant context pointers, and any requested surface/type. Keep this ticket's scope through page/component and non-UI work.
4. **Complete.** Account for every acceptance criterion using the implementation results. Report behavior, verification, and blockers. The parent spec coordinator owns integration and tracker updates when nested; otherwise update tracker state only as requested or required by project workflow, after its completion criteria are met.
5. **Finalise.** Once the ticket is complete and verified, follow the [finalise skill](../../finalise/SKILL.md) on the implementation branch, passing its merge-base with the implementation base as the fixed point. If the current branch is the implementation base, first create a feature branch preserving the work. When nested in a spec, return the results to the spec coordinator instead; it finalises the integrated branch once the whole spec is complete. Report blockers if finalisation cannot proceed.
