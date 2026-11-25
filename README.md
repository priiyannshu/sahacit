# sahacit — Symbiotic Cognition (सहचित्)

A personalized, print-first cognitive preparation system built to ace **UPSC Civil Services & Forest Services Prelims on 23 May 2027**, combining AI preparation, physical printing, and structured daily logging.

## Leading Philosophy

UPSC Prelims is treated as a sorting mechanism for **multi-dimensional thinkers**, approached without the conventional textbook-and-coaching route:

1. **Print Into Physical Reality First**: Generate and print high-value physical artifacts—**books, booklets, subject & ancient-text dictionaries, character sheets, and timeline roll cutouts/information packets**—and master them through daily tactile reading and memorization.
2. **Phased Execution (2026 → 2027)**:
   - **Through End of 2026**: Build a high-hour daily study and repeated-reading habit using printed materials, taking **PYQs occasionally** purely to harvest pattern observations and print ideas. (**CSAT Maths** and the **AI Examiner Board** are deferred to 2027.)
   - **2027**: Analyze remaining gaps after the print-first sprint and activate downstream software—the **Study Time Recorder PWA**, **AI Examiner Board** (spaced-repetition testing tied to daily diary logs and digital mirrors), **CSAT calibration**, and domain consolidation apps (`apps/`).
3. **7-Category Multi-Dimensional PYQ Lens (`pyqs/`)**: Dissect past papers across *Environment & Ecology*, *Economics*, *History & Art and Culture*, *Geography*, *Current Affairs*, *Science & Technology*, and *Polity*, tracking **3–4 category conjunctions** and empirical syllabus weightage.
4. **Daily Diary & Digital Mirrors (`diary-entries-of-a-champion/`)**: Log exact study minutes, ingested printed artifacts, repetition passes, and observations daily in structured format for downstream apps.
5. **Secondary Infrastructure**: Audio overviews (`notebooklm/`), Dewey Decimal taxonomy (`DDC/`), and the Pi5 Jupyter + `agy` substrate (`jupyter/`, parked `web/`) remain secondary supporting tools.

## Directory Structure

### Primary Active Pillars

| Path | Purpose |
|---|---|
| `AGENTS.md` | Governing Prelims 2027 philosophy, phase rules, diary protocol, and agent boundaries |
| `diary-entries-of-a-champion/` | Daily dated logs (`YYYY-MM-DD/entry.md`), ideation, paper diagnostics, and print planning manifests (see `diary-entries-of-a-champion/README.md`) |
| `booklets/` | Canonical reproducible print generators & physical PDFs (`lineages/`, plus future books, booklets, dictionaries, character sheets, cutouts) |
| `pyqs/` | Past Year Questions & official answer keys (`pyqs/2026/`) for pattern extraction |
| `apps/` *(Phase 2 / future)* | Study Time Recorder PWA, AI Examiner Board / quiz tools, and post-study consolidation apps |

### Secondary & Reference Pillars

| Path | Purpose |
|---|---|
| `notebooklm/` *(Secondary)* | NotebookLM sync scripts, steering manifests, and CLI/MCP notes (audio stored in Cloudflare R2) |
| `DDC/` *(Reference)* | Dewey Decimal Classification (`000`–`900`) directory taxonomy |
| `jupyter/` *(Secondary)* | Pi5 (`s1`) Jupyter + `agy` substrate (`library/`, `tests/`, `start.sh`, `jupyter_server_config.py`) |
| `web/` *(Parked)* | Vite + React + TypeScript frontend for the Jupyter substrate |
| `docs/archive/` *(Archive)* | Read-only historical charters (`FOUNDATION.md`, `MASTER_PLAN.md`, `plans/`) |
