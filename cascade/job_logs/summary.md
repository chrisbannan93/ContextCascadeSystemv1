<!-- @meta {
  "fileType": "append-only",
  "purpose": "A permanent, append-only historical log of all job plan summaries. It receives batches of summaries from the 'recent.md' buffer.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Job Logs Summary

This file is an append-only historical ledger of all executed job plan summaries. Its primary role is to serve as a long-term archive.

It receives **batches of job summaries** that are "swept" from `/cascade/job_logs/recent.md` when that buffer reaches its `maxEntries` capacity. This ensures that `summary.md` grows chronologically with sets of recent activities.

---
## Guidelines
- Entries (which are typically batches of summaries from `recent.md`) are appended chronologically.
- Existing content in this file must not be modified or deleted to maintain historical integrity.
- Each job summary within a batch should provide a concise record of an executed job plan, typically including:
    - Job ID (e.g., timestamp, unique hash of the plan, or sequential number).
    - The stated `intent` of the job.
    - Key files affected or key outcomes.
    - The final `status` of the job (e.g., success, failure, rolled_back).
    - Timestamp of completion.

---
*(No job summaries yet. This file will be populated with batches of job summaries swept from /cascade/job_logs/recent.md.)*
