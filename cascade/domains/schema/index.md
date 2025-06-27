<!-- @meta {
  "fileType": "index",
  "subtype": "domainIndex",
  "purpose": "Manifest for the schema domain—maps contracts, validation traces, and WIP drafts to lifecycle hygiene.",
  "editPolicy": "appendOrReplace",
  "routeScope": "schema"
} -->

### /domains/schema/index.md

> **Role:** Central map for **schema** memory.  
> Guides READ-phase hydration of contract data and ACT-phase hygiene using the `schema` lifecycle counter.

---

#### Registered Schema Assets

| Path                            | Class      | Purpose / Notes                                       |
|---------------------------------|------------|-------------------------------------------------------|
| `schema.md`                     | counter    | Tick tracker for every schema-domain WRITE            |
| `summary.md`                    | archive    | Canonical snapshot of merged schema edits             |
| `validation_trace.md`           | rolling    | Ephemeral log of recent validation runs               |
| `validators/*.json`             | static     | Auto-generated validator artefacts (read-only)        |
| `temp_notes/schema_*.md`        | ephemeral  | Scratch buffers (prunable)                            |
| `drafts/schema_*.md`            | draft      | WIP contract changes awaiting promotion               |

---

#### Default Load Plan

| Phase | Files Loaded                      | Rationale                           |
|-------|-----------------------------------|-------------------------------------|
| READ  | `summary.md`                      | Lightweight contract context        |
|       | `validation_trace.md` *(if exists)*| Required for ongoing schema jobs    |
|       | `validators/*.json` *(on demand)* | Pulled when validation diffs needed |
|       | `temp_notes/*` *(by reference)*   | Included only if job plan cites them|

---

#### Lifecycle & Threshold Integration

* Tick Source: **`/lifecycle/schema.md`**  
* Threshold Policy: **`/protocols/file_lifespans.md`**

| Threshold          | Queued Action                                   |
|--------------------|-------------------------------------------------|
| `reread_threshold` | `force_reread(schema)` – reload contract files  |
| `prune_threshold`  | purge `temp_notes` + stale `validation_trace`   |
| `merge_threshold`  | fold `validation_trace.md` → `summary.md`       |

---

#### Governance & Audit Hooks

- **Counters:** Every WRITE touching this domain increments `/lifecycle/schema.md`.  
- **Tokens:** Usage monitored in `/audit/token_summary.md`.  
- **Pruning:** Targets and ordering defined in `/audit/prune_plan.md`.  
- **Security:** Manual edits to validators trigger `/security/security_review.md`.

---

#### Maintenance Guidelines

1. **Metadata required** on all new schema files (`routeScope: schema`).  
2. Keep validator artefacts (`validators/*.json`) read-only—regenerated via job plan.  
3. Alphabetise table rows when adding new paths for merge-friendly diffs.

---

**Summary**  
This index anchors all contract-level memory for the schema domain, ensuring accurate hydration, predictable buffer decay, and audit-friendly summaries while controlling token overhead.
