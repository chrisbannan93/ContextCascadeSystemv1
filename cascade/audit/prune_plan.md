<!-- @meta {
  "fileType": "evictable",
  "subtype": "prunePlan",
  "purpose": "Rule-set that schedules deletion, archival, or merge of short-lived files once lifecycle thresholds are met.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->

### /cascade/audit/prune_plan.md

> **Role:** Guides ACT-phase pruning when any domain crosses its `prune_threshold`.  
> Lists targets in strict priority order—top rows processed first.

---

#### Prune Priority Matrix

| Prio | Path / Glob Pattern          | Criteria                           | Mode      | Notes                               |
|:---:|------------------------------|------------------------------------|-----------|-------------------------------------|
| 1   | `temp_notes/**/*.md`         | unused ≥ 3 loops                   | delete    | scratchpad, no long-term value      |
| 2   | `drafts/**/*.md`             | never referenced in index          | delete    | developer stubs                     |
| 3   | `job_logs/temp_job.md`       | TTL ≥ 1 loop                       | delete    | auto-regenerated each cycle         |
| 4   | `change_log/recent.md`       | rows > `maxEntries` (7)            | auto-merge| flush oldest row to `summary.md`    |
| 5   | `client/session_trace.md`    | status = closed OR TTL ≥ 2 loops   | archive   | moved to `archives/client/`         |
| 6   | `server/debug_output.md`     | flag = stale OR size > 50 KB       | delete    | verbose debug output                |
| 7   | `schema/validation_trace.md` | age ≥ 3 loops, no active reads     | delete    | validation trace buffers            |

*Edit rows via job plan; keep table alphabetised by Path for diff clarity.*

---

#### Trigger Logic

- **Automatic:** when a domain’s `prune_threshold` is exceeded.  
- **Manual:** job plan sets `forcePrune: true`.  
- **Emergency:** security review flags `staleLogs` or `tokenSpike`.

---

#### Execution Flow

1. **ACT** compiles `prune_batch` from the matrix above.  
2. Paths added to `job_logs/temp_job.md` under `action: prune`.  
3. **WRITE** phase deletes / archives targets in priority order.  
4. Results appended to `/audit/meta_audit.md`.

---

#### Safety & Rollback

- Deletions are **soft-checked** for recent access; skipped if touched in last loop.  
- Archives land in `/archives/<domain>/` with original path + timestamp.  
- On failure, path logged to `/lifecycle/drift_flag.md`; prune retried next loop.

---

**Summary**  
`prune_plan.md` keeps the cascade lean by systematically clearing expired or oversize buffers while preserving critical audit trails. Update cautiously through reviewed job plans to avoid unintended data loss.
