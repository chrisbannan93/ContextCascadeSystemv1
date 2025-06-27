<!-- @meta {
  "fileType": "append-only",
  "subtype": "review",
  "purpose": "Append-only ledger of all security reviews triggered by gate violations, hash mismatches, or high-risk WRITE events.",
  "editPolicy": "appendOnly",
  "routeScope": "security",
  "linkedAudits": ["audit/meta_audit.md"]
} -->

### /cascade/security/security_review.md

> **Role:** Captures every security-related incident that requires human or elevated AI review.  
> Each row documents the trigger, investigation notes, reviewer, and outcome.

---

#### Review Log  (append-only)

| Timestamp (UTC)        | Trigger Source / File             | Issue Summary                           | Reviewer | Resolution |
|------------------------|-----------------------------------|-----------------------------------------|----------|-----------|
| _none yet_             | —                                 | _Log initialised_                       | system   | n/a       |

_Add new rows at the **bottom**; never modify existing entries._

---

#### Common Triggers

1. **Write-Gate Breach** — attempt to modify a protected/immutable path.  
2. **Hash Mismatch** — immutable file fails pre- or post-WRITE hash check.  
3. **Manual Counter Edit** — any `lifecycle/*.md` counter edited outside loop logic.  
4. **Skipped Threshold Action** — required merge/prune/reload not queued.  
5. **Credential Schema Change** — auth/secret files altered without review flag.

---

#### Review Protocol

1. **Log Entry**: ACT/AUDIT appends a row here and `/audit/meta_audit.md`.  
2. **Investigation**: reviewer inspects job plan, diffs, and metadata.  
3. **Disposition**: update the log row’s *Resolution* field with one of:  
   - `cleared` — no breach; loop may resume.  
   - `patched` — issue fixed; follow-up actions complete.  
   - `flagged` — needs deeper audit; WRITE gated.  
   - `frozen` — domain locked; emergency rollback initiated.  
4. **Close-Out**: if `flagged` or `frozen`, create a job plan for remediation and note its Job ID.

---

#### Enforcement Hooks

- Presence of an **unresolved** (`flagged` / `frozen`) entry halts further WRITE cycles.  
- Resolution status is re-checked at loop start (`enforce_integrity_phase`).  
- All edits to this file are verified against append-only policy by `metadata_validator.ts`.

---

**Summary**  
`security_review.md` provides a permanent, tamper-evident chain of custody for every security incident in the cascade. Maintain strict append-only discipline and ensure each row is fully resolved before normal operations continue.
