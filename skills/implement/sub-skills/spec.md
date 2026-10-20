---
name: spec
description: "Implement a whole spec, coordinating dependent tickets when present."
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: mattpocock/skills
  based_on_version: v1.3.1(49dd158)
  based_on_skill: implement
---

Implement the whole spec. Use the project's configured tracker or supplied artifact; reuse requirements and references already resolved.

## Scope

Read the spec and associated tickets until every requirement is assigned to a ticket or identified as uncovered. Track uncovered requirements as local work items with explicit prerequisites; creating tracker tickets is optional. Ask only when the assignment changes the intended behavior or boundaries.

With no tickets, follow the [root Implementation steps](../SKILL.md#implementation) for all spec requirements, then report completion or remaining blockers. A ticket breakdown is optional.

With tickets, use one **integration branch**. Tickets and local work items form a **task graph**; the **frontier** contains unfinished work whose prerequisites are satisfied in that branch. Existing completed tickets count only when their required behavior is present in the integration base.

## Steps

1. **Prepare.** Resolve blockers and identify the current frontier. Reuse the intended integration branch, or create one from the project's implementation base. Preserve existing work. If unfinished work has no ready frontier, identify the dependency or cycle and report it.
2. **Explore when needed.** Gather code or documentation needed by the frontier. Share durable findings by context pointers so implementers can reuse them. The exploration is complete when each assigned ticket has enough context to start.
3. **Implement the frontier.** Use parallel implementers when delegation and worktrees are available. Give each a branch based on the integration tip, one ready work item, spec constraints, relevant context pointers, and any surface/type request. Tracked tickets follow [ticket](ticket.md); local work items follow the [root Implementation steps](../SKILL.md#implementation) with their resolved requirements. Each reports changes and verification evidence. Overlapping work can run sequentially; when parallel tooling is unavailable, implement the frontier sequentially on the integration branch using the same workflows.
4. **Integrate and advance.** Merge completed work serially onto the integration branch, resolve conflicts, and run checks covering the combined changes and affected dependencies. Recheck relevant acceptance criteria after conflict resolution. A ticket unblocks dependents only after its implementation is integrated and verified. Update tracker state according to project workflow at that point. Recompute the frontier and repeat until every in-scope requirement is implemented or an explicit dependency prevents progress.
5. **Verify the spec.** Account for every spec requirement, including uncovered requirements identified during scoping. Verify cross-ticket behavior and affected UI routes against the combined branch; individual ticket checks alone do not establish integration correctness. Follow `/git code-review`, fix findings, and rerun checks affected by those fixes.
6. **Finish.** Remove worktrees created for this run only after their work is integrated; preserve and report unmerged work. Report the integration branch, completed requirements and tickets, verification evidence, and remaining blockers. For branch finalisation, the user can invoke `/finalise`.
