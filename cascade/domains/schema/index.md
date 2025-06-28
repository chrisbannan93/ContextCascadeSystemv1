<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Index and routing map for all files related to data schemas, validation rules, and API contracts.",
  "editPolicy": "appendOrReplace",
  "routeScope": "schema"
} -->
# Schema Domain Index

This file serves as the master index for all memory, guidance, and specification files related to data schemas, validation rules, API contracts, and other structural definitions of the application.

---
## Structure
This index typically lists key files or sub-directories within the `/cascade/domains/schema/` path.

| Path within Schema Domain | Role / Description                     | `fileType` (if specific) |
|---------------------------|----------------------------------------|--------------------------|
| `README.md`               | Overview of schema domain memory       | `permanent`              |
| `database_schema.md`      | Database ERD and table definitions     | `permanent`              |
| `api_contracts.md`        | Detailed API endpoint specifications   | `permanent`              |
| `validation_rules.md`     | Business logic validation rules        | `permanent`              |
| `data_types.md`           | Common data type definitions           | `permanent`              |
| `schema_versions/`        | Directory for versioned schema snapshots | (directory)              |
| `schema_summary.md`       | Rolling summary of schema changes      | `rolling`                |
| ...                       | ...                                    | ...                      |

*(This is an example structure. Populate with actual files as they are created for the schema domain.)*

---
## Usage
- When a task is scoped to the `schema` domain (e.g., updating an API, modifying database structure), this index helps the AI identify relevant files.
- It's referenced by the global `/cascade/index.md` and `/cascade/system_manifest.md`.
- Lifecycle actions for the schema domain (triggered by `/cascade/lifecycle/schema.md` counter) involve rereading this index and its listed files.

---
## Maintenance
- This file should be updated whenever new persistent memory files or sub-modules are added to the `/cascade/domains/schema/` directory.
- Use `editPolicy: appendOrReplace` to allow updates to the table.
- For clarity, use full paths from the `/cascade/` root for entries in the table (e.g., `/cascade/domains/schema/api_contracts.md`).

**Current Schema Domain Index:**

| Path                                     | Role / Description               |
|------------------------------------------|----------------------------------|
| `/cascade/domains/schema/README.md`      | Overview of schema domain memory |

*(Add more entries as schema-specific memory files are created.)*
