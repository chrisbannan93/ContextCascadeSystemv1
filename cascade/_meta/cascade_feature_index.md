<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Master feature catalogue and directory reference for the ContextCascade system. Derived from system documentation.",
  "editPolicy": "appendOrReplace",
  "routeScope": "meta"
} -->
# ContextCascade Feature Index & Catalogue

This document provides a comprehensive index of all first-class features within the ContextCascade system, along with brief descriptions and references to their primary documentation or defining files. It is intended to be a quick reference for understanding the system's capabilities.

---
## Core Features

1.  **Metadata Blocks**
    *   **What**: Structured JSON-in-comment headers at the top of each file defining operational context.
    *   **Why**: Encode attributes like `fileType`, `editPolicy`, `ttlCycles`, `routeScope` for automated behavior.
    *   **Where**: All `.md` files in `/cascade/`. Validated by `validators/metadata_validator.ts`.
    *   **Ref**: Documentation §2.5.1, §4.

2.  **Canonical FileType Registry**
    *   **What**: Formal registry of nine allowed file types (`permanent`, `immutable`, `rolling`, `append-only`, `temporary`, `counter`, `evictable`, `protected`, `structural`) and their aliases.
    *   **Why**: Ensures consistent interpretation of file semantics.
    *   **Where**: Defined in Documentation §3.2.1. Enforced by `validators/metadata_validator.ts`.
    *   **Ref**: Documentation §2.5.2, §3.2.1.

3.  **Read → ACT → WRITE Loop Protocol**
    *   **What**: Disciplined three-phase protocol (Read, Act, Write) for every execution cycle.
    *   **Why**: Ensures clarity, auditability, and safety.
    *   **Where**: Defined in `/cascade/protocols/loop_protocol.md`.
    *   **Ref**: Documentation §2.5.3, `/cascade/protocols/loop_protocol.md`.

4.  **Load Modes (Lean, Domain, Full)**
    *   **What**: Hierarchical strategies for reading context files (`Lean`, `Domain`, `Full`).
    *   **Why**: Balances token budget and contextual completeness.
    *   **Where**: Logic in `protocols/load_mode_logic.md` (conceptual, actual file may vary). Referenced by load plans and lifecycle counters.
    *   **Ref**: Documentation §2.5.4.

5.  **Load Plans**
    *   **What**: Ephemeral markdown files defining the set of files for the next READ phase.
    *   **Why**: Optimizes token use and ensures relevant context ingestion.
    *   **Where**: `/cascade/load_plans/*.md` (e.g., `auto_plan_client.md`).
    *   **Ref**: Documentation §2.5.5.

6.  **Lifecycle Counters**
    *   **What**: `.md` files tracking update activity for specific domains/contexts (e.g., `client_tick.md`).
    *   **Why**: Trigger threshold-based logic (reloads, pruning, drift detection).
    *   **Where**: `/cascade/lifecycle/*.md`. Integrated with `/cascade/protocols/file_lifespans.md`.
    *   **Ref**: Documentation §2.5.6.

7.  **File Lifespan Policies**
    *   **What**: Declarative rules for when files should be reloaded, audited, merged, or deleted.
    *   **Why**: Manages file freshness, memory integrity, prevents token bloat.
    *   **Where**: `/cascade/protocols/file_lifespans.md`.
    *   **Ref**: Documentation §2.5.7.

8.  **Rolling Buffers**
    *   **What**: Files maintaining a fixed number of recent entries (e.g., `change_log/recent.md`).
    *   **Why**: Preserves short-term context efficiently.
    *   **Where**: Metadata `fileType: rolling`, `maxEntries`.
    *   **Ref**: Documentation §2.5.8.

9.  **Append-Only Logs**
    *   **What**: Historical files for events/changes in chronological order (e.g., `change_log/summary.md`).
    *   **Why**: Tamper-evident logs, reliable historical tracing.
    *   **Where**: Metadata `editPolicy: appendOnly`.
    *   **Ref**: Documentation §2.5.9.

10. **Temporary / One-Prompt Files**
    *   **What**: Volatile, single-use files (e.g., `job_logs/temp_job.md`).
    *   **Why**: Transient data, minimizing memory footprint.
    *   **Where**: Metadata `fileType: temporary`, `ttlCycles: 1`. Typically in `_taskbuffers/`.
    *   **Ref**: Documentation §2.5.10.

11. **Evictable Caches**
    *   **What**: Time-sensitive files for intermediate plans or temporary context (e.g., `load_plans/*.md`).
    *   **Why**: Manages token efficiency by offloading short-term reasoning.
    *   **Where**: Metadata `fileType: evictable`, `ttlCycles`.
    *   **Ref**: Documentation §2.5.11.

12. **Domain Routing**
    *   **What**: Metadata-driven scoping (`domain: client`) for files and actions.
    *   **Why**: Isolates context, prevents cross-domain contamination, improves token economy.
    *   **Where**: `system_manifest.md`, domain index files (`domains/*/index.md`), file metadata.
    *   **Ref**: Documentation §2.5.12.

13. **Protected Sections**
    *   **What**: Inline blocks (`<!-- PROTECTED --> ... <!-- END PROTECTED -->`) within editable files that are read-only.
    *   **Why**: Prevents drift in critical logic or assumptions.
    *   **Where**: Core control files like `loop_protocol.md`. Metadata `protected: true` at file level if entire file's sections are protected by this mechanism.
    *   **Ref**: Documentation §2.5.13.

14. **Write Gates**
    *   **What**: Declarative safeguards using glob patterns to control writable files/paths.
    *   **Why**: Protects architectural invariants, prevents rogue writes.
    *   **Where**: `/cascade/security/write_gates.md`.
    *   **Ref**: Documentation §2.5.14.

15. **Immutable Files & Hash Verification**
    *   **What**: Files that cannot be edited post-creation, tracked via cryptographic hashes.
    *   **Why**: Ensures stability of core declarations (doctrine, manifests).
    *   **Where**: Metadata `fileType: immutable`, `editPolicy: readonly`. Hashes in `/cascade/audit/integrity_snapshot.md`.
    *   **Ref**: Documentation §2.5.15.

16. **Integrity Snapshot**
    *   **What**: Canonical ledger of SHA-256 hashes for immutable/protected files.
    *   **Why**: Tamper-evidence seal, guarantees architectural trust.
    *   **Where**: `/cascade/audit/integrity_snapshot.md`.
    *   **Ref**: Documentation §2.5.16.

17. **Active Edit Lock**
    *   **What**: Volatile lockfile (`_locks/active_edit.lock`) signaling in-progress WRITE.
    *   **Why**: Prevents overlapping WRITE operations, ensures serialization.
    *   **Where**: `/cascade/_locks/active_edit.lock`.
    *   **Ref**: Documentation §2.5.17.

18. **Pre- & Post-Hash Checking**
    *   **What**: Dual-phase SHA-256 hash validation before and after WRITE for key files.
    *   **Why**: Detects corruption, unauthorized edits, ensures trustworthy state transitions.
    *   **Where**: Integrated into WRITE lifecycle for `immutable`/`protected` files, checked against `integrity_snapshot.md`.
    *   **Ref**: Documentation §2.5.18.

19. **Job Plans**
    *   **What**: Ephemeral planning artifacts (`job_logs/temp_job.md`) defining intended WRITE actions.
    *   **Why**: Traceability, intentionality, human/system confirmation for changes.
    *   **Where**: `/cascade/job_logs/temp_job.md`.
    *   **Ref**: Documentation §2.5.19.

20. **Write-Back Summary Confirmation**
    *   **What**: Post-WRITE verification where AI re-inspects written files against the job plan.
    *   **Why**: Guarantees WRITE operation succeeded exactly as intended.
    *   **Where**: Outcomes logged in `change_log/recent.md` and `audit/meta_audit.md`.
    *   **Ref**: Documentation §2.5.20.

21. **Summary Merging**
    *   **What**: System for condensing ephemeral files into durable summaries (e.g., `summary.md`).
    *   **Why**: Prevents token saturation, ensures long-term context continuity.
    *   **Where**: Controlled by metadata `mergeable`, `merge_target`, `merge_policy`.
    *   **Ref**: Documentation §2.5.21.

22. **Rolling Update Triggers**
    *   **What**: Lightweight mechanisms to update auxiliary logs/summaries post-WRITE without full replan.
    *   **Why**: Maintains freshness of recent context with minimal overhead.
    *   **Where**: Metadata `rollingUpdate`, `mergeTarget`. Affects files like `change_log/recent.md`.
    *   **Ref**: Documentation §2.5.22.

23. **Eviction Policy & Prune Plan**
    *   **What**: Rules and scripts defining how/when to delete/archive temporary or expired files.
    *   **Why**: Prevents performance degradation, memory bloat, stale context.
    *   **Where**: Master policy in `/cascade/audit/prune_plan.md`. Affects `_taskbuffers/`, `temp_notes/`, etc.
    *   **Ref**: Documentation §2.5.23.

24. **Token Budget Awareness**
    *   **What**: System tracking estimated token footprint of files/branches.
    *   **Why**: Prevents context overrun, enables smarter loading.
    *   **Where**: Tracked in `/cascade/audit/token_summary.md`.
    *   **Ref**: Documentation §2.5.24.

25. **Validator Pipeline**
    *   **What**: Utility (`validators/metadata_validator.ts`) for checking structural, metadata, and schema correctness.
    *   **Why**: Protects from malformed inputs, undefined behaviors.
    *   **Where**: `validators/metadata_validator.ts`. Errors to `meta_audit.md`.
    *   **Ref**: Documentation §2.5.25.

26. **Security Review & High-Risk Action Logging**
    *   **What**: Protocol governing and logging high-risk operations (schema rewrites, critical file mods).
    *   **Why**: Traceability and oversight for sensitive actions.
    *   **Where**: Policy in `security/security_review.md`. Logs in `audit/meta_audit.md`. Job plan flag `requiresReview: true`.
    *   **Ref**: Documentation §2.5.26.

27. **Drift Flag & Meta Audit**
    *   **What**: Mechanism for detecting and recording inconsistencies (`lifecycle/drift_flag.md`) and logging them (`audit/meta_audit.md`).
    *   **Why**: Maintains systemic trust, enables forensic debugging.
    *   **Where**: `/cascade/lifecycle/drift_flag.md`, `/cascade/audit/meta_audit.md`.
    *   **Ref**: Documentation §2.5.27.

28. **Hash Verification Workflow** (Subset of 15, 16, 18)
    *   **What**: 4-step process: Recalc hash → Compare to snapshot → If mismatch → Halt + Log + Flag.
    *   **Why**: Core to preventing architectural corruption.
    *   **Where**: `integrity_snapshot.md`, `immutable` files.
    *   **Ref**: Documentation §2.5.28.

29. **Schema & Snapshot Testing**
    *   **What**: Mechanism to capture structure, schema, metadata state at key milestones for regression testing and rollback.
    *   **Why**: Guards against structural drift in critical definitions.
    *   **Where**: Snapshots in `domains/schema/` or `audit/schema_snapshot.md`.
    *   **Ref**: Documentation §2.5.29.

30. **Extension Patterns (Counters, File Types)**
    *   **What**: Structured protocol for introducing new components (custom counters, file types).
    *   **Why**: Ensures extensibility while maintaining integrity.
    *   **Where**: Definitions in `system_manifest.md`, `metadata_schemas.md` (conceptual).
    *   **Ref**: Documentation §2.5.30.

31. **External Integrations & Hooks**
    *   **What**: Framework for interacting with external tools (CI/CD, ticketing).
    *   **Why**: Bridges cascade planning with real-world systems.
    *   **Where**: Logic in `external/` (conceptual). Metadata `external: true`, `externalHooks`.
    *   **Ref**: Documentation §2.5.31.

32. **Troubleshooting & Recovery Protocols**
    *   **What**: Defined procedures for handling system failures or inconsistencies.
    *   **Why**: Ensures system can be restored to a known good state.
    *   **Where**: `/cascade/protocols/recovery.md`.
    *   **Ref**: Documentation §2.5.32.

33. **Index Map (System + Domain Indexes)**
    *   **What**: Structured index files describing system layout and hierarchy.
    *   **Why**: Enables deterministic boot, accurate routing, memory-aware loading.
    *   **Where**: `/cascade/index.md` (global), `/cascade/domains/*/index.md` (domain-specific).
    *   **Ref**: Documentation §2.5.33.

34. **System Manifest (`system_manifest.md`)**
    *   **What**: Foundational, immutable declaration of system structure, doctrine, routing.
    *   **Why**: Anchor for cascade logic, ensures core invariants.
    *   **Where**: `/cascade/system_manifest.md`.
    *   **Ref**: Documentation §2.5.34.

35. **Loop Checkpoint (`loop_checkpoint.md`)**
    *   **What**: Sequential log recording successful completion of each full cascade loop.
    *   **Why**: Traceability, rollback orchestration, drift detection.
    *   **Where**: `/cascade/checkpoints/loop_checkpoint.md`.
    *   **Ref**: Documentation §2.5.35 (first one).

36. **Bootstrap Protocol (`00_BOOTSTRAP.md`)** (Note: Documentation has this as 2.5.35, but it's also 2.5.36 in a different numbering)
    *   **What**: Mandatory system entrypoint file defining foundational rules and boot preconditions.
    *   **Why**: Ensures sessions start from a clean, validated baseline.
    *   **Where**: `/cascade/00_BOOTSTRAP.md`.
    *   **Ref**: Documentation §1.4, §2.5.36 (or §2.5.35 last one), `/cascade/00_BOOTSTRAP.md`.

---
This index should be kept up-to-date as the ContextCascade system evolves.
It is based on "ContextCascade Developer & User Documentation v1.0".
