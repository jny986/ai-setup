---
name: security
description: "Router for security work. Use to review code for vulnerabilities, build a feature securely, harden Docker, CI/CD, cloud or dependencies, or gate a release. Sub-skills: review-code, build-securely, harden-deployment, release-gate."
argument-hint: "[sub-skill] [task]"
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
---

A router over security sub-skills, organised by situation. Each lives at `sub-skills/<sub-skill>.md` in this skill's folder.

## Steps

1. **Pick the sub-skill.**
   - Argument names a sub-skill: use it.
   - Otherwise match the task to a situation below, taking the first row that fits. When two fit equally, ask once.
2. **Follow it.** Read `sub-skills/<sub-skill>.md` and follow it as if it were the skill.

## Sub-skills

Start here. Pick by situation.

| Situation | Sub-skill |
|---|---|
| Audit existing code or a diff for vulnerabilities | [`review-code`](sub-skills/review-code.md) |
| Design or write a feature that handles input, auth, data, external calls, LLMs or personal data | [`build-securely`](sub-skills/build-securely.md) |
| Secure Dockerfiles, CI/CD, cloud, secrets or dependencies | [`harden-deployment`](sub-skills/harden-deployment.md) |
| Final check before merging or deploying | [`release-gate`](sub-skills/release-gate.md) |

## How they nest

`security build-securely` and `security harden-deployment` end at `security release-gate`. `security review-code` hands infrastructure findings to `security harden-deployment`.
