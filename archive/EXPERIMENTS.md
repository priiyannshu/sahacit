# Deferred Experiments

> **Purpose**: A registry of experiments we do not have time to run now but may revisit later. These are NOT in the critical path. Results from any experiment here may inform future phases but will never block active work.
>
> **Rule**: Before starting any experiment, create a branch `exp/<short-name>`, run it, record results in this file, and either absorb the finding into `MASTER_PLAN.md` or discard it.

---

## 1. Route B — Chunking Experiment (Laxmikanth)

**Status**: DEFERRED · **Planned test book**: Laxmikanth (also the first Route C extraction book)

**Hypothesis**: Raw reference-book text, split into paragraphs and embedded directly (no LLM node extraction), may produce a useful "semantic map" of the book via cosine edges between paragraphs.

**Protocol**:
1. Load `processed/reference-books/laxmikanth.txt`.
2. Split at each `Chapter X` heading; within each chapter, chunk by paragraph (min 100 words, max 250 words).
3. Embed each chunk with BGE Base → 768-dim vector.
4. Upsert to Vectorize with metadata `{book: "Laxmikanth", type: "raw_chunk", chapter: "Ch3"}`.
5. Cosine similarity over Laxmikanth vectors only → candidate edges ≥ 0.65.
6. Inspect: do top edges connect genuinely related paragraphs? Can you recover the underlying concept from a cluster?
7. Compare against the LLM-extracted node graph for the same book (from Route C C1).

**Success metric**: >80% of top edges are semantically related AND clusters recover identifiable concepts.

**Decision gate after experiment**:
- **If success** → add raw-chunk embeddings as a **second Vectorize index** (or tagged subset). Query both named-node index and raw-chunk index; merge results. Chunks become a discovery layer; named nodes remain the recall layer.
- **If noisy / incoherent** → discard. Stay with Route C. No harm done — chunking was a side experiment.

**Why safe to defer**: Route B does not change the Route C pipeline. If useful, it's an *addition* (a second embedding layer), not a rework.

---

## 2. Polity Embedding Bridge Experiment

**Status**: DEFERRED

**Observation**: The 464 polity (Constitution) nodes sit in a near-isolated embedding region — almost no cross-subject bridges even at cosine 0.65 (polity↔cs max 0.575, polity↔philosophy max 0.686).

**Hypothesis**: Either (a) lowering the threshold specifically for polity↔other pairs, or (b) expanding the polity KG with more conceptually-adjacent nodes (e.g., political theory, governance concepts), would create meaningful cross-subject bridges.

**Protocol**:
- Test threshold sweep 0.55–0.65 for polity↔philosophy and polity↔history pairs.
- Or, manually inject 50–100 bridge nodes (e.g., "Separation of Powers" as polity+philosophy hybrid) and re-embed.
- Measure: do new edges surface genuine conceptual links, or just noise?

**Decision gate**: Only pursue if cross-subject discovery for polity is a felt need in daily use.

---

## 3. Auto-Generated Response Templates

**Status**: DEFERRED · **Tracked as Open Q2 in MASTER_PLAN.md**

**Hypothesis**: Successful LLM responses in persistent tutor sessions can be mined to auto-generate `response_templates` entries, reducing future alias-routing cost.

**Protocol**:
- After Phase 5 (Both Doors) is stable, run a cron or manual pass over `session_messages`.
- Identify high-quality assistant turns (user thumbs-up or follow-up engagement).
- Extract slot patterns (e.g., `{concept}` in `{context}`) → template candidates.
- Human review → promote to `response_templates`.

---

## 4. Multi-User Schema Experiment

**Status**: DEFERRED · **Tracked as Open Q8 in MASTER_PLAN.md**

**Hypothesis**: The personal-state schema designed in Phase 2 can accommodate a `user_id` column with minimal migration pain.

**Protocol**:
- After Phase 6 (MVP), create a test migration adding `user_id` to `persistent_sessions`, `node_mastery`, `personal_metaphors`, etc.
- Run dual-user simulation: two distinct `user_id`s, overlapping `node_id`s, distinct mastery values.
- Measure query latency with indexed `user_id` — acceptable or not?

**Decision gate**: Only relevant if sharing the castle (or a hosted version) becomes a goal.

---

## 5. Offline-First PWA Caching

**Status**: DEFERRED · **Tracked as Open Q11 in MASTER_PLAN.md**

**Hypothesis**: A service worker + IndexedDB can cache the full `master_nodes` subset (~15K nodes) + vector metadata locally, enabling offline discovery and alias routing.

**Protocol**:
- After Phase 5 caching strategy is defined, build a background sync worker.
- Cache hot subject data (~2K nodes) for instant offline load.
- Test on a mid-range Android device — memory and startup time.

---

## 6. KG Versioning & Snapshot Diffs

**Status**: DEFERRED · **Tracked as Open Q9 in MASTER_PLAN.md**

**Hypothesis**: As the KG grows, users may want to see "what changed since last month" — new nodes, deprecated concepts, edge re-wiring.

**Protocol**:
- Store monthly `master_nodes` + `master_edges` + `semantic_edges` dumps in R2.
- Build a diff viewer: added nodes (green), removed (red), similarity drift (yellow).
- Render as a time-slider on the per-subject graph.

---

(End of file — add new experiments at the bottom with the same structure: hypothesis, protocol, success metric, decision gate.)
