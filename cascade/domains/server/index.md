<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Index and routing map for all files and sub-modules within the 'server' domain.",
  "editPolicy": "appendOrReplace",
  "routeScope": "server"
} -->
# Server Domain Index

This file serves as the master index for all memory, guidance, and specification files related to the 'server' domain of the application (backend logic, APIs, services, etc.). It helps in targeted context loading and routing for server-specific tasks.

---
## Structure
This index typically lists key files or sub-directories within the `/cascade/domains/server/` path.

| Path within Server Domain | Role / Description                  | `fileType` (if specific) |
|---------------------------|-------------------------------------|--------------------------|
| `README.md`               | Overview of server domain memory    | `permanent`              |
| `architecture.md`         | Server-side architecture decisions  | `permanent`              |
| `api_implementation.md`   | Details on API endpoint logic       | `permanent`              |
| `services.md`             | Overview of microservices/modules   | `permanent`              |
| `database_interactions.md`| How server interacts with database  | `permanent`              |
| `auth_flow.md`            | Server-side authentication flow     | `permanent`              |
| `server_summary.md`       | Rolling summary of server changes   | `rolling`                |
| ...                       | ...                                 | ...                      |

*(This is an example structure. Populate with actual files as they are created for the server domain.)*

---
## Usage
- When a task is scoped to the `server` domain, this index helps the AI identify relevant files to load.
- It's referenced by the global `/cascade/index.md` and `/cascade/system_manifest.md`.
- Lifecycle actions for the server domain (triggered by `/cascade/lifecycle/server.md` counter) might involve rereading this index and its listed files.

---
## Maintenance
- This file should be updated whenever new persistent memory files or sub-modules are added to the `/cascade/domains/server/` directory.
- Use `editPolicy: appendOrReplace` to allow updates to the table.
- For clarity, use full paths from the `/cascade/` root for entries in the table (e.g., `/cascade/domains/server/architecture.md`).

**Current Server Domain Index:**

| Path                                   | Role / Description               |
|----------------------------------------|----------------------------------|
| `/cascade/domains/server/README.md`    | Overview of server domain memory |

*(Add more entries as server-specific memory files are created.)*
