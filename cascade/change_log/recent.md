<!-- @meta {
  "fileType": "rolling",
  "subtype": "buffer",
  "purpose": "A rolling log of the most recent WRITE cycle summaries, up to a defined maximum.",
  "editPolicy": "appendOnly",
  "routeScope": "global",
  "maxEntries": 7,
  "mergeTarget": "/cascade/change_log/summary.md"
} -->
# Recent Change Log

This file contains a rolling buffer of the most recent successfully completed WRITE cycle summaries. When this log exceeds `maxEntries` (7), the oldest entry is moved to `/cascade/change_log/summary.md`.

---
*(No entries yet)*
