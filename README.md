# Project Pulse 2.0 — Pulse Retail Data Platform

> A production-style data platform built against a deliberately hostile vendor API.
> This README is written like an operations log: what the system does, what broke, why,
> and what changed so it can't break that way again.

![status](https://img.shields.io/badge/phase-0%20workshop-blue) ![streak](https://img.shields.io/badge/streak-0%20days-orange)

## 1. What this system does
Ingests Pulse Retail's orders, customers, products, payments, refunds, inventory and support
tickets from the Chaos Mart partner API; lands them idempotently; cleans and models them into a
Kimball star schema on Delta Lake; enforces data contracts; and serves an AI layer on top.

## 2. Architecture
See [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md#architecture) and [`docs/adr/`](docs/adr/).

## 3. Service levels (targets)
| Table | Freshness | Completeness | Owner |
|---|---|---|---|
| `gold.fact_order_line` | < 24 h | reconciles to source ±0 rows | Shaik |
| _add as tables ship_ | | | |

## 4. Incident log
Every significant failure — real or drilled — gets a report in [`incidents/`](incidents/).

| ID | Date | Severity | Title | Root cause (one line) | Prevention shipped |
|---|---|---|---|---|---|
| _INC-001_ | | | | | |

## 5. Known risks and open problems
- _What could break this platform today that isn't fixed yet?_

## 6. Runbooks
How to rerun, backfill, recover and rotate secrets: [`docs/runbooks/`](docs/runbooks/).

## 7. Run it
```bash
uv sync
uv run pytest
uv run python -m sources.chaos_mart.server   # vendor sandbox (from Week 1)
make pipeline                                # end-to-end local run (from Phase 2)
```

## 8. Learning log
Daily journal in [`journal/`](journal/) · scores in [`assessments/scores.csv`](assessments/scores.csv)
· progress in [`PROGRESS.md`](PROGRESS.md).
