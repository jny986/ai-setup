---
metadata:
  version: "1.0.0"
  based_on_repo: addyosmani/agent-skills
  based_on_version: 0.6.13(aeac41d)
  based_on_skill: security-and-hardening
---

# Hardening Controls

Rules per control; a concrete implementation of each lives in [hardening-patterns.md](hardening-patterns.md). Open the section you need when you reach that code, not before.

## Injection, XSS, and access control

- Parameterize every query. Never build SQL, NoSQL, or shell commands from input strings.
- Encode output through the framework's auto-escaping. If raw HTML is unavoidable, sanitize with an allowlist sanitizer first.
- Check **authorization** on every request, not just authentication: the authenticated user must own, or be permitted on, the specific resource (A01, IDOR).

Patterns: [Injection](hardening-patterns.md#injection), [XSS](hardening-patterns.md#cross-site-scripting-xss), [Access control](hardening-patterns.md#broken-access-control).

## Authentication and sessions

- Hash passwords with bcrypt (≥12 rounds), scrypt, or argon2. The session secret comes from the environment, never from code.
- Session cookies are `httpOnly`, `secure`, and `sameSite: 'lax'` or `'strict'` (the CSRF defense; `'none'` sends the cookie on cross-site requests), with a bounded `maxAge`.

Pattern: [Authentication](hardening-patterns.md#broken-authentication).

## Headers, CORS, and responses

- Security headers on every response (helmet or the framework equivalent); CSP starts from `default-src 'self'` and is tightened, not loosened.
- CORS restricted to an explicit origin list from configuration. Never `*` with credentials.
- Strip sensitive fields (`passwordHash`, reset tokens) before any response. Error bodies are generic; internals go to server logs only.

Patterns: [Misconfiguration](hardening-patterns.md#security-misconfiguration), [Sensitive data exposure](hardening-patterns.md#sensitive-data-exposure).

## Input validation and uploads

- Validate at the boundary with a schema: allowlisted shape, lengths, enums, formats. Reject with 422 and structured details; downstream code uses only the parsed, typed value.
- Uploads: allowlist MIME types, cap size, verify content (magic bytes) when it matters. The extension proves nothing.

Patterns: [Schema validation](hardening-patterns.md#schema-validation-at-boundaries), [File upload](hardening-patterns.md#file-upload-safety).

## Server-side fetches (SSRF)

Any URL the user influences — webhooks, import-from-URL, image proxies, link previews — can be aimed at internal services. Allowlist scheme and host, resolve **all** DNS records and reject any private or reserved address (loopback, link-local `169.254.169.254`, private, unique-local, for IPv4 and IPv6), and forbid redirects. That check still has a DNS-rebinding TOCTOU gap: for high-risk surfaces, pin the resolved IP or put a filtering agent in front.

Pattern: [SSRF](hardening-patterns.md#server-side-request-forgery-ssrf).

## Destructive operations on derived paths

A delete, move, or overwrite is only as safe as the value naming its target, and trust follows who *wrote* that value, not which channel delivered it: another process's command line is as attacker-controlled as a form field. A shape check proves well-formedness, not authorization. Before the call, require all three: the resolved target (symlinks resolved) sits under an **allowlisted root**; it is at least one level **below** that root; and it carries **ownership evidence read before the operation**. On refusal, log the rejected target and stop; never fall back to a broader default path.

Why the check is weaker than it reads (marker self-attestation, check/use races): [Destructive paths](hardening-patterns.md#destructive-operations-on-derived-paths). Worked code: [security-checklist.md](security-checklist.md).

## Rate limiting

Limit the API generally and auth endpoints strictly (about 10 attempts per 15 minutes). Once more than one process serves traffic, in-memory counters silently become `max × instances`, or never fire on serverless: back the limiter with a shared store.

Pattern: [Rate limiting](hardening-patterns.md#rate-limiting).
