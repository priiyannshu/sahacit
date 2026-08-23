# How the 11 Eras Were Built

All 11 history eras built 2026-04-17 → 2026-04-19 (3 days of focused work). This file captures the process, the principles, and the context — so that a future session (or a future you) can pick up the spine without re-deriving it.

## Pre-history (what came before the era-by-era work)

A bulk session spanning 2026-04-10 to 2026-04-14 produced `draft/universe.json` — 4,668 nodes + 852 timeless, 8,470 edges, 2,839 PYQs, 11 eras tagged at node level. The accompanying `draft/timeline.html` was a territorial stream-graph (~1,800 lines) with canvas rendering, hash-based node navigation, and subject toggles. It loaded `universe.json` via `fetch()` — which doesn't work on `file://` in modern browsers, hence the inlining we did 2026-04-19 to preserve viewability.

That bulk work was a **starter**, not a source of truth. It proved the shape of the problem but carried too many mis-tagged nodes, stale labels, and shallow details. Mid-April the approach pivoted: **build each era as a self-contained unit**, using universe.json only as a seed.

The `draft/` folder now lives at `archive/draft/`. Its node tags are not maintained. Era folder files are canonical.

## The build timeline (11 eras in 3 days)

| Era | Built | Nodes | PYQs triaged |
|---|---|---|---|
| 1. Prehistoric | 2026-04-17 20:23 | 71 | 2 |
| 2. Ancient Indus | 2026-04-17 23:57 | 115 | 18 |
| 3. Ancient Classical | 2026-04-18 01:35 | 266 | 80 |
| 4. Early Medieval | 2026-04-18 10:23 | 214 | 44 |
| 5. Delhi Sultanate | 2026-04-18 11:50 | 204 | 77 |
| 6. Mughal | 2026-04-18 14:13 | 263 | 70 |
| 7. Early Colonial | 2026-04-18 16:26 | 283 | 187 |
| 8. High Colonial | 2026-04-18 17:44 | 233 | 174 |
| 9. Freedom Struggle | 2026-04-18 21:12 | 389 | 238 |
| 10. Post-Independence | 2026-04-18 23:10 | 516 | 259 |
| 11. Contemporary | 2026-04-19 11:00 | 542 | 731 |
| **TOTAL** | | **3,096** | **~1,880** (slots; boundary-PYQs overlap) |

Density scales with recency — modern eras (8-11) hold over half the nodes because UPSC prelims heavily tests post-1757 content, and the contemporary era absorbs temporal polity + thematic streams that don't fit neatly into a history narrative alone.

## The workflow (converged from era 9 onwards)

Eras 1-8 used roughly this order, but **stage design came BEFORE reference-book sweeps** — that caused era 8 to design 14 India stages on a thin post-audit pull, only for Bipin Chandra's sweep to add 79 more nodes that forced Option D lane splits. Rework. Era 9 corrected the order:

1. **Pull** — nodes tagged to this era in `archive/draft/universe.json`
2. **Audit** — park non-temporal nodes, dedup, retag mislabeled boundary cases
3. **NCERT chapter sweep** — 2-4 chapters bundled per pass, extracting new nodes
4. **Reference-book sweeps** — primary books for the era (see Sources below)
5. **Temporal polity sweep** — from Laxmikanth (amendments, cases, institutions, electoral events); relevant era 9 onwards where polity becomes dense
6. **Stage design** — *now*, with full content in hand. Stages emerge from content, not the other way around.
7. **PYQ triage** — scan the 2,839-PYQ master file, keep what maps to this era
8. **Build** — `<era>.json` (data) + `<era>.html` (self-contained viz with JSON baked inline)
9. **Knowledge audit** — second pass for gaps; gap-fill adds nodes the primary sweep missed
10. **UI audit** — check the HTML for visual regressions, lane overflow, label collisions, cross-era leakage
11. **Close-out** — one-line summary; recorded per-era informally, era 11 got a formal `_close_out.md` which is now this file

## Key principles

- **Brain does the work.** Claude fetches, clarifies, and presents material. The user builds synthesis and connections. No bulk auto-generation of the knowledge graph.
- **No bulk operations.** Work one era at a time. Rough edges surface through interaction, not upfront algorithms.
- **`raw/` is read-only.** All outputs go to `processed/` or era folders. Source PDFs are never modified.
- **Chronological order.** Eras built 1 → 11 in sequence. Each later era can pull boundary nodes from earlier closed eras; earlier eras don't retroactively change.
- **Era files are source of truth.** `archive/draft/universe.json` is frozen; ignore its tags. The `eras/N.era-name/<era>.json` files are canonical.
- **Stages emerge from content.** Don't lock stage design before sweeps — the content reshapes the structure.
- **Self-contained HTMLs.** Each `<era>.html` bakes its `<era>.json` inline, so opening one on `file://` works without a server. Entire era ships as a single static file.
- **Honesty over completeness.** Unanswerable gaps are marked, not papered over. The next-phase audit priorities are exactly those gaps.

## Architectural decision (era 9)

The timeline's metaphor isn't "history" — it's "anything dated." Forcing non-temporal polity into timeline form distorts it; forcing temporal polity into a separate surface fragments study. The split follows the natural shape of the content. Four surfaces planned:

1. **Timeline** (done, this work) — all temporal syllabus content: history + temporal polity + thematic stages
2. **Map + temporal slider** (future) — geography, spatial-primary with time overlays
3. **Non-temporal polity + economics** (future) — institutional/conceptual content (Parliament, FRs, federalism, Keynesian theory)
4. **Science** (lowest priority) — engineering backgrounds suffice via YouTube refreshers

## Data shape conventions

**Era JSON** — `{metadata, era, stages, nodes}`. Each node:
```
{id, label, type, subject, detail, year, stage, era, temporal_type,
 pyq_count, pyq_ids, importance, book?, chapter_title?, chapter_file?}
```
`detail` is short prose (1-4 sentences); `stage` references a stage in the stages array; `year` is signed integer (BCE negative).

**Era HTML** — SVG-based territorial stream-graph. Each node renders as `.node-card` (SVG foreignObject div) with `data-id="<nodeId>"`. Hover tooltip shows label + temporal range + detail. No click, no modal. No hash-based deep-link handler — would need adding (~15 lines) if the PYQ interface wants to jump into specific nodes.

**Per-era PYQ bank** (`pyqs_<era>_era.json`) — **schema inconsistent across eras**, reflecting iterative refinement of the triage approach:

| Eras | Schema |
|---|---|
| 1-6 | `{pyqs: [...]}` with optional `nodes: [...]` on each PYQ (only era 1 used it, for 1 of 2 PYQs) |
| 7 | `{metadata, questions, dropped_in_triage, dropped_total}` |
| 8 | `{metadata, high, medium, boundary}` — split by triage confidence |
| 9 | `{era, counts, pyqs_high, pyqs_medium, pyqs_boundary}` — similar split, different key names |
| 10 | `{era, triage_date, questions, ...}` with `triage_level` field on each PYQ |
| 11 | `{meta, pyqs}` with `era11_bucket` field on each PYQ |

Any tool consuming these banks needs to normalize the shape.

## Sources consulted

- **NCERT** Classes 6-12, 5 subjects (history, geography, economics, polity, science) — baseline sweeps
- **Nitin Singhania** *Indian Art and Culture* — Art & Culture, UNESCO lists, classical arts
- **M. Laxmikanth** *Indian Polity* — amendments, cases, institutions, electoral events
- **Ramesh Singh** *Indian Economy* — reforms, banking, Modi schemes
- **Bipin Chandra** *India's Struggle for Independence* + *India Since Independence* — freedom struggle through contemporary
- **Shankar IAS** *Environment* — treaties, ecosystems, Indian env laws
- **Constitution of India** (Bare Act, 2024) — amendment articles, constitutional provisions
- **Upinder Singh** *A History of Ancient and Early Medieval India* — acquired during era 4; full sweep through 12th century; reserved for the post-eras cross-reference audit of eras 1-4
- **Insights on India** monthly compilations (Jan 2025 - Jan 2026) — current affairs; **deferred**, user to integrate later

## Known limitations

- **PYQ-to-node curation barely started.** Only 1 PYQ (of era 1's 2) has a `nodes: [...]` link. The proof interface (next task) exists to close this.
- **Current affairs Jan 2025-Apr 2026** not yet absorbed into era 11 — deferred pending user-led integration from Insights compilations.
- **Thin era-11 stages** — s05 UPA-II (8 nodes), s08 Modi-III (4), s09 Kashmir/Punjab (5), s10 Terrorism (3), s24 Digital India (5), s28 2008 GFC (3). Acceptable for viz; could be enriched per-PYQ later if needed.
- **No user-added edges.** Per the project convention, edges between nodes are a study artefact the user builds, not a bulk-generated graph structure.
- **No cross-era deep-link** from era HTMLs. Each HTML is a closed island. The PYQ interface will render linked nodes inline; opening the source era for context would need a hash-focus handler added to each of 11 HTMLs.

## What comes next

Ordered by the close-out from era 11, updated 2026-04-19:

1. **PYQ proof-of-architecture interface** — the structural proof that the 3,096 nodes suffice to answer UPSC prelims PYQs. Plan drafted this session. `eras/_pyq_interface/` will hold the normalized index, curation artifact, and self-contained viewer.
2. **Upinder Singh audit** of eras 1-4 (with Bipin Chandra boundary checks for 5-11).
3. **Unified viz design pass** — consolidated review of colors, spacing, typography across all 11 era HTMLs.
4. **Geography map + slider surface** (future).
5. **Non-temporal polity + economics surface** (future).
6. **Science** (last priority).
7. **Current affairs integration** into era 11 (user-led).

## In one sentence

*Between 2026-04-17 and 2026-04-19, the 4,668-node draft universe was rebuilt era-by-era into 11 self-contained, chronologically-ordered timeline artifacts totalling 3,096 curated nodes and 1,880 triaged PYQ slots, replacing a bulk-generated scratch file with a human-synthesized spine that the next phase — PYQ proof — will validate against ~1,700 questions from 30 years of UPSC prelims.*

Built 2026-04-17 through 2026-04-19. UPSC Prelims 2026: 24 May 2026.
