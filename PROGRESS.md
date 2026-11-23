# PROGRESS — Project Pulse 2.0

> Single source of truth. Updated by the tutor at every `/wrap`. Edit freely if it drifts.

## Now
- **Phase:** 0 — Python for Data Engineering
- **Week:** 1  ·  **Day:** 4 done (Mon 23 Nov). Next session = W1 D5: `if`/`else` inside loops: total revenue, orders above ₹1,000, count per city
- **Streak:** 1 day (restarted; 20-22 Nov missed)  ·  **Longest streak:** 2
- **Open thread:** 2-minute warm-up: which of `d["k"]`, `d.get("k")`, `d["k"] = v` can raise KeyError and why, plus what `for o in orders:` loops over (the list). Then `if`/`else` in loops
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
- A dict is one row (keys = column names); read a value with `d["key"]`
- `.get(key)` returns `None` and `.get(key, default)` returns the fallback only when the key is missing; `.get()` never stores anything
- Adding a key with `d["key"] = value`
- `.get()` can hide a missing-data problem (silent bad data)
- `.0f` rounds halves to even (2.5 → 2, 3.5 → 4, 4.5 → 4)
- A list of dicts is a table (one dict = one row); `for o in orders:` gives the next row each round
- Code before a loop runs once, inside runs once per row, after runs once; an empty list leaves `total` at 0 so it prints `₹0.00`
- Loud failure (TypeError, KeyError) vs silent failure (wrong type in an f-string, `None`, negative amount)
- CI basics: `ci.yml` runs on `git push`; `ruff check` finds rule breaks, `ruff format` rewrites style; `uv` and `ruff` are programs, not libraries

## Weak spots (revisit in Sunday quizzes)
- f-string number formatting `:,.2f`: used correctly in D2, but he is vague on what `f` means (fixed-point)
  and on rounding (Python rounds halves to even: 4250.5 gives 4,250, 4251.5 gives 4,252)
- Silent bad data: `qty = 0` or a negative price runs without any error. Empty list also not yet considered
  (`min([])` raises ValueError; the average divides by zero)
- Dict read vs write: `d["k"]` (read) raises KeyError if missing; `d["k"] = v` (write) creates the key and never raises KeyError. He said the write could crash on D3 and again in the D4 warm-up; got `box["bag"]` right after the notice-board analogy. Re-test in the next warm-up
- Rounding: now correct (2, 4, 4 on D4 warm-up); re-check in the Sunday quiz
- "Loop over the list, not the dict": said "dictionary" first on D4
- Run `uv run ruff format . && uv run ruff check .` before committing (D3 CI failed on E501 and format)
- A slice returns a list, so it can't be formatted with `:,.2f` directly (loops on W1 D4 fix this)
- Finishing the last 10% (D1: unused `gst`; D2: unformatted slice line). Improving: he checked against the checklist on D2

## Parking lot (ideas for later — don't chase them today)
- Indian-style digit grouping (₹1,09,563.00). Python's `,` gives Western grouping only.
