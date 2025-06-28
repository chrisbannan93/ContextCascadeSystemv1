<!-- @meta {
  "fileType": "temporary",
  "subtype": "job_plan",
  "purpose": "Ephemeral job plan for the current or upcoming WRITE cycle. Contains details of intended changes.",
  "editPolicy": "overwrite",
  "routeScope": "global",
  "ttlCycles": 1
} -->
# Temporary Job Plan

This file outlines the intended actions for the current or immediately upcoming WRITE cycle. It is generated during the ACT phase and consumed by the WRITE phase. It has a lifespan of one cycle (`ttlCycles: 1`).

---
## Structure
A job plan typically includes:
- **`intent`**: A brief description of the goal (e.g., "Patch UI routing schema").
- **`targets`**: A list of files to be modified, including:
    - `path`: The file path.
    - `expectedHashBefore`: SHA-256 hash of the file before the edit.
    - `expectedHashAfter`: Predicted SHA-256 hash after the edit.
    - `editPolicy` to be applied (e.g., `appendOnly`, `overwrite`).
    - `subtype` if applicable (e.g., `buffer`).
- **`rollbackPlan`**: Instructions or reference for rollback if the job fails.
- **`requiresReview`**: (Optional) `true` if the plan needs manual or elevated approval.
- **`securityLevel`**: (Optional) `high` for sensitive operations.

---
## Example
```yaml
intent: "Update client domain index with new component."
targets:
  - path: "cascade/domains/client/index.md"
    expectedHashBefore: "abc123def456..."
    expectedHashAfter: "789ghi012jkl..."
    editPolicy: "appendOnly"
    action: "Append new route for /component/new."
  - path: "cascade/change_log/recent.md"
    expectedHashBefore: "123..." # Optional for rolling logs if only appending
    expectedHashAfter: "456..." # Optional
    editPolicy: "appendOnly"
    action: "Log client index update."
rollbackPlan: "Revert cascade/domains/client/index.md to hash abc123def456... and remove corresponding entry from recent.md."
requiresReview: false
```

---
*(This file is typically overwritten each cycle. No active job plan at this moment.)*
