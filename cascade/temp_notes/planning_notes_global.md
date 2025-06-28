<!-- @meta {
  "fileType": "rolling",
  "subtype": "buffer",
  "purpose": "Rolling buffer for ongoing planning notes, ideas, or multi-step task tracking.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global",
  "maxEntries": 10,
  "mergePolicy": "squash",
  "mergeTarget": "/cascade/change_log/summary.md"
} -->
# Global Planning Notes (Rolling)

This file serves as a rolling buffer for general planning notes, ideas, or tracking multi-step tasks that span several cycles.

---
## Usage
- Append new notes or update existing sections.
- When `maxEntries` (e.g., 10, as an example here) is reached, older entries might be evicted or merged.
- The `mergePolicy` (e.g., `squash`) and `mergeTarget` (e.g., `/cascade/change_log/summary.md`) would define how its content is preserved long-term if needed, though these are illustrative here and should be set based on actual workflow.
- For domain-specific planning, consider creating separate files (e.g., `planning_notes_client.md`).

---
## Current Notes:

*(No notes yet. Add dated entries or task-specific sections below.)*

---
### Example Entry Format:
```
---
**Date:** YYYY-MM-DD
**Task/Topic:** Brief description
**Notes:**
- Point 1
- Point 2
- Action items...
---
```
