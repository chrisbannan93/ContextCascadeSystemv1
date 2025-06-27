<!-- @meta {
  "fileType": "policy",
  "subtype": "writeGate",
  "purpose": "Path-level allow/deny rules enforced before every WRITE commit.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global",
  "linkedAudits": ["security/security_review.md", "audit/meta_audit.md"]
} -->

### /cascade/security/write_gates.md

> **Role:** A WRITE-time firewall.  
> Every planned file mutation is checked against these rules by `validate_write_gates.ts`.  
> The first matching rule wins (`allow` > `deny`).

---

#### Gate Rules

```yaml
writeGates:
  # ---------- ALLOW ----------
  - allow: "job_logs/**"                  # temp_job, recent, summary
  - allow: "change_log/**"
  - allow: "lifecycle/**/*.md"
  - allow: "security/security_review.md"  # append-only audit rows
  - allow: "security/write_gates.md"      # self-updates via job plan
  - allow: "audit/**"                     # meta_audit, integrity snapshots
  - allow: "drafts/**"                    # developer scratch docs
  - allow: "temp_notes/**"

  # ---------- DENY ----------
  - deny: "system_manifest.md"            # immutable doctrine
  - deny: "protocols/loop_protocol.md"    # core loop logic
  - deny: "protocols/file_lifespans.md"   # threshold policy – needs review flag
  - deny: "immutable/**"                  # any immutable subtree
  - deny: "_locks/**"                     # lockfile integrity
  - deny: "external/**"                   # integration adapters
