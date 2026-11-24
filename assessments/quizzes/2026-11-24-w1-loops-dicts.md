# Quiz — 2026-11-24 — W1: dicts, loops, counting, grain (6 questions)

| # | Topic | Question (short) | His answer | Verdict |
|---|---|---|---|---|
| 1 | Dict write | `d["amount"] = 500` on a dict without that key: what prints? | C `{'city': 'salto', 'amount': 500}` | Correct |
| 2 | Counting per group | `counts[c] = counts.get(c, 0) + 1` over `["pune", "goa", "pune"]` | B `{'pune': 2, 'goa': 1}` | Correct |
| 3 | `if` in a loop, boundary | count of `a > 1000` in `[1000, 1500, 800, 1000]` | B `1` | Correct |
| 4 | Empty list | sum loop then `min([])` on an empty list | A (prints `₹0.00`, then `0`) | **Wrong** — correct: B (prints `₹0.00`, then `ValueError`) |
| 5 | Grain | grain of `orders` vs `city_counts` | B (order vs city) | Correct |
| 6 | Where code lives | `total = 0` placed inside the loop | B `300` | Correct |

**Score:** 5 / 6

**Tutor notes:** Dict read vs write and counting per group are now solid (Q1, Q2). The one miss is the same area as the D5 "fail?" answer: an empty list. A sum loop is quiet on an empty list (0), but `min([])` raises `ValueError` and an average divides by zero. Revisit in the Saturday drill and the Sunday quiz.
