<!-- @meta {
  "fileType": "policy",
  "subtype": "lifecycleIndex",
  "purpose": "Indexes all domain lifecycle counters and drives hygiene triggers (reread / prune / merge).",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
> Central registry for `lifecycle/*.md` counter files.
> Counters are incremented during **WRITE**, inspected during **ACT**, and compared to thresholds in `/protocols/file_lifespans.md`.
---
#### Registered Counters
| Counter File | Domain | What It Tracks                       |
|--------------|--------|--------------------------------------|
| `counter.md` | global | All WRITE cycles                     |
| `client.md`  | client | UI / frontend edits                  |
| `server.md`  | server | Backend / API edits                  |
| `schema.md`  | schema | Contract & validation changes        |
| `security.md`| security| High-risk actions & audit events    |
| `drift_flag.md` | system | Unresolved lifecycle contradictions |
---
#### Trigger Logic
- **WRITE phase** → increment relevant counter once per loop.
- **ACT phase** → compare ticks to `reread / prune / merge` thresholds.
- **Queued actions** → `force_reread`, `schedule_prune`, `schedule_merge`.
- **Drift** → if actions are skipped, update `/lifecycle/drift_flag.md` and log in `/audit/meta_audit.md`.
---
#### Maintenance
- Do **not** edit tick values by hand.
- Add new counters only via reviewed job plan; update this table & `file_lifespans.md`.
- Keep rows alphabetised.
---
#### Example Counter File Metadata
<!-- @meta {
  "fileType": "counter",
  "purpose": "Tracks WRITE-phase activity for the client domain.",
  "editPolicy": "incrementOnly",
  "routeScope": "client"
} -->
