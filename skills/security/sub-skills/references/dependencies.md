---
metadata:
  version: "1.0.0"
  based_on_repo: addyosmani/agent-skills
  based_on_version: 0.6.13(aeac41d)
  based_on_skill: security-and-hardening
---

# Dependencies and Supply Chain

1. **Find the installation boundary and manager.** Use the workspace root that owns the lockfile, or an independent nested project only when it is outside that workspace. Corroborate `packageManager` (when present), the lockfile, and CI; stop on disagreement or competing lockfiles. Pin the manager version.
2. **Block dependency scripts before first execution.** Bootstrap with scripts disabled or a documented fail-closed policy, inspect the pending script source, approve only the minimum, commit the policy, then verify with a clean frozen/immutable install. Never blanket-approve.
3. **Run the native audit against the committed lockfile before every release.** Triage critical/high by **reachability** (runtime, build, test, deploy paths) and fix availability. Never apply forced remediation (`npm audit fix --force` or equivalent) automatically, since forced fixes may cross declared dependency ranges; preview, read changelogs, test each upgrade. Document every deferral with a reason and a review date.
4. **Audits only match known advisories.** They do not catch a newly malicious or typosquatted package (`cross-env` vs `crossenv`). Review new dependencies, lockfile diffs, and script-policy changes together: ownership, maintenance, release age, provenance, transitive graph. Verify registry signatures where supported (`npm audit signatures`, `pnpm audit signatures`) and treat their absence as a signal to investigate, not automatic proof of compromise (A06, LLM03).

Triage decision tree: [Dependency audit triage](hardening-patterns.md#dependency-audit-triage). Manager matrix and install-script gate: [security-checklist.md](security-checklist.md).
