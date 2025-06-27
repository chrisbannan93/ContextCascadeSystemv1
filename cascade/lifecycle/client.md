<!-- @meta {
  "fileType": "counter",
  "purpose": "Tracks WRITE-phase activity across all client-domain files (UI, session, interface).",
  "editPolicy": "incrementOnly",
  "routeScope": "client",
  "created": "2025-06-27T00:00:00Z"
} -->

### /cascade/lifecycle/client.md

> **Role:** Tracks cumulative WRITE activity in the client domain.  
> Used during ACT to determine whether to reread front-end context, prune stale buffers, or merge rolling logs into durable summaries.

---

#### Tick Count  
`0`

---

#### Update Log (latest first)

| Cycle Δ | Timestamp (UTC) | Affected Files or Reason       |
|---------|-----------------|--------------------------------|
| —       | —               | Counter initialized            |

---

#### Threshold Linkage

| Trigger Type      | Threshold | Outcome When Met                            |
|-------------------|-----------|---------------------------------------------|
| `reread_threshold`| **3**     | Rehydrate client context on next READ       |
| `prune_threshold` | **5**     | Delete expired UI buffers and temp notes    |
| `merge_threshold` | **8**     | Collapse short-term UI logs into summary    |

Thresholds resolved via `/protocols/file_lifespans.md`.

---

#### Maintenance Policy

- Ticks must only increment via the loop WRITE controller.  
- Manual edits are prohibited and will trigger `/lifecycle/drift_flag.md`.  
- Audit trail is mandatory for each tick event (see Update Log).  
- Resetting the counter requires a validated job plan.

---

**Summary:**  
This counter governs lifecycle hygiene for the client domain.  
Its values directly influence how often UI state is refreshed, compacted, or cleaned.
