<!-- @meta {
  "fileType": "counter",
  "purpose": "Tracks WRITE-phase activity for the server domain (backend logic, APIs, infra configs).",
  "editPolicy": "incrementOnly",
  "routeScope": "server",
  "created": "2025-06-27T00:00:00Z"
} -->

### /cascade/lifecycle/server.md

> **Role:** Counts every successful WRITE touching a **server-scoped** file (backend, API, infra).  
> ACT-phase logic compares this tick to thresholds in `/protocols/file_lifespans.md` to keep server context fresh and token-lean.

---

#### Tick Count  
`0`

---

#### Update Log (latest first)

| Cycle Δ | Timestamp (UTC) | Changed Path / Reason                    |
|---------|-----------------|------------------------------------------|
| —       | —               | Counter initialised                      |

---

#### Threshold Reference

| Threshold Type     | Default* | ACT-Phase Outcome                                      |
|--------------------|----------|-------------------------------------------------------|
| `reread_threshold` | **3**    | Reload server-domain context on next READ             |
| `prune_threshold`  | **5**    | Delete expired server temp / rolling buffers          |
| `merge_threshold`  | **8**    | Merge server short-term logs into `summary.md`        |

\* Values resolved from `/cascade/protocols/file_lifespans.md`.

---

#### Governance Rules

- **Incremented automatically** by the loop controller—never edit the tick manually.  
- Manual edits or skipped increments create `/lifecycle/drift_flag.md` entries and are logged in `/audit/meta_audit.md`.  
- Counter resets require a reviewed maintenance job plan (rare).

---

**Summary:**  
This counter lets ContextCascade detect when backend activity has accumulated enough changes to mandate rereads, pruning, or log merging—ensuring server memory remains current without bloating the token budget.
