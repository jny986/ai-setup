---
name: harden-deployment
description: "Secure how code ships and runs: Dockerfiles, CI/CD pipelines, cloud and IAM config, secrets in the environment, dependencies and supply chain."
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: getsentry/skills, addyosmani/agent-skills, affaan-m/ECC
  based_on_version: main(d18b7aa), 0.6.13(aeac41d), v2.2.3-889-gb92f181b(b92f181b)
  based_on_skill: security-review, security-and-hardening, security-review
---

Secure the path from commit to running service. Work the sections that match the task.

## Steps

1. **Pick the surface.**

   | Surface | Read |
   |---|---|
   | Dockerfile, image | [docker](references/infrastructure/docker.md) |
   | IAM, MFA, network, logging, backups, CDN | [cloud](references/infrastructure/cloud.md) |
   | CI/CD pipeline | [cloud](references/infrastructure/cloud.md#5-cicd-pipeline-security) and [supply-chain](references/supply-chain.md) |
   | Dependencies, lockfile, audit findings | Step 2; depth in [dependencies](references/dependencies.md) |
   | Secrets | Step 3 |

2. **Dependencies.**
   1. Find the manager and lockfile that own the install; stop if they disagree or two lockfiles compete.
   2. Block install scripts before first run, approve the minimum, then verify with a clean frozen install ([install-script gate](references/security-checklist.md#install-script-gate)).
   3. Run the native audit on the committed lockfile and triage by reachability ([audit triage](references/hardening-patterns.md#dependency-audit-triage)). Preview forced fixes (`npm audit fix --force`) and test each upgrade before applying.
   4. Review every new dependency and lockfile diff for ownership, release age and provenance: audits only match known advisories, so a typosquat passes.

3. **Secrets.** They come from the environment or a cloud secrets manager; `.env.example` carries placeholders; real `.env*` files are gitignored; grep the staged diff before each commit. A secret that reached a remote is compromised: **rotate it first**, then purge history. See [secrets management](references/hardening-patterns.md#secrets-management).

4. **Verify.** Done when the surface's own checklist is fully ticked and `security release-gate` passes. Check the change against the [red flags](references/red-flags.md).
