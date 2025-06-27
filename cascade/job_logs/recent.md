<!-- @meta {
  "fileType": "rolling",
  "subtype": "buffer",
  "purpose": "Stores summaries of recent job plans before archival.",
  "editPolicy": "appendOnly",
  "maxEntries": 5,
  "routeScope": "global",
  "mergeTarget": "job_logs/summary.md",
  "mergePolicy": "append"
} -->

### /cascade/job_logs/recent.md

> **Role:** Rolling window of recent `temp_job.md` summaries.
> When `maxEntries` is exceeded, the oldest entry is appended to `summary.md` and removed here.

---

#### Recent Jobs (max 5)


