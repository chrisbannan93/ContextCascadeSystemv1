<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Catalogue of ContextCascade features and directory roles.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Cascade Feature Index
Document key features and where they are implemented across the cascade. Use this as a quick reference when extending the system.

| Feature | Description | Key Path |
|---------|-------------|----------|
| **Metadata Blocks** | JSON front matter controlling file behaviour and lifecycle. | All `.md` files |
| **Canonical File Types** | Registry of allowed `fileType` values. | `Repo_Documentation_v1.md` §3.2 |
| **Loop Protocol** | Three-phase READ → ACT → WRITE cycle. | `protocols/loop_protocol.md` |
| **Load Plans** | Lists of files to be read on the next cycle. | `load_plans/` |
| **Lifecycle Counters** | Domain-specific tick files incremented each WRITE. | `lifecycle/*.md` |
| **File Lifespan Policies** | Thresholds for reread, prune, and merge operations. | `protocols/file_lifespans.md` |
| **Rolling Buffers** | Short-term logs with fixed entry limits. | `change_log/recent.md` |
| **Append-Only Logs** | Permanent history ledger, never overwritten. | `change_log/summary.md` |
| **Integrity Snapshot** | SHA-256 hashes for immutable and protected files. | `audit/integrity_snapshot.md` |
| **Recovery Protocol** | Steps to restore state when safeguards fail. | `protocols/recovery.md` |

Add more rows as new features are introduced. Keep this index alphabetised for easy diff review.
