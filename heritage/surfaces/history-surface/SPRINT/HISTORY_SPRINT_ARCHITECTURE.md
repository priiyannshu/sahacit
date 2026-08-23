# History Sprint — Architecture & Design Decisions

**Brainstorm date:** 2026-05-16  
**Sprint deadline:** 2026-05-24 (home exam)  
**Scope:** History surface only. Geo / Eco / Polity remain narrative-only.

---

## 1. Cognitive Mode Model

Each layer of the history surface operates in a **different cognitive mode**, not a different level of detail:

| Layer | Mode | What it does | What it's bad at |
|---|---|---|---|
| Narrative chapter | **Synthesis** | Claims, causation, breadth via prose | Embodiment, recognition |
| Timeline | **Positioning** | When things happen relative to what | Felt experience, texture |
| Short stories (comics) | **Embodied episode** | Witnessed scenes; abstract claims collapsed into specific moments | Connective causation, breadth |
| Audio (2 NotebookLM hosts) | **Conversational riffing** | Pointing-at, wondering aloud, comparative gloss, easter-egg discovery | Rapid information transfer |

**Overlap policy:** Existing narrative chapters do some episodic description that short stories will now own. **Overlap accepted for now**; narrative-chapter re-edit (toward sharper synthesis-only role) deferred to *after* upper layers are built — a foundation-revisit pass.

---

## 2. Three-Tier Coverage Model

| Tier | Mechanism | Earned by | Status |
|---|---|---|---|
| **Tier 1** | Timeline position | Every node (universal) | ✅ Already done |
| **Tier 2** | Anchor panel in short story | PYQ frequency (TBD threshold) | To produce |
| **Tier 3** | Fly-by mention in visual stream | Contextual relevance to a story | To produce |

**Anchor rule:** Each entity has **exactly one anchor home** — the short story where its full-focus panel lives. Other appearances = fly-by mentions.

**Mention rule:** A fly-by mention should be *easy to fly past* on first read, but catchable on second pass. This creates the discovery loop that audio hosts mine ("did you notice him in the corner of that panel?").

---

## 3. Fly-By Mention Conventions

Mention shape assigned by entity type:

| Entity Type | Mention Shape | Cost | Notes |
|---|---|---|---|
| Person | Visual cameo | High (needs composition discipline) | Face in crowd / court / battle scene |
| Place | Background landmark | Medium | Building / map element in scene background |
| Concept | Caption-level mention | Low | Concepts already have audio anchors elsewhere |
| Event / Movement / Reform | Connective text card | Cheap | "Meanwhile, in Bengal…" between panels |

Every mention is still encoded as a graph edge from entity → short-story, **typed** as `cameo` / `background` / `caption` / `connective`. The audio layer reads the type and decides whether to riff on it.

---

## 4. Embodied-Episode Test (Production Filter)

Every short story must pass: **"Is this an embodied episode, or a summary?"**

- Summary → reject; that work belongs in the narrative chapter.
- Embodied episode → accept; show me a witnessed scene with anchored entities living in it.

Example: "Akbar reformed military administration with the mansab system" (narrative claim) becomes a short story that shows Akbar *in court* assigning mansab ranks to nobles, ranks visualized as horsemen counts, a noble protesting, the system playing out in a campaign.

---

## 5. Bundling Principle

Stages from the timeline are the **fine-grained inputs** that cluster into short stories. A short story = **a coherent micro-narrative** (a court, a campaign, a crisis, a movement arc).

- Typical era → ~10–15 short stories
- Each story bundles: 1 main event/movement/reform + 1–N anchored people / institutions / places + 0–N concepts as embedded-audio + many fly-by mentions
- The bundling decision IS the anchor-home assignment decision

**Stage preservation:** Because many stages merge into one short story, stage classification gets absorbed in the visual layer. The **stage audios on the timeline** preserve it independently — that's their unique role.

---

## 6. Art Style

- **Consistent base layer** across all eras (TBD; finalized empirically during image-creation experiments, not pre-specified)
- **Per-era artistic variations** (India-narrative vs. parallel-world feels, era-mood)
- **Per-story reference image** drives style consistency within a story (Gemini-grounded with 1–2 tight references + prompts)
- **People illustrated all the way through** — but where photographic/painting evidence exists (post-photography modernity, period paintings), it grounds the illustration. Photographic figures → precise line-work translation of the photograph into the comic's style. No raw photographs pasted into comics; the visual register stays uniform within a story.

---

## 7. Audio Architecture (deferred production, planned now)

- **Hosts:** 2 fixed NotebookLM voices across the entire surface. User has familiarity, voices are sorted.
- **Continuous-conversation feel:** Even though audios are generated piece-by-piece, they should feel like one ongoing conversation. User can "summon" hosts anywhere on the surface.
- **Audio slot types:**
  - Concept audios → embedded inside short stories at the panel where the concept appears
  - Stage audios → on the timeline, preserving stage classification absorbed by short stories
  - (Open) Person-anchor audios → TBD whether person anchor panels carry their own biographical audio
- **Audio production deferred** until visual layer is complete. User handles audio generation.
- **Critical visual-production deliverable:** the **adjacency graph** (see §8) — without it, audios can't cross-reference and the continuous-conversation feel fails.

---

## 8. Graph Schema (to formalize in Task 4)

The visual production pipeline emits a graph as a byproduct. This graph drives both PWA rendering and audio-continuity scripting.

**Entities:** era, stage, narrative-chapter, short-story, person, place, institution, event, movement, reform, concept, anchor-panel, audio-slot, PYQ

**Relationships:**
- Era *contains* stages, narrative-chapter, short-stories
- Short-story *bundles* stages; *contains* anchor-panels and embedded concept-audio-slots; *adjacent-to* other short-stories (shared entities / causal / parallel)
- Entity *has-home-in* exactly one short-story; *appears-in* many (typed: `anchor` / `cameo` / `background` / `caption` / `connective`)
- Stage *has-audio* (timeline stage audio peripheral)
- PYQ *tests* entities → weights anchor-deserving threshold and study importance

---

## 9. PWA Scaffolding (to spec in Task 5)

- **History tab** = horizontal full-screen carousel through 11 eras
- **Per-era home screen:** title → narrative chapter (read first) → short-story gallery (independent collection of clickable stories)
- **Short-story view:** full-screen sequential comic reader; anchor panels are static visual focus points in the stream; embedded audio triggers at concept moments
- **Timeline view:** stages on timeline, each with audio peripheral
- **Summon-hosts mechanism:** persistent UX to invoke the 2 audio hosts at any point (mechanism TBD in Task 5)

---

## 10. Pre-Production Task List

Five separate-session tasks converge in one finalization session before production begins. Pilot era throughout: **Mughal**.

| # | Task | Depends on | Output |
|---|---|---|---|
| 1 | PYQ-entity mapping & frequency weighting | — | Weighted entity list per era; anchor-deserving threshold |
| 2 | Bundling principle test (Mughal) | 1 | Mughal bundle plan; anchor/mention designations |
| 3 | Base art style layer finalization | 2 (one bundle) | Base style brief; reference images |
| 4 | Graph schema specification | 1 + 2 | Schema doc + Mughal example instance |
| 5 | PWA scaffolding design | 4 | Component contracts; data-flow plan |
| ★ | **Convergence session — pipeline finalization** | 1–5 | Locked production pipeline; Mughal production begins |

**Ordering:** 1 → 2 → 4 → 5; Task 3 runs parallel after Task 2 produces one bundle.

---

## See Also

- `surfaces/HISTORY_SPRINT_ASSET_PLAN.md` — node classification, asset counts, era distribution
- Era JSONs at `surfaces/history-surface/{era}/{era}.json`
- PYQ JSONs at `surfaces/history-surface/{era}/pyqs_{era}_era.json`
- Memory: `project_history_sprint_tasks` (task index for cross-session pickup)
