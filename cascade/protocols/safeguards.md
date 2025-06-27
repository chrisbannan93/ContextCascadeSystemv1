<!-- @meta {
  "fileType": "policy",
  "subtype": "safeguardsPolicy",
  "purpose": "Rules enforcing hash integrity, protected blocks and write gates.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
## Protocol Safeguards
This policy outlines mandatory checks before and after WRITE. Violations must be logged to `meta_audit.md` and may trigger `recovery.md`.

### Enforcement Matrix
| # | Safeguard | Trigger | Automated Response |
|---|-----------|---------|--------------------|
| 1 | Immutable hash check | Hash mismatch on protected/immutable file | Abort WRITE, raise `drift_flag.md` |
| 2 | Protected block edit | Attempt to modify `<!-- PROTECTED -->` content | Abort WRITE, log `protectedOverlap` |
| 3 | Write gate violation | Path not allowed by `write_gates.md` | Abort WRITE, record `gateViolation` |
| 4 | Active edit lock | `_locks/active_edit.lock` present | Enter Safe-Hold until cleared |

### Maintenance Guidance
- Keep safeguard IDs stable for audit scripts.
- Align new safeguards with thresholds in `file_lifespans.md`.
