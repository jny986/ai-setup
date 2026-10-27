---
metadata:
  version: "1.0.0"
  based_on_repo: affaan-m/ECC, claude-dev-suite/claude-dev-suite
  based_on_version: v2.2.3-889-gb92f181b(b92f181b), v1.19.0-17-ge10ab64(e10ab64)
  based_on_skill: laravel-security, php-security
  based_on_url: "https://www.php.net/manual/en/pdo.prepare.php (2026-10-27), https://www.php.net/manual/en/function.escapeshellarg.php (2026-10-27), https://www.php.net/manual/en/function.htmlspecialchars.php (2026-10-27), https://www.php.net/manual/en/function.unserialize.php (2026-10-27), https://www.php.net/manual/en/wrappers.php (2026-10-27), https://www.php.net/manual/en/features.file-upload.php (2026-10-27), https://www.php.net/manual/en/session.security.ini.php (2026-10-27), https://www.php.net/manual/en/function.password-hash.php (2026-10-27), https://www.php.net/manual/en/function.password-verify.php (2026-10-27), https://www.php.net/manual/en/function.random-bytes.php (2026-10-27), https://www.php.net/manual/en/language.operators.comparison.php (2026-10-27), https://www.php.net/manual/en/function.hash-equals.php (2026-10-27), https://laravel.com/docs/13.x/queries (2026-10-27), https://laravel.com/docs/13.x/blade (2026-10-27), https://laravel.com/docs/13.x/eloquent (2026-10-27), https://laravel.com/docs/13.x/validation (2026-10-27), https://laravel.com/docs/13.x/authorization (2026-10-27), https://laravel.com/docs/13.x/sanctum (2026-10-27), https://laravel.com/docs/13.x/authentication (2026-10-27), https://laravel.com/docs/13.x/csrf (2026-10-27), https://laravel.com/docs/13.x/filesystem (2026-10-27), https://laravel.com/docs/13.x/http-client (2026-10-27)"
---

# PHP Security Patterns

Use for core PHP and Laravel review or implementation. Dedicated Symfony and WordPress coverage is outside this reference.

## Establish context

- Detect PHP and package versions from the deployed runtime and Composer files. A Composer constraint describes allowed versions; the lock file records resolved packages. Record uncertainty when the deployed version is unavailable.
- Detect Laravel through `laravel/framework`, `artisan`, routes, Blade templates and Eloquent models. Inspect the application's middleware, policies, validation and model configuration before judging a call site.
- Trace request data, cookies, headers, uploads and attacker-written stored data to the sensitive operation. Configuration is trusted only while its values and any appended components remain server-controlled. Authentication does not remove authenticated attackers from scope.
- In review, use the parent workflow's finding criteria: identify the attacker, reachable operation, missing protection and impact. API names and search matches are leads. In builds, pair each relevant control below with an abuse case and a safe-path check.

The PHP manual and Laravel 13 documentation below were checked on 2026-10-27. Use documentation matching the target project's versions before copying version-sensitive APIs or configuration. General review and reporting rules remain in the parent workflow.

## SQL and command injection

### Queries

Bind values; map user-selected columns, tables and sort directions to fixed allowlists. [PDO placeholders](https://www.php.net/manual/en/pdo.prepare.php) represent values, not identifiers or arbitrary SQL fragments.

```php
// Vulnerable when the request value reaches SQL without a restricting control.
$pdo->query("SELECT * FROM users WHERE email = '" . $_GET['email'] . "'");

// Parameterized value; validate the request's type separately.
$stmt = $pdo->prepare('SELECT * FROM users WHERE email = :email');
$stmt->execute(['email' => $email]);

// Laravel: both bind the value, including the raw query with bindings.
User::where('email', $email)->first();
User::whereRaw('email = ?', [$email])->first();
```

For Laravel, investigate interpolated `DB::select`, `DB::statement`, `whereRaw`, `orderByRaw` and `DB::raw` expressions. A raw expression with fixed SQL and correctly bound values is not SQL injection. The [query builder](https://laravel.com/docs/13.x/queries) cannot make an attacker-selected SQL fragment safe merely by wrapping it in an ORM call. Parameterization also leaves resource authorization to the application.

### Processes and code execution

Investigate attacker-influenced `exec`, `shell_exec`, `system`, `passthru`, backticks, `proc_open` and `eval`. Prefer PHP filesystem APIs or a fixed executable with an argument-array API supported by the target runtime. Validate each argument for the operation, including option-like values.

[`escapeshellarg`](https://www.php.net/manual/en/function.escapeshellarg.php) quotes a shell argument; it does not authorize its meaning or prevent the called program from interpreting it as an option. A fixed command with constant arguments is not command injection. For source-to-sink checks, read [injection](../injection.md).

## Output escaping and templates

For ordinary HTML text and quoted attributes, encode at output with [`htmlspecialchars`](https://www.php.net/manual/en/function.htmlspecialchars.php), using `ENT_QUOTES | ENT_SUBSTITUTE` and the application's encoding, usually UTF-8. URL schemes, JavaScript and CSS need controls for their own contexts; HTML encoding alone does not validate them.

```php
// Vulnerable HTML text output when name contains attacker-supplied markup.
echo '<p>' . $_GET['name'] . '</p>';

// HTML text output, assuming name is a validated string.
echo '<p>' . htmlspecialchars($name, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') . '</p>';
```

[Blade](https://laravel.com/docs/13.x/blade) escapes `{{ $value }}`. Investigate `{!! $value !!}`, custom HTML-safe objects and attacker-controlled template source. Raw output requires trusted HTML or a maintained sanitizer configured for the permitted markup and URL schemes. For JavaScript data embedded in HTML, use `Illuminate\Support\Js::from($data)` where supported. Check the destination context before calling a pattern safe. See [XSS](../xss.md) for sanitization and URL controls.

## Deserialization

[`unserialize`](https://www.php.net/manual/en/function.unserialize.php) is unsuitable for untrusted bytes, including attacker-written cache or database values. Its `allowed_classes` option does not make untrusted deserialization safe. Prefer `json_decode` with `JSON_THROW_ON_ERROR`, then validate structure, types and size.

Trace who can write the bytes and which classes or magic methods can execute; report the demonstrated impact rather than assigning every use an automatic RCE severity. A constant or integrity-protected server-generated payload needs a different assessment from request bytes. For formats, integrity and gadget-chain analysis, read [deserialization](../deserialization.md).

## Files, includes and uploads

Investigate attacker-influenced `include`, `require`, `fopen`, `file_get_contents`, `readfile`, `unlink` and storage paths. [PHP stream wrappers](https://www.php.net/manual/en/wrappers.php) can change the operation from a local read to another resource type. Check available wrappers and runtime configuration before claiming exploitability.

- For a finite set of files or templates, map a public identifier to a server-owned path. For dynamic local paths, enforce containment under the intended directory after canonicalization; account for separators, symlinks and nonexistent destinations. `basename` alone does not establish authorization or safe storage.
- For [uploads](https://www.php.net/manual/en/features.file-upload.php), check upload errors, size and content-derived type. Treat client filenames, extensions and MIME headers as untrusted. Use a generated filename, an allowed extension consistent with the accepted content, and non-executable storage. MIME detection alone does not prove harmless content.
- In Laravel, combine appropriate [file validation](https://laravel.com/docs/13.x/validation) with [storage visibility and access controls](https://laravel.com/docs/13.x/filesystem). Authorize the owning resource before a download or temporary URL is issued. A signed URL establishes integrity and expiry, not the requester's right to obtain it.

For traversal, destructive operations, race conditions and upload-serving controls, read [file security](../file-security.md).

## Server-side URL fetching

Trace URLs reaching cURL, URL-capable streams or Laravel's [HTTP client](https://laravel.com/docs/13.x/http-client). URL syntax validation and an `http`/`https` scheme check do not restrict destinations. For user-selected destinations, enforce allowed hosts and ports, reject internal and metadata addresses, account for DNS resolution, and disable redirects or validate every destination. Apply timeouts and response-size limits. Read [SSRF](../ssrf.md) for the full control design.

An operator-configured URL with no attacker-influenced components is not an SSRF finding. Recheck that assumption when a request value changes the host, path interpretation or redirect target. In Laravel tests, use HTTP fakes and `Http::preventStrayRequests()` where supported to keep abuse cases from making real network calls.

## Authentication, sessions and CSRF

For core PHP, configure [session protections](https://www.php.net/manual/en/session.security.ini.php) before starting sessions: strict session IDs, HTTPS-only and HttpOnly cookies, and a SameSite policy appropriate to the flow. Rotate the session ID after authentication or privilege changes. Inspect existing authentication code before concluding rotation is absent.

Use [`password_hash`](https://www.php.net/manual/en/function.password-hash.php) and [`password_verify`](https://www.php.net/manual/en/function.password-verify.php), or Laravel's hashing service, with a supported password-hashing algorithm. Generate security tokens with [`random_bytes`](https://www.php.net/manual/en/function.random-bytes.php) or the framework's secure equivalent. MD5 password hashes and predictable reset tokens require tracing to an actual authentication or recovery path; checksum uses have different requirements.

For [Laravel authentication](https://laravel.com/docs/13.x/authentication), verify effective guards, login throttling and session lifecycle. After custom session login, regenerate the session; on logout, log out the guard, invalidate the session and regenerate the CSRF token. Existing starter kits or authentication packages may already provide these controls.

For cookie-authenticated state changes, inspect [request-forgery middleware](https://laravel.com/docs/13.x/csrf), route coverage and exclusions. Use `@csrf` in forms when token validation applies. Laravel 13 also supports origin verification, so a missing token alone does not establish a bypass. Check the target version and effective mode. Stateless bearer-only endpoints and signature-verified webhooks have different protections; confirm they cannot fall back to ambient cookie authentication before dismissing CSRF. See [authentication](../authentication.md) and [CSRF](../csrf.md).

## Authorization and mass assignment

### Resource access

Trace each action through [Laravel policies, gates and authorization middleware](https://laravel.com/docs/13.x/authorization). Route-model binding and an `exists` validation rule establish resource existence, not permission. An ownership-scoped query can enforce access when the scope matches the action's policy; inspect tenant boundaries and alternate paths too.

```php
// A policy registered for this model must enforce the action's access rules.
$order = Order::findOrFail($id);
Gate::authorize('view', $order);
return $order;
```

For [Sanctum](https://laravel.com/docs/13.x/sanctum), check authentication, token abilities and resource policy separately. `tokenCan` returns true for first-party SPA requests authenticated through Sanctum's SPA mode; it cannot replace ownership or action authorization. A Blade `@can` check hides UI but needs corresponding server-side enforcement. Read [authorization](../authorization.md) for IDOR and privilege checks.

### Writable fields

Inspect [Eloquent mass-assignment controls](https://laravel.com/docs/13.x/eloquent) and the exact array reaching `create`, `fill` or `update`. Check `$fillable`, `$guarded`, unguarding and force-fill operations; newer versions also support model attributes for these settings. An unguarded model is not itself a finding when callers construct only authorized fields.

For builds, construct an action-specific allowlist from validated input and assign privileged fields from trusted server decisions. Validation is not field authorization: a well-formed `is_admin` value can still be forbidden. Model casts change representation, not permission. A `$request->all()` call needs the model's effective protections traced before it becomes a mass-assignment finding.

```php
// Assumes authentication and an action-specific FormRequest have run.
// Rules validate name/email; the model allows these fields to be assigned.
$data = $request->safe()->only(['name', 'email']);
$user = new User($data);
$user->account_id = $request->user()->account_id; // Server-selected tenant.
$user->save();
```

For nested arrays, define allowed keys and validate the members actually consumed. Laravel [validation](https://laravel.com/docs/13.x/validation) does not automatically establish ownership or make every nested key safe to persist. See [business logic](../business-logic.md) for workflow constraints.

## Security-sensitive comparisons

[Loose comparisons](https://www.php.net/manual/en/language.operators.comparison.php) coerce types. PHP 8 changed some number/string comparisons, but numeric-string comparisons still need care. Verify a proposed type-juggling bypass against the target runtime and actual input types.

- Use `===`/`!==` for typed identifiers and strict membership checks such as `in_array($role, $allowedRoles, true)` after validation.
- For secrets or MACs, validate string input and use [`hash_equals($known, $supplied)`](https://www.php.net/manual/en/function.hash-equals.php), with the trusted value first. Passwords use the password-verification API.
- Require a reachable security decision and a demonstrated bypass before reporting a comparison as a vulnerability.

## Verification cases

Use the project's existing request or integration test seam. These cases guide review and builds; they do not require a new PHP application or mandatory scanner dependency.

| Branch | Abuse case | Protected case |
|---|---|---|
| SQL | Request string changes a concatenated query | Bound value remains data, including in `whereRaw` with bindings |
| HTML | Attacker markup reaches raw Blade output | Ordinary Blade text interpolation escapes markup |
| Authorization | User A requests user B's private resource | Effective policy or scoped query denies the action |
| Writable fields | Request adds `is_admin` or another tenant ID | Authorized field allowlist excludes it; tenant is server-selected |
| Deserialization | Request bytes reach `unserialize`, even with a class allowlist | JSON is decoded and its consumed fields validated |
| File/URL input | Traversal, executable upload or internal URL reaches its sink | Path containment, safe serving and destination restrictions stop the relevant abuse |
| Sessions | A session fixed before login survives authentication | Existing auth flow rotates it; logout invalidates it |
| Comparisons | Input coercion bypasses a token or role check | Validated types and the appropriate comparison reject it |

For each suspected flaw, check middleware and callers before deciding the protected case is absent. Run abuse cases in isolation with fake credentials and mocked external services. When evidence is incomplete, use the parent workflow's needs-verification bucket.

## Scope and sources

Adapted selectively from ECC's `laravel-security` and claude-dev-suite's `php-security`, pinned in the metadata. Official PHP and Laravel documentation linked beside each rule resolves version-sensitive claims. This reference covers PHP-specific controls; deployment, Composer supply chain, headers and infrastructure use [supply chain](../supply-chain.md), [misconfiguration](../misconfiguration.md) and the `security harden-deployment` workflow.
