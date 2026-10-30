# Git

A router skill for git and pull request workflows. `SKILL.md` picks a sub-skill from the task, or from a sub-skill name you pass, and the agent follows that sub-skill as if it were the skill. The sub-skills cover committing, opening PRs, reviewing diffs and PRs, addressing review feedback, repairing CI, and resolving merge conflicts.

## Install

```sh
npx skills add jny986/ai-setup --skill git
```

## Usage

```
/git [sub-skill] [task]
```

- `/git commit`: commit and push the current work.
- `/git create-pr draft, base develop`: open a draft PR against `develop`.
- `/git code-review since main`: review changes since `main`. Ask to review the repository to examine existing code.
- `/git pr-review 123`: review a PR, including prior feedback and selected publication.
- `/git review-prs`: work through the PRs awaiting your review.
- `/git pr-fixes 123`: list unanswered unresolved review threads, including those you created, choose a resolution for each, and delegate each approved fix to its own sub-agent. Run `finalise` on the branch, then ask for separate approval before replies and thread resolution.
- `/git resolving-merge-conflicts`: finish an in-progress merge or rebase.
- `/git ci-fix 123`: fix CI failures and merge conflicts on PR #123, push repairs to its existing branch, and keep monitoring until the latest head passes or a concrete blocker needs intervention. A PR URL also works.

`commit-it` still works as the old name for `git commit`. Without a sub-skill name, the router picks one from the task ("commit this", "open a PR", "review my branch"). Because the skill allows implicit invocation, asking in plain language also works without typing `/git`.

## Resources

| Path | What it is |
|---|---|
| [`SKILL.md`](SKILL.md) | The router: chooses a sub-skill and loads it. |
| [`sub-skills/commit.md`](sub-skills/commit.md) | Resolves the ticket in context, switches to the branch it calls for (a Kanopi `branch_name` is used verbatim), makes one conventional commit and pushes. Never force-pushes. |
| [`sub-skills/create-pr.md`](sub-skills/create-pr.md) | Commits and pushes via `git commit`, opens a GitHub PR with `gh` (using the repo's PR template if one exists), then watches CI and fixes failures. Hints: draft, base, title, reviewers, "verify" to run tests, lint and typecheck first. |
| [`sub-skills/code-review.md`](sub-skills/code-review.md) | Reviews development changes or a repository against standards, requirements, applicable UI/UX and security. Reports findings without making fixes. |
| [`sub-skills/pr-review.md`](sub-skills/pr-review.md) | Reviews one PR, checks prior feedback, and presents a verdict and inline comments for selection before publication. |
| [`sub-skills/review-prs.md`](sub-skills/review-prs.md) | Walks through PRs awaiting your review using `pr-review`. |
| [`sub-skills/pr-fixes.md`](sub-skills/pr-fixes.md) | Inventories unresolved review threads without a user reply, including threads the user created, proposes resolutions and waits for per-issue decisions. Uses one sub-agent per approved fix, verifies the combined result and runs `finalise` on the branch, then asks before posting replies or resolving eligible threads. |
| [`sub-skills/resolving-merge-conflicts.md`](sub-skills/resolving-merge-conflicts.md) | Resolves each conflict hunk from the intent of both sides, runs the project's checks and completes the merge or rebase. |
| [`sub-skills/ci-fix.md`](sub-skills/ci-fix.md) | Diagnoses failing checks and merge conflicts on an existing PR, verifies and pushes repairs, and repeats monitoring against the latest head until CI passes and conflicts are resolved. Reports external blockers explicitly. |
| [`agents/openai.yaml`](agents/openai.yaml) | Display metadata for OpenAI and Codex agents. |

## How the sub-skills nest

```
code-review ─▶ parallel review agents (Standards, Spec, UI/UX, Security)
            ─▶ combine reports
pr-review  ─▶ code-review ─▶ selected PR review
review-prs ─▶ pr-review
create-pr ─▶ commit, ci-fix
ci-fix ─▶ resolving-merge-conflicts (when needed)
pr-fixes ─▶ finalise ─▶ (code-review, create-pr) ─▶ reply approval
```

Pick the outermost sub-skill that matches what you want. To review a branch, fix findings and open a PR in one workflow, install the standalone [finalise skill](../finalise/SKILL.md) and invoke `/finalise`. It also runs as a required step of `git pr-fixes` before PR replies.

## Requirements

- `git` with an `origin` remote.
- `gh`, authenticated, for `git create-pr` and `git pr-review`.
- `git ci-fix` requires authenticated GitHub access to check diagnostics and push access to the PR head repository; external CI may need its provider's tools or credentials.
- `git pr-fixes` requires authenticated GitHub access, sub-agent support for fixes, and the [finalise](../finalise/SKILL.md) and [security](../security/README.md) skills; resolving threads also requires permission on the PR.
- `git code-review` prefers the installed `review` agent for each applicable axis, falling back to general-purpose agents or direct review when unavailable. See [agent setup](https://ai.jny986.com/agents.html#set-up-review). The coordinator handles reporting; `pr-review` handles publication.
- `git code-review` reads `docs/agents/issue-tracker.md` to fetch specs. Run `/setup` to create it if missing.
- `git code-review` (including when called by `finalise` or `git pr-review`) requires the [security skill](../security/README.md) for its vulnerability review. Install it with `npx skills add jny986/ai-setup --skill security`.
- Optional: a ticket MCP server such as Kanopi, used to resolve tickets and branch names.
