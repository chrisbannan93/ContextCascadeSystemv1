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
