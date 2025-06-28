<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Master index and routing map for all Cascade memory domains and protocol infrastructure.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Cascade Index Map

| Path | Role |
|------|------|
| `/cascade/00_BOOTSTRAP.md` | System entrypoint (immutable) |
| `/cascade/protocols/loop_protocol.md` | READ → ACT → WRITE enforcement |
| `/cascade/protocols/file_lifespans.md` | Refresh thresholds (by domain) |
| `/cascade/change_log/recent.md` | Rolling buffer (max 7) |
| `/cascade/change_log/summary.md` | Permanent history ledger |
| `/cascade/lifecycle/global.md` | Tick counter (global WRITE count) |
| `/cascade/lifecycle/*.md` | Domain write counters |
| `/cascade/load_plans/` | AI‑generated read plans (evictable) |
| `/cascade/job_logs/temp_job.md` | Temporary WRITE plan (1‑cycle TTL) |

---
## Notes
- This index is editable; append rows as domains expand.
- Reference only files that comply with `@meta` and loop discipline.
- `/cascade/` is structured memory; do not store application logic here.
