<!-- @meta {
  "fileType": "permanent",
  "subtype": "audit_log",
  "purpose": "Tracks estimated and actual token footprints of files and cascade branches to aid in budget awareness.",
  "editPolicy": "appendOrReplace",
  "routeScope": "audit"
} -->
# Token Usage Summary

This file stores data related to the token footprint of files and cascade branches. It helps the AI maintain token budget awareness, make informed decisions during context loading (especially in Lean Mode), and anticipate memory usage.

---
## Structure
This file might contain:
- **Per-file estimates:**
    - File path.
    - Estimated token count (based on heuristics, word count, or previous actuals).
    - Actual token count from the last time it was loaded.
    - Timestamp of the last actual count.
- **Per-domain/branch summaries:**
    - Domain path (e.g., `/cascade/client/`).
    - Total estimated token count for all files in that domain.
    - Total actual token count.
- **Global summary:**
    - Total estimated and actual token counts for the entire cascade.

---
## Example Content:
```
## Global Summary
- Total Estimated Tokens: 15200
- Total Actual Tokens (last full load): 14850
- Last Full Load Timestamp: 2025-07-15T10:00:00Z

---
## Per-Domain Summaries

### /cascade/client/
- Estimated Tokens: 3500
- Actual Tokens: 3320
- Files Tracked: 5

### /cascade/protocols/
- Estimated Tokens: 1200
- Actual Tokens: 1150
- Files Tracked: 4

---
## Per-File Details (Sample)

| File Path                          | Estimated Tokens | Actual Tokens (Last Load) | Last Actual Timestamp  |
|------------------------------------|------------------|---------------------------|------------------------|
| /cascade/00_BOOTSTRAP.md           | 150              | 145                       | 2025-07-15T09:00:00Z   |
| /cascade/index.md                  | 200              | 190                       | 2025-07-15T09:00:00Z   |
| /cascade/domains/client/index.md   | 450              | 430                       | 2025-07-15T09:05:00Z   |
| ...                                | ...              | ...                       | ...                    |

```

---
## Current Token Summary:

*(This section should be populated by an automated process or the AI based on file analysis and loading history.)*

**Last Updated:** (Timestamp)

*(No summary data yet)*

---
## Maintenance
- The AI or an external script should periodically update this file.
- Estimates can be generated via dry-run parsing or using heuristics.
- Actual token counts should be logged after files are loaded into context.
- This file itself can become large; consider strategies for summarization or rotation if it impacts performance.
- `editPolicy: appendOrReplace` allows for the file to be wholly updated by a token counting process.
