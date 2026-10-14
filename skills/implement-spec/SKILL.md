---
name: implement-spec
description: "Implement a specification in code."
disable-model-invocation: true
license: MIT
metadata:
  version: "1.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: mattpocock/skills
  based_on_version: v1.3.1(49dd158)
  based_on_skill: implement
---

You have been provided a spec. This spec should have tickets associated with it, describing how to implement the spec.

The issue tracker should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`.

The goal is the entire spec implemented on a single **integration branch**.

The tickets are not a list of steps. They are a **task graph** with blocking relationships between them. This means there is always a **frontier** of tickets which are ready to be grabbed.

Communication to and from subagents should be sparse. Communicate primarily through **context pointers**: to the spec, tickets, research notes, and previous commits. Don't duplicate information already available via pointers.

**Implementer subagents** should run in the background where possible, for maximum concurrency.

## Steps

1. Read the spec and tickets, until you can name the current **frontier** and each ticket's blockers.

2. (optional) Use an **exploration subagent** to conduct any exploration required by the tickets - relevant codebase files or external documentation. If **graphify** is implemented (i.e. `graphify-out/` exists), the exploration subagent should query it first to explore the codebase. Ensure the exploration subagent can save files - it should save its markdown notes in a directory outside the repo, accessible by all future subagents. This lets **implementer subagents** focus on implementation rather than exploration.

3. Create the integration branch.

4. Use **implementer subagents** to implement each ticket on the **frontier**, each in its own worktree, on its own branch. Each implementer subagent:
   - confirms its worktree is based on the integration branch before starting, and resets onto it if not;
   - calls the Skill tool with `tdd` to build the ticket;
   - merges the integration branch tip into its own branch before reporting done.

5. As each **implementer subagent** completes, merge its work to the integration branch with a **merger subagent**, then check whether it unblocks new tickets. Repeat step 4 for the updated **frontier** until no tickets remain.

6. (conditional) If any ticket created or changed UI, use an **implementer subagent** to run `./impeccable audit` against it and implement the recommendations, then run `./impeccable audit` again. Repeat until an audit round yields no more implementable recommendations.

7. Review each completed implementation against its ticket's requirements. If any requirement is unmet, return to step 4 to implement the missing requirements.

8. Call the Skill tool with `code-review` on the integration branch. Fix all issues raised by the code review in a single **implementer subagent**.

9. Clean up all **implementer subagent** worktrees.

10. Run `/git finalise` without asking for approval — completing the prior steps is itself the go-ahead.
