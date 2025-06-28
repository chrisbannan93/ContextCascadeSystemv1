<!-- @meta {
  "fileType": "immutable",
  "purpose": "Declarative list of active Cascade memory domains and their root paths.",
  "editPolicy": "readonly",
  "routeScope": "global"
} -->
# ContextCascade System Manifest

| Domain | Root Path | Purpose |
|--------|-----------|---------|
| core | `/cascade/` | Protocols, logs, counters, global memory |
| client | `/cascade/client/` | Client‑specific memory (optional) |
| server | `/cascade/server/` | Server‑side memory (optional) |
| schema | `/cascade/schema/` | Schema and validation rules |
| load_plans | `/cascade/load_plans/` | Evictable AI read plans |
| job_logs | `/cascade/job_logs/` | Temporary job state (TTL 1 cycle) |
| lifecycle | `/cascade/lifecycle/` | Domain counters (refresh triggers) |
| audit | `/cascade/audit/` | Integrity and hash audit logs (optional) |

---
## Notes
- Keep rows alphabetised for quick diff checks.
- Append a new row only after the corresponding domain directory exists.
- Manifest lists memory domains only; do not reference application repositories.
