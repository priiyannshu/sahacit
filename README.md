# sahacit — Symbiotic Cognition (सहचित्)

A personal learning & knowledge consolidation workspace built around **physical printed materials**, **specialized standalone tools**, **audio overviews**, and a **Pi5-hosted Jupyter + `agy` substrate**.

## Philosophy

Active learning happens across tactile and focused mediums—not inside a single monolithic app:
1. **Print & Tactile Study (`booklets/`)**: A4 duplex-friendly booklets, books, cut-out information packets, and visual lineage trees for offline, focused reading and annotation.
2. **Audio Overviews (`notebooklm/`)**: NotebookLM audio overviews generated from steering manifests, stored in Cloudflare R2 (via `wrangler`) and accessed through custom client tooling.
3. **Specialized Consolidation Apps (`apps/` when ready)**: Domain-specific software (e.g., interactive geography globe) where studied facts and insights are consolidated *after* learning and expanded incrementally.
4. **Exam Pattern Research & Mock Prep (`pyqs/`)**: Studying past papers and juicing out question patterns and types (including future PWA quiz tooling) for mock exam advantage.
5. **Always-On Cognitive Substrate (`jupyter/`, parked `web/`)**: Jupyter Server paired with `agy` as the LLM backend on an always-on Raspberry Pi 5 node (`s1`) for interactive notebooks and experimentation.

## Directory Structure

| Path | Purpose |
|---|---|
| `AGENTS.md` | Agent philosophy, directory boundaries, and print/R2/Pi5 rules |
| `booklets/` | Printable booklets, cut-out packets, and `lineages/` (historical family trees & printable HTML/PDFs) |
| `pyqs/` | Past Year Questions & official answer keys (organized by year, e.g., `pyqs/2026/`) |
| `notebooklm/` | NotebookLM sync scripts, steering manifests, and CLI/MCP tooling notes (audio artifacts in R2) |
| `DDC/` | Dewey Decimal Classification (`000`–`900`) directory taxonomy |
| `jupyter/` | Pi5 Jupyter + `agy` substrate (`library/`, `tests/`, `start.sh`, `jupyter_server_config.py`) |
| `web/` | Vite + React + TypeScript frontend for the Jupyter substrate (currently parked) |
| `docs/archive/` | Archived architectural charters (`FOUNDATION.md`, `MASTER_PLAN.md`, `plans/`) |
