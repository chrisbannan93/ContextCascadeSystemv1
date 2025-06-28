<!-- @meta {
  "fileType": "permanent",
  "purpose": "Defines glob patterns and path constraints to control which files can be written to. Acts as a write-time firewall.",
  "editPolicy": "appendOrReplace",
  "routeScope": "security"
} -->
# Write Gates Policy

This file defines the write gate policies for the ContextCascade system. It uses glob patterns and explicit path declarations to allow or deny write operations to specific files or directories. This acts as a crucial safeguard to prevent unintended or unauthorized modifications.

---
## Gate Configuration Format
Write gates are typically defined in a structured format, often YAML-like, within this document. The system will parse this section to enforce rules during the pre-WRITE validation phase.

**Key Principles:**
- **Deny by Default (Recommended):** It's often safer to deny writes to broad areas and then explicitly allow specific paths.
- **Specificity:** More specific rules usually override broader ones (though the exact precedence logic depends on the validator's implementation).
- **`allow` vs. `deny`:** Clearly state the intent.
- **`appendOnly` flag:** Can be used to allow writes but only in append mode for certain paths.

---
## Example Gate Configuration:
```yaml
writeGates:
  # Deny writes to all protocol files by default
  - deny: "/cascade/protocols/*"
  # But allow appendOrReplace to file_lifespans if specifically planned
  - allow: "/cascade/protocols/file_lifespans.md"
    editPolicy: "appendOrReplace" # Explicitly state allowed edit type

  # Immutable files - generally deny all direct writes
  - deny: "/cascade/00_BOOTSTRAP.md"
  - deny: "/cascade/system_manifest.md"
  - deny: "/cascade/init_context.md"
  # (Overrides for immutable files should be exceptional and logged via security_review.md)

  # Allow writes to job logs (temp_job is overwrite, others appendOnly)
  - allow: "/cascade/job_logs/temp_job.md"
    editPolicy: "overwrite"
  - allow: "/cascade/job_logs/recent.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/job_logs/summary.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/job_logs.md" # The index file
    editPolicy: "appendOrReplace"


  # Allow writes to change logs (recent is appendOnly, summary is appendOnly)
  - allow: "/cascade/change_log/recent.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/change_log/summary.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/change_log.md" # The index file
    editPolicy: "appendOrReplace"

  # Lifecycle counters are incrementOnly (a form of append)
  - allow: "/cascade/lifecycle/*.md" # Individual counters
    editPolicy: "incrementOnly" # Or appendOnly if incrementOnly is not a direct metadata policy
  - allow: "/cascade/lifecycle.md" # The index file
    editPolicy: "appendOrReplace"


  # Load plans are evictable and can be overwritten
  - allow: "/cascade/load_plans/*.md"
    editPolicy: "overwrite"

  # Taskbuffers are temporary and can be overwritten
  - allow: "/cascade/_taskbuffers/*.md"
    editPolicy: "overwrite"

  # Temp notes are rolling and can be appended to or sections replaced
  - allow: "/cascade/temp_notes/*.md"
    editPolicy: "appendOrReplace"

  # Audit files are generally append-only or managed by specific processes
  - allow: "/cascade/audit/meta_audit.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/audit/token_summary.md" # May be overwritten by analysis tools
    editPolicy: "overwrite"
  - allow: "/cascade/audit/integrity_snapshot.md" # Usually appendOnly, or specific update process
    editPolicy: "appendOnly"
  - allow: "/cascade/audit/prune_plan.md" # Evictable, can be overwritten
    editPolicy: "overwrite"


  # Checkpoints are append-only
  - allow: "/cascade/checkpoints/loop_checkpoint.md"
    editPolicy: "appendOnly"

  # Domain files - index files are often appendOnly or appendOrReplace
  # Content files within domains might have varying policies
  - allow: "/cascade/domains/*/index.md"
    editPolicy: "appendOrReplace"
  - allow: "/cascade/domains/*/*.md" # Be more specific for actual domain content files
    editPolicy: "appendOrReplace" # Default, can be overridden by file's own metadata

  # Security files themselves
  - allow: "/cascade/security/security_review.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/security/write_gates.md" # This file itself
    editPolicy: "appendOrReplace" # Needs to be editable, but with high review threshold

  # Meta files
  - allow: "/cascade/_meta/*.md"
    editPolicy: "appendOrReplace" # e.g., for cascade_feature_index.md

  # Deny everything else within /cascade/ by default if not explicitly allowed
  # This is a strong safeguard but requires diligent 'allow' rules.
  # - deny: "/cascade/**" (Use with caution and ensure all legitimate paths are allowed above)

```
---
## Current Gate Configuration:

# (Define your YAML or structured list of rules here)
# Example:
writeGates:
  - deny: "/cascade/protocols/*"
  - allow: "/cascade/protocols/file_lifespans.md"
    editPolicy: "appendOrReplace"
  - deny: "/cascade/00_BOOTSTRAP.md"
  - deny: "/cascade/system_manifest.md"
  - deny: "/cascade/init_context.md"
  - allow: "/cascade/job_logs/temp_job.md"
    editPolicy: "overwrite"
  - allow: "/cascade/job_logs/*.md" # recent.md, summary.md, job_logs.md (index)
    editPolicy: "appendOnly" # Default, specific files can refine
  - allow: "/cascade/change_log/*.md" # recent.md, summary.md, change_log.md (index)
    editPolicy: "appendOnly" # Default
  - allow: "/cascade/lifecycle/*.md"
  - allow: "/cascade/lifecycle.md"
    editPolicy: "appendOrReplace"
  - allow: "/cascade/load_plans/*.md"
    editPolicy: "overwrite"
  - allow: "/cascade/_taskbuffers/*.md"
    editPolicy: "overwrite"
  - allow: "/cascade/temp_notes/*.md"
    editPolicy: "appendOrReplace"
  - allow: "/cascade/audit/meta_audit.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/audit/token_summary.md"
    editPolicy: "overwrite"
  - allow: "/cascade/audit/integrity_snapshot.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/audit/prune_plan.md"
    editPolicy: "overwrite"
  - allow: "/cascade/checkpoints/loop_checkpoint.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/domains/**" # Broad allow for domains, individual files should have stricter policies
    editPolicy: "appendOrReplace"
  - allow: "/cascade/security/security_review.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/security/write_gates.md" # This file
    editPolicy: "appendOrReplace"
  - allow: "/cascade/_meta/*.md"
    editPolicy: "appendOrReplace"
  - allow: "/cascade/index.md"
    editPolicy: "appendOnly"

---
## Maintenance
- Changes to this file are considered high-risk and **must** be logged in `/cascade/security/security_review.md`.
- Regularly audit these gates against the actual file structure and intended edit policies.
- Ensure the parsing logic in the AI agent or validator correctly interprets these rules.
