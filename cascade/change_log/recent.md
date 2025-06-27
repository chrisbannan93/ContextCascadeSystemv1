<!-- @meta {
  "fileType": "rolling",
  "subtype": "buffer",
  "purpose": "Stores the last 7 WRITE-cycle summaries before they are merged into the permanent change log.",
  "editPolicy": "appendOnly",
  "maxEntries": 7,
  "routeScope": "global",
  "mergeTarget": "change_log/summary.md",
  "mergePolicy": "append"
} -->

### /cascade/change_log/recent.md

> **Role:** Lightweight window into the most-recent WRITE cycles.  
> When `maxEntries` (7) is exceeded, the oldest row is copied to `summary.md` and evicted here.

---

#### Recent Loop Activity (max 7)

| Cycle | Timestamp (UTC)      | Summary of Actions / Files Written                  | Job ID |
|:----:|----------------------|------------------------------------------------------|:-----:|
| —    | —                    | _File initialised_                                   | —     |

_Newest entries are appended **on top** (reverse-chronological)._

---

#### Retention & Merge Rules

1. **Overflow Handling**  
   - Append new row → if total > 7 rows →  
     1. Copy oldest row to `/cascade/change_log/summary.md`  
     2. Remove that row from `recent.md`

2. **Trigger Points**  
   - Automatic overflow (rule above)  
   - `forceMerge: true` in a job plan  
   - Global `merge_threshold` event from `/protocols/file_lifespans.md`

3. **Enforcement**  
   - Executed by `WRITE(handle_merge_phase)`  
   - Success logged to `/audit/meta_audit.md`; failure raises `/lifecycle/drift_flag.md`

---

#### Maintenance Guidelines

- **Do not** modify existing rows; only append.  
- Use **ISO-8601 UTC** timestamps for validator compatibility.  
- Keep descriptions concise—spillover detail belongs in the job plan or archive.

---

**Summary:**  
`recent.md` offers fast visibility for debugging without loading the full archive, while automatic roll-ups keep the buffer lean and cascade-safe.
