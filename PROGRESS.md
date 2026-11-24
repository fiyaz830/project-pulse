# PROGRESS — Project Pulse 2.0

> Single source of truth. Updated by the tutor at every `/wrap`. Edit freely if it drifts.

## Now
- **Phase:** 0 — Python for Data Engineering
- **Week:** 1  ·  **Day:** 5 done (Tue 24 Nov). Next session = Saturday drill (data detective: duplicate, missing amount and negative amount in a list of orders). If he runs `/today` on Wed 25 or Thu 26 Nov, offer to start the Sat drill early or run W1 review
- **Streak:** 2 days  ·  **Longest streak:** 2
- **Open thread:** short warm-up: in `x = d["a"]` vs `d["b"] = 5`, which is a read and which is a write, and which can raise KeyError? What is `city_counts` if `orders = []`? Then the drill
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
- `if`/`else` inside a loop asks the question again for every row; a counter starts at 0 before the loop; `>` leaves out the boundary value (an order of exactly ₹1,000 is not "above 1,000")
- Counting per group: `counts[k] = counts.get(k, 0) + 1` (read the old count or 0, add 1, write it back) ≈ `GROUP BY k, COUNT(*)`; the grain changes from one order to one city
- `d["k"]` raises KeyError when missing (read); a key holding `None` is kept and counted silently (silent bad data); an empty list doesn't crash, it gives `₹0.00` and `{}`
- CI basics: `ci.yml` runs on `git push`; `ruff check` finds rule breaks, `ruff format` rewrites style; `uv` and `ruff` are programs, not libraries

## Weak spots (revisit in Sunday quizzes)
- f-string number formatting `:,.2f`: used correctly in D2, but he is vague on what `f` means (fixed-point)
  and on rounding (Python rounds halves to even: 4250.5 gives 4,250, 4251.5 gives 4,252)
- Silent bad data: `qty = 0` or a negative price runs without any error. Empty list also not yet considered
  (`min([])` raises ValueError; the average divides by zero)
- Dict read vs write: `d["k"]` (read) raises KeyError if missing; `d["k"] = v` (write) creates the key and never raises KeyError. Wrong on D3 and D4; correct in the D5 warm-up, but on D5 he again thought `city = o["city"]` could create a key. Rule: a dict on the right of `=` is a read, on the left is a write. Re-test in the next warm-up and the Sunday quiz
- Rounding: now correct (2, 4, 4 on D4 warm-up); re-check in the Sunday quiz
- "Loop over the list, not the dict": said "dictionary" first on D4, and "list of dictionaries" / "traverse through dictionary" on D5. `o` is one dict; the loop is over the list
- Empty list: he guessed "fail?" on D5 (it doesn't crash; it gives zero results). Re-check with `min([])` and an average in the Saturday drill
- Counting per group `counts.get(k, 0) + 1`: needed a second explanation (tally sheet); re-test with a different field in the Sunday quiz
- Run `uv run ruff format . && uv run ruff check .` before committing (D3 CI failed on E501 and format)
- A slice returns a list, so it can't be formatted with `:,.2f` directly (loops on W1 D4 fix this)
- Finishing the last 10% (D1: unused `gst`; D2: unformatted slice line). Improving: he checked against the checklist on D2

## Parking lot (ideas for later — don't chase them today)
- Indian-style digit grouping (₹1,09,563.00). Python's `,` gives Western grouping only.
