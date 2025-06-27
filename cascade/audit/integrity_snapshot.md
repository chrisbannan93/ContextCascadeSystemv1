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
