# Grain register

One sentence per table. No transformation is reviewed until its grain is written here.

| Layer | Table | Grain (one row per …) | Natural key | Surrogate key |
|---|---|---|---|---|
| bronze | | one row per record received per batch | | `_record_hash` |
| silver | | | | |
| gold | | | | |
