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
