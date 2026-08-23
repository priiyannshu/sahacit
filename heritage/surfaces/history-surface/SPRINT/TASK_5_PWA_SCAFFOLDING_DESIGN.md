# Task 5 — PWA Scaffolding Design (Sketch)

**Status:** Sketch (pre-convergence). Implementation deferred until convergence session completes.  
**Date:** 2026-05-16  
**Depends on:** Task 4 (Schema spec + Mughal instance complete)

---

## Overview

Define UI components and data-flow contracts so that asset production (visual panels, audio slots) fills pre-built containers.

**Design principle:** Schema → render. AnchorPanel.visual_budget, mention_shape enum, story_kind flags all drive layout branching. No decisions are made in isolation; all tie to Task 4 schema invariants.

---

## 1. Navigation Architecture

### Current state
- `#timeline` → era carousel (all 11 eras as swipeable cards)
- `#timeline/{eraId}` → per-era stages list + stage-node expansion

### Proposed structure (Phase 1: routes)

```
#timeline                              — Era carousel (unchanged)
├─ #timeline/{eraId}                   — Era home: tab container (Narrative / Stories / Timeline)
└─ #timeline/{eraId}/story/{storyId}  — Comic viewer + anchor panels (NEW)
```

Tabs (Narrative / Stories / Timeline) are JS-switched within the era home route; no separate URLs. Sub-routes `/narrative` and `/stories` are not used. *(D4)*

**Navigation rules:**
- Carousel → click era card → `#timeline/{eraId}` (defaults to **Narrative tab**)
- Narrative tab → CTA button "Explore N Short Stories" → switches to Stories tab (same route)
- Stories tab → click story card → `#timeline/{eraId}/story/{storyId}`
- Comic viewer → adjacency edge → `#timeline/{eraId}/story/{relatedStoryId}`
- Back returns to parent view: comic viewer → Stories tab of era home; era home → carousel. *(D5)*
- Tab bar hides inside era views; reappears on carousel

**Alternate path:**
- Users can flip from narrative/stories to **Timeline tab** (existing stage-detail view) if they prefer chronological/stage-level granularity

---

## 2. Data-Loading & State Contract

### Phase 1: Data wiring

**On era entry** (`#timeline/{eraId}`):

```javascript
// Load era graph (ONE call per era, cached in STATE)
fetch(`/data/timeline/{eraId}/{eraId}_graph.json`)
  .then(r => r.json())
  .then(graph => {
    STATE.eraGraphs[eraId] = graph;
    // graph contains:
    // - era: { era_id, label, temporal_span, narrative_chapter_path, stage_ids, story_ids }
    // - narrative_chapter: { title, file_path }
    // - stories: [ { story_id, title, scene_setting, anchors[], fly_bys[], adjacencies[] }, ... ]
    // - stages: [ { stage_id, label, start, end, track, color, audio_slot_id }, ... ]
    // - audio_slots: [ { slot_id, slot_type, stage_id, story_id, node_id, trigger_note }, ... ]
    // - entity_index: { node_id → { entity_type, label, home_story_id, pyq_count, pyq_ids, ... } }
    renderEraHome(eraId, graph);
  });
```

**STATE shape (per session):**
```javascript
STATE.eraGraphs = {
  'mughal': { ...graph... },
  // other eras loaded on demand
};
STATE.currentEra = 'mughal';
STATE.currentTab = 'narrative'; // or 'stories' or 'timeline'
STATE.currentStory = null; // set when viewing #timeline/{eraId}/story/{storyId}
```

---

## 3. Component Skeleton

### 3.1 Era Home (Tab container)

**Purpose:** Display narrative chapter (default) + tab switcher to stories/timeline

```html
<div class="era-home">
  <div class="era-header">
    <a href="#timeline" class="era-back-btn">← Eras</a>
    <h1>${era.label}</h1>
    <div class="era-temporal">${era.temporal_span}</div>
  </div>

  <div class="era-tabs">
    <button class="era-tab narrative-tab active" data-tab="narrative">Narrative</button>
    <button class="era-tab stories-tab" data-tab="stories">Stories (N)</button>
    <button class="era-tab timeline-tab" data-tab="timeline">Timeline</button>
  </div>

  <div class="era-tab-content">
    <div id="narrative-pane" class="era-pane active">
      <!-- Narrative chapter prose + story gallery CTA -->
    </div>
    <div id="stories-pane" class="era-pane">
      <!-- Story gallery (carousel or grid) -->
    </div>
    <div id="timeline-pane" class="era-pane">
      <!-- Existing stage list (reused from renderTimelineEra) -->
    </div>
  </div>
</div>
```

**Contracts:**
- Default tab = narrative (synthesis first)
- Story count badge on stories-tab button (e.g., "Stories (19)")
- Tab switching is instant (data already loaded)
- Back button returns to carousel

---

### 3.2 Narrative Chapter Pane

**Purpose:** Prose synthesis + story gallery preview

**Content:**
1. Chapter prose (markdown → HTML) from `narrative_chapter.file_path`
2. CTA card: "Dive into 19 short stories" (button to stories-tab)

**Markup:**
```html
<div class="narrative-pane">
  <div class="narrative-content">
    ${renderMarkdown(narrativeChapter.content)}
  </div>
  <div class="narrative-cta">
    <button onclick="switchTab('stories')">
      Explore ${storyCount} Short Stories →
    </button>
  </div>
</div>
```

**Notes:**
- Markdown is fetched once at graph-load time (or embedded in the JSON)
- No interactive elements in prose layer (read-only narrative)

---

### 3.3 Story Gallery Pane

**Purpose:** Browse all short stories for the era

**Visual layout:**
- **Mughal case:** 19 short stories in a vertical scroll or carousel
- Story cards show:
  - Story title (e.g., "Ibadat Khana, 1578")
  - Scene setting: place + year (e.g., "Fatehpur Sikri, 1578")
  - Moment description (e.g., "Akbar's Thursday night discussions")
  - Anchor count badge + visual-budget indicators (e.g., "7 anchors: ◆◆◆◇◇")
  - Story kind icon (embodied ⚪ vs. parallel_meta ⬚)
  - Flyover: show first 2–3 anchor names (preview)

**Markup skeleton:**
```html
<div class="stories-pane">
  <div class="stories-gallery">
    ${stories.map(story => `
      <div class="story-card" onclick="navigateToStory('${story.story_id}')">
        <h3>${escapeHtml(story.title)}</h3>
        <div class="scene-setting">
          <span class="place">${story.scene_setting.place}</span>
          <span class="year">${story.scene_setting.year} CE</span>
        </div>
        <div class="moment">${story.scene_setting.moment}</div>
        
        <div class="anchor-summary">
          ${story.anchors.map(a => `
            <span class="anchor-badge" 
                  title="${a.label}"
                  data-budget="${a.visual_budget}"
                  data-concept="${a.concept_as_anchor}">
              ◆
            </span>
          `).join('')}
        </div>
        
        <div class="story-kind-indicator" data-kind="${story.story_kind}">
          ${story.story_kind === 'parallel_meta' ? '(parallel: 6 courts)' : ''}
        </div>
      </div>
    `).join('')}
  </div>
</div>
```

**CSS branching:**
- `.anchor-badge[data-budget="light"]` → lighter fill (pyq_suggestive)
- `.anchor-badge[data-concept="true"]` → highlighted/outlined (abstract entity)
- `.story-kind-indicator[data-kind="parallel_meta"]` → special styling (no single embodied moment)

---

### 3.4 Comic Viewer (Story Detail)

**Purpose:** Display one short story with anchor panels + fly-by context

**Route:** `#timeline/{eraId}/story/{storyId}`

**Structure:**
```html
<div class="comic-viewer">
  <!-- Header -->
  <div class="comic-header">
    <a href="#timeline/${eraId}/stories" class="comic-back-btn">← Stories</a>
    <h2>${story.title}</h2>
    <div class="scene-setting">
      ${story.scene_setting.place} · ${story.scene_setting.year} CE
      <span class="moment-desc">${story.scene_setting.moment}</span>
    </div>
  </div>

  <!-- Synopsis (narrative voice, not comic voice) -->
  <div class="comic-synopsis">
    ${story.synopsis}
  </div>

  <!-- Story kind badge -->
  ${story.story_kind === 'parallel_meta' ? `
    <div class="parallel-meta-note">
      ⬚ Parallel narrative: 6 contemporaneous courts (c.1580)
    </div>
  ` : ''}

  <!-- Anchor panels (ordered by render intent) -->
  <div class="anchor-panels">
    ${story.anchors.map((anchor, idx) => `
      <div class="anchor-panel"
           data-anchor-id="${anchor.anchor_id}"
           data-budget="${anchor.visual_budget}"
           data-concept="${anchor.concept_as_anchor}"
           data-source="${anchor.source}">
        
        <!-- Panel header -->
        <div class="anchor-header">
          <h3>${anchor.label}</h3>
          <div class="anchor-meta">
            <span class="entity-type">${anchor.entity_type}</span>
            ${anchor.pyq_count > 0 ? `
              <span class="pyq-badge" title="appears in ${anchor.pyq_count} PYQs">
                📋 ${anchor.pyq_count}
              </span>
            ` : ''}
            <span class="source-label" data-source="${anchor.source}">
              ${anchor.source === 'pyq' ? 'PYQ-tested' : 
                anchor.source === 'pyq_suggestive' ? 'PYQ-suggestive' : 
                'Narrative'}
            </span>
          </div>
        </div>

        <!-- Visual content goes here (asset production fills) -->
        <div class="anchor-visual">
          <!-- Image/illustration (notional for now) -->
          <div class="visual-placeholder" style="background:#e8e8e8;">
            [${anchor.visual_budget.toUpperCase()} visual budget]
            <br/>Entity: ${anchor.label}
          </div>
        </div>

        <!-- Audio playback (concept_audio or person_anchor_audio) — D6 -->
        <!-- Render only when audio_slot_id is non-null AND the audio file exists on disk. -->
        <!-- No generation UI of any kind. trigger_note is offline metadata, never shown. -->
        ${anchor.audio_slot_id ? `
          <div class="anchor-audio">
            <button class="audio-trigger" data-slot-id="${anchor.audio_slot_id}">
              🎙️ Play audio
            </button>
          </div>
        ` : ''}

        <!-- PYQ links (if any) -->
        ${anchor.pyq_ids.length > 0 ? `
          <div class="pyq-links">
            <details>
              <summary>Questions (${anchor.pyq_ids.length})</summary>
              <ul>
                ${anchor.pyq_ids.map(pyqId => `
                  <li><a href="#study?pyq=${pyqId}">${pyqId}</a></li>
                `).join('')}
              </ul>
            </details>
          </div>
        ` : ''}
      </div>
    `).join('')}
  </div>

  <!-- Fly-by mentions -->
  <div class="fly-bys">
    <h4>In this scene:</h4>
    <div class="fly-by-list">
      ${story.fly_bys.map(fb => `
        <div class="fly-by-item" data-shape="${fb.mention_shape}">
          <span class="shape-icon">
            ${fb.mention_shape === 'cameo' ? '👤' :
              fb.mention_shape === 'background' ? '🏛️' :
              fb.mention_shape === 'caption' ? '📝' :
              fb.mention_shape === 'connective' ? '→' :
              fb.mention_shape === 'timeline-only' ? '📅' : '•'}
          </span>
          <span class="fly-by-label">${fb.label}</span>
          <span class="entity-type muted">${fb.entity_type}</span>
        </div>
      `).join('')}
    </div>
  </div>

  <!-- Adjacency navigation -->
  ${story.adjacencies.length > 0 ? `
    <div class="adjacencies">
      <h4>Connected stories:</h4>
      <div class="adjacency-list">
        ${story.adjacencies.map(adj => {
          const adjStory = allStories.find(s => s.story_id === adj.story_id);
          return `
            <div class="adjacency-card" data-type="${adj.adjacency_type}">
              <div class="adj-label">
                <strong>${escapeHtml(adjStory.title)}</strong>
                <span class="adj-type">(${adj.adjacency_type})</span>
              </div>
              <div class="adj-note">${adj.note}</div>
              <button onclick="navigateToStory('${adj.story_id}')">
                Read story →
              </button>
            </div>
          `;
        }).join('')}
      </div>
    </div>
  ` : ''}

  <!-- Stage audio (TBD scope) -->
  ${story.stage_ids.length > 0 ? `
    <div class="stage-audios">
      <h4>Timeline context:</h4>
      ${story.stage_ids.map(stageId => {
        const stage = allStages.find(s => s.stage_id === stageId);
        return `
          <div class="stage-audio-item">
            <strong>${stage.label}</strong>
            ${stage.audio_slot_id ? `
              <button class="audio-trigger" data-slot-id="${stage.audio_slot_id}">
                🎙️ Stage audio
              </button>
            ` : ''}
          </div>
        `;
      }).join('')}
    </div>
  ` : ''}
</div>
```

**CSS branching:**
- `.anchor-panel[data-budget="light"]` → reduced visual real estate (pyq_suggestive source)
- `.anchor-panel[data-budget="full"]` → full-focus panel (pyq or narrative source)
- `.anchor-panel[data-concept="true"]` → special styling (abstract entity, concept-as-anchor)
- `.fly-by-item[data-shape="cameo"]` → person icon + lighter treatment
- `.fly-by-item[data-shape="timeline-only"]` → grayed out (no visual in comic)
- `.adjacency-card[data-type="causal"]` → arrow icon (A → B)
- `.adjacency-card[data-type="shared_entity"]` → entity icon (crosslink)
- `.adjacency-card[data-type="parallel"]` → parallel icon (contemporaneous)

#### 3.4a Parallel-meta carousel variant (D3)

When `story.story_kind === 'parallel_meta'` (s19 Six Courts only), the comic viewer switches from the sequential anchor-panel stream to a **swipeable carousel of 6 sub-scenes**, one per civilization track:

1. Mughal (India) — Akbar's Fatehpur Sikri
2. Ottoman — Murad III's Istanbul
3. Safavid — Abbas I's Isfahan
4. Ming → Qing transition — Beijing
5. Tudor / Elizabethan — London
6. Counter-Reformation Europe — Rome / Jesuit network

Per sub-scene budget: 1 establishing panel + 1 anchor panel (light visual budget — parallel-meta is meta, not embodied). Dot-indicator pagination. No separate route; same `#timeline/{eraId}/story/s19_six_courts_parallel` URL.

The two existing s19 anchors (`hist_jesuits`, `hist_proto_industrialisation`) anchor in the Counter-Reformation and pan-Eurasian sub-scenes respectively. Other sub-scenes show establishing panels only.

---

## 4. Schema-to-Render Contracts

### 4.1 AnchorPanel rendering

| Schema field | CSS class | Effect |
|---|---|---|
| `visual_budget: "full"` | `.anchor-panel[data-budget="full"]` | Full visual real estate (primary panel) |
| `visual_budget: "light"` | `.anchor-panel[data-budget="light"]` | Reduced treatment (pyq_suggestive) |
| `concept_as_anchor: true` | `.anchor-panel[data-concept="true"]` | Stronger visual: bordered, highlighted, concept-diagram background |
| `concept_as_anchor: false` | `.anchor-panel[data-concept="false"]` | Standard panel (person/place/event) |
| `source: "pyq"` | `.anchor-panel[data-source="pyq"]` | PYQ-tested badge + style |
| `source: "pyq_suggestive"` | `.anchor-panel[data-source="pyq_suggestive"]` | Lighter badge + style |
| `source: "narrative"` | `.anchor-panel[data-source="narrative"]` | Narrative-earned badge |
| `audio_slot_id: "as_concept_s04_sulh_i_kul"` | `.anchor-audio` → button enabled | Audio trigger button visible |
| `audio_slot_id: null` | `.anchor-audio` → button hidden | Audio slot reserved; filled in post-production |

### 4.2 FlyBy mention shapes

| `mention_shape` | Icon | Treatment | Visibility |
|---|---|---|---|
| `cameo` | 👤 | High — person visible in scene composition | Full visibility in fly-by list |
| `background` | 🏛️ | Medium — place/institution visible as landmark | Full visibility |
| `caption` | 📝 | Low — concept noted in caption/label | Collapsed by default; expand on click |
| `connective` | → | Cheap — event noted as text card between panels | Collapsed by default |
| `timeline-only` | 📅 | None — period nodes, timeline-exclusive | Grayed out / optional expand |

### 4.3 Story kind

| `story_kind` | Rendering |
|---|---|
| `embodied` | Standard single-scene layout; timeline-stage mapping 1:N |
| `parallel_meta` | Split-screen container (6 courts, etc.); special note above anchors |

### 4.4 Adjacency types

| `adjacency_type` | Icon/Label | Audio implication |
|---|---|---|
| `shared_entity` | 🔗 | "Did you notice [entity] also appeared in [story]?" |
| `causal` | → | "This [event] led directly to [next story]" |
| `parallel` | ≈ | "While this was happening, in [parallel context]…" |

---

## 5. Audio Slot Scaffolding (D6)

**Purpose:** Playback containers for audio files that already exist on disk. No generation UI of any kind.

**Semantics (D6):**
- Render audio button only when `audio_slot_id` is non-null AND the corresponding audio file exists at `/static/audio/{slot_id}.mp3` (or equivalent path).
- Button is hidden (not "coming soon") when no file exists.
- `trigger_note` in the schema is offline-workflow metadata — used manually when generating audio via NotebookLM. It is never surfaced in the PWA.

```html
<!-- Audio playback button — only rendered when file exists -->
<button class="audio-trigger"
        data-slot-type="concept_audio"
        data-slot-id="as_concept_s04_sulh_i_kul"
        data-src="/static/audio/as_concept_s04_sulh_i_kul.mp3">
  Play audio
</button>
```

---

## 6. Implementation Checklist

### Phase 1: Data wiring
- [ ] Add `STATE.eraGraphs = {}` and `STATE.currentEra`, `STATE.currentTab`, `STATE.currentStory`
- [ ] Implement era-graph loader: `fetch(/data/timeline/{eraId}/{eraId}_graph.json)`
- [ ] Parse graph JSON; validate against schema invariants (runtime checks)

### Phase 2: Navigation + component stubs
- [ ] Add routes: `#timeline/{eraId}`, `#timeline/{eraId}/narrative`, `#timeline/{eraId}/stories`, `#timeline/{eraId}/story/{storyId}`
- [ ] Implement `renderEraHome(eraId, graph)` with tab container
- [ ] Implement `renderNarrativePane(narrative_chapter)` (fetch + render markdown)
- [ ] Implement `renderStoriesGallery(stories)` with story cards
- [ ] Implement `renderComicViewer(story, allStories, allStages)` with anchor panels + fly-bys + adjacencies
- [ ] Reuse existing timeline-detail view as `#timeline/{eraId}` timeline tab

### Phase 3: Schema-to-render contracts
- [ ] CSS classes for `visual_budget`, `concept_as_anchor`, `source`, `mention_shape`, `adjacency_type`, `story_kind`
- [ ] Render conditional visibility: `.fly-by-item[data-shape="timeline-only"]` hidden/grayed; concept-audio only if `audio_slot_id` present
- [ ] Anchor panel layout: full vs. light budget branching
- [ ] Audio-trigger button scaffolding (metadata only, no player until production)

### Phase 4: Testing & refinement
- [ ] Load Mughal era graph; navigate carousel → narrative → stories → comic viewer
- [ ] Verify all 19 stories render without breaks
- [ ] Check adjacency links (23 edges in Mughal instance)
- [ ] Inspect story-kind rendering (s19 is `parallel_meta`; visual distinction evident)
- [ ] Confirm PYQ link routing to study tab (if available)

---

## 8. Convergence Session Alignment

**Task 5 sketch will be reviewed alongside:**
- Task 1 (PYQ weights → anchor thresholds)
- Task 2 (Mughal bundles → story layout expectations)
- Task 3 (Style brief → visual-budget CSS guidance)
- Task 4 (Schema + Mughal instance → data contracts)

**Potential conflicts to resolve:**
- Schema gap: Does narrative_chapter content get embedded in graph JSON or fetched separately? (Proposed: separate fetch, cite path in graph)
- Audio scope: Are `stage_audio` and `person_anchor_audio` slots reserved but deferred? (Proposed: yes, both registered; only `concept_audio` produced first)
- Parallel-meta rendering: Does s19 (Six Courts) get a true split-screen or a carousel of 6 sub-scenes? (TBD visual budget after Task 3 reference panels confirm feasibility)

---

## 9. Notes for Future Sessions

- **All three surface tabs (narrative/stories/timeline)** share the same data load. No redundant fetches.
- **Back navigation:** Always returns to carousel, not to previous tab (simpler UX).
- **Anchor-panel order matters:** Task 2 bundling defines render order; implementation must respect `anchors` array order in JSON.
- **Audio is async:** Slot metadata lives in schema; actual audio production (NotebookLM) happens post-scaffolding, post-visual-production.
- **Markup extensibility:** All `data-*` attributes are future-facing; CSS can branch on them without code changes.

---

## 10. Design Decisions (Resolved)

All three pre-convergence inconsistencies resolved in `HISTORY_SPRINT_PIPELINE_LOCK.md` §1 (D3–D6). Recorded here for reference.

### 10.1 Navigation route ambiguity — RESOLVED (D4)

**Decision:** Single-route tab model. `#timeline/{eraId}` is the era home with JS tab switcher; `/narrative` and `/stories` sub-routes removed. See §1 of this doc.

*Reference: HISTORY_SPRINT_PIPELINE_LOCK.md §1 D4*

### 10.2 Back button navigation inconsistency — RESOLVED (D5)

**Decision:** Breadcrumb navigation. Back from comic viewer → Stories tab of era home. Back from era home → carousel. See §1 of this doc.

*Reference: HISTORY_SPRINT_PIPELINE_LOCK.md §1 D5*

### 10.3 "Summon hosts" mechanism scope — RESOLVED (D6, removed from scope)

**Decision:** No summon-hosts UI of any kind. Audio buttons in the comic viewer are playback-only, hidden when no file exists. `trigger_note` stays in schema as offline metadata. See §5 of this doc.

*Reference: HISTORY_SPRINT_PIPELINE_LOCK.md §1 D6*
