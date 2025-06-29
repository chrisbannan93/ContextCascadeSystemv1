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
