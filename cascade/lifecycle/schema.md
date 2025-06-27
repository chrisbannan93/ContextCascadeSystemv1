<!-- @meta {
  "fileType": "counter",
  "purpose": "Counts WRITE-phase changes in the schema domain (contracts, models, validation rules).",
  "editPolicy": "incrementOnly",
  "routeScope": "schema",
  "created": "2025-06-27T00:00:00Z"
} -->

### /cascade/lifecycle/schema.md

> **Role:** Increments once after every WRITE that touches *schema-scoped* files.  
> Tick values drive ACT-phase hygiene decisions via `/protocols/file_lifespans.md`.

---

#### Tick Count  
`0`

---

#### Update Log (latest first)

| Δ | Timestamp (UTC)     | Touched Path / Reason                |
|---|---------------------|--------------------------------------|
| — | —                   | Counter initialised                  |

---

#### Threshold Reference (defined centrally)

| Threshold Type     | Default | ACT-Phase Outcome                                   |
|--------------------|---------|----------------------------------------------------|
| `reread_threshold` | **4**   | Reload schema context next READ                    |
| `prune_threshold`  | **6**   | Purge expired schema temp / rolling buffers        |
| `merge_threshold`  | **9**   | Merge schema buffers into `summary.md`             |

---

#### Governance Rules

* Incremented **only** by the loop controller; manual edits forbidden.  
* Each increment appends a timestamped log row above.  
* Missing increments or edits trigger `/lifecycle/drift_flag.md` and a record in `/audit/meta_audit.md`.  
* Resets are rare and require an approved maintenance job plan.

---

**Summary:**  
This counter lets the cascade know when schema evolution has accumulated enough change to warrant rereads, pruning, or log consolidation—keeping validation context fresh without uncontrolled token growth.
