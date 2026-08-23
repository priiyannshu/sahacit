# History Sprint — Graph Schema Specification

**Task:** Task 4 of the history sprint pre-production sequence  
**Date:** 2026-05-16  
**Status:** v1 (pilot: Mughal era)  
**Companion instance:** `surfaces/history-surface/6.mughal/mughal_graph.json`  
**Architecture reference:** `surfaces/HISTORY_SPRINT_ARCHITECTURE.md`

This schema formalises the data structure that visual production emits. It has two consumers:
- **PWA renderer** — drives era carousel → story gallery → comic reader navigation
- **Audio continuity** — adjacency edges let NotebookLM hosts cross-reference across stories ("did you catch the glimpse of him in that earlier court scene?")

---

## 1. Enumerations

### `entity_type`
The type of a historical entity node.

| Value | Meaning |
|---|---|
| `person` | Historical individual |
| `place` | Location (city, fort, region, river, port) |
| `institution` | Organised structure (court office, army system, religious order, legal body) |
| `event` | Discrete happening (battle, assassination, treaty, promulgation) |
| `movement` | Sustained collective or ideological arc (Bhakti, Counter-Reformation) |
| `reform` | A specific administrative or social change (zabt, abolition of sati) |
| `concept` | Abstract idea, cultural form, or material object used as a node (sulh-i-kul, Mughal painting, Guru Granth Sahib) |
| `empire` | A polity or state entity (Mughal Empire, Maratha Empire, Hyderabad State) |
| `period` | A timeline-stage construct (`period_*` nodes — exclusively `timeline-only` mention shape; never anchor candidates) |

### `mention_shape`
How a fly-by entity is encoded in a short story's visual stream.

| Value | Cost | When to use |
|---|---|---|
| `cameo` | High | Person visible in the scene composition (face in crowd, court, battlefield) |
| `background` | Medium | Place or institution visible as a landmark or setting element |
| `caption` | Low | Concept noted in a caption, label, or brief textual call-out within a panel |
| `connective` | Cheap | Event or movement noted as a text card between panels ("Meanwhile, at Golconda…") |
| `timeline-only` | None | `period_*` stage-construct nodes; present in story fly-by lists for completeness but have no visual representation in the story — they live exclusively on the timeline |

### `anchor_source`
How an entity earned its anchor panel.

| Value | Meaning |
|---|---|
| `pyq` | PYQ-frequency evidence meets the era threshold (authoritative) |
| `pyq_suggestive` | PYQ evidence exists but only via list-question matching — lighter visual budget warranted |
| `narrative` | No PYQ evidence at the era threshold; anchor justified by narrative salience |

### `visual_budget`
Rendering weight of an anchor panel. Derived from `anchor_source`.

| Value | Derived from | Effect |
|---|---|---|
| `full` | `pyq` or `narrative` | Full-focus panel — primary visual real estate in story |
| `light` | `pyq_suggestive` | Reduced treatment — a focused but not dominant panel |

### `story_kind`
Container convention for a short story.

| Value | Meaning |
|---|---|
| `embodied` | Single witnessed scene, one time+place. Standard form. |
| `parallel_meta` | Split-screen of contemporaneous contexts (e.g., six Eurasian courts c.1580). No single embodied moment. Needs distinct PWA rendering. |

### `audio_slot_type`
Type of audio peripheral.

| Value | Attached to | Hosts discuss |
|---|---|---|
| `stage_audio` | Stage (timeline) | What happened across the stage's full arc — synthesis at timeline resolution |
| `concept_audio` | AnchorPanel (concept-as-anchor) | The abstract concept materialised in that panel — its meaning, connections |
| `person_anchor_audio` | AnchorPanel (person, TBD) | Biographical sketch, PYQ angles — deferred decision; schema registers the slot |

### `adjacency_type`
Reason two short stories are adjacent (i.e., can cross-reference in audio).

| Value | Meaning |
|---|---|
| `shared_entity` | An entity appears in both stories (anchor in one, fly-by in another — or fly-by in both) |
| `causal` | Story A's events directly enable or cause Story B's events |
| `parallel` | Stories occupy the same or overlapping timeframe in different geographic/political contexts |

---

## 2. Entity Types

### 2.1 Era

Top-level container for all surfaces pertaining to one of the 11 chronological eras.

| Field | Type | Notes |
|---|---|---|
| `era_id` | string | Slug, e.g., `"mughal"` |
| `label` | string | Human label, e.g., `"Mughal Empire + Deccan + Eurasian Parallels"` |
| `era_number` | int | 1–11, chronological order |
| `temporal_span` | string | e.g., `"1526 CE – 1757 CE"` |
| `narrative_chapter_path` | string | Relative path to `narrative.md` |
| `stage_ids` | string[] | Ordered list of stage IDs within this era |
| `story_ids` | string[] | Ordered list of short-story IDs |

### 2.2 Stage

A timeline segment within an era. Stages are the fine-grained timeline units; they merge into short stories at the comic layer.

| Field | Type | Notes |
|---|---|---|
| `stage_id` | string | Slug, e.g., `"babur_humayun"` |
| `era_id` | string | Parent era |
| `label` | string | Display label |
| `start` | int | Year CE |
| `end` | int | Year CE |
| `track` | string | `"india"` \| `"parallel_europe"` \| `"parallel_islamic_west"` \| `"parallel_east_asia"` |
| `color` | string | Hex color for timeline rendering |
| `audio_slot_id` | string \| null | FK to AudioSlot; null until audio production |

### 2.3 NarrativeChapter

The synthesis-mode prose chapter for an era. Exists as a Markdown file; schema records metadata.

| Field | Type | Notes |
|---|---|---|
| `era_id` | string | |
| `file_path` | string | Relative path to the `.md` file |
| `title` | string | Chapter title from first `#` heading |

### 2.4 ShortStory

A short story = one embodied episode (or one parallel-meta container). The central production unit.

| Field | Type | Notes |
|---|---|---|
| `story_id` | string | Slug, e.g., `"s04_ibadat_khana_1578"` |
| `era_id` | string | |
| `title` | string | |
| `story_kind` | `story_kind` enum | `"embodied"` or `"parallel_meta"` |
| `scene_setting` | object | `{place: string, year: int, moment: string}` |
| `stage_ids` | string[] | Which stages this story bundles |
| `synopsis` | string | One-paragraph summary (narrative chapter voice, not comic voice) |
| `anchors` | AnchorPanel[] | Ordered array; render order is production intent |
| `fly_bys` | FlyBy[] | All fly-by entities; unordered |
| `adjacencies` | Adjacency[] | Cross-story edges; see §3.6 |

### 2.5 HistoricalEntity (base)

All era-graph nodes share this base structure. Subtypes are `person`, `place`, `institution`, `event`, `movement`, `reform`, `concept`, `empire`, `period`.

| Field | Type | Notes |
|---|---|---|
| `node_id` | string | e.g., `"hist_akbar"` |
| `entity_type` | `entity_type` enum | |
| `label` | string | Display name |
| `era_id` | string | The era this node belongs to |
| `home_story_id` | string \| null | FK to ShortStory where this entity's anchor panel lives. `null` for `period` type nodes (timeline-only). |
| `aliases` | string[] | Canonical node absorbs alias IDs (e.g., `"hist_mansabdari_system"` → canonical `"hist_mansab_system"`) |
| `pyq_count` | int | From Task 1 authoritative weights JSON |
| `pyq_ids` | int[] | PYQ IDs that test this entity |

### 2.6 AnchorPanel

An entity's full-focus panel within a short story. Nested inside ShortStory.anchors. Has its own ID for audio cross-referencing.

| Field | Type | Notes |
|---|---|---|
| `anchor_id` | string | e.g., `"ap_s04_hist_akbar"` (pattern: `ap_{story_id}_{node_id}`) |
| `node_id` | string | FK to HistoricalEntity |
| `label` | string | Display name (denormalised for rendering) |
| `entity_type` | `entity_type` enum | |
| `source` | `anchor_source` enum | |
| `pyq_count` | int | 0 for narrative-source anchors |
| `pyq_ids` | int[] | |
| `visual_budget` | `visual_budget` enum | Derived: `pyq_suggestive` → `light`, others → `full` |
| `concept_as_anchor` | boolean | `true` when the entity is abstract (concept/institution as object/practice) materialised in the scene, not a person/place physically present. Signals stronger visual treatment than a caption-only concept mention. |
| `audio_slot_id` | string \| null | FK to AudioSlot if a concept_audio or person_anchor_audio is attached |

### 2.7 FlyBy

A fly-by mention of an entity in a short story. Nested inside ShortStory.fly_bys.

| Field | Type | Notes |
|---|---|---|
| `node_id` | string | FK to HistoricalEntity |
| `label` | string | |
| `entity_type` | `entity_type` enum | |
| `mention_shape` | `mention_shape` enum | |

### 2.8 AudioSlot

Metadata for an audio peripheral. Visual production emits the slot; user generates the audio via NotebookLM.

| Field | Type | Notes |
|---|---|---|
| `slot_id` | string | e.g., `"as_stage_babur_humayun"`, `"as_concept_s04_sulh_i_kul"` |
| `slot_type` | `audio_slot_type` enum | |
| `stage_id` | string \| null | Populated for `stage_audio` |
| `story_id` | string \| null | Populated for `concept_audio` and `person_anchor_audio` |
| `node_id` | string \| null | The concept or person entity |
| `trigger_note` | string | Brief prompt for what hosts should discuss at this slot |

### 2.9 PYQ

A past-year question. Primarily a weighting input; schema records its test relationships.

| Field | Type | Notes |
|---|---|---|
| `pyq_id` | int | |
| `year` | int | |
| `subject_label` | string | UPSC subject label |
| `question_text` | string | Full question text |
| `entity_ids_tested` | string[] | FK array to HistoricalEntity.node_id |

---

## 3. Relationships

### 3.1 `contains`

| Source | Target | Cardinality |
|---|---|---|
| Era | Stage | 1:N |
| Era | NarrativeChapter | 1:1 |
| Era | ShortStory | 1:N |

Represented via `Era.stage_ids` and `Era.story_ids` arrays.

### 3.2 `bundles`

| Source | Target | Notes |
|---|---|---|
| ShortStory | Stage | Many-to-many; multiple stages per story, each stage in exactly one story per era |

Represented via `ShortStory.stage_ids`. Parallel stages (track ≠ `india`) may appear in multiple stories or only in the parallel_meta container.

### 3.3 `has-home-in`

| Source | Target | Cardinality | Invariant |
|---|---|---|---|
| HistoricalEntity | ShortStory | N:1 | Each non-period entity has **exactly one** home story |

Represented via `HistoricalEntity.home_story_id`. Period-type nodes have `home_story_id: null` — they are timeline-only.

### 3.4 `appears-in`

| Source | Target | Type attribute |
|---|---|---|
| HistoricalEntity | ShortStory | `"anchor"` \| `mention_shape` value |

An entity appears in its home story as `"anchor"` (via AnchorPanel) and in any other story as a fly-by typed by `mention_shape`. Both relationships are traversable via the entity→story reverse index (see §5).

### 3.5 `has-audio`

| Source | Target | Notes |
|---|---|---|
| Stage | AudioSlot | Via `Stage.audio_slot_id`; one slot per stage |
| AnchorPanel | AudioSlot | Via `AnchorPanel.audio_slot_id`; concept-as-anchor and (TBD) person-anchor panels |

### 3.6 `adjacent-to` (Adjacency)

Adjacency is a first-class edge on ShortStory. It is directional with a declared type; reciprocal edges must both be recorded.

```json
{
  "story_id": "s02_library_stairs_1556",
  "adjacency_type": "causal",
  "note": "Sher Shah's institutional legacy (rupiya, GT Road, zabt prototype) built during Humayun's exile is the direct substrate Akbar systematises in s03."
}
```

| Field | Type |
|---|---|
| `story_id` | string (FK to ShortStory) |
| `adjacency_type` | `adjacency_type` enum |
| `note` | string (one sentence — what the audio hosts can say) |

### 3.7 `tests`

| Source | Target |
|---|---|
| PYQ | HistoricalEntity (via `PYQ.entity_ids_tested`) |

Reverse: `HistoricalEntity.pyq_ids` holds the PYQ IDs.

---

## 4. Invariants

These must hold for any valid era graph instance.

1. **Exact-one anchor home:** Every node in the era graph (except `period` type) has `home_story_id` set to exactly one story in the same era. No node may have two anchor homes.

2. **Full coverage:** Every node in `{era}.json` appears in at least one short story — either as an anchor or as a fly-by. (`period_*` nodes appear as `timeline-only` fly-bys or are excluded from story fly-bys entirely but always live on the timeline.)

3. **Anchor exclusivity:** A node that has `home_story_id = X` appears in `story X` as an AnchorPanel, not as a FlyBy. It may appear in other stories as FlyBys.

4. **mention_shape matches entity_type:** Default mapping (architecture §3, extended):
   - `person` → `cameo`
   - `place` → `background`
   - `concept` / `reform` / `movement` → `caption`
   - `event` → `connective`
   - `institution` → `caption` (default; may be `background` if physically visible in scene)
   - `empire` → `caption`
   - `period` → `timeline-only`

5. **Adjacency reciprocity:** If story A lists story B in its `adjacencies`, story B must list story A in its `adjacencies` (possibly with a different `adjacency_type` — e.g., A→B is `causal`, B→A is `causal` with a different note, or `shared_entity`).

6. **visual_budget derived:** `visual_budget` is always deterministic from `anchor_source`: `pyq_suggestive` → `light`; all others → `full`. Never set independently.

7. **concept_as_anchor flag:** Must be `true` when the entity type is `concept`, `institution` (as an abstract system), or any entity playing the role of an idea or object in the scene rather than a physically present actor. Always `false` for `person` and `place` anchors.

8. **audio_slot_id null until production:** AudioSlot IDs in stages and anchor panels may be `null` until audio production begins. The schema defines the slot structure; production fills it.

---

## 5. JSON Representation

The graph is stored per-era as `surfaces/history-surface/{era}/{era}_graph.json`. It contains all entities for the era in a single document.

### Top-level structure

```json
{
  "schema_version": "1.0",
  "era": { ...Era object... },
  "stages": [ ...Stage objects... ],
  "narrative_chapter": { ...NarrativeChapter object... },
  "stories": [ ...ShortStory objects (with nested AnchorPanels + FlyBys + Adjacencies)... ],
  "audio_slots": [ ...AudioSlot objects (null until production)... ],
  "entity_index": {
    "hist_akbar": { ...HistoricalEntity... },
    ...
  }
}
```

### Entity reverse index

`entity_index` is a flat map from `node_id` → HistoricalEntity. HistoricalEntity records include `home_story_id`. From this, the audio layer builds:

```
entity → home story (anchor)
entity → [other stories] (fly-by appearances)
```

To build the reverse index, enumerate all AnchorPanels and FlyBys across all stories.

### Anchor panel ID convention

`anchor_id` = `"ap_{story_id}_{node_id}"`

Example: story `s04_ibadat_khana_1578`, entity `hist_akbar` → `"ap_s04_ibadat_khana_1578_hist_akbar"`

### Audio slot ID conventions

- Stage audio: `"as_stage_{stage_id}"`
- Concept audio: `"as_concept_{story_id}_{node_id}"`
- Person anchor audio (TBD): `"as_person_{story_id}_{node_id}"`

---

## 6. Mughal Pilot — Key Findings Incorporated

These Task 2 findings shaped schema decisions:

| Finding | Schema response |
|---|---|
| 5th mention shape `timeline-only` needed for `period_*` nodes | Added to `mention_shape` enum; period entities always use it |
| Story count overflow (19 > 10–15 target) | No schema change needed; count is a production finding, not a schema constraint |
| s19 (Six Courts) is a meta-scene, not embodied | `story_kind: "parallel_meta"` distinguishes it; Task 5 renders it differently |
| Concept-as-anchor cases need stronger visual treatment than captions | `concept_as_anchor: true` flag on AnchorPanel; signals Task 5 to not render as caption |
| Some institutions may warrant `background` not `caption` as fly-by | Invariant 4 allows `institution → background` override; default is `caption` |
| Era-JSON vs Task-1 pyq_count drift (~12 entities) | Schema uses Task 1 as authority (`HistoricalEntity.pyq_count` = Task 1 value); era-JSON drift is a known gap for future reconciliation |
| Adjacency edges absent from Task 2 output | Task 4 computes and adds them to the Mughal instance |
| Anchor budget (76) ≈ 2× implicit target | Narrative anchors carry `source: "narrative"` and may be downgraded to caption fly-bys during Task 3 if budget pressure; schema data supports this without re-bundling |

---

## 7. What Task 5 Consumes

The graph schema feeds Task 5 (PWA scaffolding) at these seams:

| Graph element | PWA component |
|---|---|
| Era list | Era carousel (11 slots) |
| Era → NarrativeChapter | Narrative reader tab per era |
| Era → stories (ordered) | Story gallery grid per era |
| ShortStory → anchors + fly_bys | Comic reader (sequential panels) |
| AnchorPanel.concept_as_anchor | Panel sub-renderer: concept panel vs. person panel |
| AnchorPanel.audio_slot_id | Embedded audio trigger in comic reader |
| Stage → audio_slot_id | Timeline stage audio trigger |
| ShortStory → adjacencies | "Related stories" surface + audio cross-reference metadata |
| story_kind: parallel_meta | Distinct layout (split-screen grid vs. sequential scroll) |

---

## See Also

- `surfaces/HISTORY_SPRINT_ARCHITECTURE.md` — cognitive mode model, three-tier coverage, fly-by conventions
- `surfaces/HISTORY_SPRINT_MUGHAL_BUNDLES.{json,md}` — Task 2 output (input to this schema)
- `surfaces/HISTORY_SPRINT_PYQ_WEIGHTS.json` — authoritative PYQ counts (Task 1)
- `surfaces/history-surface/6.mughal/mughal_graph.json` — Mughal era instance (Task 4 output)
