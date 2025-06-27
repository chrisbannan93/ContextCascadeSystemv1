<!-- @meta {
  "fileType": "append-only",
  "purpose": "Ledger of SHA-256 hashes for all immutable and protected files.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Integrity Snapshot
This file stores the reference hashes used to verify critical files. Append a new row whenever a protected or immutable file is created or updated. Existing entries must never be changed.

| File Path | SHA-256 Hash | Recorded At |
|-----------|--------------|-------------|
| _(example)_ `/cascade/system_manifest.md` | `2c6c2c50d63f78fce4a...` | `2025-06-25T00:00Z` |

Add a new row whenever an immutable or protected file is first written or legitimately updated. Do **not** modify existing entries—this table is an append-only audit trail used for hash verification during every loop.
