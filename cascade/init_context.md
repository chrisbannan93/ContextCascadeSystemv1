<!-- @meta {
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
