<!-- @meta {
  "fileType": "evictable",
  "ttlCycles": 3,
  "purpose": "Plan for pruning expired temporary or rolling files.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
# Prune Plan
This file lists cleanup actions the system should perform to remove stale caches and buffers. The plan expires after three cycles unless refreshed.

Format each line as `path → action` with an optional note. Example:

```
load_plans/auto_plan_client.md → delete  # expired
temp_notes/ui_scratch.md → archive       # preserve for audit
```

Entries are processed during the ACT phase. After an action executes, log the result in `meta_audit.md` and remove the line from this file.
