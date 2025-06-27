<!-- @meta {
  "fileType": "rolling",
  "maxEntries": 7,
  "evictionPolicy": "FIFO",
  "purpose": "Short window log of recent WRITE operations.",
  "editPolicy": "appendOnly",
  "routeScope": "global",
  "mergeTarget": "change_log/summary.md"
} -->
# Recent Change Log
Holds the last seven loop results. Oldest entries are merged into `summary.md` when the limit is exceeded.

| Loop | Timestamp (UTC) | Summary |
|------|-----------------|---------|
| `(example)` `42` | `2025-06-25T12:01Z` | `Updated client/index.md` |

When more than seven entries exist, the oldest is copied to `summary.md` and removed here. Never edit existing rows except through the automated merge process.
