# PROJECT_CONTEXT — Project Pulse 2.0

## Mission
Build Pulse Retail's data platform from a hostile vendor API to trustworthy Gold tables and an
AI layer — and become the engineer who can explain every design choice in a product-company
interview.

## Learner
- Senior Data Engineer (Snowflake, Kimball, MERGE-based loads, hash surrogate keys).
- Python: basics (variables, lists, dicts, loops, functions). Prior C++.
- Machine: MacBook, Apple M5, 16 GB RAM. 1 hour/day, every day.

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

## Databricks Free Edition — known constraints (verify again in Week 6)
- Serverless compute only; small sizes and daily fair-use quotas.
- Outbound internet limited to trusted domains unless verified with LinkedIn → ingestion runs
  locally and files are uploaded to a Unity Catalog Volume.
- One SQL warehouse (2X-Small); max 5 concurrent job tasks; no R/Scala.
- Inactive accounts may be deleted → the repo, not the workspace, is the source of truth.

## Architecture
```
Chaos Mart API ──(rate-limited client, local)──▶ landing/ (JSONL + manifest)
        └─▶ Bronze (Delta, append-only, ingest metadata)
              └─▶ Silver (dedup, typed, SCD2, quarantine, contracts)
                    └─▶ Gold (star schema, aggregates)
                          └─▶ AI layer (classification, RAG, text-to-SQL)
Orchestration: Databricks Jobs via bundle (cloud) · `make pipeline` (local)
Ops tables: ops.pipeline_runs, ops.table_audit, ops.dq_results
```
