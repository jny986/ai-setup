# Git

A router skill for git and pull request workflows. `SKILL.md` picks a sub-skill from the task, or from a sub-skill name you pass, and the agent follows that sub-skill as if it were the skill. The sub-skills cover committing, opening PRs, reviewing diffs and PRs, addressing review feedback, and resolving merge conflicts.

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
- `/git code-review since main`: review everything since `main`.
- `/git pr-fixes 123`: list unanswered unresolved review threads, choose a resolution for each, and delegate each approved fix to its own sub-agent. Run `finalise` on the branch, then ask for separate approval before replies and thread resolution.
- `/git resolving-merge-conflicts`: finish an in-progress merge or rebase.

`commit-it` still works as the old name for `git commit`. Without a sub-skill name, the router picks one from the task ("commit this", "open a PR", "review my branch"). Because the skill allows implicit invocation, asking in plain language also works without typing `/git`.

## Resources

| Path | What it is |
|---|---|
| [`SKILL.md`](SKILL.md) | The router: chooses a sub-skill and loads it. |
| [`sub-skills/commit.md`](sub-skills/commit.md) | Resolves the ticket in context, switches to the branch it calls for (a Kanopi `branch_name` is used verbatim), makes one conventional commit and pushes. Never force-pushes. |
| [`sub-skills/create-pr.md`](sub-skills/create-pr.md) | Commits and pushes via `git commit`, opens a GitHub PR with `gh` (using the repo's PR template if one exists), then watches CI and fixes failures. Hints: draft, base, title, reviewers, "verify" to run tests, lint and typecheck first. |
| [`sub-skills/code-review.md`](sub-skills/code-review.md) | Reviews the diff since a fixed point on three axes: repo standards and the originating spec using parallel sub-agents, plus security through `security review-code`. Security repeats fixes and reviews until every item is resolved or explicitly ignored by the user, asking for instructions when a decision is needed or progress stalls. It also checks whether your existing PR comments were addressed. On a PR, it can submit a review with the inline comments you pick, after you confirm the verdict. |
| [`sub-skills/pr-fixes.md`](sub-skills/pr-fixes.md) | Inventories unresolved review threads without a user reply, proposes resolutions and waits for per-issue decisions. Uses one sub-agent per approved fix, verifies the combined result and runs `finalise` on the branch, then asks before posting replies or resolving eligible threads. |
| [`sub-skills/resolving-merge-conflicts.md`](sub-skills/resolving-merge-conflicts.md) | Resolves each conflict hunk from the intent of both sides, runs the project's checks and completes the merge or rebase. |
| [`agents/openai.yaml`](agents/openai.yaml) | Display metadata for OpenAI and Codex agents. |

## How the sub-skills nest

```
code-review ─▶ security review-code ─▶ (fix/review loop or user instructions)
create-pr ─▶ commit
pr-fixes ─▶ finalise ─▶ (code-review, create-pr) ─▶ reply approval
```

Pick the outermost sub-skill that matches what you want. To review a branch, fix findings and open a PR in one workflow, install the standalone [finalise skill](../finalise/SKILL.md) and invoke `/finalise`. It also runs as a required step of `git pr-fixes` before PR replies.

## Requirements

- `git` with an `origin` remote.
- `gh`, authenticated, for `git create-pr` and the PR side of `git code-review`.
- `git pr-fixes` requires authenticated GitHub access, sub-agent support for fixes, and the [finalise](../finalise/SKILL.md) and [security](../security/README.md) skills; resolving threads also requires permission on the PR.
- `git code-review` reads `docs/agents/issue-tracker.md` to fetch specs. Run `/setup` to create it if missing.
- `git code-review` (including when called by `finalise` or `git review-prs`) requires the [security skill](../security/README.md) for its vulnerability review. Install it with `npx skills add jny986/ai-setup --skill security`.
- Optional: a ticket MCP server such as Kanopi, used to resolve tickets and branch names.
