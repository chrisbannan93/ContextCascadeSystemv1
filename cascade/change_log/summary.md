<!-- @meta {
  "fileType": "append-only",
  "purpose": "A permanent, append-only historical log of all system change summaries. It receives batches of summaries from the 'recent.md' buffer.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Change Log Summary

This file is an append-only historical ledger of all system change summaries, serving as a long-term archive.

It receives **batches of change summaries** that are "swept" from `/cascade/change_log/recent.md` when that buffer reaches its `maxEntries` capacity. This ensures that `summary.md` grows chronologically with sets of recent activities.

---
## Guidelines
- Entries (which are typically batches of summaries from `recent.md`) are appended chronologically.
- Existing content in this file must not be modified or deleted to maintain historical integrity.
- Each change summary within a batch should provide a concise record of a completed system modification, typically including:
    - Change ID or reference (e.g., related Job ID, timestamp of the WRITE cycle).
    - Brief description of the change (e.g., "Updated `file.md`", "Executed `prune_plan.md`").
    - Key files affected.
    - Outcome status if applicable.

---
*(No entries yet. This file will be populated with batches of change summaries swept from /cascade/change_log/recent.md.)*
