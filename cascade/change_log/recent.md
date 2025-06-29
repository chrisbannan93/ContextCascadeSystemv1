<!-- @meta {
  "fileType": "rolling",
  "subtype": "buffer",
  "purpose": "A buffer for collecting summaries of recent system changes (from WRITE phases), up to 'maxEntries'. Once full, its contents are swept to the main change_log summary.",
  "editPolicy": "appendOnly",
  "routeScope": "global",
  "maxEntries": 7,
  "mergeTarget": "/cascade/change_log/summary.md"
} -->
# Recent Change Log

This file serves as a temporary buffer, collecting summaries of system changes resulting from successfully completed WRITE phases. New change summaries are appended to this file by the AI as part of the `loop_protocol.md`.

**Lifecycle:**
1.  **Collection:** Summaries of completed changes are appended here.
2.  **Capacity Check:** After each append, the system checks if the number of change summaries has reached `maxEntries` (defined in this file's metadata, e.g., 7).
3.  **Sweep Operation:** If `maxEntries` is reached:
    *   All change summaries currently in this file are read.
    *   These summaries are appended to `/cascade/change_log/summary.md`.
    *   This `recent.md` file is then cleared of these entries (e.g., overwritten with this header or an empty state) to begin collecting the next batch.

This process ensures that `recent.md` contains only a limited number of the most recent change summaries, while `summary.md` maintains the complete historical archive of all changes.

**Entry Format:**
Each appended entry should be a concise summary of a completed change, typically including:
- Change ID or reference (e.g., related Job ID, timestamp).
- Brief description of the change (e.g., "Updated `file.md`", "Executed `prune_plan.md`").
- Key files affected.
- Timestamp of the WRITE cycle.

---
*(No entries yet. This file will be populated with change summaries. Once it reaches maxEntries, its content will be moved to summary.md and this area will be cleared.)*
