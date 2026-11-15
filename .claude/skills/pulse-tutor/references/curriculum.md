# Project Pulse 2.0 — Curriculum (24 weeks, 1 hour/day)

Domain: **Pulse Retail**, an Indian e-commerce company. Source system: **Chaos Mart**, a
vendor REST API that rate-limits, lies in its docs, sends duplicates, drifts schemas and
delivers late. Target: Delta Lake Bronze/Silver/Gold, locally (PySpark + delta-spark) and on
Databricks Free Edition.

Entities: customers, products, orders (header), order_lines, payments, refunds,
inventory_snapshots, support_tickets (free text — feeds the AI phase).

Each week: 5 build days (Mon–Fri), chaos drill (Sat), assessment + retro (Sun).
"Py:" = Python concepts the build forces (the daily gym drills these).

---

## Phase 0 — The Workshop (Week 1)

**W1 · Production habits from line one**
- Build: repo from the scaffold, `uv` env, ruff + mypy + pytest + pre-commit, first CI run green,
  `src/pulse/common/logging.py` (structured JSON logs), `src/pulse/config/settings.py`
  (typed config from env, no secrets in code).
- Concepts: reproducible environments, lockfiles, trunk-based git, Conventional Commits, CI as gate.
- Py: modules & packages, `pathlib`, f-strings, type hints, `logging`, `if __name__ == "__main__"`.
- Day 5: tutor generates the Chaos Mart vendor server in `sources/chaos_mart/` (he must NOT read
  the server code — treat it as a third party; he only gets `API_DOCS.md`).
- DoD: `uv run pytest` passes; pre-commit blocks a fake secret; CI green on GitHub.

## Phase 1 — Ingestion under hostile conditions (Weeks 2–4)

**W2 · Talking to an API that hates you**
- Build: `ingestion/client.py` — paginated client (cursor + page), timeouts, typed responses.
- Concepts: HTTP semantics, status codes, idempotent vs non-idempotent verbs, pagination styles,
  why `requests.get(url)` with no timeout is a production incident.
- Py: functions in depth, default args trap, exceptions & custom exception hierarchy, `httpx`.

**W3 · Rate limits, retries and backpressure**
- Build: retry with exponential backoff + full jitter, honour `Retry-After`, client-side token
  bucket, circuit breaker, max-attempt budget; tests with a fake transport.
- Concepts: 429 vs 503, thundering herd, retry storms, at-least-once delivery, why retries create
  duplicates (sets up Silver).
- Py: decorators, closures, `time.monotonic`, generators for pagination, `dataclasses`.

**W4 · Landing zone you can rerun 100 times**
- Build: deterministic landing paths (`raw/<entity>/ingest_date=/batch_id=/part-0000.jsonl`),
  manifest file per batch, checkpoint/watermark state, crash-and-resume test.
- Concepts: idempotency, exactly-once illusions, high-watermark vs CDC, atomic writes
  (write temp → rename), backfills.
- Py: context managers, `json` streaming, `hashlib`, `tempfile`, `os.replace`.
- **Phase 1 exam + INC-001** (written from the Saturday drill).

## Phase 2 — Bronze: keep everything, trust nothing (Weeks 5–6)

**W5 · Spark and Delta from first principles**
- Build: local PySpark + delta-spark session factory; Bronze writer adding `_ingest_ts`,
  `_batch_id`, `_source_file`, `_record_hash`; schema-on-read with `_rescued_data`-style column.
- Concepts: lazy evaluation, DAGs, narrow vs wide transforms, Delta log, ACID on object storage,
  time travel.
- Py: classes, `@classmethod`, typing `Protocol`, dependency injection for testability.

**W6 · Idempotent Bronze and the cloud twin**
- Build: rerun-safe Bronze load (`replaceWhere` on batch vs MERGE on record hash — he must argue
  which and why); upload landing files to a Unity Catalog Volume; same code runs on Databricks
  serverless; Auto Loader version for comparison.
- Concepts: append vs overwrite vs MERGE semantics, Auto Loader checkpoints, schema evolution modes.
- Py: packaging (`pyproject`, wheel), environment-aware config.
- **Phase 2 exam + INC-002.**

## Phase 3 — Silver: assume the source is garbage (Weeks 7–10)

**W7 · Grain, keys and duplicates**
- Build: declare grain for every Silver table in `docs/grain.md`; dedupe with window functions
  (latest by event time, tie-break by ingest time); hash surrogate keys.
- Concepts: natural vs surrogate keys, grain statements, `ROW_NUMBER` vs `QUALIFY`, deterministic
  tie-breaking.
- Py: `functools`, `itertools`, sorting with keys — then the Spark equivalent.

**W8 · Quarantine, not crash**
- Build: validation rules → valid rows to Silver, invalid rows to `silver.quarantine_<entity>` with
  reason codes; nothing silently dropped; reconciliation counts (in = out + quarantined).
- Concepts: dead-letter queues, error budgets, null semantics, three-valued logic, type coercion traps.
- Py: `Enum`, `pydantic` models for row validation, `pytest.mark.parametrize`.

**W9 · Time is a liar**
- Build: timezone normalisation (IST vs UTC vs naive), late-arriving data with a lookback window,
  out-of-order updates, SCD Type 2 for customers with MERGE.
- Concepts: event time vs processing time, watermarks, SCD1/2/3, effective dating, current flag bugs.
- Py: `datetime`/`zoneinfo` pitfalls, `hypothesis` property-based tests.

**W10 · Data contracts and automated quality**
- Build: `contracts/*.yaml` (open data contract standard via `datacontract-cli`), `pandera`
  schemas, a `quality/` runner that fails the pipeline on contract breach and warns on drift;
  DQ results written to an audit table.
- Concepts: producer/consumer contracts, schema drift handling policies, freshness/volume/
  distribution checks, blocking vs warning checks.
- Py: writing a small reusable library, `abc`, plugin registration pattern.
- **Phase 3 exam + INC-003.**

## Phase 4 — Gold: dimensional modelling that survives interviews (Weeks 11–13)

**W11 · Star schema for real**
- Build: `dim_customer` (SCD2), `dim_product`, `dim_date`, `fact_order_line` at stated grain;
  late-arriving dimension handling (inferred members / unknown key -1).
- Concepts: Kimball bus matrix, conformed dimensions, degenerate dimensions, factless facts.

**W12 · Join traps and metric correctness**
- Build: `fact_daily_sales` aggregate; tests that prove no fan-out (row-count and sum invariants
  before/after every join); payments vs orders reconciliation.
- Concepts: fan trap, chasm trap, many-to-many bridges, double counting, additive/semi-additive/
  non-additive measures, as-of joins.
- Py: pandas vs Spark mental models, vectorisation, why loops over rows are a smell.

**W13 · Storage and partitioning strategy**
- Build: benchmark notebook: partitioned vs liquid clustering vs Z-order on the same fact;
  small-file problem reproduced then fixed with OPTIMIZE; VACUUM + retention; write an ADR.
- Concepts: file sizing, data skipping, partition cardinality, skew and salting, AQE, broadcast joins.
- **Phase 4 exam + INC-004.**

## Phase 5 — Production orchestration, secrets and CI/CD (Weeks 14–16)

**W14 · Orchestration as code**
- Build: Databricks Asset Bundle (`databricks.yml`) defining a multi-task job: ingest → bronze →
  silver → quality gate → gold; task retries, timeouts, parameters (`run_date`), run-level batch_id.
- Concepts: DAG design, task idempotency, retries vs re-runs, SLAs, alerting.

**W15 · Backfills, reruns and secrets**
- Build: backfill command for a date range that is safe to run twice; secrets via env + local
  `.env` (git-ignored) and Databricks secret scopes if available in Free Edition (verify — if not,
  document the fallback in an ADR); `gitleaks` in pre-commit and CI.
- Concepts: least privilege, secret rotation, config layering (defaults → env → runtime params).

**W16 · CI/CD pipeline**
- Build: GitHub Actions: lint → type-check → unit tests → data-quality tests on fixture data →
  `bundle validate`; branch protection on main.
- Concepts: test pyramid for data, fixture data design, environment promotion (dev → prod targets).
- **Phase 5 exam + INC-005.**

## Phase 6 — Lineage, metadata and observability (Weeks 17–18)

**W17 · Know where every number came from**
- Build: `ops.pipeline_runs` and `ops.table_audit` tables (run id, rows in/out/quarantined,
  duration, git sha); column-level lineage doc for one Gold metric back to the API field;
  compare with Unity Catalog lineage on Databricks.
- Concepts: technical vs business lineage, OpenLineage event model, metadata as a product.

**W18 · Observability and the incident-report README**
- Build: freshness and volume anomaly checks; a Gold "pipeline health" table; README rewritten as
  the platform's incident log and operating guide.
- **Phase 6 exam + INC-006.**

## Phase 7 — The AI layer (Weeks 19–23)

**W19 · LLMs as unreliable workers**
- Build: Ollama locally; LLM-assisted normalisation of messy product categories with a labelled
  eval set, accuracy report, and fallback rules. Never trust output without validation.
- Concepts: tokens, context, temperature, structured output, evals, cost/latency trade-offs.

**W20 · Support-ticket intelligence**
- Build: classify `support_tickets` (intent, sentiment, linked order) into a Silver table with
  confidence + human-review quarantine; detect prompt injection planted in ticket text.

**W21 · RAG over your own runbooks**
- Build: chunk `incidents/` + `docs/runbooks/`, embed locally, store in a local vector store
  (LanceDB or Chroma), retrieval eval (hit-rate@k) before any generation.

**W22 · Guarded text-to-SQL over Gold**
- Build: an agent that answers business questions using only Gold tables, read-only, with a
  semantic layer doc, SQL validation, row limits and an eval set of 30 questions.

**W23 · AI in the pipeline, done safely**
- Build: wire the classifier into the orchestrated job with quality gates; compare against
  Databricks AI functions if available in Free Edition.
- **Phase 7 exam + INC-007.**

## Phase 8 — Capstone (Week 24)

- Mock system-design interview: "Design Pulse Retail's data platform" (45 min, tutor as interviewer).
- Final chaos gauntlet: three simultaneous failures, he runs the incident.
- Publish: README polished, architecture diagram, 3-minute walkthrough script.
