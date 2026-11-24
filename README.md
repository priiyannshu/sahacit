# sahacit — Symbiotic Cognition (सहचित्)

A personal learning & knowledge consolidation workspace built around **physical printed materials**, **specialized standalone tools**, **audio overviews**, and a **Pi5-hosted Jupyter + `agy` substrate**.

## Philosophy

Active learning happens across tactile and focused mediums—not inside a single monolithic app:
1. **Print & Tactile Study (`booklets/`)**: Printable booklets, books, cut-out information packets, and visual lineage trees for offline, focused reading and annotation.
2. **Audio Overviews (`notebooklm/`)**: NotebookLM audio overviews and steering manifests, accessed via custom client tooling.
3. **Specialized Consolidation Apps**: Domain-specific software (e.g., interactive geography globe) where studied facts and insights are consolidated *after* learning.
4. **Always-On Cognitive Substrate (`library/`, `web/`, `start.sh`)**: Jupyter Server paired with `agy` as the LLM backend on an always-on Raspberry Pi 5 node for interactive notebooks and experimentation.

## Directory Structure

| Path | Purpose |
|---|---|
| `booklets/` | Printable booklets, cut-out packets, and `lineages/` (historical family trees & printable HTML/PDFs) |
| `pyqs/` | Past Year Questions & official answer keys (organized by year, e.g., `pyqs/2026/`) |
| `notebooklm/` | NotebookLM sync scripts, steering manifests, and CLI/MCP tooling notes |
| `DDC/` | Dewey Decimal Classification (`000`–`900`) directory taxonomy |
| `jupyter/` | Pi5 Jupyter + `agy` substrate (`library/`, `tests/`, `start.sh`, `jupyter_server_config.py`) |
| `web/` | Vite + React + TypeScript frontend for the Jupyter substrate |
| `docs/archive/` | Archived architectural charters (`FOUNDATION.md`, `MASTER_PLAN.md`, `plans/`) |
