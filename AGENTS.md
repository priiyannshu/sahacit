# AGENTS.md — sahacit (सहचित्)

This file defines the governing philosophy, phased roadmap, directory boundaries, and operational rules for AI agents working in `sahacit`.

---

## 1. Mission & Leading Philosophy

**sahacit** is a personalized, AI-and-print cognitive system built to crack **UPSC Civil Services & Forest Services Prelims on 23 May 2027**. It rejects the conventional textbook-and-coaching route in favor of treating UPSC Prelims as a sorting mechanism for **multi-dimensional thinkers**.

1. **Print Into Physical Reality First (Leading Philosophy)**:
   - The primary focus is designing, generating, and printing high-value physical study artifacts—**books, booklets, subject & ancient-text dictionaries, character sheets, and timeline roll cutouts/information packets**.
   - Active daily memorization and repeated reading happen on physical paper, leveraging tactile reading speed and visual recall.
   - Only *after* physical artifacts are printed and analyzed in practice do remaining gaps get routed into software apps or other workflows.
2. **Phased Execution (2026 vs. 2027)**:
   - **Phase 1 — Through End of 2026 (Habit + Print-First Foundation)**:
     - Establish a disciplined, high-hour daily study habit centered on reading and memorizing printed artifacts **over and over again**.
     - Attempt **PYQs occasionally ("now and then")** solely to extract new patterns, topic distributions, and print ideas—not for premature score optimization.
     - **Deferred Out of 2026**: **No CSAT Mathematics** and **no AI Examiner Board** in 2026.
   - **Phase 2 — 2027 Consolidation, Calibration & Software**:
     - Activate the **AI Examiner Board** (examiner agents using PYQ pattern-research skills to generate authentic tests and spaced-repetition loops from daily diary logs and digital mirrors of printed packs).
     - Add targeted **CSAT calibration** (comprehension sharpness + pattern-by-pattern math) and **downstream software apps** (`apps/`), including a **Study Time Recorder PWA + database** for minute-level tracking and weekly/monthly evaluations.
3. **7-Category Multi-Dimensional PYQ Taxonomy**:
   - All Prelims pattern research uses seven core categories: **Environment and Ecology**, **Economics**, **History and Art and Culture**, **Geography**, **Current Affairs**, **Science and Technology**, and **Polity**.
   - Explicitly track **multi-category conjunctions** (3–4 categories intersecting in a single question) and empirically weighted syllabus allocation (e.g., History ~14% overall, prioritizing Modern History plus Ancient Harappan/coins/Vedas and Art & Culture paintings/caves over lower-weight Medieval coverage).
4. **Daily Diary Logging for Downstream Apps (`diary-entries-of-a-champion/`)**:
   - Every study day is logged with structured study hours/minutes, materials ingested, repetition passes, and observations so downstream applications can consume the history cleanly.
5. **Secondary Supporting Pillars**:
   - **Audio Overviews (`notebooklm/` + R2)**, **Pi5 Jupyter + `agy` substrate (`jupyter/`)**, and the **Dewey Decimal taxonomy (`DDC/`)** remain available as secondary/reference infrastructure behind the Prelims 2027 print-first workflow.

---

## 2. Directory Structure & Ownership

### Primary Active Pillars

| Path | Role & Agent Rules |
|---|---|
| `AGENTS.md`, `README.md` | **Only non-hidden files allowed at repository root.** |
| `diary-entries-of-a-champion/` | Daily dated logs (`YYYY-MM-DD/entry.md`), session ideation (`idea.md`), paper diagnostics, and print planning manifests (`output.md`). Follow `diary-entries-of-a-champion/README.md`. |
| `booklets/` | Canonical, reproducible print generators (Python/HTML-to-PDF) and physical PDFs (`booklets/lineages/`, plus future books, booklets, dictionaries, character sheets, and timeline cutouts/packets). |
| `pyqs/` | Past Year Questions & official answer keys organized by year (`pyqs/2026/`, etc.) for occasional pattern extraction. **Do not modify official/source PDFs unless explicitly asked.** |
| `apps/` *(Phase 2 / future)* | Downstream software apps: Study Time Recorder PWA, AI Examiner Board / PWA quiz pattern tools, and post-study consolidation apps. **Do not scaffold unless explicitly asked.** |

### Secondary & Reference Pillars

| Path | Role & Agent Rules |
|---|---|
| `notebooklm/` *(Secondary)* | NotebookLM sync scripts, steering manifests, and CLI/MCP tooling docs. Scripts/manifests only—no audio files in git. |
| `DDC/` *(Reference)* | Full Dewey Decimal Classification (`000`–`900`) taxonomy tree. **Keep intact; never prune "empty" folders.** |
| `jupyter/` *(Secondary)* | Self-contained Pi5 (`s1`) Jupyter + `agy` substrate (`library/`, `tests/`, `start.sh`, `jupyter_server_config.py`). Keep all paths portable. |
| `web/` *(Parked)* | Vite + React + TypeScript frontend for the Jupyter substrate. **Parked—do not touch or expand unless explicitly requested.** |
| `docs/archive/` *(Archive)* | Read-only historical plans (`FOUNDATION.md`, `FOUNDATION_ORIGINAL.md`, `MASTER_PLAN.md`, `plans/`). Keep tracked in git; never mutate. |

> **External Archive**: Legacy `22` / `preach` assets (`heritage/`) live outside this repo at `~/archive/sahacit-heritage/`. Do not re-import them into git unless explicitly instructed.

---

## 3. Domain Rules for Agents

### Daily Diary & Agent Interview Protocol (`diary-entries-of-a-champion/`)
- **Always Use the Standard Schema**: Follow the frontmatter and section schema in `diary-entries-of-a-champion/README.md` when creating or updating daily `entry.md` files so downstream applications can parse study minutes, ingested artifacts, and observations reliably.
- **Prompt for Missing Log Info**: Whenever the user is working inside `diary-entries-of-a-champion/` (or starts a daily check-in), ask concisely for any unprovided daily log fields (total hours/minutes studied, printed/digital materials read and pass count, PYQ observations, new print needs).
- **No Guessing Metrics**: Never fabricate study minutes, scores, page counts, or completion status; ask or mark unknown fields `null`.
- **Respect Phase Boundaries**: Keep 2026 sessions anchored on print generation, daily reading/memorization habits, and occasional PYQ pattern extraction—do not push CSAT Maths or AI Examiner Board workflows into 2026.

### Print & Booklet Generation (`booklets/`)
- **Paper & Folding**: Design for **A4 standard sheets** and **duplex-friendly half-fold booklets** (or explicitly sized duplex/multi-page sheets for character dossiers and timeline roll cutouts).
- **Ink Efficiency**: Use clean, monochrome-friendly styling (white/light backgrounds, crisp vectors, high-contrast typography; avoid heavy dark fills or ink-wasting backgrounds).
- **Cut-Out Information Packets & Character Sheets**: Use structured layouts with explicit **cut marks** and duplex front/back alignment; support real or AI-generated character visuals where requested.
- **Reproducibility**: Generate printable HTML/PDFs from structured source files and Python/HTML-to-PDF scripts so every physical print can be regenerated and tracked by a digital mirror.

### Downstream Software & Pattern Research (`apps/`, Phase 2)
- Build consolidation tools, the Study Time Recorder PWA, and the AI Examiner Board **only after** physical printing needs are analyzed and explicitly requested.
- Keep tools **domain-focused**, **incrementally updatable**, and fed by structured `diary-entries-of-a-champion/` logs plus digital mirrors of printed packs.

### Secondary Infrastructure (`notebooklm/`, `jupyter/`)
- **NotebookLM (`notebooklm/`)**: Use `steering_manifests/` with `nlm` / `notebooklm-py`; support Hinglish / Hindi + English registers where helpful; never commit `.mp3`/`.wav` media (store audio in Cloudflare R2 via `wrangler`).
- **Pi5 Jupyter Substrate (`jupyter/`)**: Keep all paths dynamically resolved relative to file/script location; do not modify `web/` unless explicitly requested.

---

## 4. Strict Repo Hygiene & Workflow

1. **Root Cleanliness**: Never leave loose scripts, PDFs, `.log` files, scratch outputs, or temporary files in the repository root. Only `AGENTS.md`, `README.md`, dotfiles (`.gitignore`), and top-level directories belong at `/`.
2. **Archived Philosophy Boundaries**: `docs/archive/` represents an earlier monolithic Virtual University architecture. Consult it only for historical context—never enforce its "single-app-only" or "no PWA quiz patterns" restrictions on new work.
3. **Verification & Sync**: Validate modified scripts/configs before reporting completion, keep `.gitignore` clean (`*.log`, `*.tmp`, `web/dist/`, `.ipynb_checkpoints/`, `__pycache__/`, `.venv/`, `node_modules/`), and sync cleanly to `origin/main` when wrapping up work.
