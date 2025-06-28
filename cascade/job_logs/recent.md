<!-- @meta {
  "fileType": "rolling",
  "subtype": "buffer",
  "purpose": "A rolling log of the most recent job plan summaries, up to a defined maximum.",
  "editPolicy": "appendOnly",
  "routeScope": "global",
  "maxEntries": 5,
  "mergeTarget": "/cascade/job_logs/summary.md"
} -->
# Recent Job Logs

This file contains a rolling buffer of summaries from recently executed job plans (from `temp_job.md`). When this log exceeds `maxEntries` (5), the oldest entry is moved to `/cascade/job_logs/summary.md`.

Each entry should summarize a completed job, including:
- Job ID (could be a timestamp or a unique hash of the plan).
- Intent of the job.
- Key files affected.
- Status (e.g., success, failed, rolled_back).

---
*(No job summaries yet)*
