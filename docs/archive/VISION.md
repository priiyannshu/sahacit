# The Full Architectural Plan (VISION)

> **The source blueprint for the construction of 22.**
> Saved 2026-07-28. Companion files: `MASTER_PLAN.md` (the build timeline) · `STATE.md` (live position marker).
> This document is the *what and why*. The master plan is the *when and in what order*.

---

## Part 1: The Foundation (What Exists Today)

### The Current State

The application lives at `https://22.priyanshukh1201.workers.dev`. It's a Cloudflare Worker (`src/index.ts`, 650 lines) that serves both as the API router and the static PWA host. The architecture has four layers already built:

**Layer 1 — The Knowledge Graph (D1 SQLite)**

Six tables in `prelims-master-db` (database ID: `f53475f0-c4a8-40af-bfcf-7054cf57e1d7`):

- `master_nodes` — 4,720 concept atoms (canonical facts, title, summary, subject, topic)
- `chapters` + `chapter_nodes` — 373 narrative paths with 5,233 ordered node sequences
- `pyq_corpus` + `pyq_node_links` + `pyq_attempts` — 2,839 PYQs with 6,064 concept links
- `master_edges` — 1,812 curated relationships (justified_by, example_of, led_to, includes, contrasted_with)
- `node_mastery` + `chapter_progress` — personal footprints
- `handwritten_notes` — OCR transcripts (R2 not yet bound, URLs are placeholder)

All tables are 100% hydrated. The ingestion used `/api/ingest/batch-raw` (direct SQL batches of 50, zero AI calls) to avoid rate limits.

**Layer 2 — The Durable Object (`UPSCTutorAgent`)**

A separate stateful entity with private SQLite (`ctx.storage.sql`) holding:

- `learner_nodes` — mastery score, status (UNEXPLORED/LEARNING/MASTERED/FADING/MISUNDERSTOOD), half-life days, misconceptions as JSON array
- `attempt_logs` — every attempt with confidence, time, timestamp

The Ebbinghaus forgetting curve runs here: `retention = exp(-ln(2) / half_life * elapsed_days)`. When answered correctly with high confidence, mastery climbs by `0.2 * (confidence/5)` and half-life extends. When wrong, mastery drops 0.25, half-life halves, and the wrong answer joins the misconceptions list.

The DO is NOT synced with D1. They are two separate stores for two different purposes. D1 is the persistent authoritative record. The DO is the working memory the Socratic tutor reads for session-persistent state.

**Layer 3 — Vectorize (768-dim BGE Base embeddings)**

Currently mostly empty. Only ~93 chapter files worth of nodes were embedded before Workers AI rate limits hit. The cross-subject semantic edge computation pass was never run at scale. The infrastructure is ready — the data isn't populated yet.

**Layer 4 — Workers AI**

Three models are bound and available:

- `@cf/meta/llama-3.1-8b-instruct` — Socratic tutor
- `@cf/meta/llama-3.2-11b-vision-instruct` — handwritten note OCR
- `@cf/baai/bge-base-en-v1.5` — embeddings (but expensive at scale on free tier)

### What Needs Correction Before Continuing

1. Vectorize is ~15% populated, not 100%. Semantic queries only work for the nodes that got embedded.
2. The DO and D1 are separate stores, not synced. Don't think of them as the same database.
3. R2 is unbound. The `MEDIA_BUCKET` is optional in `Env` and not configured in `wrangler.jsonc`.
4. Embeddings are for discovery, not verification. Canonical facts in D1 are the only deterministic truth.

---

## Part 2: The Two Doors (Session Architecture)

### The Single Blob

The PWA has a single interface element — a blob. It has two modes of entry, distinguished by tap pattern:

**Single Tap → Ephemeral Layer (The Command Mic)**

A one-shot interaction. No context carried forward. Each message is processed independently.

Routing pipeline (three descending tiers):

1. **Alias table lookup** (`natural_language_aliases` table in D1) — exact phrase match against the personal command library. If matched, route directly to the endpoint. No AI call. Instant.

2. **Local speech-to-intent** (on-device, offline) — if no exact match, a local model extracts intent. `"open chapter 10 from polity narrative chapters"` → `{action: navigate, target: chapter, subject: polity, position: 10}` → routes to `/api/chapters/:id`. No cloud. No AI credits.

3. **Ephemeral LLM call** (only if both above fail) — a lightweight model interprets intent, routes to the endpoint, and writes the mapping (the user's words → the recognized intent) back to the alias table. The next time the same thing is said, it's caught at tier 1.

Responses for common ephemeral queries are pre-generated as dynamic templates — the shell is cached, but slots for live data (current position, mastery score, due concepts) are filled fresh from D1 and the DO at query time.

Every ephemeral transcript is saved — compressed, neat, archived in R2 — not destroyed after processing. A serverless interval pipeline processes these archives to refine the alias table, identify commonly asked but poorly answered queries, and modify the castle's navigation based on observed usage.

**Double Tap → Persistent Layer (The Conversation Threads)**

Opens a translucent window showing previous persistent sessions — each one a named, resumable log. Resume any of them or start a new one. Only one active at a time, others wait.

Each message in a persistent session:

- Is routed through a model of the user's choosing (LLM-agnostic, pluggable)
- Receives the full hybrid context: canonical facts (D1), mastery + misconceptions (DO), semantic neighbors (Vectorize), curated edges (D1), cross-subject edges (D1), personal metaphors (D1 `personal_metaphors`), conversation history (D1 `session_messages`)
- Is spoken via real-time TTS (ElevenLabs — a consistent teacher's voice across sessions)
- Is captured via real-time STT

When a persistent session closes, a single LLM call processes the entire transcript and extracts the user's metaphors — the specific ways they described concepts. These are written to `personal_metaphors` with accuracy scores. Over time, this builds a personal metaphor map draped over the canonical knowledge graph. Future tutor responses anchor new concepts in the user's existing metaphors.

### Schema Additions for the Two-Tier Model

**New D1 tables:**

- `persistent_sessions` — id, title, subject_focus, started_at, last_active_at, status (OPEN/CLOSED/PROCESSING), model_used
- `session_messages` — id, session_id, role (user/assistant/system), content, linked_node_id, timestamp
- `personal_metaphors` — id, master_node_id, metaphor_text, session_id, accuracy_score, extracted_at, is_active
- `natural_language_aliases` — id, user_phrase, intent_type, query_template, usage_count, success_count, created_at, last_used_at
- `response_templates` — id, intent_type, template_text, slot_variables, last_refreshed, usage_count
- `node_mastery_events` — id, node_id, event_type (ATTEMPT, CHAPTER_PROGRESS, CALIBRATION, METAPHOR_REFINED), old_value, new_value, timestamp
- `conflict_queue` — id, source, extracted_text, canonical_fact, conflict_type, status, created_at, resolved_at, resolution
- `calibration_quizzes` — id, subject, started_at, completed_at, nodes_sampled, initial_state_json
- `kg_sources` — id, source_name, source_type (CURATED/READY_MADE), license, ingestion_date, node_count

**New R2 buckets:**

- `session-archives` — compressed ephemeral session transcripts (gzip JSON, metadata in D1 `session_transcripts_archive` table)
- `raw-inbox` — raw data dumps from external apps (chat exports, screenshots, voice memos)

---

## Part 3: The Personal State Journey

### Hybrid Storage Model

**D1 (persistent, long-term):**

- `node_mastery` — current snapshot (mastery_score, encounter_count, correct_count, last_tested_at, next_review_at)
- `node_mastery_events` — full event log (every mastery change with timestamp, old/new values, event type)
- `personal_metaphors` — metaphor history with accuracy scores
- `pyq_attempts` — every quiz attempt ever
- `chapter_progress` — reading bookmarks

**DO (live, session-active):**

- Current conversation history for active persistent session
- Live spaced repetition queue (computed from mastery + decay)
- Current heatmap state for active node
- Active misconceptions being worked on

**Synchronization:** The DO reads from D1 at session start (loads mastery, metaphors, etc.) and writes back to D1 on session end (persists new attempts, new mastery, new metaphors). During the session, the DO works in its own SQLite for speed.

### The Calibration Quiz (Entry Point for Each Subject)

When first entering a subject, the system offers a calibration quiz — a one-time experience per subject that seeds the initial personal state. The quiz uses a mix of breadth (proportional sampling across chapters) and depth (weight toward foundational/prerequisite nodes), 50/50.

The calibration quiz is designed based on the current global state for that subject. It samples nodes, presents PYQ-style questions or concept-recognition tasks, and infers approximate mastery on all nodes in that subject from performance on the sample.

**Metaphor collection:** After the quiz, a separate "metaphor writing session" for that subject — the user is shown the top 20-30 concepts and asked to describe each in their own words. The free-text descriptions become starting metaphors, stored in `personal_metaphors` with initial accuracy_score = 0.5 (neutral, refined as the system is used).

**Dynamic, not static:** The calibration is a starting point, not a fixed state. It improves over time. If the user later proves to know more (or less) than the calibration estimated, the system corrects the estimate. The calibration is the foundation — dynamic and constantly refined.

### Event Log Growth Management

The `node_mastery_events` table will grow large over years. Management strategy:

- Events from the last 90 days stay in D1 for fast queries
- Events older than 90 days are compressed and moved to R2 (gzip JSON, one file per month per subject)
- The D1 `node_mastery` snapshot remains the authoritative current value
- Trajectory visualizations query the recent 90 days from D1 and pull older history from R2 only when needed

---

## Part 4: The Global State (Ever-Increasing KGs)

### Multi-Source Knowledge Graph

The `master_nodes` table will grow beyond 4,720 as ready-made KGs are imported. The `kg_sources` table tracks provenance:

- **UPSC subjects** (history, polity, economics, geography) — curated, hand-extracted from NCERTs, Laxmikanth, Ramesh Singh, Bipin Chandra. High quality, domain-specific.
- **Ready-made subjects** (AI, CS, philosophy, psychology) — imported from Wikidata, ConceptNet, domain-specific ontologies. Lower curation, broader coverage.
- **Maths** — imported as a foundation/witness layer. Seen only where it cross-links with concepts being studied, never as a primary study surface. Maths has its own subject homescreen (toggleable lens) where the entire KG is visible, but nodes representing things actually engaged with are highlighted. The rest is "witnessed" as background structure.

### Cross-Linking Strategy: Import Raw, Rely on Semantic Edges

Ready-made KGs are imported as-is. No pre-computation of cross-links at import time. Instead:

1. All nodes (curated + ready-made + maths) get embedded into the same Vectorize space via the local BGE Base pass
2. The cross-subject semantic edge computation runs across all nodes
3. Edges emerge naturally between curated UPSC nodes and ready-made AI/CS/philosophy nodes based on cosine similarity in the shared latent space

This means "optimization" (CS) and "Pareto optimality" (Economics) will be cross-linked because their meanings are close — not because a human drew that edge. The semantic discovery pass is the mechanism that bridges curated and ready-made domains.

### Query Performance with 50,000+ Nodes

The application uses the current single-table design (one `master_nodes` table) with a subject column as an indexed field, plus materialized views per subject lens for fast per-lens queries. This gives:

- Fast per-subject queries via materialized views (pre-computed for common lenses)
- Natural cross-subject queries via the unified table
- No need for complex cross-table JOINs

When the KG grows beyond 50,000 nodes, partition-aware caching can be added or the hottest subjects split into their own tables, but the hybrid approach scales to at least that size without restructuring.

---

## Part 5: The Metaphor System

### The Personal Metaphor Map

`personal_metaphors` table structure:

- `id` — UUID
- `master_node_id` — the canonical concept this metaphor is about
- `metaphor_text` — the user's description in their own words
- `session_id` — which persistent session it came from
- `accuracy_score` — 0.0 to 1.0, tracks how well this metaphor predicts correct answers
- `extracted_at` — timestamp
- `is_active` — boolean (current metaphor vs. historical)

Every metaphor has an accuracy score. The score updates as the system is used:

- When a metaphor helps answer a related PYQ correctly, accuracy_score increases
- When a metaphor leads to an incorrect answer (wrong analogy applied), accuracy_score decreases
- Low-accuracy metaphors are deprioritized but never auto-deleted (the user's metaphors stay theirs)
- The tutor uses the highest-accuracy active metaphor for a concept when speaking

### Metaphor Evolution

When the metaphor for Federalism shifts from "lunch-sharing" to "corporate franchise" to "network of autonomous agents," all versions are preserved. The `is_active` flag marks the current one. The tutor can reference the evolution: "Last month you described Federalism as lunch-sharing. Now you see it as a network of autonomous agents. What changed your mind?"

This evolution log is part of the personal state journey. It shows how mental models deepened over time.

---

## Part 6: The Voice Navigation Layer

### Local Speech-to-Intent (No Cloud)

The PWA uses a local speech-to-intent model running on-device. When the user speaks:

1. STT converts speech to text (local model, offline)
2. Intent extraction parses the text into structured intent (local model, offline)
3. Intent routes directly to the corresponding API endpoint
4. Response is returned (text or TTS depending on the mode)

No cloud dependency. No AI credits. No latency from model inference. Works offline. The voice navigation layer is LLM-agnostic — it doesn't depend on any specific model, just on the intent-to-endpoint mapping.

### Two Voices

**The Navigator's Voice (Ephemeral):**
- Speaks responses to commands
- Pre-generated or simple synthesis for economy
- ElevenLabs credits used sparingly — only for complex navigation confirmations
- Consistent across all ephemeral interactions

**The Teacher's Voice (Persistent):**
- Real-time ElevenLabs TTS
- Consistent across all persistent sessions (the same voice throughout the learning journey)
- The same model that speaks can be swapped, but the voice identity persists (via ElevenLabs voice cloning or voice ID persistence)
- Higher credit cost, justified by the depth of conversation

The voice pipeline is secondary to the architecture — the system works without it, and the voices are pluggable. The important thing is the intent routing, not the TTS quality.

---

## Part 7: The Three-Layer Query Architecture

This is the core of how context gets assembled for the LLM. The LLM is the semantic attender — it doesn't know anything. It receives assembled context and produces grounded responses. The infrastructure does the assembly.

### Query Types and Their Stores

| Query Type | Stores Hit | What Happens |
|---|---|---|
| **Exact lookup** | D1 only | `SELECT * FROM master_nodes WHERE id = ?` |
| **Structural traversal** | D1 JOINs | `chapters JOIN chapter_nodes JOIN master_nodes` |
| **Semantic query** | Vectorize → D1 | Embed query → Vectorize topK → D1 SELECT by IDs |
| **Hybrid query** | Vectorize + D1 + DO | Embed → Vectorize → D1 canonical facts + DO learner state → LLM |
| **State mutation** | D1 + DO | INSERT/UPDATE mastery, attempt, progress |

### Context Assembly for the LLM

When the persistent tutor fires, the context is assembled:

```
System prompt:
  - You are the UPSC Socratic tutor
  - Active concept: Federalism (pol_federalism)

Learner state (from DO):
  - Mastery: 0.73 (LEARNING)
  - Half-life: 1.5 days
  - Misconceptions: ["Delhi is SAARC headquarters"]

Personal metaphor (from D1):
  - "Federalism is like sharing lunch with friends" (accuracy: 0.82)

Canonical facts (from D1):
  - ["Federalism requires division of powers between center and states", ...]

Curated edges (from D1):
  - includes: Separation of Powers
  - contrasts_with: Unitary System
  - example_of: Constitutional Framework

Semantic neighbors (from Vectorize → D1):
  - Economic Federalism (0.87 similarity)
  - Globalization (0.81 similarity)
  - Liberalization (0.79 similarity)

Cross-subject edges (from D1 semantic_edges):
  - pol_federalism → eco_economic_federalism (0.89)
  - pol_federalism → geo_globalization (0.81)

Maths witness nodes (where relevant):
  - pol_federalism → math_set_theory (division as partition)

Conversation history (from D1 session_messages):
  - [previous 10 messages in this session]

Learner's current question:
  - "How does Federalism work in India's GST system?"
```

The LLM attends to all of this. It doesn't "know" anything — it pattern-matches against assembled context. The infrastructure's job is to assemble the right context. The LLM's job is to use it well.

---

## Part 8: The Build Path (Three Stages)

### Stage 1: CLI-Driven (Now, Free Tier)

The application serves the existing endpoints and the PWA. The heavy processing happens via CLI scripts:

- **Local embeddings:** Run BGE Base on the laptop. Embed all 4,720+ nodes. Bulk-upsert to Vectorize via REST API. Zero Workers AI neurons burned.
- **Semantic edge computation:** Query Vectorize from Python for each node's nearest neighbors. Filter for cross-subject matches above 0.75. Write edges to D1 via `/api/edges/cross-subject` or direct SQL.
- **Ready-made KG ingestion:** Download KGs (Wikidata, ConceptNet). Parse with Python. Embed locally. Bulk-upsert to D1 and Vectorize.
- **Fact-check queue processing:** CLI script that reads the conflict queue, resolves conflicts, updates canonical facts.
- **R2 archive compression:** CLI script that compresses old session transcripts and moves them to R2.

Workers AI is reserved for:
- Socratic tutor chat (persistent sessions)
- Synthesis evaluation
- Metaphor extraction (one call per thread close)
- Handwritten note OCR

This keeps within the free 10k neurons/day tier.

### Stage 2: Hybrid (Transition)

As the application matures, move logic from CLI into native Workers:

- **R2 event triggers:** When a new file lands in the R2 raw-inbox, a Worker automatically processes it (embed, link, integrate)
- **Cron Triggers:** Scheduled Workers run the alias refinement, archive compression, and pattern analysis pipelines automatically (daily, weekly, monthly)
- **Embedding batch jobs:** A Worker runs the embedding pass for new nodes as they're added, using Workers AI (paid tier now for this specific job)
- **Fact-check queue processing:** A scheduled Worker resolves conflicts, with the conflict_queue table driving the workflow

The CLI becomes available for debugging and edge cases, but the application handles 80% of the work natively.

### Stage 3: Application-Native (Paid Tier)

Everything runs inside the application:

- Real-time R2 event processing
- Automated Cron Triggers for all pipelines
- Workers AI for all AI calls (embeddings, tutor, vision, metaphor extraction)
- The CLI is only for debugging

The voice always knows everything because the infrastructure is complete and autonomous.

**Transition trigger:** Move from Stage 1 to Stage 2 when the free 10k neurons tier is consistently sufficient for the needs AND manual CLI script runs become too frequent. Move from Stage 2 to Stage 3 when the application's native processing (R2 events, Cron Triggers, batch jobs) consistently needs more AI calls than the free tier allows.

---

## Part 9: The Voice (How the Application Feels Omniscient)

The application feels like it "knows everything" because of four mechanisms:

1. **Comprehensive canonical facts.** If every node has accurate `canonical_facts`, the LLM always has ground truth. The tutor never says "I don't know" — it says "let me check" and pulls from D1.

2. **Semantic discovery via embeddings.** When asked about something unexpected, Vectorize finds related concepts not explicitly linked. The system connects dots that wouldn't have been connected manually.

3. **Personal state via the DO + D1 hybrid.** The tutor knows the mastery level, the misconceptions, the metaphor accuracy, the memory decay. It doesn't ask about things mastered. It doesn't skip things forgotten. It's calibrated to the user.

4. **Raw data from R2.** When data comes in from other apps, the system integrates it. The voice remembers conversations had elsewhere. It says "last week you asked ChatGPT about this — here's what it said, and here's what's actually true."

The infrastructure does all the work. The LLM just speaks.

---

## Part 10: The Cognitive Science Foundation

The architecture is grounded in research:

- **Method of Loci (Bower, 1970)** — memory palaces are 2-3x more effective than rote memorization. The graph externalizes the palace.
- **Dual Coding Theory (Paivio, 1971)** — visual + verbal encoding strengthens memory. The graph provides visual structure, the text provides verbal content.
- **Spaced Repetition (Cepeda et al., 2006)** — distributed practice beats massed practice. The DO's Ebbinghaus curves implement personalized spacing.
- **Retrieval Practice (Roediger & Karpicke, 2006)** — active retrieval beats passive review. The tutor's probing questions force retrieval.
- **Interleaving (Rohrer & Taylor, 2007)** — mixing problem types improves learning. The graph enables natural cross-subject interleaving.
- **Elaborative Interrogation (Pressley et al., 1992)** — "why" questions build deeper understanding. The Socratic tutor does this.
- **Concept Mapping (Novak & Cañas, 2008)** — visual concept relationships improve comprehension. The force-directed graph is a dynamic concept map.
- **Metacognition (Flavell, 1979)** — awareness of one's own knowledge predicts success. The heatmap provides real-time metacognitive feedback.
- **Desirable Difficulties (Bjork, 1994)** — conditions that make learning harder short-term but better long-term. The tutor's probing questions, spaced repetition, and interleaving are desirable difficulties.
- **Transfer of Learning (Perkins & Salomon, 1992)** — structural understanding enables transfer. The semantic edges show structural isomorphisms across subjects.

The mental models built:
- **Structural models** — how concepts relate (the graph shape)
- **Causal models** — how things cause each other (curated edges)
- **Comparative models** — how things contrast (contrasted_with edges)
- **Temporal models** — how things unfold over time (era-tagged nodes)
- **Cross-subject models** — how concepts from different domains share structure (semantic edges)
- **Metaphor models** — how the user understands concepts (personal_metaphors)

These persist after specific facts fade. The shape is carried, not just the contents.

---

## Part 11: The Implementation Roadmap

### Immediate (Next Session)

1. Run the local BGE Base embedding pass for all 4,720 existing nodes
2. Bulk-upsert vectors to Vectorize via REST API
3. Run the cross-subject semantic edge computation (target 1,000+ edges)
4. Bind the R2 bucket in `wrangler.jsonc`
5. Create the new D1 tables: `persistent_sessions`, `session_messages`, `personal_metaphors`, `natural_language_aliases`, `response_templates`, `node_mastery_events`, `conflict_queue`, `calibration_quizzes`, `kg_sources`, `session_transcripts_archive`

### Short-Term (Next 2-3 Sessions)

6. Build the ephemeral routing pipeline (alias table → local intent → disposable LLM)
7. Build the persistent session window (translucent overlay, model selection, real-time TTS)
8. Build the metaphor extraction pipeline (one LLM call per thread close)
9. Build the calibration quiz system (breadth + depth sampling, metaphor writing session)
10. Build the interval processing pipelines (alias refinement, archive compression, pattern analysis)

### Medium-Term (Next 4-6 Sessions)

11. Download and ingest ready-made KGs (Wikidata AI/CS, ConceptNet, domain ontologies)
12. Build the R2 raw-inbox processing pipeline (R2 event triggers)
13. Build the voice navigation layer (local STT + intent model)
14. Build the maths-as-witness lens (toggleable, highlighted nodes for engaged concepts)
15. Build the fact-check queue resolution pipeline

### Long-Term (Stage 2/3 Transition)

16. Move CLI processing into native Workers (R2 triggers, Cron Triggers, batch jobs)
17. Add the 2D/3D force-directed graph UI
18. Add the heatmap overlay visualization
19. Add the vision note uploader UI
20. Transition to paid tier when free 10k neurons is consistently insufficient

---

## Part 12: Open Questions for Future Sessions

These will emerge as the build proceeds:

1. **The alias table growth strategy.** Exact phrase matches only, or semantic matching via embeddings? (Affects alias table size and routing speed.)
2. **The dynamic template generation.** Hand-author templates, or auto-generate from successful LLM responses? (Affects initial setup time and template quality.)
3. **The persistent session model menu.** Per-session model choice, per-message model switching, or automatic model selection based on query type? (Affects UX and model availability.)
4. **The R2 retention horizon.** Keep raw transcripts forever, or compress to summaries after 1 year? (Affects storage cost vs. personal archive completeness.)
5. **The conflict queue resolution authority.** User-only resolution, LLM-suggested resolution with user approval, or LLM-auto-resolution for low-risk conflicts? (Affects canonical fact integrity.)
6. **The personal narrative generation.** Should the system eventually generate a "story of your education" from mastery and metaphor history, or stay as raw state without narrative? (Affects the "memory palace reflection" feature.)
7. **The maths activation day.** When maths study begins through the app, how does the maths layer transition from "witness only" to "primary study surface"? (Affects the schema's `is_foundation` flag and the UI rendering.)
8. **The multi-user future.** This is single-user now, but the architecture should be designed to support multi-user without a complete rebuild. When and how? (Affects DO namespace and D1 row-level security.)
9. **The knowledge graph versioning.** As the global state grows and nodes are added/removed, should the system maintain version history (so one can see "what the castle looked like 6 months ago")? (Affects schema complexity and R2 storage.)
10. **The AI agent layer.** Beyond the Socratic tutor, should the application have multiple specialized agents (a "debate" agent, a "synthesis" agent, a "revision" agent)? (Affects the DO design and context assembly per agent.)
11. **The offline-first architecture.** The PWA is a PWA — can it work fully offline with the knowledge graph cached locally? (Affects PWA caching strategy and sync logic.)
12. **The export/portability.** Should the entire personal state (mastery, metaphors, attempt history) be exportable as a portable format, for migration or backup? (Affects D1 export scripts and R2 archive structure.)

---

## Summary

The castle is built. The foundation is SQLite. The semantic layer is Vectorize. The personal state is the Durable Object. The ephemeral layer is the command mic. The persistent layer is the conversation threads. The metaphor system anchors new knowledge in existing understanding. The voice navigation is local and offline. The query architecture assembles context from all stores. The build path is CLI → hybrid → native. The architecture is LLM-agnostic because the intelligence lives in the infrastructure and the translation layer, not in any single model.

The shape of the knowledge is carried, not just the contents. The mental models persist. The personal state is the most valuable thing. The journey is constant. The castle grows in the user's language.
