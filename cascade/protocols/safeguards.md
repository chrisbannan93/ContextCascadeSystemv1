<!-- @meta {
  "fileType": "policy",
  "subtype": "safeguardsPolicy",
  "purpose": "Rules enforcing hash integrity, protected blocks and write gates.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
## Protocol Safeguards
This policy outlines mandatory checks before and after WRITE. Violations must be logged to `meta_audit.md` and may trigger `recovery.md`.
