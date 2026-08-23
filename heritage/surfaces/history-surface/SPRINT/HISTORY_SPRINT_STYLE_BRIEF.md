# History Sprint — Base Art Style Brief

**Task 3 output.** Finalized empirically via Gemini test panels on pilot story `s04_ibadat_khana_1578`.  
**Status:** DRAFT — prompts ready for first test round. Refinement log below. Locked brief fills in after iteration.

---

## Pilot Story: s04 — The Ibadat Khana, Thursday Night, 1578

**Scene:** Ibadat Khana, Fatehpur Sikri. A Sunni and Shia theologian argue at volume about the Imamate; a Jain monk from Kathiawar waits; Rodolfo Acquaviva and Antonio Monserrate sit with illustrated Gospels; Abu'l Fazl writes in the corner; Birbal sits across; outside, Salim Chishti's white tomb glows; in the adjoining courtyard, Tansen tunes for Darbari Kanada.

**Why this story for style testing:**
- 7 anchors + richest cameo palette → stress-tests character-density handling
- Night interior (oil lamp light) → locks lighting model
- Mix of person anchors + concept anchors (Sulh-i-kul, Mughal Painting) → tests panel types
- Fatehpur Sikri architecture → locks the background grammar

---

## 1. Starting Style Hypothesis

This is a hypothesis, not a spec. Run the prompts, see what lands, mark what to adjust.

| Parameter | Hypothesis | Status |
|---|---|---|
| Art form | Illustrated graphic novel panel | — |
| Line work | Clean ink lines, expressive weight variation (thin atmospheric, thick character outlines) | — |
| Color palette | Sandstone ochre, deep burgundy, midnight blue, gold accent, amber lamplight | — |
| Character proportions | Slightly elongated, expressively drawn faces; historically-informed Mughal costume detail | — |
| Architecture | Accurate Fatehpur Sikri — red sandstone, Persian arches, jali lattice screens | — |
| Composition | Layered like Mughal miniature — flat depth, clear foreground/middle/background planes, no atmospheric perspective blur | — |
| Lighting | Night interior: warm amber from oil lamps; exterior: cool moonlight on white marble tomb | — |
| Borders | Thin geometric margin, Mughal tessellation motif | — |
| People rule | Fully illustrated; no raw photos or period paintings pasted in | — |

---

## 2. Gemini Prompts — First Test Round

**How to use:** Copy each prompt directly to Gemini image generation. Generate 2 variants each. Pick best or note what to change. Log adjustments in Section 3.

---

### Panel A — Exterior Establishing Shot (atmosphere, night, architecture)

```
Graphic novel panel illustration. Night scene at Fatehpur Sikri, Mughal India, circa 1578. Exterior view of the Ibadat Khana (House of Worship), a red sandstone building with Persian arched doorways and carved jali lattice screens. Oil lamps flicker inside, casting amber light through the jali onto the courtyard. To the right, the white marble dargah of Salim Chishti glows under cool moonlight, contrasting with the warm sandstone. A lone musician figure (Tansen) is visible tuning a sitar in the courtyard shadows. Sky: deep indigo with stars, crescent moon. Art style: illustrated graphic novel, clean expressive ink lines, no photo-realism. Color palette: deep burgundy, sandstone ochre, midnight blue, gold highlights, amber lamp glow. Flat layered composition inspired by Mughal miniature painting structure. Thin geometric border with Mughal tessellation motif. No text, no speech bubbles.
```

---

### Panel B — Full Assembly Interior (wide shot, crowd, establishing who is in the room)

```
Graphic novel panel illustration, wide interior shot. The Ibadat Khana debating hall, Fatehpur Sikri, 1578, night. Emperor Akbar sits cross-legged on a slightly raised platform at center, face composed and watchful, wearing white jama and gem-set turban. To his left: two Muslim theologians in heated argument, one in black Shia robes, one in white Sunni turban, hands raised. To his right: two Jesuit priests in dark cassocks holding open illustrated manuscripts. In the background corner: a figure writing by lamplight (Abu'l Fazl). Near Akbar: a witty courtier in colorful dress (Birbal). A Jain monk in white robes sits at the periphery. Oil lamps and candelabra light the scene warmly. Red sandstone walls, Persian arched alcoves, carpet underfoot. Art style: illustrated graphic novel, expressive ink lines, no photo-realism. Color palette: sandstone ochre, deep burgundy, midnight blue, gold, amber light. Flat layered Mughal-miniature-inspired composition. Thin geometric margin. No text.
```

---

### Panel C — Anchor Panel: Akbar (close-up, face, psychological state)

```
Graphic novel panel illustration, portrait close-up. Emperor Akbar, Mughal India, 1578. He is approximately 36 years old, with a broad face, trimmed beard, sharp eyes that suggest contained restlessness — not a ruler settling into ease, but one actively listening, synthesizing, weighing. He wears a white jama embroidered at the collar, a Mughal turban with a central jewel and aigrette feather. Background: out-of-focus debating assembly behind him, amber lamp glow warming one side of his face, the other side in cooler shadow. Expression: not smiling, not stern — genuinely curious. Art style: illustrated graphic novel, expressive ink work, slightly elongated face with high detail on eyes and turban, historically-informed Mughal costume. Color palette: warm amber on face, deep red background glow, midnight blue shadows. No text. Clean border.
```

---

### Panel D — Anchor Panel: Abu'l Fazl (writing, quill, Akbarnama)

```
Graphic novel panel illustration, medium shot. Abu'l Fazl, Akbar's court historian and secretary, seated by lamplight in the corner of the Ibadat Khana, 1578. He is perhaps 30 years old, lean, intense, clean-shaven with short dark hair, wearing a simple courtier's dress (white jama, sash). A quill poised over an open large manuscript (the Akbarnama in its making), ink pot beside him, scrolls stacked. Around him: the noise of the debate is implied but he is focused inward, the lamp casting a warm circle of clarity on his manuscript while the room beyond is softer. Art style: illustrated graphic novel, expressive clean ink lines. Color palette: amber lamplight on the figure and manuscript, deep indigo and burgundy receding background. The manuscript page has calligraphic markings (non-readable, suggested). Thin border. No text.
```

---

### Panel E — Concept Panel: Sulh-i-Kul (visual metaphor, not purely representational)

```
Graphic novel panel illustration, symbolic panel. Representing the concept of Sulh-i-Kul (Absolute Peace / Universal Tolerance), Akbar's policy. Visual idea: four figures stand in a loose circle — a Muslim theologian, a Jain monk, a Jesuit priest, a Hindu pandit — each facing slightly inward, not toward each other but toward a soft light source at the center (a flame or lamp). No figure dominates. All are drawn in their distinct religious dress with equal care and dignity. The light at center connects all four. Background: abstract Mughal-geometric pattern in deep blue-gold. Not a realistic room scene — more like a symbolic diagram drawn in illustration style. Art style: graphic novel, clean lines, flat color, Mughal ornamental geometry border. Color palette: one distinct accent color per figure (saffron, white, black, ochre), gold light at center, deep blue ground. No text, no labels.
```

---

### Panel F — Fly-By: Theological Debate (close-up on the arguing pair, energy and gesture)

```
Graphic novel panel illustration, medium shot. Two scholars arguing in the Ibadat Khana, 1578, night. A Sunni scholar (white turban, green embroidered robe, full beard) gestures emphatically with one hand raised, the other pointing at a manuscript in his lap. Opposite him, a Shia scholar (black turban and robe, smaller beard) leans forward with a counter-argument, finger raised. Both faces show intellectual passion — not violence, but the heat of genuine theological combat. Between them, the implied audience watches. Oil lamp light from below creates dramatic shadow on their faces. Art style: illustrated graphic novel, expressive ink lines with strong shadow work, not cartoonish. Color palette: the two scholars in contrasting greens and blacks, warm amber from below, shadow behind. Thin border. No text.
```

---

## 3. Refinement Log

*Fill in after each Gemini test round. Note what landed, what to adjust.*

| Round | Prompt | What worked | What to change | Decision |
|---|---|---|---|---|
| 1 | Panel A (Exterior establishing) | Palette locked (sandstone/indigo/amber), architecture accurate (jali visible, dome contrast clear), night lighting convincing, composition reads instantly, border convention solid | None — ready as reference | ✓ **LOCKED**. Style register confirmed: high-end illustrated narrative (not cartoonish comic). Use this panel as anchor for consistency in Panels B–F. |
| 1 | Panel B (Full assembly interior) | All seven figures legible under density. Character types visually distinct (theologians' debate clear, Akbar centered with authority, Jesuits with manuscripts, Jain monk serene). Palette/lighting identical to Panel A. Architectural detail (arches, jali, lamps) consistent. Spatial depth excellent (foreground/mid/background clear). Character expression readable (intellectual passion in debate, calm in Akbar, reverence in Jesuits). | None — clean success | ✓ **LOCKED**. Base style confirmed across radically different compositions. Density handling perfect. Ready to move to anchor close-ups (Panels C–D) to test character psychology. |
| 1 | Panel C (Akbar close-up anchor) | Three variants generated; all functionally identical (consistency confirmed). Character presence strong at thumbnail scale. Psychological state readable: calm authority + open listening (meets brief requirement). Costume detail sharp (turban gem, jama embroidery, trim beard). Background blur subtle; depth clear without distraction. Lighting consistent with Panels A–B (warm amber face, cool shadow). Eye focus conveys "listening and thinking simultaneously." | None — anchor panel style locked | ✓ **LOCKED**. Anchor close-up formula established. Character psychology readable at small scale. Reference: Image 3 variant. |
| 1 | Panel D (Abu'l Fazl writing anchor) | Two variants generated; virtually identical. Character focus (intensity/concentration) readable. Historical costume accurate (white jama, sash). Manuscript legible with calligraphic suggestion (Persian script). Lamp-light circle is tight and focuses attention on the act of writing. Background assembly figures (blurred shadows) don't distract. Lighting, palette, and line work consistent across all prior panels. | None — anchor formula confirmed | ✓ Anchor formula holds across different character moments (listening vs. writing). Fully ready for concept/fly-by tests. Reference: Image 6 variant. |
| 1 | Panel E (Sulh-i-kul concept panel) | Four distinct figures (Muslim theologian, Jain monk, Jesuit, Hindu pandit) arranged in loose circle around central flame. Each in accurate religious dress (black-white turban, white robes, black cassock, orange). Geometric tessellation background (deep blue + gold) successfully signals "diagrammatic mode" (not a failed realistic scene). Central flame metaphor for Sulh-i-kul is instantly legible. All four figures equally present (no hierarchy). Style consistency maintained despite shift to symbolic register. | None — concept-panel formula works | ✓ **LOCKED**. Concept panels successfully translate to diagrammatic register without losing illustration quality. Geometric border convention reinforces "special panel" status. |
| 1 | Panel F (Theological debate fly-by) | Two scholars in animated debate: Sunni (green robe, white turban, hand raised) vs. Shia (black robe, black turban, finger pointing). Gesture language clear and culturally appropriate (hand raised, finger emphasizing point). Facial expression readable (passion, engagement, intellectual intensity). Manuscript on lap grounds the theological argument. Lamp between creates light/heat metaphor and casts dramatic shadows. Background assembly (blurred) contextualizes without distraction. High-energy interaction readable; moment is "witnessed" not summarized. Palette and line work consistent. | None — interaction formula confirmed | ✓ **LOCKED**. High-energy multi-figure scenes work. Gesture language is expressive and clear. All six panel types tested and confirmed. Base style fully locked. Ready to document. |

---

## 4. Per-Era Variation Knobs (Framework — fill in after base is locked)

Once the base style is locked from s04 testing, document how each era *varies* within that base:

| Era | Mood | Color shift | Palette notes | Architectural grammar | Lighting |
|---|---|---|---|---|---|
| 1 Prehistoric | — | — | Ochre, burnt sienna, cave shadow | Landscape-only | Fire, daylight |
| 2 Ancient Indus | — | — | Terracotta, grey, muted | Grid city, granary brick | Overcast day |
| 3 Ancient Classical | — | — | Deep red, gold, cream | Stone temple, column | Bright daylight |
| 4 Early Medieval | — | — | — | — | — |
| 5 Delhi Sultanate | — | — | Blue tile, grey stone, white lime | Mosque arch, dome | Harsh sun, torch |
| 6 **Mughal (pilot)** | Opulent synthesis | Sandstone + jewel tones | Burgundy, midnight blue, gold | Iwan arch, jali, chahar bagh | Amber lamp, moonlight |
| 7 Early Colonial | — | — | — | — | — |
| 8 High Colonial | — | — | — | — | — |
| 9 Freedom Struggle | — | — | — | — | — |
| 10 Post-independence | — | — | — | — | — |
| 11 Contemporary | — | — | — | — | — |

**India-narrative vs. parallel-world distinction:**
- India-narrative eras (1–9, 11): grounded in Indian geography, architecture, dress
- Parallel-world scenes (e.g., s19 Six Courts): split-screen convention TBD — same base style, shifted palette per civilization (Ottoman gold-red, Safavid blue-tile, Qing jade-black, Tudor grey-stone, etc.)

---

## 5. Locked Base Style Brief

*Confirmed across all six panel types (A–F). Empirically tested on s04 Ibadat Khana.*

```
[BASE STYLE LOCKED — Round 1 Complete]

Art form:
  Illustrated graphic novel / high-end illustrated narrative.
  Clean, expressive, readable at all scales (thumbnail to full-screen).
  NOT photo-realistic; NOT cartoonish.

Line work:
  Clean ink lines with expressive weight variation.
  Thin for atmosphere, thick for character outlines and emphasis.
  Details (costume, turban gems, facial features) rendered with crisp precision.
  Shadow work (cross-hatching, gradient) creates depth and mood without muddiness.

Color palette (base):
  Primary: Sandstone ochre (architecture, earth), deep burgundy (walls, depth), midnight blue (night sky, far background)
  Accent: Gold (geometric patterns, jewels, highlights), warm amber (oil lamp glow)
  Skin tones: Warm terracotta with amber highlight on lit side, cool shadow on unlit side.
  Palette holds across all panel types.

Character proportions:
  Slightly elongated faces (not cartoonish, but stylized toward expressiveness).
  Accurate historical costume detail (turban shape, jama cut, sash, embroidery).
  Hands rendered with anatomical clarity (gestures legible even when small).
  Beards, turbans, and headgear are visually distinct per character type.

Composition structure:
  Layered like Mughal miniature painting: flat depth (no atmospheric perspective blur).
  Clear foreground / mid-ground / background planes.
  Multiple figures in same scene remain individually legible (no visual clutter).
  Background figures blur appropriately but maintain silhouette clarity.

Lighting model:
  Interior scenes: Warm amber from oil lamps + candelabra. Directional shadows cast dramatically.
  Exterior scenes: Cool moonlight on marble contrasting with warm sandstone.
  Night scenes: Interplay of warm interior glow and cool exterior blue.
  Light source (lamp, window, flame) is always visible and motivates shadow direction.
  Dramatic shadow work on faces in close-ups conveys psychological intensity.

Border/frame convention:
  Thin geometric tessellation border (Mughal geometric motif: interlocking stars, lattice).
  Consistent across all panels.
  Separates panel from surrounding space; reinforces "intentional composition" feel.

People rule:
  All figures fully illustrated (no raw photographs pasted).
  Historical costume and physical features informed by period sources, but rendered in the unified illustration style.
  Character psychology readable in face and posture at all scales.

[MUGHAL ERA VARIATION]

Color shift:
  Sandstone ochre dominates; jewel tones (deep burgundy, midnight blue) in equal measure.
  Gold used generously (tessellation, jewels, manuscript detail).
  Amber lamplight is the primary night-scene color driver.

Palette:
  Warm: Ochre, amber, terracotta, saffron accent
  Cool: Midnight blue, slate, cool shadow
  Accent: Gold, deep burgundy
  (Result: opulent but controlled; no oversaturation.)

Architectural grammar:
  Red sandstone as primary material (Fatehpur Sikri accurate).
  Persian arches (iwan) as dominant architectural element.
  Jali (lattice) screens visible in windows and decorative panels.
  Geometric carving detail on wall panels, capitals, and ceiling.
  Chahar bagh garden paths implied in exterior scenes.
  Marble domes (Salim Chishti tomb) rendered in cool white/grey.

Lighting:
  Oil lamps with flame visible (warm amber pool).
  Moonlight on white marble (cool contrast).
  Torches in courtyard scenes (flicker, directional shadow).
  Night scenes dominate (1578 Ibadat Khana = evening assembly).

[REFERENCE PANELS]
Panel A (Exterior): references/s04_panel_a.png
Panel B (Interior assembly): references/s04_panel_b.png
Panel C (Akbar anchor): references/s04_panel_c.png
Panel D (Abu'l Fazl anchor): references/s04_panel_d.png
Panel E (Sulh-i-kul concept): references/s04_panel_e.png
Panel F (Debate fly-by): references/s04_panel_f.png
```

---

## 6. What Makes a Panel "Work" — Evaluation Criteria

When reviewing Gemini outputs, check against these:

1. **Readability at speed** — Can you absorb the key figure / moment in 3 seconds? If cluttered, adjust density.
2. **Historical grounding without pedantry** — Looks plausibly Mughal, but isn't a museum exhibit; feels alive.
3. **Character expressiveness** — Faces carry emotion legible at thumbnail size.
4. **Architectural accuracy** — Red sandstone, Persian arch, jali are recognizable. Not generic "medieval."
5. **Color coherence** — The palette feels like one scene, not a grab-bag.
6. **Reproduction across sessions** — Style holds when prompt is reused with a different subject matter.
7. **Concept-panel legibility** — The symbolic Panel E (Sulh-i-kul) should read as intentionally diagrammatic, not as a failed realistic scene.
