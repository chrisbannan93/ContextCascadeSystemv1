<!-- @meta {
  "fileType": "append-only",
  "subtype": "audit_log",
  "purpose": "A persistent log for drift, contradictions, anomalies, safeguard violations, or other significant meta-level system events.",
  "editPolicy": "appendOnly",
  "routeScope": "audit"
} -->
# Meta Audit Log

This file serves as an append-only log for critical system events, particularly those related to inconsistencies, safeguard violations, lifecycle deviations, and recovery actions. It is a key resource for debugging, understanding system behavior, and ensuring traceability.

---
## Logged Events
This log should capture events such as:
- **Drift Detection:**
    - `hashMismatch`: An `immutable` or `protected` file's hash does not match the `integrity_snapshot.md`.
    - `validatorDiff`: Schema or structural differences detected by validators.
    - `unexpectedMutation`: A file was changed without a corresponding job plan.
    - `counterSkip`: A lifecycle counter did not increment as expected.
- **Safeguard Violations:**
    - `protectedOverlap`: Attempted edit within a `<!-- PROTECTED -->` block.
    - `gateViolation`: Write attempt blocked by `/security/write_gates.md`.
    - `lockConflict`: `active_edit.lock` prevented an operation.
    - `immutableWriteAttempt`: Attempt to write to an `immutable` file without proper override.
- **Lifecycle Events:**
    - `recovery-start`: Recovery protocol initiated.
    - `recovery-step`: Specific actions taken during recovery.
    - `recovery-complete`: Recovery protocol finished.
    - `staleFilePruned`: An expired file was removed.
    - `summaryMerge`: Details of a summary merge operation.
- **Security Events:**
    - `securityReviewTriggered`: A high-risk action requiring review was initiated.
    - `permissionEscalation`: An operation required escalated privileges.
- **External Integration Events:**
    - `externalHookSent`: An external hook was triggered.
    - `externalHookFailed`: An external hook failed.

---
## Entry Format
Each entry should be clearly timestamped and structured, potentially using a consistent format (e.g., Markdown list items, YAML blocks, or JSON objects if preferred for machine parsing).

**Example Markdown List Item Format:**
```
---
- **Timestamp:** YYYY-MM-DDTHH:mm:ssZ
  **Type:** `hashMismatch`
  **Severity:** CRITICAL
  **Details:** Hash for `/cascade/system_manifest.md` does not match `integrity_snapshot.md`. Expected: `abc...`, Actual: `def...`.
  **Source:** Pre-WRITE validation (Loop ID: 157)
  **ActionTaken:** WRITE aborted. `/lifecycle/drift_flag.md` raised.
---
- **Timestamp:** YYYY-MM-DDTHH:mm:ssZ
  **Type:** `recovery-start`
  **Severity:** INFO
  **Details:** Recovery protocol initiated due to `drift_flag.md`.
  **Source:** System Recovery Agent
---
```

---
## Current Audit Log:

*(This log is appended to by the system as events occur. No entries yet.)*

---
## Maintenance
- This file is append-only. Existing entries must not be altered.
- Ensure consistent formatting for entries to aid parsing and review.
- Regularly review this log for patterns or recurring issues.
- For very high-volume systems, consider log rotation strategies if file size becomes an issue, though the primary intent is a persistent, complete record.
