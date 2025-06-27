<!-- @meta {
  "fileType": "policy",
  "subtype": "thresholdPolicy",
  "purpose": "Counter thresholds that trigger rereads, pruning or merges.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
## File Lifespan Thresholds
Values below control when lifecycle counters cause maintenance actions.

| Domain Scope | reread_threshold | prune_threshold | merge_threshold |
|--------------|-----------------|-----------------|-----------------|
| global (`counter.md`) | 5 | 7 | 10 |
| client (`client.md`) | 3 | 5 | 8 |
| server (`server.md`) | 3 | 5 | 8 |
| schema (`schema.md`) | 4 | 6 | 9 |
| security (`security.md`) | 2 | 4 | 6 |

---
##### Threshold Meaning
- **`reread_threshold`** → Force a context reload for the domain on next READ.
- **`prune_threshold`** → Schedule deletion or archival of expired temp / rolling files.
- **`merge_threshold`** → Consolidate rolling buffers into durable summaries (e.g. `summary.md`).

---
##### Rationale (Lean)
- *Global* counters change most often → slightly larger window.
- *Client / Server* domains typically change more rapidly → tighter windows.
- *Schema* updates are less frequent but critical → moderate thresholds.
- *Security* events require aggressive maintenance to keep audit noise low.

---
##### Maintenance Guidance
- Update thresholds only via a reviewed job plan.
- Add a new row when introducing a new domain counter.
- Keep table alphabetised for diff-friendly PRs.
