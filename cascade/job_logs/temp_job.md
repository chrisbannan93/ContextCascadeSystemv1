<!-- @meta {
  "fileType": "temporary",
  "subtype": "job_plan",
  "purpose": "Ephemeral WRITE-phase job plan; exists for one loop to coordinate file mutations and safety checks.",
  "editPolicy": "appendOrReplace",
  "ttlCycles": 1,
  "routeScope": "global",
  "mergeTarget": "job_logs/recent.md"
} -->

### /cascade/job_logs/temp_job.md

> **Role:** Working job blueprint for the **current** loop.  
> It records intended edits, pre-hashes, expected post-hashes, and any escalation flags.  
> Once WRITE succeeds, a condensed summary of this file is appended to `job_logs/recent.md`;  
> the file is then overwritten in the next loop (TTL = 1).

---

#### 1 · Intent

| Job ID | Motivation / Prompt Summary                              |
|--------|----------------------------------------------------------|
| `J-000`| _<< auto-generated at ACT time >>_                       |

---

#### 2 · Planned Actions

| Step | Action Type   | Target Path(s)                     | Notes / Hash Before |
|------|---------------|------------------------------------|---------------------|
| 1    | overwrite     | `lifecycle/client.md`              | `sha256:xxxx`       |
| 2    | append        | `change_log/recent.md`             | `sha256:yyyy`       |
| 3    | merge         | `change_log/recent → summary.md`   | n/a                 |

*(Rows populated automatically by ACT‐phase planning logic.)*

---

#### 3 · Safety & Escalation Flags

| Flag              | Value | Description                                  |
|-------------------|-------|----------------------------------------------|
| `writeGated`      | false | true → blocks WRITE until manual approval    |
| `requiresReview`  | false | true → security review needed                |
| `forceMerge`      | true  | force flush of change_log/recent.md          |

---

#### 4 · Post-Write Verification

| Target Path                  | Expected Hash After | Actual Hash | Status |
|------------------------------|---------------------|-------------|--------|
| `lifecycle/client.md`        | `sha256:zzzz`       | _TBD_       | _TBD_  |
| `change_log/recent.md`       | `sha256:aaaa`       | _TBD_       | _TBD_  |

*(Filled by WRITE controller; mismatches raise drift flag.)*

---

#### 5 · Outcome & Checkpoint

- **WRITE result:** _pending_  
- **Checkpoint to append:** `/checkpoints/loop_checkpoint.md` if success.  
- **Failure path:** log to `/audit/meta_audit.md`, raise drift, retain this file for diagnosis.

---

**Note:**  
This file should never be committed to long-term storage.  
Its sole purpose is to provide a transparent, auditable plan for the **current** WRITE cycle, then yield a summary line for permanent logs.
