<!-- @meta {
  "fileType": "protocol",
  "subtype": "recoveryPlan",
  "purpose": "Steps to restore cascade state after safeguard failure or drift.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
## Recovery Protocol
Trigger this plan if `drift_flag.md` exists or WRITE fails. It freezes writes, verifies hashes against `integrity_snapshot.md`, and reinstates a minimal load plan before resuming normal loops.

### Recovery Steps
1. **Diagnose** – Hash-check all immutable and protected files; inspect `meta_audit.md` for cause.
2. **Contain** – Move suspect files to `/quarantine/` and set `drift_flag.md` with a short note.
3. **Restore** – Replace corrupted files from `integrity_snapshot.md` and generate a minimal load plan.
4. **Resume** – Clear the edit lock and `drift_flag.md` only after a clean READ → ACT → WRITE cycle.

Document each action taken during recovery in `audit/meta_audit.md` for historical reference.
