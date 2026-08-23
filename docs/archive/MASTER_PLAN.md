# 22 — Master Construction Plan

> **The one file carried until the end of construction.**
> **Version**: 1.0.0 | **Created**: 2026-07-28 | **Branch convention**: one branch per phase/task, PR, merge only on approval.
> **Companions**: `VISION.md` (the architectural blueprint — what & why) · `STATE.md` (live position marker — where we are on this timeline).

---

## 0. How to Use This File

1. **This file is the timeline.** It lists every phase required to take the application from its current state to the full vision in `VISION.md`, sequenced so the most valuable things are built earliest.
2. **STATE.md is the position marker.** At any moment, its "Build Timeline Position" section names the active phase, what's done, and what the next session should do. Update it at the end of every session.
3. **Phases have exit criteria.** A phase is DONE only when every exit criterion is verifiably true (counts in D1, endpoints responding, UI flows working on the deployed app). Never mark intent as done.
4. **MVP state vs Final state.** Every phase lists both. The MVP state is what must work when the phase exits. The final state is what it scales toward in later phases — recorded now so early decisions never foreclose it.
5. **Don't skip ahead casually.** Later phases assume earlier ones. If a session jumps ahead (a UI experiment, a spike), record the deviation in STATE.md.

---

## 1. The Value Spine (Why This Order)

Five principles determine the sequence:

1. **Data completeness before features.** A 15%-populated Vectorize means broken discovery everywhere. Fix the substrate first (Phase 1).
2. **Schema before behavior.** Sessions, metaphors, aliases, events can't exist without their tables (Phase 2).
3. **Sync before intelligence.** An unsynced tutor forgets you between sessions. Memory is the highest perceived-value feature (Phase 3).
4. **The core loop before the periphery.** Context assembly → both doors → metaphors is the smallest end-to-end version of the vision's promise (Phases 4–6 = MVP). Voice, visualization, and KG expansion are enhancements layered on a working loop.
5. **Free/CLI before paid/native.** Stage 1 does heavy lifting via local scripts at zero neuron cost. Native automation (Stage 2) and paid tier (Stage 3) arrive only when triggers fire (§5).

---

## 2. Timeline at a Glance

| Phase | Name | Stage | Toward | Status |
|---|---|---|---|---|
| 0 | Foundation | 1 | — | ✅ DONE (2026-07-27) |
| 1 | Semantic Layer Completion | 1 (CLI) | MVP | ⬜ |
| 2 | Personal State Schema | 1 | MVP | ⬜ |
| 3 | DO↔D1 Sync | 1 | MVP | ⬜ |
| 4 | Hybrid Context Assembly | 1 | MVP | ⬜ |
| 5 | The Blob Interface (Both Doors) | 1 | MVP | ⬜ |
| 6 | Metaphor System v1 | 1 | **MVP COMPLETE** | ⬜ |
| 7 | Calibration Quiz | 1 | scale | ⬜ |
| 8 | Interval Pipelines (Cron) | → 2 | scale | ⬜ |
| 9 | Voice Navigation Layer | 2 | scale | ⬜ |
| 10 | Ready-Made KG Expansion | 2 | scale | ⬜ |
| 11 | Visualization | 2 | scale | ⬜ |
| 12 | Fact-Check & Raw-Inbox Pipelines | 2 | scale | ⬜ |
| 13 | Native Transition | 3 | **FINAL STATE** | ⬜ |

---

## 3. The MVP Definition

**The working MVP = end of Phase 6.**

> *"Discovery works, the tutor knows you and remembers you, both doors of the blob open, and the castle begins to speak your language."*

Concretely, at MVP:

- Every one of the 4,720 nodes is embedded and semantically discoverable; ≥1,000 cross-subject edges exist.
- The full personal-state schema (10 new tables) is live.
- The tutor's memory survives sessions (DO↔D1 sync) and every mastery change is event-logged.
- Tutor responses are grounded in assembled hybrid context (canonical facts + learner state + metaphor + edges + neighbors + history).
- Single tap routes commands through the alias flywheel; double tap opens resumable conversation threads.
- Closing a thread extracts your metaphors into the graph.

Everything after Phase 6 is **scaling** — making the loop richer, more autonomous, more embodied — never fixing a broken core.

---

## 4. The Phases

---

### Phase 0 — Foundation ✅ DONE (2026-07-27)

**What exists:** Six D1 tables 100% hydrated (4,720 `master_nodes` · 373 `chapters` · 5,233 `chapter_nodes` · 2,839 `pyq_corpus` · 6,064 `pyq_node_links` · 1,812 `master_edges`), `UPSCTutorAgent` Durable Object with Ebbinghaus decay, PWA shell deployed, 13 API routes, zero-AI batch ingestion pipeline.

**Deficits carried forward** (VISION.md Part 1 corrections):
- Vectorize ~15% populated (~93 chapter files worth) — semantic queries broken for most nodes.
- R2 unbound — `MEDIA_BUCKET` optional in `Env`, absent from `wrangler.jsonc`.
- DO↔D1 unsynced — tutor state dies with the session.
- All two-door schema tables missing.

---

### Phase 1 — Semantic Layer Completion

**Stage:** 1 (CLI — zero Workers AI neurons) · **Depends on:** Phase 0

**Goal:** Make discovery real. Every node embedded, cross-subject edges computed, R2 bound.

**Why first:** Every subsequent feature (hybrid context, semantic neighbors, cross-KG linking) is fictional while Vectorize is 85% empty. This is also pure CLI work — maximum value at zero AI cost.

**Deliverables:**
- [x] Local BGE Base embedding script ready; 2,827 external KG nodes (polity/philosophy/cs) embedded and upserted to Vectorize. ✅ DONE.
- [ ] Embed the remaining 4,720 UPSC nodes (deduplicated NCERT-derived) — **deferred to Phase 10 (Route C C3)**.
- [x] Cross-subject semantic edge computation for KG-only set: 674 edges at cosine ≥ 0.65 inserted into D1. ✅ DONE.
- [ ] **LLM reasoning backfill**: batch-review the existing 674 `semantic_edges` (similarity ≥ 0.65) with Sonnet → populate `relation_type` and `reasoning` columns. **Phase 1 close-out.**
- [ ] Create R2 buckets (`session-archives`, `raw-inbox`, media) and bind `MEDIA_BUCKET` in `wrangler.jsonc`.
- [ ] Verification queries + `/api/node/:id` returning live semantic neighbors.

**Exit criteria:**
- 2,827 KG vectors in Vectorize, verified clean (0 strays). ✅
- 674 cross-subject `semantic_edges` in D1. ✅
- `SELECT COUNT(*) FROM semantic_edges WHERE reasoning IS NOT NULL` == 674 (or total edge count if threshold includes more).
- R2 binding live; Worker can read/write a test object.

**MVP state:** Semantic queries work for 100% of KG nodes; hybrid queries become possible once UPSC nodes are embedded in Phase 10.
**Final state:** Continuous native embedding — new nodes embedded automatically on ingest via Workers AI batch jobs (Phase 13); edge recomputation as the KG grows (Phase 10).

---

### Phase 2 — Personal State Schema

**Stage:** 1 · **Depends on:** Phase 0 (parallel-safe with Phase 1)

**Goal:** Create the persistence substrate for everything the two doors, metaphors, events, conflicts, calibration, and provenance need.

**Deliverables:**
- [ ] Migration `0005_session_architecture.sql`: `persistent_sessions`, `session_messages`, `personal_metaphors`, `natural_language_aliases`, `response_templates`, `node_mastery_events`, `conflict_queue`, `calibration_quizzes`, `kg_sources`, `session_transcripts_archive` — with indexes on all foreign keys and query-hot columns.
- [ ] Seed `kg_sources` with the curated UPSC row (source_type=CURATED, node_count=4,720).

**Exit criteria:**
- Migration applied to remote D1; all 10 tables exist and accept writes.
- `/api/status` reports the new schema version.

**MVP state:** Tables exist and accept writes.
**Final state:** Schema never forecloses multi-user (Open Q8) — no decision in this migration may prevent a future `user_id` column; single-user hardcoding in app code remains acceptable.

---

### Phase 3 — DO↔D1 Sync

**Stage:** 1 · **Depends on:** Phase 2

**Goal:** The tutor remembers you across sessions. The single highest perceived-value change in the plan.

**Deliverables:**
- [ ] Session-start hydration: DO loads `node_mastery`, active `personal_metaphors`, and recent context from D1.
- [ ] Session-end write-back: new attempts, mastery deltas, new misconceptions persisted to D1.
- [ ] `node_mastery_events` append on every mutation (ATTEMPT, CHAPTER_PROGRESS, CALIBRATION, METAPHOR_REFINED) with old/new values.
- [ ] Conflict policy: last-write-wins on the snapshot; the event log is the source of truth.

**Exit criteria:**
- Answer PYQs in a tutor session, close it, start a fresh session → mastery values persist.
- Every mutation produced a `node_mastery_events` row; D1 `node_mastery` equals the DO's last state.

**MVP state:** Personal state survives sessions; the heatmap is cumulative.
**Final state:** 90-day hot window in D1 + monthly gzip archives in R2 (Phase 8); trajectory visualizations spanning both (Phase 11).

---

### Phase 4 — Hybrid Context Assembly

**Stage:** 1 · **Depends on:** Phases 1, 3

**Goal:** The three-layer query architecture (VISION.md Part 7) becomes a real pipeline. This is the omniscience mechanism.

**Deliverables:**
- [ ] Query router classifying requests: exact / structural / semantic / hybrid / mutation.
- [ ] `assembleTutorContext(nodeId, sessionId)` builder producing the full context block: canonical facts (D1) + learner state (DO) + active metaphor (D1) + curated edges (D1) + semantic neighbors (Vectorize→D1) + cross-subject edges (D1) + conversation history (D1).
- [ ] Tutor prompt refactor to consume the assembled block; debug endpoint/log to inspect what was assembled.

**Exit criteria:**
- With a seeded misconception and metaphor on a test node, the tutor's response demonstrably references both.
- The assembled context block is inspectable per request.

**MVP state:** Grounded, calibrated tutoring across all UPSC nodes.
**Final state:** Maths witness nodes and cross-KG neighbors join the context as the graph grows (Phase 10); multiple specialized agents consume the same assembler (Open Q10).

---

### Phase 5 — The Blob Interface (Both Doors)

**Stage:** 1 · **Depends on:** Phases 2, 4

**Goal:** One blob, two entry modes, both shipped in a single phase — the blob is the face of the castle and ships complete.

**Deliverables — Shared:**
- [ ] Blob UI element with tap-pattern detection (single vs double tap).

**Deliverables — Single Tap (Ephemeral / Command Mic):**
- [ ] Three-tier router: (1) `natural_language_aliases` exact match → endpoint, zero AI; (2) local on-device intent parser (offline, zero credits); (3) ephemeral LLM fallback → routes **and writes the new phrase→intent mapping back to the alias table**.
- [ ] `response_templates` with live slots filled from D1/DO at query time.
- [ ] Compressed transcript archival to R2 `session-archives` + `session_transcripts_archive` metadata row.

**Deliverables — Double Tap (Persistent / Conversation Threads):**
- [ ] Translucent session window: list prior sessions, resume any, start new, one active at a time.
- [ ] `persistent_sessions` + `session_messages` CRUD APIs; history loads on resume.
- [ ] Model-pluggable router (LLM-agnostic; `model_used` recorded per session).

**Exit criteria:**
- Say the same phrase twice → the second time routes via alias with zero AI call (provable via logs).
- Close and resume a persistent session → full history reloads.
- An ephemeral transcript lands in R2 with its D1 metadata row.
- All flows work on the deployed PWA, phone-first.

**MVP state:** Both doors open; cost-per-command falls as the alias table learns your phrasing.
**Final state:** Real-time STT/TTS voices (Phase 9); auto-generated templates from successful LLM responses (Open Q2); full offline-first PWA caching (Open Q11).
**Open questions to resolve during this phase:** Q1 (alias matching: exact-only vs semantic), Q2 (template authoring vs auto-generation), Q3 (model menu granularity).

---

### Phase 6 — Metaphor System v1

**Stage:** 1 · **Depends on:** Phase 5

**Goal:** The personal metaphor map begins growing — the castle starts speaking your language.

**Deliverables:**
- [ ] Thread-close extraction: one LLM call per persistent-session close processes the transcript → candidate metaphors → `personal_metaphors` rows (`accuracy_score` = 0.5, `is_active` = true).
- [ ] Tutor anchoring: context assembly (Phase 4) includes the highest-accuracy active metaphor per concept.
- [ ] Accuracy update hook: a linked PYQ answered correctly/incorrectly after metaphor-anchored teaching nudges the score; low scores deprioritize but never auto-delete.
- [ ] Evolution preservation: superseded metaphors keep `is_active=false` history; tutor can reference the evolution ("what changed your mind?").

**Exit criteria:**
- Close a session in which you described a concept in your own words → a `personal_metaphors` row exists.
- The next session's context block contains that metaphor.
- Answering a linked PYQ moves its `accuracy_score`.

**MVP state:** The metaphor flywheel turns end-to-end.
**Final state:** A full metaphor map draped over the KG; METAPHOR_REFINED events in `node_mastery_events`; metaphor-evolution narratives in the UI (Phase 11).

### 🏁 MVP COMPLETE — end of Phase 6. Everything below is scaling.

---

### Phase 7 — Calibration Quiz

**Stage:** 1 · **Depends on:** Phases 3, 6

**Goal:** Cold-start personalization — one guided experience per subject that seeds your entire initial state.

**Deliverables:**
- [ ] Sampler: 50% breadth (proportional across chapters) + 50% depth (weighted to foundational/prerequisite nodes), designed from the current global state of the subject.
- [ ] Quiz flow: PYQ-style + concept-recognition items over the sample.
- [ ] Inference: sample performance → initial mastery estimates for **all** nodes in the subject (writes `node_mastery`, CALIBRATION events, `calibration_quizzes` row with `initial_state_json`).
- [ ] Metaphor writing session: top 20–30 concepts, free-text "describe it in your words" → `personal_metaphors` at 0.5.
- [ ] Dynamic correction: later evidence continuously overrides estimates.

**Exit criteria:**
- Completing a subject calibration gives every node in that subject a non-null initial mastery estimate and stores the `calibration_quizzes` row.
- A subsequent real attempt demonstrably adjusts the estimate.

**MVP state:** Per-subject onboarding exists; the tutor is calibrated from day one in a calibrated subject.
**Final state:** Calibration re-offered adaptively as new subject KGs arrive (Phase 10).

---

### Phase 8 — Interval Pipelines (Cron) → enters Stage 2 (Hybrid)

**Stage:** 1 → 2 · **Depends on:** Phases 3, 5

**Goal:** The castle maintains itself on a schedule; manual CLI maintenance loops end.

**Deliverables:**
- [ ] Cron Trigger — **alias refinement:** process archived ephemeral transcripts → promote/demote aliases, maintain `usage_count`/`success_count`, surface commonly-asked-but-poorly-answered queries.
- [ ] Cron Trigger — **event log archival:** `node_mastery_events` older than 90 days → monthly gzip JSON per subject in R2; D1 trimmed; snapshot stays authoritative.
- [ ] Cron Trigger — **pattern analysis:** usage-driven navigation/template improvement report.

**Exit criteria:**
- Crons fire on schedule (verified via logs/`wrangler tail`).
- A >90-day-old event round-trips through the archive.
- The alias table shows usage-driven change over time.

**MVP state:** Zero manual CLI runs for maintenance loops.
**Final state:** The full observed-usage loop modifies castle navigation automatically (VISION.md Part 2).
**Open questions to resolve:** Q4 (R2 retention horizon), Q12 (export format — shared with archive structure).

---

### Phase 9 — Voice Navigation Layer

**Stage:** 2 · **Depends on:** Phase 5

**Goal:** Hands-free, offline-first voice — pluggable, never load-bearing.

**Deliverables:**
- [ ] Local on-device STT + local intent extraction feeding the Phase 5 router — no cloud, no credits, works offline.
- [ ] Navigator voice: sparing TTS for ephemeral confirmations.
- [ ] Teacher voice: ElevenLabs real-time TTS in the persistent window, one persistent voice identity across all sessions (survives model swaps).

**Exit criteria:**
- A spoken navigation command issued offline routes correctly.
- A persistent session speaks in the consistent teacher voice.

**MVP state:** Voice works; the system remains fully functional with voice disabled.
**Final state:** Voice identity as a durable personal constant; credit budget managed per tier.

---

### Phase 10 — Ready-Made KG Expansion

**Stage:** 2 · **Depends on:** Phase 1 (pattern repeats at scale)

**Goal:** The global state grows beyond the initial UPSC core — the castle annexes both curated source material and ready-made external domains.

**Dual-track approach:**

**Track A — Route C: Curated UPSC KG Construction (NCERT + Reference Books)**
The primary expansion path. Concepts are extracted from our own processed source material, deduplicated, embedded, and linked by objective cosine similarity — never hallucinated.

- [ ] **C1 — Reference-Book Node Extraction (LLM pass)**: One book at a time, starting with **Laxmikanth**. LLM (Sonnet, read-only) reads chapter-by-chapter and emits structured nodes (id, subject, topic, label, type, detail, source_book, source_chapter). **Nodes only — no edges.** Detail is 50–75 words, discriminating, not prose. Output: `processed/reference-books/<book>_nodes.json`.
- [ ] **C2 — Unified KG Assembly (D1 merge)**: Merge three sources into `master_nodes`:
  1. `processed/ncert/*/*.json` — 342 chapter files, **9,789 raw nodes → ~4,716 unique IDs** (dedupe by normalized label + subject).
  2. Reference-book `_nodes.json` from C1.
  3. Existing 2,827 external-source nodes (polity_art_*, phil_*, cs_*) — **kept as-is**, not merged unless a clear match.
  NCERT JSON `edges[]` written to `master_edges`. Deduplication: match by normalized label; if "Federalism" exists in NCERT Ch1 and Laxmikanth Ch3, keep one canonical node linking both sources.
- [ ] **C3 — Embedding All KG Nodes**: BGE Base local batch embed for every node in the unified KG. Embedding text = `title + ": " + summary[:300] + ". " + canonical_facts[:3]`. Output `vectors.ndjson`; **additive upsert** to `prelims-concept-vectors` (existing 2,827 vectors stay). Total vectors: ~15,000–18,000. **This is where the deferred 4,720 UPSC nodes are finally embedded.**
- [ ] **C4 — Semantic Edge Computation (cosine)**: Full pairwise cosine over all vectors. Filter: `similarity >= threshold` AND cross-subject only. Threshold: start at **0.70** (established 0.65 on the small KG-only set; UPSC concepts are more domain-specific, so expect a higher floor). Write `insert_semantic_edges.sql` → D1.
- [ ] **C5 — LLM Edge Review & Labelling**: For every edge above threshold, LLM (Sonnet) reviews source + target labels/details + cosine score → assigns `relation_type` (e.g., `constitutional_basis_for`, `prerequisite_for`, `contradicts`) + backfills `reasoning` column. This is the **only** LLM cost for relationships — selective, not volumetric.

**Track B — External Ready-Made KGs (Non-UPSC Domains)**
Import high-quality, pre-built knowledge graphs for domains outside UPSC.

- [ ] `kg_sources` provenance rows (license, ingestion_date, node_count) per import.
- [ ] Importers: Wikidata (AI/CS), ConceptNet, domain ontologies (philosophy, psychology) → parse locally → embed locally → bulk-upsert D1 + Vectorize. **Import raw; no manual cross-linking** — bridges emerge from the shared embedding space.
- [ ] Semantic edge pass across the enlarged graph.
- [ ] **Maths-as-witness:** import maths KG with `is_foundation` flag; toggleable lens homescreen; engaged nodes highlighted, the rest witnessed as background structure.
- [ ] Materialized per-subject views if node counts demand them.

**Exit criteria:**
- Cross-domain semantic edges exist with similarity ≥ 0.70 (e.g., optimization ↔ Pareto optimality, federalism ↔ constitutionalism).
- Every `semantic_edges` row above threshold has non-NULL `relation_type` and `reasoning`.
- The maths lens toggles; per-source node counts are queryable.
- `wrangler vectorize list-vectors` count == total `master_nodes` count (~15K–18K).

**MVP state:** A multi-domain castle with emergent bridges; all edges are labelled and reasoned.
**Final state:** 50,000+ nodes; partition-aware caching or hot-subject table splits only if measured latency demands it.
**Open questions to resolve:** Q7 (maths activation day), Q9 (KG versioning).

---

### Phase 11 — Visualization

**Stage:** 2 · **Depends on:** Phases 3, 10 (visualizes whatever exists at the time)

**Goal:** The castle becomes visible.

**Deliverables:**
- [ ] **Per-subject force-directed graphs (primary)**: Query D1 per subject → render with D3.js / Cytoscape.js (fCose/Cola layout). One view per subject (history, geography, polity, economics, science). Nodes sized by edge degree; edges colored/thickness by similarity or `relation_type`. This is the "global state castle" — the learner navigates concept space, not a textbook table of contents.
- [ ] **Heatmap overlay**: green mastered / red decaying / dim unread, driven by `/api/mastery`.
- [ ] **Embedding-space visualization (secondary / nice-to-have)**: Export `vectors.ndjson` → UMAP/t-SNE → 2D projection → scatter colored by subject/topic. Shows cluster structure and cross-subject bridges. Static artifact first; interactive client-side UMAP in PWA later if desired.
- [ ] **Vision note uploader UI**: snap → `/api/notes/upload` → OCR → node-attached.

**Exit criteria:**
- At least one subject surface (e.g., polity) renders from live D1 data as an explorable graph.
- Heatmap colors match D1 mastery ground truth.
- An uploaded handwritten note OCRs and links to its node.
- Embedding-space scatter produced as a static artifact.

**MVP state:** An explorable castle with personal heat.
**Final state:** Trajectory visualizations from event history (D1 hot + R2 cold), metaphor-evolution views, KG version diffs (if Q9 resolves yes).

---

### Phase 12 — Fact-Check & Raw-Inbox Pipelines

**Stage:** 2 · **Depends on:** Phases 1, 2, 8

**Goal:** Canonical integrity plus external data integration at scale — the voice remembers what you said elsewhere and reconciles it with truth.

**Deliverables:**
- [ ] `conflict_queue` resolver: CLI first, then scheduled Worker; resolution authority model decided (Open Q5); every resolution event-sourced with an audit trail.
- [ ] R2 `raw-inbox` event triggers: a dropped dump (chat export, screenshot, voice memo) → automatic process (extract, embed, link, integrate).
- [ ] Reconciliation flow: "last week you asked ChatGPT about this — here's what it said, and here's what's actually true" → conflicts land in `conflict_queue`.

**Exit criteria:**
- A file dropped in `raw-inbox` is processed with zero manual steps.
- A seeded conflict is resolved via the chosen authority model with a visible audit trail.

**MVP state:** External data flows in; conflicts surface and resolve; canonical facts are never silently overwritten.
**Final state:** Continuous integrity as an ambient property of the system.

---

### Phase 13 — Native Transition → Stage 3 (Paid Tier) = FINAL STATE

**Stage:** 2 → 3 · **Depends on:** Phases 8–12

**Goal:** Everything autonomous inside the application. The CLI survives for debugging only.

**Deliverables:**
- [ ] All remaining CLI pipelines ported native: R2 triggers, full cron coverage, Workers AI batch embedding for newly added nodes.
- [ ] Paid-tier migration with neuron-budget monitoring.
- [ ] Close or explicitly defer all 20 items of VISION.md Part 11.

**Exit criteria:**
- Zero standing manual CLI steps in normal operation.
- Neuron spend observed and within budget.

**Final state:** see §6 — Definition of Done.

---

## 5. Stage Transition Triggers

| Transition | Fire when… | Marked by |
|---|---|---|
| **Stage 1 → 2 (Hybrid)** | Free 10k neurons/day is consistently sufficient **and** manual CLI runs have become routine/toilsome | Entering Phase 8 |
| **Stage 2 → 3 (Native)** | Native processing (R2 events, crons, batch jobs) consistently exceeds free 10k neurons/day | Entering Phase 13 |

---

## 6. Definition of Done (The Final State)

The construction is complete when all of the following are true:

1. **Global state:** 50,000+ nodes across curated UPSC + ready-made domains + maths witness layer, all provenance-tracked in `kg_sources`, all embedded in one Vectorize space, all cross-linked by computed semantic edges.
2. **Discovery:** Any concept findable semantically in one query; cross-domain bridges surfaced automatically.
3. **Personal state:** Full mastery history (90-day hot in D1 + cold archives in R2), event-sourced; calibrated per subject; metaphor map with accuracy scores and evolution history.
4. **The blob:** Both doors + voice; alias flywheel handles the majority of ephemeral commands at zero AI cost; persistent threads grounded in full hybrid context with the consistent teacher voice.
5. **Autonomy:** All pipelines (archival, alias refinement, conflict resolution, raw-inbox, embeddings) run native on triggers/crons; CLI is debug-only.
6. **Integrity:** Canonical facts never silently change — every mutation is event-sourced and auditable.
7. **The feeling:** The four omniscience mechanisms of VISION.md Part 9 all work — comprehensive facts, semantic discovery, calibrated personal state, integrated external data. The infrastructure does the work; the LLM just speaks.

---

## 7. Open Questions Registry

Tracked from VISION.md Part 12, mapped to the phase that must resolve each. STATE.md carries their live status.

| # | Question | Resolve by | Status |
|---|---|---|---|
| Q1 | Alias growth: exact-match only vs semantic matching | Phase 5 | open |
| Q2 | Response templates: hand-authored vs auto-generated | Phase 5 | open |
| Q3 | Persistent model menu: per-session vs per-message vs automatic | Phase 5 | open |
| Q4 | R2 retention horizon: forever vs summarize after 1 year | Phase 8 | open |
| Q5 | Conflict resolution authority: user-only vs LLM-suggested vs auto | Phase 12 | open |
| Q6 | Personal narrative generation: story-of-your-education vs raw state | post-MVP, any phase may propose | open |
| Q7 | Maths activation day: witness → primary surface transition | Phase 10 | open |
| Q8 | Multi-user future: when/how without rebuild | constrained from Phase 2 onward; decide pre-Stage 3 | open |
| Q9 | KG versioning: castle snapshots over time | Phase 10 | open |
| Q10 | Specialized agents beyond the Socratic tutor | Phase 4 assembler must not foreclose; decide post-MVP | open |
| Q11 | Offline-first PWA with locally cached KG | Phase 5 (caching strategy), Phase 9 (voice offline) | open |
| Q12 | Export/portability of entire personal state | Phase 8 (archive format) | open |

---

## 8. Session Protocol

At the **start** of every working session:

1. Read STATE.md → "Build Timeline Position" → confirms the active phase.
2. Open this file → read the active phase's deliverables and exit criteria.
3. Confirm with the user which deliverable(s) this session targets.

At the **end** of every working session:

1. Verify exit criteria honestly; update checkboxes in this file.
2. Update STATE.md position section (active phase, % of phase done, next actions, blockers).
3. Commit on the working branch, push, PR — merge only on user approval.
