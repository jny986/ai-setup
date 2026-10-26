---
name: review-prs
description: "Review open pull requests awaiting the user's review. Lists them, then goes through them one by one, asking continue or skip for each, timing the ticket when it has a time tracker. Use when the user asks to review PRs, their review queue, or \"what needs my review\". Invoked as /git review-prs."
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
---

Work through the PRs waiting on the user, reviewing each with `git code-review`.

## Steps

1. **List.** First check the local docs (`AGENTS.md`, `CONTRIBUTING.md`, `docs/agents/`) for a label a PR needs before it's ready for review. Then `gh pr list --search "review-requested:@me is:open draft:false" --json number,title,author,baseRefName,url`, adding `--label "<label>"` when the docs name one. None documented: no label filter. A PR number or URL passed as an argument reviews just that PR (from step 3).
2. **Go one by one.** Show the next PR (number, title, author, URL) and ask whether to continue or skip it. Wait for the answer. None open: say so and stop.
3. **Start the timer.** On "continue", find the PR's ticket (see `git code-review` step 2) and the ticket system in `docs/agents/issue-tracker.md`. If that system tracks time against tickets (e.g. Kanopi timesheets), start a timer on the ticket now. No ticket, or no time tracking: skip this step.
4. **Review.** Check the PR out in its own worktree so the user's branch is untouched: follow "Check out a PR in its own worktree" in [references/gh-review.md](references/gh-review.md), one command per call. Refer to the same file for submitting the review and replying to threads. Follow the complete `git code-review` workflow there with the PR's base branch as the fixed point, including its mandatory full `security review-code` run and coverage record in step 6. Run it in this session: do the Standards, Spec and (for UI changes) UI/UX reviews yourself, one after the other, instead of dispatching sub-agents in step 4; use the same reviewer briefs and smell baseline. Follow its PR review hand-off in step 8, waiting for each user answer before submitting the review.
5. **Clean up.** `git worktree remove ../pr-<n>` once its review is submitted or skipped. Retain any local branch holding security fixes until those commits are included in the PR or the user decides how to handle them.
6. **Stop the timer.** Once the user has decided what to do with the review (submit, edit, drop), stop any timer started in step 3.
7. **Ready for the next PR?** Ask whether they're ready to move on. Wait for the answer. If so, return to step 2 for the next PR.
8. **Summarise.** When no PRs are left (or the user stops), one line per PR: number, verdict submitted (or "not submitted"), unfixed finding count.
