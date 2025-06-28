<!-- @meta {
  "fileType": "protected",
  "purpose": "Defines the structured execution loop used by ContextCascade: READ → ACT → WRITE.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
#### Loop Protocol
<!-- PROTECTED -->
#### Three-Phase Execution Loop
This protocol enforces strict sequencing of AI task execution into three non-overlapping phases.
##### Phase 1 — READ
- Load context files as defined in the **active load plan** generated during the previous ACT.
- Perform no mutation or job logic.
- Validate hashes for all `immutable` or `protected` files.
##### Phase 2 — ACT
- Perform reasoning and generate a **job plan** (`temp_job.md`) plus an updated load plan (if needed).
- Create no file writes.
##### Phase 3 — WRITE
- **Pre-WRITE hash check**: verify immutable/protected files still match `integrity_snapshot.md`.
- Execute the job plan and mutate only allowed files.
- Recompute hashes and confirm against `expectedHashAfter`.
- Log deltas to `/cascade/change_log/` and increment lifecycle counters.
- Abort and enter Safe-Hold if any safeguard fails.
<!-- END PROTECTED -->
---
#### Loop Entry / Exit
- **Entry**: Allowed only when no `drift_flag.md` exists.
- **Exit**: Occurs after a successful WRITE and delta audit.
#### Safe-Hold Triggers
- Hash or safeguard failure
- Stale or conflicting `_locks/active_edit.lock`
- Missing / malformed `temp_job.md`
#### Audit Expectations
- Each phase transition must be traceable by job ID.
- Counters must increment exactly once per WRITE.
#### Maintenance Guidance
- Never modify PROTECTED sections except via security-reviewed job plans.
