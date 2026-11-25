# sahacit — Master Construction Plan

> **Created**: 2026-08-30 · **Repo**: `sahacit` (formerly `vu`) · **Status**: Active
> **Companions**: `FOUNDATION.md` (the vision & philosophical charter) · `docs/archive/` (the `22`, `preach`, and original seed heritage)

---

## 0. How to Use This File

1. **This file is the timeline.** Every phase required to take sahacit from its current state to a working personal university, sequenced so the most valuable things are built earliest.
2. **Phases have exit criteria.** A phase is DONE only when every criterion is verifiably true — endpoints responding, cells rendering, loops completing. Never mark intent as done.
3. **Clean system first, data hydration at the very fucking end.** We build the system (engines, schemas, UI, loops, pipelines, state tracking) completely clean without ANY heritage data hydration. No 671 NCERT chapters, no 4,720 concept nodes, no 2,839 PYQs, and no EVS ledgers are ingested while constructing the system. We use minimal synthetic fixtures (1 mock course, 1 mock lecture, dummy test concepts) strictly to verify functionality. Data is hydrated only after the entire machine is built, verified, and operational.
4. **Minimal before beautiful.** The frontend starts ugly and functional. Aesthetics are in the polish phase.
5. **This laptop is the server.** Everything runs locally during construction. Raspberry Pi deployment and Cloudflare hosting come at the end, after the system works.

---

## 1. The Value Spine (Why This Order)

Carried forward from the original `22` master plan, adapted:

1. **Clean system before data hydration.** Build the pipes, the engine, the canvas, and the state machines first with clean, minimal mock fixtures. Ingesting massive data into a half-built system creates sludge, false progress, and debugging friction. Build the system clean; hydrate data into it at the very end.
2. **Substrate before features.** The Jupyter engine and notebook lifecycle must work before any UI is built on top.
3. **The core loop before the catalog.** A single notebook with a working tutor loop proves the entire architecture. Course organization comes after.
4. **Personal state before global state.** What you learn and how you connect it is more valuable than how the catalog is organized.
5. **Local CLI before deployment.** Everything runs on this laptop first. Pi and Cloudflare arrive only when the system works end-to-end.
6. **Minimal before beautiful.** Raw cells first. University aesthetic last.

---

## 2. How the Old `22` Master Plan Maps to This One

The archived `22` master plan had 14 phases across 3 stages, building a Cloudflare edge stack (Workers, D1, Vectorize, Durable Objects, PWA). Every goal of that plan is achieved here — but with radically simpler means:

| `22` Phase | What It Solved | How sahacit Solves It | sahacit Phase |
|---|---|---|---|
| **0 — Foundation** | Architecture & Cold Archive | Foundation charter, taxonomy structure, and archiving heritage assets in `heritage/` (unhydrated cold storage) | 0 |
| **1 — Semantic Layer** | Vectorize embeddings for discovery | NotebookLM's native context window + agy cli's full-file context | — (unnecessary) |
| **2 — Personal State Schema** | 10 D1 tables for mastery/metaphors | SQLite personal state + notebook-as-memory (clean schema, mock tested) | 5 |
| **3 — DO↔D1 Sync** | Session persistence across reconnects | The `.ipynb` file *is* the persistent session | — (solved by design) |
| **4 — Hybrid Context Assembly** | Grounding LLM in facts + learner state | agy cli reads the full notebook (facts + your notes + errors + metaphors in one document) | 3 |
| **5 — Blob Interface** | Voice + chat interaction UI | The cell canvas (markdown for notes, code for AI interaction) | 2 |
| **6 — Metaphor System** | Extract & track personal metaphors | Paper KG photos + voice notes + notebook extraction pipeline | 5 |
| **7 — Calibration Quiz** | Cold-start diagnostic | Ritual journey notebooks (Classes 1–10) with embedded assessments | 4 (engine) / 8 (hydration) |
| **8 — Interval Pipelines** | Nightly batch processing | Nightly pipeline: audio transcription → KG extraction → next-day content generation | 6 |
| **9 — Voice Navigation** | Voice-first interface | agy cli understands .mp3 directly; audio recorded as learning artifacts | 3 |
| **10 — KG Expansion** | Adding external knowledge sources | OpenCourseWare integration; DDC-organized catalog (clean/synthetic scaffold) | 4 |
| **11 — Visualization** | Knowledge graph visualization | Personal state KG visualization (paper → digital → rendered graph) | 5 |
| **12 — Fact-Check Pipelines** | Verifying LLM outputs | Zero-loss extraction methodology (carried from `preach`) applied to notebook content | 6 |
| **13 — Native Transition** | Production deployment | Pi server + Cloudflare frontend | 7 |
| **14 — Grand Hydration** | Data hydration | Bulk compile & hydrate 671 chapters, 4,720 concept nodes, 2,839 PYQs, EVS ledgers | 8 |

> **Note:** Phases 1 and 3 of the old plan are **solved by architectural choice** — a Jupyter notebook is simultaneously a session log, a context document, and a persistent state file. No sync infrastructure needed.

---

## 3. The Architecture

### 3.1 The Two States

| | Global State | Personal State |
|---|---|---|
| **What it is** | The university's catalog — everything VU *offers* | The learner's knowledge — everything you *know* |
| **Structure** | Relational database (DDC-influenced hierarchy) | Knowledge graph (progressive, extracted from learning) |
| **Schema origin** | Dewey Decimal Classification × OpenCourseWare course structure | Extracted from notebooks, paper KGs, voice notes, mastery tracking |
| **User-facing form** | "Courses the university offers" | "Your knowledge map" — nodes, edges, metaphors, mastery scores |
| **Why not a KG?** (global) | A catalog is a tree, not a graph. DDC is hierarchical. Forcing it into a KG is wasted work. | — |
| **Why a KG?** (personal) | — | Your connections between concepts are unique to you. They *are* a graph. They drive learning trajectories. |

### 3.2 The Notebook as Dual-Purpose Artifact

```
Notebook = Active Learning Session + Unprocessed Personal State Unit
```

While you're in it → it's your classroom (notes, code, AI interaction, exercises).
After you're done → it's raw material for KG extraction (concepts learned, connections made, metaphors used, doubts resolved).

### 3.3 The Cell Contract

| Cell Type | Purpose | AI Trigger? |
|---|---|---|
| **Markdown** | Your notes, thoughts, questions written as prose | **No.** Passive. The learner's private space. |
| **Code** | Harness calls, exercises, AI interaction prompts | **Yes.** `Shift+Enter` execution wakes the tutor via `jupyter-tutor` poller. |

### 3.4 The Audio Contract

| Stage | What Happens | Tool |
|---|---|---|
| **During learning** | Record voice thoughts as `.mp3` files alongside the notebook | Device mic / simple recorder |
| **Real-time AI response** | agy cli can read `.mp3` directly — no transcription needed for immediate interaction | agy cli multimodal |
| **Later processing** | Audio transcribed for personal state updates (mastery, metaphors, doubts) | Nightly pipeline |

### 3.5 The Paper KG Pipeline

```
Hand-draw KG on paper while learning
        ↓
Photograph it → store as image in notebook directory
        ↓
Record voice note explaining the drawing → store as .mp3
        ↓
Image + Audio → LLM extracts structured KG (nodes, edges, labels)
        ↓
Digital KG rendered per notebook → joins into global personal state KG
```

### 3.6 Component Topology (Laptop-as-Server)

```
┌─────────────────────────────────────────────────────────┐
│                    This Laptop                          │
│                                                         │
│  ┌──────────────┐     ┌──────────────────────────────┐  │
│  │ Frontend     │────▶│ Jupyter Server (port 8888)   │  │
│  │ (Vite/React) │◀────│  ├─ Contents REST API        │  │
│  │ localhost:5173│ WS  │  ├─ Kernel WebSocket         │  │
│  └──────────────┘     │  └─ .ipynb files on disk     │  │
│                       └──────────┬───────────────────┘  │
│                                  │ file change           │
│                       ┌──────────▼───────────────────┐  │
│                       │ agy cli + jupyter-tutor      │  │
│                       │  ├─ Polls for Shift+Enter    │  │
│                       │  ├─ Reads notebook + .mp3    │  │
│                       │  └─ Appends response cells   │  │
│                       └──────────────────────────────┘  │
│                                                         │
│  ┌──────────────┐     ┌──────────────────────────────┐  │
│  │ SQLite DB    │     │ nlm cli (NotebookLM)         │  │
│  │ ├─ Catalog   │     │  └─ Batch content generation │  │
│  │ └─ Personal  │     └──────────────────────────────┘  │
│  │    State     │                                       │
│  └──────────────┘                                       │
└─────────────────────────────────────────────────────────┘
```

### 3.7 Future Topology (Pi + Cloudflare)

```
┌─────────────────────────┐         ┌────────────────────┐
│ Raspberry Pi (always-on)│         │ Cloudflare Pages   │
│  ├─ Jupyter Server      │◀───────▶│  └─ Frontend (PWA) │
│  ├─ agy cli             │  HTTPS  │                    │
│  ├─ SQLite databases    │         └────────────────────┘
│  ├─ nlm cli             │
│  └─ Nightly pipeline    │
└─────────────────────────┘
```

---

## 4. The MVP Definition

**The working MVP = end of Phase 3.**

> *"A single course notebook opens in the browser. You read markdown content. You write notes in markdown cells. You execute a code cell and the tutor responds. Your .mp3 voice thoughts are understood. The notebook saves. It all just works."*

Everything after Phase 3 is **enrichment** — building the catalog, extracting KGs, generating content overnight, making it beautiful. The core loop must work first.

---

## 5. Timeline at a Glance

| Phase | Name | Focus | Status |
|---|---|---|---|
| 0 | Heritage & Foundation | Vision charter & archived cold storage | ✅ DONE |
| 1 | The Local Engine | Jupyter Server + notebook lifecycle | ✅ DONE |
| 2 | The Minimal Canvas | Headless cell UI in React | ✅ DONE |
| 3 | The Seamless Loop | Frontend ↔ Jupyter ↔ agy cli wired end-to-end | **MVP** ✅ DONE |
| 4 | The Catalog Engine | DDC schema, course hierarchy, library UI (clean/synthetic only) | ⬜ |
| 5 | The Personal State | SQLite KG, mastery tracking, extraction pipeline (clean/mock verification) | ⬜ |
| 6 | The Nightly Pipeline | Batch processing, content generation, KG extraction | ⬜ |
| 7 | Deployment & Polish | Pi server, Cloudflare frontend, university aesthetic | ⬜ |
| 8 | The Grand Hydration | Hydrate heritage data (671 chapters, 4,720 nodes, 2,839 PYQs, EVS) | ⬜ |

> **Iron Law**: Phases 1 through 7 are built and tested **100% clean without data hydration**. We use only minimal synthetic fixtures (1 mock course, 1 mock lecture, dummy concept atoms) to build and verify the engines. The heritage data in `heritage/` is hydrated into the system strictly in **Phase 8**, after the entire machine is proven.

---

## 6. The Phases

---

### Phase 0 — Heritage & Foundation ✅ DONE

**What exists:**

- **FOUNDATION.md**: The vision and philosophical charter (university metaphor, living loop, progressive KG, linguistic register). Original seed archived in `docs/archive/FOUNDATION_ORIGINAL.md`.
- **DDC taxonomy**: Complete 10-class Dewey Decimal directory structure (000–900) with subdivisions.
- **Heritage assets** (`heritage/` — **Cold Storage / Unhydrated**):
  - 671 clean HTML chapters (357 NCERT + 314 reference books) with `manifest.json`.
  - 4,720 canonical concept nodes (`node_lookup.json`, 1.76 MB).
  - 2,839 PYQs with 6,064 concept links.
  - 1,812 curated edges + 674 cross-subject semantic edges.
  - 77 atomic EVS chapter ledgers (Classes 3–6) + 7 thematic spiral units.
  - 2,827 extended ontology nodes (Indian Constitution articles, InPhO philosophy, CS/AI concepts).
  - Discrimination cards, drill clusters, bilingual transcripts, concept illustrations.
- **Pipeline scripts** (`pipeline/`): Zero-loss extraction, NotebookLM steering manifests, verification gates.
- **Tooling docs** (`tooling/`): `notebooklm-py` and `notebooklm-mcp-cli` evaluation.
- **jupyter-tutor skill**: Working notebook poller + cell appender + reader scripts.

**Deficits & Hydration Constraint:**
- No database schema exists (catalog or personal state).
- No notebook templates exist for courses.
- **Hydration Boundary**: Heritage data remains strictly cold in `heritage/` until Phase 8. Do NOT attempt to ingest or compile heritage files while constructing Phases 1–7. Build the system first.

---

### Phase 1 — The Local Engine ✅ DONE

**Goal:** Jupyter Server running headlessly on this laptop with CORS enabled, and the ability to programmatically create, read, execute, and save notebooks.

**Deliverables:**

- [x] Jupyter Server configured and launchable via a single command (`./start.sh`).
  - Token-based auth (`token: 'sahacit-dev'`).
  - CORS headers allowing `localhost:5173` (Vite dev server).
  - Notebook root directory: `sahacit/library/` (clean in-repo library).
  - Fixed kernelspec interpreter path to `sahacit/.venv/bin/python`.
- [x] Clean test notebook (`library/test/sandbox.ipynb`) created programmatically.
- [x] Proof that `@jupyterlab/services` and Python REST client can:
  - Fetch notebook contents via REST.
  - Start a kernel session and execute code.
  - Save the notebook back via PUT.
- [x] Dynamic external modification detection verified via REST API `last_modified` polling.
- [x] Automated test suite in `tests/test_substrate.py` verifying all 5 engine criteria end-to-end.

**Exit criteria:**
A script (`tests/test_substrate.py`) loads a notebook, starts a kernel session, modifies files externally, and verifies updates via the Contents API — all headless without opening JupyterLab UI.

---

### Phase 2 — The Minimal Canvas ✅ DONE

**Goal:** A browser-based cell renderer with live side-by-side editing and lightweight library exploration.

**Stack:** React + TypeScript + Vite.

**Deliverables:**

- [x] Vite React TS app scaffolded in `web/` (builds cleanly with zero errors).
- [x] Dependencies installed: `@jupyterlab/services`, `@uiw/react-codemirror`, `react-markdown`, `rehype-katex`, `remark-math`, `remark-gfm`, `ansi-to-html`.
- [x] `NotebookView` component:
  - Loads notebook JSON from Jupyter Server on mount.
  - Renders ordered list of cells.
  - Debounced auto-save on change & blur.
  - Polls `last_modified` every 1.2s to hot-merge external modifications smoothly.
- [x] `CellView` component:
  - **Code cell**: CodeMirror 6 editor with Python syntax highlighting, execution counter gutter, play button, and execution state indicator.
  - **Side-by-side Markdown cell**: CodeMirror editor on the left pane, live KaTeX/Markdown preview on the right pane, with an optional toggle button to collapse to preview-only mode.
  - **Output container**: Renders outputs by MIME type (`text/plain`, `text/html`, `image/png`, error tracebacks with ANSI coloring).
- [x] Cell controls:
  - Top and per-cell hover controls (`+ Code`, `+ Markdown`, `Delete`).
  - Cells insertable at any position and deletable.
- [x] `FileExplorer` component:
  - Powered by Jupyter Contents API to browse directories and `.ipynb` files in `sahacit/library/`.
  - Create new untitled notebook directly into current directory.
  - Collapsible sidebar with quick toggle.
- [x] URL query param sync (`?path=...`) to directly open and share any notebook.

**Exit criteria:**
Opening `localhost:5173` displays the clean canvas and library explorer, renders KaTeX math live alongside the Markdown editor, executes code cells through the kernel, and inserts/deletes cells seamlessly.

---

### Phase 3 — The Seamless Loop (MVP) ✅ DONE

**Goal:** Wire the three components into a single, working loop: User edits in browser → Jupyter kernel executes → agy cli responds → UI updates.

**Deliverables:**

- [x] **Execution path**: User presses Shift+Enter in a code cell → frontend sends `execute_request` via WebSocket to Jupyter kernel → output streams back and renders in the output container → frontend PUTs the updated notebook to Jupyter Server (saves to disk).
- [x] **Tutor wakeup**: `jupyter-tutor` poller running in `sahacit-tutor` tmux session, watching the active notebook. When a code cell with `#` comments or an error is executed, agy cli wakes up, reads the notebook, and appends a response (markdown + optional code cell).
- [x] **UI hot-reload**: Frontend detects file changes (via polling the Contents API `last_modified` timestamp every 1.2s) and smoothly merges new cells into the view without losing scroll position or focus.
- [x] **Audio integration**: Code cells can reference `.mp3` files; agy cli multimodal handles spoken audio directly.
- [x] **Save semantics**: Side-by-side Markdown cell edits auto-save on typing and blur. The notebook file on disk is always the source of truth.

**Exit criteria:**
1. Open a notebook in the browser (`http://localhost:5173/?path=test/sandbox.ipynb`).
2. Write `# explain how the gradient vector points in the direction of steepest ascent` in a code cell. Press Shift+Enter.
3. agy cli wakes up within seconds, reads the notebook, and appends an explanation cell + numerical verification cell.
4. The explanation appears in the browser without manual refresh.
5. Record a voice thought as `.mp3`, reference it in a code cell, and agy cli understands it.

**The MVP is Live & Verified.** 🎯

---

### Phase 4 — The Catalog Engine (Global State)

> **Core Rule**: Build clean without data hydration. Seed the catalog strictly with 1–2 synthetic dummy courses to verify schema, CRUD operations, tree hierarchy, and UI navigation. Do NOT ingest the 671 NCERT chapters, 77 EVS ledgers, or PYQs here.

**Goal:** Build the university's course catalog engine — the DDC-influenced relational database and UI that organizes courses, lectures, and starter notebooks.

**Deliverables:**

- [ ] **Catalog database schema** (SQLite: `catalog.db`):
  ```
  subjects          — DDC-aligned subject areas (e.g., "500 — Science", "320 — Political Science")
  courses           — Named learning trajectories (e.g., "TEST-101 — Intro to Algorithms")
  lectures          — Ordered units within a course
  lecture_sources   — Links to source material (syllabus ref, doc ref)
  notebooks         — The .ipynb file pointers per lecture
  ```
- [ ] **OpenCourseWare / Course Scaffolder**:
  - A script/utility to create a course and scaffold starter `.ipynb` lecture notebooks from a syllabus template.
  - Tested against a synthetic sample syllabus (e.g. 3 dummy lectures).
- [ ] **Synthetic Test Catalog**:
  - Seed 1–2 mock courses (e.g. `TEST-101: Foundational Computing`, `TEST-201: Natural Philosophy`) with sample markdown and exercise cells.
  - Verify course creation, lecture ordering, and starter notebook creation.
- [ ] **Course Library UI**:
  - A clean catalog/library view listing courses grouped by DDC class.
  - Clicking a course lists its lectures.
  - Clicking a lecture opens its notebook directly into the cell canvas.

**Exit criteria:**
Opening the app allows navigating from DDC classes to a synthetic test course, seeing its lectures, and clicking a lecture opens its starter notebook in the cell canvas ready for learning. Zero heritage data hydrated.

---

### Phase 5 — The Personal State (Progressive KG)

> **Core Rule**: Build and verify the personal state engine using clean test sessions and synthetic concept nodes. Do NOT bulk-preload the 4,720 canonical nodes or 2,827 ontology nodes into the personal state database.

**Goal:** Build the personal knowledge graph engine — starting from notebooks and paper KGs, progressively crystallized into a structured, queryable graph.

**Deliverables:**

- [ ] **Personal state database schema** (SQLite: `personal_state.db`):
  ```
  enrolled_courses     — Courses the learner has started (subset of catalog)
  notebook_progress    — Per-notebook: status (active/completed/reviewing), time spent, last opened
  concept_nodes        — Extracted concept atoms from completed notebooks
  concept_edges        — Connections between concepts (extracted from learning, paper KGs, cross-notebook links)
  personal_metaphors   — Metaphor text, accuracy score, active flag, source notebook, timestamp
  mastery_scores       — Per-concept: score (0.0–1.0), status, half_life, encounter_count, next_review_at
  mastery_events       — Event log (ATTEMPT, METAPHOR_REFINED, NOTEBOOK_COMPLETED, CALIBRATION)
  paper_kgs            — Image path, voice note path, extraction status, source notebook
  audio_captures       — .mp3 path, transcription status, extracted insights, source notebook
  ```
- [ ] **Notebook → KG extraction pipeline**:
  - When a notebook is marked "completed," an LLM pass extracts:
    - Concepts learned (new concept nodes).
    - Connections made (new edges, especially cross-course bridges).
    - Metaphors used (personal_metaphors entries).
    - Doubts resolved vs. remaining.
  - Extracted data inserted into the personal state database.
- [ ] **Paper KG pipeline**:
  - Photo + voice note stored in notebook directory.
  - LLM (multimodal) processes image + audio → structured graph JSON.
  - Rendered as a digital KG and merged into personal state.
- [ ] **Mastery tracking**:
  - Ebbinghaus decay formula: `retention = exp(-(ln2 / half_life) × elapsed_days)`.
  - Status transitions: `UNEXPLORED → LEARNING → MASTERED → FADING → REVIEW_DUE`.
  - Spaced repetition scheduling (next_review_at) driven by half_life and encounter_count.
- [ ] **Personal state visualization** (minimal):
  - A view showing the learner's concept nodes and edges as a rendered graph.
  - Color-coded by mastery status (green mastered, amber learning, red fading, grey unexplored).

**Exit criteria:**
After completing 3 test notebooks across 2 mock courses, the personal state KG shows extracted concepts with edges between them — including at least one cross-course connection. A paper KG photo + voice note is successfully extracted into the digital graph.

---

### Phase 6 — The Nightly Pipeline (Batch Processing)

**Goal:** The asynchronous intelligence layer. Processes today's learning overnight, prepares tomorrow's material.

**Deliverables:**

- [ ] **Audio processing pipeline**:
  - All `.mp3` captures from the day → transcribed (Whisper or cloud API).
  - Transcripts → LLM reasoning pass:
    - Extract: doubts, confusions, "aha" moments.
    - Extract: personal metaphors.
    - Update: mastery scores based on engagement evidence.
    - Flag: metaphor corrections needed.
- [ ] **Content generation pipeline**:
  - Based on weekly trajectory + updated personal state → generate next day's notebook content.
  - Uses NotebookLM (`nlm` CLI) with steering manifests for:
    - Audio overviews / conversational podcasts.
    - Study guides and structured notes (compiled into notebook markdown cells).
    - Exercises and formative checks (compiled into notebook code cells).
- [ ] **KG consolidation**:
  - Nightly merge of day's notebook extractions into the global personal state KG.
  - Edge deduplication and conflict resolution.
  - Mastery decay recalculation across all concepts.
- [ ] **Pipeline orchestration**:
  - A single entry point (script or Makefile target) that runs the full nightly cycle.
  - Idempotent — safe to re-run.

**Exit criteria:**
After a day of learning (3+ notebooks engaged, 2+ audio captures), running the nightly pipeline produces: updated mastery scores, new personal KG edges, transcribed audio with extracted insights, and a generated starter notebook for tomorrow's next lecture.

---

### Phase 7 — Deployment & Polish

**Goal:** Move from laptop to production. Make it beautiful.

**Deliverables:**

- [ ] **Raspberry Pi deployment**:
  - Jupyter Server running as a systemd service.
  - agy cli + jupyter-tutor poller running as a daemon.
  - SQLite databases on Pi storage.
  - Nightly pipeline triggered by cron.
  - Accessible from the local network (and optionally via Cloudflare Tunnel).
- [ ] **Cloudflare Pages frontend**:
  - The React app built and deployed to Cloudflare Pages.
  - Connects to Pi's Jupyter Server over HTTPS (via Cloudflare Tunnel or direct).
- [ ] **University aesthetic**:
  - Typography, spacing, color palette that feels like a personal university.
  - Dark mode.
  - Smooth animations for cell insertion/deletion.
  - Course library feels like browsing a university catalog.
  - Personal state KG visualization is beautiful and interactive.
- [ ] **Mobile/tablet responsive**:
  - The cell canvas works on iPad / tablet for reading and note-taking.

**Exit criteria:**
The full system runs on the Pi. The frontend is accessible from any device on the network. It looks and feels like *your* university.

---

### Phase 8 — The Grand Hydration (Heritage Ingestion)

> **The Final Step**: The system engines, canvas, loop, catalog UI, personal state KG, nightly pipelines, and deployment are fully built and verified with zero real data. Only now is the accumulated heritage data hydrated into the live, working system.

**Goal:** Hydrate the production system with all canonical intellectual assets accumulated in `heritage/`.

**Deliverables:**

- [ ] **Catalog Hydration (671 Chapters)**:
  - Batch compiler script reading `heritage/library/manifest.json`, `heritage/library/ncert/`, `heritage/library/ref/`, and `heritage/surfaces/`.
  - Map chapters into DDC-classified courses (`300 Social Sciences`, `500 Natural Sciences`, `900 History & Geography`) in `catalog.db`.
  - Generate clean starter `.ipynb` lecture notebooks for all courses.
- [ ] **Ritual Journey Hydration (77 EVS Ledgers & 7 Spiral Units)**:
  - Compile the 77 atomic EVS chapter ledgers (Classes 3–6) and 7 thematic spiral units into the Classes 1–10 calibration journey courses.
- [ ] **Formative PYQ Bank Hydration (2,839 Questions)**:
  - Ingest `upsc_prelims_pyq.json` and `pyq_master_bank.json`.
  - Link questions to relevant courses and embed formative check cells into corresponding review notebooks.
- [ ] **Canonical Vocabulary & Glossary Ingestion (4,720 Nodes)**:
  - Load `heritage/frontend-data/node_lookup.json` (4,720 nodes) into a read-only concept glossary lookup database for the Phase 5/6 extraction pipeline.
  - Ensure extractor accurately grounds learner concepts to canonical node IDs without polluting personal state with unlearned nodes.
- [ ] **Media & Illustration Assets**:
  - Link and verify high-resolution concept illustrations (visuals, geography diagrams) within course notebooks.
- [ ] **End-to-End System Audit**:
  - Verify every hydrated course opens cleanly in the canvas.
  - Verify starter notebooks execute correctly and seamlessly invoke the tutor.

**Exit criteria:**
The catalog displays the full university curriculum with all 671 chapters across DDC classes and the complete Classes 1–10 ritual journey; lecture notebooks open instantly with canonical text, illustrations, and embedded formative questions; the tutor grounds queries against the 4,720-node vocabulary.

---

## 7. What Carries Forward from `22` and `preach`

> **Note on Hydration Timing**: All assets listed below are preserved in `heritage/` as cold archives. They are hydrated into the live system exclusively in **Phase 8**, strictly after all system components and loops in Phases 1–7 are built and verified.

### Heritage Assets (Preserved for Phase 8 Hydration)
- **671 chapters** (NCERT + reference books) with complete manifest → seed the catalog's NCERT courses.
- **4,720 canonical concept nodes** → seed the personal state KG's vocabulary when encountered during learning.
- **2,839 PYQs** with concept links → evaluation material for courses.
- **77 EVS atomic ledgers** + 7 thematic spiral units → the ritual journey (Classes 1–10) course content.
- **2,827 external ontology nodes** (Constitution, Philosophy, CS) → enrichment for cross-domain KG edges.
- **Discrimination cards & drill clusters** → exercise material for notebook code cells.
- **Concept illustrations** (SVG/WebP) → visual aids embedded in notebook markdown cells.

### Methodologies (Proven & Preserved)
- **Zero-loss extraction** (`preach`): deterministic entity extraction → entity ledger → verification gates.
- **Route C** (`22`): objective vector discovery + selective LLM labelling for KG edge construction.
- **Cognitive science foundations**: Method of Loci, dual coding, spaced repetition (Ebbinghaus), retrieval practice, desirable difficulties.
- **The 4-Layer Concept Model**: Core Knowledge → Narrative → Application → Personal State.
- **Steering manifest architecture**: structured prompts for NotebookLM batch generation.

### Naming Conventions & Metaphors (Preserved)
- *"The Castle"* / *"The Memory Palace"* — structural externalization of knowledge.
- *"Canonical Facts vs. Personal Metaphors"* — the distinction between source truth and personal understanding.
- *"Cognitive Overlay / Heatmap"* — visualization of mastery state (green/amber/red/grey).
- *"Route C"* — the KG construction methodology.
- *"Discriminating Detail"* — 50–75 word concept descriptions focused on recognition, not encyclopedic prose.
- *"The Ritual Journey"* — Classes 1–10 calibration phase.
- *"The Value Spine"* — construction sequencing principles.

---

## 8. What's Decided (vs. `FOUNDATION.md` §11)

The original FOUNDATION.md listed 6 undecided items. Current status:

| Question | Decision |
|---|---|
| **Nightly pipeline infrastructure** | Runs locally on this laptop during dev. Moves to Pi for production. |
| **App platform** | React + Vite SPA. Deployed to Cloudflare Pages for production. |
| **Storage architecture** | SQLite (local-first). Two databases: catalog + personal state. |
| **Audio handling** | Raw `.mp3` stored alongside notebooks. agy cli reads them directly. Transcription deferred to nightly pipeline (Whisper or cloud API — TBD). |
| **Deployment topology** | Laptop (dev) → Pi + Cloudflare Tunnel (production). |
| **Exam-specific course design** | Courses scaffolded from OCW syllabuses + NCERT + exam syllabuses. DDC classification per course. Heritage PYQ corpus provides evaluation layer. |

---

## 9. The Global State Does Not Need to Be a KG

This is a deliberate architectural decision, worth recording explicitly.

The **global state** (catalog) is a tree: `DDC Class → Subject → Course → Lecture → Notebook`. Trees are hierarchical. Relational databases model trees perfectly. A KG adds edges between arbitrary nodes — but the catalog's value is in its *organization*, not in cross-catalog connections.

The **personal state** is where a KG earns its keep. When the learner connects binary heaps to priority queues to Dijkstra's algorithm to the Indian Railways network — those edges exist only in their head. No catalog contains them. They drive learning trajectories: "you understood X and Y, so Z bridges both."

**Knowledge progressively KG-ifies from global catalog into personal state.** The notebook is the transformation medium:

```
Catalog (tree) → Notebook (learning session) → Personal State (graph)
```

The global catalog never needs to be a graph. Its knowledge becomes graph-shaped only after passing through the learner.
