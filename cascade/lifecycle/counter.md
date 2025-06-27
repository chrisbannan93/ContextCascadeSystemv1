<!-- @meta {
  "fileType": "counter",
  "purpose": "Global lifecycle counter — increments after every successful WRITE cycle.",
  "editPolicy": "incrementOnly",
  "routeScope": "global",
  "created": "2025-06-27T00:00:00Z"
} -->

### /cascade/lifecycle/counter.md

> **Role:** Acts as the cascade’s heartbeat.  
> Every WRITE phase adds **+1**; ACT-phase logic compares this tick to the global thresholds in `/protocols/file_lifespans.md` to decide when to trigger system-wide rereads, pruning, or merges.

---

#### Tick Count  
`0`

---

#### Update Log (latest first)

| Cycle Δ | Timestamp (UTC)       | Action                                               |
|---------|----------------------|------------------------------------------------------|
| —       | —                    | Counter initialised                                  |

---

#### Behaviour & Thresholds
- **Incremented automatically** by the loop controller; **never edited manually**.  
- When `tick ≥ reread_threshold` (default **5**), ACT queues `force_reread(global)`.  
- `prune_threshold` & `merge_threshold` (defaults **7** & **10**) trigger global buffer cleanup and summary consolidation.  
- After hygiene actions complete, the counter **continues upward** (no auto-reset). Resets require a reviewed maintenance job.

---

#### Audit & Drift Handling
- Each increment is appended to this file’s table with an ISO-8601 timestamp.  
- Skipped increments or manual edits raise `/lifecycle/drift_flag.md` and are logged in `/audit/meta_audit.md`.

---

**Summary:**  
This counter provides a single source of truth for how many WRITE loops the cascade has executed. Accurate ticks are essential for timely context refresh and token-budget hygiene. Leave editing to the system and track all anomalies through the audit pipeline.
