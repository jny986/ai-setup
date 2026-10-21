# GitHub PR review operations

Every command is one call: no `&&`, `;`, `|`, heredoc or `$(...)`. Chains get rejected as a whole.

## Payloads from files

Write JSON or Markdown bodies to a temp file with the Write tool, then pass the file path. Use `--jq` instead of piping to `jq`.

## Submit a review with inline comments

Write `/tmp/review-<n>.json`:

```json
{
  "event": "REQUEST_CHANGES",
  "body": "Review-level comment.",
  "comments": [
    { "path": "src/file.php", "line": 42, "side": "RIGHT", "body": "Inline comment." }
  ]
}
```

- `event`: `APPROVE`, `REQUEST_CHANGES` or `COMMENT`. `REQUEST_CHANGES` requires a `body`.
- `line` is a line of the new file inside the diff. Multi-line: add `start_line` and `start_side`.

Then submit:

`gh api repos/{owner}/{repo}/pulls/<n>/reviews --input /tmp/review-<n>.json`

## Reply to a review comment

`gh api repos/{owner}/{repo}/pulls/<n>/comments/<comment-id>/replies -F body=@/tmp/reply-<id>.md`

Short replies: `-f body="text"`. `<comment-id>` is the `id` of the thread's first comment.

## Read comments

- Reviews and top-level comments: `gh pr view <n> --json comments,reviews`
- Inline comments: `gh api repos/{owner}/{repo}/pulls/<n>/comments --jq '.[] | {id, path, line, user: .user.login, body}'`

## Check out a PR in its own worktree

Run each as its own call:

1. `git worktree add ../pr-<n> --detach`
2. `git -C ../pr-<n> fetch origin pull/<n>/head`
3. `git -C ../pr-<n> checkout --detach FETCH_HEAD`

Run later git commands with `git -C ../pr-<n>`.
