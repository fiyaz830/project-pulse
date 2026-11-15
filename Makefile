.PHONY: setup test lint check vendor pipeline
setup:  ## install everything
	uv sync --all-groups && uv run pre-commit install
test:
	uv run pytest
lint:
	uv run ruff check . && uv run ruff format --check . && uv run mypy src
check: lint test
vendor: ## start the Chaos Mart sandbox (from Week 7 Day 5)
	uv run python -m sources.chaos_mart.server
pipeline: ## end-to-end local run (you build this in Phase 3+)
	@echo "Not built yet — that's your job."
