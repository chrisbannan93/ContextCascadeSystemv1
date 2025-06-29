<!-- @meta {
  "fileType": "rolling",
  "subtype": "buffer",
  "purpose": "A buffer for collecting summaries of recently completed jobs, up to 'maxEntries'. Once full, its contents are swept to the main summary log.",
  "editPolicy": "appendOnly",
  "routeScope": "global",
  "maxEntries": 5,
  "mergeTarget": "/cascade/job_logs/summary.md"
} -->
# Recent Job Logs

This file serves as a temporary buffer, collecting summaries of recently executed job plans (derived from `temp_job.md` after successful completion). New job summaries are appended to this file by the AI.

**Lifecycle:**
1.  **Collection:** Summaries of completed jobs are appended here.
2.  **Capacity Check:** After each append, the system checks if the number of job summaries has reached `maxEntries` (defined in this file's metadata, e.g., 5).
3.  **Sweep Operation:** If `maxEntries` is reached:
    *   All job summaries currently in this file are read.
    *   These summaries are appended to `/cascade/job_logs/summary.md`.
    *   This `recent.md` file is then cleared of these entries (e.g., overwritten with this header or an empty state) to begin collecting the next batch.

This process ensures that `recent.md` contains only a limited number of the most recent job summaries, while `summary.md` maintains the complete historical archive.

**Entry Format:**
Each appended entry should be a concise summary of a completed job, typically including:
- Job ID (e.g., timestamp, unique hash of the plan, or sequential number).
- Stated `intent` of the job.
- Key files affected or key outcomes.
- Final `status` (e.g., success, failed, rolled_back).
- Timestamp of completion.

---
*(No job summaries yet. This file will be populated with job summaries. Once it reaches maxEntries, its content will be moved to summary.md and this area will be cleared.)*
