---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
license: MIT
metadata:
  version: "1.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: mattpocock/skills
  based_on_version: v1.2.3(6acc160)
  based_on_skill: implement
---

Implement the work described by the user in the spec or tickets.

Treat the tickets as a **task graph**, not a checklist: blocking relationships define a **frontier** of tickets ready to be grabbed at any time.

Communicate with subagents sparsely, through **context pointers** (the spec, tickets, research notes) rather than restating their content.

## Steps

1. Read the spec and tickets until you can name the current **frontier** and each ticket's blockers.

2. (optional) Run an **exploration subagent** for any research the tickets require — relevant codebase files or external documentation. It saves its markdown notes outside the repo, so later subagents can reach them by pointer instead of re-exploring.

3. Run an **implementer subagent** per frontier ticket, each in its own worktree and branch, in the background for concurrency. Each uses /tdd at pre-agreed seams, and runs typechecking and its own test files regularly.

4. As each subagent finishes, mark its ticket done and recompute the frontier. Repeat step 3 until no tickets remain.

5. Clean up all implementer worktrees.
