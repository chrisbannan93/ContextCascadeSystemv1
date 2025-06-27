<!-- @meta {
  "fileType": "flag",
  "purpose": "Lifecycle drift indicator — logs protocol inconsistencies or skipped hygiene actions.",
  "editPolicy": "appendOnly",
  "routeScope": "global",
  "linkedAudits": ["audit/meta_audit.md"]
} -->

### /cascade/lifecycle/drift_flag.md

> **Role:** Raised when cascade behavior deviates from protocol expectations  
> (e.g., counter threshold met but no action queued, skipped merges, manual counter edits).

---

#### Active Flags  (append-only)

| Timestamp (UTC)       | Raised By                  | Issue Detected                                 | Domain |
|-----------------------|----------------------------|------------------------------------------------|--------|
| _none_                | —                          | —                                              | —      |

_Add a new row on each drift event; never delete existing rows._

---

#### Automatic Raise Conditions

1. Counter crosses a threshold, but ACT does **not** queue the required action.  
2. `recent.md` exceeds `maxEntries` without a merge to `summary.md`.  
3. Manual edits detected in any `lifecycle/*.md` counter file.  
4. `handle_merge_phase()` or `plan_refresh_phase()` halts or errors.  

---

#### Enforcement Behavior

- New, unacknowledged drift flags **halt WRITE** on the next loop.  
- ACT logs the flag to `/audit/meta_audit.md` with full context.  
- Resolution requires a job plan that references the specific flag row.

---

#### Clearing Procedure

1. Create a maintenance job plan detailing remediation.  
2. Execute the job; verify hashes & counters.  
3. Append a “_resolved_” note to the flag row with timestamp + job ID.  
4. Resume normal WRITE operations.

---

**Summary:**  
`drift_flag.md` is a tamper-evident ledger of lifecycle inconsistencies.  
Treat every entry as a priority defect until resolved; unresolved drift can corrupt context hygiene and token budgeting.
