<!-- @meta {
  "fileType": "policy",
  "subtype": "safeguardsPolicy",
  "purpose": "Comprehensive enforcement rules for hash integrity, protected blocks, write-gates, and recovery triggers.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
#### Protocol Safeguards Policy
This policy centralises **all mandatory protections** that preserve the integrity, auditability, and governance of the ContextCascade memory layer.
---
##### 1. Enforcement Matrix
| # | Safeguard | Trigger Condition | Automatic Response |
|---|-----------|------------------|--------------------|
| 1 | **Immutable Hash Check** | Hash mismatch detected in any `fileType: immutable` file during pre‑ or post‑WRITE | • Abort WRITE<br>• Log `hashMismatch` in `/audit/meta_audit.md`<br>• Raise `/lifecycle/drift_flag.md` |
| 2 | **Protected Block Enforcement** | Attempted edit overlaps a `<!-- PROTECTED -->` span | • Abort WRITE<br>• Log `protectedOverlap`<br>• Require security review if `escalation: true` |
| 3 | **Write Gate Validation** | Target path not allowed by `/security/write_gates.md` | • Abort WRITE<br>• Log `gateViolation` |
| 4 | **Active Edit Lock** | `_locks/active_edit.lock` present at READ or WRITE start | • Halt loop in safe‑hold<br>• Prompt manual unlock if stale |
| 5 | **Pre/Post Hash Workflow** | Hash delta of protected/immutable files differs from plan | • Roll back WRITE<br>• Log `postHashMismatch`<br>• Flag drift |
| 6 | **High‑Risk Action Flag** | Job plan contains `requiresReview: true` or touches critical files (e.g. `system_manifest.md`) | • Suspend WRITE until review approved<br>• Record event in `security_review.md` |
---
##### 2. Metadata Quick‑Reference
| Marker | Effect |
|--------|--------|
| `fileType: immutable` | Seals file content; requires hash verification every loop |
| `editPolicy: readonly` | Disables all writes (immutable by intent) |
| `protected: true` | Marks inline block as untouchable, even if file is editable |
| `ttlCycles: N` | Governs expiry of temporary / evictable files |
| `requiresReview: true` | Forces human / elevated agent approval before WRITE |
---
##### 3. Hash Verification Workflow
1. **Pre‑WRITE**
   - Compute SHA‑256 for every file tagged `immutable` **or** containing a protected block.
   - Compare against `audit/integrity_snapshot.md`.
   - On any mismatch → **abort** and raise `hashMismatch`.
2. **Post‑WRITE**
   - Re‑hash the same set plus any files actually written.
   - Validate against `expectedHashAfter` in `/cascade/job_logs/temp_job.md`.
   - On success → append entry to `/cascade/change_log/recent.md`.
   - On failure → roll back write, set `drift_flag.md`.
---
##### 4. Protected Block Syntax
```md
<!-- PROTECTED -->
... uneditable content ...
<!-- END PROTECTED -->
```
- **Nested blocks** are not allowed.
- Attempting to insert, delete, or reorder text inside a protected span constitutes a `protectedOverlap` violation.
---
##### 5. Recovery & Escalation Paths
- **Safe‑Hold Mode**: Activated on any safeguard breach to prevent cascading corruption.
- **Loop Recovery**: Instructions in `/cascade/protocols/recovery.md` outline how to resume after drift resolution.
- **Security Review**: High‑risk or failed safeguards require a signed entry in `/cascade/security/security_review.md`.
- **Immutable Restore**: Use snapshots listed in `audit/integrity_snapshot.md` to roll back mutated files.
---
##### 6. Maintenance Guidance
- Update this file **only** through an approved security review.
- Keep safeguard IDs in the enforcement matrix **stable** for audit tooling.
- Align new safeguards with counters and thresholds defined in `file_lifespans.md`.
