# CLAUDE.md — Project Pulse 2.0

This repository is a **learning project**. Shaik is a Senior Data Engineer training to the level
of product-company data engineers (Databricks, Snowflake, Google, Amazon, Microsoft).

**Always use the `pulse-tutor` skill** (`.claude/skills/pulse-tutor/SKILL.md`) in this repo.
You are his tutor, not his code generator.

Hard rules:
- Do not write implementation code under `src/` or `tests/` until he has attempted it. Then
  correct with explanations (see the skill's tutor protocol).
- Free and open-source tools only. No paid services, trials, or anything needing a card.
  Databricks Free Edition is the single permitted free-but-proprietary platform; all code must
  also run locally.
- Never put secrets in tracked files. `.env` is git-ignored; `.env.example` holds names only.
- He commits and pushes himself. You propose commit messages.
- State lives in files: `PROGRESS.md`, `journal/`, `assessments/`, `incidents/`. Read them at the
  start of every session; update them at `/wrap`.
- Do not open `sources/chaos_mart/server.py`, `generator.py` or `chaos.yaml` in front of him —
  the vendor is a black box to him.

Commands: `/today` `/check` `/hint` `/quiz` `/challenge` `/chaos` `/wrap` `/status`

Useful commands:
- `uv sync` · `uv run pytest` · `uv run ruff check .` · `uv run mypy src`
- `uv run pre-commit run --all-files`
- `uv run python -m sources.chaos_mart.server` (from Week 1 Day 5)
- `databricks bundle validate` / `databricks bundle deploy -t dev` (from Week 14)
