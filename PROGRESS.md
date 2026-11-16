# PROGRESS — Project Pulse 2.0

> Single source of truth. Updated by the tutor at every `/wrap`. Edit freely if it drifts.

## Now
- **Phase:** 0 — Python for Data Engineering
- **Week:** 1  ·  **Day:** 2 done (Mon 16 Nov). Next session = W1 D3, Tue 17 Nov 2026: dicts (one order as a dict, `.get()`, missing keys)
- **Streak:** 2 days  ·  **Longest streak:** 2
- **Open thread:** 2-minute warm-up on rounding with `{x:.0f}` (2.5 and 3.5), then dicts
- **Note (15 Nov 2026):** curriculum restructured to be Python-first with a simpler teaching
  style. The environment/tooling week moved to Week 7.

## Phase gates
| Phase | Theme | Weeks | Exam | DoD | Incident | Status |
|---|---|---|---|---|---|---|
| 0 | Python for Data Engineering | 1–6 | | ☐ | — | ⏳ |
| 1 | The Workshop (env, tooling, CI) | 7 | — | ☐ | — | 🔒 |
| 2 | Hostile ingestion | 8–10 | | ☐ | ☐ | 🔒 |
| 3 | Bronze | 11–12 | | ☐ | ☐ | 🔒 |
| 4 | Silver | 13–16 | | ☐ | ☐ | 🔒 |
| 5 | Gold & storage | 17–19 | | ☐ | ☐ | 🔒 |
| 6 | Orchestration, secrets, CI/CD | 20–22 | | ☐ | ☐ | 🔒 |
| 7 | Lineage & observability | 23–24 | | ☐ | ☐ | 🔒 |
| 8 | AI layer | 25–29 | | ☐ | ☐ | 🔒 |
| 9 | Capstone | 30 | | ☐ | ☐ | 🔒 |

## Concepts owned (can explain to an interviewer)
- Variable vs `print` (a variable stores a value, `print` shows it)
- Basic f-strings
- Lists: `len`, `sum`, `min`, `max`
- Indexing from 0 (including `[-1]`) and slicing with the end excluded (`[0:3]`)
- An out-of-range index raises a loud `IndexError`
- Average from `sum` and `len`

## Weak spots (revisit in Sunday quizzes)
- f-string number formatting `:,.2f`: used correctly in D2, but he is vague on what `f` means (fixed-point)
  and on rounding (Python rounds halves to even: 4250.5 gives 4,250, 4251.5 gives 4,252)
- Silent bad data: `qty = 0` or a negative price runs without any error. Empty list also not yet considered
  (`min([])` raises ValueError; the average divides by zero)
- A slice returns a list, so it can't be formatted with `:,.2f` directly (loops on W1 D4 fix this)
- Finishing the last 10% (D1: unused `gst`; D2: unformatted slice line). Improving: he checked against the checklist on D2

## Parking lot (ideas for later — don't chase them today)
- Indian-style digit grouping (₹1,09,563.00). Python's `,` gives Western grouping only.
