<!-- @meta {
  "fileType": "protocol",
  "subtype": "recoveryPlan",
  "purpose": "Structured fallback procedure triggered by safeguard failure, drift, or WRITE abortion.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
#### Recovery Protocol
This file governs how the system recovers when the loop fails due to safeguard violations, hash mismatches, or unresolved drift.
---
##### 1. Automatic Triggers
- Presence of `/lifecycle/drift_flag.md`
- WRITE aborted during `loop_protocol.md`
- Stale `_locks/active_edit.lock` preventing job completion
- Corrupted or missing `temp_job.md`
---
##### 2. Recovery Phases
###### Phase A — Diagnose
1. Halt all WRITE operations
2. Review `/audit/meta_audit.md` for safeguard or hash breach
3. Validate `audit/integrity_snapshot.md` against current file states
4. Verify `temp_job.md` plan integrity
###### Phase B — Contain & Flag
1. Move unstable or suspect files to `/quarantine/YYYY-MM-DD/`
2. If not already present, create `/lifecycle/drift_flag.md` with cause summary
3. Document all actions in `/audit/meta_audit.md`
###### Phase C — Restore
1. Use `integrity_snapshot.md` to replace corrupted `immutable` or `protected` files
2. Generate a minimal load plan referencing only core files (BOOTSTRAP, INDEX, MANIFEST)
3. Clear `drift_flag.md` only after successful plan load and hash check
---
##### 3. Manual Interventions
- Restoration steps require elevated agent or human confirmation
- Log each override in `/security/security_review.md` tagged `recovery`
---
##### 4. Emergency Halt
If integrity cannot be restored:
1. Archive `/cascade/` ➜ `/cascade_stale_YYYYMMDD/`
2. Rebootstrap using seed files
3. Transfer only audited summaries or logs
4. Log postmortem to `/audit/meta_audit.md` with `postmortem` tag
---
##### 5. Post-Recovery Actions
| File | Expected Update |
|------|------------------|
| `/audit/meta_audit.md` | Recovery event logged |
| `/change_log/recent.md` | Deltas appended |
| `/checkpoints/loop_checkpoint.md` | New checkpoint tagged `recovery-N` |
| `/lifecycle/drift_flag.md` | Deleted or archived |
| `/quarantine/` | Retain for 30 days minimum |
---
##### 6. Prevention Notes
- Validate `temp_job.md` for each cycle
- Monitor lifecycle counters for drift or stalling
- Run a dry loop audit (`read-only mode`) periodically
