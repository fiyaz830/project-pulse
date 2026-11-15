# PROJECT_CONTEXT — Project Pulse 2.0

## Mission
Build Pulse Retail's data platform from a hostile vendor API to trustworthy Gold tables and an
AI layer — and become the engineer who can explain every design choice in a product-company
interview.

## Learner
- Senior Data Engineer (Snowflake, Kimball, MERGE-based loads, hash surrogate keys).
- Python: basics (variables, lists, dicts, loops, functions). Prior C++.
- Machine: MacBook, Apple M5, 16 GB RAM. 1 hour/day, every day.
- **Priority:** Python for data engineering first (Phase 0, Weeks 1–6), from the basics, with
  core DE ideas (grain, ETL, duplicates, idempotency, joins) introduced simply along the way.
  Tooling (environments, CI) comes later, in Week 7.
- **Preferred teaching style:** simple, conversational, step by step: plain explanation → tiny
  example with output → small exercise. SQL analogies help; dense jargon doesn't.

## Toolchain (all ₹0, no card, no trial)
| Need | Tool | Licence |
|---|---|---|
| Python env & packaging | uv | Apache-2.0 / MIT |
| Lint / format / types | ruff, mypy | MIT |
| Tests | pytest, hypothesis | MIT / MPL-2.0 |
| Git hooks / secret scan | pre-commit, gitleaks | MIT |
| Processing | PySpark + delta-spark, DuckDB | Apache-2.0 / MIT |
| Source system | FastAPI + uvicorn + Faker (Chaos Mart) | MIT |
| HTTP client | httpx | BSD |
| Validation & contracts | pydantic, pandera, datacontract-cli | MIT |
| Local LLMs & vectors | Ollama, LanceDB or Chroma | MIT / Apache-2.0 |
| CI | GitHub Actions (free for public repos) | — |
| Cloud twin | Databricks Free Edition | free, proprietary |
| Databricks tooling | Databricks CLI + Asset Bundles | free, Databricks licence |

## Databricks Free Edition — known constraints (verify again in Week 12)
- Serverless compute only; small sizes and daily fair-use quotas.
- Outbound internet limited to trusted domains unless verified with LinkedIn → ingestion runs
  locally and files are uploaded to a Unity Catalog Volume.
- One SQL warehouse (2X-Small); max 5 concurrent job tasks; no R/Scala.
- Inactive accounts may be deleted → the repo, not the workspace, is the source of truth.

## Architecture
Phase 0 (Weeks 1–6) is plain Python on small files in `gym/data/`, ending with a mini pipeline
(`raw/ → clean/ → report`) in `src/pulse/mini_pulse/`. The full platform starts in Week 7:
```
Chaos Mart API ──(rate-limited client, local)──▶ landing/ (JSONL + manifest)
        └─▶ Bronze (Delta, append-only, ingest metadata)
              └─▶ Silver (dedup, typed, SCD2, quarantine, contracts)
                    └─▶ Gold (star schema, aggregates)
                          └─▶ AI layer (classification, RAG, text-to-SQL)
Orchestration: Databricks Jobs via bundle (cloud) · `make pipeline` (local)
Ops tables: ops.pipeline_runs, ops.table_audit, ops.dq_results
```
