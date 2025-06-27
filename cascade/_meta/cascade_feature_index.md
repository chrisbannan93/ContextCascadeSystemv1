<!-- @meta {
  "fileType": "structural",
  "subtype": "featureMap",
  "purpose": "Authoritative catalogue of ContextCascade first-class features, mapping each to its governing file(s) and enforcement phase.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->

### /_meta/cascade_feature_index.md

> **Role:** Quick-reference map of every core ContextCascade capability.  
> Loaded in **Lean Mode** so tools and humans can locate feature owners without incurring heavy token cost.

---

#### Feature Catalogue  (alphabetised)

| #  | Feature (§2.5)                   | Canonical File / Path(s)                             | Primary Loop Phase |
|----|----------------------------------|------------------------------------------------------|--------------------|
| 01 | **Active Edit Lock**             | `_locks/active_edit.md`                              | WRITE              |
| 02 | **Append-Only Logs**             | `change_log/summary.md`, `audit/meta_audit.md`       | WRITE              |
| 03 | **Bootstrap Protocol**           | `cascade/00_BOOTSTRAP.md`                            | session start      |
| 04 | **Domain Routing**               | `domains/*/index.md`, `cascade/system_manifest.md`   | READ               |
| 05 | **Drift Flag**                   | `lifecycle/drift_flag.md`                            | ACT / WRITE        |
| 06 | **Evictable Caches**             | `load_plans/*.md` (`ttlCycles`)                      | ACT                |
| 07 | **Extension Patterns**           | `drafts/*`, updates in `system_manifest.md`          | ACT validation     |
| 08 | **External Integrations & Hooks**| `external/**` adapters                               | post-WRITE hooks   |
| 09 | **File Lifespan Policy**         | `protocols/file_lifespans.md`                        | ACT                |
| 10 | **Hash Verification Workflow**   | loop controller scripts + `audit/integrity_snapshot` | WRITE              |
| 11 | **Immutable Files & Hashes**     | `immutable/**`, `audit/integrity_snapshot.md`        | READ / WRITE       |
| 12 | **Index Map**                    | `cascade/index.md`, domain indexes                   | READ               |
| 13 | **Integrity Snapshot**           | `audit/integrity_snapshot.md`                        | AUDIT              |
| 14 | **Job Plans**                    | `job_logs/temp_job.md`                               | ACT / WRITE        |
| 15 | **Lifecycle Counters**           | `lifecycle/*.md`                                     | WRITE / ACT        |
| 16 | **Load Modes** (Lean/Domain/Full)| `protocols/load_mode_logic.md`                       | READ               |
| 17 | **Load Plans**                   | `load_plans/*.md`                                    | ACT → next READ    |
| 18 | **Loop Checkpoint**              | `checkpoints/loop_checkpoint.md`                     | WRITE → next READ  |
| 19 | **Metadata Blocks**              | `@meta` headers in every file                        | READ               |
| 20 | **Prune Plan & Eviction**        | `audit/prune_plan.md`                                | ACT / WRITE        |
| 21 | **Read → ACT → WRITE Loop**      | `protocols/loop_protocol.md`                         | entire loop        |
| 22 | **Rolling Buffers**              | `change_log/recent.md`, `job_logs/recent.md`         | WRITE              |
| 23 | **Rolling Update Triggers**      | `plan_refresh_phase()` in loop controller            | ACT                |
| 24 | **Schema Snapshot Testing**      | `audit/schema_snapshot.md`                           | AUDIT              |
| 25 | **Security Review Workflow**     | `security/security_review.md`                        | AUDIT              |
| 26 | **Summary Merging**              | domain-level `summary.md` files                      | WRITE              |
| 27 | **System Manifest**              | `cascade/system_manifest.md`                         | READ / AUDIT       |
| 28 | **Token Budget Awareness**       | `audit/token_summary.md`                             | ACT                |
| 29 | **Validator Pipeline**           | `validators/metadata_validator.ts`                   | ACT                |
| 30 | **Write Back Confirmation**      | loop controller post-WRITE checks                    | WRITE              |
| 31 | **Write Gates**                  | `security/write_gates.md`                            | ACT validation     |

---

#### Maintenance

* **Add features** only after they’re registered in `system_manifest.md` and enforced in code.  
* Keep rows alphabetised by **Feature** name for diff clarity.  
* Use concise descriptions; deeper details live in the governing files.

---

**Summary**  
`cascade_feature_index.md` is the authoritative map of system capabilities, ensuring anyone (or any tool) can resolve *where* a feature is defined and *how* it’s enforced, without loading the entire cascade context.
