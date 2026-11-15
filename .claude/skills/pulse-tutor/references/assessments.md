# Assessments

All assessments are saved under `assessments/` with his answers, and scored into
`assessments/scores.csv` (`date,type,topic,score,max,notes`).

## Phase 0 adjustments (Weeks 1–6)

- Quizzes: 6 questions (Sunday: 8). Types: "what does this code print?", "which line has the
  bug?", "which Python tool fits this job?", and simple DE ideas (grain, duplicates, ETL).
- Explanations after each answer are short and friendly; show the correct code's output.
- Challenges: 15–20 minutes, pure Python only (pandas allowed from Week 5), one small function
  with 3–5 tests.
- Phase 0 exam: 12 MCQs + 1 challenge (20 min) + 1 "explain it simply" written question
  (e.g. "explain to a new joiner what grain means, with an example"). Pass mark 80%.

## `/quiz` — MCQs

- Default 8 questions on the current week; on Sunday 10 questions = 7 this week + 3 spaced-repetition
  questions on items listed under *Weak spots* in PROGRESS.md.
- Ask **one question at a time**. Wait for his answer before revealing.
- Mix of types: concept, "what does this output", "which design fails and why", "spot the bug",
  "what is the grain".
- Distractors must be plausible mistakes a real engineer makes (e.g. "use DISTINCT to fix the
  duplicates" as a wrong option for a fan-out question).
- After each answer: correct/incorrect + a 2–3 line explanation + the production consequence.
- Save to `assessments/quizzes/YYYY-MM-DD-<topic>.md` with question, his answer, verdict.

## `/challenge` — coding challenge

- 20–30 minutes. Write the brief to `assessments/challenges/YYYY-MM-DD-<slug>/README.md` with:
  scenario, input fixture (small, nasty), expected behaviour, constraints, time box.
- Provide failing tests in the same folder (`test_challenge.py`). He writes `solution.py`.
- Grade on: correctness (tests), edge cases, idempotency, readability, complexity. Score /10.
- Rotate types: Python (pure), PySpark transformation, SQL (window/grain/join), debugging a broken
  pipeline, design-on-paper (write an ADR in 20 min).

## Sunday weekly review

1. Quiz (10 MCQs, as above).
2. Challenge (one, 25 min).
3. Retro: what went well / what was hard / one thing to change next week.
4. Update streak, scores and *Weak spots*; announce next week's theme with a teaser.

## Phase exams (last Sunday of a phase)

- 15 MCQs + 1 challenge + 1 "explain it to an interviewer" verbal question (he answers in writing,
  you grade like a hiring panel: strong hire / hire / lean no / no).
- Pass mark 80%. Record the result in PROGRESS.md Phase table.
