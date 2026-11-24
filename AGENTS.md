# AGENTS.md — sahacit (सहचित्)

This file defines the governing philosophy, directory boundaries, and operational rules for AI agents working in `sahacit`.

---

## 1. Core Philosophy

**sahacit** separates **active learning** from **post-study knowledge consolidation**:

1. **No Monolithic All-in-One Study App**: Do not try to force active studying, reading, and note-taking into a single software application. Active learning happens through tactile physical media and focused audio.
2. **Print-First Tactile Study (`booklets/`)**: Active study is driven by physical printed booklets, books, and cut-out information packets produced for focused, offline reading and annotation.
3. **Audio Overviews (`notebooklm/` + R2)**: NotebookLM audio overviews remain a core study companion, accessed via custom client tooling and backed by Cloudflare R2.
4. **Post-Study Consolidation (`apps/`, when ready)**: Software applications are built *after* studying to consolidate specific domains into living tools (e.g., an interactive geography globe where newly encountered facts can be added incrementally).
5. **Exam Pattern Research & Mock Prep (`pyqs/` + future PWA quiz tools)**: Dedicated space for dissecting past papers and juicing out question patterns, trap structures, and question types for mock exam preparation advantage.
6. **Always-On Cognitive Substrate (`jupyter/`, parked `web/`)**: An always-on Raspberry Pi 5 node (`s1`) runs the Jupyter + `agy` LLM backend for interactive notebook experimentation when needed.

---

## 2. Directory Structure & Ownership

| Path | Role & Agent Rules |
|---|---|
| `AGENTS.md`, `README.md` | **Only non-hidden files allowed at repository root.** |
| `booklets/` | Printable booklets, cut-out packets, and current experimental work (`booklets/lineages/`). |
| `pyqs/` | Past Year Questions & official answer keys organized by year (`pyqs/2026/`, etc.). Do not modify official/source PDFs unless explicitly asked. |
| `notebooklm/` | NotebookLM sync scripts, steering manifests, and CLI/MCP tooling docs. Scripts/manifests only—no audio files in git. |
| `DDC/` | Full Dewey Decimal Classification (`000`–`900`) taxonomy tree. **Keep intact; never prune "empty" folders.** |
| `jupyter/` | Self-contained Pi5 Jupyter + `agy` substrate (`library/`, `tests/`, `start.sh`, `jupyter_server_config.py`). Keep all paths portable. |
| `web/` | Vite + React + TypeScript frontend for the Jupyter substrate. **Parked—do not touch or expand unless explicitly requested.** |
| `apps/` *(future)* | Dedicated directory for specialized standalone consolidation apps and PWA quiz/pattern-research tools. **Do not scaffold unless explicitly asked.** |
| `docs/archive/` | Read-only historical plans (`FOUNDATION.md`, `FOUNDATION_ORIGINAL.md`, `MASTER_PLAN.md`, `plans/`). Keep tracked in git; never mutate. |

> **External Archive**: Legacy `22` / `preach` assets (`heritage/`) live outside this repo at `~/archive/sahacit-heritage/`. Do not re-import them into git unless explicitly instructed.

---

## 3. Domain Rules for Agents

### Print & Booklet Generation (`booklets/`)
- **Paper & Folding**: Design for **A4 standard sheets** and **duplex-friendly half-fold booklets**.
- **Ink Efficiency**: Use clean, monochrome-friendly styling (white/light backgrounds, crisp vectors, high-contrast typography; avoid heavy dark fills or ink-wasting backgrounds).
- **Cut-Out Information Packets**: For flashcards, strips, or pocket packets, use structured grid layouts with explicit **cut marks** and duplex alignment where applicable.
- **Reproducibility**: Generate printable HTML/PDFs from structured source files and Python/HTML-to-PDF scripts so every booklet can be regenerated cleanly.

### NotebookLM Audio Overviews (`notebooklm/`)
- Use `steering_manifests/` with `nlm` / `notebooklm-py` to tailor audio overviews to study units.
- Support bilingual **Hinglish / Hindi + English** registers where helpful.
- **Storage Boundary**: Never commit `.mp3`, `.wav`, or large media artifacts to git. Store generated audio overviews in **Cloudflare R2** (managed/accessed via `wrangler`) for consumption by custom client apps.

### Consolidation Apps & Question-Pattern Research
- Keep consolidation tools **domain-focused** and **incrementally updatable** (easy to add newly encountered facts, coordinates, or concepts over time).
- **PWA Quiz & Pattern Extraction**: Unlike older archived docs (`docs/archive/`), **PWA quiz patterns ARE an intentional part of the roadmap**—specifically for researching, categorizing, and juicing out question patterns and types for mock exam advantage.

### Pi5 (`s1`) Jupyter + `agy` Substrate (`jupyter/`)
- Keep `jupyter/jupyter_server_config.py`, `jupyter/start.sh`, and `jupyter/tests/test_substrate.py` free of hardcoded machine or user paths (always resolve dynamically relative to file/script location).
- Do not modify `web/` unless the user explicitly asks to work on the Jupyter frontend.

---

## 4. Strict Repo Hygiene & Workflow

1. **Root Cleanliness**: Never leave loose scripts, PDFs, `.log` files, scratch outputs, or temporary files in the repository root. Only `AGENTS.md`, `README.md`, dotfiles (e.g., `.gitignore`), and top-level directories belong at `/`.
2. **Archived Philosophy Boundaries**: `docs/archive/` represents an earlier monolithic Virtual University architecture. Consult it only for historical context—never enforce its "single-app-only" or "no PWA quiz patterns" restrictions on new work.
3. **Verification & Sync**: Validate modified scripts/configs before reporting completion, keep `.gitignore` clean (`*.log`, `*.tmp`, `web/dist/`, `.ipynb_checkpoints/`, `__pycache__/`, `.venv/`, `node_modules/`), and sync cleanly to `origin/main` when wrapping up work.
