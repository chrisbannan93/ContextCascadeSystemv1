<!-- @meta {
  "fileType": "append-only",
  "subtype": "archive",
  "purpose": "Permanent ledger of every WRITE-cycle summary merged from change_log/recent.md.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->

### /cascade/change_log/summary.md

> **Role:** Immutable audit trail of *all* past WRITE-phase loop summaries.  
> Rows arrive here from `/cascade/change_log/recent.md` whenever that buffer overflows (`maxEntries` = 7) or a manual/threshold merge is triggered.

---

#### Historical Loop Activity  
*(chronological — oldest at top, newest appended last)*

| Cycle | Timestamp (UTC)        | Summary / Files Written                           | Job ID |
|------:|------------------------|---------------------------------------------------|:------:|
| —     | —                      | _Archive initialised_                             |  —     |

---

#### Integrity & Audit Rules

* **Append-only:** any attempt to edit or delete existing rows triggers `/lifecycle/drift_flag.md` and logs a violation in `/audit/meta_audit.md`.  
* **Timestamp format:** ISO-8601 UTC (`YYYY-MM-DD HH:MM:SSZ`).  
* **Validator checks:** monotonic cycle numbers and non-decreasing timestamps.  
* **External archival:** if older segments are exported, leave a stub row noting the export range and destination.

---

**Summary:**  
`summary.md` guarantees full provenance for every WRITE cycle, supporting forensic review, compliance checks, and rollback analysis. Keep it immutable and consistently formatted.
