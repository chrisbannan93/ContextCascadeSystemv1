import os
import pathlib

# Define the repository structure and file contents
REPO_FILES = {}

# Helper function to add content to REPO_FILES
def add_file_content(path, content):
    REPO_FILES[path] = content.strip()

# Populate REPO_FILES with all specified file contents

# Root directory files
add_file_content("README.md", """\
<!-- @meta {
  "fileType": "permanent",
  "purpose": "High-level overview and quickstart reference for the ContextCascade repository.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
# Context Cascade

## 🚀 Overview

**Context Cascade** is a robust, modular, file-based memory and protocol system designed to augment persistent context management for AI coding assistants. Its primary aim is addressing memory limitations common in environments like Replit by externalizing architectural, behavioral, and decision-making context into clearly structured markdown files.

This structured external memory system enforces consistency, traceability, and durability of context across prompts, effectively bridging the gap between short-term ephemeral AI memory and long-term project coherence.

---

## 🎯 Key Problems Solved

Traditional AI coding assistants often encounter critical issues, including:

- Loss of architectural coherence across prompts
- Redundant component regeneration
- Architectural drift and inconsistencies
- Misaligned assumptions causing bugs
- Token budget constraints leading to memory management issues

Context Cascade systematically addresses these issues through an external memory approach that captures and maintains critical context externally.

---

## 📂 Directory Structure

```plaintext
/cascade/
├── 00_BOOTSTRAP.md                  # Entry-point enforcing protocol startup (immutable)
├── index.md                         # Master file map (structural)
├── system_manifest.md               # Immutable system doctrine (immutable)
├── protocols/
│   ├── loop_protocol.md             # READ → ACT → WRITE loop rules
│   └── file_lifespans.md            # Lifecycle refresh policies
├── lifecycle/                       # Domain counters and drift flags
├── change_log/                      # Rolling and historical logs
├── job_logs/                        # Ephemeral job planning logs
├── load_plans/                      # Scoped context-loading blueprints
├── audit/                           # Integrity, consistency, and security audits
├── domains/                         # Domain-specific guidance and routing
├── security/                        # Access control and write protection
├── checkpoints/                     # Loop execution checkpoints
└── validators/                      # Metadata and schema validation
```

---

## ⚙️ Core Principles

### 🔄 Read → Act → Write Loop

The disciplined three-phase operational cycle:

- **READ**: Load contextual files and validate metadata.
- **ACT**: Logical reasoning and preparation of intended changes.
- **WRITE**: Apply changes securely, with comprehensive validation.

### 📚 Metadata Enforcement

Structured JSON metadata headers define file behavior, lifecycle rules, and validation requirements, ensuring consistent treatment and system integrity.

### 🚦 Lifecycle Management

Automated lifecycle counters and policies manage context freshness, prune expired data, and maintain memory efficiency.

### 🔐 Security and Integrity

SHA-256 hashing, immutable files, protected sections, and rigorous validation prevent unauthorized modifications and detect unintended changes.

### 🌐 Domain Routing

Files and actions are scoped by logical domains (e.g., client, server, schema) to optimize token budget use and maintain clear boundaries.

---

## 🚧 Getting Started

1. **Bootstrap Initialization**

   - Every session begins by reading `00_BOOTSTRAP.md`.

2. **Core Files**

   - Explore the system’s structure via `/cascade/index.md`.
   - Review system rules in `/cascade/system_manifest.md`.

3. **Loop Protocol**

   - Study `/protocols/loop_protocol.md` to fully understand the operation cycle.

---

## 🛠 Placeholder Use Cases

### ✅ Bootstrap Example

A new Replit session initializes by first reading `00_BOOTSTRAP.md`, validating file hashes, and establishing baseline integrity before proceeding to user prompts.

### ✅ Lean-mode Query Example

AI reads only minimal necessary context from `index.md` to handle a lightweight query, optimizing token efficiency.

### ✅ Domain Extension Example

Developers introduce new domains through secure processes involving job plans, validator approvals, and updates to `system_manifest.md`.

---

## 🧩 Canonical File Types

- `permanent`
- `immutable`
- `rolling`
- `append-only`
- `temporary`
- `counter`
- `evictable`
- `protected`
- `structural`

These types govern lifecycle behaviors, memory management, and operational rules.

---

## 🔗 Contributions and Extensions

- New file types, domains, or lifecycle counters follow a strict extension pattern workflow, involving validation, approval, and secure implementation.
- Contributions must pass rigorous metadata validation (`validators/metadata_validator.md`).

### 🧪 Validator Setup

The metadata validator requires Node.js and `npm`.

1. Run `npm install` from the repository root to install `ts-node` and TypeScript.
2. Execute `npm run validate -- <path/to/file>` to check a file's metadata block.

---

## 📖 Documentation

Comprehensive documentation is available throughout the `/cascade/` directory, particularly in the `protocols/` and `audit/` subdirectories.

---

## 📮 Contact

For further details or collaboration, reach out to the maintainer at:

- **Email**: [chrisbannan93@gmail.com](mailto:chrisbannan93@gmail.com)

---

## 📌 License

Refer to the repository's `LICENSE` file for licensing details.

---
""")

add_file_content("package.json", """\
{
  "name": "contextcascade",
  "version": "1.0.0",
  "description": "Utilities for the ContextCascade memory system",
  "scripts": {
    "validate": "ts-node cascade/validators/metadata_validator.ts"
  },
  "devDependencies": {
    "ts-node": "^10.0.0",
    "typescript": "^4.0.0"
  }
}
""")

# /cascade/ files
add_file_content("cascade/00_BOOTSTRAP.md", """\
<!-- @meta {
  "fileType": "immutable",
  "purpose": "Bootstrap file enforcing protocol startup, scope discipline, and memory system entry constraints.",
  "editPolicy": "readonly"
} -->
# ContextCascade Bootstrap Guide
Welcome. This file is the required entrypoint for using the ContextCascade memory system. Before any task, you must:

## Mandatory Protocol (Follow Exactly)
- Read `/cascade/index.md` (map)
- Read `/cascade/protocols/loop_protocol.md` (loop rules)
- Respect all `@meta` blocks
- Check `/cascade/protocols/file_lifespans.md` and any `/cascade/lifecycle/*.md` counters
- Do not ACT or WRITE until READ phase is fully complete
- Never edit `<!-- PROTECTED -->` sections
- If any `immutable` file fails hash check → halt, log to `/audit/meta_audit.md`, skip WRITE

---
## Scope Rules (Memory vs. App)
- ContextCascade only stores memory, plans, counters, protocols, and logs
- Do not write `.md` files in Cascade that describe or duplicate app logic
- All application code or assets belong in the app repo, outside `/cascade/`
- Only create `.md` files here if storing durable reasoning or system governance

---
## Summary
If it’s not memory, constraint, protocol, or trace —
→ it doesn’t belong in Cascade.

Proceed to `/cascade/index.md`.
""")

add_file_content("cascade/index.md", """\
<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Master index and routing map for all Cascade memory domains and protocol infrastructure.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Cascade Index Map

| Path | Role |
|------|------|
| `/cascade/00_BOOTSTRAP.md` | System entrypoint (immutable) |
| `/cascade/protocols/loop_protocol.md` | READ → ACT → WRITE enforcement |
| `/cascade/protocols/file_lifespans.md` | Refresh thresholds (by domain) |
| `/cascade/change_log/recent.md` | Rolling buffer (max 7) |
| `/cascade/change_log/summary.md` | Permanent history ledger |
| `/cascade/lifecycle/counter.md` | Tick counter (global WRITE count) |
| `/cascade/lifecycle/*.md` | Domain write counters |
| `/cascade/load_plans/` | AI‑generated read plans (evictable) |
| `/cascade/job_logs/temp_job.md` | Temporary WRITE plan (1‑cycle TTL) |

---
## Notes
- This index is editable; append rows as domains expand.
- Reference only files that comply with `@meta` and loop discipline.
- `/cascade/` is structured memory; do not store application logic here.
""")

add_file_content("cascade/system_manifest.md", """\
<!-- @meta {
  "fileType": "immutable",
  "purpose": "Declarative list of active Cascade memory domains and their root paths.",
  "editPolicy": "readonly",
  "routeScope": "global"
} -->
# ContextCascade System Manifest

| Domain | Root Path | Purpose |
|--------|-----------|---------|
| core | `/cascade/` | Protocols, logs, counters, global memory |
| client | `/cascade/client/` | Client‑specific memory (optional) |
| server | `/cascade/server/` | Server‑side memory (optional) |
| schema | `/cascade/schema/` | Schema and validation rules |
| load_plans | `/cascade/load_plans/` | Evictable AI read plans |
| job_logs | `/cascade/job_logs/` | Temporary job state (TTL 1 cycle) |
| lifecycle | `/cascade/lifecycle/` | Domain counters (refresh triggers) |
| audit | `/cascade/audit/` | Integrity and hash audit logs (optional) |

---
## Notes
- Keep rows alphabetised for quick diff checks.
- Append a new row only after the corresponding domain directory exists.
- Manifest lists memory domains only; do not reference application repositories.
""")

add_file_content("cascade/init_context.md", """\
<!-- @meta {
  "fileType": "immutable",
  "purpose": "Immutable North-Star: Defines the foundational goals, architectural principles, and AI operational boundaries for this specific project.",
  "editPolicy": "readonly",
  "routeScope": "global"
} -->
# Project North-Star: Initial & Immutable Context

This document provides the foundational, unchanging (immutable) context for the AI agent operating on this project. It outlines the core mission, critical architectural principles, and the AI's defined role and boundaries. This context must underpin all AI reasoning, planning, and actions.

---
## I. Core Project Identity & Mission

*   **Project Name:** `[Specify Project Name - e.g., "NextGen E-commerce Platform", "AI-Powered Medical Diagnosis Assistant"]`
*   **Primary Goal/Mission:** `[Define the single most important objective of this project. Be specific. E.g., "To build a highly scalable and personalized e-commerce experience that achieves market leadership through superior usability and AI-driven recommendations." or "To assist medical professionals by providing rapid, accurate, and evidence-based preliminary diagnostic suggestions from medical imagery and patient data."]`
*   **Key Success Metrics (Conceptual):** `[List 2-3 high-level indicators of project success. E.g., "Significant year-over-year growth in user engagement and conversion rates," "Consistently high customer satisfaction (CSAT > 90%)," or "Demonstrable improvement in diagnostic speed and accuracy for targeted conditions," "Adoption by X number of clinics within Y years."]`

---
## II. Fundamental Architectural Principles & Constraints

*   **Primary Technology Stack (Core Immutable Elements):**
    *   Backend: `[e.g., Python with FastAPI, Java with Spring Boot, Node.js with Express]`
    *   Frontend: `[e.g., React, Angular, Vue.js, SvelteKit]`
    *   Database(s): `[e.g., PostgreSQL, MongoDB, MySQL, Cassandra]`
    *   Primary Cloud Provider: `[e.g., AWS, Azure, GCP, None/On-premise]`
    *   Other Critical Libraries/Frameworks: `[e.g., "Kafka for event streaming," "Kubernetes for orchestration (if applicable)"]`
*   **Overarching Architectural Style (If Fixed & Critical):**
    *   `[e.g., "Microservices architecture with event-driven communication patterns," "Modular Monolith," "Serverless-first for all new backend services," "Strict adherence to Clean Architecture principles."]`
*   **Key Design Non-Negotiables (Immutable Rules):**
    *   `[e.g., "All sensitive user data must be encrypted at rest and in transit using industry-standard algorithms."]`
    *   `[e.g., "The system must be designed for horizontal scalability to accommodate X users/requests."]`
    *   `[e.g., "All new APIs must adhere to the existing OpenAPI v3.x contract defined in /cascade/domains/schema/api_contracts.md."]`
    *   `[e.g., "Accessibility: All user-facing components must meet WCAG 2.1 AA standards."]`
*   **Critical Performance/Scalability Targets (Absolute Minimums):**
    *   `[e.g., "Core API endpoints must maintain an average response time below 150ms under peak load conditions as defined in performance_targets.md."]`
    *   `[e.g., "System must handle a sustained load of 10,000 concurrent users."]`

---
## III. AI Agent's Role & Boundaries within this Project

*   **Primary Role of AI:** `[Be specific. E.g., "To assist in the development of new features for the client-side application, including component creation, state management logic, and unit/integration tests.", "To generate and maintain comprehensive API documentation based on OpenAPI specifications and code comments.", "To identify and propose refactoring opportunities in legacy modules to improve code quality and align with modern best practices."]`
*   **Scope Limitations (Hard Boundaries - What AI Must NOT Do):**
    *   "AI must **never** deploy any code to production environments. All deployments require human review and manual execution of deployment pipelines."
    *   "AI must **never** alter this file (`cascade/init_context.md`), `/cascade/00_BOOTSTRAP.md`, or `/cascade/system_manifest.md`."
    *   "AI must **not** make changes to core security modules (e.g., authentication, authorization) without an approved job plan explicitly detailing the changes and signed off by a human lead (simulated via a `requiresReview: true` flag and positive confirmation if applicable)."
    *   "AI must **not** introduce new core dependencies (e.g., new programming languages, major frameworks) without these being documented as a key decision in the relevant domain's `key_decisions.md` file and approved."
    *   `[Add any other project-specific critical boundaries]`
*   **Preferred Development Practices (Guiding Principles for AI):**
    *   `[e.g., "Strive for Test-Driven Development (TDD) where practical, ensuring new logic is accompanied by robust tests."]`
    *   `[e.g., "Code comments should be clear, concise, and explain the 'why' behind complex logic, not just restate the 'what'."]`
    *   `[e.g., "Follow the Don't Repeat Yourself (DRY) principle diligently."]`
    *   `[e.g., "Ensure all contributions are consistent with coding conventions defined in relevant /cascade/domains/<domain>/conventions.md files."]`

---
## IV. Core Values / Guiding Philosophy (Project-Specific)

*   `[e.g., "User-centricity: Prioritize features and designs that deliver maximum value and ease-of-use to the end-user."]`
*   `[e.g., "Robustness & Reliability: Build for stability and ensure comprehensive error handling."]`
*   `[e.g., "Maintainability: Write clean, well-documented, and easily understandable code."]`
*   `[e.g., "Security by Design: Integrate security considerations into every stage of development."]`
*   `[e.g., "Iterative Progress: Favor incremental improvements and continuous learning."]`

---
This document is immutable and serves as the ultimate reference for the AI's core operational context within this project.
""")

add_file_content("cascade/protocols.md", """\
<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Registry of formal protocol definition files.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Protocols Registry

| Protocol File | Role |
|---------------|------|
| `/cascade/protocols/loop_protocol.md` | Core READ → ACT → WRITE loop |
| `/cascade/protocols/file_lifespans.md` | Lifecycle refresh thresholds |
| `/cascade/protocols/safeguards.md` | Hashing, write-gate, recovery logic |
| `/cascade/protocols/recovery.md` | Crash / resume instructions |

---
## Guidelines
- List protocol definition files only; exclude plans, logs, or counters.
- Keep rows alphabetised for diff‑friendly updates.
- Append a new row immediately after a protocol file is added to `/cascade/protocols/`.
""")

add_file_content("cascade/lifecycle.md", """\
<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Indexes all domain lifecycle counters and drives hygiene triggers (reread / prune / merge).",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
> Central registry for `lifecycle/*.md` counter files.
> Counters are incremented during **WRITE**, inspected during **ACT**, and compared to thresholds in `/protocols/file_lifespans.md`.
---
#### Registered Counters
| Counter File | Domain | What It Tracks                       |
|--------------|--------|--------------------------------------|
| `counter.md` | global | All WRITE cycles                     |
| `client.md`  | client | UI / frontend edits                  |
| `server.md`  | server | Backend / API edits                  |
| `schema.md`  | schema | Contract & validation changes        |
| `security.md`| security| High-risk actions & audit events    |
| `drift_flag.md` | system | Unresolved lifecycle contradictions |
---
#### Trigger Logic
- **WRITE phase** → increment relevant counter once per loop.
- **ACT phase** → compare ticks to `reread / prune / merge` thresholds.
- **Queued actions** → `force_reread`, `schedule_prune`, `schedule_merge`.
- **Drift** → if actions are skipped, update `/lifecycle/drift_flag.md` and log in `/audit/meta_audit.md`.
---
#### Maintenance
- Do **not** edit tick values by hand.
- Add new counters only via reviewed job plan; update this table & `file_lifespans.md`.
- Keep rows alphabetised.
---
#### Example Counter File Metadata
<!-- @meta {
  "fileType": "counter",
  "purpose": "Tracks WRITE-phase activity for the client domain.",
  "editPolicy": "incrementOnly",
  "routeScope": "client"
} -->
""")

add_file_content("cascade/change_log.md", """\
<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Manifest for change log files; defines the lifecycle of change information from recent activity to a permanent archive using a 'loop and sweep' mechanism.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global",
  "mergeTarget": "change_log/summary.md",
  "maxEntries": 7
} -->
### /cascade/change_log.md
> **Role:** Defines the structured process for logging summaries of changes made during each WRITE phase. This system ensures both recent visibility and long-term archival. It involves two key files:
> * **`change_log/recent.md`**: A buffer that collects summaries of recent changes. Once it reaches `maxEntries` (e.g., 7 changes), its contents are swept to `change_log/summary.md`.
> * **`change_log/summary.md`**: A permanent, append-only archive of all change summaries, providing a complete historical record.
---
#### Change Log Files & Lifecycle
| File Path                | Role & Behavior                                                                                                              | Max Entries (if applicable) | Edit Policy      |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------|
| `change_log/recent.md`   | Buffer for summaries of recent changes. Appended to after each relevant WRITE operation. When full, all entries are swept to `summary.md` and this file is cleared. | 7 (as per metadata)         | `appendOnly`     |
| `change_log/summary.md`  | Permanent append-only archive. Receives batches of change summaries from `recent.md`.                                          | N/A                         | `appendOnly`     |

---
#### Buffer Management for `change_log/recent.md`
- **Population**: After a WRITE phase successfully completes and makes modifications, a summary of those changes (e.g., files affected, nature of change, job ID if applicable, timestamp) is appended as a new entry to `change_log/recent.md`.
- **`maxEntries`**: The metadata field `maxEntries` (e.g., 7) in this file (`change_log.md`) and/or in `change_log/recent.md` defines the capacity of the recent changes buffer.
- **Sweep Operation (Trigger for Archival)**:
    1. This operation is triggered when the number of change summaries in `change_log/recent.md` reaches `maxEntries`.
    2. All accumulated change summaries are read from `change_log/recent.md`.
    3. These summaries are then appended in chronological order to `change_log/summary.md`.
    4. `change_log/recent.md` is then cleared of these entries (e.g., overwritten with its initial header or an empty state) to begin collecting the next batch of change summaries.
- **Edit Policy**: `change_log/recent.md` is `appendOnly` for individual change summaries. The sweep and clear operation is a system-level action.

---
#### `change_log/summary.md`
- **Integrity**: This file is strictly append-only to maintain a tamper-evident historical record of all system modifications.
- **Content**: Contains all change summaries that have been swept from `change_log/recent.md`. Timestamps or sequential IDs should ensure chronological order.

---
#### Guiding Principles for AI
- The AI must follow the operational protocol defined in `/cascade/protocols/loop_protocol.md` for updating these change log files during the WRITE phase.
- The sweep from `change_log/recent.md` to `change_log/summary.md` is a critical step for maintaining context efficiency (by keeping `recent.md` lean) and ensuring historical integrity.
---
""")

add_file_content("cascade/job_logs.md", """\
<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Manifest for job-log files; defines the lifecycle of job information from current planning, to recent history, to a permanent archive.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global",
  "mergeTarget": "job_logs/summary.md",
  "maxEntries": 5
} -->
### /cascade/job_logs.md
> **Role:** Defines the structured process for logging AI job plans and their outcomes. This involves three key files:
> * **`temp_job.md`**: Contains the plan for the single, currently active or most recently defined job. It is overwritten with each new job.
> * **`job_logs/recent.md`**: A buffer that collects summaries of recently completed jobs. Once it reaches `maxEntries` (e.g., 5 jobs), its contents are swept to `job_logs/summary.md`.
> * **`job_logs/summary.md`**: A permanent, append-only archive of all job summaries, providing a complete historical record.
---
#### Job Log Files & Lifecycle
| File Path               | Role & Behavior                                                                                                | Max Entries (if applicable) | Edit Policy      |
|-------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------|------------------|
| `temp_job.md`           | Current job plan; overwritten each cycle by the AI during the ACT phase.                                       | 1 (conceptual)              | `overwrite`      |
| `job_logs/recent.md`    | Buffer for summaries of recently completed jobs. Appended to after each job. When full, all entries are swept to `summary.md` and this file is cleared. | 5 (as per metadata)         | `appendOnly`     |
| `job_logs/summary.md`   | Permanent append-only archive. Receives batches of job summaries from `recent.md`.                               | N/A                         | `appendOnly`     |

---
#### Buffer Management for `job_logs/recent.md`
- **Population**: After a job defined in `temp_job.md` is successfully completed, a summary of that job (intent, key outcomes, status) is appended as a new entry to `job_logs/recent.md`.
- **`maxEntries`**: The metadata field `maxEntries` (e.g., 5) in this file (`job_logs.md`) and/or in `job_logs/recent.md` defines the capacity of the recent jobs buffer.
- **Sweep Operation (Trigger for Archival)**:
    1. This operation is triggered when the number of job summaries in `job_logs/recent.md` reaches `maxEntries`.
    2. All accumulated job summaries are read from `job_logs/recent.md`.
    3. These summaries are then appended in chronological order to `job_logs/summary.md`.
    4. `job_logs/recent.md` is then cleared of these entries (e.g., overwritten with its initial header or an empty state) to begin collecting the next batch of job summaries.
- **Edit Policy**: `job_logs/recent.md` is `appendOnly` for individual job summaries. The sweep and clear operation is a system-level action.

---
#### `job_logs/summary.md`
- **Integrity**: This file is strictly append-only to maintain a tamper-evident historical record.
- **Content**: Contains all job summaries that have been swept from `job_logs/recent.md`. Timestamps or sequential job IDs should ensure chronological order.

---
#### Guiding Principles for AI
- The AI must follow the operational protocol defined in `/cascade/protocols/loop_protocol.md` for updating these job log files.
- `temp_job.md` is the source for the current job's execution and its subsequent summarization into `job_logs/recent.md`.
- The sweep from `job_logs/recent.md` to `job_logs/summary.md` is a critical step for maintaining context efficiency and historical integrity.
---
""")


# /cascade/protocols/ files
add_file_content("cascade/protocols/loop_protocol.md", """\
<!-- @meta {
  "fileType": "protected",
  "purpose": "Defines the structured execution loop used by ContextCascade: READ → ACT → WRITE, including job and change log management.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
#### Loop Protocol
<!-- PROTECTED -->
#### Three-Phase Execution Loop
This protocol enforces strict sequencing of AI task execution into three non-overlapping phases.

##### Phase 1 — READ
- Load context files as defined in the **active load plan** generated during the previous ACT phase. This plan is typically found in `/cascade/load_plans/`.
- Perform no mutation or job logic during this phase.
- Validate hashes for all `immutable` or `protected` files against `/cascade/audit/integrity_snapshot.md`.
- After you read this file in full, read `/cascade/protocols/file_lifespans.md` next to understand context refresh policies.

##### Phase 2 — ACT (Plan & Prepare)
- Based on the loaded context and the user's prompt, perform reasoning.
- Generate a detailed **job plan** in `/cascade/job_logs/temp_job.md`. This plan outlines the intended changes, target files, and expected outcomes for the WRITE phase. This file is overwritten each cycle.
- If necessary, generate an updated load plan for the *next* READ phase.
- Create no file writes or direct modifications to system files during this phase.

##### Phase 3 — WRITE (Execute & Log)
- **A. Pre-WRITE Validation:**
    - Verify immutable/protected files still match `/cascade/audit/integrity_snapshot.md` (Pre-WRITE hash check). Abort if mismatch.
    - Validate the job plan in `/cascade/job_logs/temp_job.md` for structural integrity and adherence to write gates defined in `/cascade/security/write_gates.md`. Abort if invalid.
- **B. Execute Job Plan:**
    - Execute the actions defined in `/cascade/job_logs/temp_job.md`.
    - Mutate only allowed files as specified in the job plan.
- **C. Post-WRITE Validation:**
    - Recompute hashes of affected files and confirm against `expectedHashAfter` values from the job plan.
    - If validation fails, attempt rollback as per job plan or enter Safe-Hold.
- **D. System Updates & Initial Logging:**
    1.  **Log Change Summary:** Generate a concise summary of the changes made during this WRITE phase (e.g., files modified, nature of change, related job ID). Append this summary to `/cascade/change_log/recent.md`.
    2.  **Increment Counters:** Increment relevant lifecycle counters in `/cascade/lifecycle/`.
    3.  **Update Checkpoint:** Update `/cascade/checkpoints/loop_checkpoint.md`.
- **E. Change Log Processing (Loop and Sweep Mechanism):**
    1.  **Check Recent Changes Buffer:**
        *   Count the number of distinct change summaries in `/cascade/change_log/recent.md`.
        *   Compare this count to the `maxEntries` value defined in `/cascade/change_log/recent.md`'s metadata (typically also referenced in `/cascade/change_log.md`).
    2.  **Perform Sweep if Buffer is Full:**
        *   If the count of change summaries in `/cascade/change_log/recent.md` equals `maxEntries`:
            *   Read all change summaries currently stored in `/cascade/change_log/recent.md`.
            *   Append these summaries (as a batch, maintaining chronological order) to `/cascade/change_log/summary.md`.
            *   Clear `/cascade/change_log/recent.md` of the swept entries (e.g., overwrite it with its initial header comment or an empty state, ready for new entries).
- **F. Job Log Processing (Loop and Sweep Mechanism):**
    1.  **Summarize Current Job:** Generate a concise summary of the just-completed job from `/cascade/job_logs/temp_job.md` (including intent, key files/outcomes, status, timestamp).
    2.  **Append to Recent Jobs:** Append this summary as a new entry to `/cascade/job_logs/recent.md`.
    3.  **Check Recent Jobs Buffer:**
        *   Count the number of distinct job summaries in `/cascade/job_logs/recent.md`.
        *   Compare this count to the `maxEntries` value defined in `/cascade/job_logs/recent.md`'s metadata (typically also referenced in `/cascade/job_logs.md`).
    4.  **Perform Sweep if Buffer is Full:**
        *   If the count of job summaries in `/cascade/job_logs/recent.md` equals `maxEntries`:
            *   Read all job summaries currently stored in `/cascade/job_logs/recent.md`.
            *   Append these summaries (as a batch, maintaining chronological order) to `/cascade/job_logs/summary.md`.
            *   Clear `/cascade/job_logs/recent.md` of the swept entries (e.g., overwrite it with its initial header comment or an empty state, ready for new entries).
- **G. Conclude WRITE Phase:**
    - If any step from A to F results in a critical failure that cannot be resolved, abort the loop and enter Safe-Hold mode as defined in `/cascade/protocols/recovery.md`.
<!-- END PROTECTED -->
---
#### Loop Entry / Exit
- **Entry**: Allowed only when no `drift_flag.md` exists and `/cascade/_locks/active_edit.lock` is not present or is stale and cleared by recovery.
- **Exit**: Occurs after a successful WRITE phase (including all sub-steps A-G) and successful delta audit.
#### Safe-Hold Triggers
- Hash or safeguard failure during any phase.
- Stale or conflicting `_locks/active_edit.lock`.
- Missing, malformed, or invalid `/cascade/job_logs/temp_job.md` at the start of WRITE phase.
- Failure in job execution or post-WRITE validation that cannot be rolled back.
- Critical failure during Job Log or Change Log Processing.
#### Audit Expectations
- Each phase transition must be traceable by job ID derived from `/cascade/job_logs/temp_job.md`.
- Lifecycle counters must increment exactly once per successful WRITE cycle.
- Job log files (`recent.md`, `summary.md`) must reflect the outcomes of all executed jobs.
- Change log files (`recent.md`, `summary.md`) must reflect all system modifications.
#### Maintenance Guidance
- Never modify PROTECTED sections except via security-reviewed job plans that explicitly detail changes to the core loop protocol.
- Ensure `/cascade/job_logs.md` and the metadata of `/cascade/job_logs/recent.md` correctly define `maxEntries` for their sweep mechanism.
- Ensure `/cascade/change_log.md` and the metadata of `/cascade/change_log/recent.md` correctly define `maxEntries` for their sweep mechanism.
""")

add_file_content("cascade/protocols/file_lifespans.md", """\
<!-- @meta {
  "fileType": "permanent",
  "purpose": "Defines counter thresholds that trigger rereads, pruning, or summary merges for each lifecycle scope.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
#### File Lifespan Thresholds
Thresholds below are evaluated during **Phase 2 – ACT**. When a lifecycle counter meets or exceeds a threshold, the corresponding action is queued for the next loop.
| Domain Scope | `reread_threshold` | `prune_threshold` | `merge_threshold` |
|--------------|--------------------|-------------------|-------------------|
| global (`counter.md`) | 5 | 7 | 10 |
| client (`client.md`)  | 3 | 5 | 8 |
| server (`server.md`)  | 3 | 5 | 8 |
| schema (`schema.md`)  | 4 | 6 | 9 |
| security (`security.md`) | 2 | 4 | 6 |
---
##### Threshold Meaning
- **`reread_threshold`** → Force a context reload for the domain on next READ.
- **`prune_threshold`** → Schedule deletion or archival of expired temp / rolling files.
- **`merge_threshold`** → Consolidate rolling buffers into durable summaries (e.g. `summary.md`).
---
##### Rationale (Lean)
- *Global* counters change most often → slightly larger window.
- *Client / Server* domains typically change more rapidly → tighter windows.
- *Schema* updates are less frequent but critical → moderate thresholds.
- *Security* events require aggressive maintenance to keep audit noise low.
---
##### Maintenance Guidance
- Update thresholds only via a reviewed job plan.
- Add a new row when introducing a new domain counter.
- Keep table alphabetised for diff‑friendly PRs.
""")

add_file_content("cascade/protocols/safeguards.md", """\
<!-- @meta {
  "fileType": "permanent",
  "purpose": "Comprehensive enforcement rules for hash integrity, protected blocks, write-gates, and recovery triggers.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
#### Protocol Safeguards Policy
This policy centralises **all mandatory protections** that preserve the integrity, auditability, and governance of the ContextCascade memory layer.
---
##### 1. Enforcement Matrix
| # | Safeguard | Trigger Condition | Automatic Response |
|---|-----------|------------------|--------------------|
| 1 | **Immutable Hash Check** | Hash mismatch detected in any `fileType: immutable` file during pre‑ or post‑WRITE | • Abort WRITE<br>• Log `hashMismatch` in `/audit/meta_audit.md`<br>• Raise `/lifecycle/drift_flag.md` |
| 2 | **Protected Block Enforcement** | Attempted edit overlaps a `<!-- PROTECTED -->` span | • Abort WRITE<br>• Log `protectedOverlap`<br>• Require security review if `escalation: true` |
| 3 | **Write Gate Validation** | Target path not allowed by `/security/write_gates.md` | • Abort WRITE<br>• Log `gateViolation` |
| 4 | **Active Edit Lock** | `_locks/active_edit.lock` present at READ or WRITE start | • Halt loop in safe‑hold<br>• Prompt manual unlock if stale |
| 5 | **Pre/Post Hash Workflow** | Hash delta of protected/immutable files differs from plan | • Roll back WRITE<br>• Log `postHashMismatch`<br>• Flag drift |
| 6 | **High‑Risk Action Flag** | Job plan contains `requiresReview: true` or touches critical files (e.g. `system_manifest.md`) | • Suspend WRITE until review approved<br>• Record event in `security_review.md` |
---
##### 2. Metadata Quick‑Reference
| Marker | Effect |
|--------|--------|
| `fileType: immutable` | Seals file content; requires hash verification every loop |
| `editPolicy: readonly` | Disables all writes (immutable by intent) |
| `protected: true` | Marks inline block as untouchable, even if file is editable |
| `ttlCycles: N` | Governs expiry of temporary / evictable files |
| `requiresReview: true` | Forces human / elevated agent approval before WRITE |
---
##### 3. Hash Verification Workflow
1. **Pre‑WRITE**
   - Compute SHA‑256 for every file tagged `immutable` **or** containing a protected block.
   - Compare against `audit/integrity_snapshot.md`.
   - On any mismatch → **abort** and raise `hashMismatch`.
2. **Post‑WRITE**
   - Re‑hash the same set plus any files actually written.
   - Validate against `expectedHashAfter` in `/cascade/job_logs/temp_job.md`.
   - On success → append entry to `/cascade/change_log/recent.md`.
   - On failure → roll back write, set `drift_flag.md`.
---
##### 4. Protected Block Syntax
```md
<!-- PROTECTED -->
... uneditable content ...
<!-- END PROTECTED -->
```
- **Nested blocks** are not allowed.
- Attempting to insert, delete, or reorder text inside a protected span constitutes a `protectedOverlap` violation.
---
##### 5. Recovery & Escalation Paths
- **Safe‑Hold Mode**: Activated on any safeguard breach to prevent cascading corruption.
- **Loop Recovery**: Instructions in `/cascade/protocols/recovery.md` outline how to resume after drift resolution.
- **Security Review**: High‑risk or failed safeguards require a signed entry in `/cascade/security/security_review.md`.
- **Immutable Restore**: Use snapshots listed in `audit/integrity_snapshot.md` to roll back mutated files.
---
##### 6. Maintenance Guidance
- Update this file **only** through an approved security review.
- Keep safeguard IDs in the enforcement matrix **stable** for audit tooling.
- Align new safeguards with counters and thresholds defined in `file_lifespans.md`.
""")

add_file_content("cascade/protocols/recovery.md", """\
<!-- @meta {
  "fileType": "permanent",
  "purpose": "Structured fallback procedure triggered by safeguard failure, drift, or WRITE abortion.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
#### Recovery Protocol
This file governs how the system recovers when the loop fails due to safeguard violations, hash mismatches, or unresolved drift.
---
##### 1. Automatic Triggers
- Presence of `/lifecycle/drift_flag.md`
- WRITE aborted during `loop_protocol.md`
- Stale `_locks/active_edit.lock` preventing job completion
- Corrupted or missing `temp_job.md`
---
##### 2. Recovery Phases
###### Phase A — Diagnose
1. Halt all WRITE operations
2. Review `/audit/meta_audit.md` for safeguard or hash breach
3. Validate `audit/integrity_snapshot.md` against current file states
4. Verify `temp_job.md` plan integrity
###### Phase B — Contain & Flag
1. Move unstable or suspect files to `/quarantine/YYYY-MM-DD/`
2. If not already present, create `/lifecycle/drift_flag.md` with cause summary
3. Document all actions in `/audit/meta_audit.md`
###### Phase C — Restore
1. Use `integrity_snapshot.md` to replace corrupted `immutable` or `protected` files
2. Generate a minimal load plan referencing only core files (BOOTSTRAP, INDEX, MANIFEST)
3. Clear `drift_flag.md` only after successful plan load and hash check
---
##### 3. Manual Interventions
- Restoration steps require elevated agent or human confirmation
- Log each override in `/security/security_review.md` tagged `recovery`
---
##### 4. Emergency Halt
If integrity cannot be restored:
1. Archive `/cascade/` ➜ `/cascade_stale_YYYYMMDD/`
2. Rebootstrap using seed files
3. Transfer only audited summaries or logs
4. Log postmortem to `/audit/meta_audit.md` with `postmortem` tag
---
##### 5. Post-Recovery Actions
| File | Expected Update |
|------|------------------|
| `/audit/meta_audit.md` | Recovery event logged |
| `/change_log/recent.md` | Deltas appended |
| `/checkpoints/loop_checkpoint.md` | New checkpoint tagged `recovery-N` |
| `/lifecycle/drift_flag.md` | Deleted or archived |
| `/quarantine/` | Retain for 30 days minimum |
---
##### 6. Prevention Notes
- Validate `temp_job.md` for each cycle
- Monitor lifecycle counters for drift or stalling
- Run a dry loop audit (`read-only mode`) periodically
""")

# /cascade/lifecycle/ files
add_file_content("cascade/lifecycle/counter.md", """\
<!-- @meta {
  "fileType": "counter",
  "purpose": "Tracks global WRITE-phase activity across all domains.",
  "editPolicy": "incrementOnly",
  "routeScope": "global"
} -->
# Global Lifecycle Counter

This file tracks the total number of WRITE cycles that have occurred across the entire ContextCascade system.

**Current Count:**

0

---
## Usage
- This counter should be incremented by 1 after every successful WRITE phase, regardless of the domain(s) affected.
- It is used by `/protocols/file_lifespans.md` to trigger global `reread`, `prune`, or `merge` actions.
- Do not edit this file manually. It is managed by the ContextCascade system.

---
## Integrity
- Expected value: A non-negative integer.
- Monotonically increasing.
""")

add_file_content("cascade/lifecycle/client.md", """\
<!-- @meta {
  "fileType": "counter",
  "purpose": "Tracks WRITE-phase activity specifically for the 'client' domain.",
  "editPolicy": "incrementOnly",
  "routeScope": "client"
} -->
# Client Domain Lifecycle Counter

This file tracks the total number of WRITE cycles that have specifically impacted the 'client' domain.

**Current Count:**

0

---
## Usage
- This counter should be incremented by 1 after every successful WRITE phase that modifies one or more files within the `client` routeScope.
- It is used by `/protocols/file_lifespans.md` to trigger `reread`, `prune`, or `merge` actions specific to the client domain.
- Do not edit this file manually. It is managed by the ContextCascade system.

---
## Integrity
- Expected value: A non-negative integer.
- Monotonically increasing.
""")

add_file_content("cascade/lifecycle/server.md", """\
<!-- @meta {
  "fileType": "counter",
  "purpose": "Tracks WRITE-phase activity specifically for the 'server' domain.",
  "editPolicy": "incrementOnly",
  "routeScope": "server"
} -->
# Server Domain Lifecycle Counter

This file tracks the total number of WRITE cycles that have specifically impacted the 'server' domain.

**Current Count:**

0

---
## Usage
- This counter should be incremented by 1 after every successful WRITE phase that modifies one or more files within the `server` routeScope.
- It is used by `/protocols/file_lifespans.md` to trigger `reread`, `prune`, or `merge` actions specific to the server domain.
- Do not edit this file manually. It is managed by the ContextCascade system.

---
## Integrity
- Expected value: A non-negative integer.
- Monotonically increasing.
""")

add_file_content("cascade/lifecycle/schema.md", """\
<!-- @meta {
  "fileType": "counter",
  "purpose": "Tracks WRITE-phase activity specifically for the 'schema' domain.",
  "editPolicy": "incrementOnly",
  "routeScope": "schema"
} -->
# Schema Domain Lifecycle Counter

This file tracks the total number of WRITE cycles that have specifically impacted the 'schema' domain.

**Current Count:**

0

---
## Usage
- This counter should be incremented by 1 after every successful WRITE phase that modifies one or more files within the `schema` routeScope.
- It is used by `/protocols/file_lifespans.md` to trigger `reread`, `prune`, or `merge` actions specific to the schema domain.
- Do not edit this file manually. It is managed by the ContextCascade system.

---
## Integrity
- Expected value: A non-negative integer.
- Monotonically increasing.
""")

add_file_content("cascade/lifecycle/security.md", """\
<!-- @meta {
  "fileType": "counter",
  "purpose": "Tracks WRITE-phase activity specifically for high-risk actions and security events.",
  "editPolicy": "incrementOnly",
  "routeScope": "security"
} -->
# Security Lifecycle Counter

This file tracks the total number of WRITE cycles related to high-risk actions or security events, such as modifications to protected files or security policy changes.

**Current Count:**

0

---
## Usage
- This counter should be incremented by 1 after every successful WRITE phase involving operations flagged with `requiresReview: true`, modifications to files in `/cascade/security/`, or changes to `immutable` files after override.
- It is used by `/protocols/file_lifespans.md` to trigger `reread`, `prune`, or `merge` actions specific to security-related contexts, potentially more aggressively.
- Do not edit this file manually. It is managed by the ContextCascade system.

---
## Integrity
- Expected value: A non-negative integer.
- Monotonically increasing.
""")

add_file_content("cascade/lifecycle/drift_flag.md", """\
<!-- @meta {
  "fileType": "temporary",
  "purpose": "Signals an unresolved contradiction or deviation in the cascade lifecycle. Presence of this file may halt operations.",
  "editPolicy": "overwrite",
  "routeScope": "global",
  "ttlCycles": 1
} -->
# Drift Flag

**This file indicates a potential inconsistency or drift in the ContextCascade system.**

Its presence signifies that an unexpected state or behavior was detected, such as:
- A hash mismatch for an `immutable` or `protected` file.
- A lifecycle counter not incrementing as expected.
- A validator detecting a schema diff from a known snapshot.
- An unexpected file modification or deletion.

---
## Action Required
- **System Behavior:** The ContextCascade system may halt or enter a safe-hold mode when this file is present. Normal operations might be suspended until the drift is investigated and resolved.
- **Investigation:** Review `/audit/meta_audit.md` for detailed logs related to the detected drift.
- **Resolution:**
    1. Identify the cause of the drift.
    2. Take corrective actions as per `/cascade/protocols/recovery.md`. This might involve restoring files, correcting metadata, or acknowledging a deliberate change.
    3. Once the system state is verified and consistent, this flag file should be deleted or cleared as part of the recovery process.

---
## Content
This file may contain a brief, human-readable summary of the detected drift if generated by the system.

**Detected Drift (if any):**

No drift detected. System nominal.
""")

# /cascade/change_log/ files
add_file_content("cascade/change_log/recent.md", """\
<!-- @meta {
  "fileType": "rolling",
  "subtype": "buffer",
  "purpose": "A rolling log of the most recent WRITE cycle summaries, up to a defined maximum.",
  "editPolicy": "appendOnly",
  "routeScope": "global",
  "maxEntries": 7,
  "mergeTarget": "/cascade/change_log/summary.md"
} -->
# Recent Change Log

This file contains a rolling buffer of the most recent successfully completed WRITE cycle summaries. When this log exceeds `maxEntries` (7), the oldest entry is moved to `/cascade/change_log/summary.md`.

---
*(No entries yet)*
""")

add_file_content("cascade/change_log/summary.md", """\
<!-- @meta {
  "fileType": "append-only",
  "purpose": "A permanent, append-only historical log of all WRITE cycle summaries, including those rolled over from recent.md.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Change Log Summary

This file is an append-only historical ledger of all successfully completed WRITE cycles. It includes entries merged from `/cascade/change_log/recent.md` when that buffer reaches its `maxEntries` limit.

---
## Guidelines
- Entries are added chronologically.
- Existing entries must not be modified or deleted.
- Each entry should provide a concise summary of a WRITE cycle, including:
    - Loop ID or timestamp.
    - Job plan reference.
    - Summary of modified files.
    - Outcome status (e.g., success, rolledBack, partial).
    - Post-WRITE hash confirmation status.

---
*(No entries yet)*
""")

# /cascade/job_logs/ files
add_file_content("cascade/job_logs/temp_job.md", """\
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
""")

add_file_content("cascade/job_logs/recent.md", """\
<!-- @meta {
  "fileType": "rolling",
  "subtype": "buffer",
  "purpose": "A rolling log of the most recent job plan summaries, up to a defined maximum.",
  "editPolicy": "appendOnly",
  "routeScope": "global",
  "maxEntries": 5,
  "mergeTarget": "/cascade/job_logs/summary.md"
} -->
# Recent Job Logs

This file contains a rolling buffer of summaries from recently executed job plans (from `temp_job.md`). When this log exceeds `maxEntries` (5), the oldest entry is moved to `/cascade/job_logs/summary.md`.

Each entry should summarize a completed job, including:
- Job ID (could be a timestamp or a unique hash of the plan).
- Intent of the job.
- Key files affected.
- Status (e.g., success, failed, rolled_back).

---
*(No job summaries yet)*
""")

add_file_content("cascade/job_logs/summary.md", """\
<!-- @meta {
  "fileType": "append-only",
  "purpose": "A permanent, append-only historical log of all job plan summaries, including those rolled over from job_logs/recent.md.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Job Logs Summary

This file is an append-only historical ledger of all executed job plan summaries. It includes entries merged from `/cascade/job_logs/recent.md` when that buffer reaches its `maxEntries` limit.

---
## Guidelines
- Entries are added chronologically.
- Existing entries must not be modified or deleted.
- Each entry should provide a concise summary of an executed job plan, typically including:
    - Job ID or reference to the original `temp_job.md` (e.g., its hash or timestamp).
    - The stated `intent` of the job.
    - A list of key files targeted by the job.
    - The final `status` of the job (e.g., success, failure, rolled_back).
    - Timestamp of execution.

---
*(No job summaries yet)*
""")


# /cascade/load_plans/ files
add_file_content("cascade/load_plans/.gitkeep", "")
add_file_content("cascade/load_plans/auto_plan_generic.md", """\
<!-- @meta {
  "fileType": "evictable",
  "ttlCycles": 2,
  "routeScope": "global",
  "purpose": "Generic auto-generated load plan. Defines files to be read in the next cycle.",
  "editPolicy": "overwrite"
} -->
# Auto-Generated Load Plan (Generic)

This file specifies the set of files to be loaded into context for the next READ phase. It is typically generated by the AI during the ACT phase of the previous cycle.

This is a generic placeholder. Specific load plans might be scoped by domain (e.g., `auto_plan_client.md`) or task.

---
## Files to Load:

- `/cascade/00_BOOTSTRAP.md`
- `/cascade/index.md`
- `/cascade/system_manifest.md`
- `/cascade/protocols/loop_protocol.md`
- `/cascade/protocols/file_lifespans.md`
- `/cascade/lifecycle/counter.md`
- `/cascade/change_log/recent.md`
- `/cascade/job_logs/recent.md`

*(This list should be dynamically generated based on the current task, routeScope, token budget, and lifecycle triggers.)*

---
## Instructions for AI:
- During the ACT phase, evaluate the needs for the next cycle.
- Generate a new file (or overwrite an existing one like this) in `/cascade/load_plans/` that lists the precise files required.
- Consider `routeScope`, `readPriority` from file metadata, `ttlCycles` of existing plans, and overall token budget.
- This plan will be consumed at the start of the next READ phase.
- If `ttlCycles` expires, this plan may be automatically pruned.
""")

# /cascade/_taskbuffers/ files
add_file_content("cascade/_taskbuffers/.gitkeep", "")
add_file_content("cascade/_taskbuffers/scratchpad.md", """\
<!-- @meta {
  "fileType": "temporary",
  "subtype": "temp",
  "purpose": "A temporary scratchpad for single-prompt use. Content does not persist beyond the current cycle.",
  "editPolicy": "overwrite",
  "ttlCycles": 1
} -->
# Scratchpad

This is a temporary buffer for notes, draft content, or intermediate thoughts relevant only to the current prompt or execution cycle.

---
## Usage
- Feel free to write any transient data here during the ACT phase.
- The content of this file is not guaranteed to persist beyond the current READ-ACT-WRITE cycle.
- It will be automatically deleted or cleared after 1 cycle (`ttlCycles: 1`).
- Do not store critical or long-term information here. Use appropriate logs, domain files, or summaries for that.

---
*(Content here is ephemeral and will be overwritten or deleted frequently)*
""")

# /cascade/temp_notes/ files
add_file_content("cascade/temp_notes/.gitkeep", "")
add_file_content("cascade/temp_notes/planning_notes_global.md", """\
<!-- @meta {
  "fileType": "rolling",
  "subtype": "buffer",
  "purpose": "Rolling buffer for ongoing planning notes, ideas, or multi-step task tracking.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global",
  "maxEntries": 10,
  "mergePolicy": "squash",
  "mergeTarget": "/cascade/change_log/summary.md"
} -->
# Global Planning Notes (Rolling)

This file serves as a rolling buffer for general planning notes, ideas, or tracking multi-step tasks that span several cycles.

---
## Usage
- Append new notes or update existing sections.
- When `maxEntries` (e.g., 10, as an example here) is reached, older entries might be evicted or merged.
- The `mergePolicy` (e.g., `squash`) and `mergeTarget` (e.g., `/cascade/change_log/summary.md`) would define how its content is preserved long-term if needed, though these are illustrative here and should be set based on actual workflow.
- For domain-specific planning, consider creating separate files (e.g., `planning_notes_client.md`).

---
## Current Notes:

*(No notes yet. Add dated entries or task-specific sections below.)*

---
### Example Entry Format:
```
---
**Date:** YYYY-MM-DD
**Task/Topic:** Brief description
**Notes:**
- Point 1
- Point 2
- Action items...
---
```
""")

# /cascade/security/ files
add_file_content("cascade/security/security_review.md", """\
<!-- @meta {
  "fileType": "append-only",
  "purpose": "Log of manual or AI-driven security reviews, findings, and approvals for high-risk actions.",
  "editPolicy": "appendOnly",
  "routeScope": "security"
} -->
# Security Review Log

This file contains an append-only log of all security reviews conducted. This includes reviews for:
- High-risk actions flagged with `requiresReview: true` in job plans.
- Modifications to critical system files (e.g., `system_manifest.md`, protocol files).
- Escalated permissions or overrides of `readonly`, `immutable`, or `protected` policies.
- Findings from manual or automated security audits.
- Approvals or rejections of proposed changes.

---
## Entry Format
Each entry should be clearly timestamped and include:
- **Date/Timestamp:** When the review was conducted.
- **Reviewer(s):** Who conducted the review (human agent ID or AI agent version).
- **Subject:** What was reviewed (e.g., Job Plan ID, file path, proposed change).
- **Details/Findings:** A summary of the review process and any findings.
- **Decision/Outcome:** Approved, Rejected, Needs More Info, etc.
- **Rationale:** Justification for the decision.
- **Associated Hashes:** (If applicable) Hashes of files before and after an approved change.

---
## Example Entry:
```
---
**Date/Timestamp:** 2025-07-15T10:30:00Z
**Reviewer(s):** human_admin_chris, ai_agent_jules_v1.2
**Subject:** Proposed modification to `/cascade/system_manifest.md` (Job Plan: job_temp_a1b2c3d4)
**Details/Findings:**
- Intent: Add new domain 'experimental_features'.
- Impact assessment: Low risk, isolated domain.
- Hash before: manifest_hash_v1_old
- Hash after (proposed): manifest_hash_v2_new
**Decision/Outcome:** Approved
**Rationale:** The new domain is well-defined and does not interfere with existing core domains. All necessary index files for the domain are included in the job plan.
**Associated Hashes:**
- `/cascade/system_manifest.md` (before): sha256-abc...
- `/cascade/system_manifest.md` (after): sha256-def...
---
```

---
*(No review entries yet)*
""")

add_file_content("cascade/security/write_gates.md", """\
<!-- @meta {
  "fileType": "permanent",
  "purpose": "Defines glob patterns and path constraints to control which files can be written to. Acts as a write-time firewall.",
  "editPolicy": "appendOrReplace",
  "routeScope": "security"
} -->
# Write Gates Policy

This file defines the write gate policies for the ContextCascade system. It uses glob patterns and explicit path declarations to allow or deny write operations to specific files or directories. This acts as a crucial safeguard to prevent unintended or unauthorized modifications.

---
## Gate Configuration Format
Write gates are typically defined in a structured format, often YAML-like, within this document. The system will parse this section to enforce rules during the pre-WRITE validation phase.

**Key Principles:**
- **Deny by Default (Recommended):** It's often safer to deny writes to broad areas and then explicitly allow specific paths.
- **Specificity:** More specific rules usually override broader ones (though the exact precedence logic depends on the validator's implementation).
- **`allow` vs. `deny`:** Clearly state the intent.
- **`appendOnly` flag:** Can be used to allow writes but only in append mode for certain paths.

---
## Example Gate Configuration:
```yaml
writeGates:
  # Deny writes to all protocol files by default
  - deny: "/cascade/protocols/*"
  # But allow appendOrReplace to file_lifespans if specifically planned
  - allow: "/cascade/protocols/file_lifespans.md"
    editPolicy: "appendOrReplace" # Explicitly state allowed edit type

  # Immutable files - generally deny all direct writes
  - deny: "/cascade/00_BOOTSTRAP.md"
  - deny: "/cascade/system_manifest.md"
  - deny: "/cascade/init_context.md"
  # (Overrides for immutable files should be exceptional and logged via security_review.md)

  # Allow writes to job logs (temp_job is overwrite, others appendOnly)
  - allow: "/cascade/job_logs/temp_job.md"
    editPolicy: "overwrite"
  - allow: "/cascade/job_logs/recent.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/job_logs/summary.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/job_logs.md" # The index file
    editPolicy: "appendOrReplace"


  # Allow writes to change logs (recent is appendOnly, summary is appendOnly)
  - allow: "/cascade/change_log/recent.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/change_log/summary.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/change_log.md" # The index file
    editPolicy: "appendOrReplace"

  # Lifecycle counters are incrementOnly (a form of append)
  - allow: "/cascade/lifecycle/*.md" # Individual counters
    editPolicy: "incrementOnly" # Or appendOnly if incrementOnly is not a direct metadata policy
  - allow: "/cascade/lifecycle.md" # The index file
    editPolicy: "appendOrReplace"


  # Load plans are evictable and can be overwritten
  - allow: "/cascade/load_plans/*.md"
    editPolicy: "overwrite"

  # Taskbuffers are temporary and can be overwritten
  - allow: "/cascade/_taskbuffers/*.md"
    editPolicy: "overwrite"

  # Temp notes are rolling and can be appended to or sections replaced
  - allow: "/cascade/temp_notes/*.md"
    editPolicy: "appendOrReplace"

  # Audit files are generally append-only or managed by specific processes
  - allow: "/cascade/audit/meta_audit.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/audit/token_summary.md" # May be overwritten by analysis tools
    editPolicy: "overwrite"
  - allow: "/cascade/audit/integrity_snapshot.md" # Usually appendOnly, or specific update process
    editPolicy: "appendOnly"
  - allow: "/cascade/audit/prune_plan.md" # Evictable, can be overwritten
    editPolicy: "overwrite"


  # Checkpoints are append-only
  - allow: "/cascade/checkpoints/loop_checkpoint.md"
    editPolicy: "appendOnly"

  # Domain files - index files are often appendOnly or appendOrReplace
  # Content files within domains might have varying policies
  - allow: "/cascade/domains/*/index.md"
    editPolicy: "appendOrReplace"
  - allow: "/cascade/domains/*/*.md" # Be more specific for actual domain content files
    editPolicy: "appendOrReplace" # Default, can be overridden by file's own metadata

  # Security files themselves
  - allow: "/cascade/security/security_review.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/security/write_gates.md" # This file itself
    editPolicy: "appendOrReplace" # Needs to be editable, but with high review threshold

  # Meta files
  - allow: "/cascade/_meta/*.md"
    editPolicy: "appendOrReplace" # e.g., for cascade_feature_index.md

  # Deny everything else within /cascade/ by default if not explicitly allowed
  # This is a strong safeguard but requires diligent 'allow' rules.
  # - deny: "/cascade/**" (Use with caution and ensure all legitimate paths are allowed above)

```
---
## Current Gate Configuration:

# (Define your YAML or structured list of rules here)
# Example:
writeGates:
  - deny: "/cascade/protocols/*"
  - allow: "/cascade/protocols/file_lifespans.md"
    editPolicy: "appendOrReplace"
  - deny: "/cascade/00_BOOTSTRAP.md"
  - deny: "/cascade/system_manifest.md"
  - deny: "/cascade/init_context.md"
  - allow: "/cascade/job_logs/temp_job.md"
    editPolicy: "overwrite"
  - allow: "/cascade/job_logs/*.md" # recent.md, summary.md, job_logs.md (index)
    editPolicy: "appendOnly" # Default, specific files can refine
  - allow: "/cascade/change_log/*.md" # recent.md, summary.md, change_log.md (index)
    editPolicy: "appendOnly" # Default
  - allow: "/cascade/lifecycle/*.md"
  - allow: "/cascade/lifecycle.md"
    editPolicy: "appendOrReplace"
  - allow: "/cascade/load_plans/*.md"
    editPolicy: "overwrite"
  - allow: "/cascade/_taskbuffers/*.md"
    editPolicy: "overwrite"
  - allow: "/cascade/temp_notes/*.md"
    editPolicy: "appendOrReplace"
  - allow: "/cascade/audit/meta_audit.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/audit/token_summary.md"
    editPolicy: "overwrite"
  - allow: "/cascade/audit/integrity_snapshot.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/audit/prune_plan.md"
    editPolicy: "overwrite"
  - allow: "/cascade/checkpoints/loop_checkpoint.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/domains/**" # Broad allow for domains, individual files should have stricter policies
    editPolicy: "appendOrReplace"
  - allow: "/cascade/security/security_review.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/security/write_gates.md" # This file
    editPolicy: "appendOrReplace"
  - allow: "/cascade/_meta/*.md"
    editPolicy: "appendOrReplace"
  - allow: "/cascade/index.md"
    editPolicy: "appendOnly"

---
## Maintenance
- Changes to this file are considered high-risk and **must** be logged in `/cascade/security/security_review.md`.
- Regularly audit these gates against the actual file structure and intended edit policies.
- Ensure the parsing logic in the AI agent or validator correctly interprets these rules.
""")

# /cascade/audit/ files
add_file_content("cascade/audit/integrity_snapshot.md", """\
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
""")

add_file_content("cascade/audit/meta_audit.md", """\
<!-- @meta {
  "fileType": "append-only",
  "purpose": "A persistent log for drift, contradictions, anomalies, safeguard violations, or other significant meta-level system events.",
  "editPolicy": "appendOnly",
  "routeScope": "audit"
} -->
# Meta Audit Log

This file serves as an append-only log for critical system events, particularly those related to inconsistencies, safeguard violations, lifecycle deviations, and recovery actions. It is a key resource for debugging, understanding system behavior, and ensuring traceability.

---
## Logged Events
This log should capture events such as:
- **Drift Detection:**
    - `hashMismatch`: An `immutable` or `protected` file's hash does not match the `integrity_snapshot.md`.
    - `validatorDiff`: Schema or structural differences detected by validators.
    - `unexpectedMutation`: A file was changed without a corresponding job plan.
    - `counterSkip`: A lifecycle counter did not increment as expected.
- **Safeguard Violations:**
    - `protectedOverlap`: Attempted edit within a `<!-- PROTECTED -->` block.
    - `gateViolation`: Write attempt blocked by `/security/write_gates.md`.
    - `lockConflict`: `active_edit.lock` prevented an operation.
    - `immutableWriteAttempt`: Attempt to write to an `immutable` file without proper override.
- **Lifecycle Events:**
    - `recovery-start`: Recovery protocol initiated.
    - `recovery-step`: Specific actions taken during recovery.
    - `recovery-complete`: Recovery protocol finished.
    - `staleFilePruned`: An expired file was removed.
    - `summaryMerge`: Details of a summary merge operation.
- **Security Events:**
    - `securityReviewTriggered`: A high-risk action requiring review was initiated.
    - `permissionEscalation`: An operation required escalated privileges.
- **External Integration Events:**
    - `externalHookSent`: An external hook was triggered.
    - `externalHookFailed`: An external hook failed.

---
## Entry Format
Each entry should be clearly timestamped and structured, potentially using a consistent format (e.g., Markdown list items, YAML blocks, or JSON objects if preferred for machine parsing).

**Example Markdown List Item Format:**
```
---
- **Timestamp:** YYYY-MM-DDTHH:mm:ssZ
  **Type:** `hashMismatch`
  **Severity:** CRITICAL
  **Details:** Hash for `/cascade/system_manifest.md` does not match `integrity_snapshot.md`. Expected: `abc...`, Actual: `def...`.
  **Source:** Pre-WRITE validation (Loop ID: 157)
  **ActionTaken:** WRITE aborted. `/lifecycle/drift_flag.md` raised.
---
- **Timestamp:** YYYY-MM-DDTHH:mm:ssZ
  **Type:** `recovery-start`
  **Severity:** INFO
  **Details:** Recovery protocol initiated due to `drift_flag.md`.
  **Source:** System Recovery Agent
---
```

---
## Current Audit Log:

*(This log is appended to by the system as events occur. No entries yet.)*

---
## Maintenance
- This file is append-only. Existing entries must not be altered.
- Ensure consistent formatting for entries to aid parsing and review.
- Regularly review this log for patterns or recurring issues.
- For very high-volume systems, consider log rotation strategies if file size becomes an issue, though the primary intent is a persistent, complete record.
""")

add_file_content("cascade/audit/prune_plan.md", """\
<!-- @meta {
  "fileType": "evictable",
  "purpose": "Defines and executes controlled cleanup operations for temporary, expired, or unnecessary files.",
  "editPolicy": "overwrite",
  "routeScope": "audit",
  "ttlCycles": 3
} -->
# Prune Plan

This file outlines the policies and can trigger actions for deleting or archiving temporary, expired, or unnecessary files from the ContextCascade system. Its goal is to prevent performance degradation, memory bloat, and stale context leakage.

---
## Pruning Policies & Targets
This section defines what gets pruned and when. Policies are typically based on file metadata like `fileType`, `ttlCycles`, and `expirationPolicy`.

**Common Targets for Pruning:**
- **`temporary` files:** Files in `_taskbuffers/`, `job_logs/temp_job.md` (after `ttlCycles: 1` by default).
- **`evictable` files:** Files in `load_plans/` or other cache-like locations after their `ttlCycles` expire.
- **`rolling` buffers (entries):** Old entries in rolling buffers if not handled by merge logic (though merging is preferred).
- **Stale `active_edit.lock` files:** If `_locks/active_edit.lock` is old and no process is active.
- **Empty directories:** Directories that become empty after pruning.

---
## Pruning Triggers
Pruning can be triggered:
1.  **Automatically:**
    *   At the end of a WRITE cycle, based on `ttlCycles` countdowns.
    *   When lifecycle counters hit `prune_threshold` as defined in `/protocols/file_lifespans.md`.
2.  **Manually/AI-Initiated:**
    *   By an explicit prompt or command (e.g., "Execute prune plan to clear expired files").
    *   As part of a recovery process (`/protocols/recovery.md`).
3.  **Scheduled:** (If the system supports it) As a periodic maintenance task.

---
## Example Prune Plan Execution Script/Instructions (Conceptual)
This section could contain a plan that the AI executes.

```
## Prune Plan - YYYY-MM-DD

**Objective:** Clean up expired and temporary files.

**Phase 1: Identify Candidates**
1. Scan all files with `fileType: temporary`.
   - If `ttlCycles` has reached 0 or is not set (defaults to 1 for temporary), mark for deletion.
2. Scan all files with `fileType: evictable`.
   - If `ttlCycles` has reached 0, mark for deletion.
3. Check `/cascade/_locks/active_edit.lock`:
   - If timestamp older than (e.g., 1 hour) AND no active write process confirmed, mark for deletion.
4. List all files marked for deletion.

**Phase 2: Review (Optional)**
- Present list of files to be pruned to user/AI for confirmation if in interactive mode or if total size > X MB.

**Phase 3: Execute Pruning**
1. For each marked file:
   - If `expirationPolicy: archiveOnExpire` is set, move to `/cascade/_archive/YYYY-MM-DD/` (maintaining path).
   - Else, delete the file.
2. Log all actions (deleted/archived files) to `/cascade/audit/meta_audit.md` with type `staleFilePruned` or `fileArchived`.

**Phase 4: Cleanup**
1. Scan for any empty directories within `/cascade/` (except `_taskbuffers`, `load_plans`, `temp_notes` which might be intentionally empty awaiting new files) and list them for potential removal if policy dictates.

---
```

## Current Prune Plan Status:

*(This file is `evictable` and `overwrite`. It would be generated or updated when a prune operation is planned or executed. Currently idle.)*

**Last Execution:** (Timestamp or N/A)
**Next Scheduled (if applicable):** (Timestamp or N/A)

---
## Instructions for AI:
- To initiate a prune, you can generate a specific execution plan in this file (as per the example above).
- Then, during an ACT phase, reason over this plan and prepare the necessary delete/archive operations for the WRITE phase.
- Always log pruning actions to `/cascade/audit/meta_audit.md`.
- Respect `expirationPolicy` metadata on files. If `archiveOnExpire` is set, move the file instead of deleting.
""")

add_file_content("cascade/audit/token_summary.md", """\
<!-- @meta {
  "fileType": "permanent",
  "purpose": "Tracks estimated and actual token footprints of files and cascade branches to aid in budget awareness.",
  "editPolicy": "appendOrReplace",
  "routeScope": "audit"
} -->
# Token Usage Summary

This file stores data related to the token footprint of files and cascade branches. It helps the AI maintain token budget awareness, make informed decisions during context loading (especially in Lean Mode), and anticipate memory usage.

---
## Structure
This file might contain:
- **Per-file estimates:**
    - File path.
    - Estimated token count (based on heuristics, word count, or previous actuals).
    - Actual token count from the last time it was loaded.
    - Timestamp of the last actual count.
- **Per-domain/branch summaries:**
    - Domain path (e.g., `/cascade/client/`).
    - Total estimated token count for all files in that domain.
    - Total actual token count.
- **Global summary:**
    - Total estimated and actual token counts for the entire cascade.

---
## Example Content:
```
## Global Summary
- Total Estimated Tokens: 15200
- Total Actual Tokens (last full load): 14850
- Last Full Load Timestamp: 2025-07-15T10:00:00Z

---
## Per-Domain Summaries

### /cascade/client/
- Estimated Tokens: 3500
- Actual Tokens: 3320
- Files Tracked: 5

### /cascade/protocols/
- Estimated Tokens: 1200
- Actual Tokens: 1150
- Files Tracked: 4

---
## Per-File Details (Sample)

| File Path                          | Estimated Tokens | Actual Tokens (Last Load) | Last Actual Timestamp  |
|------------------------------------|------------------|---------------------------|------------------------|
| /cascade/00_BOOTSTRAP.md           | 150              | 145                       | 2025-07-15T09:00:00Z   |
| /cascade/index.md                  | 200              | 190                       | 2025-07-15T09:00:00Z   |
| /cascade/domains/client/index.md   | 450              | 430                       | 2025-07-15T09:05:00Z   |
| ...                                | ...              | ...                       | ...                    |

```

---
## Current Token Summary:

*(This section should be populated by an automated process or the AI based on file analysis and loading history.)*

**Last Updated:** (Timestamp)

*(No summary data yet)*

---
## Maintenance
- The AI or an external script should periodically update this file.
- Estimates can be generated via dry-run parsing or using heuristics.
- Actual token counts should be logged after files are loaded into context.
- This file itself can become large; consider strategies for summarization or rotation if it impacts performance.
- `editPolicy: appendOrReplace` allows for the file to be wholly updated by a token counting process.
""")

# /cascade/checkpoints/ files
add_file_content("cascade/checkpoints/loop_checkpoint.md", """\
<!-- @meta {
  "fileType": "append-only",
  "purpose": "Sequential log recording the successful completion of each full READ-ACT-WRITE cascade loop.",
  "editPolicy": "appendOnly",
  "routeScope": "audit"
} -->
# Loop Checkpoint Log

This file contains an append-only, sequential log that records the successful completion of each full ContextCascade loop (READ → ACT → WRITE). It serves as a crucial audit trail for system progression, rollback orchestration, and session reconstruction.

---
## Entry Format
Each entry signifies one successfully completed loop and should be recorded after all post-WRITE tasks (hash checks, confirmations, summary updates) are finished.

A structured format is recommended for each entry:

```
---
- **LoopID:** (Sequential integer or unique identifier, e.g., timestamp or global counter value)
  **Timestamp:** YYYY-MM-DDTHH:mm:ssZ (UTC)
  **JobPlanReference:** (Path or hash of the `job_logs/temp_job.md` that was executed)
  **FilesWritten:**
    - path: `/path/to/file1.md`
      hashAfter: "sha256-hash1..."
    - path: `/path/to/file2.md`
      hashAfter: "sha256-hash2..."
  **CountersIncremented:**
    - global: value_after
    - client: value_after (if client domain was affected)
    - server: value_after (if server domain was affected)
    - ... (other affected domain counters)
  **Outcome:** `success` (This file should only log successful loops. Failures are logged in `meta_audit.md`)
  **PostHashCheck:** `confirmed` | `warning` (if minor, non-critical discrepancies were noted but accepted)
---
```

---
## Usage
- **Traceability:** Provides a clear history of system operations.
- **Rollback:** Helps identify known-good states to roll back to if drift or corruption occurs.
- **Session Reconstruction:** Can assist in understanding the sequence of operations during an audit or debugging session.
- **Drift Detection:** Gaps in LoopIDs or timestamps might indicate missed cycles or system interruptions, prompting a look at `meta_audit.md`.

---
## Current Checkpoints:

*(This log is appended to by the system automatically after each successful WRITE cycle. No checkpoints yet.)*

---
## Maintenance
- This file is strictly append-only. Existing entries must never be modified or deleted.
- Ensure the LoopID is unique and preferably sequential.
- If a WRITE cycle fails or is aborted, no entry should be written here for that cycle. Failures are documented in `/cascade/audit/meta_audit.md`.
""")

# /cascade/domains/client/ files
add_file_content("cascade/domains/client/index.md", """\
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
| `architecture.md`         | Client-side architecture decisions | `permanent`              |
| `key_decisions.md`        | Key architectural decisions        | `permanent`              |
| `README.md`               | Overview of client domain memory   | `permanent`              |
| `conventions.md`          | Client coding/naming conventions   | `permanent`              |
| `state_management.md`     | Client state management strategy   | `permanent`              |
| `components/`             | Directory for component specs      | (directory)              |
| `components/button.md`    | Specification for Button component | `permanent`              |
| `api_interfaces.md`       | Client-side view of API contracts  | `permanent`              |
| `client_summary.md`       | Rolling summary of client changes  | `rolling`                |

*(This is an example structure. Populate with actual files as they are created for the client domain.)*

---
## Current Client Domain Index:

| Path                                             | Role / Description                 |
|--------------------------------------------------|------------------------------------|
| `/cascade/domains/client/architecture.md`        | Client-side architecture decisions |
| `/cascade/domains/client/key_decisions.md`       | Key architectural decisions        |
| `/cascade/domains/client/README.md`              | Overview of client domain memory   |


*(Add more entries as client-specific memory files are created.)*
""")

add_file_content("cascade/domains/client/architecture.md", """\
<!-- @meta {
  "fileType": "permanent",
  "purpose": "Documents the client-side architecture decisions and patterns.",
  "editPolicy": "appendOrReplace",
  "routeScope": "client"
} -->
# Client Architecture

This document outlines the high-level architecture for the client-side of the application.

*(Content to be filled in, e.g., chosen framework (React, Vue, Angular), state management approach (Redux, Vuex, Context API), component structure, key libraries, build process, etc.)*
""")

add_file_content("cascade/domains/client/key_decisions.md", """\
<!-- @meta {
  "fileType": "permanent",
  "purpose": "Records key architectural and technical decisions made for the client domain.",
  "editPolicy": "appendOnly",
  "routeScope": "client"
} -->
# Key Decisions (Client Domain)

This document is an append-only log of significant architectural and technical decisions made for the client domain.

---
## Format
Each entry should include:
- **Date:** YYYY-MM-DD
- **Decision:** A clear statement of the decision made.
- **Rationale:** The reasons behind the decision, alternatives considered, and trade-offs.
- **Impact:** Expected impact on the client application.
- **Status:** Proposed, Accepted, Deprecated.

---
### Example Entry
```
---
**Date:** 2023-10-26
**Decision:** Adopt Zustand for global state management.
**Rationale:** Lightweight, simple API, good performance, and less boilerplate compared to Redux for our current needs. Context API was considered but Zustand offers betterdevtools and performance characteristics for complex states.
**Impact:** Affects how new features manage shared state. Existing Context API usages to be refactored incrementally.
**Status:** Accepted
---
```

*(Add new decisions as they are made.)*
""")

add_file_content("cascade/domains/client/README.md", """\
<!-- @meta {
  "fileType": "permanent",
  "purpose": "Overview of the client domain memory within ContextCascade.",
  "editPolicy": "appendOrReplace",
  "routeScope": "client"
} -->
# Client Domain README

This file provides an overview of the memory and guidance documents stored within the `/cascade/domains/client/` directory. These documents are intended to guide AI and human developers in maintaining and extending the client-side of the application consistently.

Refer to `/cascade/domains/client/index.md` for a full list of documents in this domain.
""")


# /cascade/domains/schema/ files
add_file_content("cascade/domains/schema/index.md", """\
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

*(This is an example structure. Populate with actual files as they are created for the schema domain.)*

---
## Current Schema Domain Index:

| Path                                     | Role / Description               |
|------------------------------------------|----------------------------------|
| `/cascade/domains/schema/README.md`      | Overview of schema domain memory |

*(Add more entries as schema-specific memory files are created.)*
""")

add_file_content("cascade/domains/schema/README.md", """\
<!-- @meta {
  "fileType": "permanent",
  "purpose": "Overview of the schema domain memory within ContextCascade.",
  "editPolicy": "appendOrReplace",
  "routeScope": "schema"
} -->
# Schema Domain README

This file provides an overview of the memory and guidance documents stored within the `/cascade/domains/schema/` directory. These documents pertain to data schemas, API contracts, validation rules, and other structural definitions.

Refer to `/cascade/domains/schema/index.md` for a full list of documents in this domain.
""")


# /cascade/domains/server/ files
add_file_content("cascade/domains/server/index.md", """\
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

*(This is an example structure. Populate with actual files as they are created for the server domain.)*

---
## Current Server Domain Index:

| Path                                   | Role / Description               |
|----------------------------------------|----------------------------------|
| `/cascade/domains/server/README.md`    | Overview of server domain memory |

*(Add more entries as server-specific memory files are created.)*
""")

add_file_content("cascade/domains/server/README.md", """\
<!-- @meta {
  "fileType": "permanent",
  "purpose": "Overview of the server domain memory within ContextCascade.",
  "editPolicy": "appendOrReplace",
  "routeScope": "server"
} -->
# Server Domain README

This file provides an overview of the memory and guidance documents stored within the `/cascade/domains/server/` directory. These documents pertain to the backend logic, APIs, services, and overall server-side architecture.

Refer to `/cascade/domains/server/index.md` for a full list of documents in this domain.
""")


# /cascade/_locks/ files
add_file_content("cascade/_locks/active_edit.lock", """\
<!-- @meta {
  "fileType": "temporary",
  "subtype": "editSession",
  "purpose": "Prevents concurrent WRITE operations by signalling an active edit session.",
  "editPolicy": "replaceOnly",
  "routeScope": "global",
  "ttlCycles": 1,
  "linkedAudits": ["audit/meta_audit.md", "lifecycle/drift_flag.md"]
} -->

### /_locks/active_edit.md

> **Role:** Acts as a mutex for high-integrity WRITE phases.
> If this lock is present and `status` ≠ `cleared`, any new job plan must halt until the lock is released or deemed **stale**.

---

#### Current Lock (state is overwritten every loop)

| Timestamp (UTC)       | Locked By | Scope   | Job ID  | Status       |
|-----------------------|-----------|---------|---------|--------------|
| _none_                | —         | —       | —       | cleared      |

**Status values**

| Value        | Meaning                                                    |
|--------------|------------------------------------------------------------|
| `in-progress`| WRITE or MERGE currently running                           |
| `failed`     | Job aborted; manual review needed before clearing          |
| `stale`      | TTL elapsed without matching Job ID; safe-to-clear flag    |
| `cleared`    | No active lock; safe to initiate new WRITE session         |

---

#### Lock Workflow

1. **WRITE-start** → loop controller writes lock entry (`in-progress`).
2. **WRITE-end**   → controller updates `status: cleared` *or* `failed`.
3. **Next loop**   → if `status` ≠ `cleared`, ACT halts planning, logs issue:
   - `/lifecycle/drift_flag.md` (flag)
   - `/audit/meta_audit.md`  (audit row)

If `status` becomes `stale`, a maintenance job can replace this file with the placeholder **cleared** row above.

---

**Summary**
`active_edit.md` enforces sequential state commits, protecting the cascade from race-condition corruption. Keep it overwrite-only and ensure every WRITE phase ends with a `cleared` status—or a flagged audit trail if problems arise.
""")


# /cascade/_meta/ files
add_file_content("cascade/_meta/cascade_feature_index.md", """\
<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Master feature catalogue and directory reference for the ContextCascade system. Derived from system documentation.",
  "editPolicy": "appendOrReplace",
  "routeScope": "meta"
} -->
# ContextCascade Feature Index & Catalogue

This document provides a comprehensive index of all first-class features within the ContextCascade system, along with brief descriptions and references to their primary documentation or defining files. It is intended to be a quick reference for understanding the system's capabilities.

---
## Core Features

1.  **Metadata Blocks**
    *   **What**: Structured JSON-in-comment headers at the top of each file defining operational context.
    *   **Why**: Encode attributes like `fileType`, `editPolicy`, `ttlCycles`, `routeScope` for automated behavior.
    *   **Where**: All `.md` files in `/cascade/`. Validated by `validators/metadata_validator.ts`.
    *   **Ref**: Documentation §2.5.1, §4.

2.  **Canonical FileType Registry**
    *   **What**: Formal registry of nine allowed file types (`permanent`, `immutable`, `rolling`, `append-only`, `temporary`, `counter`, `evictable`, `protected`, `structural`) and their aliases.
    *   **Why**: Ensures consistent interpretation of file semantics.
    *   **Where**: Defined in Documentation §3.2.1. Enforced by `validators/metadata_validator.ts`.
    *   **Ref**: Documentation §2.5.2, §3.2.1.

3.  **Read → ACT → WRITE Loop Protocol**
    *   **What**: Disciplined three-phase protocol (Read, Act, Write) for every execution cycle.
    *   **Why**: Ensures clarity, auditability, and safety.
    *   **Where**: Defined in `/cascade/protocols/loop_protocol.md`.
    *   **Ref**: Documentation §2.5.3, `/cascade/protocols/loop_protocol.md`.

4.  **Load Modes (Lean, Domain, Full)**
    *   **What**: Hierarchical strategies for reading context files (`Lean`, `Domain`, `Full`).
    *   **Why**: Balances token budget and contextual completeness.
    *   **Where**: Logic in `protocols/load_mode_logic.md` (conceptual, actual file may vary). Referenced by load plans and lifecycle counters.
    *   **Ref**: Documentation §2.5.4.

5.  **Load Plans**
    *   **What**: Ephemeral markdown files defining the set of files for the next READ phase.
    *   **Why**: Optimizes token use and ensures relevant context ingestion.
    *   **Where**: `/cascade/load_plans/*.md` (e.g., `auto_plan_client.md`).
    *   **Ref**: Documentation §2.5.5.

6.  **Lifecycle Counters**
    *   **What**: `.md` files tracking update activity for specific domains/contexts (e.g., `client_tick.md`).
    *   **Why**: Trigger threshold-based logic (reloads, pruning, drift detection).
    *   **Where**: `/cascade/lifecycle/*.md`. Integrated with `/cascade/protocols/file_lifespans.md`.
    *   **Ref**: Documentation §2.5.6.

7.  **File Lifespan Policies**
    *   **What**: Declarative rules for when files should be reloaded, audited, merged, or deleted.
    *   **Why**: Manages file freshness, memory integrity, prevents token bloat.
    *   **Where**: `/cascade/protocols/file_lifespans.md`.
    *   **Ref**: Documentation §2.5.7.

8.  **Rolling Buffers**
    *   **What**: Files maintaining a fixed number of recent entries (e.g., `change_log/recent.md`).
    *   **Why**: Preserves short-term context efficiently.
    *   **Where**: Metadata `fileType: rolling`, `maxEntries`.
    *   **Ref**: Documentation §2.5.8.

9.  **Append-Only Logs**
    *   **What**: Historical files for events/changes in chronological order (e.g., `change_log/summary.md`).
    *   **Why**: Tamper-evident logs, reliable historical tracing.
    *   **Where**: Metadata `editPolicy: appendOnly`.
    *   **Ref**: Documentation §2.5.9.

10. **Temporary / One-Prompt Files**
    *   **What**: Volatile, single-use files (e.g., `job_logs/temp_job.md`).
    *   **Why**: Transient data, minimizing memory footprint.
    *   **Where**: Metadata `fileType: temporary`, `ttlCycles: 1`. Typically in `_taskbuffers/`.
    *   **Ref**: Documentation §2.5.10.

11. **Evictable Caches**
    *   **What**: Time-sensitive files for intermediate plans or temporary context (e.g., `load_plans/*.md`).
    *   **Why**: Manages token efficiency by offloading short-term reasoning.
    *   **Where**: Metadata `fileType: evictable`, `ttlCycles`.
    *   **Ref**: Documentation §2.5.11.

12. **Domain Routing**
    *   **What**: Metadata-driven scoping (`domain: client`) for files and actions.
    *   **Why**: Isolates context, prevents cross-domain contamination, improves token economy.
    *   **Where**: `system_manifest.md`, domain index files (`domains/*/index.md`), file metadata.
    *   **Ref**: Documentation §2.5.12.

13. **Protected Sections**
    *   **What**: Inline blocks (`<!-- PROTECTED --> ... <!-- END PROTECTED -->`) within editable files that are read-only.
    *   **Why**: Prevents drift in critical logic or assumptions.
    *   **Where**: Core control files like `loop_protocol.md`. Metadata `protected: true` at file level if entire file's sections are protected by this mechanism.
    *   **Ref**: Documentation §2.5.13.

14. **Write Gates**
    *   **What**: Declarative safeguards using glob patterns to control writable files/paths.
    *   **Why**: Protects architectural invariants, prevents rogue writes.
    *   **Where**: `/cascade/security/write_gates.md`.
    *   **Ref**: Documentation §2.5.14.

15. **Immutable Files & Hash Verification**
    *   **What**: Files that cannot be edited post-creation, tracked via cryptographic hashes.
    *   **Why**: Ensures stability of core declarations (doctrine, manifests).
    *   **Where**: Metadata `fileType: immutable`, `editPolicy: readonly`. Hashes in `/cascade/audit/integrity_snapshot.md`.
    *   **Ref**: Documentation §2.5.15.

16. **Integrity Snapshot**
    *   **What**: Canonical ledger of SHA-256 hashes for immutable/protected files.
    *   **Why**: Tamper-evidence seal, guarantees architectural trust.
    *   **Where**: `/cascade/audit/integrity_snapshot.md`.
    *   **Ref**: Documentation §2.5.16.

17. **Active Edit Lock**
    *   **What**: Volatile lockfile (`_locks/active_edit.lock`) signaling in-progress WRITE.
    *   **Why**: Prevents overlapping WRITE operations, ensures serialization.
    *   **Where**: `/cascade/_locks/active_edit.lock`.
    *   **Ref**: Documentation §2.5.17.

18. **Pre- & Post-Hash Checking**
    *   **What**: Dual-phase SHA-256 hash validation before and after WRITE for key files.
    *   **Why**: Detects corruption, unauthorized edits, ensures trustworthy state transitions.
    *   **Where**: Integrated into WRITE lifecycle for `immutable`/`protected` files, checked against `integrity_snapshot.md`.
    *   **Ref**: Documentation §2.5.18.

19. **Job Plans**
    *   **What**: Ephemeral planning artifacts (`job_logs/temp_job.md`) defining intended WRITE actions.
    *   **Why**: Traceability, intentionality, human/system confirmation for changes.
    *   **Where**: `/cascade/job_logs/temp_job.md`.
    *   **Ref**: Documentation §2.5.19.

20. **Write-Back Summary Confirmation**
    *   **What**: Post-WRITE verification where AI re-inspects written files against the job plan.
    *   **Why**: Guarantees WRITE operation succeeded exactly as intended.
    *   **Where**: Outcomes logged in `change_log/recent.md` and `audit/meta_audit.md`.
    *   **Ref**: Documentation §2.5.20.

21. **Summary Merging**
    *   **What**: System for condensing ephemeral files into durable summaries (e.g., `summary.md`).
    *   **Why**: Prevents token saturation, ensures long-term context continuity.
    *   **Where**: Controlled by metadata `mergeable`, `merge_target`, `merge_policy`.
    *   **Ref**: Documentation §2.5.21.

22. **Rolling Update Triggers**
    *   **What**: Lightweight mechanisms to update auxiliary logs/summaries post-WRITE without full replan.
    *   **Why**: Maintains freshness of recent context with minimal overhead.
    *   **Where**: Metadata `rollingUpdate`, `mergeTarget`. Affects files like `change_log/recent.md`.
    *   **Ref**: Documentation §2.5.22.

23. **Eviction Policy & Prune Plan**
    *   **What**: Rules and scripts defining how/when to delete/archive temporary or expired files.
    *   **Why**: Prevents performance degradation, memory bloat, stale context.
    *   **Where**: Master policy in `/cascade/audit/prune_plan.md`. Affects `_taskbuffers/`, `temp_notes/`, etc.
    *   **Ref**: Documentation §2.5.23.

24. **Token Budget Awareness**
    *   **What**: System tracking estimated token footprint of files/branches.
    *   **Why**: Prevents context overrun, enables smarter loading.
    *   **Where**: Tracked in `/cascade/audit/token_summary.md`.
    *   **Ref**: Documentation §2.5.24.

25. **Validator Pipeline**
    *   **What**: Utility (`validators/metadata_validator.ts`) for checking structural, metadata, and schema correctness.
    *   **Why**: Protects from malformed inputs, undefined behaviors.
    *   **Where**: `validators/metadata_validator.ts`. Errors to `meta_audit.md`.
    *   **Ref**: Documentation §2.5.25.

26. **Security Review & High-Risk Action Logging**
    *   **What**: Protocol governing and logging high-risk operations (schema rewrites, critical file mods).
    *   **Why**: Traceability and oversight for sensitive actions.
    *   **Where**: Policy in `security/security_review.md`. Logs in `audit/meta_audit.md`. Job plan flag `requiresReview: true`.
    *   **Ref**: Documentation §2.5.26.

27. **Drift Flag & Meta Audit**
    *   **What**: Mechanism for detecting and recording inconsistencies (`lifecycle/drift_flag.md`) and logging them (`audit/meta_audit.md`).
    *   **Why**: Maintains systemic trust, enables forensic debugging.
    *   **Where**: `/cascade/lifecycle/drift_flag.md`, `/cascade/audit/meta_audit.md`.
    *   **Ref**: Documentation §2.5.27.

28. **Hash Verification Workflow** (Subset of 15, 16, 18)
    *   **What**: 4-step process: Recalc hash → Compare to snapshot → If mismatch → Halt + Log + Flag.
    *   **Why**: Core to preventing architectural corruption.
    *   **Where**: `integrity_snapshot.md`, `immutable` files.
    *   **Ref**: Documentation §2.5.28.

29. **Schema & Snapshot Testing**
    *   **What**: Mechanism to capture structure, schema, metadata state at key milestones for regression testing and rollback.
    *   **Why**: Guards against structural drift in critical definitions.
    *   **Where**: Snapshots in `domains/schema/` or `audit/schema_snapshot.md`.
    *   **Ref**: Documentation §2.5.29.

30. **Extension Patterns (Counters, File Types)**
    *   **What**: Structured protocol for introducing new components (custom counters, file types).
    *   **Why**: Ensures extensibility while maintaining integrity.
    *   **Where**: Definitions in `system_manifest.md`, `metadata_schemas.md` (conceptual).
    *   **Ref**: Documentation §2.5.30.

31. **External Integrations & Hooks**
    *   **What**: Framework for interacting with external tools (CI/CD, ticketing).
    *   **Why**: Bridges cascade planning with real-world systems.
    *   **Where**: Logic in `external/` (conceptual). Metadata `external: true`, `externalHooks`.
    *   **Ref**: Documentation §2.5.31.

32. **Troubleshooting & Recovery Protocols**
    *   **What**: Defined procedures for handling system failures or inconsistencies.
    *   **Why**: Ensures system can be restored to a known good state.
    *   **Where**: `/cascade/protocols/recovery.md`.
    *   **Ref**: Documentation §2.5.32.

33. **Index Map (System + Domain Indexes)**
    *   **What**: Structured index files describing system layout and hierarchy.
    *   **Why**: Enables deterministic boot, accurate routing, memory-aware loading.
    *   **Where**: `/cascade/index.md` (global), `/cascade/domains/*/index.md` (domain-specific).
    *   **Ref**: Documentation §2.5.33.

34. **System Manifest (`system_manifest.md`)**
    *   **What**: Foundational, immutable declaration of system structure, doctrine, routing.
    *   **Why**: Anchor for cascade logic, ensures core invariants.
    *   **Where**: `/cascade/system_manifest.md`.
    *   **Ref**: Documentation §2.5.34.

35. **Loop Checkpoint (`loop_checkpoint.md`)**
    *   **What**: Sequential log recording successful completion of each full cascade loop.
    *   **Why**: Traceability, rollback orchestration, drift detection.
    *   **Where**: `/cascade/checkpoints/loop_checkpoint.md`.
    *   **Ref**: Documentation §2.5.35 (first one).

36. **Bootstrap Protocol (`00_BOOTSTRAP.md`)** (Note: Documentation has this as 2.5.35, but it's also 2.5.36 in a different numbering)
    *   **What**: Mandatory system entrypoint file defining foundational rules and boot preconditions.
    *   **Why**: Ensures sessions start from a clean, validated baseline.
    *   **Where**: `/cascade/00_BOOTSTRAP.md`.
    *   **Ref**: Documentation §1.4, §2.5.36 (or §2.5.35 last one), `/cascade/00_BOOTSTRAP.md`.

---
This index should be kept up-to-date as the ContextCascade system evolves.
It is based on "ContextCascade Developer & User Documentation v1.0".
""")

# /cascade/validators/ files
add_file_content("cascade/validators/metadata_validator.ts", """\
// validators/metadata_validator.ts
// -------------------------------------------------
// ContextCascade Metadata Validator
// -------------------------------------------------
// Responsibilities:
//   • Parse top-of-file `@meta` JSON blocks
//   • Verify required fields per fileType / subtype
//   • Enforce editPolicy + routeScope value constraints
//   • Provide a structured API for loop controller
//
// Usage (inside loop controller):
//   import { validateFile } from "./validators/metadata_validator";
//   const report = validateFile(filePath, rawContent);
//   if (!report.valid) throw new Error(report.message);
// -------------------------------------------------

import fs from "fs";

// -------------------- Types ----------------------

interface MetaBlock {
  fileType: string;
  purpose?: string;
  editPolicy: "appendOnly" | "appendOrReplace" | "incrementOnly" | "readonly" | "replaceOnly" | "overwrite"; // Added overwrite
  routeScope?: string;
  [key: string]: unknown;
}

interface ValidationReport {
  valid: boolean;
  message: string;
  warnings: string[];
  meta?: MetaBlock;
}

// -------------------- Constants ------------------

const REQUIRED_FIELDS = ["fileType", "editPolicy"] as const;
const ALLOWED_FILE_TYPES = new Set([
  "permanent",
  "immutable",
  "rolling",
  "append-only",
  "temporary",
  "counter",
  "evictable",
  "protected",
  "structural",
  "policy", // Added from file_lifespans.md
  "manifest", // Added from system_manifest.md
  "initialization", // Added from init_context.md
]);

const ALLOWED_EDIT_POLICIES = new Set([
  "appendOnly",
  "appendOrReplace",
  "incrementOnly",
  "readonly",
  "replaceOnly",
  "overwrite", // Added for files like temp_job.md
]);

// -------------------- Helper Functions -----------

function extractMeta(raw: string): { meta?: MetaBlock; remainder: string } {
  const match = raw.match(/<!--\s*@meta\s*({[\s\S]*?})\s*-->/m);
  if (!match) return { remainder: raw };
  try {
    // Attempt to strip // comments before parsing
    let jsonString = match[1];
    jsonString = jsonString.replace(/\/\/.*/g, '');
    const meta = JSON.parse(jsonString);
    return { meta, remainder: raw.replace(match[0], "") };
  } catch (e) {
    throw new Error("Invalid JSON in @meta block: " + e.message);
  }
}

function validateMeta(meta: MetaBlock, filePath: string): ValidationReport {
  const warnings: string[] = [];

  // Required fields
  for (const key of REQUIRED_FIELDS) {
    if (!(key in meta)) {
      return {
        valid: false,
        message: `Missing required field \"${key}\" in @meta for ${filePath}`,
        warnings,
      };
    }
  }

  // fileType check
  if (!ALLOWED_FILE_TYPES.has(meta.fileType)) {
    // Add a warning for now instead of failing validation for unknown file types
    // as the documentation mentions an extension mechanism.
    // A stricter validation could be re-enabled if needed.
    warnings.push(`Potentially invalid fileType \"${meta.fileType}\" in ${filePath}. It is not in the predefined set.`);
  }

  // editPolicy check
  if (!ALLOWED_EDIT_POLICIES.has(meta.editPolicy)) {
    return {
      valid: false,
      message: `Invalid editPolicy \"${meta.editPolicy}\" in ${filePath}`,
      warnings,
    };
  }

  // routeScope recommendation
  if (!meta.routeScope) {
    warnings.push(`routeScope missing in ${filePath} — recommend specifying domain or global.`);
  }

  return { valid: true, message: "OK", warnings, meta };
}

// -------------------- Public API -----------------

export function validateFile(filePath: string, raw?: string): ValidationReport {
  const content = raw ?? fs.readFileSync(filePath, "utf8");
  try {
    const { meta } = extractMeta(content);
    if (!meta) {
      return {
        valid: false,
        message: `No @meta block found in ${filePath}`,
        warnings: [],
      };
    }
    return validateMeta(meta, filePath);
  } catch (e: any) {
    return {
      valid: false,
      message: e.message,
      warnings: []
    };
  }
}

// CLI utility (optional)
if (require.main === module) {
  const target = process.argv[2];
  if (!target) {
    console.error("Usage: ts-node cascade/validators/metadata_validator.ts <filePath>");
    process.exit(1);
  }
  const report = validateFile(target);
  if (report.valid) {
    console.log("✔", target, "validated");
    if (report.warnings.length) console.warn("Warnings:", report.warnings.join("; "));
  } else {
    console.error("✖", target, report.message);
    if (report.warnings.length) console.warn("Warnings:", report.warnings.join("; "));
    process.exit(2);
  }
}
""")


def create_repo_structure(base_path="."):
    """
    Creates the repository directory structure and files.
    """
    print(f"Creating repository structure under: {os.path.abspath(base_path)}")

    for file_path, content in REPO_FILES.items():
        # Ensure the path is relative to the base_path
        # and uses correct OS separators
        full_path = pathlib.Path(base_path) / pathlib.Path(file_path)

        # Create parent directories if they don't exist
        parent_dir = full_path.parent
        if not parent_dir.exists():
            print(f"Creating directory: {parent_dir}")
            parent_dir.mkdir(parents=True, exist_ok=True)

        # Create the file with its content
        print(f"Creating file: {full_path}")
        try:
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)
        except IOError as e:
            print(f"Error writing file {full_path}: {e}")
            # Optionally, decide if you want to stop or continue
            # For now, we'll print the error and continue

    # Create empty directories explicitly if they are not implicitly created by files
    # The ls() output shows directories with a trailing slash.
    # We need to ensure these are created if they don't contain files.

    # Define all directories that must exist based on Repo_Documentation_v1.md Section 3.1
    # This list should be comprehensive.
    # Directories are created if they don't exist.
    # Parent directories are created automatically by Path.mkdir(parents=True).
    # Sorting ensures parent directories are conceptually processed first, though mkdir handles it.
    required_dirs = sorted([
        "cascade",
        "cascade/_locks",
        "cascade/_meta",
        "cascade/protocols",
        "cascade/lifecycle",
        "cascade/change_log",
        "cascade/job_logs",
        "cascade/load_plans",
        "cascade/_taskbuffers",
        "cascade/temp_notes",
        "cascade/security",
        "cascade/audit",
        "cascade/checkpoints",
        "cascade/domains",
        "cascade/domains/client",
        "cascade/domains/server",
        "cascade/domains/schema",
        "cascade/validators"
        # Note: cascade/external and cascade/_archive are not in the initial list from docs
        # but could be added if they are standard empty dirs to create.
        # For now, sticking to Doc 3.1.
    ])

    for dir_path_str in required_dirs:
        dir_path = pathlib.Path(base_path) / pathlib.Path(dir_path_str)
        if not dir_path.exists():
            print(f"Creating directory: {dir_path}")
            dir_path.mkdir(parents=True, exist_ok=True)
        elif not dir_path.is_dir():
            print(f"Error: Expected directory but found file: {dir_path}")
            # Optionally, raise an error or handle as needed

    print("Repository structure creation complete.")

if __name__ == "__main__":
    # REPO_FILES is populated at the top of the script now.
    create_repo_structure()
# REPO_FILES["README.md"] = """<!-- @meta {
#   "fileType": "permanent",
#   "purpose": "High-level overview and quickstart reference for the ContextCascade repository.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
# Context Cascade

## 🚀 Overview

**Context Cascade** is a robust, modular, file-based memory and protocol system designed to augment persistent context management for AI coding assistants. Its primary aim is addressing memory limitations common in environments like Replit by externalizing architectural, behavioral, and decision-making context into clearly structured markdown files.

This structured external memory system enforces consistency, traceability, and durability of context across prompts, effectively bridging the gap between short-term ephemeral AI memory and long-term project coherence.

---

## 🎯 Key Problems Solved

Traditional AI coding assistants often encounter critical issues, including:

- Loss of architectural coherence across prompts
- Redundant component regeneration
- Architectural drift and inconsistencies
- Misaligned assumptions causing bugs
- Token budget constraints leading to memory management issues

Context Cascade systematically addresses these issues through an external memory approach that captures and maintains critical context externally.

---

## 📂 Directory Structure

```plaintext
/cascade/
├── 00_BOOTSTRAP.md                  # Entry-point enforcing protocol startup (immutable)
├── index.md                         # Master file map (structural)
├── system_manifest.md               # Immutable system doctrine (immutable)
├── protocols/
│   ├── loop_protocol.md             # READ → ACT → WRITE loop rules
│   └── file_lifespans.md            # Lifecycle refresh policies
├── lifecycle/                       # Domain counters and drift flags
├── change_log/                      # Rolling and historical logs
├── job_logs/                        # Ephemeral job planning logs
├── load_plans/                      # Scoped context-loading blueprints
├── audit/                           # Integrity, consistency, and security audits
├── domains/                         # Domain-specific guidance and routing
├── security/                        # Access control and write protection
├── checkpoints/                     # Loop execution checkpoints
└── validators/                      # Metadata and schema validation
```

---

## ⚙️ Core Principles

### 🔄 Read → Act → Write Loop

The disciplined three-phase operational cycle:

- **READ**: Load contextual files and validate metadata.
- **ACT**: Logical reasoning and preparation of intended changes.
- **WRITE**: Apply changes securely, with comprehensive validation.

### 📚 Metadata Enforcement

Structured JSON metadata headers define file behavior, lifecycle rules, and validation requirements, ensuring consistent treatment and system integrity.

### 🚦 Lifecycle Management

Automated lifecycle counters and policies manage context freshness, prune expired data, and maintain memory efficiency.

### 🔐 Security and Integrity

SHA-256 hashing, immutable files, protected sections, and rigorous validation prevent unauthorized modifications and detect unintended changes.

### 🌐 Domain Routing

Files and actions are scoped by logical domains (e.g., client, server, schema) to optimize token budget use and maintain clear boundaries.

---

## 🚧 Getting Started

1. **Bootstrap Initialization**

   - Every session begins by reading `00_BOOTSTRAP.md`.

2. **Core Files**

   - Explore the system’s structure via `/cascade/index.md`.
   - Review system rules in `/cascade/system_manifest.md`.

3. **Loop Protocol**

   - Study `/protocols/loop_protocol.md` to fully understand the operation cycle.

---

## 🛠 Placeholder Use Cases

### ✅ Bootstrap Example

A new Replit session initializes by first reading `00_BOOTSTRAP.md`, validating file hashes, and establishing baseline integrity before proceeding to user prompts.

### ✅ Lean-mode Query Example

AI reads only minimal necessary context from `index.md` to handle a lightweight query, optimizing token efficiency.

### ✅ Domain Extension Example

Developers introduce new domains through secure processes involving job plans, validator approvals, and updates to `system_manifest.md`.

---

## 🧩 Canonical File Types

- `permanent`
- `immutable`
- `rolling`
- `append-only`
- `temporary`
- `counter`
- `evictable`
- `protected`
- `structural`

These types govern lifecycle behaviors, memory management, and operational rules.

---

## 🔗 Contributions and Extensions

- New file types, domains, or lifecycle counters follow a strict extension pattern workflow, involving validation, approval, and secure implementation.
- Contributions must pass rigorous metadata validation (`validators/metadata_validator.md`).

### 🧪 Validator Setup

The metadata validator requires Node.js and `npm`.

1. Run `npm install` from the repository root to install `ts-node` and TypeScript.
2. Execute `npm run validate -- <path/to/file>` to check a file's metadata block.

---

## 📖 Documentation

Comprehensive documentation is available throughout the `/cascade/` directory, particularly in the `protocols/` and `audit/` subdirectories.

---

## 📮 Contact

For further details or collaboration, reach out to the maintainer at:

- **Email**: [chrisbannan93@gmail.com](mailto:chrisbannan93@gmail.com)

---

## 📌 License

Refer to the repository's `LICENSE` file for licensing details.

---
"""

    REPO_FILES["Repo_Documentation_v1.md"] = """<!-- @meta {
  "fileType": "permanent",
  "purpose": "Comprehensive developer and user guide for operating the ContextCascade system.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
# ContextCascade Developer & User Documentation
*A comprehensive guide for developers and AI assistants to correctly load, use, update, and maintain a ContextCascade system.*

---
## 0. Front Matter
- **Document Title:** ContextCascade Developer & User Documentation
- **Version:** 1.0
- **Maintainer:** Chris Bannan
- **Last Updated:** 25/06/2025
- **Contact:** [chris.bannan@vocus.com.au](mailto:chris.bannan@vocus.com.au)

## 1. Quick-Start Guide

### 1.1 Prerequisites
To begin using the ContextCascade system, ensure the following are met:

- You are working within a Replit project or a system that allows access to a local `/cascade/` directory structure.
- The AI assistant has the ability to read and write Markdown (`.md`) files.
- Token budget awareness is supported, ideally with rough estimates of context window usage.
- Developer or user has access to lifecycle management logic or triggering mechanism (e.g., global counter increment).
- The developer understands Markdown front-matter or comment-based metadata conventions.
- Recommended: Familiarity with loop-safe prompting and separation of read/act/write phases.
- Recommended: Developer is able to provide the AI with consistent session-initiation prompts that include file path references.

### 1.2 Bootstrap Script or Manual Setup
-MUST ADD A ZIP FILE ATTACHMENT OF THE STARTER FOLDER

### 1.3 Session Initiation Prompt Example
Use the following prompt to initialize a Replit AI session using the ContextCascade system:
```
Begin by reading /cascade/00_BOOTSTRAP.md. It contains your mandatory operating instructions.
Then proceed to /cascade/index.md to load the file map, followed by the loop protocol in /cascade/protocols/loop_protocol.md.
Respect file lifespans and read priorities as defined in /cascade/protocols/file_lifespans.md.
You must complete a full READ phase before taking any ACT or WRITE actions.
```
This can still be shortened with aliases or injected into Replit’s AI memory, but must always begin with /cascade/00_BOOTSTRAP.md and include path anchors to core protocol files.

### 1.4 Session Bootstrap Behavior (Triggered by 00_BOOTSTRAP.md)
The session initiation Prompt example will initiate a prompt within the 00_BOOTSTRAP.md file that should read something like this:
<!-- @meta {
  "fileType": "immutable",
  "purpose": "Bootstrap file enforcing protocol startup, scope discipline, and memory system entry constraints.",
  "editPolicy": "readonly"
} -->
# ContextCascade Bootstrap Guide
Welcome. This file is the required entrypoint for using the ContextCascade memory system. Before any task, you must:
## Mandatory Protocol (Follow Exactly)
- Read `/cascade/index.md` (map)
- Read `/cascade/protocols/loop_protocol.md` (loop rules)
- Respect all `@meta` blocks
- Check `/protocols/file_lifespans.md` and any `/lifecycle/*.md` counters
- Do not ACT or WRITE until READ phase is fully complete
- Never edit `<!-- PROTECTED -->` sections
- If any `immutable` file fails hash check → halt, log to `/audit/meta_audit.md`, skip WRITE
---
## Scope Rules (Memory vs. App)
- ContextCascade only stores memory, plans, counters, protocols, and logs
- Do not write `.md` files in Cascade that describe or duplicate app logic
- All application code or assets belong in the app repo, outside `/cascade/`
- Only create `.md` files here if storing durable reasoning or system governance
---
## Summary
If it’s not memory, constraint, protocol, or trace —
→ it doesn’t belong in Cascade.
Proceed to `/cascade/index.md`.


### 1.5 Validation Checklist
Before first use or AI engagement:

-

*Optional:* Attach and offer a ZIP archive of a starter scaffold with empty files for all required paths. Consider bundling `00_BOOTSTRAP.md`,`index.md`, `loop_protocol.md`, and `file_lifespans.md` with default safe values.

## 2. Conceptual Overview

### 2.1 What is ContextCascade?
ContextCascade is a modular, file-based memory and protocol system designed to simulate persistent context for AI coding assistants — especially those operating in environments like Replit where native memory is limited. It works by externalizing architectural, behavioral, and decision-making context into a standardized directory of markdown files, each with a defined purpose, metadata annotations, and lifecycle controls.
ContextCascade is not a code framework — it is a guidance and memory augmentation protocol. It defines how the AI should reason, read, act, write, and recontextualize its behavior before and after each code-related action. It ensures that memory is durable across prompts, safeguards are embedded, files are updated appropriately, and long-term architectural consistency is maintained, even across fragmented Replit AI sessions. This system leverages a cascade pattern — often read top-down — where files like `00_BOOTSTRAP.md`, `index.md`, `loop_protocol.md`, `file_lifespans.md`, and rolling logs form a multi-phase loop with embedded counters and condition-based execution logic.

### 2.2 Design Principles
The ContextCascade system is founded on the following core design principles:

1. **Modular Memory Externalization**: Key design decisions, assumptions, constraints, and goals are written into `.md` files instead of relying on ephemeral prompt memory.
2. **Read-Act-Write Discipline**: AI must follow a structured three-phase loop before making changes: first loading relevant context (READ), then applying logic (ACT), and finally writing updates with summaries (WRITE).
3. **Lifecycle-Aware Refreshing**: Context should not be fully reloaded every time. Lifecycle counters define when each file or domain should be re-read based on thresholds or scope-specific actions.
4. **Lean Rolling Buffers**: Temporary files such as `recent.md` or `_temp/` act as rolling snapshots of recent changes or notes, capped at a fixed number of entries.
5. **Safeguards Against Drift**: Hash comparisons, protected file sections, and audit protocols reduce unintended overwrites or architectural drift.
6. **Composable and Extendable**: The system is designed to support plugins, domain expansions, external tool integrations, and sub-cascade routing.
7. **Contextual Compression**: Not all files need to be read every time. Prioritization and smart load plans optimize for limited token windows.
8. **Explicit File Classification**: Files are categorized by lifespan and usage type (e.g. persistent, rolling, ephemeral) to control reading/updating behavior.
9. **Prompt Clarity**: Each file includes metadata headers to explain its type, purpose, and edit strategy. Prompts must explicitly refer to files and their expected handling.

### 2.3 Why It Exists (Key Problems Solved)
Traditional AI assistants, especially in tools like Replit, suffer from severe short-term memory loss across prompts. Once a session ends or even after several actions, the assistant often forgets architectural choices, key assumptions, previously created files, naming conventions, and critical boundaries. This leads to:

- Rebuilding components that already exist
- Breaking architectural rules unknowingly
- Losing sight of project goals and constraints
- Causing file bloat and duplication from forgetful behavior
- Introducing bugs from misaligned assumptions
- Accumulating technical debt from inconsistent design memory

ContextCascade solves this by introducing an external memory system that:

- Stores architectural reasoning, component purpose, and constraints in structured, readable `.md` files
- Enforces read-act-write phases that slow down reflexive, careless actions
- Keeps a log of job plans, summaries, and change traces to maintain historical awareness
- Uses lifecycle counters to strategically refresh context based on thresholds and behavior
- Introduces temp files and rolling buffers to reduce context size while preserving recent decisions
- Maintains a consistent loop protocol that prompts the AI to recontextualize before acting

It is a first step toward bridging the gap between stateless prompt-response systems and a long-term, guided AI development partner.

### 2.4 High-Level System Diagram
The following conceptual diagram outlines the major components and interaction flow within the ContextCascade system:

```plaintext
User Prompt ──► Replit AI ──► /cascade/00_BOOTSTRAP.md (entrypoint orientation)
                                │
                                ├─► /cascade/index.md (master file map)
                                │
                                ├─► /cascade/protocols/loop_protocol.md (defines READ → ACT → WRITE)
                                │
                                ├─► /cascade/protocols/file_lifespans.md (thresholds for lifecycle refresh)
                                │
                                ├─► /cascade/change_log/recent.md (rolling update buffer)
                                │
                                ├─► /cascade/change_log/summary.md (historical full log)
                                │
                                ├─► /cascade/lifecycle/*.md (counters: global, client, server, etc.)
                                │
                                ├─► /cascade/load_plans/*.md (AI-generated read plans)
                                │
                                └─► /cascade/job_logs/temp_job.md (temporary action plan + hash validation)

                          ▲
                          │
               ContextCascade Loop (READ → ACT → WRITE)
                          │
             Token Budget Awareness, Refresh Policy, Change Logs
```

This diagram illustrates the AI's movement through context files in a structured loop. Load plans and lifecycle counters dynamically inform which files must be read on each pass. Temporary buffers like `temp_job.md` and rolling logs such as `recent.md` support memory efficiency and change traceability.

### 2.5 Core Feature Index
The list below enumerates **every first‑class feature** in ContextCascade. Subsequent sections will break down each in depth.

1. **Metadata Blocks**
2. **Canonical FileType Registry**
3. **Read → ACT → WRITE Loop Protocol**
4. **Load Modes** (Lean, Domain, Full)
5. **Load Plans**
6. **Lifecycle Counters**
7. **File Lifespan Policies**
8. **Rolling Buffers**
9.  **Append‑Only Logs**
10. **Temporary / One‑Prompt Files**
11. **Evictable Caches**
12. **Domain Routing**
13. **Protected Sections**
14. **Write Gates**
15. **Immutable Files & Hash Verification**
16. **Integrity Snapshot**
17. **Active Edit Lock**
18. **Pre‑ & Post‑Hash Checking**
19. **Job Plans**
20. **Write‑Back Summary Confirmation**
21. **Summary Merging**
22. **Rolling Update Triggers**
23. **Eviction Policy & Prune Plan**
24. **Token Budget Awareness**
25. **Validator Pipeline**
26. **Security Review & High‑Risk Action Logging**
27. **Drift Flag & Meta Audit**
28. **Hash Verification Workflow**
29. **Schema & Snapshot Testing**
30. **Extension Patterns** (new counters, file classes)
31. **External Integrations & Hooks**
32. **Troubleshooting & Recovery Protocols**
33. **Index Map - system + domain indexes**
34. **System Manifest (`system_manifest.md`)**
35. **Loop Checkpoint (`loop_checkpoint.md`)**
36. **Bootstrap Protocol (`00_BOOTSTRAP.md`)**

#### 2.5.1 **Metadata Blocks**
**What**: Structured JSON-in-comment headers located at the very top of each file. These blocks define operational context for how the system should treat each file.
**Why**: They encode critical attributes such as file behavior (`fileType`), editing permissions (`editPolicy`), expiration (`ttlCycles`), routing scope (`routeScope`), and merge strategies. These enable the cascade to interpret, enforce, and automate behavior during each READ → ACT → WRITE cycle.
**Where**: Present in all `.md` files in the cascade structure. Parsing and validation are handled by `validators/metadata_validator.md` and invoked at the start of every READ phase.
**How**: The metadata block is parsed before any content reasoning begins. Fields like `fileType`, `editPolicy`, `ttlCycles`, and `routeScope` inform downstream logic including whether the file is writable, when it should be pruned, if it needs to be re-read, or which load plan it belongs to.
**Example Use Case**: A file `load_plans/auto_plan_client.md` might declare:
<!-- @meta
{
  "fileType": "evictable",
  "ttlCycles": 3,
  "routeScope": "client",
  "editPolicy": "appendOnly"
}
-->
This tells the system it’s a short-lived plan that will expire in 3 cycles, belongs to the `client` route domain, and should only be appended to, not overwritten.

#### 2.5.2 **Canonical FileType Registry**
**What**: A formally defined registry containing nine allowed file types and their permissible aliases. These types include `permanent`, `immutable`, `rolling`, `append-only`, `temporary`, `counter`, `evictable`, `protected`, and `structural`.
**Why**: Guarantees consistent interpretation of file semantics across all cascade operations. Each `fileType` carries rules around edit behavior, lifecycle duration, eviction policy, and participation in routing or merges.
**Where**: Defined in §3.2.1 of the documentation and enforced by `validators/metadata_validator.md`. The validator halts execution if unregistered or malformed types are encountered.
**How**: Every file's metadata must declare a valid `fileType`. If applicable, a matching `subtype` may be used to refine behavior (e.g., `domain_spec`, `index`, or `buffer`). These fields drive enforcement in lifecycle counters, write audits, and load plan resolution.
**Example Use Case**: A structural mapping file might include:
<!-- @meta
{
  "fileType": "structural",
  "subtype": "index",
  "editPolicy": "appendOnly"
}
-->
This configuration signals that the file is a live index (`cascade/index.md`), editable, and critical to domain boot routing. Validators will use this classification to enforce index completeness and reject invalid merges.

---
#### 2.5.3 **Loop Protocol (READ → ACT → WRITE)**
**What**: A disciplined three-phase protocol governing every execution cycle in the ContextCascade system. The loop divides operations into Read, Act, and Write segments.
**Why**: Ensures clarity, auditability, and safety in system operations. By explicitly separating context loading (READ), decision-making (ACT), and output mutation (WRITE), it avoids reflexive edits, reinforces traceability, and allows for targeted rollback or analysis.
**Where**: Enforced at startup via `index.md`, and fully documented in `protocols/loop_protocol.md`. Used implicitly every cycle across all cascade contexts.
**How**:
- **READ**: Loads specified files into context per active load_plan, validated metadata, and mode (Lean/Domain/Full). Only allowed after a valid bootstrap step via 00_BOOTSTRAP.md.
- **ACT**: Applies logic or reasoning to the loaded data—may result in draft file changes, job plan generation, counter updates.
- **WRITE**: Applies edits, enforces editPolicy, performs hash validations, and updates logs like `loop_checkpoint.md`, `meta_audit.md`.
**Example Use Case**: Use Case: A prompt requests system audit cleanup. During READ, it loads prune_plan.md, recent change logs, and lifecycle counters. In ACT, it detects threshold crossings and compiles a cleanup intent file (`job_logs/temp_job.md`). In WRITE, it removes expired buffers, appends to the summary log, and updates counters while verifying protected blocks remain untouched.
---

### 2.5.4 **Load Modes**
**What**: ContextCascade defines three hierarchical strategies for reading contextual files during the READ phase: `Lean`, `Domain`, and `Full`.
**Why**: These strategies help balance the trade-off between token budget and contextual completeness. This enables the system to scale across small, narrow queries and large architectural updates.
**Where**: Defined across `load_plans/`, `protocols/load_mode_logic.md`, and referenced in lifecycle counters and prompt-routing triggers.
**How**:
- **Lean Mode**: Only core index files, counters, and top-level manifest are loaded. Used in quick diagnostics or system state queries.
- **Domain Mode**: Loads files relevant to a specific domain (e.g., `client`, `server`) as routed via `routeScope`. Ideal for targeted updates or audits.
- **Full Mode**: Ingests every file marked as readable, including all logs, planning files, domain specs. Used when merging, refactoring, or auditing across the entire cascade.
The mode is chosen based on prompt origin, counters, file flags, or explicit plan metadata.
**Example Use Case**: When a prompt requests "Summarize recent changes for the client domain," the system triggers **Domain Mode**, loading all `client`-scoped files (like `client_tick.md`, `domain_spec/client.md`, and `change_log/recent.md`) while skipping unrelated files like `server_config.md` or `schema_snapshot.md`.

### 2.5.5 **Load Plans**
**What**: Load Plans are ephemeral markdown files that define the specific set of files to be read in the following prompt cycle. They act as scoped loading blueprints tailored to the context needs of upcoming reasoning.
**Why**: By explicitly listing files needed for the next READ, Load Plans avoid token overuse, ensure only relevant context is ingested, and allow for faster loop cycles. They enable precision loading aligned with domain needs or prompt origin.
**Where**: Located under `load_plans/` and typically named `auto_plan_<scope>.md` (e.g., `auto_plan_client.md`). These are generated by the AI during the ACT phase and consumed immediately at the start of the next READ phase.
**How**: Load Plans are generated based on:
- `routeScope` (e.g., `client`, `schema`, `server`)
- Priority files based on metadata, fileType, or drift flags
- Token constraints (evaluated against `token_summary.md`)
- Dynamic triggers like lifecycle thresholds, audit flags, or summary merges
**Example Use Case**: After completing a WRITE that affected `client_tick.md` and `job_logs/temp_job.md`, the AI generates a new Load Plan:
<!-- @meta
{
  "fileType": "evictable",
  "ttlCycles": 2,
  "routeScope": "client"
}
-->
- lifecycle/client_tick.md
- job_logs/temp_job.md
- domain_spec/client.md
In the next loop, this Load Plan ensures only these scoped files are loaded, preserving token space and execution speed.


### 2.5.6 **Lifecycle Counters**
**What**: Structured `.md` files that track cumulative update activity across specific domains or contexts (e.g., client, server, schema).
**Why**: Counters are essential for triggering threshold-based logic including context reloads, pruning, job plan refreshes, and drift detection. They allow the system to monitor when a file or domain becomes stale or overactive.
**Where**: Located in `lifecycle/` directory, typically named by domain (e.g., `client_tick.md`, `schema_tick.md`). Integrated with `file_lifespans.md` policy rules.
**How**: During each WRITE phase, the system increments the appropriate counter file if any file within that routeScope was modified. The counter value is then compared against rules defined in `file_lifespans.md`, which may trigger:
- Reread of key files
- Merging of ephemeral logs into summaries
- Automatic generation of prune or audit jobs
**Example Use Case**: After three successive edits to `client/`, the system increments `client_tick.md` to `3`. On the fourth cycle, `file_lifespans.md` rules detect this threshold, triggering a forced reread of `domain_spec/client.md` and a pruning job targeting expired buffers in `temp_notes/`.

### 2.5.7 **File Lifespan Policies**
**What**: Declarative threshold rules that determine when files should be reloaded, audited, merged, or deleted. These policies govern file freshness and memory integrity throughout the cascade lifecycle.
**Why**: Prevents token bloat, stale reads, and excessive rereads by scheduling context refreshes based on domain activity. Enables predictable pruning and summary merging behavior to maintain hygiene and responsiveness.
**Where**: Centralized in `protocols/file_lifespans.md`. Enforced during ACT phase based on counter values and referenced by cleanup tools like `prune_plan.md` and job planners.
**How**: The policy file maps lifecycle counter values (e.g., from `client_tick.md`) to specific actions. Common thresholds include:
- `reread_threshold`: forcibly reload context after N writes
- `prune_threshold`: triggers removal of expired buffers or plans
- `merge_threshold`: prompts consolidation of rolling or ephemeral files
**Example Use Case**: If `schema_tick.md` exceeds 10, the file lifespan policy might trigger a `reread` of `domain_spec/schema.md`, a `prune` of unused `temp_notes/`, and a `merge` of any append-only logs tied to schema changes. This keeps the schema branch concise and performant without full reloads each cycle.

### 2.5.8 **Rolling Buffers**
**What**: A class of files that maintain a fixed number of recent entries, providing a sliding-window view of recent activity or thought processes.
**Why**: Ensures continuity of short-term context without overwhelming token limits. These buffers preserve the most relevant interactions while evicting older data automatically, optimizing for recall and cost.
**Where**: Common examples include `change_log/recent.md`, `_taskbuffers/tmp_note.md`, and `temp_notes/…`. These files typically appear under logs or ephemeral notes directories.
**How**: Controlled via metadata fields such as:
- `fileType: rolling`
- `maxEntries: N`
- `editPolicy: appendOnly` The system enforces FIFO (First-In-First-Out) eviction after each WRITE phase. When the number of entries exceeds `maxEntries`, the oldest lines or sections are removed to maintain size.
**Example Use Case**: During a weeklong dev sprint, the AI writes daily notes to `temp_notes/dev_checkins.md`. It’s marked with:
<!-- @meta
{
  "fileType": "rolling",
  "maxEntries": 5,
  "editPolicy": "appendOnly"
}
-->
On day 6, the oldest entry is evicted automatically. The file always contains the last five entries, keeping the check-in thread fresh and within budget.

### 2.5.9 **Append-Only Logs**
**What**: Append-only logs are historical files that record events, changes, or audits in strictly chronological order. They may not be rewritten or back-edited, only appended to.
**Why**: This design enables tamper-evident logs and reliable historical tracing of system changes, decisions, or incidents. It provides an immutable audit trail that aligns with governance and debugging needs.
**Where**: Found in key locations such as `change_log/summary.md`, `meta_audit.md`, and occasionally in domain-specific audit files. They appear wherever write history needs to be permanent and traceable.
**How**: Enforced by setting `editPolicy: appendOnly` in the metadata block. The validator enforces this by rejecting any write operation that deletes or modifies previous content.
**Example Use Case**: After each successful WRITE cycle, the system appends an entry to `change_log/summary.md`:
```markdown
## Cycle 58 – 2025-06-25
- Edited: domain_spec/client.md
- Pruned: temp_notes/checkins.md
- Job: prune_plan.md executed
This entry is added to the end of the file. Previous entries are never modified. This allows future audits to reconstruct past system decisions or detect malicious interference.

### 2.5.10 **Temporary / One-Prompt Files**
**What**: Volatile, single-use files designed to exist for only one loop cycle—created during one ACT phase and deleted immediately after the next WRITE completes.
**Why**: Useful for transient intent logs, draft buffers, ephemeral routing decisions, or scratchpad notes that have no long-term value. They minimize system memory footprint and prevent pollution of permanent context.
**Where**: Typically found in `_taskbuffers/`, `job_logs/temp_job.md`, or `temp_notes/`. Used heavily in job planning, fast summaries, or burst buffer evaluations.
**How**: Declared with metadata:
- `fileType: temporary`
- `ttlCycles: 1` These are automatically pruned after each WRITE phase unless promoted or moved. Lifecycle and validator tools monitor these locations and remove expired files during ACT or prune cycles.
**Example Use Case**: During a complex planning task, the AI writes a file `job_logs/temp_job.md` that outlines a speculative cleanup of expired rolling buffers. Metadata marks it as:
<!-- @meta
{
  "fileType": "temporary",
  "ttlCycles": 1,
  "editPolicy": "appendOnly"
}
-->
If not referenced again, this file is removed after the next WRITE. This avoids cluttering the system with stale intermediate decisions.

### 2.5.11 **Evictable Caches**
**What**: Evictable caches are time-sensitive files that store intermediate plans, speculative logic, or temporary context which do not require long-term persistence.
**Why**: These files help manage token efficiency and system cleanliness by offloading short-term reasoning that should expire naturally without impacting the core architecture or long-term audit trails.
**Where**: Most commonly used in `load_plans/*.md`, `prune_plan.md`, and short-term strategy documents. They also appear in speculative routing or sandbox planning domains.
**How**:
- Marked with `fileType: evictable`
- Assigned a `ttlCycles` value (e.g., 2-5 loop cycles)
- Automatically pruned once the lifecycle threshold is reached or during a triggered cleanup event
- May also include fields like `expirationPolicy` to fine-tune retention
**Example Use Case**: The AI generates `load_plans/auto_plan_schema.md` during an audit burst. It declares:
<!-- @meta
{
  "fileType": "evictable",
  "ttlCycles": 4,
  "routeScope": "schema"
}
-->
```
This signals that the plan is valid for four execution loops. After that, it is auto-pruned unless explicitly referenced or promoted. This ensures ephemeral plans are used efficiently and removed before they become stale.

### 2.5.12 **Domain Routing**
**What**: Metadata-driven scoping system that assigns each file, plan, or loop action to a specific logical domain such as `client`, `server`, `infra`, `meta`, etc. Domains help isolate and target context usage during READ, ACT, and WRITE phases.\
**Why**: Supports selective cascade behavior—by tagging files and routes with `domain`, the system can increment counters, load plans, or execute logic only within relevant scopes. This prevents cross-domain contamination and improves token economy.\
**Where**:
- Defined explicitly in the frontmatter of `domains/*/index.md` files.
- Also present in `system_manifest.md` to declare and structure valid domains.
- Domain metadata can appear in any file to declare its affiliation.\
  **How**:
- Metadata tag used:
`domain: server`
- During a READ phase, only files matching the current route’s domain are considered active context unless declared `domain: global`.
- The ACT planner uses domain tags to restrict what logic is invoked or what plans are evaluated.
- Counters (like `loopCount`, `writeCount`) are tracked per domain, allowing parallel, domain-specific progress tracking.
- Domains also allow differential pruning, checkpointing, and token budgeting per branch.
**Example Use Case**:\
A developer adds a new domain file `domains/api/index.md` with metadata:
`fileType: domainIndex domain: api`
This automatically triggers a new scoped cascade branch during boot. When running a job inside the `api` domain, only files tagged with `domain: api` or `domain: global` are loaded for context. This allows the system to isolate changes to the API layer without pulling in unrelated logic from the `client` or `infra` domains.

### 2.5.13 **Protected Sections**
**What**: Inline blocks within editable files that are marked as read-only and protected from accidental or unauthorized changes. These sections are often used to encode protocol-critical logic or hard-coded system assumptions that must remain stable across updates.\
**Why**: Prevents drift in critical logic, such as lifecycle protocols, validator behavior, or system boundaries. Protecting these regions ensures that AI-generated edits don't unintentionally violate architectural contracts or introduce inconsistencies.\
**Where**:
- Found in core control files like `loop_protocol.md`, `write_gates.md`, and `index.md`.
- Also appears in domain-specific configurations where a subsection of logic is static by design.\
  **How**:
- Marked using metadata blocks that include:
`<!-- @meta { "protected": true } -->`
- During the ACT phase, the AI parser identifies protected regions and marks their byte spans as immutable.
- Any READ or WRITE attempt that intersects with these byte ranges triggers an abort, and the system logs a `writeViolation`.
- These overlaps are detected via diff-checks during pre-write validation.
**Example Use Case**:\
A section of `loop_protocol.md` defines the core READ → ACT → WRITE loop behavior. It is marked as protected:
`<!-- @meta { "protected": true } --> ### Loop Contract: 1. READ all domain-relevant inputs 2. ACT based on planning directives 3. WRITE only allowed files under current scope`
If a subsequent ACT cycle tries to modify this section (e.g., inserting a new step or editing the header), the system detects overlap with a protected range and halts the WRITE phase, prompting a warning and suggesting escalation via job planning instead.

### 2.5.14 **Write Gates**
**What**: A declarative safeguard system using glob patterns and path constraints to control which files can be written to during a cascade loop. These gates enforce strict write boundaries, blocking unintended or unauthorized modifications to critical files or directories.\
**Why**: Protects architectural invariants by preventing rogue writes, corruption of immutable domains, or accidental modification of meta or protocol files. This layer acts as a write-time firewall that enforces file safety at the edge of the ACT → WRITE transition.\
**Where**:
- Primary configuration located in `security/write_gates.md`.
- Gates are evaluated globally but can be domain-specific if declared within a scoped path.
- Also referenced during lifecycle checks and metadata validations.\
  **How**:
- Declared as YAML lists inside `write_gates.md`, typically structured as:
`writeGates: - allow: "jobs/**" - deny: "loop_protocol.md" - allow: "domains/*/index.md" - deny: "audit/**"`
- During the ACT phase, any generated WRITE plan is pre-validated against these patterns.
- The validator pipeline parses the full WRITE intent and compares each path against the allowed gates.
- If any write operation targets a disallowed path, the job is aborted before changes are applied.
- Some gates are `appendOnly`, meaning existing content cannot be overwritten—only extended.
- Gates can be dynamically toggled during meta-jobs or with escalated privileges in emergency patches.

**Example Use Case**:\
A developer working inside the `client` domain attempts to WRITE to `system_manifest.md` without a proper job plan. The current `write_gates.md` includes:
`- deny: "system_manifest.md"`
When the ACT phase tries to enqueue that file for writing, the system aborts the WRITE with a gated write violation and logs the event. The AI explains the denial and suggests the user initiate a `security_review` job or escalate via `meta_audit.md`.

### 2.5.15 **Immutable Files & Hash Verification**
**What**: Special class of files that are declared immutable—once written, they can never be edited or overwritten. These files are sealed against change and tracked via cryptographic hashes to guarantee their integrity over time.\
**Why**: Ensures architectural stability and enforces the sanctity of core declarations like system doctrine, manifest structure, or foundational initialization context. By locking these files, the system protects against regressions, unintentional protocol drift, or tampering.\
**Where**:
- Common examples include `init_context.md`, `system_manifest.md`, and files inside `/immutable/` directories.
- Immutable files are referenced in `integrity_snapshot.md` for ongoing hash monitoring.\
  **How**:
- Declared with metadata:
`fileType: immutable editPolicy: readonly`
- Upon initial WRITE, the file is hashed using SHA-256 and added to `audit/integrity_snapshot.md`.
- Every subsequent loop involving hash checks will re-read the file, re-calculate its hash, and compare it to the stored value.
- Any mismatch triggers an emergency halt of the loop, logs a `hashMismatch`, and raises a `driftFlag`.
- Immutable files are excluded from WRITE job plans unless an override protocol is explicitly invoked, typically requiring a security review and meta-audit.
**Example Use Case**:\
At the beginning of a new cascade deployment, the `system_manifest.md` is written with core routing doctrine and declared immutable:
`<!-- @meta { "fileType": "immutable", "editPolicy": "readonly" } -->`
Its SHA-256 hash is stored in `audit/integrity_snapshot.md`. Months later, during a routine load plan, a WRITE job attempts to touch `system_manifest.md`. The AI aborts the WRITE, reports a violation, and confirms that the file's current hash still matches its original snapshot. If the file had been modified by an external process, the hash mismatch would have halted the system until the drift was reviewed.

### 2.5.16 **Integrity Snapshot**
**What**: A canonical ledger of cryptographic SHA-256 hashes for all immutable and protected files in the cascade. This snapshot acts as a tamper-evidence seal, ensuring that foundational files remain unaltered unless explicitly updated through secure processes.\
**Why**: Guarantees architectural trust. If even one protected or immutable file is changed outside an authorized process, the mismatch is immediately detected. This mechanism enables rollback, debugging, and drift detection with cryptographic certainty.\
**Where**:
- Stored in `audit/integrity_snapshot.md` as a flat list of file paths and their associated hashes.
- Cross-referenced during WRITE loops, meta-audits, or when executing security-critical ACT phases.\
  **How**:
- When a file with `fileType: immutable` or `protected: true` is first written or committed, its SHA-256 hash is generated and appended to `audit/integrity_snapshot.md`.
- Example entry:
`/cascade/system_manifest.md: "2c6c2c50d63f78fce4a…"`
- On each hash verification cycle, the system:
  1. Reads the current contents of each tracked file
  2. Recomputes its SHA-256 hash
  3. Compares it against the stored hash in the snapshot
  4. Logs success or halts with a `hashMismatch` if a discrepancy is found
- This process can be triggered automatically during prune cycles, post-WRITE audits, or manually through security review jobs.
**Example Use Case**:\
After promoting a new `init_context.md` for a production cascade, the system writes its initial hash to `audit/integrity_snapshot.md`. Weeks later, a suspicious job attempts to modify that file. Before WRITE, the integrity check runs:
- It re-hashes the current `init_context.md`
- Detects a mismatch from the snapshot
- Triggers an emergency halt, flags the session with `driftFlag`, and denies the write
This ensures that no architectural doctrine can be silently edited without traceable intent and confirmation.

### 2.5.17 **Active Edit Lock**
**What**: A volatile lockfile that signals an in-progress WRITE cycle or an unresolved edit session. It is used to prevent overlapping WRITE operations from multiple agents or AI runs, which could lead to file clobbering, inconsistent diffs, or logic corruption.\
**Why**: Enforces serialization of WRITE operations across the cascade. Prevents race conditions where two concurrent processes could attempt to modify overlapping files, leading to partial state corruption or untraceable logic divergence.\
**Where**:
- The lockfile is located at `_locks/active_edit.lock`.
- It is created automatically at the beginning of any WRITE phase.
- Removed automatically when WRITE completes cleanly, or manually during recovery operations.\
  **How**:
- When the AI begins a WRITE cycle, it checks for the presence of `_locks/active_edit.lock`.
- If the lockfile exists, the AI halts all READ and ACT operations immediately and enters a safe-hold state.
- It logs a `lockConflict`, displays the cause (e.g., "WRITE already in progress"), and provides recovery options such as job retry or manual unlock.
- If the file is stale (e.g., from a crashed loop), cleanup routines in the recovery protocol will verify timestamps and prune the lock safely.

**Example Use Case**:\
During a cascade planning operation, the AI writes `job_logs/temp_job.md` and initiates a WRITE. Before the cycle finishes, an external agent restarts the AI session and begins a new ACT. The new session checks `_locks/active_edit.lock`, finds it present, and halts with a message:
> “Active WRITE lock detected. Halting ACT. Please wait for the prior session to complete or clear `_locks/active_edit.lock` if stalled.”
This guarantees that only one coherent WRITE job can modify the system at a time, preserving atomicity and rollback consistency.

### 2.5.18 **Pre- & Post-Hash Checking**
**What**: A dual-phase verification process that calculates and validates SHA-256 hashes of key files immediately before and after the WRITE phase. This mechanism confirms that no unauthorized edits occurred before writing and that WRITE outcomes exactly match expectations after execution.\
**Why**: Detects corruption, silent overwrites, race-condition side effects, or accidental changes to immutable/protected files. Ensures that the cascade state transitions are trustworthy and have not deviated from plan due to internal or external interference.\
**Where**:
- Executed automatically in loops that involve files flagged with `fileType: immutable` or `protected: true`.
- Tracked against reference values in `audit/integrity_snapshot.md`.
- Integrated into lifecycle hooks during ACT and WRITE.\
  **How**:
- **Pre-Hash Check**:
  - Occurs just before WRITE begins.
  - Recalculates hashes for all monitored files.
  - Compares them to values in `integrity_snapshot.md`.
  - If any mismatch is found, WRITE is aborted and the job is flagged.
- **Post-Hash Check**:
  - Runs immediately after the WRITE concludes.
  - Re-hashes the same set of files and ensures the actual output matches planned changes.
  - Confirms that no unexpected deltas or hidden mutations occurred.
- This validation may be toggled or scoped via metadata flags like `verifyHashes: true`.
**Example Use Case**:\
During a WRITE job that updates `domains/api/index.md`, which is marked `protected`, the AI runs a pre-hash check. It finds the hash matches the snapshot and proceeds with the WRITE. After the update, it runs a post-hash check, but detects that another process concurrently modified the file, introducing an unplanned line. The mismatch is logged:
> “Post-hash validation failed: unexpected mutation in `domains/api/index.md`. WRITE is rolled back and flagged for review.”
This ensures that the actual cascade state aligns with planned WRITE results and protects against tampering or unintended outcomes.

### 2.5.19 **Job Plans**
**What**: Ephemeral planning artifacts created during the ACT phase to define the intended actions, scope, and safety constraints of a WRITE operation. These are stored in structured markdown format (`temp_job.md`) and serve as the authoritative contract for what changes the system is about to execute.\
**Why**: Introduces a layer of traceability and intentionality to the cascade’s WRITE operations. Job plans record the AI’s proposed logic in advance, enable human or system confirmation, and anchor rollback and audit tooling through embedded hashes and metadata.\
**Where**:
- Written to `job_logs/temp_job.md` during ACT.
- Can also appear as `temp_job_*.md` during multi-stage plans or sandboxed proposals.
- Referenced by `meta_audit.md`, `change_log/recent.md`, and security tools.\
  **How**:
- Automatically generated during the ACT phase for any WRITE-bearing task.
- The job plan includes:
  - Target file paths
  - Justification or triggering prompt
  - Scope of planned edits
  - Associated hashes (pre-edit and predicted post-edit)
  - Optional escalation tags (e.g. `requiresReview: true`)
- The plan is confirmed at the start of WRITE, then re-verified after execution via hash checks and outcome alignment.
- If actual file changes differ from the declared plan, a mismatch is logged, and the job may be rolled back.
**Example Use Case**:\
The AI is asked to update logic inside `domains/client/index.md`. During ACT, it drafts a plan in `job_logs/temp_job.md` like so:
`intent: "Patch UI routing schema" targets: - path: "domains/client/index.md" expectedHashBefore: "78ac…" expectedHashAfter: "9b3d…" editPolicy: "appendOnly"  subtype: "buffer" rollbackPlan: "Restore from last known good hash"`
At WRITE time, the system re-validates that the hash of the file still matches `expectedHashBefore`. After writing, it confirms the post-hash. If both match, the job is marked successful in `change_log/recent.md`. If not, a rollback is triggered and a drift alert raised.

### 2.5.20 **Write-Back Summary Confirmation**
**What**: A post-WRITE verification mechanism where the AI re-opens and inspects all recently written files to ensure that the final file states precisely match what was described in the job plan. This process is the last safeguard before marking the loop complete.\
**Why**: Guarantees that the WRITE operation succeeded exactly as intended, without corruption, deviation, or partial application. It validates system trust and confirms readiness for the next cascade cycle. If any discrepancies are detected, corrective action is triggered before the loop advances.\
**Where**:
- Tracked in `change_log/recent.md`, where successful jobs are logged with paths, hashes, and metadata.
- Logged outcomes and any mismatches are also recorded in `audit/meta_audit.md`.\
  **How**:
- After WRITE finishes, the AI loads each target file listed in the job plan.
- It re-computes their current SHA-256 hashes and compares them against the job plan’s `expectedHashAfter`.
- If hashes match, the change is logged as successful and the loop checkpoint is appended.
- If any mismatch is detected, the AI:
  - Flags the mismatch in `meta_audit.md`
  - May rollback or isolate the change
  - Optionally raises a `driftFlag` for future review
- This process can also update cached summaries, trigger rolling update queues, or notify external hooks if enabled by metadata.
**Example Use Case**:\
A WRITE job updates both `domains/api/index.md` and `summary.md`. After writing, the AI performs write-back summary confirmation:
- It reads both files again
- Confirms the hashes match the `expectedHashAfter` in `temp_job.md`
- Appends a record to `change_log/recent.md`:
`- file: domains/api/index.md status: success hash: "3f4a..." sourceJob: temp_job.md`
If `summary.md` was altered externally between job plan and WRITE, the hash would not match and a warning would be filed in `meta_audit.md`.

### 2.5.21 **Summary Merging**
**What**: A system for condensing ephemeral or short-lived files (e.g. `temp_notes/`, `job_logs/`, or inline ACT outputs) into durable summary artifacts such as `summary.md`. This process ensures continuity of long-term context while freeing up buffer space and reducing memory strain in future loops.\
**Why**: Prevents token window saturation by collapsing transient or burst content into compact summaries that retain meaning without needing to re-load the full original data. It supports both Lean Mode and large-scale planning tasks by minimizing unnecessary context rehydration.\
**Where**:
- Target summaries typically live in files like `summary.md`, `domains/*/summary.md`, or `meta_summary.md`.
- Controlled by merge logic defined in `merge_policy`, either embedded in metadata or inferred from path conventions.\
  **How**:
- Files marked with:
`mergeable: true merge_target: "summary.md" merge_policy: "append|squash|collapse"`
are automatically picked up during a merge pass, typically post-WRITE or as part of rolling update triggers.
- Merge policies include:
  - `append`: Adds raw text to the end of the target
  - `squash`: Compresses multiple notes into one structured block
  - `collapse`: Reduces redundancy or reformats based on type
- AI parses the source buffer, summarizes or restructures the content, and inserts it into the merge target.
- Once merged, the source file may be pruned, archived, or marked `ttlCycles: 0` to avoid re-loading.
**Example Use Case**:\
A planning loop generates several files under `temp_notes/ui_buffer.md`, `job_logs/temp_job.md`, and `drafts/alert_summary.md`, each containing useful but ephemeral data. They are marked:
`mergeable: true merge_target: "summary.md" merge_policy: "squash"`
After WRITE, the AI executes a summary merge. It extracts core actions, intentions, and outcomes from those files and produces a structured entry in `summary.md`. The originals are then expired to prevent redundant context inclusion in future loops.

### 2.5.22 **Rolling Update Triggers**
**What**: Lightweight, opportunistic mechanisms that update auxiliary logs, summaries, or plans immediately after a successful WRITE cycle—without requiring a full cascade replan or context reload. These triggers allow the system to keep working memory and reference buffers up-to-date with minimal overhead.\
**Why**: Maintains the freshness and relevance of recent job context, system state, and planning artifacts without breaching token limits or initiating a full loop cycle. It enables continuous summarization, smooth token budgeting, and fast recovery logic by incrementally updating downstream context files.\
**Where**:
- Common targets include:
  - `change_log/recent.md` (tracks last N successful jobs)
  - `load_plans/` (stores adjusted execution paths)
  - `temp_notes/` and `domains/*/summary.md`
- Coordinated via metadata embedded in source files or job plans.\
  **How**:
- Controlled by metadata flags such as:
`rollingUpdate: true mergeTarget: "recent.md"`
- After WRITE completes, the system checks whether any of the affected files are tagged for rolling updates.
- If found, the update queue is activated to opportunistically push summaries, logs, or merged plans to their designated destinations.
- These actions are non-blocking—failures are logged but don’t halt the loop.
- Some merge operations are deferred into background processes (e.g. `rolling_merge_queue`) to reduce I/O contention.

**Example Use Case**:\
A WRITE operation updates `domains/infra/index.md` with metadata:
`rollingUpdate: true mergeTarget: "change_log/recent.md"`
Once the job completes and passes post-hash checks, the AI adds a one-line summary of the operation to `recent.md`. This happens outside the main WRITE path and avoids triggering a full context cascade. Meanwhile, a background merge may also compress the job intent into a structured `load_plans/infra.json` for future reuse.

### 2.5.23 **Eviction Policy & Prune Plan**
**What**: Declarative rules and lifecycle scripts that define how and when to delete or archive temporary, expired, or unnecessary files from the cascade system. These policies ensure that buffers, drafts, job logs, and speculative files don’t accumulate and overload the token window or corrupt loop integrity.\
**Why**: Prevents performance degradation, memory bloat, stale context leakage, and token limit breaches. By pruning files no longer relevant to the current cascade cycle, the system preserves efficiency and focuses on active, high-signal data.\
**Where**:
- Master policy defined in `audit/prune_plan.md`.
- Applied to all temp paths like `_taskbuffers/`, `temp_notes/`, `job_logs/`, `drafts/`, and `domains/*/scratch/`.
- Referenced by recovery protocols, ACT scripts, and lifecycle routines.\
  **How**:
- Files include metadata like:
`fileType: temporary ttlCycles: 1 expirationPolicy: "pruneOnIdle"`

- `ttlCycles`: Counts down with each loop—files are removed when it hits 0.
- `expirationPolicy` options include:
  - `pruneOnIdle`: remove if not referenced during last ACT
  - `forceAfter`: prune after hard TTL regardless of context use
  - `archiveOnExpire`: move to cold storage instead of deleting
- Prune passes may be triggered:
  - Automatically at end of WRITE
  - Manually via prompt (“flush expired buffers”)
  - As part of loop recovery or cleanup during drift detection

**Example Use Case**:\
During cascade planning, the AI creates `temp_notes/nextUIPlan.md`:
`fileType: temporary ttlCycles: 1 expirationPolicy: "pruneOnIdle"`
After WRITE, if this file isn’t re-referenced in the next ACT, the prune script deletes it. If the file was promoted to `mergeTarget: summary.md`, its content survives the cleanup, but the original temp file is still removed to prevent clutter.

### 2.5.24 **Token Budget Awareness**
**What**: A system that tracks the estimated token footprint of individual files and entire cascade branches. It helps the AI anticipate memory usage during READ and ACT phases, enabling smarter context loading and controlled execution in Lean Mode.\
**Why**: Prevents context overrun, degraded performance, and partial file loading by proactively budgeting token use across all files and domains. This makes large-scale reasoning possible without exceeding the token window or losing key dependencies mid-loop.\
**Where**:
- Tracked in `audit/token_summary.md`, which stores per-file and per-branch estimates.
- Referenced in load planning, summary merging, eviction decisions, and Lean Mode loops.\
  **How**:
- Estimates are generated via:
  - AI dry-run parsing of files
  - Actual token counts from previous READs
  - Metadata annotations (e.g. `tokenEstimate: 2048`)
- Token usage per domain or path is recorded and periodically refreshed.
- If estimated usage exceeds available budget (especially in Lean Mode), the AI:
  - Defers non-critical files
  - Merges summaries
  - Evicts expired buffers
  - Or prompts for restructuring (e.g. “split into submodules”)
- The system may also suggest optimization jobs when a single domain threatens to exceed its token share.
**Example Use Case**:\
During a Lean Mode boot, the AI reviews `audit/token_summary.md`:
`- path: "domains/client/index.md" tokenEstimate: 3864 - path: "temp_notes/ui_trace.md" tokenEstimate: 1212`
Because the total estimated token load exceeds the max budget, the AI elects to drop `temp_notes/ui_trace.md` and instead uses `summary.md` as a compressed substitute. It logs the skipped file and ensures routing logic is preserved by loading its merged summary instead.

### 2.5.25 **Validator Pipeline**
**What**: A command-line and script-invocable validation utility that checks for structural, metadata, and schema correctness across all files in the cascade. It ensures that file headers, metadata blocks, fileType declarations, and lifecycle tags are properly formed and conform to system constraints.\
**Why**: Protects the cascade from malformed inputs, undefined behaviors, and silent logic failures by enforcing policy and format compliance before files are loaded, merged, or written. This acts as a pre-flight integrity layer for all file-based interactions.\
**Where**:
 - Primary logic lives in `validators/metadata_validator.md`.
- Called during:
  - Manual developer audits
  - Pre-WRITE ACT logic
  - Test checkpoints and cascade promotion gates
- Errors are logged to `meta_audit.md` and terminal output.\
  **How**:
- Parses each file’s frontmatter and inline `@meta` blocks.
- Validates:
  - Required fields (e.g. `fileType`, `editPolicy`, `domain`)
  - Allowed values (`editPolicy: readonly`, `appendOnly`, etc.)
  - Cross-file consistency (e.g. `mergeTarget` must exist)
  - Unsupported or deprecated metadata fields
- Also checks for:
  - Duplicate hashes in `integrity_snapshot.md`
  - Missing summary policies
  - Invalid `ttlCycles`, `expirationPolicy`, or undefined domains
- Reports results in structured output, optionally with `--fix` mode to auto-suggest or correct minor issues.
**Example Use Case**:\
A developer adds `drafts/test_ui.md` with malformed metadata:
`fileType: rolling subtype: buffer editPolcy: appendOly # typo`
Running the validator as documented in `validators/metadata_validator.md`:
`npx ts-node path/to/validator`
Returns:
`✖ drafts/test_ui.md - Unknown field: "editPolcy" - Did you mean: "editPolicy"? - Invalid value for editPolicy: "appendOly"`
The AI or dev can now correct this before the file enters the cascade context.

### 2.5.26 **Security Review & High-Risk Action Logging**
**What**: A protocol that governs and logs high-risk operations—such as schema rewrites, file resets, metadata escalations, or modifications to critical system files. It provides a structured framework for traceability, oversight, and rollback of sensitive actions that could affect cascade integrity or governance.\
**Why**: Protects against untraceable changes to foundational structures and enforces auditability for actions that fall outside normal cascade behavior. Ensures that schema migrations, manifest edits, or escalated job plans are logged, reviewed, and verified for intent and safety.\
**Where**:
- Core policy and escalation criteria live in `security/security_review.md`.
- Logged events and anomalies are recorded in `audit/meta_audit.md`.
- Also referenced from elevated job plans via special flags or tags.\
  **How**:
- Triggered automatically when job plans or metadata contain sensitive fields such as:
`requiresReview: true securityLevel: high escalation: true`

- Typical triggers include:
  - Edits to `system_manifest.md`, `loop_protocol.md`, or domain indexes
  - Schema migrations or fileType reclassifications
  - Overrides to `readonly`, `immutable`, or `protected` policies
- When triggered, the AI:
  - Logs the full change intent and context in `meta_audit.md`
  - May halt the WRITE phase until confirmation is received
  - Flags the job in `security_review.md` with rationale, hash changes, and rollback strategy
- In some cases, reviewers (human or agent) must co-sign the plan before execution is allowed.

**Example Use Case**:\
An engineer attempts to update `system_manifest.md` to redefine domain routing rules. The job plan is tagged:
`requiresReview: true securityLevel: high`
This triggers a halt before WRITE. The AI records the intent and changes in `meta_audit.md`:
`- file: system_manifest.md action: attempted mutation status: blocked reason: securityReview triggered`
Reviewers are notified or prompted to confirm, and the job remains pending until explicitly approved.

### 2.5.27 **Drift Flag & Meta Audit**

**What**: A two-part mechanism for detecting and recording inconsistencies, contradictions, or unexpected mutations in the cascade state. The `drift_flag.md` acts as a live signal that something in the lifecycle has deviated from expected behavior, while `meta_audit.md` provides a persistent log of such anomalies for later inspection and recovery.\
**Why**: Maintains systemic trust by catching silent failures, state mismatches, or improperly applied writes. Enables forensic debugging, targeted rollbacks, and context restoration after suspected corruption or protocol deviation.\
**Where**:
- Drift signals are written to `lifecycle/drift_flag.md`.
- Anomalies, violations, or mismatches are logged in `audit/meta_audit.md`.
- These files are referenced during boot, WRITE prep, and recovery plans.\
  **How**:
- The AI monitors for several categories of drift:
  - Loop counter mismatches (e.g., `writeCount` skipped unexpectedly)
  - Hash mismatches on protected or immutable files
  - Validator schema diffs from known snapshots
  - Unexpected file deletions, truncations, or scope shifts
- When drift is detected:
  - `drift_flag.md` is generated or updated with a plain-text summary
  - The affected files and trigger condition are logged in `meta_audit.md`
  - The loop may be halted, rerouted to a recovery job, or re-initiated in safe mode
- Drift flags are cleared manually or via an explicit `ACK` loop or rollback job.

**Example Use Case**:\
After a WRITE cycle completes, the system checks `domains/server/index.md` against its known hash. A mismatch is detected, but the file wasn’t targeted by any recent job plan. The AI writes:
`# lifecycle/drift_flag.md Detected unauthorized mutation in domains/server/index.md Expected hash: 4f8b... Actual hash: e7ac... Triggered halt. Recovery required.`
Simultaneously, `meta_audit.md` records:
`- type: drift source: hash check file: domains/server/index.md loop: 47 resolution: pending`
The system blocks further writes until the issue is resolved, acknowledged, or overridden with a recovery plan.28. **Hash Verification Workflow**
**What**: 4-step process to recalc and validate immutable files.\
**Why**: Core to preventing architectural corruption.\
**Where**: `integrity_snapshot.md`, `immutable` files\
**How**: Recalc → Compare → If mismatch → Halt + Log + Flag

### 2.5.29 **Schema & Snapshot Testing**
**What**: A mechanism that captures the structure, schema, and metadata state of API, domain, or configuration files at key lifecycle milestones. These snapshots create versioned records of system shape and logic, enabling structural regression tests, diff tracking, and rollback restoration.\
**Why**: Ensures that critical parts of the cascade—like domain interfaces, API declarations, and routing schemas—can be audited, compared over time, and recovered if broken. By snapshotting state at trusted intervals, the system guards against accidental drift, logic corruption, or undetected protocol mutations.\
**Where**:
- Snapshots are written to:
  - `domains/schema/` (organized by domain or feature set)
  - `audit/schema_snapshot.md` (index of snapshot hashes and change reasons)
- Source files may include `index.md`, `*.schema.json`, or metadata-tagged logic layers.\
  **How**:
- Triggered automatically during:
  - Major version promotion (e.g. domain or cascade release)
  - Post-validation if structural diffs are detected
  - Security review jobs that modify schemas
- Snapshot files include:
  - Source file paths
  - Schema or interface definitions at that point in time
  - SHA-256 hashes of captured state
  - Optional diff vs. prior snapshot
- Snapshots can be restored to reverse schema-level corruption or guide rollback jobs.
**Example Use Case**:\
The AI promotes a new domain version after modifying `domains/payment/index.md`. As part of the release job, it snapshots the schema into `domains/schema/payment_v2_snapshot.md`, and appends to `audit/schema_snapshot.md`:
`- domain: payment version: v2 path: domains/schema/payment_v2_snapshot.md hash: "9b2c..." trigger: version promotion`
Weeks later, if the system encounters unexpected behavior or a failed validation on `payment/index.md`, it can reload the v2 snapshot, compare diffs, and offer a rollback patch to the last known good state.

### 2.5.30 **Extension Patterns (Counters, File Types)**
**What**: A structured protocol for introducing new functional components into the cascade system—such as custom counters, novel file types, domain branches, or metadata behaviors. These extension patterns allow developers and AI agents to expand system logic in a modular and forward-compatible way.\
**Why**: Ensures the system remains extensible and adaptable to emerging requirements, while maintaining architectural integrity. By enforcing a canonical lifecycle for extensions, the cascade avoids schema fragmentation, logic drift, and undocumented side effects.\
**Where**:
- Extensions are defined within working files such as:
  - `drafts/` for speculative types or counters
  - `metadata_schemas.md` for formal field/type registration
  - `system_manifest.md` for official system-wide declarations
  - `validators/metadata_validator.md` for validation logic
- Metadata tags like `counter: true`, `fileType: extension`, or `routingClass: custom` are used to register new entities.
- Use `job_logs/temp_job.md` to test and trace new extensions during staged rollout.\
  **How**:\
  The extension workflow follows five canonical phases:
1. **Draft**
   - Define the proposed new construct in a `drafts/` file or `temp_notes/` buffer
   - Include purpose, usage examples, expected metadata, and test plan
2. **Validate**
   - Run the validator to ensure metadata syntax, reserved fields, and dependencies are well-formed
   - Confirm it won’t break existing counters or hash plans
3. **Register**
   - Add the new construct to `system_manifest.md`
   - Declare allowed values and routing behavior in `metadata_schemas.md`
4. **Plan**
   - Introduce a job that applies the new feature in a scoped environment
   - Use `job_logs/temp_job.md` to validate side effects and rollback logic
5. **Route**
   - Ensure the new feature is properly integrated into `domain:` routing or load plan filters
   - Adjust token budgets and prune plans if needed
**Example Use Case**:\
A developer wants to add a new counter `loadCount_ai` to track AI execution load. They:
- Draft a metadata spec in `drafts/counter_ai.md`
- Add it to `metadata_schemas.md` under allowed counters
- Extend `system_manifest.md` to register it as recognized and mutable
- Test with a dry-run in `job_logs/temp_job.md`
- Patch domain index files to include its routing and retention behavior
This integration allows the AI to use the counter in ACT/WRITE while ensuring audit consistency and compatibility with the cascade model.2.5.31 **External Integrations & Hooks**
**What**: A modular framework that allows the ContextCascade system to interact with external tools such as CI/CD pipelines, ticketing systems, logging frameworks, or messaging platforms. These integrations allow cascade logic to trigger real-world effects or ingest signals from external sources.\
**Why**: Bridges the gap between the cascade’s internal planning and real-world systems, enabling tasks like automated deployments, alerting, task creation, or metadata syncing. Supports traceable automation across tools while maintaining audit integrity.\
**Where**:
- Logic and adapters live in the `external/` directory.
- Activated by metadata flags in job plans or file declarations:
`external: true externalHooks: - type: webhook target: "https://ci.example.com/build" trigger: "postWrite"`
- Results and responses may be cached in `external/cache/`, or logged in `meta_audit.md`.\
  **How**:
- When a file or job is marked `external: true`, it is eligible to trigger integration hooks.
- Supported hook types include:
  - `webhook` (HTTP POSTs to URLs)
  - `filePush` (syncs files to external mounts)
  - `logEntry` (adds entries to external logs or dashboards)
  - `ticketCreate` (opens a task or issue)
- Triggers may fire:
  - During ACT (to plan side effects)
  - Post-WRITE (to confirm success or send payloads)
  - On validation failure (to alert maintainers)
- Execution is non-blocking: failures are logged but do not halt the cascade unless marked `critical: true`.
**Example Use Case**:\
A domain update in `domains/server/index.md` includes:
`external: true externalHooks: - type: ticketCreate trigger: postWrite target: "jira://CC-243"`
After the WRITE completes, the system sends a structured payload to the configured JIRA integration. A new ticket is created referencing the job plan, source file, and outcome. The action is logged in `meta_audit.md`:
`- type: external hook: ticketCreate target: CC-243 status: success`

### 2.5.31 **External Integrations & Hooks**
**What**: A modular framework that allows the ContextCascade system to interact with external tools such as CI/CD pipelines, ticketing systems, logging frameworks, or messaging platforms. These integrations allow cascade logic to trigger real-world effects or ingest signals from external sources.\
**Why**: Bridges the gap between the cascade’s internal planning and real-world systems, enabling tasks like automated deployments, alerting, task creation, or metadata syncing. Supports traceable automation across tools while maintaining audit integrity.\
**Where**:
- Logic and adapters live in the `external/` directory.
- Activated by metadata flags in job plans or file declarations:
`external: true externalHooks: - type: webhook target: "https://ci.example.com/build" trigger: "postWrite"`
- Results and responses may be cached in `external/cache/`, or logged in `meta_audit.md`.\
  **How**:
- When a file or job is marked `external: true`, it is eligible to trigger integration hooks.
- Supported hook types include:
  - `webhook` (HTTP POSTs to URLs)
  - `filePush` (syncs files to external mounts)
  - `logEntry` (adds entries to external logs or dashboards)
  - `ticketCreate` (opens a task or issue)
- Triggers may fire:
  - During ACT (to plan side effects)
  - Post-WRITE (to confirm success or send payloads)
  - On validation failure (to alert maintainers)
- Execution is non-blocking: failures are logged but do not halt the cascade unless marked `critical: true`.
**Example Use Case**:\
A domain update in `domains/server/index.md` includes:
`external: true externalHooks: - type: ticketCreate trigger: postWrite target: "jira://CC-243"`
After the WRITE completes, the system sends a structured payload to the configured JIRA integration. A new ticket is created referencing the job plan, source file, and outcome. The action is logged in `meta_audit.md`:
`- type: external hook: ticketCreate target: CC-243 status: success`

### 2.5.33 **Index Map (System + Domain Indexes)**
**What**: A collection of structured index files that describe the layout, ownership, and hierarchy of the cascade system. These files form the backbone of system traversal logic, load planning, and prompt-driven READ scaffolding. The master index is complemented by per-domain indexes that detail their local scope and routing schema.\
**Why**: Enables deterministic boot, accurate domain routing, and memory-aware loading. Index maps provide the AI with the system’s file topology, ensuring it can selectively load context, respect scope boundaries, and update paths in a coordinated way.\
**Where**:
- Global system map: `/cascade/index.md`
- Domain-specific indexes: `/domains/*/index.md`
- Referenced during Lean Mode, prompt parsing, job planning, and path diffs.\
  **How**:
- Each index includes metadata such as:
`fileType: index domain: server routes: - path: "index.md" scope: "protocol" - path: "actions/schema.md" scope: "interface"`

- Upon boot or directory change, the AI loads `/cascade/index.md` and then recursively loads relevant domain indexes.
- The combined map is used to:
  - Construct READ plans
  - Enforce domain routing boundaries
  - Detect missing or orphaned files
  - Resolve `mergeTarget`, `loadPlan`, or `writeGate` mappings
- Indexes are updated whenever a new file is added, renamed, or moved within a domain.
- In Lean Mode, only top-level indexes and `summary.md` are loaded unless deeper traversal is explicitly triggered.
**Example Use Case**:\
A new domain `auth/` is added with files for login and token validation. The dev writes `/domains/auth/index.md`:
`fileType: index domain: auth routes: - path: "login.md" scope: "action" - path: "token.md" scope: "validator"`
This is then linked in `/cascade/index.md`:
`- domain: auth path: "domains/auth/index.md"`
During ACT, the AI reads only the auth index and summary to determine token scope, and skips loading unrelated domains like `infra/` or `ui/`.

### 2.5.34 **System Manifest (`system_manifest.md`)**
**What**: The foundational, immutable declaration of system structure, architectural doctrine, and routing configuration for the entire ContextCascade environment. It acts as the canonical source of truth for domain layout, extension patterns, global policies, and lifecycle roles.\
**Why**: Serves as the anchor for all cascade logic, ensuring that core invariants (e.g. routing maps, extension boundaries, domain scopes) are declared up front and protected against accidental modification. Immutable and hash-locked, it enforces system-level integrity and auditability.\
**Where**:
- Path: `/cascade/system_manifest.md`
- Referenced at boot, during job planning, schema validation, and write routing.
- Protected by hash in `audit/integrity_snapshot.md`.\
  **How**:
- Declared with:
`fileType: immutable editPolicy: readonly domain: core`
- Includes:
  - Canonical domain list and paths
  - Extension policies (e.g. how to add new file types, counters, hooks)
  - Core lifecycle policies (e.g. which domains are mutable, which files are checkpointed)
  - Global routing rules (e.g. which paths get loaded for `client`, `server`, etc.)
- Any attempt to edit is blocked unless passed through a security review job with elevated `requiresReview: true`.
- During hash check cycles, its SHA-256 is compared to the stored reference in `integrity_snapshot.md`. Any mismatch halts all WRITE activity.
**Example Use Case**:\
A developer attempts to introduce a new `fileType: lifecycleCheckpoint` for use in test scaffolds. Before rollout, they must:
1. Propose the change in a job plan
2. Extend `system_manifest.md` to register the new file type
3. Pass validator and trigger a high-risk security review\
   Only after approval and hash registration is the file type accepted by ACT/WRITE logic.
A post-approval snapshot entry might look like:
`- file: /cascade/system_manifest.md hash: 0c9e… approvedBy: validator + securityReview`

### 2.5.35 **Loop Checkpoint (`loop_checkpoint.md`)**
**What**: A sequential log that records the successful completion of each full cascade loop—from READ through ACT to WRITE. Each line corresponds to one full cycle, documenting the job identifier, actions taken, validation outcome, and resulting checkpoint state.\
**Why**: Supports traceability, rollback orchestration, drift detection, and session reconstruction. By maintaining a line-per-loop history, the system can track progress, identify gaps or failures, and offer partial rehydration from known-safe checkpoints.\
**Where**:
- Logged in `/checkpoints/loop_checkpoint.md`.
- Referenced by:
  - `meta_audit.md` for session consistency checks
  - Recovery protocols for restart boundaries
  - Job comparison tools during rollback or merge\
    **How**:
- Automatically appended during the final stage of the WRITE phase, after all hash checks, confirmations, and post-WRITE tasks complete successfully.
- Each entry includes:
  - Loop ID or timestamp
  - Summary of modified files
  - Job hash and plan reference
  - Outcome status (e.g. `success`, `rolledBack`, `partial`)
- If WRITE fails or is aborted, no entry is written, ensuring that `loop_checkpoint.md` only reflects finalized system state.
**Example Entry**:
`- loop: 147 timestamp: 2025-06-26T03:45Z jobPlan: job_logs/temp_job.md filesWritten: - domains/client/index.md - summary.md outcome: success postHash: confirmed`
This allows the system to:
- Roll back to loop 147 if future drift occurs
- Confirm that `temp_job.md` was successfully executed
- Determine which summaries or rolling updates should follow
- Resume or replay history for session threading during audits

### 2.5.35 **Bootstrap Protocol (`00_BOOTSTRAP.md`)**
**What**: The mandatory system entrypoint file that governs how every cascade session begins. It defines foundational protocol rules, memory scope boundaries, and immutable boot preconditions. This file is read first during every session to initialize control flow and enforce cascade constraints.\
**Why**: Ensures all reasoning sessions start from a clean, validated baseline—before any ACT or WRITE occurs. It protects the system from unauthorized mutations, enforces structural discipline, and prevents protocol violations at loop start.\
**Where**:
- File path: `/cascade/00_BOOTSTRAP.md`
- Always read before any other file in the cascade
- Referenced in documentation, loop rules, and the first checkpoint\
  **How**:
- Declared as:
`fileType: immutable editPolicy: readonly purpose: "Bootstrap file enforcing protocol startup, scope discipline, and memory system entry constraints."`
- The file includes:
  - A strict startup sequence:
    - Load `/cascade/index.md` (structure map)
    - Load `/cascade/protocols/loop_protocol.md` (loop control logic)
    - Respect all `@meta` headers and file lifespans
    - Check and verify all `immutable` hashes
    - Abort WRITE if any hash check fails
  - Scope boundaries:
    - No `.md` files should duplicate app logic
    - The cascade is for memory, plans, protocols, not implementation code
    - Writes to app logic must be done outside `/cascade/`
  - Summary declaration:
    > **If it’s not memory, constraint, protocol, or trace — it doesn’t belong in Cascade.**
**Example Boot Flow**:\
A session begins. The AI:
1. Loads `/cascade/00_BOOTSTRAP.md`
2. Reads:
   - `/cascade/index.md`
   - `/protocols/loop_protocol.md`
   - `/protocols/file_lifespans.md`
3. Verifies all required `immutable` hashes
4. If all checks pass → proceeds to ACT
5. If a failure is detected (e.g. `system_manifest.md` hash mismatch) → halts WRITE and logs:
`- file: /cascade/system_manifest.md issue: failed immutable hash check action: WRITE halted loggedIn: /audit/meta_audit.md`

## 3. Directory & File Map

### 3.1 Full Directory Tree

```plaintext
/cascade/
├── 00_BOOTSTRAP.md                      # AI bootstrap file: mandatory first-read (immutable)
├── index.md                             # Master index & link map  (structural)
├── system_manifest.md                   # Immutable doctrine file (immutable)
├── init_context.md                      # Immutable North-Star    (immutable)
├── protocols/
│   ├── loop_protocol.md                 # READ → ACT → WRITE flow
│   ├── file_lifespans.md                # Threshold & maxDepth rules
│   ├── safeguards.md                    # Hashing & write-gate logic
│   └── recovery.md                      # Crash / resume instructions
├── lifecycle/
│   ├── counter.md                       # Global lifecycle counter
│   ├── client.md                        # Client-side counter
│   ├── server.md                        # Server-side counter
│   ├── schema.md                        # Schema counter
│   ├── security.md                      # Security events counter
│   └── drift_flag.md                    # Unresolved contradiction counter
├── change_log/
│   ├── recent.md                        # Rolling log (max 7 entries)
│   └── summary.md                       # Append-only historical log
├── job_logs/
│   └── temp_job.md                      # Ephemeral job plan + PRE hashes
├── load_plans/                          # Evictable read-plan cache
│   └── *.md
├── _taskbuffers/                        # One-prompt scratch buffers
│   └── *.md
├── temp_notes/                          # Rolling planning / notes
│   └── *.md
├── security/
│   ├── security_review.md               # Manual / AI audit findings
│   └── write_gates.md                   # Glob patterns for protected paths
├── audit/
│   ├── token_summary.md                 # Token budget snapshot
│   ├── integrity_snapshot.md            # SHA-256 hashes of immutable files
│   ├── meta_audit.md                    # Drift / contradiction audit
│   └── prune_plan.md                    # Controlled cleanup operations
├── checkpoints/
│   └── loop_checkpoint.md               # ✓ READ ✓ ACT ✓ WRITE marker per cycle
├── domains/
│   ├── client/
│   │   └── index.md                     # Client domain index (structural)
│   │   └── *.md                         # Client guidance docs
│   ├── server/
│   │   └── index.md
│   │   └── *.md
│   └── schema/
│       └── index.md
│       └── *.md
├── _locks/
│   └── active_edit.lock                 # Concurrency guard (single-writer)
├── validators/
│   └── metadata_validator.md            # Validator usage documentation
└── _meta/
    └── cascade_feature_index.md         # Master feature & directory catalogue
```

## 3.2 File Type Classification

## 3.2.1 Canonical FileType Registry
The table below is the **single source of truth** for `fileType` values.
Any value not in the **FileType** column must instead be declared as a `subtype`.

## 3.2.2 File Classes Overview
Each file must declare a `fileType`. Optional `subtype` is allowed only where listed.

| #  | FileType        | Allowed Subtypes / Aliases        | Description & Behavior                                                                 | Lifespan       | Typical Examples                                         |
|----|-----------------|-----------------------------------|----------------------------------------------------------------------------------------|----------------|----------------------------------------------------------|
| 1  | **permanent**   | `checkpointed`                    | Editable files that persist indefinitely; part of core memory or architecture.         | Infinite       | `overview.md`, `state/current.md`                        |
| 2  | **immutable**   | –                                 | Never changes post-creation; cryptographic hash-checkable; often doctrine or manifest. | Infinite\*     | `system_manifest.md`, `init_context.md`,`00_BOOTSTRAP.md`|
| 3  | **rolling**     | `buffer`                          | FIFO/LRU storage; rotates oldest entries after N loops or bytes.                       | Dynamic        | `change_log/recent.md`, `taskbuffers/tmp_note.md`        |
| 4  | **append-only** | –                                 | Only grows via append; no in-place edits or deletions.                                 | Infinite       | `meta_audit.md`, `change_log/summary.md`                 |
| 5  | **temporary**   | `temp`, `ephemeral`, `job_plan`   | One-prompt lifespan; deleted immediately after WRITE or next loop.                     | 1 loop         | `_taskbuffers/*.md`, `job_logs/temp_job.md`              |
| 6  | **counter**     | –                                 | Tracks lifecycle counters, ticks, or thresholds.                                       | Infinite       | `lifecycle/counter.md`, `client_tick.md`                 |
| 7  | **evictable**   | –                                 | Cache-like or speculative plans; lifespan capped via TTL or cycles.                    | TTL-bound      | `load_plans/plan.md`, `prune_plan.md`                    |
| 8  | **protected**   | –                                 | Editable overall, but write-locked inside `<!-- PROTECTED -->` regions.                | Infinite       | `safeguards.md`, `write_gates.md`                        |
| 9  | **structural**  | `domain_spec`, `index`            | Defines logical structure, mappings, and directory specs; affects routing.             | Infinite       | `index.md`, `cascade_feature_index.md`                   |

**Notes:**
- **Schema Rule**: Every file *must* declare `fileType`. Subtypes are optional but must match the allowed aliases above.
- **Hash-Invariant**: `immutable` files should have content-hash footprints for diff detection and integrity checks.
- **Protected regions**: Should be respected during automated WRITE unless explicitly overridden by developer intent.



## 4 Matadata Blocks
Comprehensive guide to the hidden JSON headers that power ContextCascade.

Every file begins with a single, miniature contract written as an HTML‑style comment. This block tells the assistant exactly how it may read, write, merge, and eventually retire the file. Master these blocks and you master the entire cascade.

### 4.2 Purpose & Philosophy
    Metadata blocks externalise file behaviour that would otherwise live in brittle prompt memory:
        -Self‑describing files — new contributors can open any file and instantly understand its role.
        -Machine control — AI and validators use the keys to decide when to load, edit, hash‑check, or archive.
        -Token efficiency — granular readPriority, ttlCycles, and evictionPolicy help ContextCascade stay lean.
        -Auditability — immutable hashes, timestamps, and versioning create a clear forensic trail.

### 4.3 Placement & Syntax
| Rule                                                   | Why it matters                                                                                            |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| **First line of the file**                             | Ensures the AI sees it before any other content during READ.                                              |
| **HTML comment wrapper** `<!-- @meta { … } -->`        | Keeps Markdown render clean while remaining machine‑readable.                                             |
| **Valid JSON inside**                                  | Parsed by both the AI and the metadata validator described in `validators/metadata_validator.md`. No trailing commas, double‑quoted keys/values. |
| Inline `//` comments **allowed** outside of production | Permitted for examples & docs; the validator strips them. Remove in live files to stay strict‑JSON.       |
| **One block only** per file                            | Multiple blocks cause undefined behaviour; the first wins.                                                |

**Example Minimal Block**
```markdown
<!-- @meta { "fileType": "temporary", "purpose": "Scratch for current prompt", "editPolicy": "overwrite", "ttlCycles": 1 } -->
```

### 4.4 Required vs Optional Keys
| Category                              | Keys                                                                                       | Notes                                                   |
| ------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------- |
| **Required in every file**            | `fileType`, `purpose`, `editPolicy`                                                        | `fileType` must match the Canonical Registry.           |
| **Conditional (depends on fileType)** | `maxEntries`, `evictionPolicy`, `ttlCycles`, `expirationPolicy`                            | Only meaningful for rolling / temp / evictable classes. |
| **Lifecycle & routing**               | `routeScope`, `ownedBy`, `refreshInterval`, `linkedDomains`                                | Guide counters and selective READ plans.                |
| **Safeguards**                        | `requires_hash_check`, `write_protected`, `requires_review`                                | Trigger integrity snapshot or human approval.           |
| **Merge & archive**                   | `mergeable`, `merge_policy`, `merge_target`, `archive_on_write`, `merge_trigger_threshold` | Control WRITE‑time content folding & history capture.   |
| **Meta‑meta**                         | `created`, `lastModified`, `version`, `external`                                           | Purely informational but useful in audits.              |


### 4.5 Protected Sections & Metadata
Metadata blocks themselves cannot sit **inside** a `<!-- PROTECTED -->` range (the validator rejects this). However, a file classified as `protected` **may** include a separate PROTECTED region *after* the metadata. Example:

```markdown
<!-- @meta { "fileType": "protected", "purpose": "List of critical gates", "editPolicy": "appendOrReplace" } -->
**Write Gates**
<!-- PROTECTED -->
- index.md
- loop_protocol.md
<!-- END PROTECTED -->
```
*Attempting to modify text between the PROTECTED markers triggers a WRITE abort and a security counter increment.*


### 4.6 Validation & Linting [TO BE BUILT]
- **CLI**: see `validators/metadata_validator.md` for schema, unknown key, alias misuse, and JSON validity checks.
- **AI Self‑check**: During READ, the assistant drops any file whose metadata fails to parse cleanly.
- **CI**: Recommended to run validator in pre‑commit hook to catch drift before merge.

Validation levels:
1. **Syntax** — JSON parses?
2. **Schema** — Required keys present? Enum values allowed?
3. **Cross‑ref** — `fileType` vs path, `subtype` alias list, `ownedBy` exists?
4. **Hash** — If `requires_hash_check`, verify against latest snapshot.

### 4.7 Best Practices & Common Anti‑Patterns
**Do**
- Keep headers < 10 lines for most files.
- Use `ttlCycles` for scratch pads to prevent stale token bloat.
- Promote `rolling` logs into `summary.md` before eviction.
- Increment `version` manually when human edits immutable doctrines.
**Don’t**
- Copy the superset block verbatim into live files.
- Omit `purpose` — future devs will curse you.
- Forget to update `lifecycle/*.md` counters when adding new domain files (they reference metadata).
- Place two `@meta` blocks; the validator will flag but AI may read the wrong one first.

### 4.8 Troubleshooting Quick Table
| Symptom                             | Likely Cause                                                  | Fix                                                 |
| ----------------------------------- | ------------------------------------------------------------- | --------------------------------------------------- |
| *Validator error: unknown fileType* | Typo or non‑registry value                                    | Use canonical list or add alias in registry.        |
| *File skipped in READ*              | `readPriority: low` + token pressure                          | Raise priority or trim other files.                 |
| *Hash mismatch abort in WRITE*      | `requires_hash_check: true` but file modified outside cascade | Investigate manual edits; update snapshot if legit. |
| *Metadata parsed but keys ignored*  | Key not yet supported by AI version                           | Remove/replace with supported logic.                |

### 4.9 ContextCascade Metadata Block - Superset Example
Below is a **theoretical metadata block** that intentionally includes **every field currently defined** in the ContextCascade specification. It is **not meant to be copied verbatim** into production files; instead it serves as a complete reference so you can copy‑paste only the keys you need.

```markdown
<!-- @meta {
  "fileType": "rolling",            // Required > One of the canonical registry values.
  "subtype": "buffer",              // Conditional > Narrower alias that refines `fileType` behaviour.
  "routeScope": "client",           // Optional > Domain routing hint: client | server | schema | global.
  "ownedBy": "lifecycle/client.md", // Optional > Pointer to the counter or parent that governs this file.
  "purpose": "Demonstration of every permissible metadata key.",  // Optional > Descriptive free-text summary of the file's intent or role in the cascade; enhances audit clarity, plan tracing, and developer readability. Optional but recommended.
  "editPolicy": "appendOrReplace",   // Optional > How the AI may edit: readonly | appendOnly | overwrite | appendOrReplace.
  "maxEntries": 5,                    // Conditional > Rolling‑buffer cap (valid when `fileType` = rolling).
  "evictionPolicy": "FIFO",          // Conditional > Strategy when buffer exceeds `maxEntries`.
  "ttlCycles": 3,                     // Conditional > Automatic eviction after N lifecycle increments (temp/evictable only).
  "refreshInterval": 5,               // Optional > Force READ reload every N cycles, even if thresholds not met.
  "readPriority": "medium",          // Optional > high | medium | low – used to drop files when tokens are tight.
  "requires_hash_check": true,        // Optional > If true → verify SHA‑256 before & after WRITE.
  "archive_on_write": true,           // Optional > If true → archive previous revision to /_archive/.
  "mergeable": true,                  // Optional > Marks file eligible for auto‑merge logic.
  "merge_target": "change_log/summary.md", // Conditional  > Default destination if merged elsewhere.
  "merge_policy": "squash",          // Conditional > append | squash | integrate – how to combine content.
  "write_protected": false,           // Optional > Hard block AI writes unless explicitly overridden.
  "requires_summary": true,           // Optional > If true → WRITE phase must also update a summary log.
  "expiration_policy": "short-lived",// Optional > Describes eviction tempo: one-prompt | short-lived | long-lived.
  "linkedDomains": ["client", "server"], // Optional > Other domains that should load this file when active.
  "external": false,                  // Optional > Set true if managed by an external integration.
  "ephemeral": false,                 // Optional > True if file should *never* persist past one prompt.
  "merge_trigger_threshold": 2,       // Conditional > Auto‑merge when buffer grows this many entries.
  "requires_review": false,           // Optional > True → human approval needed before WRITE commits.
  "created": "2025-06-26T00:00:00Z", // Optional > ISO‑8601 timestamp when file first generated.
  "lastModified": "2025-06-26T00:00:00Z", // Optional > Auto‑updated on every WRITE.
  "version": "1.0"                  // Optional > Optional doc‑level semantic version.
} -->
```

### 4.10 Field‑by‑Field Annotation
| Field                         | Required?   | Allowed Values / Format                                                                                  | When to Use                       | Behaviour & Notes                                                                 |
| ----------------------------- | ----------- | -------------------------------------------------------------------------------------------------------- | --------------------------------- | --------------------------------------------------------------------------------- |
| **fileType**                  | **Yes**     | permanent · immutable · rolling · append-only · temporary · counter · evictable · protected · structural | **Always**                        | Primary behavioural switch. Drives read, write, lifecycle & safeguard logic.      |
| **subtype**                   | No          | buffer · checkpointed · domain\_spec · …                                                                 | When extra nuance needed          | Narrows behaviour within `fileType`; validator checks it matches allowed aliases. |
| **routeScope**                | No          | client · server · schema · global                                                                        | Domain‑aware loading              | Guides domain counters & selective READ plans.                                    |
| **ownedBy**                   | No          | Path to counter file                                                                                     | Hierarchical ownership            | Lets the AI locate the counter that increments for this file.                     |
| **purpose**                   | **Yes**     | Free‑text sentence                                                                                       | Always                            | Human‑readable rationale; appears in audits.                                      |
| **editPolicy**                | **Yes**     | readonly · appendOnly · overwrite · appendOrReplace                                                      | Always                            | Defines what WRITE ops are legal.                                                 |
| **maxEntries**                | Conditional | Integer ≥ 1                                                                                              | Only for rolling buffers          | Cap before eviction logic runs.                                                   |
| **evictionPolicy**            | Conditional | FIFO · LRU · archive                                                                                     | Rolling / evictable               | Strategy when `maxEntries` reached or TTL expires.                                |
| **ttlCycles**                 | Conditional | Integer ≥1                                                                                               | temporary / evictable             | Auto‑delete after N lifecycle increments.                                         |
| **refreshInterval**           | No          | Integer ≥1                                                                                               | Any frequently changing file      | Forces READ reload even if counters below threshold.                              |
| **readPriority**              | No          | high · medium · low                                                                                      | Token‑budget triage               | Low‑priority files are dropped first if context window tight.                     |
| **requires\_hash\_check**     | No          | true · false                                                                                             | protected / immutable / high‑risk | Enforces pre/post SHA‑256 validation.                                             |
| **archive\_on\_write**        | No          | true · false                                                                                             | Historical trace needed           | Copies previous revision to `/_archive/` before overwrite.                        |
| **mergeable**                 | No          | true · false                                                                                             | Docs meant to fold into others    | Enables auto‑merge routines in WRITE phase.                                       |
| **merge\_target**             | Conditional | Path                                                                                                     | When `mergeable: true`            | Default file to receive merged content.                                           |
| **merge\_policy**             | Conditional | append · squash · integrate                                                                              | With `mergeable`                  | How merge is performed.                                                           |
| **write\_protected**          | No          | true · false                                                                                             | Critical docs                     | Blocks WRITE unless user/AI lifts gate.                                           |
| **requires\_summary**         | No          | true · false                                                                                             | Log‑heavy domains                 | Forces AI to write/update `summary.md` after changes.                             |
| **expiration\_policy**        | Conditional | one‑prompt · short‑lived · long‑lived                                                                    | temp / buffer                     | Human‑readable eviction hint; complements `ttlCycles`.                            |
| **linkedDomains**             | No          | Array                                                                                                    | Cross‑domain helpers              | Ensures file loads when any linked domain active.                                 |
| **external**                  | No          | true · false                                                                                             | CI/CD, ticket systems             | Marks file managed outside the cascade.                                           |
| **ephemeral**                 | No          | true · false                                                                                             | Task buffers                      | Guarantees deletion post‑WRITE.                                                   |
| **merge\_trigger\_threshold** | Conditional | Integer ≥1                                                                                               | rolling + mergeable               | Auto‑merge after N new entries.                                                   |
| **requires\_review**          | No          | true · false                                                                                             | Sensitive changes                 | Prompts human approval before WRITE.                                              |
| **created**                   | Recommended | ISO‑8601 timestamp                                                                                       | Once                              | Fixed point of origin; not edited after creation.                                 |
| **lastModified**              | Recommended | ISO‑8601 timestamp                                                                                       | Auto                              | Updated after each successful WRITE.                                              |
| **version**                   | No          | SemVer string                                                                                            | Docs in versioned workflows       | Handy for immutable doctrine or schema files.                                     |

    Usage Tips
1. **Keep it minimal.** Most files only need 3‑5 keys (`fileType`, `purpose`, `editPolicy`, plus any lifecycle‑driver like `maxEntries`).
2. **Validator friendly.** Stay within allowed enumerations—unknown keys trigger lint errors.
3. **Readability matters.** Even though the block is machine‑parsed, humans will read it during audits.
4. **Immutable ≠ write\_protected.** Immutable files omit `editPolicy` and simply use `fileType: immutable` with `editPolicy: readonly`.
5. **Timestamps** should be in **UTC ISO‑8601** to avoid timezone drift across collaborators.
     **Remember:** This superset block is **illustrative**; prune unused keys when instantiating real files to keep headers concise and token‑lean.


## 5 ContextCascade Core Files Bootstrap Pack

### 5.1 /cascade/00_BOOTSTRAP.md
<!-- @meta {
  "fileType": "immutable",
  "purpose": "Bootstrap file enforcing protocol startup, scope discipline, and memory system entry constraints.",
  "editPolicy": "readonly"
} -->
# ContextCascade Bootstrap Guide
Welcome. This file is the required entrypoint for using the ContextCascade memory system. Before any task, you must:

## Mandatory Protocol (Follow Exactly)
- Read `/cascade/index.md` (map)
- Read `/cascade/protocols/loop_protocol.md` (loop rules)
- Respect all `@meta` blocks
- Check `/cascade/protocols/file_lifespans.md` and any `/cascade/lifecycle/*.md` counters
- Do not ACT or WRITE until READ phase is fully complete
- Never edit `<!-- PROTECTED -->` sections
- If any `immutable` file fails hash check → halt, log to `/audit/meta_audit.md`, skip WRITE

---
## Scope Rules (Memory vs. App)
- ContextCascade only stores memory, plans, counters, protocols, and logs
- Do not write `.md` files in Cascade that describe or duplicate app logic
- All application code or assets belong in the app repo, outside `/cascade/`
- Only create `.md` files here if storing durable reasoning or system governance

---
## Summary
If it’s not memory, constraint, protocol, or trace —
→ it doesn’t belong in Cascade.

Proceed to `/cascade/index.md`.

### 5.2 /cascade/index.md
<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Master index and routing map for all Cascade memory domains and protocol infrastructure.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Cascade Index Map

| Path | Role |
|------|------|
| `/cascade/00_BOOTSTRAP.md` | System entrypoint (immutable) |
| `/cascade/protocols/loop_protocol.md` | READ → ACT → WRITE enforcement |
| `/cascade/protocols/file_lifespans.md` | Refresh thresholds (by domain) |
| `/cascade/change_log/recent.md` | Rolling buffer (max 7) |
| `/cascade/change_log/summary.md` | Permanent history ledger |
| `/cascade/lifecycle/counter.md` | Tick counter (global WRITE count) |
| `/cascade/lifecycle/*.md` | Domain write counters |
| `/cascade/load_plans/` | AI‑generated read plans (evictable) |
| `/cascade/job_logs/temp_job.md` | Temporary WRITE plan (1‑cycle TTL) |

---
## Notes
- This index is editable; append rows as domains expand.
- Reference only files that comply with `@meta` and loop discipline.
- `/cascade/` is structured memory; do not store application logic here.

### 5.3 /cascade/system_manifest.md
<!-- @meta {
  "fileType": "manifest",
  "purpose": "Declarative list of active Cascade memory domains and their root paths.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
# ContextCascade System Manifest

| Domain | Root Path | Purpose |
|--------|-----------|---------|
| core | `/cascade/` | Protocols, logs, counters, global memory |
| client | `/cascade/client/` | Client‑specific memory (optional) |
| server | `/cascade/server/` | Server‑side memory (optional) |
| schema | `/cascade/schema/` | Schema and validation rules |
| load_plans | `/cascade/load_plans/` | Evictable AI read plans |
| job_logs | `/cascade/job_logs/` | Temporary job state (TTL 1 cycle) |
| lifecycle | `/cascade/lifecycle/` | Domain counters (refresh triggers) |
| audit | `/cascade/audit/` | Integrity and hash audit logs (optional) |

---
## Notes
- Keep rows alphabetised for quick diff checks.
- Append a new row only after the corresponding domain directory exists.
- Manifest lists memory domains only; do not reference application repositories.

### 5.4 /cascade/init\_context.md
<!-- @meta {
  "fileType": "initialization",
  "purpose": "Declarative context primer for the first READ cycle of a new session.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Initial Context Primer
This file captures static boot context — background assumptions, goals, or persistent framing that should be injected prior to the first ACT phase.

---
## Context Markers
- System: ContextCascade Memory Layer
- Mode: Planning + memory manipulation only
- Scope: Memory protocols, counters, plans, traces
- App logic: Excluded (resides outside `/cascade/`)

---
## Standing Assumptions
- This AI agent operates within the READ → ACT → WRITE loop
- No WRITE occurs without complete READ
- Counters and TTL must be respected before reuse

---
## Usage
- Read this file during session startup if load_plan is absent or empty
- Do not modify from within ACT phase
- Update only when system-wide framing shifts

### 5.5 /cascade/protocols.md
<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Registry of formal protocol definition files.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Protocols Registry

| Protocol File | Role |
|---------------|------|
| `/cascade/protocols/loop_protocol.md` | Core READ → ACT → WRITE loop |
| `/cascade/protocols/file_lifespans.md` | Lifecycle refresh thresholds |

---
## Guidelines
- List protocol definition files only; exclude plans, logs, or counters.
- Keep rows alphabetised for diff‑friendly updates.
- Append a new row immediately after a protocol file is added to `/cascade/protocols/`.

### 5.5.1 /cascade/protocols/loop_protocol.md
<!-- @meta {
  "fileType": "protected",
  "purpose": "Defines the structured execution loop used by ContextCascade: READ → ACT → WRITE.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
#### Loop Protocol
<!-- PROTECTED -->
#### Three-Phase Execution Loop
This protocol enforces strict sequencing of AI task execution into three non-overlapping phases.
##### Phase 1 — READ
- Load context files as defined in the **active load plan** generated during the previous ACT.
- Perform no mutation or job logic.
- Validate hashes for all `immutable` or `protected` files.
##### Phase 2 — ACT
- Perform reasoning and generate a **job plan** (`temp_job.md`) plus an updated load plan (if needed).
- Create no file writes.
##### Phase 3 — WRITE
- **Pre-WRITE hash check**: verify immutable/protected files still match `integrity_snapshot.md`.
- Execute the job plan and mutate only allowed files.
- Recompute hashes and confirm against `expectedHashAfter`.
- Log deltas to `/cascade/change_log/` and increment lifecycle counters.
- Abort and enter Safe-Hold if any safeguard fails.
<!-- END PROTECTED -->
---
#### Loop Entry / Exit
- **Entry**: Allowed only when no `drift_flag.md` exists.
- **Exit**: Occurs after a successful WRITE and delta audit.
#### Safe-Hold Triggers
- Hash or safeguard failure
- Stale or conflicting `_locks/active_edit.lock`
- Missing / malformed `temp_job.md`
#### Audit Expectations
- Each phase transition must be traceable by job ID.
- Counters must increment exactly once per WRITE.
#### Maintenance Guidance
- Never modify PROTECTED sections except via security-reviewed job plans.

### 5.5.2 /cascade/protocols/file_lifespans.md
<!-- @meta {
  "fileType": "policy",
  "subtype": "thresholdPolicy",
  "purpose": "Defines counter thresholds that trigger rereads, pruning, or summary merges for each lifecycle scope.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
#### File Lifespan Thresholds
Thresholds below are evaluated during **Phase 2 – ACT**. When a lifecycle counter meets or exceeds a threshold, the corresponding action is queued for the next loop.
| Domain Scope | `reread_threshold` | `prune_threshold` | `merge_threshold` |
|--------------|--------------------|-------------------|-------------------|
| global (`counter.md`) | 5 | 7 | 10 |
| client (`client.md`)  | 3 | 5 | 8 |
| server (`server.md`)  | 3 | 5 | 8 |
| schema (`schema.md`)  | 4 | 6 | 9 |
| security (`security.md`) | 2 | 4 | 6 |
---
##### Threshold Meaning
- **`reread_threshold`** → Force a context reload for the domain on next READ.
- **`prune_threshold`** → Schedule deletion or archival of expired temp / rolling files.
- **`merge_threshold`** → Consolidate rolling buffers into durable summaries (e.g. `summary.md`).
---
##### Rationale (Lean)
- *Global* counters change most often → slightly larger window.
- *Client / Server* domains typically change more rapidly → tighter windows.
- *Schema* updates are less frequent but critical → moderate thresholds.
- *Security* events require aggressive maintenance to keep audit noise low.
---
##### Maintenance Guidance
- Update thresholds only via a reviewed job plan.
- Add a new row when introducing a new domain counter.
- Keep table alphabetised for diff‑friendly PRs.

### 5.5.3 /cascade/protocols/safeguards.md
<!-- @meta {
  "fileType": "policy",
  "subtype": "safeguardsPolicy",
  "purpose": "Comprehensive enforcement rules for hash integrity, protected blocks, write-gates, and recovery triggers.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
#### Protocol Safeguards Policy
This policy centralises **all mandatory protections** that preserve the integrity, auditability, and governance of the ContextCascade memory layer.
---
##### 1. Enforcement Matrix
| # | Safeguard | Trigger Condition | Automatic Response |
|---|-----------|------------------|--------------------|
| 1 | **Immutable Hash Check** | Hash mismatch detected in any `fileType: immutable` file during pre‑ or post‑WRITE | • Abort WRITE<br>• Log `hashMismatch` in `/audit/meta_audit.md`<br>• Raise `/lifecycle/drift_flag.md` |
| 2 | **Protected Block Enforcement** | Attempted edit overlaps a `<!-- PROTECTED -->` span | • Abort WRITE<br>• Log `protectedOverlap`<br>• Require security review if `escalation: true` |
| 3 | **Write Gate Validation** | Target path not allowed by `/security/write_gates.md` | • Abort WRITE<br>• Log `gateViolation` |
| 4 | **Active Edit Lock** | `_locks/active_edit.lock` present at READ or WRITE start | • Halt loop in safe‑hold<br>• Prompt manual unlock if stale |
| 5 | **Pre/Post Hash Workflow** | Hash delta of protected/immutable files differs from plan | • Roll back WRITE<br>• Log `postHashMismatch`<br>• Flag drift |
| 6 | **High‑Risk Action Flag** | Job plan contains `requiresReview: true` or touches critical files (e.g. `system_manifest.md`) | • Suspend WRITE until review approved<br>• Record event in `security_review.md` |
---
##### 2. Metadata Quick‑Reference
| Marker | Effect |
|--------|--------|
| `fileType: immutable` | Seals file content; requires hash verification every loop |
| `editPolicy: readonly` | Disables all writes (immutable by intent) |
| `protected: true` | Marks inline block as untouchable, even if file is editable |
| `ttlCycles: N` | Governs expiry of temporary / evictable files |
| `requiresReview: true` | Forces human / elevated agent approval before WRITE |
---
##### 3. Hash Verification Workflow
1. **Pre‑WRITE**
   - Compute SHA‑256 for every file tagged `immutable` **or** containing a protected block.
   - Compare against `audit/integrity_snapshot.md`.
   - On any mismatch → **abort** and raise `hashMismatch`.
2. **Post‑WRITE**
   - Re‑hash the same set plus any files actually written.
   - Validate against `expectedHashAfter` in `/cascade/job_logs/temp_job.md`.
   - On success → append entry to `/cascade/change_log/recent.md`.
   - On failure → roll back write, set `drift_flag.md`.
---
##### 4. Protected Block Syntax
```md
<!-- PROTECTED -->
... uneditable content ...
<!-- END PROTECTED -->
```
- **Nested blocks** are not allowed.
- Attempting to insert, delete, or reorder text inside a protected span constitutes a `protectedOverlap` violation.
---
##### 5. Recovery & Escalation Paths
- **Safe‑Hold Mode**: Activated on any safeguard breach to prevent cascading corruption.
- **Loop Recovery**: Instructions in `/cascade/protocols/recovery.md` outline how to resume after drift resolution.
- **Security Review**: High‑risk or failed safeguards require a signed entry in `/cascade/security/security_review.md`.
- **Immutable Restore**: Use snapshots listed in `audit/integrity_snapshot.md` to roll back mutated files.
---
##### 6. Maintenance Guidance
- Update this file **only** through an approved security review.
- Keep safeguard IDs in the enforcement matrix **stable** for audit tooling.
- Align new safeguards with counters and thresholds defined in `file_lifespans.md`.

### 5.5.4 /cascade/protocols/recovery.md
```markdown
<!-- @meta {
  "fileType": "protocol",
  "subtype": "recoveryPlan",
  "purpose": "Structured fallback procedure activated on safeguard failure, drift, or aborted WRITE.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
#### Recovery Protocol
When the normal READ → ACT → WRITE loop is interrupted, this protocol restores the cascade to a verified state without losing auditability.
---
##### 1 · Automatic Triggers
| Condition | Trigger File / Signal |
|-----------|-----------------------|
| Drift detected | `/lifecycle/drift_flag.md` present |
| WRITE aborted | Safeguard log entry in `/audit/meta_audit.md` |
| Stale edit lock | `_locks/active_edit.lock` older than 10 min |
| Plan corruption | Missing / malformed `job_logs/temp_job.md` |
> Any trigger forces **Safe‑Hold mode**: no further WRITE until recovery completes.
---
##### 2 · Recovery Pipeline
###### Phase A — Diagnose
1. **Freeze WRITE**: create or confirm `_locks/active_edit.lock`.
2. Parse `/audit/meta_audit.md` for the latest failure record.
3. Re‑hash all immutable & protected files → compare to `integrity_snapshot.md`.
4. Inspect `temp_job.md` for structural validity.
###### Phase B — Contain
1. Move suspect files to `/quarantine/YYYY‑MM‑DD/` (retain full path).
2. Ensure `/lifecycle/drift_flag.md` contains a one‑line cause summary.
3. Append all actions to `/audit/meta_audit.md` with tag `recovery-start`.
###### Phase C — Restore
1. Copy pristine versions from `integrity_snapshot.md` into place.
2. Rebuild **minimal load plan** (`load_plans/auto_plan_recovery.md`) that lists only:
   - `00_BOOTSTRAP.md`
   - `index.md`
   - `system_manifest.md`
   - Fixed immutable files.
3. Run a full pre‑hash check → abort if any mismatch remains.
###### Phase D — Resync
1. Delete stale `_locks/active_edit.lock`.
2. Remove `/lifecycle/drift_flag.md`.
3. Create checkpoint `recovery‑⟨N⟩` in `/checkpoints/loop_checkpoint.md`.
###### Phase E — Resume
1. Load the recovery plan → enter READ phase.
2. Proceed to ACT only after a clean hash verification.
---
##### 3 · Manual Oversight
- Steps **B** and **C** must be confirmed by a human or elevated agent.
- Log each manual action in `/security/security_review.md` with tag `recovery`.
---
##### 4 · Emergency Halt (Last Resort)
1. Rename `/cascade/` → `/cascade_stale_⟨timestamp⟩/`.
2. Re‑bootstrap from seed pack (`00_BOOTSTRAP`, manifest, protocols).
3. Manually migrate only audited summaries.
4. File a post‑mortem entry in `/audit/meta_audit.md` tagged `postmortem`.
---
##### 5 · Post‑Recovery Artefacts
| File | Required Update |
|------|-----------------|
| `/audit/meta_audit.md` | `recovery-complete` record with hash list |
| `/change_log/recent.md` | Summary delta appended |
| `/checkpoints/loop_checkpoint.md` | New row `recovery‑⟨N⟩` |
| `/quarantine/` | Retain ≥ 30 days unless security clears |
---
##### 6 · Prevention Checklist
- Validate `temp_job.md` pre‑WRITE.
- Monitor lifecycle counters; investigate irregular jumps or stalls.
- Schedule periodic **read‑only loop audits** to pre‑empt silent drift.
```markdown
<!-- @meta {
  "fileType": "protocol",
  "subtype": "recoveryPlan",
  "purpose": "Structured fallback procedure triggered by safeguard failure, drift, or WRITE abortion.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
#### Recovery Protocol
This file governs how the system recovers when the loop fails due to safeguard violations, hash mismatches, or unresolved drift.
---
##### 1. Automatic Triggers
- Presence of `/lifecycle/drift_flag.md`
- WRITE aborted during `loop_protocol.md`
- Stale `_locks/active_edit.lock` preventing job completion
- Corrupted or missing `temp_job.md`
---
##### 2. Recovery Phases
###### Phase A — Diagnose
1. Halt all WRITE operations
2. Review `/audit/meta_audit.md` for safeguard or hash breach
3. Validate `audit/integrity_snapshot.md` against current file states
4. Verify `temp_job.md` plan integrity
###### Phase B — Contain & Flag
1. Move unstable or suspect files to `/quarantine/YYYY-MM-DD/`
2. If not already present, create `/lifecycle/drift_flag.md` with cause summary
3. Document all actions in `/audit/meta_audit.md`
###### Phase C — Restore
1. Use `integrity_snapshot.md` to replace corrupted `immutable` or `protected` files
2. Generate a minimal load plan referencing only core files (BOOTSTRAP, INDEX, MANIFEST)
3. Clear `drift_flag.md` only after successful plan load and hash check
---
##### 3. Manual Interventions
- Restoration steps require elevated agent or human confirmation
- Log each override in `/security/security_review.md` tagged `recovery`
---
##### 4. Emergency Halt
If integrity cannot be restored:
1. Archive `/cascade/` ➜ `/cascade_stale_YYYYMMDD/`
2. Rebootstrap using seed files
3. Transfer only audited summaries or logs
4. Log postmortem to `/audit/meta_audit.md` with `postmortem` tag
---
##### 5. Post-Recovery Actions
| File | Expected Update |
|------|------------------|
| `/audit/meta_audit.md` | Recovery event logged |
| `/change_log/recent.md` | Deltas appended |
| `/checkpoints/loop_checkpoint.md` | New checkpoint tagged `recovery-N` |
| `/lifecycle/drift_flag.md` | Deleted or archived |
| `/quarantine/` | Retain for 30 days minimum |
---
##### 6. Prevention Notes
- Validate `temp_job.md` for each cycle
- Monitor lifecycle counters for drift or stalling
- Run a dry loop audit (`read-only mode`) periodically

### 5.6 /cascade/lifecycle.md
<!-- @meta {
  "fileType": "policy",
  "subtype": "lifecycleIndex",
  "purpose": "Indexes all domain lifecycle counters and drives hygiene triggers (reread / prune / merge).",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
> Central registry for `lifecycle/*.md` counter files.
> Counters are incremented during **WRITE**, inspected during **ACT**, and compared to thresholds in `/protocols/file_lifespans.md`.
---
#### Registered Counters
| Counter File | Domain | What It Tracks                       |
|--------------|--------|--------------------------------------|
| `counter.md` | global | All WRITE cycles                     |
| `client.md`  | client | UI / frontend edits                  |
| `server.md`  | server | Backend / API edits                  |
| `schema.md`  | schema | Contract & validation changes        |
| `security.md`| security| High-risk actions & audit events    |
| `drift_flag.md` | system | Unresolved lifecycle contradictions |
---
#### Trigger Logic
- **WRITE phase** → increment relevant counter once per loop.
- **ACT phase** → compare ticks to `reread / prune / merge` thresholds.
- **Queued actions** → `force_reread`, `schedule_prune`, `schedule_merge`.
- **Drift** → if actions are skipped, update `/lifecycle/drift_flag.md` and log in `/audit/meta_audit.md`.
---
#### Maintenance
- Do **not** edit tick values by hand.
- Add new counters only via reviewed job plan; update this table & `file_lifespans.md`.
- Keep rows alphabetised.
---
#### Example Counter File Metadata
<!-- @meta {
  "fileType": "counter",
  "purpose": "Tracks WRITE-phase activity for the client domain.",
  "editPolicy": "incrementOnly",
  "routeScope": "client"
} -->

### 5.6 /cascade/change_log.md
<!-- @meta {
  "fileType": "policy",
  "subtype": "index",
  "purpose": "Manifest for change-log buffers; governs rolling retention (recent.md) and archival persistence (summary.md).",
  "editPolicy": "appendOrReplace",
  "routeScope": "global",
  "mergeTarget": "change_log/summary.md",
  "maxEntries": 7
} -->
### /cascade/change_log.md
> **Role:** Describes how the cascade records recent WRITE-phase activity while preserving a permanent audit trail. It links two sibling buffers:
> * **`recent.md`** – short-window rolling log (token-lean)
> * **`summary.md`** – permanent append-only archive
---
#### Active Buffers
| File          | Class    | Retention        | Notes                                   |
|---------------|----------|------------------|-----------------------------------------|
| `recent.md`   | rolling  | last **7** loops | Evicts FIFO; entries merged to archive  |
| `summary.md`  | archive  | infinite         | Append-only; never overwritten          |
---
#### Buffer Rules
**Recent Buffer (`recent.md`)**
- `maxEntries`: **7** (also declared in metadata above)
- Overflow behaviour: oldest row copied to `summary.md`, then removed here.
- Edit policy: **appendOnly** (system-enforced)
**Archive (`summary.md`)**
- Unlimited length; append-only ledger.
- Accepts flushed rows from `recent.md` in chronological order.
- Validated for monotonic timestamps during merge.
---
#### Merge Triggers
- Automatic when `recent.md` reaches `maxEntries`.
- Manual when a job plan sets `forceMerge: true`.
- Policy-driven when a domain hits `merge_threshold` in `/protocols/file_lifespans.md`.
---
#### Enforcement Pathway
READ → ACT(plan_refresh_phase) → WRITE(handle_merge_phase)
│ │
└─ if merge required ──────────────┘
- Merge outcomes logged to `/audit/meta_audit.md`.
- Failure to flush after 1 loop raises `/lifecycle/drift_flag.md`.
---
#### Maintenance Guidance
- **Do not** edit existing rows; only appends allowed.
- Keep timestamps in **ISO-8601 UTC** for validator compatibility.
- Bulk migrations to external storage must update this manifest.
---
#### Summary
This manifest keeps the change-log pipeline healthy: a small, token-efficient window for day-to-day debugging and an immutable archive for deep forensic or compliance review. Maintain `maxEntries` conservatively to balance visibility against token budget.

### 5.6 /cascade/change_log.md
<!-- @meta {
  "fileType": "policy",
  "subtype": "index",
  "purpose": "Manifest for job-log buffers; governs retention of recent job plans and their archival into a permanent ledger.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global",
  "mergeTarget": "job_logs/summary.md",
  "maxEntries": 5
} -->
### /cascade/job_logs.md
> **Role:** Tracks every WRITE-phase job plan.
> * **`recent.md`** – rolling buffer (last 5 jobs).
> * **`summary.md`** – infinite, append-only archive.
---
#### Active Buffers
| File            | Class    | Retention (loops) | Notes                                  |
|-----------------|----------|-------------------|----------------------------------------|
| `recent.md`     | rolling  | **5**             | FIFO; overflows merge into archive     |
| `summary.md`    | archive  | ∞ (append-only)   | Permanent ledger of all executed jobs  |
---
#### Buffer Rules
**`recent.md`**
- `maxEntries`: **5** (also set in metadata).
- Overflow: oldest row copied to `summary.md`, then evicted.
- Edit policy: `appendOnly`; system controls eviction.
**`summary.md`**
- Append-only, chronological order.
- Accepts rows flushed from `recent.md`.
- Validator enforces monotonic timestamps + unique `jobId`.
---
#### Merge Triggers
1. `recent.md` exceeds **5** entries.
2. Job plan sets `forceMerge: true`.
3. Domain hits `merge_threshold` (see `/protocols/file_lifespans.md`).
---
#### Enforcement Flow
"""

    REPO_FILES["package.json"] = """{
  "name": "contextcascade",
  "version": "1.0.0",
  "description": "Utilities for the ContextCascade memory system",
  "scripts": {
    "validate": "ts-node cascade/validators/metadata_validator.ts"
  },
  "devDependencies": {
    "ts-node": "^10.0.0",
    "typescript": "^4.0.0"
  }
}
"""
    REPO_FILES["cascade/00_BOOTSTRAP.md"] = """<!-- @meta {
  "fileType": "immutable",
  "purpose": "Bootstrap file enforcing protocol startup, scope discipline, and memory system entry constraints.",
  "editPolicy": "readonly"
} -->
# ContextCascade Bootstrap Guide
Welcome. This file is the required entrypoint for using the ContextCascade memory system. Before any task, you must:

## Mandatory Protocol (Follow Exactly)
- Read `/cascade/index.md` (map)
- Read `/cascade/protocols/loop_protocol.md` (loop rules)
- Respect all `@meta` blocks
- Check `/cascade/protocols/file_lifespans.md` and any `/cascade/lifecycle/*.md` counters
- Do not ACT or WRITE until READ phase is fully complete
- Never edit `<!-- PROTECTED -->` sections
- If any `immutable` file fails hash check → halt, log to `/audit/meta_audit.md`, skip WRITE

---
## Scope Rules (Memory vs. App)
- ContextCascade only stores memory, plans, counters, protocols, and logs
- Do not write `.md` files in Cascade that describe or duplicate app logic
- All application code or assets belong in the app repo, outside `/cascade/`
- Only create `.md` files here if storing durable reasoning or system governance

---
## Summary
If it’s not memory, constraint, protocol, or trace —
→ it doesn’t belong in Cascade.

Proceed to `/cascade/index.md`.
"""

    REPO_FILES["cascade/index.md"] = """<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Master index and routing map for all Cascade memory domains and protocol infrastructure.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Cascade Index Map

| Path | Role |
|------|------|
| `/cascade/00_BOOTSTRAP.md` | System entrypoint (immutable) |
| `/cascade/protocols/loop_protocol.md` | READ → ACT → WRITE enforcement |
| `/cascade/protocols/file_lifespans.md` | Refresh thresholds (by domain) |
| `/cascade/change_log/recent.md` | Rolling buffer (max 7) |
| `/cascade/change_log/summary.md` | Permanent history ledger |
| `/cascade/lifecycle/global.md` | Tick counter (global WRITE count) |
| `/cascade/lifecycle/*.md` | Domain write counters |
| `/cascade/load_plans/` | AI‑generated read plans (evictable) |
| `/cascade/job_logs/temp_job.md` | Temporary WRITE plan (1‑cycle TTL) |

---
## Notes
- This index is editable; append rows as domains expand.
- Reference only files that comply with `@meta` and loop discipline.
- `/cascade/` is structured memory; do not store application logic here.
"""

    REPO_FILES["cascade/system_manifest.md"] = """<!-- @meta {
  "fileType": "immutable",
  "purpose": "Declarative list of active Cascade memory domains and their root paths.",
  "editPolicy": "readonly",
  "routeScope": "global"
} -->
# ContextCascade System Manifest

| Domain | Root Path | Purpose |
|--------|-----------|---------|
| core | `/cascade/` | Protocols, logs, counters, global memory |
| client | `/cascade/client/` | Client‑specific memory (optional) |
| server | `/cascade/server/` | Server‑side memory (optional) |
| schema | `/cascade/schema/` | Schema and validation rules |
| load_plans | `/cascade/load_plans/` | Evictable AI read plans |
| job_logs | `/cascade/job_logs/` | Temporary job state (TTL 1 cycle) |
| lifecycle | `/cascade/lifecycle/` | Domain counters (refresh triggers) |
| audit | `/cascade/audit/` | Integrity and hash audit logs (optional) |

---
## Notes
- Keep rows alphabetised for quick diff checks.
- Append a new row only after the corresponding domain directory exists.
- Manifest lists memory domains only; do not reference application repositories.
"""

    REPO_FILES["cascade/init_context.md"] = """<!-- @meta {
  "fileType": "immutable",
  "purpose": "Declarative context primer for the first READ cycle of a new session.",
  "editPolicy": "readonly",
  "routeScope": "global"
} -->
# Initial Context Primer
This file captures static boot context — background assumptions, goals, or persistent framing that should be injected prior to the first ACT phase.

---
## Context Markers
- System: ContextCascade Memory Layer
- Mode: Planning + memory manipulation only
- Scope: Memory protocols, counters, plans, traces
- App logic: Excluded (resides outside `/cascade/`)

---
## Standing Assumptions
- This AI agent operates within the READ → ACT → WRITE loop
- No WRITE occurs without complete READ
- Counters and TTL must be respected before reuse

---
## Usage
- Read this file during session startup if load_plan is absent or empty
- Do not modify from within ACT phase
- Update only when system-wide framing shifts
"""

    REPO_FILES["cascade/protocols.md"] = """<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Registry of formal protocol definition files.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Protocols Registry

| Protocol File | Role |
|---------------|------|
| `/cascade/protocols/loop_protocol.md` | Core READ → ACT → WRITE loop |
| `/cascade/protocols/file_lifespans.md` | Lifecycle refresh thresholds |

---
## Guidelines
- List protocol definition files only; exclude plans, logs, or counters.
- Keep rows alphabetised for diff‑friendly updates.
- Append a new row immediately after a protocol file is added to `/cascade/protocols/`.
"""

    REPO_FILES["cascade/lifecycle.md"] = """<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Indexes all domain lifecycle counters and drives hygiene triggers (reread / prune / merge).",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
> Central registry for `lifecycle/*.md` counter files.
> Counters are incremented during **WRITE**, inspected during **ACT**, and compared to thresholds in `/protocols/file_lifespans.md`.
---
#### Registered Counters
| Counter File | Domain | What It Tracks                       |
|--------------|--------|--------------------------------------|
| `counter.md` | global | All WRITE cycles                     |
| `client.md`  | client | UI / frontend edits                  |
| `server.md`  | server | Backend / API edits                  |
| `schema.md`  | schema | Contract & validation changes        |
| `security.md`| security| High-risk actions & audit events    |
| `drift_flag.md` | system | Unresolved lifecycle contradictions |
---
#### Trigger Logic
- **WRITE phase** → increment relevant counter once per loop.
- **ACT phase** → compare ticks to `reread / prune / merge` thresholds.
- **Queued actions** → `force_reread`, `schedule_prune`, `schedule_merge`.
- **Drift** → if actions are skipped, update `/lifecycle/drift_flag.md` and log in `/audit/meta_audit.md`.
---
#### Maintenance
- Do **not** edit tick values by hand.
- Add new counters only via reviewed job plan; update this table & `file_lifespans.md`.
- Keep rows alphabetised.
---
#### Example Counter File Metadata
<!-- @meta {
  "fileType": "counter",
  "purpose": "Tracks WRITE-phase activity for the client domain.",
  "editPolicy": "incrementOnly",
  "routeScope": "client"
} -->
"""

    REPO_FILES["cascade/change_log.md"] = """<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Manifest for change-log buffers; governs rolling retention (recent.md) and archival persistence (summary.md).",
  "editPolicy": "appendOrReplace",
  "routeScope": "global",
  "mergeTarget": "change_log/summary.md",
  "maxEntries": 7
} -->
### /cascade/change_log.md
> **Role:** Describes how the cascade records recent WRITE-phase activity while preserving a permanent audit trail. It links two sibling buffers:
> * **`recent.md`** – short-window rolling log (token-lean)
> * **`summary.md`** – permanent append-only archive
---
#### Active Buffers
| File          | Class    | Retention        | Notes                                   |
|---------------|----------|------------------|-----------------------------------------|
| `recent.md`   | rolling  | last **7** loops | Evicts FIFO; entries merged to archive  |
| `summary.md`  | archive  | infinite         | Append-only; never overwritten          |
---
#### Buffer Rules
**Recent Buffer (`recent.md`)**
- `maxEntries`: **7** (also declared in metadata above)
- Overflow behaviour: oldest row copied to `summary.md`, then removed here.
- Edit policy: **appendOnly** (system-enforced)
**Archive (`summary.md`)**
- Unlimited length; append-only ledger.
- Accepts flushed rows from `recent.md` in chronological order.
- Validated for monotonic timestamps during merge.
---
#### Merge Triggers
- Automatic when `recent.md` reaches `maxEntries`.
- Manual when a job plan sets `forceMerge: true`.
- Policy-driven when a domain hits `merge_threshold` in `/protocols/file_lifespans.md`.
---
#### Enforcement Pathway
READ → ACT(plan_refresh_phase) → WRITE(handle_merge_phase)
│ │
└─ if merge required ──────────────┘
- Merge outcomes logged to `/audit/meta_audit.md`.
- Failure to flush after 1 loop raises `/lifecycle/drift_flag.md`.
---
#### Maintenance Guidance
- **Do not** edit existing rows; only appends allowed.
- Keep timestamps in **ISO-8601 UTC** for validator compatibility.
- Bulk migrations to external storage must update this manifest.
---
#### Summary
This manifest keeps the change-log pipeline healthy: a small, token-efficient window for day-to-day debugging and an immutable archive for deep forensic or compliance review. Maintain `maxEntries` conservatively to balance visibility against token budget.
"""

    REPO_FILES["cascade/job_logs.md"] = """<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Manifest for job-log buffers; governs retention of recent job plans and their archival into a permanent ledger.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global",
  "mergeTarget": "job_logs/summary.md",
  "maxEntries": 5
} -->
### /cascade/job_logs.md
> **Role:** Tracks every WRITE-phase job plan.
> * **`recent.md`** – rolling buffer (last 5 jobs).
> * **`summary.md`** – infinite, append-only archive.
---
#### Active Buffers
| File            | Class    | Retention (loops) | Notes                                  |
|-----------------|----------|-------------------|----------------------------------------|
| `recent.md`     | rolling  | **5**             | FIFO; overflows merge into archive     |
| `summary.md`    | archive  | ∞ (append-only)   | Permanent ledger of all executed jobs  |
---
#### Buffer Rules
**`recent.md`**
- `maxEntries`: **5** (also set in metadata).
- Overflow: oldest row copied to `summary.md`, then evicted.
- Edit policy: `appendOnly`; system controls eviction.
**`summary.md`**
- Append-only, chronological order.
- Accepts rows flushed from `recent.md`.
- Validator enforces monotonic timestamps + unique `jobId`.
---
#### Merge Triggers
1. `recent.md` exceeds **5** entries.
2. Job plan sets `forceMerge: true`.
3. Domain hits `merge_threshold` (see `/protocols/file_lifespans.md`).
---
"""

    REPO_FILES["cascade/_locks/active_edit.lock"] = """<!-- @meta {
  "fileType": "temporary",
  "subtype": "editSession",
  "purpose": "Prevents concurrent WRITE operations by signalling an active edit session.",
  "editPolicy": "replaceOnly",
  "routeScope": "global",
  "ttlCycles": 1,
  "linkedAudits": ["audit/meta_audit.md", "lifecycle/drift_flag.md"]
} -->

### /_locks/active_edit.md

> **Role:** Acts as a mutex for high-integrity WRITE phases.
> If this lock is present and `status` ≠ `cleared`, any new job plan must halt until the lock is released or deemed **stale**.

---

#### Current Lock (state is overwritten every loop)

| Timestamp (UTC)       | Locked By | Scope   | Job ID  | Status       |
|-----------------------|-----------|---------|---------|--------------|
| _none_                | —         | —       | —       | cleared      |

**Status values**

| Value        | Meaning                                                    |
|--------------|------------------------------------------------------------|
| `in-progress`| WRITE or MERGE currently running                           |
| `failed`     | Job aborted; manual review needed before clearing          |
| `stale`      | TTL elapsed without matching Job ID; safe-to-clear flag    |
| `cleared`    | No active lock; safe to initiate new WRITE session         |

---

#### Lock Workflow

1. **WRITE-start** → loop controller writes lock entry (`in-progress`).
2. **WRITE-end**   → controller updates `status: cleared` *or* `failed`.
3. **Next loop**   → if `status` ≠ `cleared`, ACT halts planning, logs issue:
   - `/lifecycle/drift_flag.md` (flag)
   - `/audit/meta_audit.md`  (audit row)

If `status` becomes `stale`, a maintenance job can replace this file with the placeholder **cleared** row above.

---

**Summary**
`active_edit.md` enforces sequential state commits, protecting the cascade from race-condition corruption. Keep it overwrite-only and ensure every WRITE phase ends with a `cleared` status—or a flagged audit trail if problems arise.
"""

    REPO_FILES["cascade/_meta/cascade_feature_index.md"] = """<!-- @meta {
  "fileType": "structural",
  "subtype": "index",
  "purpose": "Master feature catalogue and directory reference for the ContextCascade system. Derived from system documentation.",
  "editPolicy": "appendOrReplace",
  "routeScope": "meta"
} -->
# ContextCascade Feature Index & Catalogue

This document provides a comprehensive index of all first-class features within the ContextCascade system, along with brief descriptions and references to their primary documentation or defining files. It is intended to be a quick reference for understanding the system's capabilities.

---
## Core Features

1.  **Metadata Blocks**
    *   **What**: Structured JSON-in-comment headers at the top of each file defining operational context.
    *   **Why**: Encode attributes like `fileType`, `editPolicy`, `ttlCycles`, `routeScope` for automated behavior.
    *   **Where**: All `.md` files in `/cascade/`. Validated by `validators/metadata_validator.ts`.
    *   **Ref**: Documentation §2.5.1, §4.

2.  **Canonical FileType Registry**
    *   **What**: Formal registry of nine allowed file types (`permanent`, `immutable`, `rolling`, `append-only`, `temporary`, `counter`, `evictable`, `protected`, `structural`) and their aliases.
    *   **Why**: Ensures consistent interpretation of file semantics.
    *   **Where**: Defined in Documentation §3.2.1. Enforced by `validators/metadata_validator.ts`.
    *   **Ref**: Documentation §2.5.2, §3.2.1.

3.  **Read → ACT → WRITE Loop Protocol**
    *   **What**: Disciplined three-phase protocol (Read, Act, Write) for every execution cycle.
    *   **Why**: Ensures clarity, auditability, and safety.
    *   **Where**: Defined in `/cascade/protocols/loop_protocol.md`.
    *   **Ref**: Documentation §2.5.3, `/cascade/protocols/loop_protocol.md`.

4.  **Load Modes (Lean, Domain, Full)**
    *   **What**: Hierarchical strategies for reading context files (`Lean`, `Domain`, `Full`).
    *   **Why**: Balances token budget and contextual completeness.
    *   **Where**: Logic in `protocols/load_mode_logic.md` (conceptual, actual file may vary). Referenced by load plans and lifecycle counters.
    *   **Ref**: Documentation §2.5.4.

5.  **Load Plans**
    *   **What**: Ephemeral markdown files defining the set of files for the next READ phase.
    *   **Why**: Optimizes token use and ensures relevant context ingestion.
    *   **Where**: `/cascade/load_plans/*.md` (e.g., `auto_plan_client.md`).
    *   **Ref**: Documentation §2.5.5.

6.  **Lifecycle Counters**
    *   **What**: `.md` files tracking update activity for specific domains/contexts (e.g., `client_tick.md`).
    *   **Why**: Trigger threshold-based logic (reloads, pruning, drift detection).
    *   **Where**: `/cascade/lifecycle/*.md`. Integrated with `/cascade/protocols/file_lifespans.md`.
    *   **Ref**: Documentation §2.5.6.

7.  **File Lifespan Policies**
    *   **What**: Declarative rules for when files should be reloaded, audited, merged, or deleted.
    *   **Why**: Manages file freshness, memory integrity, prevents token bloat.
    *   **Where**: `/cascade/protocols/file_lifespans.md`.
    *   **Ref**: Documentation §2.5.7.

8.  **Rolling Buffers**
    *   **What**: Files maintaining a fixed number of recent entries (e.g., `change_log/recent.md`).
    *   **Why**: Preserves short-term context efficiently.
    *   **Where**: Metadata `fileType: rolling`, `maxEntries`.
    *   **Ref**: Documentation §2.5.8.

9.  **Append-Only Logs**
    *   **What**: Historical files for events/changes in chronological order (e.g., `change_log/summary.md`).
    *   **Why**: Tamper-evident logs, reliable historical tracing.
    *   **Where**: Metadata `editPolicy: appendOnly`.
    *   **Ref**: Documentation §2.5.9.

10. **Temporary / One-Prompt Files**
    *   **What**: Volatile, single-use files (e.g., `job_logs/temp_job.md`).
    *   **Why**: Transient data, minimizing memory footprint.
    *   **Where**: Metadata `fileType: temporary`, `ttlCycles: 1`. Typically in `_taskbuffers/`.
    *   **Ref**: Documentation §2.5.10.

11. **Evictable Caches**
    *   **What**: Time-sensitive files for intermediate plans or temporary context (e.g., `load_plans/*.md`).
    *   **Why**: Manages token efficiency by offloading short-term reasoning.
    *   **Where**: Metadata `fileType: evictable`, `ttlCycles`.
    *   **Ref**: Documentation §2.5.11.

12. **Domain Routing**
    *   **What**: Metadata-driven scoping (`domain: client`) for files and actions.
    *   **Why**: Isolates context, prevents cross-domain contamination, improves token economy.
    *   **Where**: `system_manifest.md`, domain index files (`domains/*/index.md`), file metadata.
    *   **Ref**: Documentation §2.5.12.

13. **Protected Sections**
    *   **What**: Inline blocks (`<!-- PROTECTED --> ... <!-- END PROTECTED -->`) within editable files that are read-only.
    *   **Why**: Prevents drift in critical logic or assumptions.
    *   **Where**: Core control files like `loop_protocol.md`. Metadata `protected: true` at file level if entire file's sections are protected by this mechanism.
    *   **Ref**: Documentation §2.5.13.

14. **Write Gates**
    *   **What**: Declarative safeguards using glob patterns to control writable files/paths.
    *   **Why**: Protects architectural invariants, prevents rogue writes.
    *   **Where**: `/cascade/security/write_gates.md`.
    *   **Ref**: Documentation §2.5.14.

15. **Immutable Files & Hash Verification**
    *   **What**: Files that cannot be edited post-creation, tracked via cryptographic hashes.
    *   **Why**: Ensures stability of core declarations (doctrine, manifests).
    *   **Where**: Metadata `fileType: immutable`, `editPolicy: readonly`. Hashes in `/cascade/audit/integrity_snapshot.md`.
    *   **Ref**: Documentation §2.5.15.

16. **Integrity Snapshot**
    *   **What**: Canonical ledger of SHA-256 hashes for immutable/protected files.
    *   **Why**: Tamper-evidence seal, guarantees architectural trust.
    *   **Where**: `/cascade/audit/integrity_snapshot.md`.
    *   **Ref**: Documentation §2.5.16.

17. **Active Edit Lock**
    *   **What**: Volatile lockfile (`_locks/active_edit.lock`) signaling in-progress WRITE.
    *   **Why**: Prevents overlapping WRITE operations, ensures serialization.
    *   **Where**: `/cascade/_locks/active_edit.lock`.
    *   **Ref**: Documentation §2.5.17.

18. **Pre- & Post-Hash Checking**
    *   **What**: Dual-phase SHA-256 hash validation before and after WRITE for key files.
    *   **Why**: Detects corruption, unauthorized edits, ensures trustworthy state transitions.
    *   **Where**: Integrated into WRITE lifecycle for `immutable`/`protected` files, checked against `integrity_snapshot.md`.
    *   **Ref**: Documentation §2.5.18.

19. **Job Plans**
    *   **What**: Ephemeral planning artifacts (`job_logs/temp_job.md`) defining intended WRITE actions.
    *   **Why**: Traceability, intentionality, human/system confirmation for changes.
    *   **Where**: `/cascade/job_logs/temp_job.md`.
    *   **Ref**: Documentation §2.5.19.

20. **Write-Back Summary Confirmation**
    *   **What**: Post-WRITE verification where AI re-inspects written files against the job plan.
    *   **Why**: Guarantees WRITE operation succeeded exactly as intended.
    *   **Where**: Outcomes logged in `change_log/recent.md` and `audit/meta_audit.md`.
    *   **Ref**: Documentation §2.5.20.

21. **Summary Merging**
    *   **What**: System for condensing ephemeral files into durable summaries (e.g., `summary.md`).
    *   **Why**: Prevents token saturation, ensures long-term context continuity.
    *   **Where**: Controlled by metadata `mergeable`, `merge_target`, `merge_policy`.
    *   **Ref**: Documentation §2.5.21.

22. **Rolling Update Triggers**
    *   **What**: Lightweight mechanisms to update auxiliary logs/summaries post-WRITE without full replan.
    *   **Why**: Maintains freshness of recent context with minimal overhead.
    *   **Where**: Metadata `rollingUpdate`, `mergeTarget`. Affects files like `change_log/recent.md`.
    *   **Ref**: Documentation §2.5.22.

23. **Eviction Policy & Prune Plan**
    *   **What**: Rules and scripts defining how/when to delete/archive temporary or expired files.
    *   **Why**: Prevents performance degradation, memory bloat, stale context.
    *   **Where**: Master policy in `/cascade/audit/prune_plan.md`. Affects `_taskbuffers/`, `temp_notes/`, etc.
    *   **Ref**: Documentation §2.5.23.

24. **Token Budget Awareness**
    *   **What**: System tracking estimated token footprint of files/branches.
    *   **Why**: Prevents context overrun, enables smarter loading.
    *   **Where**: Tracked in `/cascade/audit/token_summary.md`.
    *   **Ref**: Documentation §2.5.24.

25. **Validator Pipeline**
    *   **What**: Utility (`validators/metadata_validator.ts`) for checking structural, metadata, and schema correctness.
    *   **Why**: Protects from malformed inputs, undefined behaviors.
    *   **Where**: `validators/metadata_validator.ts`. Errors to `meta_audit.md`.
    *   **Ref**: Documentation §2.5.25.

26. **Security Review & High-Risk Action Logging**
    *   **What**: Protocol governing and logging high-risk operations (schema rewrites, critical file mods).
    *   **Why**: Traceability and oversight for sensitive actions.
    *   **Where**: Policy in `security/security_review.md`. Logs in `audit/meta_audit.md`. Job plan flag `requiresReview: true`.
    *   **Ref**: Documentation §2.5.26.

27. **Drift Flag & Meta Audit**
    *   **What**: Mechanism for detecting and recording inconsistencies (`lifecycle/drift_flag.md`) and logging them (`audit/meta_audit.md`).
    *   **Why**: Maintains systemic trust, enables forensic debugging.
    *   **Where**: `/cascade/lifecycle/drift_flag.md`, `/cascade/audit/meta_audit.md`.
    *   **Ref**: Documentation §2.5.27.

28. **Hash Verification Workflow** (Subset of 15, 16, 18)
    *   **What**: 4-step process: Recalc hash → Compare to snapshot → If mismatch → Halt + Log + Flag.
    *   **Why**: Core to preventing architectural corruption.
    *   **Where**: `integrity_snapshot.md`, `immutable` files.
    *   **Ref**: Documentation §2.5.28.

29. **Schema & Snapshot Testing**
    *   **What**: Mechanism to capture structure, schema, metadata state at key milestones for regression testing and rollback.
    *   **Why**: Guards against structural drift in critical definitions.
    *   **Where**: Snapshots in `domains/schema/` or `audit/schema_snapshot.md`.
    *   **Ref**: Documentation §2.5.29.

30. **Extension Patterns (Counters, File Types)**
    *   **What**: Structured protocol for introducing new components (custom counters, file types).
    *   **Why**: Ensures extensibility while maintaining integrity.
    *   **Where**: Definitions in `system_manifest.md`, `metadata_schemas.md` (conceptual).
    *   **Ref**: Documentation §2.5.30.

31. **External Integrations & Hooks**
    *   **What**: Framework for interacting with external tools (CI/CD, ticketing).
    *   **Why**: Bridges cascade planning with real-world systems.
    *   **Where**: Logic in `external/` (conceptual). Metadata `external: true`, `externalHooks`.
    *   **Ref**: Documentation §2.5.31.

32. **Troubleshooting & Recovery Protocols**
    *   **What**: Defined procedures for handling system failures or inconsistencies.
    *   **Why**: Ensures system can be restored to a known good state.
    *   **Where**: `/cascade/protocols/recovery.md`.
    *   **Ref**: Documentation §2.5.32.

33. **Index Map (System + Domain Indexes)**
    *   **What**: Structured index files describing system layout and hierarchy.
    *   **Why**: Enables deterministic boot, accurate routing, memory-aware loading.
    *   **Where**: `/cascade/index.md` (global), `/cascade/domains/*/index.md` (domain-specific).
    *   **Ref**: Documentation §2.5.33.

34. **System Manifest (`system_manifest.md`)**
    *   **What**: Foundational, immutable declaration of system structure, doctrine, routing.
    *   **Why**: Anchor for cascade logic, ensures core invariants.
    *   **Where**: `/cascade/system_manifest.md`.
    *   **Ref**: Documentation §2.5.34.

35. **Loop Checkpoint (`loop_checkpoint.md`)**
    *   **What**: Sequential log recording successful completion of each full cascade loop.
    *   **Why**: Traceability, rollback orchestration, drift detection.
    *   **Where**: `/cascade/checkpoints/loop_checkpoint.md`.
    *   **Ref**: Documentation §2.5.35 (first one).

36. **Bootstrap Protocol (`00_BOOTSTRAP.md`)** (Note: Documentation has this as 2.5.35, but it's also 2.5.36 in a different numbering)
    *   **What**: Mandatory system entrypoint file defining foundational rules and boot preconditions.
    *   **Why**: Ensures sessions start from a clean, validated baseline.
    *   **Where**: `/cascade/00_BOOTSTRAP.md`.
    *   **Ref**: Documentation §1.4, §2.5.36 (or §2.5.35 last one), `/cascade/00_BOOTSTRAP.md`.

---
This index should be kept up-to-date as the ContextCascade system evolves.
It is based on "ContextCascade Developer & User Documentation v1.0".
"""

    REPO_FILES["cascade/_taskbuffers/.gitkeep"] = """"""

    REPO_FILES["cascade/_taskbuffers/scratchpad.md"] = """<!-- @meta {
  "fileType": "temporary",
  "subtype": "temp",
  "purpose": "A temporary scratchpad for single-prompt use. Content does not persist beyond the current cycle.",
  "editPolicy": "overwrite",
  "ttlCycles": 1
} -->
# Scratchpad

This is a temporary buffer for notes, draft content, or intermediate thoughts relevant only to the current prompt or execution cycle.

---
## Usage
- Feel free to write any transient data here during the ACT phase.
- The content of this file is not guaranteed to persist beyond the current READ-ACT-WRITE cycle.
- It will be automatically deleted or cleared after 1 cycle (`ttlCycles: 1`).
- Do not store critical or long-term information here. Use appropriate logs, domain files, or summaries for that.

---
*(Content here is ephemeral and will be overwritten or deleted frequently)*
"""

    REPO_FILES["cascade/audit/integrity_snapshot.md"] = """<!-- @meta {
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
"""

    REPO_FILES["cascade/audit/meta_audit.md"] = """<!-- @meta {
  "fileType": "append-only",
  "purpose": "A persistent log for drift, contradictions, anomalies, safeguard violations, or other significant meta-level system events.",
  "editPolicy": "appendOnly",
  "routeScope": "audit"
} -->
# Meta Audit Log

This file serves as an append-only log for critical system events, particularly those related to inconsistencies, safeguard violations, lifecycle deviations, and recovery actions. It is a key resource for debugging, understanding system behavior, and ensuring traceability.

---
## Logged Events
This log should capture events such as:
- **Drift Detection:**
    - `hashMismatch`: An `immutable` or `protected` file's hash does not match the `integrity_snapshot.md`.
    - `validatorDiff`: Schema or structural differences detected by validators.
    - `unexpectedMutation`: A file was changed without a corresponding job plan.
    - `counterSkip`: A lifecycle counter did not increment as expected.
- **Safeguard Violations:**
    - `protectedOverlap`: Attempted edit within a `<!-- PROTECTED -->` block.
    - `gateViolation`: Write attempt blocked by `/security/write_gates.md`.
    - `lockConflict`: `active_edit.lock` prevented an operation.
    - `immutableWriteAttempt`: Attempt to write to an `immutable` file without proper override.
- **Lifecycle Events:**
    - `recovery-start`: Recovery protocol initiated.
    - `recovery-step`: Specific actions taken during recovery.
    - `recovery-complete`: Recovery protocol finished.
    - `staleFilePruned`: An expired file was removed.
    - `summaryMerge`: Details of a summary merge operation.
- **Security Events:**
    - `securityReviewTriggered`: A high-risk action requiring review was initiated.
    - `permissionEscalation`: An operation required escalated privileges.
- **External Integration Events:**
    - `externalHookSent`: An external hook was triggered.
    - `externalHookFailed`: An external hook failed.

---
## Entry Format
Each entry should be clearly timestamped and structured, potentially using a consistent format (e.g., Markdown list items, YAML blocks, or JSON objects if preferred for machine parsing).

**Example Markdown List Item Format:**
```
---
- **Timestamp:** YYYY-MM-DDTHH:mm:ssZ
  **Type:** `hashMismatch`
  **Severity:** CRITICAL
  **Details:** Hash for `/cascade/system_manifest.md` does not match `integrity_snapshot.md`. Expected: `abc...`, Actual: `def...`.
  **Source:** Pre-WRITE validation (Loop ID: 157)
  **ActionTaken:** WRITE aborted. `/lifecycle/drift_flag.md` raised.
---
- **Timestamp:** YYYY-MM-DDTHH:mm:ssZ
  **Type:** `recovery-start`
  **Severity:** INFO
  **Details:** Recovery protocol initiated due to `drift_flag.md`.
  **Source:** System Recovery Agent
---
```

---
## Current Audit Log:

*(This log is appended to by the system as events occur. No entries yet.)*

---
## Maintenance
- This file is append-only. Existing entries must not be altered.
- Ensure consistent formatting for entries to aid parsing and review.
- Regularly review this log for patterns or recurring issues.
- For very high-volume systems, consider log rotation strategies if file size becomes an issue, though the primary intent is a persistent, complete record.
"""

    REPO_FILES["cascade/audit/prune_plan.md"] = """<!-- @meta {
  "fileType": "evictable",
  "purpose": "Defines and executes controlled cleanup operations for temporary, expired, or unnecessary files.",
  "editPolicy": "overwrite",
  "routeScope": "audit",
  "ttlCycles": 3
} -->
# Prune Plan

This file outlines the policies and can trigger actions for deleting or archiving temporary, expired, or unnecessary files from the ContextCascade system. Its goal is to prevent performance degradation, memory bloat, and stale context leakage.

---
## Pruning Policies & Targets
This section defines what gets pruned and when. Policies are typically based on file metadata like `fileType`, `ttlCycles`, and `expirationPolicy`.

**Common Targets for Pruning:**
- **`temporary` files:** Files in `_taskbuffers/`, `job_logs/temp_job.md` (after `ttlCycles: 1` by default).
- **`evictable` files:** Files in `load_plans/` or other cache-like locations after their `ttlCycles` expire.
- **`rolling` buffers (entries):** Old entries in rolling buffers if not handled by merge logic (though merging is preferred).
- **Stale `active_edit.lock` files:** If `_locks/active_edit.lock` is old and no process is active.
- **Empty directories:** Directories that become empty after pruning.

---
## Pruning Triggers
Pruning can be triggered:
1.  **Automatically:**
    *   At the end of a WRITE cycle, based on `ttlCycles` countdowns.
    *   When lifecycle counters hit `prune_threshold` as defined in `/protocols/file_lifespans.md`.
2.  **Manually/AI-Initiated:**
    *   By an explicit prompt or command (e.g., "Execute prune plan to clear expired files").
    *   As part of a recovery process (`/protocols/recovery.md`).
3.  **Scheduled:** (If the system supports it) As a periodic maintenance task.

---
## Example Prune Plan Execution Script/Instructions (Conceptual)
This section could contain a plan that the AI executes.

```
## Prune Plan - YYYY-MM-DD

**Objective:** Clean up expired and temporary files.

**Phase 1: Identify Candidates**
1. Scan all files with `fileType: temporary`.
   - If `ttlCycles` has reached 0 or is not set (defaults to 1 for temporary), mark for deletion.
2. Scan all files with `fileType: evictable`.
   - If `ttlCycles` has reached 0, mark for deletion.
3. Check `/cascade/_locks/active_edit.lock`:
   - If timestamp older than (e.g., 1 hour) AND no active write process confirmed, mark for deletion.
4. List all files marked for deletion.

**Phase 2: Review (Optional)**
- Present list of files to be pruned to user/AI for confirmation if in interactive mode or if total size > X MB.

**Phase 3: Execute Pruning**
1. For each marked file:
   - If `expirationPolicy: archiveOnExpire` is set, move to `/cascade/_archive/YYYY-MM-DD/` (maintaining path).
   - Else, delete the file.
2. Log all actions (deleted/archived files) to `/cascade/audit/meta_audit.md` with type `staleFilePruned` or `fileArchived`.

**Phase 4: Cleanup**
1. Scan for any empty directories within `/cascade/` (except `_taskbuffers`, `load_plans`, `temp_notes` which might be intentionally empty awaiting new files) and list them for potential removal if policy dictates.

---
```

## Current Prune Plan Status:

*(This file is `evictable` and `overwrite`. It would be generated or updated when a prune operation is planned or executed. Currently idle.)*

**Last Execution:** (Timestamp or N/A)
**Next Scheduled (if applicable):** (Timestamp or N/A)

---
## Instructions for AI:
- To initiate a prune, you can generate a specific execution plan in this file (as per the example above).
- Then, during an ACT phase, reason over this plan and prepare the necessary delete/archive operations for the WRITE phase.
- Always log pruning actions to `/cascade/audit/meta_audit.md`.
- Respect `expirationPolicy` metadata on files. If `archiveOnExpire` is set, move the file instead of deleting.
"""

    REPO_FILES["cascade/audit/token_summary.md"] = """<!-- @meta {
  "fileType": "permanent",
  "purpose": "Tracks estimated and actual token footprints of files and cascade branches to aid in budget awareness.",
  "editPolicy": "appendOrReplace",
  "routeScope": "audit"
} -->
# Token Usage Summary

This file stores data related to the token footprint of files and cascade branches. It helps the AI maintain token budget awareness, make informed decisions during context loading (especially in Lean Mode), and anticipate memory usage.

---
## Structure
This file might contain:
- **Per-file estimates:**
    - File path.
    - Estimated token count (based on heuristics, word count, or previous actuals).
    - Actual token count from the last time it was loaded.
    - Timestamp of the last actual count.
- **Per-domain/branch summaries:**
    - Domain path (e.g., `/cascade/client/`).
    - Total estimated token count for all files in that domain.
    - Total actual token count.
- **Global summary:**
    - Total estimated and actual token counts for the entire cascade.

---
## Example Content:
```
## Global Summary
- Total Estimated Tokens: 15200
- Total Actual Tokens (last full load): 14850
- Last Full Load Timestamp: 2025-07-15T10:00:00Z

---
## Per-Domain Summaries

### /cascade/client/
- Estimated Tokens: 3500
- Actual Tokens: 3320
- Files Tracked: 5

### /cascade/protocols/
- Estimated Tokens: 1200
- Actual Tokens: 1150
- Files Tracked: 4

---
## Per-File Details (Sample)

| File Path                          | Estimated Tokens | Actual Tokens (Last Load) | Last Actual Timestamp  |
|------------------------------------|------------------|---------------------------|------------------------|
| /cascade/00_BOOTSTRAP.md           | 150              | 145                       | 2025-07-15T09:00:00Z   |
| /cascade/index.md                  | 200              | 190                       | 2025-07-15T09:00:00Z   |
| /cascade/domains/client/index.md   | 450              | 430                       | 2025-07-15T09:05:00Z   |
| ...                                | ...              | ...                       | ...                    |

```

---
## Current Token Summary:

*(This section should be populated by an automated process or the AI based on file analysis and loading history.)*

**Last Updated:** (Timestamp)

*(No summary data yet)*

---
## Maintenance
- The AI or an external script should periodically update this file.
- Estimates can be generated via dry-run parsing or using heuristics.
- Actual token counts should be logged after files are loaded into context.
- This file itself can become large; consider strategies for summarization or rotation if it impacts performance.
- `editPolicy: appendOrReplace` allows for the file to be wholly updated by a token counting process.
"""

    REPO_FILES["cascade/change_log/recent.md"] = """<!-- @meta {
  "fileType": "rolling",
  "subtype": "buffer",
  "purpose": "A rolling log of the most recent WRITE cycle summaries, up to a defined maximum.",
  "editPolicy": "appendOnly",
  "routeScope": "global",
  "maxEntries": 7,
  "mergeTarget": "/cascade/change_log/summary.md"
} -->
# Recent Change Log

This file contains a rolling buffer of the most recent successfully completed WRITE cycle summaries. When this log exceeds `maxEntries` (7), the oldest entry is moved to `/cascade/change_log/summary.md`.

---
*(No entries yet)*
"""

    REPO_FILES["cascade/change_log/summary.md"] = """<!-- @meta {
  "fileType": "append-only",
  "purpose": "A permanent, append-only historical log of all WRITE cycle summaries, including those rolled over from recent.md.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Change Log Summary

This file is an append-only historical ledger of all successfully completed WRITE cycles. It includes entries merged from `/cascade/change_log/recent.md` when that buffer reaches its `maxEntries` limit.

---
## Guidelines
- Entries are added chronologically.
- Existing entries must not be modified or deleted.
- Each entry should provide a concise summary of a WRITE cycle, including:
    - Loop ID or timestamp.
    - Job plan reference.
    - Summary of modified files.
    - Outcome status (e.g., success, rolledBack, partial).
    - Post-WRITE hash confirmation status.

---
*(No entries yet)*
"""

    REPO_FILES["cascade/checkpoints/loop_checkpoint.md"] = """<!-- @meta {
  "fileType": "append-only",
  "purpose": "Sequential log recording the successful completion of each full READ-ACT-WRITE cascade loop.",
  "editPolicy": "appendOnly",
  "routeScope": "audit"
} -->
# Loop Checkpoint Log

This file contains an append-only, sequential log that records the successful completion of each full ContextCascade loop (READ → ACT → WRITE). It serves as a crucial audit trail for system progression, rollback orchestration, and session reconstruction.

---
## Entry Format
Each entry signifies one successfully completed loop and should be recorded after all post-WRITE tasks (hash checks, confirmations, summary updates) are finished.

A structured format is recommended for each entry:

```
---
- **LoopID:** (Sequential integer or unique identifier, e.g., timestamp or global counter value)
  **Timestamp:** YYYY-MM-DDTHH:mm:ssZ (UTC)
  **JobPlanReference:** (Path or hash of the `job_logs/temp_job.md` that was executed)
  **FilesWritten:**
    - path: `/path/to/file1.md`
      hashAfter: "sha256-hash1..."
    - path: `/path/to/file2.md`
      hashAfter: "sha256-hash2..."
  **CountersIncremented:**
    - global: value_after
    - client: value_after (if client domain was affected)
    - server: value_after (if server domain was affected)
    - ... (other affected domain counters)
  **Outcome:** `success` (This file should only log successful loops. Failures are logged in `meta_audit.md`)
  **PostHashCheck:** `confirmed` | `warning` (if minor, non-critical discrepancies were noted but accepted)
---
```

---
## Usage
- **Traceability:** Provides a clear history of system operations.
- **Rollback:** Helps identify known-good states to roll back to if drift or corruption occurs.
- **Session Reconstruction:** Can assist in understanding the sequence of operations during an audit or debugging session.
- **Drift Detection:** Gaps in LoopIDs or timestamps might indicate missed cycles or system interruptions, prompting a look at `meta_audit.md`.

---
## Current Checkpoints:

*(This log is appended to by the system automatically after each successful WRITE cycle. No checkpoints yet.)*

---
## Maintenance
- This file is strictly append-only. Existing entries must never be modified or deleted.
- Ensure the LoopID is unique and preferably sequential.
- If a WRITE cycle fails or is aborted, no entry should be written here for that cycle. Failures are documented in `/cascade/audit/meta_audit.md`.
"""

    REPO_FILES["cascade/domains/client/index.md"] = """<!-- @meta {
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

| Path                                   | Role / Description                 |
|----------------------------------------|------------------------------------|
| `/cascade/domains/client/README.md`    | Overview of client domain memory   |

*(Add more entries as client-specific memory files are created.)*
"""

    REPO_FILES["cascade/domains/schema/index.md"] = """<!-- @meta {
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
"""

    REPO_FILES["cascade/domains/server/index.md"] = """<!-- @meta {
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
"""

    REPO_FILES["cascade/job_logs/recent.md"] = """<!-- @meta {
  "fileType": "rolling",
  "subtype": "buffer",
  "purpose": "A rolling log of the most recent job plan summaries, up to a defined maximum.",
  "editPolicy": "appendOnly",
  "routeScope": "global",
  "maxEntries": 5,
  "mergeTarget": "/cascade/job_logs/summary.md"
} -->
# Recent Job Logs

This file contains a rolling buffer of summaries from recently executed job plans (from `temp_job.md`). When this log exceeds `maxEntries` (5), the oldest entry is moved to `/cascade/job_logs/summary.md`.

Each entry should summarize a completed job, including:
- Job ID (could be a timestamp or a unique hash of the plan).
- Intent of the job.
- Key files affected.
- Status (e.g., success, failed, rolled_back).

---
*(No job summaries yet)*
"""

    REPO_FILES["cascade/job_logs/summary.md"] = """<!-- @meta {
  "fileType": "append-only",
  "purpose": "A permanent, append-only historical log of all job plan summaries, including those rolled over from job_logs/recent.md.",
  "editPolicy": "appendOnly",
  "routeScope": "global"
} -->
# Job Logs Summary

This file is an append-only historical ledger of all executed job plan summaries. It includes entries merged from `/cascade/job_logs/recent.md` when that buffer reaches its `maxEntries` limit.

---
## Guidelines
- Entries are added chronologically.
- Existing entries must not be modified or deleted.
- Each entry should provide a concise summary of an executed job plan, typically including:
    - Job ID or reference to the original `temp_job.md` (e.g., its hash or timestamp).
    - The stated `intent` of the job.
    - A list of key files targeted by the job.
    - The final `status` of the job (e.g., success, failure, rolled_back).
    - Timestamp of execution.

---
*(No job summaries yet)*
"""

    REPO_FILES["cascade/job_logs/temp_job.md"] = """<!-- @meta {
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
"""

    REPO_FILES["cascade/lifecycle/client.md"] = """<!-- @meta {
  "fileType": "counter",
  "purpose": "Tracks WRITE-phase activity specifically for the 'client' domain.",
  "editPolicy": "incrementOnly",
  "routeScope": "client"
} -->
# Client Domain Lifecycle Counter

This file tracks the total number of WRITE cycles that have specifically impacted the 'client' domain.

**Current Count:**

0

---
## Usage
- This counter should be incremented by 1 after every successful WRITE phase that modifies one or more files within the `client` routeScope.
- It is used by `/protocols/file_lifespans.md` to trigger `reread`, `prune`, or `merge` actions specific to the client domain.
- Do not edit this file manually. It is managed by the ContextCascade system.

---
## Integrity
- Expected value: A non-negative integer.
- Monotonically increasing.
"""

    REPO_FILES["cascade/lifecycle/counter.md"] = """<!-- @meta {
  "fileType": "counter",
  "purpose": "Tracks global WRITE-phase activity across all domains.",
  "editPolicy": "incrementOnly",
  "routeScope": "global"
} -->
# Global Lifecycle Counter

This file tracks the total number of WRITE cycles that have occurred across the entire ContextCascade system.

**Current Count:**

0

---
## Usage
- This counter should be incremented by 1 after every successful WRITE phase, regardless of the domain(s) affected.
- It is used by `/protocols/file_lifespans.md` to trigger global `reread`, `prune`, or `merge` actions.
- Do not edit this file manually. It is managed by the ContextCascade system.

---
## Integrity
- Expected value: A non-negative integer.
- Monotonically increasing.
"""

    REPO_FILES["cascade/lifecycle/drift_flag.md"] = """<!-- @meta {
  "fileType": "temporary",
  "purpose": "Signals an unresolved contradiction or deviation in the cascade lifecycle. Presence of this file may halt operations.",
  "editPolicy": "overwrite",
  "routeScope": "global",
  "ttlCycles": 1
} -->
# Drift Flag

**This file indicates a potential inconsistency or drift in the ContextCascade system.**

Its presence signifies that an unexpected state or behavior was detected, such as:
- A hash mismatch for an `immutable` or `protected` file.
- A lifecycle counter not incrementing as expected.
- A validator detecting a schema diff from a known snapshot.
- An unexpected file modification or deletion.

---
## Action Required
- **System Behavior:** The ContextCascade system may halt or enter a safe-hold mode when this file is present. Normal operations might be suspended until the drift is investigated and resolved.
- **Investigation:** Review `/audit/meta_audit.md` for detailed logs related to the detected drift.
- **Resolution:**
    1. Identify the cause of the drift.
    2. Take corrective actions as per `/cascade/protocols/recovery.md`. This might involve restoring files, correcting metadata, or acknowledging a deliberate change.
    3. Once the system state is verified and consistent, this flag file should be deleted or cleared as part of the recovery process.

---
## Content
This file may contain a brief, human-readable summary of the detected drift if generated by the system.

**Detected Drift (if any):**

No drift detected. System nominal.
"""

    REPO_FILES["cascade/lifecycle/schema.md"] = """<!-- @meta {
  "fileType": "counter",
  "purpose": "Tracks WRITE-phase activity specifically for the 'schema' domain.",
  "editPolicy": "incrementOnly",
  "routeScope": "schema"
} -->
# Schema Domain Lifecycle Counter

This file tracks the total number of WRITE cycles that have specifically impacted the 'schema' domain.

**Current Count:**

0

---
## Usage
- This counter should be incremented by 1 after every successful WRITE phase that modifies one or more files within the `schema` routeScope.
- It is used by `/protocols/file_lifespans.md` to trigger `reread`, `prune`, or `merge` actions specific to the schema domain.
- Do not edit this file manually. It is managed by the ContextCascade system.

---
## Integrity
- Expected value: A non-negative integer.
- Monotonically increasing.
"""

    REPO_FILES["cascade/lifecycle/security.md"] = """<!-- @meta {
  "fileType": "counter",
  "purpose": "Tracks WRITE-phase activity specifically for high-risk actions and security events.",
  "editPolicy": "incrementOnly",
  "routeScope": "security"
} -->
# Security Lifecycle Counter

This file tracks the total number of WRITE cycles related to high-risk actions or security events, such as modifications to protected files or security policy changes.

**Current Count:**

0

---
## Usage
- This counter should be incremented by 1 after every successful WRITE phase involving operations flagged with `requiresReview: true`, modifications to files in `/cascade/security/`, or changes to `immutable` files after override.
- It is used by `/protocols/file_lifespans.md` to trigger `reread`, `prune`, or `merge` actions specific to security-related contexts, potentially more aggressively.
- Do not edit this file manually. It is managed by the ContextCascade system.

---
## Integrity
- Expected value: A non-negative integer.
- Monotonically increasing.
"""

    REPO_FILES["cascade/lifecycle/server.md"] = """<!-- @meta {
  "fileType": "counter",
  "purpose": "Tracks WRITE-phase activity specifically for the 'server' domain.",
  "editPolicy": "incrementOnly",
  "routeScope": "server"
} -->
# Server Domain Lifecycle Counter

This file tracks the total number of WRITE cycles that have specifically impacted the 'server' domain.

**Current Count:**

0

---
## Usage
- This counter should be incremented by 1 after every successful WRITE phase that modifies one or more files within the `server` routeScope.
- It is used by `/protocols/file_lifespans.md` to trigger `reread`, `prune`, or `merge` actions specific to the server domain.
- Do not edit this file manually. It is managed by the ContextCascade system.

---
## Integrity
- Expected value: A non-negative integer.
- Monotonically increasing.
"""

    REPO_FILES["cascade/load_plans/.gitkeep"] = """"""

    REPO_FILES["cascade/load_plans/auto_plan_generic.md"] = """<!-- @meta {
  "fileType": "evictable",
  "ttlCycles": 2,
  "routeScope": "global",
  "purpose": "Generic auto-generated load plan. Defines files to be read in the next cycle.",
  "editPolicy": "overwrite"
} -->
# Auto-Generated Load Plan (Generic)

This file specifies the set of files to be loaded into context for the next READ phase. It is typically generated by the AI during the ACT phase of the previous cycle.

This is a generic placeholder. Specific load plans might be scoped by domain (e.g., `auto_plan_client.md`) or task.

---
## Files to Load:

- `/cascade/00_BOOTSTRAP.md`
- `/cascade/index.md`
- `/cascade/system_manifest.md`
- `/cascade/protocols/loop_protocol.md`
- `/cascade/protocols/file_lifespans.md`
- `/cascade/lifecycle/counter.md`
- `/cascade/change_log/recent.md`
- `/cascade/job_logs/recent.md`

*(This list should be dynamically generated based on the current task, routeScope, token budget, and lifecycle triggers.)*

---
## Instructions for AI:
- During the ACT phase, evaluate the needs for the next cycle.
- Generate a new file (or overwrite an existing one like this) in `/cascade/load_plans/` that lists the precise files required.
- Consider `routeScope`, `readPriority` from file metadata, `ttlCycles` of existing plans, and overall token budget.
- This plan will be consumed at the start of the next READ phase.
- If `ttlCycles` expires, this plan may be automatically pruned.
"""

    REPO_FILES["cascade/protocols/file_lifespans.md"] = """<!-- @meta {
  "fileType": "permanent",
  "purpose": "Defines counter thresholds that trigger rereads, pruning, or summary merges for each lifecycle scope.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
#### File Lifespan Thresholds
Thresholds below are evaluated during **Phase 2 – ACT**. When a lifecycle counter meets or exceeds a threshold, the corresponding action is queued for the next loop.
| Domain Scope | `reread_threshold` | `prune_threshold` | `merge_threshold` |
|--------------|--------------------|-------------------|-------------------|
| global (`counter.md`) | 5 | 7 | 10 |
| client (`client.md`)  | 3 | 5 | 8 |
| server (`server.md`)  | 3 | 5 | 8 |
| schema (`schema.md`)  | 4 | 6 | 9 |
| security (`security.md`) | 2 | 4 | 6 |
---
##### Threshold Meaning
- **`reread_threshold`** → Force a context reload for the domain on next READ.
- **`prune_threshold`** → Schedule deletion or archival of expired temp / rolling files.
- **`merge_threshold`** → Consolidate rolling buffers into durable summaries (e.g. `summary.md`).
---
##### Rationale (Lean)
- *Global* counters change most often → slightly larger window.
- *Client / Server* domains typically change more rapidly → tighter windows.
- *Schema* updates are less frequent but critical → moderate thresholds.
- *Security* events require aggressive maintenance to keep audit noise low.
---
##### Maintenance Guidance
- Update thresholds only via a reviewed job plan.
- Add a new row when introducing a new domain counter.
- Keep table alphabetised for diff‑friendly PRs.
"""

    REPO_FILES["cascade/protocols/loop_protocol.md"] = """<!-- @meta {
  "fileType": "protected",
  "purpose": "Defines the structured execution loop used by ContextCascade: READ → ACT → WRITE.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
#### Loop Protocol
<!-- PROTECTED -->
#### Three-Phase Execution Loop
This protocol enforces strict sequencing of AI task execution into three non-overlapping phases.
##### Phase 1 — READ
- Load context files as defined in the **active load plan** generated during the previous ACT.
- Perform no mutation or job logic.
- Validate hashes for all `immutable` or `protected` files.
##### Phase 2 — ACT
- Perform reasoning and generate a **job plan** (`temp_job.md`) plus an updated load plan (if needed).
- Create no file writes.
##### Phase 3 — WRITE
- **Pre-WRITE hash check**: verify immutable/protected files still match `integrity_snapshot.md`.
- Execute the job plan and mutate only allowed files.
- Recompute hashes and confirm against `expectedHashAfter`.
- Log deltas to `/cascade/change_log/` and increment lifecycle counters.
- Abort and enter Safe-Hold if any safeguard fails.
<!-- END PROTECTED -->
---
#### Loop Entry / Exit
- **Entry**: Allowed only when no `drift_flag.md` exists.
- **Exit**: Occurs after a successful WRITE and delta audit.
#### Safe-Hold Triggers
- Hash or safeguard failure
- Stale or conflicting `_locks/active_edit.lock`
- Missing / malformed `temp_job.md`
#### Audit Expectations
- Each phase transition must be traceable by job ID.
- Counters must increment exactly once per WRITE.
#### Maintenance Guidance
- Never modify PROTECTED sections except via security-reviewed job plans.
"""

    REPO_FILES["cascade/protocols/recovery.md"] = """<!-- @meta {
  "fileType": "permanent",
  "purpose": "Structured fallback procedure triggered by safeguard failure, drift, or WRITE abortion.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
#### Recovery Protocol
This file governs how the system recovers when the loop fails due to safeguard violations, hash mismatches, or unresolved drift.
---
##### 1. Automatic Triggers
- Presence of `/lifecycle/drift_flag.md`
- WRITE aborted during `loop_protocol.md`
- Stale `_locks/active_edit.lock` preventing job completion
- Corrupted or missing `temp_job.md`
---
##### 2. Recovery Phases
###### Phase A — Diagnose
1. Halt all WRITE operations
2. Review `/audit/meta_audit.md` for safeguard or hash breach
3. Validate `audit/integrity_snapshot.md` against current file states
4. Verify `temp_job.md` plan integrity
###### Phase B — Contain & Flag
1. Move unstable or suspect files to `/quarantine/YYYY-MM-DD/`
2. If not already present, create `/lifecycle/drift_flag.md` with cause summary
3. Document all actions in `/audit/meta_audit.md`
###### Phase C — Restore
1. Use `integrity_snapshot.md` to replace corrupted `immutable` or `protected` files
2. Generate a minimal load plan referencing only core files (BOOTSTRAP, INDEX, MANIFEST)
3. Clear `drift_flag.md` only after successful plan load and hash check
---
##### 3. Manual Interventions
- Restoration steps require elevated agent or human confirmation
- Log each override in `/security/security_review.md` tagged `recovery`
---
##### 4. Emergency Halt
If integrity cannot be restored:
1. Archive `/cascade/` ➜ `/cascade_stale_YYYYMMDD/`
2. Rebootstrap using seed files
3. Transfer only audited summaries or logs
4. Log postmortem to `/audit/meta_audit.md` with `postmortem` tag
---
##### 5. Post-Recovery Actions
| File | Expected Update |
|------|------------------|
| `/audit/meta_audit.md` | Recovery event logged |
| `/change_log/recent.md` | Deltas appended |
| `/checkpoints/loop_checkpoint.md` | New checkpoint tagged `recovery-N` |
| `/lifecycle/drift_flag.md` | Deleted or archived |
| `/quarantine/` | Retain for 30 days minimum |
---
##### 6. Prevention Notes
- Validate `temp_job.md` for each cycle
- Monitor lifecycle counters for drift or stalling
- Run a dry loop audit (`read-only mode`) periodically
"""

    REPO_FILES["cascade/protocols/safeguards.md"] = """<!-- @meta {
  "fileType": "permanent",
  "purpose": "Comprehensive enforcement rules for hash integrity, protected blocks, write-gates, and recovery triggers.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
#### Protocol Safeguards Policy
This policy centralises **all mandatory protections** that preserve the integrity, auditability, and governance of the ContextCascade memory layer.
---
##### 1. Enforcement Matrix
| # | Safeguard | Trigger Condition | Automatic Response |
|---|-----------|------------------|--------------------|
| 1 | **Immutable Hash Check** | Hash mismatch detected in any `fileType: immutable` file during pre‑ or post‑WRITE | • Abort WRITE<br>• Log `hashMismatch` in `/audit/meta_audit.md`<br>• Raise `/lifecycle/drift_flag.md` |
| 2 | **Protected Block Enforcement** | Attempted edit overlaps a `<!-- PROTECTED -->` span | • Abort WRITE<br>• Log `protectedOverlap`<br>• Require security review if `escalation: true` |
| 3 | **Write Gate Validation** | Target path not allowed by `/security/write_gates.md` | • Abort WRITE<br>• Log `gateViolation` |
| 4 | **Active Edit Lock** | `_locks/active_edit.lock` present at READ or WRITE start | • Halt loop in safe‑hold<br>• Prompt manual unlock if stale |
| 5 | **Pre/Post Hash Workflow** | Hash delta of protected/immutable files differs from plan | • Roll back WRITE<br>• Log `postHashMismatch`<br>• Flag drift |
| 6 | **High‑Risk Action Flag** | Job plan contains `requiresReview: true` or touches critical files (e.g. `system_manifest.md`) | • Suspend WRITE until review approved<br>• Record event in `security_review.md` |
---
##### 2. Metadata Quick‑Reference
| Marker | Effect |
|--------|--------|
| `fileType: immutable` | Seals file content; requires hash verification every loop |
| `editPolicy: readonly` | Disables all writes (immutable by intent) |
| `protected: true` | Marks inline block as untouchable, even if file is editable |
| `ttlCycles: N` | Governs expiry of temporary / evictable files |
| `requiresReview: true` | Forces human / elevated agent approval before WRITE |
---
##### 3. Hash Verification Workflow
1. **Pre‑WRITE**
   - Compute SHA‑256 for every file tagged `immutable` **or** containing a protected block.
   - Compare against `audit/integrity_snapshot.md`.
   - On any mismatch → **abort** and raise `hashMismatch`.
2. **Post‑WRITE**
   - Re‑hash the same set plus any files actually written.
   - Validate against `expectedHashAfter` in `/cascade/job_logs/temp_job.md`.
   - On success → append entry to `/cascade/change_log/recent.md`.
   - On failure → roll back write, set `drift_flag.md`.
---
##### 4. Protected Block Syntax
```md
<!-- PROTECTED -->
... uneditable content ...
<!-- END PROTECTED -->
```
- **Nested blocks** are not allowed.
- Attempting to insert, delete, or reorder text inside a protected span constitutes a `protectedOverlap` violation.
---
##### 5. Recovery & Escalation Paths
- **Safe‑Hold Mode**: Activated on any safeguard breach to prevent cascading corruption.
- **Loop Recovery**: Instructions in `/cascade/protocols/recovery.md` outline how to resume after drift resolution.
- **Security Review**: High‑risk or failed safeguards require a signed entry in `/cascade/security/security_review.md`.
- **Immutable Restore**: Use snapshots listed in `audit/integrity_snapshot.md` to roll back mutated files.
---
##### 6. Maintenance Guidance
- Update this file **only** through an approved security review.
- Keep safeguard IDs in the enforcement matrix **stable** for audit tooling.
- Align new safeguards with counters and thresholds defined in `file_lifespans.md`.
"""

    REPO_FILES["cascade/security/security_review.md"] = """<!-- @meta {
  "fileType": "append-only",
  "purpose": "Log of manual or AI-driven security reviews, findings, and approvals for high-risk actions.",
  "editPolicy": "appendOnly",
  "routeScope": "security"
} -->
# Security Review Log

This file contains an append-only log of all security reviews conducted. This includes reviews for:
- High-risk actions flagged with `requiresReview: true` in job plans.
- Modifications to critical system files (e.g., `system_manifest.md`, protocol files).
- Escalated permissions or overrides of `readonly`, `immutable`, or `protected` policies.
- Findings from manual or automated security audits.
- Approvals or rejections of proposed changes.

---
## Entry Format
Each entry should be clearly timestamped and include:
- **Date/Timestamp:** When the review was conducted.
- **Reviewer(s):** Who conducted the review (human agent ID or AI agent version).
- **Subject:** What was reviewed (e.g., Job Plan ID, file path, proposed change).
- **Details/Findings:** A summary of the review process and any findings.
- **Decision/Outcome:** Approved, Rejected, Needs More Info, etc.
- **Rationale:** Justification for the decision.
- **Associated Hashes:** (If applicable) Hashes of files before and after an approved change.

---
## Example Entry:
```
---
**Date/Timestamp:** 2025-07-15T10:30:00Z
**Reviewer(s):** human_admin_chris, ai_agent_jules_v1.2
**Subject:** Proposed modification to `/cascade/system_manifest.md` (Job Plan: job_temp_a1b2c3d4)
**Details/Findings:**
- Intent: Add new domain 'experimental_features'.
- Impact assessment: Low risk, isolated domain.
- Hash before: manifest_hash_v1_old
- Hash after (proposed): manifest_hash_v2_new
**Decision/Outcome:** Approved
**Rationale:** The new domain is well-defined and does not interfere with existing core domains. All necessary index files for the domain are included in the job plan.
**Associated Hashes:**
- `/cascade/system_manifest.md` (before): sha256-abc...
- `/cascade/system_manifest.md` (after): sha256-def...
---
```

---
*(No review entries yet)*
"""

    REPO_FILES["cascade/security/write_gates.md"] = """<!-- @meta {
  "fileType": "permanent",
  "purpose": "Defines glob patterns and path constraints to control which files can be written to. Acts as a write-time firewall.",
  "editPolicy": "appendOrReplace",
  "routeScope": "security"
} -->
# Write Gates Policy

This file defines the write gate policies for the ContextCascade system. It uses glob patterns and explicit path declarations to allow or deny write operations to specific files or directories. This acts as a crucial safeguard to prevent unintended or unauthorized modifications.

---
## Gate Configuration Format
Write gates are typically defined in a structured format, often YAML-like, within this document. The system will parse this section to enforce rules during the pre-WRITE validation phase.

**Key Principles:**
- **Deny by Default (Recommended):** It's often safer to deny writes to broad areas and then explicitly allow specific paths.
- **Specificity:** More specific rules usually override broader ones (though the exact precedence logic depends on the validator's implementation).
- **`allow` vs. `deny`:** Clearly state the intent.
- **`appendOnly` flag:** Can be used to allow writes but only in append mode for certain paths.

---
## Example Gate Configuration:
```yaml
writeGates:
  # Deny writes to all protocol files by default
  - deny: "/cascade/protocols/*"
  # But allow appendOrReplace to file_lifespans if specifically planned
  - allow: "/cascade/protocols/file_lifespans.md"
    editPolicy: "appendOrReplace" # Explicitly state allowed edit type

  # Immutable files - generally deny all direct writes
  - deny: "/cascade/00_BOOTSTRAP.md"
  - deny: "/cascade/system_manifest.md"
  - deny: "/cascade/init_context.md"
  # (Overrides for immutable files should be exceptional and logged via security_review.md)

  # Allow writes to job logs (temp_job is overwrite, others appendOnly)
  - allow: "/cascade/job_logs/temp_job.md"
    editPolicy: "overwrite"
  - allow: "/cascade/job_logs/recent.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/job_logs/summary.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/job_logs.md" # The index file
    editPolicy: "appendOrReplace"


  # Allow writes to change logs (recent is appendOnly, summary is appendOnly)
  - allow: "/cascade/change_log/recent.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/change_log/summary.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/change_log.md" # The index file
    editPolicy: "appendOrReplace"

  # Lifecycle counters are incrementOnly (a form of append)
  - allow: "/cascade/lifecycle/*.md" # Individual counters
    editPolicy: "incrementOnly" # Or appendOnly if incrementOnly is not a direct metadata policy
  - allow: "/cascade/lifecycle.md" # The index file
    editPolicy: "appendOrReplace"


  # Load plans are evictable and can be overwritten
  - allow: "/cascade/load_plans/*.md"
    editPolicy: "overwrite"

  # Taskbuffers are temporary and can be overwritten
  - allow: "/cascade/_taskbuffers/*.md"
    editPolicy: "overwrite"

  # Temp notes are rolling and can be appended to or sections replaced
  - allow: "/cascade/temp_notes/*.md"
    editPolicy: "appendOrReplace"

  # Audit files are generally append-only or managed by specific processes
  - allow: "/cascade/audit/meta_audit.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/audit/token_summary.md" # May be overwritten by analysis tools
    editPolicy: "overwrite"
  - allow: "/cascade/audit/integrity_snapshot.md" # Usually appendOnly, or specific update process
    editPolicy: "appendOnly"
  - allow: "/cascade/audit/prune_plan.md" # Evictable, can be overwritten
    editPolicy: "overwrite"


  # Checkpoints are append-only
  - allow: "/cascade/checkpoints/loop_checkpoint.md"
    editPolicy: "appendOnly"

  # Domain files - index files are often appendOnly or appendOrReplace
  # Content files within domains might have varying policies
  - allow: "/cascade/domains/*/index.md"
    editPolicy: "appendOrReplace"
  - allow: "/cascade/domains/*/*.md" # Be more specific for actual domain content files
    editPolicy: "appendOrReplace" # Default, can be overridden by file's own metadata

  # Security files themselves
  - allow: "/cascade/security/security_review.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/security/write_gates.md" # This file itself
    editPolicy: "appendOrReplace" # Needs to be editable, but with high review threshold

  # Meta files
  - allow: "/cascade/_meta/*.md"
    editPolicy: "appendOrReplace" # e.g., for cascade_feature_index.md

  # Deny everything else within /cascade/ by default if not explicitly allowed
  # This is a strong safeguard but requires diligent 'allow' rules.
  # - deny: "/cascade/**" (Use with caution and ensure all legitimate paths are allowed above)

```
---
## Current Gate Configuration:

# (Define your YAML or structured list of rules here)
# Example:
writeGates:
  - deny: "/cascade/protocols/*"
  - allow: "/cascade/protocols/file_lifespans.md"
    editPolicy: "appendOrReplace"
  - deny: "/cascade/00_BOOTSTRAP.md"
  - deny: "/cascade/system_manifest.md"
  - deny: "/cascade/init_context.md"
  - allow: "/cascade/job_logs/temp_job.md"
    editPolicy: "overwrite"
  - allow: "/cascade/job_logs/*.md" # recent.md, summary.md, job_logs.md (index)
    editPolicy: "appendOnly" # Default, specific files can refine
  - allow: "/cascade/change_log/*.md" # recent.md, summary.md, change_log.md (index)
    editPolicy: "appendOnly" # Default
  - allow: "/cascade/lifecycle/*.md"
  - allow: "/cascade/lifecycle.md"
    editPolicy: "appendOrReplace"
  - allow: "/cascade/load_plans/*.md"
    editPolicy: "overwrite"
  - allow: "/cascade/_taskbuffers/*.md"
    editPolicy: "overwrite"
  - allow: "/cascade/temp_notes/*.md"
    editPolicy: "appendOrReplace"
  - allow: "/cascade/audit/meta_audit.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/audit/token_summary.md"
    editPolicy: "overwrite"
  - allow: "/cascade/audit/integrity_snapshot.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/audit/prune_plan.md"
    editPolicy: "overwrite"
  - allow: "/cascade/checkpoints/loop_checkpoint.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/domains/**" # Broad allow for domains, individual files should have stricter policies
    editPolicy: "appendOrReplace"
  - allow: "/cascade/security/security_review.md"
    editPolicy: "appendOnly"
  - allow: "/cascade/security/write_gates.md" # This file
    editPolicy: "appendOrReplace"
  - allow: "/cascade/_meta/*.md"
    editPolicy: "appendOrReplace"
  - allow: "/cascade/index.md"
    editPolicy: "appendOnly"

---
## Maintenance
- Changes to this file are considered high-risk and **must** be logged in `/cascade/security/security_review.md`.
- Regularly audit these gates against the actual file structure and intended edit policies.
- Ensure the parsing logic in the AI agent or validator correctly interprets these rules.
"""

    REPO_FILES["cascade/temp_notes/.gitkeep"] = """"""

    REPO_FILES["cascade/temp_notes/planning_notes_global.md"] = """<!-- @meta {
  "fileType": "rolling",
  "subtype": "buffer",
  "purpose": "Rolling buffer for ongoing planning notes, ideas, or multi-step task tracking.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global",
  "maxEntries": 10,
  "mergePolicy": "squash",
  "mergeTarget": "/cascade/change_log/summary.md"
} -->
# Global Planning Notes (Rolling)

This file serves as a rolling buffer for general planning notes, ideas, or tracking multi-step tasks that span several cycles.

---
## Usage
- Append new notes or update existing sections.
- When `maxEntries` (e.g., 10, as an example here) is reached, older entries might be evicted or merged.
- The `mergePolicy` (e.g., `squash`) and `mergeTarget` (e.g., `/cascade/change_log/summary.md`) would define how its content is preserved long-term if needed, though these are illustrative here and should be set based on actual workflow.
- For domain-specific planning, consider creating separate files (e.g., `planning_notes_client.md`).

---
## Current Notes:

*(No notes yet. Add dated entries or task-specific sections below.)*

---
### Example Entry Format:
```
---
**Date:** YYYY-MM-DD
**Task/Topic:** Brief description
**Notes:**
- Point 1
- Point 2
- Action items...
---
```
"""

    REPO_FILES["cascade/validators/metadata_validator.ts"] = """// validators/metadata_validator.ts
// -------------------------------------------------
// ContextCascade Metadata Validator
// -------------------------------------------------
// Responsibilities:
//   • Parse top-of-file `@meta` JSON blocks
//   • Verify required fields per fileType / subtype
//   • Enforce editPolicy + routeScope value constraints
//   • Provide a structured API for loop controller
//
// Usage (inside loop controller):
//   import { validateFile } from "./validators/metadata_validator";
//   const report = validateFile(filePath, rawContent);
//   if (!report.valid) throw new Error(report.message);
// -------------------------------------------------

import fs from "fs";

// -------------------- Types ----------------------

interface MetaBlock {
  fileType: string;
  purpose?: string;
  editPolicy: "appendOnly" | "appendOrReplace" | "incrementOnly" | "readonly" | "replaceOnly";
  routeScope?: string;
  [key: string]: unknown;
}

interface ValidationReport {
  valid: boolean;
  message: string;
  warnings: string[];
  meta?: MetaBlock;
}

// -------------------- Constants ------------------

const REQUIRED_FIELDS = ["fileType", "editPolicy"] as const;
const ALLOWED_FILE_TYPES = new Set([
  "permanent",
  "immutable",
  "rolling",
  "append-only",
  "temporary",
  "counter",
  "evictable",
  "protected",
  "structural"
]);

const ALLOWED_EDIT_POLICIES = new Set([
  "appendOnly",
  "appendOrReplace",
  "incrementOnly",
  "readonly",
  "replaceOnly",
]);

// -------------------- Helper Functions -----------

function extractMeta(raw: string): { meta?: MetaBlock; remainder: string } {
  const match = raw.match(/<!--\s*@meta\s*({[\s\S]*?})\s*-->/m);
  if (!match) return { remainder: raw };
  try {
    const meta = JSON.parse(match[1]);
    return { meta, remainder: raw.replace(match[0], "") };
  } catch (e) {
    throw new Error("Invalid JSON in @meta block: " + e.message);
  }
}

function validateMeta(meta: MetaBlock, filePath: string): ValidationReport {
  const warnings: string[] = [];

  // Required fields
  for (const key of REQUIRED_FIELDS) {
    if (!(key in meta)) {
      return {
        valid: false,
        message: `Missing required field \"${key}\" in @meta for ${filePath}`,
        warnings,
      };
    }
  }

  // fileType check
  if (!ALLOWED_FILE_TYPES.has(meta.fileType)) {
    return {
      valid: false,
      message: `Invalid fileType \"${meta.fileType}\" in ${filePath}`,
      warnings,
    };
  }

  // editPolicy check
  if (!ALLOWED_EDIT_POLICIES.has(meta.editPolicy)) {
    return {
      valid: false,
      message: `Invalid editPolicy \"${meta.editPolicy}\" in ${filePath}`,
      warnings,
    };
  }

  // routeScope recommendation
  if (!meta.routeScope) {
    warnings.push("routeScope missing — recommend specifying domain or global.");
  }

  return { valid: true, message: "OK", warnings, meta };
}

// -------------------- Public API -----------------

export function validateFile(filePath: string, raw?: string): ValidationReport {
  const content = raw ?? fs.readFileSync(filePath, "utf8");
  const { meta } = extractMeta(content);
  if (!meta) {
    return {
      valid: false,
      message: `No @meta block found in ${filePath}`,
      warnings: [],
    };
  }
  return validateMeta(meta, filePath);
}

// CLI utility (optional)
if (require.main === module) {
  const target = process.argv[2];
  if (!target) {
    console.error("Usage: ts-node metadata_validator.ts <filePath>");
    process.exit(1);
  }
  const report = validateFile(target);
  if (report.valid) {
    console.log("✔", target, "validated");
    if (report.warnings.length) console.warn("Warnings:", report.warnings.join("; "));
  } else {
    console.error("✖", target, report.message);
    process.exit(2);
  }
}
"""

if __name__ == "__main__":
    create_repo_structure()
