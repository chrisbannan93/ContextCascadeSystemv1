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
