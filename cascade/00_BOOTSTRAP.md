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
