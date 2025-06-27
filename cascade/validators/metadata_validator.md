<!-- @meta {
  "fileType": "permanent",
  "purpose": "Documentation for the metadata validation CLI used in READ and WRITE phases.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
# Metadata Validator Guide
Run the metadata validator described in `validators/metadata_validator.md` to check all cascade files for schema compliance. This tool parses `@meta` blocks and ensures required fields are present.
Include this validator in CI pipelines to prevent malformed metadata from entering the repository. Use `--fix` to automatically correct minor style issues when available.
