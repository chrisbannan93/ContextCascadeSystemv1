<!-- @meta {
  "fileType": "protected",
  "purpose": "Defines the structured execution loop used by ContextCascade: READ → ACT → WRITE, including job and change log management.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
#### Loop Protocol
<!-- PROTECTED -->
#### Three-Phase Execution Loop
This protocol enforces strict sequencing of AI task execution into three non-overlapping phases.

##### Phase 1 — READ
- Load context files as defined in the **active load plan** generated during the previous ACT phase. This plan is typically found in `/cascade/load_plans/`.
- Perform no mutation or job logic during this phase.
- Validate hashes for all `immutable` or `protected` files against `/cascade/audit/integrity_snapshot.md`.
- After you read this file in full, read `/cascade/protocols/file_lifespans.md` next to understand context refresh policies.

##### Phase 2 — ACT (Plan & Prepare)
- Based on the loaded context and the user's prompt, perform reasoning.
- Generate a detailed **job plan** in `/cascade/job_logs/temp_job.md`. This plan outlines the intended changes, target files, and expected outcomes for the WRITE phase. This file is overwritten each cycle.
- If necessary, generate an updated load plan for the *next* READ phase.
- Create no file writes or direct modifications to system files during this phase.

##### Phase 3 — WRITE (Execute & Log)
- **A. Pre-WRITE Validation:**
    - Verify immutable/protected files still match `/cascade/audit/integrity_snapshot.md` (Pre-WRITE hash check). Abort if mismatch.
    - Validate the job plan in `/cascade/job_logs/temp_job.md` for structural integrity and adherence to write gates defined in `/cascade/security/write_gates.md`. Abort if invalid.
- **B. Execute Job Plan:**
    - Execute the actions defined in `/cascade/job_logs/temp_job.md`.
    - Mutate only allowed files as specified in the job plan.
- **C. Post-WRITE Validation:**
    - Recompute hashes of affected files and confirm against `expectedHashAfter` values from the job plan.
    - If validation fails, attempt rollback as per job plan or enter Safe-Hold.
- **D. System Updates & Initial Logging:**
    1.  **Log Change Summary:** Generate a concise summary of the changes made during this WRITE phase (e.g., files modified, nature of change, related job ID). Append this summary to `/cascade/change_log/recent.md`.
    2.  **Increment Counters:** Increment relevant lifecycle counters in `/cascade/lifecycle/`.
    3.  **Update Checkpoint:** Update `/cascade/checkpoints/loop_checkpoint.md`.
- **E. Change Log Processing (Loop and Sweep Mechanism):**
    1.  **Check Recent Changes Buffer:**
        *   Count the number of distinct change summaries in `/cascade/change_log/recent.md`.
        *   Compare this count to the `maxEntries` value defined in `/cascade/change_log/recent.md`'s metadata (typically also referenced in `/cascade/change_log.md`).
    2.  **Perform Sweep if Buffer is Full:**
        *   If the count of change summaries in `/cascade/change_log/recent.md` equals `maxEntries`:
            *   Read all change summaries currently stored in `/cascade/change_log/recent.md`.
            *   Append these summaries (as a batch, maintaining chronological order) to `/cascade/change_log/summary.md`.
            *   Clear `/cascade/change_log/recent.md` of the swept entries (e.g., overwrite it with its initial header comment or an empty state, ready for new entries).
- **F. Job Log Processing (Loop and Sweep Mechanism):**
    1.  **Summarize Current Job:** Generate a concise summary of the just-completed job from `/cascade/job_logs/temp_job.md` (including intent, key files/outcomes, status, timestamp).
    2.  **Append to Recent Jobs:** Append this summary as a new entry to `/cascade/job_logs/recent.md`.
    3.  **Check Recent Jobs Buffer:**
        *   Count the number of distinct job summaries in `/cascade/job_logs/recent.md`.
        *   Compare this count to the `maxEntries` value defined in `/cascade/job_logs/recent.md`'s metadata (typically also referenced in `/cascade/job_logs.md`).
    4.  **Perform Sweep if Buffer is Full:**
        *   If the count of job summaries in `/cascade/job_logs/recent.md` equals `maxEntries`:
            *   Read all job summaries currently stored in `/cascade/job_logs/recent.md`.
            *   Append these summaries (as a batch, maintaining chronological order) to `/cascade/job_logs/summary.md`.
            *   Clear `/cascade/job_logs/recent.md` of the swept entries (e.g., overwrite it with its initial header comment or an empty state, ready for new entries).
- **G. Conclude WRITE Phase:**
    - If any step from A to F results in a critical failure that cannot be resolved, abort the loop and enter Safe-Hold mode as defined in `/cascade/protocols/recovery.md`.
<!-- END PROTECTED -->
---
#### Loop Entry / Exit
- **Entry**: Allowed only when no `drift_flag.md` exists and `/cascade/_locks/active_edit.lock` is not present or is stale and cleared by recovery.
- **Exit**: Occurs after a successful WRITE phase (including all sub-steps A-G) and successful delta audit.
#### Safe-Hold Triggers
- Hash or safeguard failure during any phase.
- Stale or conflicting `_locks/active_edit.lock`.
- Missing, malformed, or invalid `/cascade/job_logs/temp_job.md` at the start of WRITE phase.
- Failure in job execution or post-WRITE validation that cannot be rolled back.
- Critical failure during Job Log or Change Log Processing.
#### Audit Expectations
- Each phase transition must be traceable by job ID derived from `/cascade/job_logs/temp_job.md`.
- Lifecycle counters must increment exactly once per successful WRITE cycle.
- Job log files (`recent.md`, `summary.md`) must reflect the outcomes of all executed jobs.
- Change log files (`recent.md`, `summary.md`) must reflect all system modifications.
#### Maintenance Guidance
- Never modify PROTECTED sections except via security-reviewed job plans that explicitly detail changes to the core loop protocol.
- Ensure `/cascade/job_logs.md` and the metadata of `/cascade/job_logs/recent.md` correctly define `maxEntries` for their sweep mechanism.
- Ensure `/cascade/change_log.md` and the metadata of `/cascade/change_log/recent.md` correctly define `maxEntries` for their sweep mechanism.
