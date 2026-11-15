# Chaos Mart — build spec for the tutor (spoilers; Shaik should not read)

Build this on **Week 1, Day 5** into `sources/chaos_mart/` (`server.py`, `generator.py`,
`chaos.yaml`). Stack: FastAPI + uvicorn + Faker, seeded RNG so every run is reproducible.
Run with `uv run python -m sources.chaos_mart.server` on `localhost:8800`.

Shaik receives only `sources/chaos_mart/API_DOCS.md` — the vendor's documentation, which is
deliberately incomplete in the ways listed under "Doc lies".

## Endpoints
- `GET /v1/customers`, `/v1/products`, `/v1/orders`, `/v1/order_lines`, `/v1/payments`,
  `/v1/refunds`, `/v1/inventory_snapshots`, `/v1/support_tickets`
- Query params: `updated_since` (ISO-8601), `page_size` (max 500), `cursor`
- Auth: header `X-API-Key` read from env `CHAOS_MART_API_KEY` (teaches secrets on day one)

## Chaos knobs (`chaos.yaml`, each 0.0–1.0 or count; tutor changes these for drills)
- `rate_limit_per_minute` (default 60), `burst` (10); 429 with `Retry-After` seconds
  (sometimes HTTP-date when `retry_after_http_date: true`)
- `p_503`, `p_timeout_seconds`, `p_html_200` (200 with HTML body)
- `p_duplicate_record`, `p_out_of_order_update`, `p_future_timestamp`
- `p_null_required_field`, `p_bad_email`, `p_whitespace_case_noise`
- `p_orphan_order_line` (product not yet published), `late_arrival_hours`
- `schema_drift`: list of {entity, from_day, change} e.g. add column, int → "12.5%" string,
  INR → paise for `partner_id=P07`
- `cursor_repeat_bug: false`
- Timestamps: mix of `Z`, `+05:30` and naive strings (naive means IST — undocumented)
- `support_tickets.body` occasionally contains prompt-injection text (Phase 7)

## Doc lies (what API_DOCS.md gets wrong or omits)
- Says timestamps are "UTC"; they are not always.
- Says IDs are unique per page; duplicates happen across pages.
- Omits `Retry-After` format variance and the HTML 200 case.
- Documents `amount` as "decimal rupees"; partner P07 sends paise from day 30 of data.
