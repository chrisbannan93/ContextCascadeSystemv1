<!-- @meta {
  "fileType": "counter",
  "purpose": "Counts WRITE-phase changes to security-domain files (auth flows, gate policies, hash checks).",
  "editPolicy": "incrementOnly",
  "routeScope": "security",
  "created": "2025-06-27T00:00:00Z"
} -->

### /cascade/lifecycle/security.md

> **Role:** Records every WRITE that touches a **security-scoped** file.  
> Tick values are compared to thresholds in `/protocols/file_lifespans.md` to keep high-risk logic fresh and audit noise low.

---

#### Tick Count  
`0`

---

#### Update Log (latest first)

| Δ | Timestamp (UTC) | Trigger / File    |
|---|-----------------|-------------------|
| — | —               | Counter initialised |

---

#### Threshold Reference (defined centrally)

| Threshold | Default | ACT-Phase Outcome                                   |
|-----------|---------|-----------------------------------------------------|
| `reread_threshold` | **2** | Reload security context on next READ          |
| `prune_threshold`  | **4** | Delete stale security buffers & temp logs     |
| `merge_threshold`  | **6** | Merge security logs into `summary.md`         |

---

#### Governance Rules

- **Incremented automatically** after qualifying WRITE events; manual edits forbidden.  
- Every increment appends a timestamped row to the table above.  
- Missing increments or manual edits raise `/lifecycle/drift_flag.md` and are logged in `/audit/meta_audit.md`.  
- Counter resets require an approved maintenance job plan.

---

**Summary:**  
This counter ensures security-domain activity prompts rapid rereads, pruning, and log consolidation, maintaining strict oversight of sensitive memory without bloating the token budget.
