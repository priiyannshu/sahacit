# 22 System State & Architectural Blueprint

> **Date & Version**: 2026-07-28 | v3.1.0-master-plan  
> **Repository**: `22` (Cloudflare Workers + D1 + Vectorize + Durable Objects)  
> **App URL**: [https://22.priyanshukh1201.workers.dev](https://22.priyanshukh1201.workers.dev)  
> **Ingestion Status**: ✅ **100% COMPLETE & HYDRATED**  
> **Governing documents**: [`MASTER_PLAN.md`](MASTER_PLAN.md) (the build timeline) · [`VISION.md`](VISION.md) (the architectural blueprint)

---

## 1. Executive Summary & Vision

**22** is a personal, edge-native, multimodal learning infrastructure designed to replicate and digitize knowledge for Priyanshu (age 22). It is NOT a generic quiz app or a simple note-taking system—it is a **4-Layered Multi-Graph Engine** built to enable cross-subject concept linking, spaced repetition memory decay, handwritten note semantizing, and visual force-directed graph exploration.

*   **No Authentication / Single User**: Auth code/picker was completely removed/bypassed. The system auto-logs in as `Priyanshu`.
*   **Original UI Restored**: `app.js` and `game.css` were preserved in their exact original form per explicit user request. UI design will happen in a separate dedicated phase.
*   **Edge Stack**: Cloudflare Workers, Cloudflare D1 (SQLite), Cloudflare Vectorize (768-dim BGE Base), Cloudflare Durable Objects (`UPSCTutorAgent`), Workers AI (`Llama 3.1 8B Instruct`, `Llama 3.2 11B Vision`).

---

## 1A. Build Timeline Position (per `MASTER_PLAN.md`)

> **Active Phase**: **Phase 1 — Semantic Layer Completion** (Stage 1, CLI)  
> **MVP Status**: ⬜ **Not yet** — the working MVP completes at the end of **Phase 6** (MASTER_PLAN.md §3)  
> **Position last updated**: 2026-07-28 (session 3 — merged to `main` as PR #2) — Phase 1 IN PROGRESS (KG-only semantic layer COMPLETE: 2,827 nodes + 828 edges in D1, 674 cross-subject semantic_edges, Vectorize clean. Remaining: R2 buckets + optional UPSC embedding)

| Phase | Name | Status |
|---|---|---|---|
| 0 | Foundation | ✅ DONE (2026-07-27) |
| 1 | Semantic Layer Completion | 🔵 **ACTIVE — IN PROGRESS** |
| 2 | Personal State Schema | ⬜ Pending |
| 3 | DO↔D1 Sync | ⬜ Pending |
| 4 | Hybrid Context Assembly | ⬜ Pending |
| 5 | The Blob Interface (Both Doors) | ⬜ Pending |
| 6 | Metaphor System v1 → 🏁 **MVP** | ⬜ Pending |
| 7–13 | Scaling phases (calibration → cron → voice → KG expansion → viz → integrity → native) | ⬜ Pending (see MASTER_PLAN.md §2) |

### Known Deficits (carried into Phase 1, per VISION.md Part 1)

1. **Vectorize population**: KG layer 100% populated (2,827 KG vectors upserted, all `polity_art_*` / `phil_*` / `cs_*`). UPSC `master_nodes` (4,720) NOT yet embedded — **deferred by user decision** (KG-only focus for now; revisit in Phase 10 or when discovery across UPSC nodes is needed). → Phase 1 / Phase 10.
2. **R2 unbound** — `MEDIA_BUCKET` is optional in `Env` and absent from `wrangler.jsonc`. → Phase 1 fixes.
3. **DO↔D1 unsynced** — tutor learner state dies with the session; D1 and the DO are two separate stores. → Phase 3 fixes.
4. **Two-door schema missing** — none of the 10 new tables (`persistent_sessions`, `personal_metaphors`, `natural_language_aliases`, etc.) exist yet. → Phase 2 fixes.

---

## 5. This Session — 2026-07-28 (Session 2)

**Branch**: `main` (no new branch created this session; exploratory work)
**Commits**: 0 (all work was local/exploratory)
**Untracked artifacts produced**: `kg/`, `models/`, `app/pipeline/ingest_kg.py`

### Achieved

| Work Item | Details |
|---|---|
| **D1 Export** | All 4,720 existing `master_nodes` exported → `app/data/kg/output/old_master_nodes_archive.json`; 100 vector IDs listed in `app/data/kg/output/old_vector_ids.txt` |
| **BGE Base Model** | Downloaded `BAAI/bge-base-en-v1.5` (768-dim) to `app/data/models/kg-embeddings/` — ready for local embedding pass |
| **KG Ingestion Script** | Wrote `app/pipeline/ingest_kg.py` — extracts nodes from 3 external KGs (Indian Constitution via `indianconstitution` pkg, InPhO philosophy ontology, CS/AI seed concepts), embeds locally, outputs SQL |
| **External KG Extraction** | 2,827 new nodes extracted: **464 polity** (Indian Constitution articles), **2,209 philosophy** (InPhO thinkers/ideas), **154 CS/AI** (seed concepts) → `app/data/kg/output/all_nodes.json` |
| **Edge Extraction** | 828 edges: 192 cross-references (polity articles), 636 influenced-by (philosophy) → `app/data/kg/output/all_edges.json` |
| **Local Embedding Pass** | All 2,827 new nodes embedded with BGE Base → `app/data/kg/output/vectors.ndjson` (48 MB, 768-dim normalized vectors) |
| **SQL Generation** | `app/data/kg/output/insert_nodes.sql` (5,206 lines) + `insert_edges.sql` (828 lines) for D1 batch insertion |

### What Was NOT Done / Deferred (carried forward)

1. **Existing 4,720 UPSC nodes NOT embedded** — **deferred by user decision** ("only the KG ones for now"). Vectorize currently holds ONLY the 2,827 KG vectors; the UPSC `master_nodes` have no embeddings. Revisit when cross-UPSC discovery is needed (Phase 10 KG expansion pattern).
2. **R2 buckets NOT created or bound** in `wrangler.jsonc` — still pending (Phase 1 deliverable). `MEDIA_BUCKET` remains optional/unbound.
3. **`reasoning` field on `semantic_edges` is NULL** — deferred; user chose "LLM reasoning later" (backfill via a batch Worker AI job for edges ≥ 0.85).

### Done This Session (Session 3 — 2026-07-28)

| Work Item | Details |
|---|---|
| **Vectorize verified clean** | Scanned all 2,827 vector IDs via `list-vectors` pagination — **0 UPSC strays**. Index holds exactly the 2,827 KG embeddings (`polity_art_*`, `phil_*`, `cs_*`). |
| **KG nodes confirmed in D1** | 2,827 rows in `master_nodes` (subjects: polity 464, philosophy 2,209, cs 154). Confirmed already-merged in prior session. |
| **KG edges confirmed in D1** | 828 `cross_references` rows in `master_edges` (source/target are KG node IDs). Confirmed already-merged. |
| **Cross-subject semantic edges computed** | Local cosine over the 2,827 normalized BGE vectors, threshold **0.65** (user chose over planned 0.75 — 0.75 yielded only 22, all philosophy↔cs). Result: **674 edges** → `app/data/kg/output/insert_semantic_edges.sql` → inserted into `semantic_edges`. |
| **Edge breakdown** | `philosophy ↔ cs`: 669 · `polity ↔ philosophy`: 5 · `polity ↔ cs`: 0 (polity region maxes at 0.575 cosine — no bridge at 0.65). |
| **D1 verification** | `SELECT COUNT(*) FROM semantic_edges` = 674. Top edge: `cs_turing_machine ↔ phil_turing_machine` @ 0.9417. |

### Notable Observation
The **polity (Constitution) nodes sit in a near-isolated embedding region** — they form almost no cross-subject bridges even at 0.65 (polity↔cs max 0.575, polity↔philosophy max 0.686). If richer polity cross-links are wanted later, either (a) lower the threshold on just those pairs, or (b) expand the polity KG with more conceptually-adjacent nodes.

### Phase 1 Progress

| Deliverable | Status |
|---|---|
| Local BGE Base embedding script ready | ✅ `app/pipeline/ingest_kg.py` + model at `app/data/models/kg-embeddings/` |
| Embed 2,827 KG nodes → Vectorize | ✅ 2,827 vectors upserted, verified clean (0 UPSC strays) |
| 2,827 new KG nodes → D1 | ✅ 2,827 `master_nodes` + 828 `master_edges` merged |
| Cross-subject semantic edges (KG-only) | ✅ 674 edges @ cosine ≥ 0.65 (`semantic_edges` populated) |
| Embed 4,720 UPSC nodes → Vectorize | ⬜ Deferred by user (KG-only focus) |
| R2 buckets created + bound | ⬜ Pending (Phase 1 deliverable) |

### Next Session — 2026-07-28 (Session 4) Plan

**Test (user-driven):** User will ask the agent to "tell me the semantic edges from my Vectorize" — i.e. verify discovery works end-to-end by querying Vectorize / reading `semantic_edges` from D1 and reporting cross-subject connections (e.g. similar concepts to a given node). Pre-req for this test is already satisfied: Vectorize clean + `semantic_edges` populated. A CLI coding agent can run all of this directly via `wrangler` (D1 `execute`, `vectorize query`, `r2` — see AGENTS.md §6).

**Remaining Phase 1 deliverables (ordered):**
1. **R2 buckets** — `wrangler r2 bucket create session-archives && wrangler r2 bucket create raw-inbox`; add `MEDIA_BUCKET` binding to `wrangler.jsonc`. Verify Worker read/write of a test object.
2. **(Optional / deferred) UPSC embedding** — only if cross-UPSC discovery is needed: embed 4,720 `master_nodes` locally (reuse `ingest_kg.py` logic on `old_master_nodes_archive.json`), upsert to Vectorize, then recompute semantic edges across the full graph. **User has deferred this for now.**
3. **(Optional / deferred) LLM reasoning backfill** — batch Worker AI job to populate `semantic_edges.reasoning` for edges ≥ 0.85.
4. **Verification + PR** — run `/api/node/:id` semantic-neighbor check, update checkboxes in MASTER_PLAN.md, commit on a feature branch, PR, merge on approval.

### Key Artifacts Reference

| Path | Description |
|---|---|
| `app/pipeline/ingest_kg.py` | KG extraction + embedding pipeline (polity/philosophy/cs) |
| `app/data/models/kg-embeddings/` | BGE Base EN v1.5 (768-dim) downloaded from HuggingFace |
| `app/data/kg/output/all_nodes.json` | 2,827 new KG nodes (polity 464, philosophy 2,209, cs 154) |
| `app/data/kg/output/all_edges.json` | 828 edges (polity cross-refs 192 + philosophy influenced 636) |
| `app/data/kg/output/vectors.ndjson` | 48 MB of 768-dim normalized vectors for the 2,827 new nodes |
| `app/data/kg/output/old_master_nodes_archive.json` | D1 export of all 4,720 existing master_nodes |
| `app/data/kg/output/old_vector_ids.txt` | IDs of ~100 nodes that have old Workers AI embeddings in Vectorize |
| `app/data/kg/output/insert_nodes.sql` | SQL to batch-insert new nodes into D1 |
| `app/data/kg/output/insert_edges.sql` | SQL to batch-insert new edges into D1 |
| `app/data/kg/output/insert_semantic_edges.sql` | SQL to insert 674 cross-subject `semantic_edges` (cosine ≥ 0.65, reasoning NULL) into D1 |
| `kg/inpho/inpho.owl` | InPhO philosophy ontology source (OWL) |

---

## 2. All Design Choices & Architectural Decisions

### A. The 4-Layered Multi-Graph Architecture

| Layer | Component | Description & Design Decision |
|---|---|---|
| **Layer 1: Core Knowledge** | `master_nodes` | **One Canonical Node**: A concept (e.g. *Federalism*, *Inflation*) is a single atom of truth regardless of how many books/chapters mention it. |
| **Layer 2: Narrative Layer** | `chapters`, `chapter_nodes` | **Ordered Narrative Paths**: Chapters in books (NCERTs, Laxmikanth, Ramesh Singh) are playlists/paths through Layer 1. `seq_position` preserves exact chapter reading order. |
| **Layer 3: Application Layer** | `pyq_corpus`, `pyq_node_links`, `pyq_attempts` | **Evaluation Nodes**: PYQs test concepts. Each attempt logs option chosen + time taken (`time_taken_ms`) as dual signals for the heat algorithm. |
| **Layer 4: Personal State** | `node_mastery`, `chapter_progress` | **Cognitive Overlay (Heatmap)**: Durable Object / D1 state tracking per-node mastery (0.0 to 1.0), encounter count, Ebbinghaus decay, and reading position bookmarks. |

### B. Dual Edge System
- **Curated Edges (`master_edges`)**: Structural, author-intended relationships (`justified_by`, `example_of`, `led_to`, `includes`, `contrasted_with`) extracted directly from processed chapter JSONs.
- **Semantic Edges (`semantic_edges`)**: AI-computed cross-subject connections with mathematical similarity scores (Vectorize 768-dim cosine) + LLM reasoning strings.

### C. Data Source & Ingestion Strategy
- **Source of Truth**: The root `app/data/processed/` directory containing **375+ structured JSON chapter files** across NCERT (Polity, Economics, History, Geography, Science), Non-Temporal concepts, PYQ links (`pyq_links.json`), and Reference Books (`Laxmikanth`, `Ramesh Singh`, `Bipin Chandra`, etc.).
- **Bypassing CF AI Limits**: Bulk node ingestion uses `/api/ingest/batch-raw` which writes directly to D1 in batches of 50 without hitting Workers AI inline. This solved the Cloudflare HTTP 429 / connection drop issues.

---

## 3. Database Schema Overview (Migrations `0001` - `0004`)

### Live Hydrated Counts in D1 (`prelims-master-db`):

| Table | Layer | Live Record Count | Status |
|---|---|---|---|
| `master_nodes` | Layer 1: Core Knowledge | **4,720 nodes** | ✅ 100% Hydrated |
| `chapters` | Layer 2: Narrative | **373 chapters** | ✅ 100% Hydrated |
| `chapter_nodes` | Layer 2: Narrative Sequences | **5,233 linkages** | ✅ 100% Hydrated |
| `pyq_corpus` | Layer 3: Application Corpus | **2,839 PYQs** | ✅ 100% Hydrated |
| `pyq_node_links` | Layer 3: PYQ↔Node Links | **6,064 linkages** | ✅ 100% Hydrated |
| `master_edges` | Curated Edges | **1,812 edges** | ✅ 100% Hydrated |

---

## 4. API Routes Registry (`src/index.ts`)

| Endpoint | Method | Description |
|---|---|---|
| `/api/status` | GET | Health & active infrastructure versions |
| `/api/chapters` | GET / POST | List/create chapters with ordered node sequences |
| `/api/chapters/:id` | GET | Get chapter with full node sequence & progress |
| `/api/ingest/batch-raw` | POST | High-speed D1 batch node insertion (zero CF AI rate limits) |
| `/api/ingest/nodes` | POST | Ingest nodes + optional vector embeddings |
| `/api/pyq-links` | POST | Batch insert PYQ ↔ Node links |
| `/api/pyq-attempt` | POST | Log PYQ attempt (updates `node_mastery` heatmap) |
| `/api/node/:id` | GET | Full node detail with chapters, PYQs, mastery, & dual edges |
| `/api/node/:id/pyqs` | GET | List all PYQs testing a specific concept node |
| `/api/mastery` | GET | Fetch mastery heatmap data across nodes/subjects |
| `/api/chapter-progress` | POST | Update reading bookmark for a chapter |
| `/api/notes/upload` | POST | Upload handwritten note image → Vision AI OCR → D1 extraction |
| `/api/agent/chat` | POST | Socratic Tutor Chat (Durable Object + Llama 3.1 8B) |

---

## 6. Next Steps & Planning Ahead

> **This section is superseded by the master timeline.** All future work is sequenced in [`MASTER_PLAN.md`](MASTER_PLAN.md) and the live position is tracked in §1A above. The items previously listed here have been absorbed into the timeline.
>
> **Next session**: read §1A → open `MASTER_PLAN.md` at Phase 1 → follow the session protocol in `MASTER_PLAN.md` §8 → execute the ordered sequence in §5 (This Session's "Next Session Must") above.
