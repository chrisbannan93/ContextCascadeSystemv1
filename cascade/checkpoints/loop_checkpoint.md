<!-- @meta {
  "fileType": "checkpoint",
  "subtype": "loopBoundary",
  "purpose": "Marks validated WRITE-phase loop completions for traceability and state-lock verification.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->

### /cascade/checkpoints/loop_checkpoint.md

> **Role:** Immutable ledger of successful WRITE-phase completions.  
> Each entry proves the loop executed with integrity, all counters and summaries were committed, and no unresolved drift exists.

---

#### Loop Checkpoints (append-only)

| Cycle | Timestamp (UTC)       | Job ID   | Commit Hash (Post-WRITE)     | Status Notes                  |
|:-----:|------------------------|----------|-------------------------------|-------------------------------|
| —     | —                      | —        | —                             | _Checkpoint log initialized_  |

---

#### Write Conditions (required for entry)

1. All domain counters incremented cleanly.  
2. `job_logs/temp_job.md` passed pre/post hash validation.  
3. No unresolved flags in `/lifecycle/drift_flag.md`.  
4. If merge required, `change_log/recent.md` was flushed.  
5. `meta_audit.md` did not log WRITE-phase blocking errors.

---

#### Enforcement Logic

- Written once per **complete loop cycle**, during `WRITE(commit_phase)`.
- If omitted → next loop enters **safe mode** (plan gated).
- Hash is SHA-256 digest of all committed changes in job plan.

---

#### Validation Use

- Used by `ACT(enforce_integrity_phase)` to determine:
  - If WRITE was safely finalized
  - If loop state is resumable
- Required before scheduling new jobs, merges, or resets.

---

**Summary**  
`loop_checkpoint.md` acts as a gatekeeper for cascade loop continuity.  
No job plan or mutation should proceed without a valid, verifiable checkpoint entry.
