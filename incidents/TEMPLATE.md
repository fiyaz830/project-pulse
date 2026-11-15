# INC-### — <short title>

| Field | Value |
|---|---|
| Date | YYYY-MM-DD |
| Severity | SEV1 (wrong numbers reached consumers) / SEV2 (pipeline down, data late) / SEV3 (degraded, caught by checks) |
| Detected by | alert / DQ check / human / chaos drill |
| Duration | detection → mitigation → resolution |
| Tables affected | |

## Summary
Two or three sentences a VP could read.

## Impact
Which numbers were wrong or late, for whom, by how much.

## Timeline (IST)
- HH:MM — what happened / what you saw / what you did

## Root cause
The technical cause. Then **5 whys** down to the design or process gap.

## Detection
How it was found. How it *should* have been found, and how much earlier.

## Mitigation and fix
What stopped the bleeding; what fixed it properly. Link commits.

## Prevention (action items)
- [ ] Test / check / contract / alert that makes this class of failure impossible or loud

## Lessons
What you now understand that you didn't before.
