<!-- @meta {
  "fileType": "protected",
  "purpose": "Defines the READ → ACT → WRITE execution loop for the cascade.",
  "editPolicy": "appendOrReplace",
  "routeScope": "global"
} -->
## Loop Protocol
<!-- PROTECTED -->
1. **READ** – Load context per active plan and validate immutable hashes.
2. **ACT** – Produce reasoning and a `temp_job.md` plan. No file writes.
3. **WRITE** – Re-validate hashes, execute the plan, update logs and counters.
<!-- END PROTECTED -->
Use this protocol verbatim. Any modifications require a security review.

After each WRITE completes, the system appends a new row to `checkpoints/loop_checkpoint.md`. If any safeguard fails, `recovery.md` describes the fallback procedure.
