<!-- @meta {
  "fileType": "temporary",
  "subtype": "job_plan",
  "ttlCycles": 1,
  "purpose": "Ephemeral plan describing the next WRITE actions.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
# Temporary Job Plan
This file is generated during ACT and executed during the next WRITE. It is deleted after one loop.

Recommended structure:

```yaml
intent: short description
targets:
  - path: example.md
    action: append
expectedHashBefore: abc123
expectedHashAfter: def456
```

The WRITE phase validates these hashes before and after applying the edits.
