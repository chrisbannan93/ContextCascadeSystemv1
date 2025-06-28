<!-- @meta {
  "fileType": "append-only",
  "purpose": "A canonical ledger of cryptographic hashes (SHA-256) for all immutable and protected files in the cascade.",
  "editPolicy": "appendOnly",
  "routeScope": "audit"
} -->
# Integrity Snapshot

This file acts as a tamper-evident seal for the ContextCascade system. It stores a list of file paths and their corresponding SHA-256 hashes for all files declared as `immutable` or containing `protected` sections.

---
## Format
Each line in the snapshot represents a tracked file:
`<file_path>: "<sha256_hash>"`

---
## Usage
- **Initial Hashing:** When a file is first marked `immutable` or a `protected` section is defined and committed, its hash is calculated and appended to this list.
- **Verification:** During each loop (especially pre-WRITE and post-WRITE phases for relevant operations), the system:
    1. Reads the current content of each file listed here.
    2. Recomputes its SHA-256 hash.
    3. Compares it against the stored hash in this snapshot.
- **Mismatch:** If a hash mismatch is detected:
    - The operation (e.g., WRITE) is typically aborted.
    - A `hashMismatch` event is logged in `/cascade/audit/meta_audit.md`.
    - `/cascade/lifecycle/drift_flag.md` may be raised.

---
## Example Entries:
```
/cascade/00_BOOTSTRAP.md: "a1b2c3d4e5f6..."
/cascade/system_manifest.md: "f6e5d4c3b2a1..."
/cascade/protocols/loop_protocol.md: "1a2b3c4d5e6f..."
```

---
## Current Snapshot:

*(This section is populated automatically by the system when immutable files are created/updated through a secure process, or when protected sections are defined. Manual additions should be done with extreme care and typically involve a security review.)*

*(No snapshot entries yet)*

---
## Maintenance
- Entries should only be added or updated through a verified and secure process.
- Modifying an `immutable` file legitimately (e.g., a planned doctrine update) requires:
    1. A security review process (logged in `/cascade/security/security_review.md`).
    2. Approval for the change.
    3. Re-hashing the file.
    4. Appending the new hash to this snapshot (often with a comment indicating the version or change reason). The old hash entry might be commented out or archived, rather than deleted, for historical tracking.
- `editPolicy: appendOnly` ensures history is preserved. Updates to existing file hashes mean appending a new line for that file, versioning it.
