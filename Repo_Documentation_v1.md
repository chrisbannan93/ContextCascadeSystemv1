# ContextCascade Developer & User Documentation

*A comprehensive guide for developers and AI assistants to correctly load, use, update, and maintain a ContextCascade system.*

---
## 0. Front Matter

- **Document Title:** ContextCascade Developer & User Documentation
- **Version:** 1.0
- **Maintainer:** Chris Bannan
- **Last Updated:** 25/06/2025
- **Contact:** [chris.bannan@vocus.com.au](mailto\:chris.bannan@vocus.com.au)

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
Please load the ContextCascade system starting at /cascade/index.md. Use the loop protocol defined in /cascade/protocols/loop_protocol.md.
Respect file lifespans and read priorities as defined in /cascade/protocols/file_lifespans.md.
Only act after completing a full READ phase.
```

This can be shortened with aliases or injected into Replit’s AI memory, but must always include the file path anchors.

### 1.4 Validation Checklist

Before first use or AI engagement:

-

*Optional:* Attach and offer a ZIP archive of a starter scaffold with empty files for all required paths. Consider bundling `index.md`, `loop_protocol.md`, and `file_lifespans.md` with default safe values.

## 2. Conceptual Overview

### 2.1 What is ContextCascade?

ContextCascade is a modular, file-based memory and protocol system designed to simulate persistent context for AI coding assistants — especially those operating in environments like Replit where native memory is limited.

It works by externalizing architectural, behavioral, and decision-making context into a standardized directory of markdown files, each with a defined purpose, metadata annotations, and lifecycle controls.

ContextCascade is not a code framework — it is a guidance and memory augmentation protocol. It defines how the AI should reason, read, act, write, and recontextualize its behavior before and after each code-related action.

It ensures that memory is durable across prompts, safeguards are embedded, files are updated appropriately, and long-term architectural consistency is maintained, even across fragmented Replit AI sessions.

This system leverages a cascade pattern — often read top-down — where files like `index.md`, `loop_protocol.md`, `file_lifespans.md`, and rolling logs form a multi-phase loop with embedded counters and condition-based execution logic.

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
User Prompt ──► Replit AI ──► /cascade/index.md
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

## 3. Directory & File Map

### 3.1 Full Directory Tree

```plaintext
/cascade/
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
│   └── metadata_validator.ts            # CLI: header, hash, timestamp checks
└── _meta/
    └── cascade_feature_index.md         # Master feature & directory catalogue
```

## 3.2 File Type Classification

## 3.2.1 Canonical FileType Registry
The table below is the **single source of truth** for `fileType` values.  
Any value not in the **FileType** column must instead be declared as a `subtype`.

| FileType      | Allowed Subtypes / Aliases  | Behavior Summary                         |
|---------------|-----------------------------|------------------------------------------|
| permanent     | checkpointed                | Editable, persists forever.              |
| immutable     | –                           | Never changes; hash-protected.           |
| rolling       | buffer                      | FIFO or LRU rotation.                    |
| append-only   | –                           | Only `append`; no deletes.               |
| temporary     | temp · ephemeral · job_plan | Auto-evicted ≤ 1 loop.                   |
| counter       | –                           | Stores lifecycle counts.                 |
| evictable     | –                           | TTL-based caches / plans.                |
| protected     | –                           | Write-locked inside `<!-- PROTECTED -->`.|
| structural    | domain_spec · index         | Pure navigation / mapping.               |

**Schema rule:**  
 • Every file **must** declare `fileType` from the left column.  
 • Optional `subtype` may be used **only** if listed in the centre column.

## 3.2.2 File Classes Overview (9 types) 

Below is an updated table with **nine** file‑type classes, adding **immutable** to capture files that must never change after initial creation.

| # | File Type       | Description                                                  | Lifespan   | Example Files                                 |
| - | --------------- | ------------------------------------------------------------ | ---------- | --------------------------------------------- |
| 1 | **Permanent**   | Persist entire project; editable if architecture changes.    | Infinite   | `overview.md`, `state/current.md`             |
| 2 | **Immutable**   | **Never modified** after creation; core doctrine / manifest. | Infinite\* | `system_manifest.md`, `init_context.md`       |
| 3 | **Rolling**     | Holds last N entries; drops oldest on overflow.              | Dynamic    | `change_log/recent.md`, `temp_notes/…`        |
| 4 | **Append‑Only** | Chronological log; only appends.                             | Infinite   | `change_log/summary.md`, `meta_audit.md`      |
| 5 | **Temporary**   | One‑prompt buffers; deleted post‑WRITE.                      | 1 cycle    | `_taskbuffers/*.md`, `job_logs/temp_job.md`   |
| 6 | **Counter**     | Tracks domain or global iterations.                          | Infinite   | `lifecycle/counter.md`, `lifecycle/client.md` |
| 7 | **Evictable**   | Cache / plan files with TTL or cycle cap.                    | TTL        | `load_plans/*.md`, `prune_plan.md`            |
| 8 | **Protected**   | Editable except inside `<!-- PROTECTED -->` blocks.          | Infinite   | `write_gates.md`, `safeguards.md`             |
| 9 | **Structural**  | Index or mapping files; reflect directory changes.           | Infinite   | `index.md`, `cascade_feature_index.md`        |

\* Immutable files participate in integrity hashing and should trigger alerts if altered.

### Immutable File Safeguard

- **Metadata** must include `"fileType": "immutable"` and `"editPolicy": "readonly"`.
- Immutable files are hashed on every integrity snapshot (`audits/integrity_snapshot.md`).
- If a hash mismatch is detected, AI must:
  1. Halt WRITE phase.
  2. Log violation in `temp_notes/security_flags.md`.
  3. Increment `lifecycle/security.md` counter.
  4. Await human review.

Metadata example:

```markdown
<!-- @meta {
  "fileType": "immutable",
  "purpose": "System doctrine and architecture that must never change.",
  "editPolicy": "readonly"
} -->
```

### Hash Verification Workflow

1. During READ phase on every 10th global lifecycle count, AI loads `integrity_snapshot.md`.
2. Recalculate hashes for all files classified as `immutable`.
3. Compare to stored hashes.
4. If mismatch → follow Immutable File Safeguard steps above.

---

### 3.3 File Purpose Annotations

Each ContextCascade file should begin with a lightweight metadata header that explicitly describes its purpose, usage rules, and expected behavior. This ensures the AI assistant always understands how to interpret and interact with the file.

#### Required Metadata Block (Markdown Comment Format)

```markdown
<!-- @meta {
  "fileType": "rolling",               // One of: permanent, rolling, append-only, temporary, counter, evictable, protected, structural
  "purpose": "Buffer for recent updates and summaries.",
  "editPolicy": "appendOrReplace",      // Could be: readonly, appendOnly, overwrite, appendOrReplace
  "maxEntries": 5,                      // For rolling buffers only
  "evictionPolicy": "FIFO"             // For buffers and caches
} -->
```

#### Interpretation Guide

- `fileType`: Informs the AI of its behavior and relationship to the system (read/update/delete logic).
- `purpose`: Describes what the file holds and why.
- `editPolicy`: Tells the AI how it can interact with the file.
- `maxEntries` and `evictionPolicy`: Optional for rolling files; define entry limits and replacement rules.

#### Example Metadata Header for `recent.md`

```markdown
<!-- @meta {
  "fileType": "rolling",
  "purpose": "Contains the 5 most recent update logs for short-term context recall.",
  "editPolicy": "appendOrReplace",
  "maxEntries": 5,
  "evictionPolicy": "FIFO"
} -->
```

#### Placement

This metadata block should be the first element in the file before any visible content. It serves as a directive for the AI, offering a lightweight but clear schema for system behavior.

### 3.4 How to Add or Modify Directories

When introducing new directories or modifying existing ones within the ContextCascade system, follow this structured protocol to ensure system-wide consistency and AI compliance:

#### 3.4.1 File Path Creation

- New directories must follow lowercase, hyphenated naming (e.g. `client-notes/`, `api-contracts/`).
- Place new domain-specific folders inside the appropriate `/domains/` subfolder when applicable.
- Avoid underscores in folder names unless reserved (e.g., `_taskbuffers/`).

#### 3.4.2 Metadata Anchoring

Each new directory must contain:

- A root-level `README.md` or `index.md` with a metadata block:

```markdown
<!-- @meta {
  "fileType": "structural",
  "subtype": "domain_spec",
  "routeScope": "client",
  "ownedBy": "lifecycle/client.md",
  "purpose": "Domain index & routing metadata.",
  "editPolicy": "appendOrReplace"
} -->

```

- Include guidance about:
  - File naming rules
  - Purpose of the directory
  - How files inside it should be read, updated, and purged
  - Sample prompt usage for AI to interact with it

#### 3.4.3 Register the Directory in System Index

- Add the new directory path to `/cascade/index.md`
- Add an entry in `/cascade/_meta/cascade_feature_index.md` that:
  - Briefly describes the directory’s role
  - Links to any protocols or lifespans it follows

### 3.4.4 Add to Load Plans (Optional)

If this new directory needs regular reading:

- Create or update a plan in `/cascade/load_plans/` referencing:
  - When it should be loaded (e.g. every Nth lifecycle read, post-client change)
  - What files within it are prioritized

### 3.4.5 Assign Lifecycle Policies

If the directory has temporary, rolling, or log-style contents:

- Specify thresholds or TTLs in `/protocols/file_lifespans.md`
- Create a scoped lifecycle counter if needed (`/lifecycle/<domain>.md`)

### 3.4.6 Update Loop Protocol (if needed)

If the new directory requires special handling (e.g. pre-write validation, elevated review):

- Update `/protocols/loop_protocol.md` to include any READ/WRITE phase adjustments.
- Flag any protected files in `/security/write_gates.md`

### 3.4.7 AI Prompting Instructions

Include example prompt snippets in the `index.md` or domain `README.md` that show how to:

- Reference the directory from Replit AI
- Request reads or summaries
- Request creation of new file types within it

#### Example Directory Addition Summary

```markdown
New Directory: `/domains/api/`
Purpose: To house API contracts, schema examples, and integration assumptions.
- Added `index.md` with metadata
- Registered in `/cascade/index.md`
- Added read behavior to `load_plans/api_load_plan.md`
- TTL threshold set to 10 lifecycles in `file_lifespans.md`
- Added client counter trigger in `lifecycle/api.md`
```

Following this procedure ensures new directories and structural updates remain compatible with all lifecycle counters, logs, security write gates, and loop protocols.

## 4. Metadata & File Headers

### 4.1 Required Metadata for All Files

Every file in the ContextCascade system must begin with a standardized metadata comment block to ensure AI comprehension of its type, purpose, and handling strategy.

**Required Metadata Fields:**

- `fileType`: One of `permanent`, `immutable`, `rolling`, `append-only`, `temporary`, `counter`, `evictable`, `protected`, `structural`
- `purpose`: A concise description of the file’s role in the system
- `editPolicy`: Defines how the file can be edited (e.g. `readonly`, `appendOnly`, `overwrite`, `appendOrReplace`)
- *(Optional but encouraged)* `maxEntries`, `evictionPolicy`, `ttlCycles`, `refreshInterval`

**Example Metadata Header:**

```markdown
<!-- @meta {
  "fileType": "immutable",
  "purpose": "System doctrine that must never change after initialization.",
  "editPolicy": "readonly"
} -->
```

**Placement:**

- Always place the metadata comment as the first line in the file
- This metadata block is not rendered in Markdown viewers, but is machine-readable by Replit AI and parsing tools

**Interpretation Behavior:**

- AI assistants must parse and act on this block before performing READ or WRITE operations
- Metadata should be updated by the AI if a file’s behavior or threshold changes as part of a job plan (except `immutable` files which must remain unchanged)

**Additional Metadata Conventions:**

- Use `ttlCycles` to define temporary file lifespan in lifecycle counter units
- Use `refreshInterval` to instruct AI how often to reread this file (overrides global plan if present)
- Use `linkedDomains` to specify if a file should only be loaded under specific client/server/schema operations

**Metadata Parsing Example:**

A `temp_notes/planning_scratch.md` file might use:

```markdown
<!-- @meta {
  "fileType": "temporary",
  "purpose": "One-prompt planning buffer, discarded after WRITE phase.",
  "editPolicy": "overwrite",
  "ttlCycles": 1
} -->
```

### 4.2 Format Examples by File Type Format Examples by File Type

Below are populated examples for each of the main file types defined within the ContextCascade system. Each includes a metadata header, sample content, and in some cases, structural guidelines for appending or overwriting data.

#### 4.2.1 Permanent File (e.g., `loop_protocol.md`)

```markdown
<!-- @meta {
  "fileType": "permanent",
  "purpose": "Defines the action loop protocol for each AI operation.",
  "editPolicy": "overwrite"
} -->

## Loop Protocol (READ → ACT → WRITE)

1. READ: Load relevant context files according to load plan and file lifespans.
2. ACT: Perform logic, decisions, planning, or execution.
3. WRITE: Save outputs, plans, logs, and summaries with hash protection.
```

#### 4.2.2 Rolling File (e.g., `change_log/recent.md`)

```markdown
<!-- @meta {
  "fileType": "rolling",
  "purpose": "Holds the 5 most recent updates to help AI maintain short-term memory.",
  "editPolicy": "appendOrReplace",
  "maxEntries": 5,
  "evictionPolicy": "FIFO"
} -->

### Most Recent Updates
1. Added `api_endpoints.md` for new client API
2. Updated `client_contract.md` with token-based auth
3. Created `temp_job.md` for UI refactor hash-checking
```

#### 4.2.3 Append-Only File (e.g., `change_log/summary.md`)

```markdown
<!-- @meta {
  "fileType": "append-only",
  "purpose": "Full chronological log of all AI-generated changes.",
  "editPolicy": "appendOnly"
} -->

#### Log Entry - Cycle 32
- Modified `server/index.md`
- Refactored job plan structure
- Summary: Aligned backend spec with frontend component
```

#### 4.2.4 Temporary File (e.g., `job_logs/temp_job.md`)

```markdown
<!-- @meta {
  "fileType": "temporary",
  "subtype": "job_plan",
  "purpose": "One-cycle job plan with file hashes for post-check validation.",
  "editPolicy": "overwrite",
  "ttlCycles": 1
} -->


## Temp Job Plan (Prompt ID: 49)

### Planned Changes
- Modify `client_nav.md`
- Create `modal_access.md`

### File Hash Pre/After
- `client_nav.md`: 298f... → b813...
- `modal_access.md`: null → b22a...
```

#### 4.2.5 Counter Tracker (e.g., `lifecycle/client.md`)

```markdown
<!-- @meta {
  "fileType": "counter",
  "purpose": "Tracks how often client files are updated.",
  "editPolicy": "appendOrReplace"
} -->

## Client Lifecycle Counter
- Current Count: 21
- Last Trigger: `client_ui_update.md`
- Next Action Threshold: 25
```

#### 4.2.6 Evictable Cache File (e.g., `load_plans/api_load_plan.md`)

```markdown
<!-- @meta {
  "fileType": "evictable",
  "purpose": "Temporary file to control context loading for API modules.",
  "editPolicy": "overwrite",
  "ttlCycles": 5
} -->

## API Load Plan (Client Module)
- Read: `client_endpoints.md`, `client_auth.md`
- Skip: `archive/`, `legacy_ui.md`
```

#### 4.2.7 Protected File (e.g., `security/write_gates.md`)

```markdown
<!-- @meta {
  "fileType": "protected",
  "purpose": "Lists write-locked files that require elevated safeguards.",
  "editPolicy": "appendOrReplace"
} -->

## Write Gates (Critical Protection)
<!-- PROTECTED -->
- `index.md`
- `loop_protocol.md`
<!-- END PROTECTED -->
```

#### 4.2.8 Structural File (e.g., `index.md`)

```markdown
<!-- @meta {
  "fileType": "structural",
  "subtype": "domain_spec",
  "routeScope": "server",
  "ownedBy": "lifecycle/server.md",
  "purpose": "Domain index & routing metadata.",
  "editPolicy": "appendOrReplace"
} -->


## /cascade Directory Map
- protocols/
- lifecycle/
- change_log/
- job_logs/
- load_plans/
```

These templates serve as the canonical format for each file type. All ContextCascade implementations should align to these conventions to ensure AI compatibility and loop integrity.

### 4.3 Protected Sections (`<!-- PROTECTED -->`)

Some ContextCascade files include protected sections marked with `<!-- PROTECTED -->` and `<!-- END PROTECTED -->`. These sections must **never be edited** or removed by the AI assistant, regardless of the task.

#### 4.3.1 Purpose

- Preserve critical logic, architectural rules, or human-authored content.
- Prevent loop overwrites from accidentally modifying base protocols or definitions.

#### 4.3.2 Behavior Rules

- AI assistants must parse the markdown and recognize all lines between `<!-- PROTECTED -->` and `<!-- END PROTECTED -->` as **read-only**.
- Updates can be made to other parts of the file if allowed by `editPolicy`, but must **not modify protected blocks**.

#### 4.3.3 Use Cases

- `loop_protocol.md`: Critical for loop integrity and action sequencing.
- `write_gates.md`: Defines write-protected files that should not be overwritten without permission.
- `index.md`: Anchors system structure and is often partially protected.

#### 4.3.4 AI Validation Step

- When performing the WRITE phase, check whether edits intersect with protected sections.
- If they do, reject the update and append a `job_logs/temp_job.md` note explaining why the write was aborted.

### 4.4 Immutable & Checkpoint File Examples

##### 4.4.1 loop_checkpoint.md

```markdown
<!-- @meta {
  "fileType": "permanent",
  "subtype": "checkpointed",
  "purpose": "Records completion status of each loop cycle (✓ READ ✓ ACT ✓ WRITE).",
  "editPolicy": "overwrite"
} -->

Loop #42 | loopId: d9a7-42b1 | ✓ READ ✓ ACT ✓ WRITE | 2025-06-25T14:21:00Z
```

##### 4.4.2 system_manifest.md (Immutable Example)

```markdown
<!-- @meta {
  "fileType": "immutable",
  "purpose": "Core doctrine and architecture references for ContextCascade.",
  "editPolicy": "readonly"
} -->

# System Manifest (Do Not Edit)

- Defines directory taxonomy
- Sets fundamental design principles
- Any change requires manual override and new hash snapshot
```

Some ContextCascade files include protected sections marked with `<!-- PROTECTED -->` and `<!-- END PROTECTED -->`. These sections must **never be edited** or removed by the AI assistant, regardless of the task.

### Purpose

- Preserve critical logic, architectural rules, or human-authored content.
- Prevent loop overwrites from accidentally modifying base protocols or definitions.

### Behavior Rules

- AI assistants must parse the markdown and recognize all lines between `<!-- PROTECTED -->` and `<!-- END PROTECTED -->` as **read-only**.
- Updates can be made to other parts of the file if allowed by `editPolicy`, but must **not modify protected blocks**.

### Use Cases

- `loop_protocol.md`: Critical for loop integrity and action sequencing.
- `write_gates.md`: Defines write-protected files that should not be overwritten without permission.
- `index.md`: Anchors system structure and is often partially protected.

### AI Validation Step

- When performing the WRITE phase, check whether edits intersect with protected sections.
- If they do, reject the update and append a `job_logs/temp_job.md` note explaining why the write was aborted.

### Example

```markdown
<!-- PROTECTED -->
- `index.md`
- `loop_protocol.md`
<!-- END PROTECTED -->
````

In this example, the AI may not modify these filenames or reorder/delete them, even if changes are requested elsewhere in the system.

Always treat these protected blocks as immutable unless explicitly directed by the user or a trusted elevated protocol.

## 5. Lifecycle Counters

### 5.1 Global and Domain-Specific Counters

Counters in the ContextCascade system serve as trigger mechanisms that track how many lifecycle iterations or prompt cycles have occurred. These counters determine when specific files or domains should be reloaded, refreshed, or purged. They help maintain balance between contextual fidelity and memory efficiency.

#### 5.1.1 Counter Types

- **Global Counter (**\`\`\*\*\*\*)\*\*

  - Tracks overall prompt cycles or interactions with the entire ContextCascade system.
  - Used to trigger periodic integrity checks, full context refreshes, and token budget audits.

- **Domain-Specific Counters (**`****, **`**, etc.)**

  - Track interactions or changes scoped to specific areas (e.g., client-side logic, server configuration).
  - Help the AI selectively reload only relevant parts of the cascade.

#### 5.1.2 Conditional Counting (New Mechanism)

ContextCascade supports **conditional lifecycle increments** based on file interaction scope:

- If an AI prompt modifies only client-side files → increment only `client.md`.
- If it updates server-side files → increment only `server.md`.
- If both domains are touched → increment both.
- If global rules or architectural doctrine is engaged → increment the global counter.

This ensures precise control over when to refresh or reread files, improving efficiency and trace accuracy.

#### 5.1.3 Metadata & Logging

Each counter file must include a consistent metadata header with the following fields:

```markdown
---
file_type: lifecycle_counter
scope: global | domain-specific
category: trigger | conditional | rolling
last_incremented: YYYY-MM-DDTHH:MM:SSZ
threshold_next_check: integer
---
```

These metadata fields help AI routines evaluate when to reload the file, determine if thresholds have been exceeded, and log event timestamps for audit trails. Each time a counter is incremented, the `last_incremented` timestamp should update.

A corresponding log entry may be appended to `meta_audit.md` or `token_summary.md` for traceability.

#### 5.1.4 Counter Threshold Use

Each counter supports an optional **trigger threshold** value. When the counter reaches this threshold, the AI should perform an action such as:

- Re-reading certain files
- Pruning or compressing buffers
- Conducting integrity or drift audits
- Resetting stale plans

Thresholds are defined in `file_lifespans.md` and vary by file class or domain. For example:

```yaml
client.md:
  threshold: 5
  action: reread client/* and update recent.md
```

AI should compare the current counter value against these thresholds and conditionally trigger reads or updates to ensure lean operation while preserving cascade context fidelity.

### 5.2 Counter Trigger Thresholds

#### Types of Thresholds:

1. **Fixed Thresholds** – These are hardcoded values in `file_lifespans.md` that define a set lifecycle count after which an action must be taken (e.g., reread, audit).
2. **Sliding Thresholds** – Thresholds that adapt based on AI behavior or file class. For example, if more frequent changes occur, the threshold may reduce to preserve fidelity.
3. **Compound Thresholds** – Thresholds triggered only if multiple counters reach a defined state together (e.g., both `client.md` and `server.md` at threshold).
4. **Time-Based Thresholds** – Optional, for long-idle sessions, the AI may check if elapsed time warrants a context refresh even if counts are low.

#### How AI Determines Thresholds

Thresholds are configured in `protocols/file_lifespans.md`. During the READ phase of the loop protocol, the AI checks:

- The current value in the relevant counter file
- The configured threshold from `file_lifespans.md`
- Whether a file is protected, temporary, or subject to pruning rules
- Whether this check has already occurred recently (by checking `last_incremented`)

If threshold values are reached or exceeded, AI performs corresponding maintenance or file loading operations.

#### Example Threshold Block (in `file_lifespans.md`)

```yaml
client.md:
  threshold: 5
  action:
    - reread: ["domains/client/*.md"]
    - update: ["change_log/recent.md"]
    - audit: ["audit/meta_audit.md"]

server.md:
  threshold: 7
  action:
    - reread: ["domains/server/*.md"]
    - prune: ["temp_notes/server/*"]
```

#### Best Practices

- Use odd-numbered thresholds to reduce the chance of simultaneous threshold collisions.
- Maintain low thresholds (3–7) for volatile areas like `temp_notes/*`.
- Allow higher thresholds (10–20) for stable, rarely changing domains like schema.
- Always confirm that the AI logs counter actions in `meta_audit.md` or similar audit files.
- Ensure counter files are never auto-deleted unless explicitly marked as ephemeral.

### 5.3 Rolling Update Triggers

Rolling update triggers are events or thresholds that signal the AI to perform non-critical but helpful updates to various cascade files. Unlike lifecycle-triggered reads, rolling update triggers usually occur after a successful WRITE phase, allowing the system to append summaries, update short-term logs, and prepare the cascade for the next session without overloading context.

#### Use Cases

Rolling update triggers enhance the fluidity and responsiveness of the ContextCascade system. They are useful for tasks that don’t warrant full rereads or threshold-based audits but still maintain continuity and context hygiene.

- Post-WRITE phase job plan logging
- Appending human-readable summaries
- Syncing short-term buffers
- Nudging recent.md or scratch areas with low-effort updates
- Refreshing incomplete load plans

#### When Rolling Updates Are Triggered

Rolling updates are typically triggered when:

- A WRITE phase successfully completes and files are saved
- A counter threshold is close to but not yet exceeded
- The AI determines from pattern detection that a small update will benefit continuity
- A temp\_job.md includes a `post_action` directive

#### Target Files for Rolling Update Triggers

- `change_log/recent.md`: Append a simplified trace of the last action.
- `load_plans/*.md`: Update or replace outdated read strategies.
- `temp_notes/*`: Prune irrelevant notes and tag them as expired.
- `summary.md`: Append only if certain structural markers are found (e.g., `## Milestone`).
- `meta_audit.md`: Record the trigger source if non-critical.

#### Rolling Update Control in Loop Protocol

- During the WRITE phase, the AI checks `rolling_update_eligible` metadata.
- If true, a separate rolling update queue is generated and appended to `temp_job.md`.
- These rolling updates are executed immediately unless in dry-run or debug mode.
- AI avoids triggering rolling updates if `recent.md` was just modified to prevent recursion.

#### Best Practices

- Always validate that a rolling update doesn’t increase total token count by more than 2%.
- Avoid rolling updates that affect files marked `file_type: immutable`.
- Rate-limit rolling updates to no more than 1 per 3 prompts per file.
- Do not trigger on temp or one-prompt files unless explicitly flagged as recyclable.

#### Example Job Log Entry

```markdown
### Rolling Update (Triggered After WRITE)
files_updated:
  - change_log/recent.md
  - load_plans/auto_plan_server.md
reason: "Successful WRITE and fresh job plan generated"
notes: "Merged last user action summary and prepared new read strategy"
```

### 5.4 Domain Routing (client/server/schema/etc)

The ContextCascade system leverages domain-specific counters and routing logic to ensure only relevant files are loaded and modified during each lifecycle iteration. This improves token efficiency and safeguards structural integrity.

#### 5.4.1 Purpose of Domain Routing

Domain routing allows the AI to:

- Identify and isolate file updates to a specific context domain (e.g., client, server, schema)
- Minimize unnecessary reads of unrelated domains
- Prevent counter inflation across unrelated areas
- Track isolated changes for audit clarity

#### 5.4.2 Routing Mechanics

Domain routes are determined by directory path and reinforced via metadata headers in each domain file:

```markdown
---
file_type: domain_spec
route_scope: client | server | schema
owned_by: domain_lifecycle_counter.md
...
```

The AI uses this metadata and path logic to:

- Increment the correct domain lifecycle counter
- Trigger domain-specific threshold behavior
- Append logs to `change_log/recent.md` using a domain-aware template

#### 5.4.3 Cross-Domain Scenarios

In cases where the AI touches multiple domains (e.g., both client and schema):

- All involved counters must increment
- Each affected file’s routing must be preserved in the job log
- A combined threshold audit may be scheduled depending on `file_lifespans.md`

#### 5.4.4 Domain-Aware Load Plans

Load plans in `/load_plans/` are named according to their intended domain scope:

- `auto_plan_client.md`
- `auto_plan_schema.md`

These guide AI loading behavior when performing READ phase operations, and allow partial refreshes of the cascade context.

#### 5.4.5 Best Practices

- Keep domain routing metadata updated across all scoped files.
- Use `/domains/` subfolders to organize client, server, and schema separately.
- Avoid cross-domain plans unless changes cannot be isolated.
- Ensure job logs include domain flags for traceability and rollback.

## 6. Phase Protocols (Loop)

### 6.1 READ Phase (Loading Strategy)

The READ phase is a lightweight, threshold-aware loading pass that decides **what** files to ingest and **in what order**, balancing token budget, domain scope, and integrity safeguards before any ACT logic runs.

#### 6.1.1 Goals

1. **Load just enough context** to make an informed decision in ACT.  
2. **Respect file lifespans & counters** defined in `protocols/file_lifespans.md`.  
3. **Detect drift or tampering early** via optional hash checks on immutable/protected files.  
4. **Stay within the active model’s token window** (lean first, expand only if needed).  

#### 6.1.2 Load Modes

There are three canonical READ phase loading modes:

**• Lean Mode**  
_Default for small prompts or when the token budget is tight._  
**Loads:**
- `index.md`
- `protocols/loop_protocol.md`
- The active `load_plans/*.md`
- Minimal domain index files
- Any lifecycle counters that just incremented

**• Domain Mode**  
_Triggered when the prompt targets a single domain and its lifecycle counter is below threshold._  
**Loads:**
- Everything in the target `/domains/<scope>/` tree
- All files from Lean Mode
- Domain-specific logic, assets, and `lifecycle/<domain>.md`
- Relies on `domain_routing` metadata in `system_manifest.md` and `load_plans/auto_plan_<scope>.md`

**• Full Mode**  
_Used as a fallback in any of the following conditions:_  
(a) Multiple domains are flagged  
(b) Global counter hits its threshold  
(c) A hash check or integrity audit was requested  

**Loads:**
- The entire cascade (except `evictable`, `temp`, or `expired` files)
- Subject to token cap and pruning rules (e.g., `read_priority: low` gets dropped first)

`load_plans/auto_plan_<scope>.md` is auto-generated at the **end of each WRITE** and consumed here to pick the appropriate mode :contentReference[oaicite:1]{index=1}.

#### 6.1.3 Core Algorithm (pseudo-steps)

1. **Boot**  
   - Read `/cascade/index.md` for the canonical file map.  
   - Always read `loop_protocol.md` to confirm phase sequencing.

2. **Check Counters & Thresholds**  
   - For every `lifecycle/*.md`, compare `Current Count` to its YAML in `file_lifespans.md` :contentReference[oaicite:2]{index=2}.  
   - Decide if a threshold action (e.g., reread domain, audit) is due.

3. **Select Load Mode** (see section 6.1.2 Load Modes above).  
   
4. **Assemble File List**  
   - Begin with mandatory doctrine/immutable files (`system_manifest.md`, etc.).  
   - Append mode-specific files.  
   - Skip any file tagged `read_priority: low` if token headroom < 20 %.  

5. **Integrity Pre-Check (optional)**  
   - If `requires_hash_check: true`, verify SHA-256 against `audit/integrity_snapshot.md`.  
   - Abort READ and switch to **Emergency Recovery** if mismatch.

6. **Record Read Manifest**  
   - Write `/checkpoints/loop_checkpoint.md` line: `READ ✓ | files_loaded: n | mode: X | ts:`.  
   - Include manifest in `job_logs/temp_job.md` for ACT visibility.

#### 6.1.4 Example Load Manifest

```yaml
# job_logs/temp_job.md (excerpt)
read_phase:
  mode: domain
  token_budget: 14K / 32K
  files_loaded:
    - index.md
    - protocols/loop_protocol.md
    - protocols/file_lifespans.md
    - domains/client/index.md
    - domains/client/auth_logic.md
    - lifecycle/client.md
    - load_plans/auto_plan_client.md
```

#### 6.1.5 Safeguards & Fallbacks

- **Token Overflow**  
  → Drop files tagged `read_priority: low`, then drop `rolling` logs if necessary, before halting the READ phase.

- **Hash Mismatch on Immutable File**  
  → Skip ACT phase entirely and escalate to the recovery protocol.

- **Stale Lock (`_locks/active_edit.lock`)**  
  → Abort READ phase immediately and advise manual override or human intervention.

- **Missing Load Plan**  
  → Regenerate an emergency plan in-flight using Lean Mode parameters, then proceed with READ.

#### 6.1.6 Best Practices

- Keep **mode selection deterministic**—if multiple are valid, prefer the one with the **lowest total token cost**.
- Regenerate `load_plans/*.md` **only after** a successful WRITE to prevent infinite recursion loops.
- Store the **total estimated tokens per READ** in `audit/token_summary.md` to monitor footprint over time.
- Lean Mode should **rarely exceed 25%** of the model’s token window—treat this as a **soft budget cap**.

### 6.2 ACT Phase (Write, Summarize, Apply)
 
The ACT phase follows a successful READ and performs the system’s active logic: updating counters, writing summaries, merging files, and triggering downstream planning behaviors — all within defined write-gate policies and integrity constraints.

#### 6.2.1 Goals

1. **Apply changes** based on the prompt’s intent and cascade state.
2. **Write to disk** using rules defined in `write_gates.md`.
3. **Update planning files** if triggers fired during READ or ACT.
4. **Record the state delta** in logs and update checkpoints.
5. **Prepare the system for the next cycle or new external input.**

#### 6.2.2 Write Control Pipeline

The ACT phase uses the following logic to determine what may be written:

1. **Detect Candidate Files**
   - Use domain router and prompt scope to infer affected files.
   - Cross-reference all eligible write targets against `/security/write_gates.md`.
2. **Gate Evaluation**
   - For each file:
     - Is it `writable: true` in its metadata?
     - Does it require a `reason` field or upstream review?
     - Does it need to match a `merge_policy`?
3. **Merge If Necessary**
   - If the file is `mergeable: true` and already exists:
     - Load `merge_policy.md` from the domain or root scope.
     - Resolve and re-write with preserved preamble, unless `overwrite: true`.
4. **Write to Disk**
   - Respect `fileType` and TTL defined in its metadata.
   - Write full content snapshot to:
     - `/temp/` (if ephemeral)
     - `/summary/` or domain folders (if persistent)
     - `/_archive/` for version-stamped historical copies (if `archive_on_write: true`)


#### 6.2.3 Triggers and Reactions

During ACT, various conditions can fire triggers:

| Trigger | Source | Reaction |
|--------|--------|----------|
| `counter == threshold` | `lifecycle/*.md` | Force domain re-plan or summary write |
| `requires_summary == true` | metadata flag | Auto-write summary to `summary/` folder |
| `external_ticket: required` | prompt or system_manifest | Escalate to `/external/escalations.md` |

#### 6.2.4 Logging the ACT Phase

After all writes and merges complete:

```yaml
# job_logs/temp_job.md (excerpt)
act_phase:
  write_targets:
    - domains/client/auth_logic.md
    - lifecycle/client.md
    - summary/client_summary.md
  triggered_replans: 1
  archived_files: 2
  timestamp: 2025-06-25T20:44Z
  post_state_checksum: sha256:abc123...
```
Checkpoint line in `/checkpoints/loop_checkpoint.md`:
ACT ✓ | writes: 3 | merges: 1 | ts: 2025-06-25T20:44Z

#### 6.2.5 Best Practices

- Never write outside gated paths (`security/write_gates.md`).
- Keep summaries under **50 lines** unless explicitly exempted.
- Use `merge_policy.md` to avoid overwriting crucial preambles or footers.
- Regenerate `/load_plans/auto_plan_<scope>.md` only if file lifespans or content warrants.
- Always update counters **after** confirmed ACT writes — not before.

### 7.2 `temp_notes/*` Buffers

`temp_notes/*` serves as a scratchpad system for ephemeral planning, rapid ideation, or staging partial updates before they are committed to domain or rolling files. These files are designed to be volatile and are expected to be purged, merged, or promoted within a short number of cycles.

#### Purpose

- Enable low-stakes planning, hypothesis logging, or speculative modeling
- Temporarily store alternate versions or in-progress drafts
- Provide a writable zone without affecting domain integrity or triggering threshold audits

#### Metadata Header

```markdown
---
file_type: temp
expiration_policy: short-lived
writeable: true
read_priority: low
---
```

#### Rules of Use

- Files in this buffer should **never** be considered a single source of truth
- They may be loaded in Domain or Full Modes only if referenced explicitly in `temp_job.md`
- Not loaded in Lean Mode unless the task explicitly originated from the notes buffer

#### Lifecycle

- Max lifespan should not exceed 3–5 prompt cycles
- Each file should include a timestamp and auto-expiry metadata if available
- May be manually merged into `domains/` or `recent.md` when finalized

#### Example Use Cases

- Brainstorming logic trees or option maps
- Capturing partial API contracts before schema promotion
- Recording unsanctioned experiments or developer journaling

#### Safeguards

- AI must avoid referencing `temp_notes/*` outputs as canonical decisions
- Should never be used to guide irreversible WRITE actions
- Rolling summary logs should *not* record temp\_notes changes unless escalated to official files

#### Best Practices

- Limit each file to a single prompt thread or topic
- Use structured headers and clear expiration cues
- Periodically audit and purge stale entries with `prune_plan.md`

### 7.3 Eviction Policy

Eviction policy governs how and when temporary files, rolling buffers, and short-lived context artifacts are cleaned up to ensure token efficiency, relevance, and memory hygiene within the ContextCascade system.

#### Eviction Triggers

- Lifecycle thresholds reached (defined in `file_lifespans.md`)
- Manual flagging in `temp_job.md`
- Presence of expiration metadata in file headers
- Periodic pruning operations defined in `prune_plan.md`
- Inactivity (number of prompt cycles since last access)

#### File Classes Subject to Eviction

- `temp_notes/*`
- `_taskbuffers/*`
- `load_plans/*.md`
- `job_logs/temp_job.md`
- One-prompt ephemeral files

#### Metadata Used for Eviction

```markdown
---
file_type: temp | buffer | ephemeral
expiration_policy: short-lived | one-prompt | evictable
last_used: YYYY-MM-DDTHH:MM:SSZ
read_priority: low
---
```

#### Eviction Behaviors

- Files marked `expiration_policy: one-prompt` are deleted immediately after WRITE phase
- Files marked `short-lived` are evicted after 3–5 prompts or when no longer referenced in load plans
- Eviction actions are logged to `meta_audit.md`
- Optional dry-run evictions may be tested by simulating threshold crossing

#### Best Practices

- Avoid hard-deleting unless files are confirmed obsolete
- Always log pruning rationale to `prune_plan.md`
- Consider promoting valuable temp file content to `recent.md` or domain files before purge
- Do not evict immutable or protected files regardless of inactivity

### 7.4 Summary Merging Behavior

Summary merging defines how transient updates (e.g., short logs, temp\_notes, changelog items) are collapsed or integrated into long-lived summary files such as `summary.md`, `meta_audit.md`, or domain-specific chronicles. This helps reduce token load while preserving narrative continuity over time.

#### When Merging Is Triggered

- After crossing a defined lifecycle threshold
- When rolling updates contain substantial information tagged `mergeable: true`
- When temp\_notes or recent.md contains summary-worthy content
- When `summary.md` or another long-term doc has a `needs_merge: true` marker

#### Merge Sources

- `change_log/recent.md`
- `temp_notes/*`
- `load_plans/` with finalized plans
- `job_logs/temp_job.md` if marked significant

#### Merge Targets

- `change_log/summary.md`: Event and milestone history
- `meta_audit.md`: Lifespan, counter, or policy enforcement record
- `domains/client/*.md`: If structural guidance was derived from planning

#### Metadata Headers That Enable Merging

```markdown
---
mergeable: true
merge_target: change_log/summary.md
merge_policy: append | squash | integrate
---
```

#### Merge Policies

- **Append**: Directly adds new section at end of file.
- **Squash**: Collapses entries from multiple files into one block.
- **Integrate**: Parses contents into headings/sections of target.

#### Safeguards

- Never merge files that are temporary unless flagged `mergeable`
- AI should verify merge consistency via hash checks if critical
- Job log must state reason for merge and cite source(s)

#### Best Practices

- Use AI-assisted human prompt to approve critical merges
- Timestamp all merge blocks with original file source
- If merging from temp\_notes, include original filename and note context

#### Example Merge Log in Job Plan

```markdown
### Merge Summary
source_files:
  - temp_notes/api_draft_2025.md
  - change_log/recent.md
merged_into: change_log/summary.md
merge_policy: squash
reason: "Captured schema evolution milestone and team discussion"
```

## 8. Job Plans & Trace Audits

### 8.1 Job Plan Format

Job Plans are structured markdown blocks that instruct the AI on the intent, scope, affected files, and safeguards for each major action taken during the ACT → WRITE cycle. These files appear in `job_logs/temp_job.md` and act as short-term trace records that also support pre- and post-execution auditing.

#### Required Structure

```markdown
---
file_type: job_plan
executed_by: ai | human
intent: <description>
timestamp: YYYY-MM-DDTHH:MM:SSZ
---

## Action Summary
- Objective: <clear goal>
- Affected Domains: client | server | schema
- Safeguard Status: passed | conditional | flagged

## Files Affected
- /domains/client/sync_logic.md
- /change_log/recent.md

## Notes
Brief rationale for action and links to upstream context if available.
```

#### Best Practices

- Keep intent concise and verifiable
- Link back to READ phase file list and lifecycle counters
- If plan includes risky writes, flag them for review
- Store temp\_job.md as a rolling job buffer until a summary is committed

#### AI Usage

- AI should parse job plans to confirm write targets
- Use job plan headers to verify that domain routing and lifecycle counting logic were correct
- AI should decline execution if job plan metadata is malformed or critical context is missing

### 8.2 Pre/Post Hash Checking

Pre- and post-hash checking ensures integrity in the file update process by verifying that no unauthorized or unexpected changes have occurred before or after a WRITE phase. This forms part of the safeguard logic embedded in the loop protocol.

#### Purpose

- Validate that files marked as `immutable` or `write_protected` have not been altered.
- Compare SHA-256 hashes from `integrity_snapshot.md` before a WRITE operation and after it completes.
- Allow rollback or halt execution if discrepancies are detected.

#### Workflow

1. **Pre-WRITE Phase**:

   - Load current SHA-256 hash for each file listed in the job plan.
   - Check against latest entries in `audit/integrity_snapshot.md`.
   - If mismatch is found, log warning in `meta_audit.md` and halt WRITE unless overridden.

2. **Post-WRITE Phase**:

   - Recompute file hashes for all affected files.
   - Update `integrity_snapshot.md` only if WRITE was successful and validated.
   - Flag inconsistencies and optionally initiate reversion or additional audit job.

#### Metadata Requirements

```markdown
---
file_type: protected | immutable
requires_hash_check: true
last_verified_hash: <SHA256>
---
```

#### Sample Audit Entry

```markdown
### Integrity Audit Log
file: domains/client/api_logic.md
expected_hash: 74fc...ee21
after_write_hash: 74fc...ee21
status: passed
notes: Auto-validated after domain update
```

#### Best Practices

- Hash-check only for files marked `requires_hash_check: true`
- Store hash audits alongside job plans in the same loop cycle
- Use dry-run jobs to simulate expected hashes and plan effects
- Alert users immediately if immutable files are breached

### 8.3 Write-Back Summary Confirmation

The Write-Back Summary Confirmation phase ensures that all expected changes made during the WRITE phase are successfully committed, verified, and acknowledged in the cascade system. This helps to maintain context integrity and enables future traceability.

#### Objectives

- Confirm that AI-generated edits were correctly written to their target files
- Validate the structure and metadata of updated files
- Log a summary entry to `change_log/recent.md` or `meta_audit.md`
- Perform post-write cleanup or preparation for next loop

#### Confirmation Tasks

1. **File Confirmation**

   - Re-open each file listed in the job plan
   - Verify content changes match expected deltas
   - Check metadata integrity and presence of required headers

2. **Audit Logging**

   - Append a summary block to `change_log/recent.md` or `meta_audit.md`
   - Include write target filenames, timestamp, and outcome status

3. **Domain Counter Sync**

   - Update relevant domain or global counters based on file class and scope
   - Log lifecycle increment reason if applicable

4. **Post-Write Rolling Actions**

   - If rolling updates were included, mark them complete in `temp_job.md`
   - Set `write_confirmed: true` flag to prevent redundant rechecks

#### Example Summary Confirmation Log

```markdown
### Write-Back Summary Confirmation
status: success
files_written:
  - /domains/client/form_logic.md
  - /change_log/recent.md
timestamp: 2025-06-25T11:03:00Z
notes: Completed AI-planned write to client logic, domain counter incremented, rolling summary flushed
```

#### Safeguards

- Abort summary confirmation if hashes mismatch unless manually overridden
- Log any skipped file due to write-protection or error
- Require a corresponding job plan or loop checkpoint to validate context

#### Best Practices

- Always link confirmation logs to the originating `temp_job.md`
- Include affected domains to facilitate audit trail filtering
- For human-assisted sessions, provide prompt guidance to verify summary manually

## 9. Maintenance & Audits

### 9.1 `token_summary.md`
Tracks the estimated token usage across ContextCascade components. Used to identify files or sections that are disproportionately large and need pruning or optimization. Helps prevent token overflow and enables leaner loading protocols.

- **Triggers:** Periodic global lifecycle counter thresholds (e.g., every 10 prompts).
- **Actions:** Suggests pruning of verbose notes or splitting oversized files.
- **Metadata:** Contains last update timestamp, top token contributors.

### 9.2 `integrity_snapshot.md`
Maintains a hash index of critical or immutable files, especially those classified as `immutable`, `protected`, or `doctrine` files.

- **Purpose:** Prevents undetected corruption or unauthorized mutation.
- **Trigger:** Generated or refreshed on a defined lifecycle threshold or after architectural file changes.
- **Contents:** Filename, SHA-256 hash, file type, classification.
- **Verification Process:** Recomputed hashes are compared during WRITE phase if high-risk changes or file drift are detected. A mismatch indicates unauthorized edits.
- **Failsafe:** Optional backup or alert flagging if protected file hash mismatch is detected.

### 9.3 `meta_audit.md`
Logs any drift from metadata expectations: file headers, lifespans, hash mismatch, access violations.

- **Includes:**
  - Mismatched classification vs. directory placement
  - Outdated or malformed metadata headers
  - Files not touched despite lifecycle thresholds being passed
  - Drift in lifecycle activity vs. defined trigger behaviors

### 9.4 `prune_plan.md`
Maintains a deferred cleanup strategy for stale notes, outdated buffers, oversized logs, etc.

- **Trigger:** Token budget warnings or manual/automated review cycles
- **Contents:**
  - Suggested deletions or truncations
  - Rewrites into permanent summaries
  - Eviction priorities across temp classes
  - Rolling buffer flush instructions (e.g., `recent.md` rotation)

### 9.5 Metadata Validator (`validators/metadata_validator.ts`)
A CLI tool or script that validates file headers and embedded metadata for compliance with ContextCascade standards. `<!MUST REVISIT/BUILD THIS ASK CHATGPT!>`

- **Validates:**
  - File class types (e.g., immutable, temp, rolling)
  - Metadata completeness (e.g., purpose, scope, threshold behavior)
  - Write-gate protection markers
  - Hash entries if required
  - Properly declared eviction policy fields
  - Lifecycle ID sync (ensures alignment with counter checkpoints)
  > The validator now enforces the Canonical FileType Registry (§ 3.2.1).  
  > • `fileType` **must** match a registry value.  
  > • If a `subtype` field exists it **must** be one of the allowed aliases for that `fileType`.  
  > • Unknown `fileType` or `subtype` → validation **error**.

## 10. Load Plans & Indexing

### 10.1 `index.md` Purpose
Top-level entrypoint used to define the cascade’s structure and guide initial boot-up logic.

- **Includes:**
  - Links to domain indexes and protocol files
  - Cascade layout and file class summaries
  - AI bootstrapping and cascade traversal instructions
  - Boot order recommendations and read priorities

### 10.2 Domain-Specific Index Files
Each domain (e.g., `client/`, `server/`, `schema/`) contains a local index.

- **Purpose:**
  - Enables selective loading
  - Reduces unnecessary reads during scoped updates

- **Contents:**
  - File list within domain
  - Domain purpose summary
  - Last touched lifecycle ID
  - Associated counter link (if domain-bound lifecycle counter exists)

### 10.3 Auto-Generated `load_plans/`
Temporary, per-prompt loading plans generated in real time based on the active job type and file thresholds.

- **Lifecycle:** Prompt-session only (auto-evicted)
- **Contents:** List of files and order for reading
- **Source:** Derived from thresholds + counters
- **Use:** Helps AI stay lean in READ phase
- **Deletion:** Always deleted post-WRITE unless flagged for checkpointing

## 11. Security Protocols

### 11.1 `security_review.md` (Placeholder)
Reserved for high-sensitivity audits, such as permission elevation or file injection attempts.

- **Future Use:** Will log sensitive action attempts and provide hash trace validation.
- **Activation:** Only generated or updated upon high-risk signal or manual override request

### 11.2 Protected File Write Gates
Explicitly lists protected files (e.g., `doctrine/`, `immutable/`) and under what rules, if any, they can be written to.

- **Format:** Glob patterns, role-based exceptions, conditional write approval workflows.
- **Auto-Enforced:** Via validators and loop safeguards during ACT and WRITE phases

### 11.3 High-Risk Action Logging
Defines criteria for logging high-risk actions (e.g., schema rewrites, counter resets).

- **Outcome:**
  - Forces integrity snapshot
  - Requires manual or AI confirmation
  - Appends to `meta_audit.md`

### 11.4 Write-Gate Glob Patterns
Custom patterns for identifying sensitive files across any directory.

- **Format:** YAML or JSON glob config
- **Enforced In:** `validators/` or custom middleware before writes
- **Examples:** `**/doctrine/**`, `**/immutable/**`, `security/**`

## 12. Temp Files & Eviction Rules

### 12.1 Task Buffers `_taskbuffers/`
Contains rolling prompt-local buffers scoped to individual prompt chains.

- **Eviction Rule:** Cleared after N prompts or successful summary merge.
- **Use Case:** Job plan iterations, debug history
- **Log Behavior:** May temporarily log AI uncertainty or in-flight decisions
- **Metadata:** Should include prompt ID, cascade ref ID, and created timestamp
- **Interaction Note:** AI should treat contents as ephemeral unless checkpointing is triggered

### 12.2 One-Prompt Files
Ephemeral files created for just a single action or response.

- **Examples:** temp_job.md, temp_plan.md
- **Lifecycle:** Evicted immediately after WRITE phase
- **Safety Mechanism:** May back up if write-back fails or response is interrupted
- **Tagging Convention:** Always include `ephemeral=true` in file metadata
- **Interaction Note:** AI should never reference one-prompt files beyond the current job cycle

### 12.3 When to Auto-Delete
Each temp file or buffer class defines:

- **Eviction Policy:** Lifecycle threshold or deletion condition
- **Triggers:** Lifecycle counter matches, token budget breach, explicit job completion
- **Backup:** If marked sensitive, files first summarized or checkpointed before deletion
- **Overrides:** Admin may tag files `hold=true` in metadata to delay deletion
- **Interaction Note:** AI may be required to run a `prune_plan.md` job before proceeding with large new sessions

## 13. Testing & Consistency

### 13.1 Triggering Test Suites
Testing can be triggered through lifecycle checkpoints, manual prompts, or protocol flags. Automated testing ensures schema conformity, file integrity, and structural alignment before proceeding to complex operations.

- **Trigger Sources:** Lifecycle thresholds, schema changes, metadata violations, or audit triggers
- **Tests Include:**
  - Valid metadata headers
  - Proper token load balancing
  - Prompt-safe directory structure
  - Recursive integrity check of immutable files

### 13.2 Schema / UI Snapshots
Schema snapshots capture expected system structure or API/data models at key intervals for regression prevention.

- **Snapshot Contents:**
  - Schema hash
  - Last updated file list
  - Associated domain indexes
- **Usage:**
  - During domain rollouts
  - After schema refactor
  - Before server/infra feature merges

### 13.3 File Integrity Checking
Ongoing checking of content and hash values for all classified files (`immutable`, `doctrine`, `protected`).

- **Tools Used:** `integrity_snapshot.md`, `metadata_validator.ts`
- **Trigger Timing:** WRITE phase completion, rollback detection, high-risk action logging

## 14. Extension Patterns

### 14.1 Adding a New Counter

- **Location:** Add counter file to `/lifecycle/` directory.
- **Metadata:**
  - Name, domain scope
  - Threshold logic
  - Link to affected files or protocols
- **Indexing:** Update `file_lifespans.md` and `index.md`.
- **Optional:** Add logic to metadata validator and domain-level read plans.

### 14.2 New File Class Template

- **Metadata Requirements:**
  - File type (`temp`, `rolling`, `immutable`, etc.)
  - Eviction rules (if any)
  - Threshold count (optional)
  - Domain link
  - Write constraints
- **Suggested Workflow:**
  - Draft template in `temp_notes/`
  - Validate with metadata script
  - Stage with job plan
  - Merge into domain or root as needed

### 14.3 Integrating with External Systems

- **Use Cases:** Deployment logs, CI/CD hooks, ticketing integrations
- **Location:** Mount in `external/` or subdomain directory
- **Metadata Considerations:** Requires file class and authentication mode
- **Loop Integration:** Hook into ACT or WRITE via job plan with `external=true` marker

## 15. Prompt Templates

### 15.1 Session Bootstrap

Used at the beginning of a development session to re-anchor the assistant into the ContextCascade system.

**Example Prompt:**

```
Start by loading the ContextCascade system from /cascade/index.md. Follow the loop protocol in /cascade/protocols/loop_protocol.md. Only act after the full READ phase completes.
```

**Expected AI Behavior:**

- Load index, read plans, and domain indexes
- Read loop protocol and file lifespans
- Initialize checkpoint, counters, and loadPlan

---

### 15.2 Feature Development

Used to introduce a new feature request, functionality enhancement, or bug fix.

**Example Prompt:**

```
I want to add an endpoint for user session validation in the server domain. Plan and apply the changes using ContextCascade. Begin by reading server/index.md and related schema contracts.
```

**Expected AI Behavior:**

- Update domain counters (e.g., server)
- Modify server files within write gates
- Generate job plan, log hashes, checkpoint WRITE phase
- Trigger rolling updates in temp_notes or recent.md

---

### 15.3 Deep Trace Job Plan

Used for long, auditable workflows that touch multiple domains or file systems.

**Example Prompt:**

```
Prepare a deep job trace for refactoring both client and server data handling to support streaming mode. Plan, hash, and checkpoint all relevant steps.
```

**Expected AI Behavior:**

- Increment global and domain counters
- Write detailed temp_job.md plan
- Update loop_checkpoint.md, recent.md
- Reference security/write_gates.md and prune_plan.md as needed
- Append to change_log/summary.md if over threshold

---

### 15.4 Emergency Recovery

Used to regain stability or integrity of the cascade system after a suspected failure or inconsistency.

**Example Prompt:**

```
Emergency mode: scan all hashes in integrity_snapshot.md and recover the last stable cascade. Abort any unsafe writes. Log contradictions to meta_audit.md.
```

**Expected AI Behavior:**

- Skip ACT if integrity drift detected
- Regenerate job plan with audit flag
- Compare recent.md vs summary.md
- Restore snapshot lineage or raise alert
- Lock active_edit.lock if concurrent AI activity is suspected

## 16. Troubleshooting & FAQ

### 16.1 Token Limit Errors

**Symptoms:**

- AI truncates output unexpectedly
- Cascade files are skipped during READ
- WRITE phase does not complete fully

**Causes:**

- Cascade system exceeds context window (~8K or 16K tokens depending on model)
- Accidental inclusion of large markdown/code blocks in rolling logs or domain docs

**Resolution:**

- Use `token_summary.md` to identify bloated files
- Archive stale context to `_archive/` or trim with `prune_plan.md`
- Adjust `file_lifespans.md` to deprioritize non-critical READs
- Consider triggering a soft refresh cycle via prompt:

```
Trigger pruning and partial flush to reduce token budget in next cycle.
```

---

### 16.2 Write-Back Failures

**Symptoms:**

- `temp_job.md` is written but cascade files are not updated
- AI throws validation error at WRITE phase

**Causes:**

- File locked via `active_edit.lock`
- `write_gates.md` blocking file access
- `integrity_snapshot.md` hash mismatch on protected files

**Resolution:**

- Check `security/write_gates.md` for path blocks
- Delete stale lock file at `_locks/active_edit.lock` (with human confirmation)
- Re-run metadata validator to ensure headers are intact
- Trigger WRITE fallback prompt:

```
Retry WRITE phase with verification bypass disabled, and hash logging ON.
```

---

### 16.3 File Not Found

**Symptoms:**

- Prompt references a file the AI cannot locate
- ACT phase throws error during domain route or checkpoint step

**Causes:**

- New file not scaffolded before reference
- Index.md not updated with file link
- Load plan expired or corrupt

**Resolution:**

- Confirm file path exists in `/cascade/index.md` or domain index
- Regenerate load plan:

```
Generate new load plan for [missing_file] and insert into load_plans/ with TTL of 7 cycles.
```

- Check for file in archive or prune log

## Appendix A: Mini Cascade Snapshot

This snapshot illustrates a minimal yet functional ContextCascade setup for early-stage development or lightweight experimentation.

```
/cascade/
├── index.md                     # Root entrypoint with chain order
├── protocols/
│   └── loop_protocol.md         # READ → ACT → WRITE structure
├── lifecycle/
│   └── counter.md               # Global prompt cycle counter
├── change_log/
│   └── recent.md                # Rolling snapshot of updates (max 5 entries)
├── job_logs/
│   └── temp_job.md              # Last job trace & file hashes
├── domains/
│   ├── client/
│   │   └── index.md             # Client index + feature log
│   └── server/
│       └── index.md             # Server index + current endpoints
├── audit/
│   └── token_summary.md         # Token usage snapshot
├── _locks/
│   └── active_edit.lock         # Concurrency guard
```

Key Metadata (Required):

- `fileType`: [immutable | rolling | structural | checkpointed | domain]
- `editPolicy`: [readonly | append | overwrite | evictable]
- `ttlCycles`: <int, optional>

Use this skeleton to rapidly stand up a compliant, AI-ready ContextCascade instance that can grow over time.

## Appendix B: Glossary of Terms

**ACT Phase** – The portion of the loop protocol where the AI interprets loaded context and creates or modifies files before the WRITE phase. It is tightly safeguarded against unauthorized file writes or logic drift.

**Active Edit Lock** – A lock file (`_locks/active_edit.lock`) used to prevent simultaneous write attempts from multiple agents. Must be cleared before WRITE begins.

**Append-Only Log** – A file such as `summary.md` that can only grow by adding content at the end. Used to maintain an untampered history of actions.

**Cascade Chain** – The structured sequence of `.md` files beginning at `index.md` that defines the directional loading, logic, and architecture for the entire context system.

**Checkpoint File** – A file (like `loop_checkpoint.md`) that records the status and outcomes of a completed loop cycle.

**Context Drift** – Occurs when updates are made to files or systems that are inconsistent with earlier logic or metadata. Mitigated by audits and `drift_flag.md` counters.

**Domain Counter** – A file like `lifecycle/client.md` that tracks how often a specific functional area (e.g., client or server) has been touched, triggering selective READs.

**Drift Flag** – A counter file incremented when contradictory behavior or state mismatch is detected. Exceeding thresholds triggers audits or system halt.

**Evictable** – A metadata flag that allows files like `load_plans/*.md` to be deleted after TTL expiry or usage threshold.

**Hash Verification** – A safeguard action that checks stored hash values (typically from `integrity_snapshot.md`) against actual file content to detect tampering.

**Immutable** – A file classification indicating a document that should never change (e.g., `init_context.md`). Backed by hash checking.

**Integrity Snapshot** – A file (`integrity_snapshot.md`) that stores the SHA-256 hashes of all immutable and checkpointed files. Serves as a tamper-detection record.

**Job Plan** – The AI’s detailed execution plan for a change, stored in `temp_job.md`, includes hashes, file targets, and expected outcomes.

**Lifecycle Counter** – A prompt loop tracker that signals when certain files should be reread, pruned, or checkpointed.

**Load Plan** – A file that specifies what documents to READ for a given task. Used to optimize context loading without overloading the model.

**Loop Protocol** – The procedural contract defined in `loop_protocol.md` that structures all AI activity into three repeating phases: READ → ACT → WRITE.

**Metadata Header** – A required JSON block at the top of each file that declares its `fileType`, `purpose`, `editPolicy`, and more.

**READ Phase** – First step in the loop protocol where AI loads all necessary files based on the cascade map, lifespans, and routing logic.

**Rolling Buffer** – A file like `recent.md` that stores the last N actions or events, automatically evicting the oldest entry.

**Rolling Snapshot** – Synonym for a rolling buffer, emphasizing that it offers a window into short-term state.

**Structural File** – A navigational or linking file like `index.md` or any domain-level index used for recursive file discovery.

**TTL (Time To Live)** – A metadata field controlling how many prompt cycles a file should persist before being auto-evicted.

**Write Gate** – A rule in `write_gates.md` that blocks changes to protected paths. Enforced during the WRITE phase to prevent critical file corruption.

**WRITE Phase** – Final step where AI confirms, applies, and logs all changes. Write failures due to locks, hashes, or gates are flagged and rolled back.

**Metadata Validator** – A CLI script used to check metadata conformance and classification tags for every cascade file. Blocks malformed data during validation workflows.

## Appendix C: Change Log of this Documentation

### Version 1.0 – System Initialization

- Established full lifecycle counter logic
- Added core directory layout and file class metadata types
- Introduced domain routing and loop protocol scaffolding
- Implemented READ → ACT → WRITE job plan behavior
- Embedded concurrency safeguards (`active_edit.lock`)

### Version 1.1 – Traceability & Audit Enhancements

- Introduced `loop_checkpoint.md` to enforce cycle tracking
- Created `temp_job.md` for per-prompt job tracing with hash comparison
- Added `summary.md` and `recent.md` dual-log architecture
- Implemented conditional lifecycle counters by domain
- Defined WRITE rollback on drift, token overflow, or gate violation

### Version 1.2 – Security Controls & Validator Tooling

- Defined `write_gates.md` with glob pattern support
- Added `metadata_validator.ts` to enforce file header hygiene
- Implemented `integrity_snapshot.md` for SHA-256-based immutability
- Defined eviction policies using `ttlCycles` in metadata

### Version 1.3 – Prompt Protocols and Bootstrap Templates

- Added prompt templates for bootstrap, trace jobs, feature requests, and recovery
- Codified cascade file refresh timing using lifecycle counters and thresholds
- Populated detailed troubleshooting section

### Version 1.4 – Glossary & Snapshot Completion

- Fully populated glossary of terms
- Added `Appendix A` for minimal scaffold snapshot
- Defined token overflow and write error recovery processes

---

Each section will include file format examples, metadata header requirements, usage notes, and AI prompting best practices.

##
