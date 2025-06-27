<!-- @meta {
  "fileType": "append-only",
  "subtype": "checkpointed",
  "purpose": "Record of each completed READ→ACT→WRITE cycle.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Loop Checkpoint Ledger
Append one line per successful loop including job plan reference and result.

| Loop | Timestamp (UTC) | Job Plan | Outcome |
|------|-----------------|----------|---------|
| `(example)` `40` | `2025-06-24T11:45Z` | `job_logs/temp_job.md` | `success` |

Each checkpoint verifies that the job plan executed as intended. Use this ledger to reconstruct cascade history or to locate recovery points.
