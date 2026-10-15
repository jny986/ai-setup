---
name: review-code
description: Audit existing code or a diff for exploitable vulnerabilities, then report findings.
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: getsentry/skills, addyosmani/agent-skills, affaan-m/ECC
  based_on_version: main(d18b7aa), 0.6.13(aeac41d), v2.2.3-889-gb92f181b(b92f181b)
  based_on_skill: security-review, security-and-hardening, security-review
---

Audit the code you were given. Report only what you can trace to an attacker.

## Steps

1. **Scope.** Report on the file, diff or component provided. Research the whole codebase: a pattern match alone is never a finding.

2. **Load guides.** Match what the code does, and read each match before judging it.

   | Code does | Read |
   |---|---|
   | API routes, GraphQL, REST design | [authorization](references/authorization.md), [authentication](references/authentication.md), [injection](references/injection.md), [api-security](references/api-security.md) |
   | Renders HTML, templates, forms | [xss](references/xss.md), [csrf](references/csrf.md) |
   | Handles files or uploads | [file-security](references/file-security.md) |
   | Crypto, secrets, tokens, PII | [cryptography](references/cryptography.md), [data-protection](references/data-protection.md) |
   | Deserializes data | [deserialization](references/deserialization.md) |
   | Fetches URLs server-side | [ssrf](references/ssrf.md) |
   | Multi-step business flow | [business-logic](references/business-logic.md) |
   | WebSocket, client-side JS, LLM input | [modern-threats](references/modern-threats.md) |
   | Config, headers, CORS | [misconfiguration](references/misconfiguration.md) |
   | Dependencies, CI | [supply-chain](references/supply-chain.md) |
   | Error handling, audit logs | [error-handling](references/error-handling.md), [logging](references/logging.md) |
   | Python | [python](references/languages/python.md) |
   | JavaScript, TypeScript | [javascript](references/languages/javascript.md) |
   | Dockerfile | [docker](references/infrastructure/docker.md) |
   | Cloud, CI/CD, IAM config | Switch to `security harden-deployment` |

3. **Trace.** For each suspect pattern, follow the value from its source to the sink. A finding needs an **attacker-controlled** source: request params, body, headers, cookies, path segments, uploads, other users' data, WebSocket messages. Settings, env vars, constants and signed session data are server-controlled, so they are not findings ([full source table](references/do-not-flag.md#attacker-controlled-vs-server-controlled)). Look for validation, sanitization, middleware and framework protection along the way. [Flag patterns](references/flag-patterns.md) lists the sinks that are findings on sight and the ones that need their source checked first.

4. **Sort.** Every suspect lands in one bucket:

   | Bucket | Test | Action |
   |---|---|---|
   | Finding | Vulnerable pattern and attacker-controlled input confirmed by the trace | Report with severity |
   | Needs verification | Vulnerable pattern, source unclear after the trace | Note it |
   | Drop | Theoretical, best-practice, defense-in-depth, test code, dead code, framework-mitigated | Say nothing |

5. **Report.** Done when every finding shows its full trace and severity. Use the [report template](references/report-template.md). If nothing qualifies, say: "No high-confidence vulnerabilities identified."

   | Severity | Impact | Examples |
   |---|---|---|
   | Critical | Direct exploit, severe impact, no auth required | RCE, SQL injection to data, auth bypass, hardcoded secrets |
   | High | Exploitable with conditions, significant impact | Stored XSS, SSRF to metadata, IDOR to sensitive data |
   | Medium | Specific conditions required, moderate impact | Reflected XSS, CSRF on state-changing actions, path traversal |
   | Low | Defense-in-depth, minimal direct impact | Missing headers, verbose errors, weak algorithms in non-critical context |

## Gotchas

- Framework-mitigated patterns (auto-escaping, ORM parameterization) are findings only through their escape hatches: `|safe`, `mark_safe`, `dangerouslySetInnerHTML`, `v-html`, `.raw()`, `.extra()`. Common false positives and the escape hatches that make them real: [do-not-flag](references/do-not-flag.md). Test files, dead code and documentation strings are out of scope unless the review targets them.
- Authenticated-only paths stay in scope: record the auth requirement in the finding.
