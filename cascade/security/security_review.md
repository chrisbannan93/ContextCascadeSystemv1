<!-- @meta {
  "fileType": "append-only",
  "purpose": "Log of manual or AI-driven security reviews, findings, and approvals for high-risk actions.",
  "editPolicy": "appendOnly",
  "routeScope": "security"
} -->
# Security Review Log

This file contains an append-only log of all security reviews conducted. This includes reviews for:
- High-risk actions flagged with `requiresReview: true` in job plans.
- Modifications to critical system files (e.g., `system_manifest.md`, protocol files).
- Escalated permissions or overrides of `readonly`, `immutable`, or `protected` policies.
- Findings from manual or automated security audits.
- Approvals or rejections of proposed changes.

---
## Entry Format
Each entry should be clearly timestamped and include:
- **Date/Timestamp:** When the review was conducted.
- **Reviewer(s):** Who conducted the review (human agent ID or AI agent version).
- **Subject:** What was reviewed (e.g., Job Plan ID, file path, proposed change).
- **Details/Findings:** A summary of the review process and any findings.
- **Decision/Outcome:** Approved, Rejected, Needs More Info, etc.
- **Rationale:** Justification for the decision.
- **Associated Hashes:** (If applicable) Hashes of files before and after an approved change.

---
## Example Entry:
```
---
**Date/Timestamp:** 2025-07-15T10:30:00Z
**Reviewer(s):** human_admin_chris, ai_agent_jules_v1.2
**Subject:** Proposed modification to `/cascade/system_manifest.md` (Job Plan: job_temp_a1b2c3d4)
**Details/Findings:**
- Intent: Add new domain 'experimental_features'.
- Impact assessment: Low risk, isolated domain.
- Hash before: manifest_hash_v1_old
- Hash after (proposed): manifest_hash_v2_new
**Decision/Outcome:** Approved
**Rationale:** The new domain is well-defined and does not interfere with existing core domains. All necessary index files for the domain are included in the job plan.
**Associated Hashes:**
- `/cascade/system_manifest.md` (before): sha256-abc...
- `/cascade/system_manifest.md` (after): sha256-def...
---
```

---
*(No review entries yet)*
