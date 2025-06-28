<!-- @meta {
  "fileType": "append-only",
  "purpose": "A permanent, append-only historical log of all WRITE cycle summaries, including those rolled over from recent.md.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Change Log Summary

This file is an append-only historical ledger of all successfully completed WRITE cycles. It includes entries merged from `/cascade/change_log/recent.md` when that buffer reaches its `maxEntries` limit.

---
## Guidelines
- Entries are added chronologically.
- Existing entries must not be modified or deleted.
- Each entry should provide a concise summary of a WRITE cycle, including:
    - Loop ID or timestamp.
    - Job plan reference.
    - Summary of modified files.
    - Outcome status (e.g., success, rolledBack, partial).
    - Post-WRITE hash confirmation status.

---
*(No entries yet)*
