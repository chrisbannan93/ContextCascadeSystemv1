<!-- @meta {
  "fileType": "evictable",
  "purpose": "Defines and executes controlled cleanup operations for temporary, expired, or unnecessary files.",
  "editPolicy": "overwrite",
  "routeScope": "audit",
  "ttlCycles": 3
} -->
# Prune Plan

This file outlines the policies and can trigger actions for deleting or archiving temporary, expired, or unnecessary files from the ContextCascade system. Its goal is to prevent performance degradation, memory bloat, and stale context leakage.

---
## Pruning Policies & Targets
This section defines what gets pruned and when. Policies are typically based on file metadata like `fileType`, `ttlCycles`, and `expirationPolicy`.

**Common Targets for Pruning:**
- **`temporary` files:** Files in `_taskbuffers/`, `job_logs/temp_job.md` (after `ttlCycles: 1` by default).
- **`evictable` files:** Files in `load_plans/` or other cache-like locations after their `ttlCycles` expire.
- **`rolling` buffers (entries):** Old entries in rolling buffers if not handled by merge logic (though merging is preferred).
- **Stale `active_edit.lock` files:** If `_locks/active_edit.lock` is old and no process is active.
- **Empty directories:** Directories that become empty after pruning.

---
## Pruning Triggers
Pruning can be triggered:
1.  **Automatically:**
    *   At the end of a WRITE cycle, based on `ttlCycles` countdowns.
    *   When lifecycle counters hit `prune_threshold` as defined in `/protocols/file_lifespans.md`.
2.  **Manually/AI-Initiated:**
    *   By an explicit prompt or command (e.g., "Execute prune plan to clear expired files").
    *   As part of a recovery process (`/protocols/recovery.md`).
3.  **Scheduled:** (If the system supports it) As a periodic maintenance task.

---
## Example Prune Plan Execution Script/Instructions (Conceptual)
This section could contain a plan that the AI executes.

```
## Prune Plan - YYYY-MM-DD

**Objective:** Clean up expired and temporary files.

**Phase 1: Identify Candidates**
1. Scan all files with `fileType: temporary`.
   - If `ttlCycles` has reached 0 or is not set (defaults to 1 for temporary), mark for deletion.
2. Scan all files with `fileType: evictable`.
   - If `ttlCycles` has reached 0, mark for deletion.
3. Check `/cascade/_locks/active_edit.lock`:
   - If timestamp older than (e.g., 1 hour) AND no active write process confirmed, mark for deletion.
4. List all files marked for deletion.

**Phase 2: Review (Optional)**
- Present list of files to be pruned to user/AI for confirmation if in interactive mode or if total size > X MB.

**Phase 3: Execute Pruning**
1. For each marked file:
   - If `expirationPolicy: archiveOnExpire` is set, move to `/cascade/_archive/YYYY-MM-DD/` (maintaining path).
   - Else, delete the file.
2. Log all actions (deleted/archived files) to `/cascade/audit/meta_audit.md` with type `staleFilePruned` or `fileArchived`.

**Phase 4: Cleanup**
1. Scan for any empty directories within `/cascade/` (except `_taskbuffers`, `load_plans`, `temp_notes` which might be intentionally empty awaiting new files) and list them for potential removal if policy dictates.

---
```

## Current Prune Plan Status:

*(This file is `evictable` and `overwrite`. It would be generated or updated when a prune operation is planned or executed. Currently idle.)*

**Last Execution:** (Timestamp or N/A)
**Next Scheduled (if applicable):** (Timestamp or N/A)

---
## Instructions for AI:
- To initiate a prune, you can generate a specific execution plan in this file (as per the example above).
- Then, during an ACT phase, reason over this plan and prepare the necessary delete/archive operations for the WRITE phase.
- Always log pruning actions to `/cascade/audit/meta_audit.md`.
- Respect `expirationPolicy` metadata on files. If `archiveOnExpire` is set, move the file instead of deleting.
