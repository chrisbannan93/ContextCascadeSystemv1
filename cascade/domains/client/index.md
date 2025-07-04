<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Index and routing map for all files and sub-modules within the 'client' domain.",
  "editPolicy": "appendOrReplace",
  "routeScope": "client"
} -->
# Client Domain Index

This file serves as the master index for all memory, guidance, and specification files related to the 'client' domain of the application. It helps in targeted context loading and routing for client-specific tasks.

---
## Structure
This index typically lists key files or sub-directories within the `/cascade/domains/client/` path. Each entry might specify the role or type of content.

| Path within Client Domain | Role / Description                 | `fileType` (if specific) |
|---------------------------|------------------------------------|--------------------------|
| `README.md`               | Overview of client domain memory   | `permanent`              |
| `architecture.md`         | Client-side architecture decisions | `permanent`              |
| `conventions.md`          | Client coding/naming conventions   | `permanent`              |
| `state_management.md`     | Client state management strategy   | `permanent`              |
| `components/`             | Directory for component specs      | (directory)              |
| `components/button.md`    | Specification for Button component | `permanent`              |
| `api_interfaces.md`       | Client-side view of API contracts  | `permanent`              |
| `client_summary.md`       | Rolling summary of client changes  | `rolling`                |
| ...                       | ...                                | ...                      |

*(This is an example structure. Populate with actual files as they are created for the client domain.)*

---
## Usage
- When a task is scoped to the `client` domain, this index helps the AI identify relevant files to load.
- It's referenced by the global `/cascade/index.md` and `/cascade/system_manifest.md`.
- Lifecycle actions for the client domain (triggered by `/cascade/lifecycle/client.md` counter) might involve rereading this index and its listed files.

---
## Maintenance
- This file should be updated whenever new persistent memory files or sub-modules are added to the `/cascade/domains/client/` directory.
- Use `editPolicy: appendOrReplace` to allow updates to the table.
- Keep paths relative to the `/cascade/domains/client/` directory for entries in the table, or use full paths from `/cascade/` root for clarity. Using full paths from `/cascade/` root is often less ambiguous. For example: `/cascade/domains/client/architecture.md`. The table above uses relative for brevity.

**Current Client Domain Index:**

| Path                                           | Role / Description                                                                 | `fileType` (Expected) |
|------------------------------------------------|------------------------------------------------------------------------------------|-----------------------|
| `/cascade/domains/client/README.md`            | Overview, purpose, and general guidance for the client domain's Cascade context.   | `permanent`           |
| `/cascade/domains/client/architecture.md`      | Detailed description of the client-side application architecture.                  | `permanent`           |
| `/cascade/domains/client/key_decisions.md`     | Log of significant architectural and technical decisions for the client domain.    | `permanent`           |
| `/cascade/domains/client/conventions.md`       | Coding standards, naming conventions, and style guides specific to client code.  | `permanent`           |
| `/cascade/domains/client/state_management.md`  | Strategy and patterns for managing client-side state (global and local).         | `permanent`           |
| `/cascade/domains/client/api_interfaces.md`    | Client-side perspective of API contracts it consumes.                              | `permanent`           |
| `/cascade/domains/client/testing_strategy.md`  | Guidelines and approach for unit, integration, and E2E testing of client code.   | `permanent`           |
| `/cascade/domains/client/client_summary.md`    | AI-distilled summary of the current client domain state, key decisions, and issues. | `permanent`           |
| `/cascade/domains/client/components/`          | Directory for specifications or documentation of reusable UI components.           | (directory)           |

*(This index should be actively maintained. Add new entries as client-specific memory and guidance files are created or planned.)*
