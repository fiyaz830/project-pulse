# Chaos Mart Partner API — v1

*Official vendor documentation. Last updated: "recently".*

Base URL (local sandbox): `http://localhost:8800`
Auth: send your key in the `X-API-Key` header. Keys are issued via the `CHAOS_MART_API_KEY`
environment variable in the sandbox.

## Rate limits
Partners may make up to 60 requests per minute. Exceeding the limit returns `429 Too Many
Requests` with a `Retry-After` header in seconds.

## Resources
`GET /v1/{resource}` where resource is one of: `customers`, `products`, `orders`,
`order_lines`, `payments`, `refunds`, `inventory_snapshots`, `support_tickets`.

| Param | Type | Notes |
|---|---|---|
| `updated_since` | ISO-8601 | Records changed at or after this time |
| `page_size` | int | Max 500 |
| `cursor` | string | From `next_cursor` of the previous response |

Response:
```json
{ "data": [ ... ], "next_cursor": "abc123" | null }
```

## Guarantees
- All timestamps are UTC.
- Record IDs are unique.
- `amount` fields are decimal rupees.

*The server code in this folder is the vendor's system. Treat it as a black box: integrate
against these docs and what you observe, exactly as you would with a real partner.*
