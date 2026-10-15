---
metadata:
  version: "1.0.0"
  based_on_repo: addyosmani/agent-skills
  based_on_version: 0.6.13(aeac41d)
  based_on_skill: security-and-hardening
---

# Personal Data and Privacy

Hardening asks "can an attacker read it?" Privacy asks "should *we* hold it at all, and for how long?" The cheapest data to protect, breach, and comply over is the data you never collected; treat personal data as a liability to minimize.

- **Classify fields as you add them** (non-personal, PII, sensitive) and handle each class accordingly. You cannot protect, or honor a deletion request for, data you cannot find.
- **Collect only against a stated purpose.** "Might be useful later" is latent breach scope, not a purpose. Keep PII out of telemetry.
- **Set retention up front, then actually delete.** Every personal-data store needs a TTL and a working deletion path, including backups, caches, search indexes, and analytics copies.
- **Support the data-subject rights your jurisdiction requires** (GDPR, CCPA, and kin): export, correct, delete. Design the schema so a user's data is findable and erasable, not smeared irreversibly across systems.
- **Consent gates collection and third-party sharing, and is auditable.** Sending PII to an analytics, ad, or LLM vendor is sharing; the vendor needs a data-processing agreement. Make region a configurable policy, not a hardcoded assumption.

Classification table: [Data classification](hardening-patterns.md#data-classification). A privacy incident starts the breach-notification clock.
