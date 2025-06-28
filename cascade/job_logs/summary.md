<!-- @meta {
  "fileType": "append-only",
  "purpose": "A permanent, append-only historical log of all job plan summaries, including those rolled over from job_logs/recent.md.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Job Logs Summary

This file is an append-only historical ledger of all executed job plan summaries. It includes entries merged from `/cascade/job_logs/recent.md` when that buffer reaches its `maxEntries` limit.

---
## Guidelines
- Entries are added chronologically.
- Existing entries must not be modified or deleted.
- Each entry should provide a concise summary of an executed job plan, typically including:
    - Job ID or reference to the original `temp_job.md` (e.g., its hash or timestamp).
    - The stated `intent` of the job.
    - A list of key files targeted by the job.
    - The final `status` of the job (e.g., success, failure, rolled_back).
    - Timestamp of execution.

---
*(No job summaries yet)*
