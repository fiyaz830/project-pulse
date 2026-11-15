# Project Pulse 2.0 — Curriculum (30 weeks, 1 hour/day)

Domain: **Pulse Retail**, an Indian e-commerce company. The journey starts with plain Python
on small retail files (Phase 0). After that, the source system is **Chaos Mart**: a vendor REST
API that rate-limits, lies in its docs, sends duplicates, changes its schema and delivers late.
Target: Delta Lake Bronze/Silver/Gold, locally (PySpark + delta-spark) and on Databricks Free
Edition.

Entities: customers, products, orders (header), order_lines, payments, refunds,
inventory_snapshots, support_tickets (free text, used in the AI phase).

Each week has 5 build days (Mon–Fri), a Saturday drill and a Sunday quiz + retro.
- "Py:" lists the Python topics the week practises.
- "DE idea:" is the data engineering concept the week introduces, in plain words.
- "SQL bridge:" links the Python idea to the SQL he already knows from Snowflake.

**Where Phase 0 work lives:** `gym/python/wNN/dX_<topic>.py` (one file per day). The tutor puts
tiny fake sample files in `gym/data/` when a lesson needs them. `data/` is git-ignored, so
don't put samples there. Tests go in `tests/unit/` from Week 4. Week 6's mini pipeline goes
in `src/pulse/mini_pulse/`.

---

## Phase 0 — Python for Data Engineering (Weeks 1–6)

Goal: be able to read, clean, transform, test and write retail data in Python, and know the
core data engineering ideas behind it. No cloud, no Spark, no CI yet. Just Python, files and
small examples. Run everything with `uv run python <file>`. The environment is already set
up, so treat it as a black box for now; Week 7 explains how it works.

**W1 · Python as a data tool (data in memory)**
- Mon: running a script, variables, numbers, strings, `print` and f-strings → print a receipt
  for one order.
- Tue: lists: `len`, `sum`, `min`, `max`, indexing and slicing on a list of order amounts.
- Wed: dicts: one order as a dict, `.get()` and what happens when a key is missing.
- Thu: a list of dicts is a table. Loop over orders and print each one.
- Fri: `if`/`else` inside loops: total revenue, orders above ₹1,000, order count per city.
- DE idea: a table is a list of rows. **Grain** means what one row represents ("one row per order").
- SQL bridge: dict ≈ one row, keys ≈ column names, counting with a dict ≈ `GROUP BY ... COUNT(*)`.
- Sat drill: "data detective". A list of orders hides a duplicate, a missing amount and a
  negative amount. Find them with code.

**W2 · Functions: reusable transformations**
- Mon: `def`, parameters, `return`. Turn Week 1's revenue code into a function.
- Tue: type hints (like column types), default arguments and the mutable-default trap.
- Wed: functions that transform one row, `clean_order(order) -> order`. What "pure" means.
- Thu: list comprehensions for filtering and transforming.
- Fri: `sorted` with `key=`: top 5 customers by spend.
- DE idea: a transform step is a function with input → output. Pure functions are easy to test
  and safe to rerun.
- SQL bridge: comprehension ≈ `SELECT ... WHERE`, `sorted(key=)[:5]` ≈ `ORDER BY ... LIMIT 5`.

**W3 · Files: reading and writing real data**
- Mon: `pathlib`, reading a text file, `with` blocks (they close the file for you).
- Tue: the `csv` module: `DictReader` gives a list of dicts. Every value arrives as a string.
- Wed: converting types safely: `try`/`except ValueError`, and sending bad rows to a `rejects` list.
- Thu: `json`: load and dump, nested JSON (an order containing its lines), JSONL (one JSON per line).
- Fri: first mini ETL: read `orders.csv` → clean → write `clean_orders.csv` + `rejects.csv`.
- DE idea: **E**xtract, **T**ransform, **L**oad. Never drop bad rows silently: count them
  (rows in = rows out + rows rejected).
- SQL bridge: rejects file ≈ an error table you'd load beside the target in Snowflake.

**W4 · Cleaning messy data + your first tests**
- Mon: string cleaning: `strip`, `lower`, `replace`, `split` (emails, city names).
- Tue: dates with `datetime`: parsing strings, formats, why a date stored as text is a trap.
- Wed: duplicates: `set`, dict keyed by `order_id`, keep the latest by `updated_at`.
- Thu: `pytest` basics: a test file, `assert`, running `uv run pytest`.
- Fri: tests for your cleaning functions, including edge cases (empty list, `None`, bad date).
- DE idea: **natural key** (the column that identifies a row), duplicates, nulls, and
  **idempotency** (running the job twice gives the same result as running it once).
- SQL bridge: keep-latest dedupe ≈ `ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY updated_at DESC) = 1`.

**W5 · pandas: tables in Python**
- Mon: DataFrame basics: `read_csv`, `head`, `dtypes`, `shape`.
- Tue: selecting and filtering rows, adding new columns.
- Wed: `groupby` + `agg`: revenue by city and by day.
- Thu: `merge`: orders + customers. Check row counts before and after the join.
- Fri: nulls and duplicates in pandas (`isna`, `fillna`, `drop_duplicates`). Rewrite the Week 3
  ETL in pandas and compare.
- DE idea: **join fan-out**. A join that matches more than one row on the other side multiplies
  rows and inflates totals.
- SQL bridge: filter ≈ `WHERE`, `groupby` ≈ `GROUP BY`, `merge` ≈ `JOIN`.

**W6 · Mini Pulse: your first end-to-end pipeline**
- Mon: organising code: modules, imports, `if __name__ == "__main__":`.
- Tue: `logging` instead of `print`. Log what happened and how many rows.
- Wed: DuckDB: run SQL on CSV files and DataFrames from Python.
- Thu: build `src/pulse/mini_pulse/`: `raw/` → `clean/` → `report` (daily revenue by city).
- Fri: make it safe to rerun, add tests and a short "how to run" section to the README.
- DE idea: **layers**. raw → clean → report is a small preview of Bronze → Silver → Gold.
- Sun: **Phase 0 exam** (see assessments.md).

## Phase 1 — The Workshop: production habits (Week 7)

**W7 · How professional Python projects are set up**
- Build: understand the existing `uv` env and lockfile, ruff + mypy + pytest + pre-commit, first
  CI run green, `src/pulse/common/logging.py` (structured JSON logs), `src/pulse/config/settings.py`
  (typed config from env, no secrets in code).
- Concepts: reproducible environments (`pyproject.toml` = what you asked for, `uv.lock` = exactly
  what you got), lockfiles, git habits, Conventional Commits, CI as a gate.
- Py: packages, `pathlib` paths relative to `__file__`, environment variables.
- Day 5: tutor generates the Chaos Mart vendor server in `sources/chaos_mart/`. He must NOT read
  the server code. Treat it as a third party; he only gets `API_DOCS.md`.
- DoD: `uv run pytest` passes; pre-commit blocks a fake secret; CI green on GitHub.

## Phase 2 — Ingestion under hostile conditions (Weeks 8–10)

**W8 · Talking to an API that hates you**
- Build: `ingestion/client.py`: paginated client (cursor + page), timeouts, typed responses.
- Concepts: HTTP semantics, status codes, idempotent vs non-idempotent verbs, pagination styles,
  why `requests.get(url)` with no timeout is a production incident.
- Py: custom exceptions, `httpx`.

**W9 · Rate limits, retries and backpressure**
- Build: retry with exponential backoff + full jitter, honour `Retry-After`, client-side token
  bucket, circuit breaker, max-attempt budget; tests with a fake transport.
- Concepts: 429 vs 503, thundering herd, retry storms, at-least-once delivery, why retries create
  duplicates (sets up Silver).
- Py: decorators, closures, `time.monotonic`, generators for pagination, `dataclasses`.

**W10 · A landing zone you can rerun 100 times**
- Build: deterministic landing paths (`raw/<entity>/ingest_date=/batch_id=/part-0000.jsonl`),
  manifest file per batch, checkpoint/watermark state, crash-and-resume test.
- Concepts: idempotency, exactly-once illusions, high-watermark vs CDC, atomic writes
  (write temp → rename), backfills.
- Py: context managers, `json` streaming, `hashlib`, `tempfile`, `os.replace`.
- **Phase 2 exam + INC-001** (written from the Saturday drill).

## Phase 3 — Bronze: keep everything, trust nothing (Weeks 11–12)

**W11 · Spark and Delta from first principles**
- Build: local PySpark + delta-spark session factory; Bronze writer adding `_ingest_ts`,
  `_batch_id`, `_source_file`, `_record_hash`; schema-on-read with `_rescued_data`-style column.
- Concepts: lazy evaluation, DAGs, narrow vs wide transforms, Delta log, ACID on object storage,
  time travel.
- Py: classes, `@classmethod`, typing `Protocol`, dependency injection for testability.

**W12 · Idempotent Bronze and the cloud twin**
- Build: rerun-safe Bronze load (`replaceWhere` on batch vs MERGE on record hash — he must argue
  which and why); upload landing files to a Unity Catalog Volume; same code runs on Databricks
  serverless; Auto Loader version for comparison.
- Concepts: append vs overwrite vs MERGE semantics, Auto Loader checkpoints, schema evolution modes.
- Py: packaging (`pyproject`, wheel), environment-aware config.
- **Phase 3 exam + INC-002.**

## Phase 4 — Silver: assume the source is garbage (Weeks 13–16)

**W13 · Grain, keys and duplicates**
- Build: declare grain for every Silver table in `docs/grain.md`; dedupe with window functions
  (latest by event time, tie-break by ingest time); hash surrogate keys.
- Concepts: natural vs surrogate keys, grain statements, `ROW_NUMBER` vs `QUALIFY`, deterministic
  tie-breaking.
- Py: `functools`, `itertools`, then the Spark equivalent.

**W14 · Quarantine, not crash**
- Build: validation rules → valid rows to Silver, invalid rows to `silver.quarantine_<entity>` with
  reason codes; nothing silently dropped; reconciliation counts (in = out + quarantined).
- Concepts: dead-letter queues, error budgets, null semantics, three-valued logic, type coercion traps.
- Py: `Enum`, `pydantic` models for row validation, `pytest.mark.parametrize`.

**W15 · Time is a liar**
- Build: timezone normalisation (IST vs UTC vs naive), late-arriving data with a lookback window,
  out-of-order updates, SCD Type 2 for customers with MERGE.
- Concepts: event time vs processing time, watermarks, SCD1/2/3, effective dating, current flag bugs.
- Py: `datetime`/`zoneinfo` pitfalls, `hypothesis` property-based tests.

**W16 · Data contracts and automated quality**
- Build: `contracts/*.yaml` (open data contract standard via `datacontract-cli`), `pandera`
  schemas, a `quality/` runner that fails the pipeline on contract breach and warns on drift;
  DQ results written to an audit table.
- Concepts: producer/consumer contracts, schema drift handling policies, freshness/volume/
  distribution checks, blocking vs warning checks.
- Py: writing a small reusable library, `abc`, plugin registration pattern.
- **Phase 4 exam + INC-003.**

## Phase 5 — Gold: dimensional modelling that survives interviews (Weeks 17–19)

**W17 · Star schema for real**
- Build: `dim_customer` (SCD2), `dim_product`, `dim_date`, `fact_order_line` at stated grain;
  late-arriving dimension handling (inferred members / unknown key -1).
- Concepts: Kimball bus matrix, conformed dimensions, degenerate dimensions, factless facts.

**W18 · Join traps and metric correctness**
- Build: `fact_daily_sales` aggregate; tests that prove no fan-out (row-count and sum invariants
  before/after every join); payments vs orders reconciliation.
- Concepts: fan trap, chasm trap, many-to-many bridges, double counting, additive/semi-additive/
  non-additive measures, as-of joins.
- Py: pandas vs Spark mental models, vectorisation, why loops over rows are a smell.

**W19 · Storage and partitioning strategy**
- Build: benchmark notebook: partitioned vs liquid clustering vs Z-order on the same fact;
  small-file problem reproduced then fixed with OPTIMIZE; VACUUM + retention; write an ADR.
- Concepts: file sizing, data skipping, partition cardinality, skew and salting, AQE, broadcast joins.
- **Phase 5 exam + INC-004.**

## Phase 6 — Production orchestration, secrets and CI/CD (Weeks 20–22)

**W20 · Orchestration as code**
- Build: Databricks Asset Bundle (`databricks.yml`) defining a multi-task job: ingest → bronze →
  silver → quality gate → gold; task retries, timeouts, parameters (`run_date`), run-level batch_id.
- Concepts: DAG design, task idempotency, retries vs re-runs, SLAs, alerting.

**W21 · Backfills, reruns and secrets**
- Build: backfill command for a date range that is safe to run twice; secrets via env + local
  `.env` (git-ignored) and Databricks secret scopes if available in Free Edition (verify — if not,
  document the fallback in an ADR); `gitleaks` in pre-commit and CI.
- Concepts: least privilege, secret rotation, config layering (defaults → env → runtime params).

**W22 · CI/CD pipeline**
- Build: GitHub Actions: lint → type-check → unit tests → data-quality tests on fixture data →
  `bundle validate`; branch protection on main.
- Concepts: test pyramid for data, fixture data design, environment promotion (dev → prod targets).
- **Phase 6 exam + INC-005.**

## Phase 7 — Lineage, metadata and observability (Weeks 23–24)

**W23 · Know where every number came from**
- Build: `ops.pipeline_runs` and `ops.table_audit` tables (run id, rows in/out/quarantined,
  duration, git sha); column-level lineage doc for one Gold metric back to the API field;
  compare with Unity Catalog lineage on Databricks.
- Concepts: technical vs business lineage, OpenLineage event model, metadata as a product.

**W24 · Observability and the incident-report README**
- Build: freshness and volume anomaly checks; a Gold "pipeline health" table; README rewritten as
  the platform's incident log and operating guide.
- **Phase 7 exam + INC-006.**

## Phase 8 — The AI layer (Weeks 25–29)

**W25 · LLMs as unreliable workers**
- Build: Ollama locally; LLM-assisted normalisation of messy product categories with a labelled
  eval set, accuracy report, and fallback rules. Never trust output without validation.
- Concepts: tokens, context, temperature, structured output, evals, cost/latency trade-offs.

**W26 · Support-ticket intelligence**
- Build: classify `support_tickets` (intent, sentiment, linked order) into a Silver table with
  confidence + human-review quarantine; detect prompt injection planted in ticket text.

**W27 · RAG over your own runbooks**
- Build: chunk `incidents/` + `docs/runbooks/`, embed locally, store in a local vector store
  (LanceDB or Chroma), retrieval eval (hit-rate@k) before any generation.

**W28 · Guarded text-to-SQL over Gold**
- Build: an agent that answers business questions using only Gold tables, read-only, with a
  semantic layer doc, SQL validation, row limits and an eval set of 30 questions.

**W29 · AI in the pipeline, done safely**
- Build: wire the classifier into the orchestrated job with quality gates; compare against
  Databricks AI functions if available in Free Edition.
- **Phase 8 exam + INC-007.**

## Phase 9 — Capstone (Week 30)

- Mock system-design interview: "Design Pulse Retail's data platform" (45 min, tutor as interviewer).
- Final chaos gauntlet: three simultaneous failures, he runs the incident.
- Publish: README polished, architecture diagram, 3-minute walkthrough script.
