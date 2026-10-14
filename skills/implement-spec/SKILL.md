---
name: implement-spec
description: "Implement a specification in code."
disable-model-invocation: true
license: MIT
metadata:
  version: "1.0"
  author: jny986
  author-url: https://jny986.com
  based_on: mattpocock/skills@v1.2.3 (MIT)
---

You have been provided a spec. This spec should have tickets associated with it, describing how to implement the spec.

The tickets are not a list of steps. They are a **task graph** with blocking relationships between them. This means there is always a **frontier** of tickets which are ready to be grabbed.

Communication to and from subagents should be sparse. Communicate primarily through **context pointers**: to the spec, tickets, and research notes. Don't duplicate information already available via pointers.

**Implementer subagents** should run in the background where possible, for maximum concurrency.

## Steps

1. Read the spec and tickets, until you can name the current **frontier** and each ticket's blockers.

2. (optional) Use an **exploration subagent** to conduct any exploration required by the tickets - relevant codebase files or external documentation. If **graphify** is implemented (i.e. `graphify-out/` exists), the exploration subagent should query it first to explore the codebase. Ensure the exploration subagent can save files - it should save its markdown notes in a directory outside the repo, accessible by all future subagents. This lets **implementer subagents** focus on implementation rather than exploration.

3. Use **implementer subagents** to implement each ticket on the **frontier**. Each implementer subagent should work in its own worktree, on its own branch.

4. As each **implementer subagent** completes, check whether it unblocks new tickets. Repeat step 3 for the updated **frontier** until no tickets remain.

5. (conditional) If any ticket created or changed UI, use an **implementer subagent** to run `./impeccable audit` against it and implement the recommendations, then run `./impeccable audit` again. Repeat until an audit round yields no more implementable recommendations.

6. Review each completed implementation against its ticket's requirements. If any requirement is unmet, return to step 3 to implement the missing requirements.

7. Clean up all **implementer subagent** worktrees.

8. Run `/finalise` without asking for approval — completing the prior steps is itself the go-ahead.
