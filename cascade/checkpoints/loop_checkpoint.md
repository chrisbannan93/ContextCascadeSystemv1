<!-- @meta {
  "fileType": "append-only",
  "purpose": "Sequential log recording the successful completion of each full READ-ACT-WRITE cascade loop.",
  "editPolicy": "appendOnly",
  "routeScope": "audit"
} -->
# Loop Checkpoint Log

This file contains an append-only, sequential log that records the successful completion of each full ContextCascade loop (READ → ACT → WRITE). It serves as a crucial audit trail for system progression, rollback orchestration, and session reconstruction.

---
## Entry Format
Each entry signifies one successfully completed loop and should be recorded after all post-WRITE tasks (hash checks, confirmations, summary updates) are finished.

A structured format is recommended for each entry:

```
---
- **LoopID:** (Sequential integer or unique identifier, e.g., timestamp or global counter value)
  **Timestamp:** YYYY-MM-DDTHH:mm:ssZ (UTC)
  **JobPlanReference:** (Path or hash of the `job_logs/temp_job.md` that was executed)
  **FilesWritten:**
    - path: `/path/to/file1.md`
      hashAfter: "sha256-hash1..."
    - path: `/path/to/file2.md`
      hashAfter: "sha256-hash2..."
  **CountersIncremented:**
    - global: value_after
    - client: value_after (if client domain was affected)
    - server: value_after (if server domain was affected)
    - ... (other affected domain counters)
  **Outcome:** `success` (This file should only log successful loops. Failures are logged in `meta_audit.md`)
  **PostHashCheck:** `confirmed` | `warning` (if minor, non-critical discrepancies were noted but accepted)
---
```

---
## Usage
- **Traceability:** Provides a clear history of system operations.
- **Rollback:** Helps identify known-good states to roll back to if drift or corruption occurs.
- **Session Reconstruction:** Can assist in understanding the sequence of operations during an audit or debugging session.
- **Drift Detection:** Gaps in LoopIDs or timestamps might indicate missed cycles or system interruptions, prompting a look at `meta_audit.md`.

---
## Current Checkpoints:

*(This log is appended to by the system automatically after each successful WRITE cycle. No checkpoints yet.)*

---
## Maintenance
- This file is strictly append-only. Existing entries must never be modified or deleted.
- Ensure the LoopID is unique and preferably sequential.
- If a WRITE cycle fails or is aborted, no entry should be written here for that cycle. Failures are documented in `/cascade/audit/meta_audit.md`.
