# GitHub PR review operations

Every command is one call: no `&&`, `;`, `|`, heredoc or `$(...)`. Chains get rejected as a whole.

## Payloads from files

Write JSON or Markdown bodies to a temp file with the Write tool, then pass the file path. Use `--jq` instead of piping to `jq`.

## Submit a review: result, comment and inline comments

One `POST` creates and submits the review. Write `/tmp/review-<n>.json`:

```json
{
  "commit_id": "<head-sha>",
  "event": "REQUEST_CHANGES",
  "body": "Review-level comment.",
  "comments": [
    { "path": "src/file.php", "line": 42, "side": "RIGHT", "body": "Single-line comment." },
    { "path": "src/file.php", "start_line": 50, "start_side": "RIGHT", "line": 54, "side": "RIGHT", "body": "Multi-line comment." }
  ]
}
```

Then:

`gh api repos/{owner}/{repo}/pulls/<n>/reviews --input /tmp/review-<n>.json`

Top-level fields:

- `event`: the result. `APPROVE`, `REQUEST_CHANGES` or `COMMENT`. Omitted, the review stays `PENDING` and is not visible to others (see Pending reviews).
- `body`: the review-level comment. Required for `REQUEST_CHANGES` and `COMMENT`; optional for `APPROVE`. Omit `comments` for a review with no inline comments.
- `commit_id`: head SHA of the PR (`gh pr view <n> --json headRefOid --jq .headRefOid`). Defaults to the latest commit; set it so comments anchor to the commit that was reviewed, otherwise a later push leaves them outdated.

Each `comments[]` item:

- `path` and `body`: required. `path` is relative to the repo root.
- `line`: the file line number (not the diff offset) the comment attaches to. For a multi-line comment, the last line of the range. The line must appear in the PR diff, or the whole review fails with 422.
- `side`: `RIGHT` for added or unchanged lines (new file's numbering); `LEFT` for deleted lines (old file's numbering). Always set it.
- `start_line` and `start_side`: first line of a multi-line range, same meaning as `line` and `side`. Both are required for multi-line.
- Avoid `position` (legacy diff offset, being phased out).

On a 422, fix the offending `line` or `path` and resubmit. Check `gh pr view <n> --json reviews` before retrying so a review isn't posted twice.

## Review with no inline comments

`gh pr review <n> --approve -F /tmp/review-body.md`

Use `--request-changes` or `--comment` for the other results. `--body-file`/`-F` reads the body from a file. `gh pr review` cannot attach inline comments.

## Pending reviews

For a review built over several steps, create it without `event`, then submit:

1. `gh api repos/{owner}/{repo}/pulls/<n>/reviews --input /tmp/review-<n>.json` (payload without `event`). Note the `id` in the response.
2. `gh api repos/{owner}/{repo}/pulls/<n>/reviews/<review-id>/events --input /tmp/submit-<n>.json` with `{"event": "APPROVE", "body": "..."}`. `event` is required here.

## Reply to a review comment

`gh api repos/{owner}/{repo}/pulls/<n>/comments/<comment-id>/replies -F body=@/tmp/reply-<id>.md`

Short replies: `-f body="text"`. `<comment-id>` must be the thread's top-level comment; replies to replies are not supported.

## Standalone inline comment

Outside a review (a single immediate comment, notifying right away):

`gh api repos/{owner}/{repo}/pulls/<n>/comments --input /tmp/comment-<n>.json`

Payload: `body`, `commit_id`, `path`, `line`, `side` (all required for a single-line comment), plus `start_line` and `start_side` for a range. For a file-level comment, set `"subject_type": "file"` and drop `line`. Prefer the review payload above so the comments land as one review.

## Read comments

- Reviews and top-level comments: `gh pr view <n> --json comments,reviews`
- Inline comments: `gh api repos/{owner}/{repo}/pulls/<n>/comments --jq '.[] | {id, path, line, user: .user.login, body}'`

## Read review threads

For unresolved-thread workflows, use GraphQL `repository.pullRequest.reviewThreads`; the REST comments list alone does not supply resolution state. Get the authenticated login with `gh api user --jq .login`.

Write a GraphQL JSON request to a temp file and run `gh api graphql --input /tmp/threads-<n>.json`. Query `reviewThreads(first: 100, after: $cursor)` for:

- `id`, `isResolved`, `isOutdated`, `path`, `line`, `originalLine`, `viewerCanResolve`.
- `comments(first: 100)` with each comment's `id`, `databaseId`, `url`, `body`, `createdAt`, `author { login }` and `replyTo { id }`.
- `pageInfo { hasNextPage endCursor }` on both connections.

Advance the thread cursor until exhausted. Independently exhaust each thread's comments using `node(id: $threadId) { ... on PullRequestReviewThread { comments(first: 100, after: $commentCursor) { ... } } }`. Paginating the outer connection does not paginate nested comments. Use the root comment's URL and REST `databaseId` for linking and replying; keep the thread's GraphQL `id` for resolution. Handle GraphQL `errors` and missing data as failed reads even if the HTTP status is successful.

## Resolve an approved thread

After the calling workflow's approval step, check `viewerCanResolve` and send this mutation through `gh api graphql` using a JSON request file:

```graphql
mutation($threadId: ID!) {
  resolveReviewThread(input: {threadId: $threadId}) {
    thread { id isResolved }
  }
}
```

Confirm the returned `isResolved` is true. A permission failure leaves the thread open and must be reported. Thread fields and mutations are documented in the [GitHub GraphQL pull request reference](https://docs.github.com/en/enterprise-cloud%40latest/graphql/reference/pulls).

## Check out a PR in its own worktree

Run each as its own call:

1. `git worktree add ../pr-<n> --detach`
2. `git -C ../pr-<n> fetch origin pull/<n>/head`
3. `git -C ../pr-<n> checkout --detach FETCH_HEAD`

Run later git commands with `git -C ../pr-<n>`.
