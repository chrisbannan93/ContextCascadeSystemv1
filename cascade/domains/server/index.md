<!-- @meta {
  "fileType": "structural",
  "subtype": "domainIndex",
  "purpose": "Manifest for the server domain. Lists backend memory files and defines load / hygiene behaviour.",
  "editPolicy": "appendOrReplace",
  "routeScope": "server"
} -->

### /domains/server/index.md

> **Role:** Maps the **server** memory surface—API logic, infra plans, and debug buffers.  
> Guides READ hydration and ACT-phase hygiene using lifecycle counters and threshold policy.

---

#### Registered Server Files

| Path                          | Class      | Purpose                                          |
|-------------------------------|----------- |--------------------------------------------------|
| `server.md`                   | counter    | Lifecycle ticks for backend WRITE activity       |
| `debug_output.md`             | rolling    | Runtime logs & trace buffers (prunable)          |
| `summary.md`                  | archive    | Durable digest of merged server logs             |
| `temp_notes/server_*.md`      | ephemeral  | Scratch buffers used during active jobs          |
| `drafts/server_*.md`          | draft      | WIP backend plans or experimental notes          |

---

#### Default Load Plan

| Phase | Included Files                      | Rationale                        |
|-------|-------------------------------------|----------------------------------|
| READ  | `summary.md`                        | Lightweight context hydrate      |
|       | `debug_output.md` *(if exists)*     | Needed only for active debugging |
|       | `temp_notes/*` *(on demand)*        | Loaded when referenced           |

---

#### Lifecycle Integration

* Tick source: **`/lifecycle/server.md`**  
* Thresholds from **`/protocols/file_lifespans.md`**

| Threshold        | Action Queued                          |
|------------------|----------------------------------------|
| `reread_threshold` | `force_reread(server)`                |
| `prune_threshold`  | purge `temp_notes` + old `debug_output` |
| `merge_threshold`  | move `debug_output.md` → `summary.md` |

---

#### Governance & Audit

* All server writes increment `server.md` counter.  
* Token usage tracked via `/audit/token_summary.md`.  
* Prune decisions follow `/audit/prune_plan.md`.  
* File additions must include valid `@meta` with `routeScope: server`.

---

**Summary**  
This index defines the backend memory map, ensuring server logic is hydrated efficiently, debug buffers are pruned on schedule, and summaries remain compact for future READ cycles.
