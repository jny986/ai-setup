---
name: finalize
description: Finalize a branch of this repo's skill work: review, skills-check every skill in skills/, rebuild indexes, run check-all.sh, then create the PR.
disable-model-invocation: true
---

Run only when the user explicitly invokes `/finalize`.

Take a branch from "dev work done" to "PR open" in this repo. Read `docs/agents/skills.md` for frontmatter, provenance and index rules, and the `git` skill's `sub-skills/code-review.md`, `sub-skills/commit.md` and `sub-skills/create-pr.md` for those workflows. Work the steps in order.

## Steps

1. **Diff base.** Measure the branch against a fixed point:
   - Upstream tracked: `git merge-base @{u} HEAD`.
   - Else `git merge-base --fork-point <default-branch> HEAD` when it succeeds.
   - Else the merge-base of the default branch (`gh repo view --json defaultBranchRef -q .defaultBranchRef.name`) with `HEAD`.
   - Unresolved: ask the user for the fixed point.

2. **Code review.** Follow `git code-review` against the fixed point, including its security loop. Done when it reports.

3. **Skills-check.** Follow `security skills-check` with scope fixed to every skill folder under `skills/`, regardless of what the branch touched. Skip `source-skills/` and `.agents/skills/`. Done when each skill has a verdict. Treat each `BLOCK` or `DANGER` verdict and each Critical or Warning finding as a finding to fix in step 4; list Info findings in the summary.

4. **Fix findings.** Fix every Standards, Spec and skills-check finding directly. Keep the list of what was fixed. A finding you judge a false positive goes to the user with the quoted evidence instead of being fixed.

5. **Rebuild indexes.** Run `python3 scripts/build-index.py` when the branch added, moved, renamed or re-described a skill or sub-skill, or bumped `metadata.version`. Review `git diff skills.html SKILLS.md`; both are generated, so edit the source and rebuild.

6. **Check.** Run `scripts/check-all.sh`. Done when it exits 0; fix each failing step and rerun.

7. **Commit.** If steps 4 to 6 changed files, make one new commit, e.g. `fix: address review findings`, with regenerated `skills.html` and `SKILLS.md` included. Amending or folding into existing commits is out; add a new commit.

8. **Re-review.** Skip when every change in step 4 was cosmetic (formatting, naming, comments, dead-code removal). Otherwise repeat steps 2 and 3 once against the same fixed point, then step 6, and report anything remaining.

9. **Summarise.** Tell the user what was fixed (or "no issues found"): the code review and skills-check results, `check-all.sh` status, and any finding the user chose to ignore, with their decision. Proceed to step 10 without waiting.

10. **Create the PR.** Follow `git create-pr`. The `finalize` invocation is the user's go-ahead: commit, push and PR creation proceed without a separate confirmation once steps 2 and 3 complete.
