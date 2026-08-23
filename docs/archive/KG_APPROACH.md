# KG Construction Approach — Route C (ARCHIVED)

> **⚠️ ARCHIVED — 2026-07-28**
> All decisions in this file have been merged into `MASTER_PLAN.md` (Phase 10 and Phase 11). This document is preserved for reference only. **Do not modify.** For the active plan, see `MASTER_PLAN.md`.
>
> **Status**: ARCHIVED. Decisions reflected in MASTER_PLAN.md Phase 1 (LLM reasoning backfill), Phase 10 (Route C pipeline + external KG expansion), and Phase 11 (per-subject graphs + embedding-space view).
> **Owner**: Priyanshu + Claude. **Stack**: Cloudflare D1 + Vectorize (768-dim BGE Base) + local BGE embedding scripts.

---

## 0. TL;DR Decision

- **Primary path = Route C**: LLM extracts **nodes only** from text → merged into a unified KG in D1 → BGE Base embeds every node → cosine similarity produces candidate semantic edges → **LLM reviews & labels** the edges above a threshold → labelled edges stored in D1 `semantic_edges`.
- **Chunking route (Route B) is DEFERRED** to a future experiment — run on one reference book, results inform whether raw-text embedding becomes a supplementary layer. It does NOT block Route C.
- Edges are **never** LLM-inferred directly from text. They are discovered by vector similarity, then labelled by LLM. This removes hallucination from edge creation and keeps LLM cost low.
- The existing 2,827 external-source KG nodes (polity_art_*, phil_*, cs_*) are **kept as-is**; new UPSC nodes are added alongside them and cross-subject edges are computed across the full set.

---

## 1. Why Route C (Not Pure-LLM Edges, Not Pure-Chunking)

Three candidate approaches were considered:

| Route | What happens | Edge source | LLM cost | Edge quality |
|---|---|---|---|---|
| **A — LLM extracts nodes + edges** | LLM reads text → produces (concept, relation, concept) triples | LLM output | High (2+ passes / chapter) | Medium; **hallucination risk** — LLM invents plausible-but-false links |
| **B — Chunk → embed raw text** | Split text into paragraphs → embed each → cosine edges | Vector similarity | ~0 for extraction | Anonymous paragraph links; no concept labels; too granular for recall |
| **C — LLM nodes → embed → cosine → LLM-label** (CHOSEN) | LLM extracts concepts only → embed → cosine gives candidate edges → LLM labels top edges | Vector similarity (discovery) + LLM (labelling only) | 1 extraction pass + selective review | **High** — discovery is objective, labels are accurate on a small reviewed set |

**Route C wins** because:
1. Vector similarity is **objective** — two concepts are linked because their usage contexts are genuinely close, not because an LLM guessed they should be.
2. LLM is used only where it adds value (extraction of concepts; labelling of high-confidence edges) — never for the volume edge-inference step.
3. It matches the structure we already have: the 342 NCERT chapter JSONs are concept-level nodes with explicit labels. That granularity (1 node = 1 recognizable concept) is exactly what a learner needs against a PYQ surface. Paragraph chunks (Route B) are too small to be study units.

---

## 2. Route C — Phased Pipeline

Each phase is a self-contained unit with inputs, outputs, and an exit criterion. Mirror this into MASTER_PLAN.md Phase 10/11.

### Phase C1 — Reference-Book Node Extraction (LLM pass)

**Goal**: Convert reference-book texts into structured node JSONs (nodes only, no edges).

**Inputs**: `processed/reference-books/*.txt`
- `laxmikanth.txt` (2.3 MB, Polity)
- `nitin_singhania.txt` (1.5 MB, Art & Culture)
- `shankar_ias.txt` (2.1 MB, Environment)
- `ramesh_singh.txt` (Economics)
- `bipin_chandra.txt`, `rs_sharma.txt`, `satish_chandra.txt`, `upinder_singh.txt` (History)
- `constitution_of_india.txt` (Constitution)

**Method**: LLM (Sonnet, per AGENTS.md "spawned-agent permissions" — read-only Sonnet returning JSON) reads each book chapter-by-chapter and emits:

```json
{
  "id": "subj_short_concept",
  "subject": "geography|polity|history|economics|science",
  "topic": "chapter topic",
  "label": "Human Concept Name",
  "type": "concept|institution|person|event|theory",
  "detail": "50-75 word description (recognition-against-context, not prose)",
  "source_book": "Laxmikanth",
  "source_chapter": "Chapter 3: Federalism",
  "pyq_match": []
}
```

**Constraints**:
- LLM produces **nodes only**. No `relation` field. No edges.
- Node detail follows the cognitive-substrate principle (from archive memory): crisp discriminating detail over comprehensive prose; 50-75 words; structured bullets for closed sets.

**Extraction order** (per user decision): **one book at a time, starting with Laxmikanth** (the chunking-test book — see §4). Proceed to the next book after observing results.

**Outputs**: `processed/reference-books/<book>_nodes.json` per book.

**Exit criterion**: Each reference book has a `_nodes.json` with deduped concept nodes, no edges, correct subject/topic labels.

---

### Phase C2 — Unified KG Assembly (D1 merge)

**Goal**: Merge all node sources into one D1-hosted KG, deduplicating concepts.

**Sources to merge**:
1. `processed/ncert/*/*.json` — 342 chapter files, **9,789 raw nodes → 4,716 unique IDs** (see §3 for the collapse math).
2. Reference-book `_nodes.json` from C1 (new nodes).
3. Existing D1 `master_nodes` (2,827 external-source nodes: polity_art_*, phil_*, cs_*) — **KEPT AS-IS**.

**Operations**:
1. Insert NCERT nodes into `master_nodes` (dedupe by `id`; if `id` already exists from another chapter, merge `source_chapters` list).
2. Insert reference-book nodes into `master_nodes` (dedupe by normalized label + subject).
3. Insert NCERT JSON `edges[]` into `master_edges` (these are the within-subject, chapter-authored edges: `from`, `to`, `relation`).
4. **Deduplication rule**: match by normalized label (lowercase, strip punctuation). If "Federalism" exists in NCERT Ch1 and Laxmikanth Ch3, keep one canonical node; link both `source_chapter` / `source_book` to it. Do NOT auto-merge across the existing 2,827 external nodes unless a clear match (e.g., `polity_art_21` ↔ a "Right to Constitutional Remedies" node) — leave cross-layer edges to C4.

**Exit criterion**: `master_nodes` count = 2,827 (existing) + ~4,716 (NCERT unique) + reference-book nodes. `master_edges` contains all NCERT-authored edges. No node has duplicate `id`.

---

### Phase C3 — Embedding All KG Nodes

**Goal**: Produce 768-dim BGE vectors for every node in the unified KG.

**Method**:
1. For each node build embedding text: `title + ": " + summary[:300] + ". " + canonical_facts[:3]`.
2. Batch-embed with BGE Base (`models/kg-embeddings/.../bge-base-en-v1.5`) — same model already used for the 2,827 KG nodes.
3. Output `kg/output/vectors.ndjson` (id + 768-dim normalized values + metadata: subject, topic, title).
4. **Upsert to `prelims-concept-vectors`** — additive. Existing 2,827 vectors stay. New vectors are added. (Do NOT clear the index.)

**Total vectors after upsert**: ~2,827 + ~4,716 + reference-book nodes ≈ **15,000–18,000**.

**Note on embedding mechanics** (see §5 for detail): BGE tokenizes → transformer encoder (self-attention) → mean-pool → L2-normalize. Cosine similarity between two normalized vectors = their dot product. The model "knows" no meanings — it places text with similar usage context near each other in 768-dim space.

**Exit criterion**: `wrangler vectorize list-vectors prelims-concept-vectors` count == total node count in D1 `master_nodes`. Index holds BOTH old KG + new UPSC vectors.

---

### Phase C4 — Semantic Edge Computation (cosine)

**Goal**: Compute cross-subject semantic edges via cosine similarity over the full vector set.

**Method**:
1. Load all vectors (old + new) into a numpy array.
2. Compute full pairwise cosine similarity matrix.
3. Filter: `similarity >= threshold` AND `subject_A != subject_B` (cross-subject only — within-subject edges already come from NCERT JSONs in C2).
4. Write `kg/output/insert_semantic_edges.sql` (columns: source_node_id, target_node_id, source_subject, target_subject, similarity_score, reasoning=NULL, created_at).
5. Execute via `wrangler d1 execute prelims-master-db --remote --file ...`.

**Threshold**: Start at **0.65** (established in prior session — 0.75 was too strict, yielding only 22 edges all philosophy↔cs). After the full 15K+ distribution is visible, re-evaluate. Likely raise to **0.70–0.75** for cross-subject UPSC edges (concepts are more domain-specific than the philosophy↔cs term-overlap that dominated before).

**Exit criterion**: `SELECT COUNT(*) FROM semantic_edges` reflects the new cross-subject edges. Distribution histogram of similarities reviewed; threshold locked.

---

### Phase C5 — LLM Edge Review & Labelling

**Goal**: Add explicit relationship types to candidate edges (the loss-of-label problem is solved here).

**Method**:
1. For each candidate edge above threshold, present to LLM (Sonnet): source node label + detail, target node label + detail, cosine score.
2. LLM assigns `relation_type` (e.g., `constitutional_basis_for`, `challenges`, `prerequisite_for`, `complementary_with`, `contradicts`, `temporal_precedes`) + `confidence`.
3. UPDATE `semantic_edges` rows with `relation_type` and backfill the `reasoning` column (deferred in prior session — now filled).

**Cost profile**: Only edges above threshold get reviewed. Expect a few hundred to a few thousand edges across 15K nodes — manageable batch sizes. This is the **only** LLM cost for relationships, and it's selective.

**Exit criterion**: Every `semantic_edges` row above threshold has a non-NULL `relation_type` and `reasoning`.

---

### Phase C6 — Visualization (per-subject graph + embedding space)

**Goal**: Deliver the Obsidian-style per-subject graphs and an optional embedding-space view.

**Per-subject graphs** (primary deliverable):
- Query D1: `SELECT * FROM master_nodes WHERE subject = 'polity'` + edges where both endpoints are polity nodes.
- Render as force-directed graph (D3.js / Cytoscape.js with fCose/Cola layout) — one view per subject (history, geography, polity, economics, science).
- Nodes sized by edge degree (more connections = more important). Edges colored/thickness by similarity or relation_type.
- This is the "global state castle" — the learner navigates concept space, not a textbook table of contents.

**Embedding-space visualization** (Phase 2 nice-to-have):
- Export `vectors.ndjson` → run UMAP/t-SNE → 2D projection → scatter colored by subject/topic.
- Shows cluster structure (philosophy cluster, CS cluster, polity cluster, UPSC clusters) and the **bridges** where cross-subject semantic edges exist.
- Could be interactive in the PWA via a client-side `ml-lib` UMAP if desired later.

**Exit criterion**: At least polity surface graph renders from live D1 data. Embedding-space scatter produced as a static artifact (Phase 11 in MASTER_PLAN.md).

---

## 3. The Node Collapse Math (9,789 → 4,716)

From data analysis of `processed/ncert/*/*.json` (2026-07-28):

| Metric | Count |
|---|---|
| Raw nodes across all 342 NCERT JSONs | **9,789** |
| Unique node IDs | **4,716** |
| Unique labels (by name) | 4,623 |
| Labels appearing >1x, same subject (different chapters) | 4,349 |
| Labels appearing >1x, cross-subject | 126 |

**Why the collapse**: The same concept (same `id`) is extracted independently in multiple chapter JSONs. E.g., `pol_federalism` appears in Polity Ch1, Ch2, etc. Deduplicating by `id` collapses 9,789 → 4,716.

**The old 4,720-node UPSC KG** = 4,716 deduplicated NCERT IDs + a handful of reference-book / cross-subject bridging nodes. So the old flat graph was simply the deduplicated version of the raw chapter JSONs we already have.

**Cross-subject overlap examples** (126 labels span 2+ subjects):
- "Abolition of Untouchability" → history (`hist_abolition_untouchability`) + polity (`pol_abolition_of_untouchability`)
- "Acid Rain" → geography + science
- "Agenda 21" → geography + polity
- "Animal Husbandry" → science + economics
- "Antarctica" → geography + polity

These overlaps are exactly what C4's cross-subject cosine edges will surface and C5 will label.

---

## 4. Chunking Route (Route B) — DEFERRED EXPERIMENT

**Status**: NOT in the critical path. Run as a side experiment when convenient (e.g., while C1–C5 proceed on the main track).

**Hypothesis**: Raw reference-book text, split into paragraphs and embedded directly (no LLM node extraction), may produce a useful "semantic map" of the book via cosine edges between paragraphs.

**Protocol** (per user decision: test on **Laxmikanth**, split **by "Chapter X" heading first, then paragraphs**, success = **>80% of top edges semantically related**):

1. Load `laxmikanth.txt`.
2. Split at each `Chapter X` heading; within each chapter, chunk by paragraph (min 100 words, max 250 words).
3. Embed each chunk with BGE Base → 768-dim vector.
4. Upsert to Vectorize with metadata `{book: "Laxmikanth", type: "raw_chunk", chapter: "Ch3"}`.
5. Cosine similarity over Laxmikanth vectors only → candidate edges ≥ 0.65.
6. Inspect: do top edges connect genuinely related paragraphs? Can you recover the underlying concept from a cluster?
7. Compare against the LLM-extracted node graph for the same book (from C1).
8. **Evaluation**: cluster coherence, noise level (% spurious edges), concept recoverability, token/cost comparison.

**Decision gate after experiment**:
- **If >80% of top edges are semantically related AND clusters recover identifiable concepts** → add raw-chunk embeddings as a **second Vectorize index** (or a tagged subset of the same index). Query both the named-node index and the raw-chunk index; merge results. Chunks become a discovery layer; named nodes remain the recall layer.
- **If noisy / incoherent** → discard. Stay with Route C. No harm done — chunking was a side experiment.

**Why it's safe to defer**: Route B does not change the Route C pipeline. If it proves useful, it's an *addition* (a second embedding layer), not a rework.

---

## 5. Embedding Mechanics — What BGE Base Actually Does

Reference for anyone modifying this pipeline later.

```
Text → Tokenize → Transformer Encoder → Mean Pool → L2 Normalize → 768-dim vector
```

1. **Tokenize**: Text → ~30K subword units (e.g., `"Federalism"` → `["Feder", "alism"]`). Handles any English word incl. domain jargon by decomposing into known subwords.
2. **Transformer Encoder**: All tokens pass through self-attention layers simultaneously. Every token's vector is contextualized by every other token. ("bank" in "river bank" vs "bank account" → different vectors.) Not sequential left-to-right reading.
3. **Mean Pool**: All per-token vectors averaged into one 768-dim vector = the node embedding.
4. **L2 Normalize**: Vector scaled to unit length. After this, **cosine similarity = dot product** — trivial to compute for edge discovery.

**What the model "knows"**: No dictionary of meanings. During pretraining on ~3.3B tokens (Wikipedia, web, books), it learned to place text with similar usage context near each other. "Federalism" sits near "constitution", "government", "rights" because those words co-occur in similar contexts — not because the model understands the concept.

**Coverage limits**: Strong on common English concepts; weaker on rare UPSC-specific terms ("doctrine of eclipse", "panchayati raj"); poor on Hindi/mixed-language text (relevant for some NCERT content).

---

## 6. LLM Usage & Cost Profile (Route C)

| Step | LLM? | Notes |
|---|---|---|
| NCERT JSON creation | Yes (already DONE) | 342 chapter files, one-time cost, concept-level |
| C1 — Reference-book node extraction | **Yes** (1 pass/book) | Nodes only, no edges. Sonnet, read-only, returns JSON |
| C3 — Embedding | **No** | BGE Base local batch, automated |
| C4 — Edge computation | **No** | Cosine similarity, automated |
| C5 — Edge labelling | **Yes** (selective) | Only edges above threshold; Sonnet assigns relation_type + reasoning |
| **Total LLM passes** | **2** | Extraction + selective review |

**Comparison vs old approach** (LLM read textbooks + generated edges): old used 2–3 LLM passes per chapter AND risked hallucinated edges. Route C uses 1 extraction pass + 1 selective review, with edges discovered objectively by cosine.

---

## 7. Mapping to MASTER_PLAN.md

This approach maps onto existing phases:

- **Phase 10 (Ready-Made KG Expansion)**: C1 (ref-book extraction) → C2 (unified KG) → C3 (embed) → C4 (semantic edges) → C5 (LLM label). The "Ready-Made KG" is the deduplicated NCERT + reference-book concept graph.
- **Phase 11 (Visualization)**: C6 (per-subject force-directed graphs + UMAP embedding-space view).
- **Phase 1 (Semantic Layer Completion)**: the existing 2,827 KG nodes are KEPT; C3 adds UPSC nodes to the same Vectorize index. Cross-subject edges in C4 will finally include UPSC↔UPSC and UPSC↔KG bridges (currently absent — the 674 edges are 99.3% philosophy↔cs).

**Open items to resolve when wiring into MASTER_PLAN.md**:
1. Which reference book is the C1 starting point — **Laxmikanth** (also the chunking-test book).
2. Chunking split method for Laxmikanth — **by Chapter heading, then paragraphs**.
3. Chunking success metric — **>80% of top edges semantically related**.
4. Existing 2,827 nodes policy — **keep as-is, add cross-subject edges with new UPSC nodes** (do NOT delete; do NOT merge/dedupe against them unless clear match).
5. Extraction order — **one book at a time, Laxmikanth first**.

---

## 8. Key Files & Commands (for implementation sessions)

**Inputs**:
- `processed/ncert/<subject>/*.json` — 342 chapter KGs (nodes + edges)
- `processed/reference-books/*.txt` — raw textbook texts
- `kg/output/old_master_nodes_archive.json` — D1 export of old 4,720 KG (reference only, not reused)
- `models/kg-embeddings/.../bge-base-en-v1.5` — local BGE model

**Scripts** (extend, don't rewrite):
- `scripts/ingest_kg.py` — currently extracts from 3 external KGs + embeds. Extend to also ingest NCERT JSONs + reference-book `_nodes.json`.
- New: `scripts/build_unified_kg.py` — merges NCERT + ref-book nodes into `master_nodes` with dedupe.
- New: `scripts/compute_semantic_edges.py` — cosine over full vector set → `insert_semantic_edges.sql`.
- New: `scripts/label_edges.py` — LLM review of edges above threshold → UPDATE `semantic_edges`.

**D1**:
```bash
wrangler d1 execute prelims-master-db --remote --command "SELECT COUNT(*) FROM master_nodes;"
wrangler d1 execute prelims-master-db --remote --file kg/output/insert_semantic_edges.sql
```

**Vectorize**:
```bash
wrangler vectorize upsert prelims-concept-vectors --file kg/output/vectors.ndjson
wrangler vectorize list-vectors prelims-concept-vectors --json
```

**R2** (still pending from Phase 1): `wrangler r2 bucket create session-archives && wrangler r2 bucket create raw-inbox` + bind `MEDIA_BUCKET` in `wrangler.jsonc`.
