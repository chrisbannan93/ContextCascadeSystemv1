<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Manifest for job-log buffers; governs retention of recent job plans and their archival into a permanent ledger.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global",
  "mergeTarget": "job_logs/summary.md",
  "maxEntries": 5
} -->
### /cascade/job_logs.md
> **Role:** Tracks every WRITE-phase job plan.
> * **`recent.md`** – rolling buffer (last 5 jobs).
> * **`summary.md`** – infinite, append-only archive.
---
#### Active Buffers
| File            | Class    | Retention (loops) | Notes                                  |
|-----------------|----------|-------------------|----------------------------------------|
| `recent.md`     | rolling  | **5**             | FIFO; overflows merge into archive     |
| `summary.md`    | archive  | ∞ (append-only)   | Permanent ledger of all executed jobs  |
---
#### Buffer Rules
**`recent.md`**
- `maxEntries`: **5** (also set in metadata).
- Overflow: oldest row copied to `summary.md`, then evicted.
- Edit policy: `appendOnly`; system controls eviction.
**`summary.md`**
- Append-only, chronological order.
- Accepts rows flushed from `recent.md`.
- Validator enforces monotonic timestamps + unique `jobId`.
---
#### Merge Triggers
1. `recent.md` exceeds **5** entries.
2. Job plan sets `forceMerge: true`.
3. Domain hits `merge_threshold` (see `/protocols/file_lifespans.md`).
---
