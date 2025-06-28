<!-- @meta {
  "fileType": "policy",
  "subtype": "index",
  "purpose": "Manifest for change-log buffers; governs rolling retention (recent.md) and archival persistence (summary.md).",
  "editPolicy": "appendOrReplace",
  "routeScope": "global",
  "mergeTarget": "change_log/summary.md",
  "maxEntries": 7
} -->
### /cascade/change_log.md
> **Role:** Describes how the cascade records recent WRITE-phase activity while preserving a permanent audit trail. It links two sibling buffers:
> * **`recent.md`** – short-window rolling log (token-lean)
> * **`summary.md`** – permanent append-only archive
---
#### Active Buffers
| File          | Class    | Retention        | Notes                                   |
|---------------|----------|------------------|-----------------------------------------|
| `recent.md`   | rolling  | last **7** loops | Evicts FIFO; entries merged to archive  |
| `summary.md`  | archive  | infinite         | Append-only; never overwritten          |
---
#### Buffer Rules
**Recent Buffer (`recent.md`)**
- `maxEntries`: **7** (also declared in metadata above)
- Overflow behaviour: oldest row copied to `summary.md`, then removed here.
- Edit policy: **appendOnly** (system-enforced)
**Archive (`summary.md`)**
- Unlimited length; append-only ledger.
- Accepts flushed rows from `recent.md` in chronological order.
- Validated for monotonic timestamps during merge.
---
#### Merge Triggers
- Automatic when `recent.md` reaches `maxEntries`.
- Manual when a job plan sets `forceMerge: true`.
- Policy-driven when a domain hits `merge_threshold` in `/protocols/file_lifespans.md`.
---
#### Enforcement Pathway
READ → ACT(plan_refresh_phase) → WRITE(handle_merge_phase)
│ │
└─ if merge required ──────────────┘
- Merge outcomes logged to `/audit/meta_audit.md`.
- Failure to flush after 1 loop raises `/lifecycle/drift_flag.md`.
---
#### Maintenance Guidance
- **Do not** edit existing rows; only appends allowed.
- Keep timestamps in **ISO-8601 UTC** for validator compatibility.
- Bulk migrations to external storage must update this manifest.
---
#### Summary
This manifest keeps the change-log pipeline healthy: a small, token-efficient window for day-to-day debugging and an immutable archive for deep forensic or compliance review. Maintain `maxEntries` conservatively to balance visibility against token budget.
