<!-- @meta {
  "fileType": "protected",
  "purpose": "Glob patterns defining allowed and denied write paths.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
# Write Gates
YAML formatted rules controlling which files may be modified. Example:
```yaml
writeGates:
  - allow: "domains/*/index.md"
  - deny: "audit/**"
```
