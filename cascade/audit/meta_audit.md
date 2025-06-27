<!-- @meta {
  "fileType": "audit",
  "subtype": "integrityLog",
  "purpose": "System-wide log of loop-phase violations, integrity gaps, or protocol mismatches.",
  "editPolicy": "appendOnly",
  "routeScope": "global",
  "linkedFlags": ["lifecycle/drift_flag.md"]
} -->

### /cascade/audit/meta_audit.md

> **Role:** Append-only audit ledger.  
> Tracks drift, gate violations, hash mismatches, and skipped lifecycle actions during loop execution phases.  
> Used by `enforce_integrity_phase()` to block unsafe WRITE or escalate unresolved inconsistencies.

---

#### Recorded Events (append-only)

| Timestamp (UTC)       | Phase   | Type              | Description                                     | Affected Path / Ref         |
|------------------------|---------|-------------------|-------------------------------------------------|-----------------------------|
| _none yet_             | —       | —                 | Log initialised                                 | —                           |

---

#### Valid Audit Types

- `mergeSkipped` → buffer hit `maxEntries`, but merge not queued  
- `gateViolation` → WRITE attempt blocked by `/security/write_gates.md`  
- `thresholdBypassed` → tick hit threshold, but ACT skipped action  
- `manualEdit` → counter edited outside WRITE loop  
- `hashMismatch` → file hash deviated during WRITE  
- `auditEscalation` → flagged from `/security/security_review.md`

---

#### Enforcement Behavior

- Each row here is cross-checked against `/lifecycle/drift_flag.md`.  
- On loop start, any unresolved entries **block WRITE** unless `writeGated: false` is explicitly set.  
- All entries must reference a valid file path or component ID.  
- Only ACT, WRITE, or AUDIT layers may append to this file.

---

#### Maintenance Guidance

- Never delete or overwrite rows.  
- All timestamps must use **ISO‑8601 UTC** (`YYYY-MM-DDTHH:MM:SSZ`).  
- Alphabetise entries if bulk-imported.  
- Do not reference draft, temp, or unregistered paths.

---

**Summary**  
`meta_audit.md` is the canonical record of system protocol violations and lifecycle drift.  
It ensures unsafe changes cannot silently bypass enforcement gates or hygiene workflows.
