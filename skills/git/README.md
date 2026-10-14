# Git

A router skill for git and pull request workflows. `SKILL.md` picks one of five guides from the task, or from a guide name you pass, and the agent follows that guide as if it were the skill. The guides cover committing, opening PRs, finalising a branch, reviewing a diff and resolving merge conflicts.

## Install

```sh
npx skills add jny986/ai-setup --skill git
```

## Usage

```
/git [guide] [task]
```

- `/git commit`: commit and push the current work.
- `/git create-pr draft, base develop`: open a draft PR against `develop`.
- `/git finalise`: review, fix, then open the PR.
- `/git code-review since main`: review everything since `main`.
- `/git resolving-merge-conflicts`: finish an in-progress merge or rebase.

`commit-it` still works as the old name for `commit`. Without a guide name, the router picks one from the task ("commit this", "open a PR", "review my branch"). Because the skill allows implicit invocation, asking in plain language also works without typing `/git`.

## Resources

| Path | What it is |
|---|---|
| [`SKILL.md`](SKILL.md) | The router: chooses a guide and loads it. |
| [`references/commit.md`](references/commit.md) | Resolves the ticket in context, switches to the branch it calls for (a Kanopi `branch_name` is used verbatim), makes one conventional commit and pushes. Never force-pushes. |
| [`references/create-pr.md`](references/create-pr.md) | Commits and pushes via `commit`, opens a GitHub PR with `gh` (using the repo's PR template if one exists), then watches CI and fixes failures. Hints: draft, base, title, reviewers, "verify" to run tests, lint and typecheck first. |
| [`references/finalise.md`](references/finalise.md) | Runs `code-review`, fixes its findings in one new commit, re-reviews once if needed, then runs `create-pr`. Only runs when you ask for it explicitly. |
| [`references/code-review.md`](references/code-review.md) | Reviews the diff since a fixed point on two axes, repo standards and the originating spec, using parallel sub-agents, and checks whether your existing PR comments were addressed. On a PR, it can submit a review with the inline comments you pick, after you confirm the verdict. |
| [`references/resolving-merge-conflicts.md`](references/resolving-merge-conflicts.md) | Resolves each conflict hunk from the intent of both sides, runs the project's checks and completes the merge or rebase. |
| [`agents/openai.yaml`](agents/openai.yaml) | Display metadata for OpenAI and Codex agents. |

## How the guides nest

```
finalise ─▶ code-review ─▶ (fixes) ─▶ create-pr ─▶ commit
```

Pick the outermost guide that matches what you want. `finalise` already runs the other three, so you don't need to call them first.

## Requirements

- `git` with an `origin` remote.
- `gh`, authenticated, for `create-pr`, `finalise` and the PR side of `code-review`.
- `code-review` reads `docs/agents/issue-tracker.md` to fetch specs. Run `/setup-matt-pocock-skills` to create it if missing.
- Optional: a ticket MCP server such as Kanopi, used to resolve tickets and branch names.
