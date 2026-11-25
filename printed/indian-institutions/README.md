# Indian Institutions — Print Atlas Workspace

Canonical working directory for researching, authoring, validating, and compiling **Book 1: Indian Institutions (UPSC Prelims 2027 Atlas)**.

## Key Files

- `SPEC.md` — Governing architecture, editorial rules (de-congested layout, two-column whitespace use, zero AI/dev text artifacts), and 7-Block schema summary.
- `RESEARCH_PLAN.md` — Batch-by-batch research & verification roadmap for all **134 institutions** across Parts I–VII.
- `data/schema.json` — Formal JSON Schema for institution records.
- `data/roster.json` — Master 134-institution roster grouped across 7 Functional Parts.
- `data/state_skeleton.json` — Opening *Skeleton of the Indian State* macro-map.
- `data/institutions/*.json` — Per-institution JSON records (`005_parliament.json`, `021_eci.json`, `044_rbi.json`, `088_ngt.json`, `092_wccb.json` completed as benchmarks; remaining 129 queued per `RESEARCH_PLAN.md`).
- `build.py` — Validates JSON records, generates deterministic Master Cross-Indexes (`generated/book_payload.json`), and compiles the A4 duplex PDF via Typst `0.15.1`.
- `typst/` — Monochrome A4 duplex print templates (`main.typ`, `theme.typ`, `skeleton.typ`, `entry.typ`, `indexes.typ`).

## Build Command

```bash
python3 printed/indian-institutions/build.py
```
