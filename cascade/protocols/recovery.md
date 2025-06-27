<!-- @meta {
  "fileType": "protocol",
  "subtype": "recoveryPlan",
  "purpose": "Steps to restore cascade state after safeguard failure or drift.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
## Recovery Protocol
Trigger this plan if `drift_flag.md` exists or WRITE fails. It freezes writes, verifies hashes against `integrity_snapshot.md`, and reinstates a minimal load plan before resuming normal loops.
