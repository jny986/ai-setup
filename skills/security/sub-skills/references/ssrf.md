---
metadata:
  version: "1.0.0"
  based_on_repo: getsentry/skills
  based_on_version: main(d18b7aa)
  based_on_skill: security-review
---

# Server-Side Request Forgery (SSRF) Prevention Reference

## Overview

SSRF vulnerabilities allow attackers to induce the server-side application to make HTTP requests to an arbitrary domain of the attacker's choosing. This can be used to:

- Access internal services not exposed to the internet
- Read cloud metadata (AWS, GCP, Azure credentials)
- Scan internal networks
- Bypass firewalls and access controls
- Exploit internal services with known vulnerabilities

## Attack Scenarios

### Cloud Metadata Access (AWS)

```bash
# Attacker provides URL:
http://169.254.169.254/latest/meta-data/iam/security-credentials/role-name

# Server fetches and returns AWS credentials:
{
  "AccessKeyId": "ASIA...",
  "SecretAccessKey": "...",
  "Token": "..."
}
```

### Internal Service Access

```bash
# Attacker provides URL:
http://localhost:8080/admin/delete-all
http://internal-service.local/sensitive-data

# Server makes request to internal service that trusts localhost
```

### Port Scanning

```bash
# Attacker probes internal network:
http://192.168.1.1:22    # SSH
http://192.168.1.1:3306  # MySQL
http://192.168.1.1:6379  # Redis
```

---

## Prevention Strategies

### 1. Limit destinations

Prefer a fixed set of service endpoints over accepting arbitrary URLs. When the destination must be selected, parse with the same URL semantics used by the HTTP client and enforce an exact scheme, normalized hostname and port allowlist. Reject userinfo, malformed or ambiguous URLs and unsupported schemes. Hostname checks alone do not stop redirects, DNS rebinding or an allowed service that proxies to another destination.

When arbitrary external destinations are required, enforce a network egress policy that denies internal, loopback, link-local, private, multicast, reserved and metadata destinations for both IPv4 and IPv6, including IPv4-mapped IPv6. Apply the policy at the actual connection, not just to a separately resolved hostname. Use a maintained address classification and account for deployment-specific internal ranges; a static list of RFC1918 addresses is not exhaustive.

### 2. Bind validation to the connection

Resolve all A and AAAA answers with a trusted resolver and reject disallowed addresses. Connect only to a validated address using a client or egress proxy that pins the selected address for that connection. Preserve the original hostname for TLS certificate verification, SNI and the HTTP Host header. A normal second DNS lookup at request time reopens a rebinding window; replacing the hostname with an IP and setting only `Host` does not preserve TLS hostname verification. Ensure proxy settings, connection pooling and retries cannot bypass the policy or select a different unvalidated address. Prefer a vetted egress proxy or transport with these guarantees to custom URL rewriting.

### 3. Handle redirects and metadata

Disable automatic redirects. If redirects are necessary, resolve each `Location` against the current URL, limit hops, and repeat the entire URL, destination, DNS and connection policy for every hop before connecting. Never forward credentials to a different origin without explicit authorization. Apply reasonable connect/read timeouts and response size limits.

Deny cloud metadata and internal service access at the network layer, including alternate metadata addresses and DNS names. AWS IMDSv2 is defense in depth, not a substitute for blocking SSRF: some vulnerable request primitives can issue the required method and headers. URL substring tests do not enforce destination policy.

### 4. Parser and address bypasses

Test IPv4, IPv6, IPv4-mapped IPv6, loopback, link-local, private, multicast and reserved ranges, plus alternate numeric and encoded forms that the actual HTTP client accepts. Reject ambiguous forms rather than blindly percent-decoding an entire URL: decoding can change its structure. Test mixed public/private DNS answers, DNS changes between validation and connection, redirects to private addresses, proxies, and retries. Validate the destination actually contacted while retaining TLS verification for its hostname.

---

## Grep Patterns for Detection

```bash
# URL fetching functions
grep -rn "requests\.get\|requests\.post\|urllib\.request\|urlopen\|fetch\|axios" --include="*.py" --include="*.js"

# URL from user input
grep -rn "request\.args\|request\.form\|request\.json\|req\.query\|req\.body" --include="*.py" --include="*.js" | grep -i "url"

# Potential SSRF sinks
grep -rn "curl_exec\|file_get_contents\|fopen\|readfile" --include="*.php"

# Missing validation
grep -rn "requests\.get(url\|fetch(url" --include="*.py" --include="*.js"
```

---

## Testing Checklist

- [ ] User-controlled URLs validated against allowlist
- [ ] Non-public and deployment-specific destinations blocked at the actual connection
- [ ] Cloud metadata IPs blocked (169.254.169.254 and alternate metadata addresses)
- [ ] IPv6 internal addresses blocked
- [ ] URL redirects not followed blindly
- [ ] All DNS answers validated and the connection pinned to an allowed address, with hostname TLS verification and proxy behavior checked
- [ ] URL encoding/alternate representations handled
- [ ] IMDSv2 required (AWS environments)
- [ ] Timeouts configured to prevent DoS

---

## References

- [OWASP SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
- [CWE-918: Server-Side Request Forgery](https://cwe.mitre.org/data/definitions/918.html)
- [AWS IMDSv2 Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)
- [PortSwigger SSRF Guide](https://portswigger.net/web-security/ssrf)
