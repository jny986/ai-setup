# Git

A router skill for git and pull request workflows. `SKILL.md` picks one of five sub-skills from the task, or from a sub-skill name you pass, and the agent follows that sub-skill as if it were the skill. The sub-skills cover committing, opening PRs, finalising a branch, reviewing a diff and resolving merge conflicts.

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
- `/git finalise`: run code and security reviews, fix findings, then open the PR.
- `/git code-review since main`: review everything since `main`.
- `/git resolving-merge-conflicts`: finish an in-progress merge or rebase.

`commit-it` still works as the old name for `git commit`. Without a sub-skill name, the router picks one from the task ("commit this", "open a PR", "review my branch"). Because the skill allows implicit invocation, asking in plain language also works without typing `/git`.

## Resources

| Path | What it is |
|---|---|
| [`SKILL.md`](SKILL.md) | The router: chooses a sub-skill and loads it. |
| [`sub-skills/commit.md`](sub-skills/commit.md) | Resolves the ticket in context, switches to the branch it calls for (a Kanopi `branch_name` is used verbatim), makes one conventional commit and pushes. Never force-pushes. |
| [`sub-skills/create-pr.md`](sub-skills/create-pr.md) | Commits and pushes via `git commit`, opens a GitHub PR with `gh` (using the repo's PR template if one exists), then watches CI and fixes failures. Hints: draft, base, title, reviewers, "verify" to run tests, lint and typecheck first. |
| [`sub-skills/finalise.md`](sub-skills/finalise.md) | Runs `git code-review`, fixes its findings and re-reviews once if needed, then runs `security review-code` against the same base. Security review allows two automatic fix passes for straightforward issues and asks for instructions on unresolved findings before `git create-pr`. Only runs when you ask for it explicitly. |
| [`sub-skills/code-review.md`](sub-skills/code-review.md) | Reviews the diff since a fixed point on two axes, repo standards and the originating spec, using parallel sub-agents, and checks whether your existing PR comments were addressed. On a PR, it can submit a review with the inline comments you pick, after you confirm the verdict. |
| [`sub-skills/resolving-merge-conflicts.md`](sub-skills/resolving-merge-conflicts.md) | Resolves each conflict hunk from the intent of both sides, runs the project's checks and completes the merge or rebase. |
| [`agents/openai.yaml`](agents/openai.yaml) | Display metadata for OpenAI and Codex agents. |

## How the sub-skills nest

```
finalise ─▶ code-review ─▶ (fixes) ─▶ security review-code ─▶ (fix/review loop or user instructions) ─▶ create-pr ─▶ commit
```

Pick the outermost sub-skill that matches what you want. `git finalise` runs these nested workflows, so you don't need to call them first.

## Requirements

- `git` with an `origin` remote.
- `gh`, authenticated, for `git create-pr`, `git finalise` and the PR side of `git code-review`.
- `git code-review` reads `docs/agents/issue-tracker.md` to fetch specs. Run `/setup` to create it if missing.
- `git finalise` requires the [security skill](../security/README.md) for its vulnerability review. Install it with `npx skills add jny986/ai-setup --skill security`.
- Optional: a ticket MCP server such as Kanopi, used to resolve tickets and branch names.
