<!-- @meta {
  "fileType": "audit",
  "subtype": "tokenLedger",
  "purpose": "Snapshot of token consumption per domain and phase; informs pruning, merges, and load-plan optimisation.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global",
  "generatedBy": "ACT-phase token_sampler.ts"
} -->

### /cascade/audit/token_summary.md

> **Role:** Provides a **single-snapshot** view of recent token usage so the cascade can tune READ loads, prune oversized buffers, and adjust `file_lifespans.md` thresholds.  
> This file is regenerated each loop (replace-in-place).

---

#### Domain-Level Usage  (last N loops)

| Domain   | Tokens (last loop) | Tokens (rolling 7) | Primary Drivers                    |
|----------|--------------------|--------------------|------------------------------------|
| global   |  —                 |  —                 | metadata, indices, protocol files  |
| client   |  —                 |  —                 | UI buffers, session notes          |
| server   |  —                 |  —                 | API trees, backend plans           |
| schema   |  —                 |  —                 | contracts, validation rules        |
| security |  —                 |  —                 | hash logs, review entries          |
| job_logs |  —                 |  —                 | temp plans, archives               |
| change_log | —                |  —                 | recent + summary buffers           |

_Values populated automatically; blanks indicate first-run or reset._

---

#### Phase Breakdown  (last loop)

| Phase | Token Cost | Top Contributors (≈)                |
|-------|------------|-------------------------------------|
| READ  | —          | lifecycle counters, indices         |
| ACT   | —          | plan_refresh, validators            |
| WRITE | —          | merges, ledger writes, hashes       |

---

#### Audit Triggers

Token anomalies raise soft signals that ACT may convert into actions:

| Condition                                   | Action Enqueued                       |
|---------------------------------------------|---------------------------------------|
| Domain > 40 % of total for 7-loop window     | schedule_prune(domain)                |
| Phase cost spike > 25 % vs 7-loop average   | force_reread(global) + review note    |
| Total usage > 80 % token budget             | compress rolling buffers, alert audit |

All triggered actions are logged to `/audit/meta_audit.md`.

---

#### Maintenance Notes

* **Generation:** `ACT → token_sampler.ts` rewrites this file *in place* each loop; manual edits are ignored.  
* **History:** Prior snapshots are *not* preserved here; they reside in `/audit/token_history/` if archival is enabled.  
* **Validators:** ensure table rows remain alphabetised and phases stay in fixed order (`READ`, `ACT`, `WRITE`).

---

**Summary**  
`token_summary.md` is a living dashboard for cascade token health.  
Use it to guide pruning frequency, summary merging, and Lean-mode load-plan decisions.
