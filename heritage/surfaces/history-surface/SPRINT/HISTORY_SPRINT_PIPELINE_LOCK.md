# History Sprint — Pipeline Lock (Convergence Session Output)

**Date:** 2026-05-16
**Status:** v1 — locks the pipeline for Mughal pilot production
**Inputs reviewed:** Task 1 (PYQ weights) + Task 2 (Mughal bundles) + Task 3 (Style brief) + Task 4 (Graph schema + Mughal instance) + Task 5 (PWA scaffolding sketch)
**Architecture reference:** `HISTORY_SPRINT_ARCHITECTURE.md`
**Output:** This file is the gate document. Mughal production may begin once the action items in §4 are complete.

---

## 1. Convergence Decisions

Five decisions resolved. One previously-proposed decision (D6) was removed from scope.

### D1 — Story & anchor budget for Mughal: **ACCEPT 19 stories / 76 anchors**

Architectural target (10–15 stories, ~30–45 anchors) was a guideline, not a contract. Faithful application of the embodied-episode test legitimately pushed the count up — splitting Aurangzeb's reign into 3 scenes (s08 Delhi-Jizya / s09 Aurangabad / s10 Anandpur) and splitting the economy stage into two (s14 Surat-port / s15 Bihar-village) added the four stories above the upper bound. The 43 narrative-source anchors are downgradable to caption-fly-bys if production pace lags; 33 PYQ-earned anchors are non-negotiable.

**Production math** (sanity check, not a contract):
- 19 stories × ~9 panels avg = ~170 panels for Mughal pilot
- Establishing + wide-interior (2 base panels) + anchor panels (~4 avg) + fly-by interactions (~2–3) per story
- Feasibility verified empirically against Task 3 panel-generation throughput; budget holds within the 8 days remaining to the home exam (2026-05-24)

**Mid-production downgrade policy:** If pace slips, demote narrative-source concept anchors first (e.g., `hist_basohli_painting`, `hist_proto_industrialisation`, `hist_hundi_system`) to `mention_shape: caption`. PYQ-earned and PYQ-suggestive anchors are protected.

### D2 — Anchor render order: **fix the sort, re-emit graph JSON**

Current `mughal_graph.json` orders `anchors[]` by **PYQ-count descending**. Task 5 §3.4 specifies "anchors array order is production intent" — i.e., the PWA renders panels in array order. These two facts are in conflict: rendering s04 by PYQ-desc opens with Akbar's face, when the embodied scene demands establishing-shot first (Fatehpur Sikri exterior / Ibadat Khana interior) before character close-ups.

**Resolution:** Replace the PYQ-count sort in `_task2_mughal_bundles/build_bundles.py` with a panel-flow priority sort that follows Task 3's tested panel sequence (A→B→C/D→E→F).

**Default sort key per anchor:**

```
priority_for_render_order = {
    "place":       0,   # establishing / background grammar
    "institution": 1,   # interior / system establishment
    "person":      2,   # character close-ups
    "event":       3,   # battle / promulgation scenes
    "empire":      3,   # tied with event
    "concept":     4,   # diagrammatic / Panel-E register
    "reform":      4,   # tied with concept
    "movement":    4,   # tied with concept
    "period":      99,  # period nodes never anchor (see schema invariant 1)
}

sort_key = (priority, -pyq_count)
```

This yields, for s04: Fatehpur Sikri → Ibadat Khana → Akbar → Abu'l Fazl → Tansen → Sulh-i-kul → Mughal Painting. Matches embodied-narrative flow.

**Per-story override:** If the default ordering fails a specific story's embodied logic (rare — flag during production), the bundle source spec accepts an explicit `anchor_render_order_override: [node_id, …]` field on the story. `build_bundles.py` honors the override when present.

**No schema doc change required** — the schema already states "Ordered array; render order is production intent." Action is purely in `build_bundles.py` + re-run.

### D3 — Parallel-meta rendering (s19 Six Courts): **carousel of 6 sub-scenes**

Task 3 did not test parallel_meta panels. Split-screen rendering at phone size is high-risk: six contemporaneous courts in one composition is hard to keep readable. Carousel is conservative and matches phone-first PWA constraints.

**Sub-scene partition:** Six sub-scenes, one per civilization track in the bundled stages:
1. Mughal (India) — Akbar's Fatehpur Sikri
2. Ottoman — Murad III's Istanbul
3. Safavid — Abbas I's Isfahan
4. Ming → Qing transition — Beijing
5. Tudor / Elizabethan — London
6. Counter-Reformation Europe — Rome / Jesuit network

**Per sub-scene budget:** 1 establishing panel + 1 anchor panel (light visual budget — parallel-meta is meta, not embodied). Total for s19: ~12 panels (vs. ~9 for an embodied story). Acceptable.

**Schema:** No change. PWA reads `story_kind: parallel_meta` and switches comic-viewer layout from sequential-stream to swipeable-carousel.

**Sub-scene anchor mapping:** Production task. The two existing s19 anchors (`hist_jesuits`, `hist_proto_industrialisation`) anchor in the Counter-Reformation and pan-Eurasian sub-scenes respectively. Other sub-scenes carry establishing panels only (no dedicated anchor) — fine, since the parallel-meta's purpose is contrast, not depth.

### D4 — PWA navigation: **single-route tab model**

`#timeline/{eraId}` → era home with JS tab switcher (Narrative / Stories / Timeline). Sub-routes `/narrative`, `/stories` are removed. Story detail keeps its own route: `#timeline/{eraId}/story/{storyId}`.

Matches polity surface pattern. Simpler state. Task 5 §10.1 alternate (multi-route) discarded.

### D5 — PWA back navigation: **breadcrumb**

Comic viewer → back → Stories tab of era home.
Era home → back → Carousel.
No "always carousel" rule. User expectation prevails over implementation simplicity.

Task 5 §1 should be revised to remove "Back button on narrative/stories/comic → return to carousel" and replace with "Back returns to parent view (story → stories tab; era → carousel)."

### D6 — Summon-hosts mechanism: **REMOVED FROM SCOPE**

The audio-generation CTA, summon-hosts modal, and "Copy context → NotebookLM" button are **not in the PWA**. The `trigger_note` field stays in the schema as offline-workflow metadata (user reads it when generating NotebookLM audio manually), but it never renders in the PWA.

**Implication for Task 5:** §6 ("Summon Hosts Mechanism") is deleted from the spec. Audio-trigger buttons in the comic viewer (Task 5 §3.4, §5) are retained but their semantics narrow: they are *playback controls* for audio files that already exist on disk. They show nothing (or stay hidden) when no audio file is present. No generation UI of any kind.

---

## 2. Production Pipeline (Locked Order)

```
[Task 1 PYQ weights]  ──┐
[Task 2 bundles MD]   ──┤
                        │
                        ▼
            build_bundles.py  ──>  MUGHAL_BUNDLES.json   (D2: re-sort anchors)
                        │
                        ▼
            build_mughal_graph.py ──> mughal_graph.json   (re-emit; invariants re-verified)
                        │
                        ▼
            [Per-story production loop]
                │
                ├──> Panel manifest:  6.mughal/panels/{story_id}/manifest.json
                ├──> Gemini prompts:  derived from Task 3 style brief + story scene_setting + anchors
                ├──> Panel images:    6.mughal/panels/{story_id}/panel_NNN.png
                │
                ▼
            PWA wiring (Task 5 implementation)
                │
                ├──> Phase 1: data loader + STATE.eraGraphs
                ├──> Phase 2: era home + story gallery + comic viewer
                ├──> Phase 3: parallel_meta carousel branch
                │
                ▼
            [Audio production — deferred per architecture §7]
                │
                └──> Schema audio_slots populated retroactively when files exist
```

**Not in this pipeline (decoupled):**
- Narrative chapter prose — already exists at `6.mughal/narrative.md`. PWA fetches separately. Path is in `era.narrative_chapter_path`.
- Adjacency edges — emitted in Task 4, audio-layer consumer (deferred).

---

## 3. File Layout (Authoritative)

| Path | Content | Producer |
|---|---|---|
| `surfaces/history-surface/SPRINT/HISTORY_SPRINT_PIPELINE_LOCK.md` | This file | Convergence session |
| `surfaces/history-surface/SPRINT/HISTORY_SPRINT_ARCHITECTURE.md` | Design decisions, cognitive-mode model | Pre-sprint brainstorm |
| `surfaces/history-surface/SPRINT/HISTORY_SPRINT_PYQ_WEIGHTS.{md,json}` | Per-era PYQ weights | Task 1 / `_task1_pyq_weights.py` |
| `surfaces/history-surface/SPRINT/HISTORY_SPRINT_MUGHAL_BUNDLES.{md,json}` | 19 Mughal stories, anchor/fly-by lists | Task 2 / `_task2_mughal_bundles/build_bundles.py` |
| `surfaces/history-surface/SPRINT/HISTORY_SPRINT_STYLE_BRIEF.md` | Locked base style + Mughal variation | Task 3 |
| `surfaces/history-surface/SPRINT/references/s04_panel_{a..f}.png` | Style reference panels | Task 3 |
| `surfaces/history-surface/SPRINT/HISTORY_SPRINT_GRAPH_SCHEMA.md` | Schema spec | Task 4 |
| `surfaces/history-surface/SPRINT/TASK_5_PWA_SCAFFOLDING_DESIGN.md` | Component contracts (revise per D4/D5/D6) | Task 5 |
| `surfaces/history-surface/6.mughal/mughal_graph.json` | Era graph instance (consumed by PWA) | Task 4 / `_task4_adjacency/build_mughal_graph.py` |
| `surfaces/history-surface/6.mughal/adjacency.json` | Intermediate adjacency edges | Task 4 |
| `surfaces/history-surface/6.mughal/narrative.md` | Synthesis-mode prose chapter | Pre-existing |
| `surfaces/history-surface/6.mughal/panels/{story_id}/manifest.json` | Ordered panel list per story | **Production task (new)** |
| `surfaces/history-surface/6.mughal/panels/{story_id}/panel_NNN.png` | Panel images | **Production task (new)** |
| `game/static/data/timeline/mughal/mughal_graph.json` | PWA-served copy of era graph | **Production wiring (new)** |
| `game/static/data/timeline/mughal/panels/...` | PWA-served panel images | **Production wiring (new)** |

---

## 4. Mughal Go-Ahead Checklist

These are the concrete blockers to starting Mughal panel production. Each is small.

### 4.1 Graph re-emission (D2)
- [ ] Edit `_task2_mughal_bundles/build_bundles.py` to replace PYQ-desc anchor sort with panel-flow priority sort (key in §1 D2)
- [ ] Add support for per-story `anchor_render_order_override` field in the bundle source spec (only used if a story explicitly overrides)
- [ ] Re-run `build_bundles.py` → updated `HISTORY_SPRINT_MUGHAL_BUNDLES.json`
- [ ] Re-run `_task4_adjacency/build_mughal_graph.py` → updated `mughal_graph.json`
- [ ] Verify all 8 schema invariants still hold (script does this; just confirm)

### 4.2 Task 5 design revisions (D4 / D5 / D6)
- [ ] Strike `#timeline/{eraId}/narrative` and `#timeline/{eraId}/stories` sub-routes from Task 5 §1 (D4)
- [ ] Update Task 5 §1 back-button rule to "back returns to parent view" (D5)
- [ ] Delete Task 5 §6 "Summon Hosts Mechanism" entirely (D6)
- [ ] Narrow Task 5 §3.4 / §5 audio-trigger semantics to *playback-only* (D6)
- [ ] Update Task 5 §3.4 to add `story_kind === 'parallel_meta'` carousel branch (D3)

### 4.3 First production loop (s01 Panipat 1526 as smoke test)
- [ ] Create `6.mughal/panels/s01_panipat_1526/manifest.json` with planned panel sequence (~7 panels: 1 exterior establishing of plain, 1 wide battlefield, 3 anchor close-ups for Babur / Battle / Mughal Empire, 2 connective panels for Khanwa / Chanderi)
- [ ] Generate panels via Gemini using Task 3 style brief + s01 scene_setting + anchors
- [ ] Compare panel coherence to s04 reference set (Task 3 panels A–F as baseline)
- [ ] Decide: production pace OK for full 19-story run, or compress?

### 4.4 PWA Phase 1 (data wiring)
- [ ] Copy `mughal_graph.json` → `game/static/data/timeline/mughal/mughal_graph.json`
- [ ] Implement `STATE.eraGraphs` loader (Task 5 §2)
- [ ] Implement `renderEraHome` tab container (Task 5 §3.1)
- [ ] Implement narrative-pane markdown render (Task 5 §3.2)
- [ ] Implement stories-gallery render (Task 5 §3.3)
- [ ] Smoke-test with empty panel images (placeholders) — verify nav works before panels exist

### 4.5 PWA Phase 2 (comic viewer)
- [ ] Implement `renderComicViewer` for `story_kind: embodied` (Task 5 §3.4)
- [ ] Implement parallel_meta carousel variant (D3)
- [ ] Wire adjacency links (23 unique edges)
- [ ] CSS branching for visual_budget / concept_as_anchor / mention_shape (Task 5 §4)
- [ ] Wire panel images from `panels/{story_id}/` once generated

---

## 5. Out of Scope (Deferred)

These remain open but **do not block Mughal production**.

- **Audio production** — all of it. Stage audios, concept audios, person-anchor-audio decision. Per architecture §7: visual layer first, audio last.
- **Audio playback wiring in PWA** — buttons hidden until files exist. Schema field `audio_slot_id` stays null on every AnchorPanel and Stage during Mughal visual production.
- **PYQ-count reconciliation** — 12 entities where era-JSON's hand-curated `pyq_count` disagrees with Task 1's regex count. Tagged `narrative`; no production impact. Reconcile post-pilot.
- **Person-anchor audio decision** — schema accommodates the slot type (`person_anchor_audio`); decision whether to populate it deferred per architecture §7.
- **Eras 2–11 (non-Mughal) graph emission** — `{era}_graph.json` for the other 10 eras. After Mughal pilot validates pipeline, extend `build_*_graph.py` to consume bundle-MD for each remaining era. Estimate: 10 sessions × 1 each.
- **Coverage extension to SQLite log** — per memory note `project_sqlite_coverage_extension`, defer until history-tab sprint completes.

---

## 6. Re-Runnability (which script produces what)

```
_task1_pyq_weights.py
    Input:   raw/pyq/*.json + surfaces/history-surface/{era}/*.json
    Output:  HISTORY_SPRINT_PYQ_WEIGHTS.{md,json}
    Re-run:  When PYQ pool changes or label-normalization rules change

_task2_mughal_bundles/build_bundles.py   [TO BE UPDATED PER D2]
    Input:   PYQ_WEIGHTS.json + bundle source spec (hand-defined 19 stories)
    Output:  HISTORY_SPRINT_MUGHAL_BUNDLES.{md,json}
    Re-run:  After D2 sort change. Asserts coverage invariants.

_task4_adjacency/build_adjacency.py
    Input:   MUGHAL_BUNDLES.json
    Output:  6.mughal/adjacency.json
    Re-run:  When bundles change.

_task4_adjacency/build_mughal_graph.py
    Input:   MUGHAL_BUNDLES.json + adjacency.json + mughal.json + narrative.md path + PYQ_WEIGHTS.json
    Output:  6.mughal/mughal_graph.json
    Re-run:  After D2 re-run. Asserts all 8 schema invariants.
```

Production-side scripts (TBD, new):

```
_production/build_panel_manifest.py
    Input:   mughal_graph.json + Task 3 style brief
    Output:  6.mughal/panels/{story_id}/manifest.json (per story)
    Re-run:  Per story, or all stories.

_production/generate_panels.py
    Input:   manifest.json + Gemini API
    Output:  panel_NNN.png files
    Re-run:  Per panel, or per story.
```

These two production-side scripts are designed-but-unbuilt. Building them is part of §4.3.

---

## 7. Convergence Outcome

The five pre-production tasks are mutually consistent post-decisions D1–D5. The schema (Task 4) holds without modification. The PWA spec (Task 5) needs three small revisions (D4, D5, D6) which are listed in §4.2.

The two real action items before image generation can start are:
1. Re-run `build_bundles.py` + `build_mughal_graph.py` with the D2 sort change
2. Build the two new production scripts in §6 (`build_panel_manifest.py`, `generate_panels.py`)

Both are small. Mughal pilot production can begin in the next session.

---

## See Also

- `HISTORY_SPRINT_ARCHITECTURE.md` — design decisions and rationale
- `HISTORY_SPRINT_ASSET_PLAN.md` — peripheral asset classification (now superseded in part by D1's anchor budget)
- Memory: `project_history_sprint_tasks` — task index, picked up across sessions
- Memory: `project_history_tab_sprint` — sprint framing and deadline
