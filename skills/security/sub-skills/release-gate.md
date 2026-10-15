---
name: release-gate
description: Final security check before merging or deploying a change.
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: getsentry/skills, addyosmani/agent-skills, affaan-m/ECC
  based_on_version: main(d18b7aa), 0.6.13(aeac41d), v2.2.3-889-gb92f181b(b92f181b)
  based_on_skill: security-review, security-and-hardening, security-review
---

The gate before merge or deploy. Every item gets a checkable answer: pass, fail, or not applicable with a reason.

## Steps

1. **Run the checks.** Skip a row only when the change cannot touch it.

   | Check | Pass when |
   |---|---|
   | Secrets | None in source or git history |
   | Dependencies | Native audit has no reachable critical or high findings; CI blocks unreviewed install scripts |
   | Input | Every external input is schema-validated at its boundary |
   | Injection and XSS | Queries are parameterized; output is encoded |
   | Auth | Authentication and per-resource authorization on every protected endpoint |
   | Sessions | Cookies are `httpOnly`, `secure`, `sameSite`; CSRF protection on state-changing routes |
   | Headers and CORS | HTTPS enforced; security headers present; CORS uses an explicit origin list |
   | Errors and logs | Responses hide internals; logs hold no secrets, tokens or PII |
   | Rate limits | Auth endpoints limited, on a shared store when more than one instance serves traffic |
   | Server fetches | User-influenced URLs pass an allowlist (SSRF) |
   | Destructive paths | Resolved target is under an allowlisted root, below it, with ownership evidence |
   | LLM features | Model output validated and encoded before use; no secrets or tenant data in context |
   | Personal data | Classified, minimized, has retention and a deletion path |
   | Cloud and CI/CD | Passes [the cloud pre-deployment list](references/infrastructure/cloud.md#pre-deployment-cloud-security-checklist) when infra changed |

2. **Report.** Done when every row has an answer. Open with the failures, each pointing to the control in `build-securely` or `harden-deployment` that fixes it. Full list: [security checklist](references/security-checklist.md).
