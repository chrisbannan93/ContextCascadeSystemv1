<!-- @meta {
  "fileType": "append-only",
  "subtype": "checkpointed",
  "purpose": "Record of each completed READ→ACT→WRITE cycle.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Loop Checkpoint Ledger
Append one line per successful loop including job plan reference and result.

| Loop | Timestamp (UTC) | Job Plan | Outcome |
|------|-----------------|----------|---------|
