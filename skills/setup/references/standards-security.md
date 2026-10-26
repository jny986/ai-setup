---
metadata:
  version: "1.0.0"
  based_on_repo: spatie/guidelines-skills
  based_on_version: 1.1.0(eca8f60)
  based_on_skill: spatie-security
---

# Security Standards

## Passwords
- Store all passwords in a password manager.
- Ensure each password is unique; no reuse.
- Enable two-factor authentication on the password manager and other accounts when available.

## GitHub
- Sign all commits.
- Follow [GitHub's commit-signing instructions](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits).

## Application Security
- Transmit all HTTP traffic over SSL.
- Use CSRF tokens in all forms.
- Use appropriate HTTP methods for significant actions: `DELETE`, `POST`, `PUT` — never `GET`.
- Add automated authorization tests to verify only authorized users can access restricted functionality.

## Database Security
- Hash all stored passwords.
- Encrypt API keys stored in databases.
- Use separate database users per database with appropriate read/write permissions.
- Restrict database access to whitelisted hosts only (webserver and developer machines).

## Server Security
- Keep NGINX, PHP, Ubuntu, and similar software up to date.
- Use SSH with private key authentication; disable password authentication.
- Install and enable `unattended-upgrades` for automatic security updates.
- Configure firewalls to permit only necessary traffic (typically ports 22 and 443).
- Manage servers through configuration management or infrastructure-as-code for rapid patching and access revocation.

## General
- Use off-site backups and test restores periodically.
- Protect all private keys with passwords.
- Enable full-disk encryption on all developer devices.
- Never use public searchable services such as public pastebins or gists for sensitive code or data.
- Never install pirated software on a computer or phone.
- Install browser extensions only from official browser stores, keep them to a minimum, and account for ownership changes or malicious takeovers.
- Never use browser extensions that can track typed keys, passwords, or browser history.
