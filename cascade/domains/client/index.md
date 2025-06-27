<!-- @meta {
  "fileType": "index",
  "subtype": "domainIndex",
  "purpose": "Manifest for the client domain. Routes all UI memory, ephemeral state, and cascade hygiene targets.",
  "editPolicy": "appendOrReplace",
  "routeScope": "client"
} -->

### /domains/client/index.md

> **Role:** Domain index for the **client** memory scope.  
> Resolves active, rolling, and archival UI content for context hydration and hygiene scheduling.

---

#### Registered Client Files

| Path                         | Class         | Purpose                                     |
|------------------------------|---------------|---------------------------------------------|
| `client.md`                  | counter       | Lifecycle tick tracker for UI changes       |
| `session_trace.md`           | rolling       | Logs session-bound client memory            |
| `summary.md`                 | archive       | Durable digest of recent UI state           |
| `temp_notes/*.md`            | ephemeral     | Short-lived notes from active interactions  |
| `drafts/client_*.md`         | draft         | Experimental UI stubs and pending memory    |

---

#### Domain Load Behavior

- **READ phase**:
  - Loads `summary.md` by default
  - Loads `session_trace.md` if session is live
  - Loads `temp_notes/*.md` only if referenced in job plan

- **ACT phase**:
  - Inspects tick from `/lifecycle/client.md`
  - Applies thresholds from `/protocols/file_lifespans.md`:
    - `reread_threshold` → `force_reread(client)`
    - `prune_threshold` → queue `temp_notes/*.md`
    - `merge_threshold` → compress `session_trace.md` into `summary.md`

---

#### Maintenance & Validation

- All WRITE-phase changes increment `/lifecycle/client.md`
- Memory footprint tracked via `/audit/token_summary.md`
- Pruning decisions resolved through `/audit/prune_plan.md`
- File additions require valid `@meta` headers and must declare `routeScope: client`

---

**Summary**  
This domain index defines the **client-facing memory surface**, providing UI context during READ, managing buffer hygiene during ACT, and orchestrating summary and ephemeral state flow during WRITE.
