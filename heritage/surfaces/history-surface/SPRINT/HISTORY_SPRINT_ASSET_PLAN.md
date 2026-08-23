# History Sprint — Peripheral Asset Classification

**Sprint duration:** 2026-05-15 to 2026-05-24 (9 days)  
**Objective:** Complete one fully-realized subject surface (History) with all peripheral assets wired into PWA  
**Testing ground:** Home exam 2026-05-24; proof-of-concept for Geo/Eco/Polity visual overhauls post-exam

---

## Architectural Insight (revised 2026-05-16)

**People, Institutions, and Places do NOT live as standalone illustration galleries.** Instead, they are **anchor panels embedded within the comic visual narratives** of Events / Movements / Reforms.

- Each person/institution/place still gets **one dedicated full-focus panel** carrying all the UPSC-relevant detail that a standalone illustration would have carried.
- That panel sits inside the temporal flow of the comic narrative — at the moment the entity enters the story.
- Visual style of the anchor panel matches the narrative it lives in (consistency across the comic sequence).
- The anchor panel acts as a **pause point** in the sequential stream — the reader stops, absorbs the dedicated full-focus content, then continues.

This collapses the asset surface from **three production tracks (illustrations / audio / comics)** down to **two: comics-with-anchors and audio**.

---

## Asset Buckets — Revised Architecture

### Track A: Comic Visual Narratives (the spine)
**Container nodes (674 narratives):**
| Node Type | Count | Narrative Length |
|---|---|---|
| Events | 572 | 4-8 base panels + anchor panels |
| Movements | 70 | 4-6 base panels + anchor panels |
| Reforms | 32 | 4-6 base panels + anchor panels |

**Anchor panels embedded inside narratives (919 anchors):**
| Anchor Type | Count | Function |
|---|---|---|
| People | 555 | Full-focus biographical panel at moment of entry into narrative |
| Institutions | 220 | Full-focus system/structure panel at moment of establishment/relevance |
| Places | 144 | Full-focus geographic/architectural panel at moment of significance |

**Comic style requirements:**
- Visual style locked per era (mughal era comics look mughal-period, freedom-struggle comics feel late-colonial, etc.)
- Anchor panels inherit the era's style but get extra detail density
- Sequential reading direction; clear panel transitions

### Track B: Audio Layer (903 audio files)
| Node Type | Count | Duration | Content |
|---|---|---|---|
| Concepts | 734 | 2-4 min | Definition, context, evolution, UPSC relevance |
| Periods | 169 | 1-2 min | Timeline, political/social/cultural conditions, transitions |

**Open question:** Do People-anchor panels also carry their own audio (the 2-3 min biography from the original plan), or does the visual panel alone carry the load?

---

## Era Distribution Recap

### Comic narratives by era (674 total)
```
Era                    Events  Movements  Reforms  Total comics
Contemporary           149     3          —        152
Post-Independence      135     21         2        158
Freedom Struggle       127     23         5        155
Early-Colonial          44     5          11       60
High-Colonial           40     8          13       61
Mughal                  37     1          2        40
Delhi Sultanate         12     2          1        15
Ancient-Classical       11     —          —        11
Early-Medieval           8     7          —        15
Ancient-Indus            6     —          —        6
Prehistoric              3     —          —        3
```

### Anchor panels by era (919 total)
```
Era                    People  Institutions  Places  Total anchors
Freedom Struggle       92      21            1       114
Mughal                 90      12            5       107
Post-Independence      67      63            6       136
Delhi Sultanate        63      4             23      90
Ancient-Classical      61      13            33      107
High-Colonial          51      34            1       86
Early-Colonial         46      14            4       64
Early-Medieval         45      10            20      75
Contemporary           36      48            4       88
Ancient-Indus          4       1             26      31
Prehistoric            —       —             31      31
```

### Audio files by era (903 total)
```
Era                    Concepts  Periods  Total audio
Ancient-Classical      124       3        127
Early-Colonial         123       17       140
Mughal                 94        13       107
Early-Medieval         92        9        101
Delhi Sultanate        69        11       80
Ancient-Indus          66        9        75
High-Colonial          51        20       71
Freedom Struggle       49        25       74
Prehistoric            30        7        37
Contemporary           20        30       50
Post-Independence      16        25       41
```

---

## Production Implications of the Anchor Integration

1. **Each comic narrative becomes longer / richer** — a typical Mughal event-comic might have 6 base panels + 3 anchor panels (1 person + 1 institution + 1 place) = 9 panels total.

2. **Cross-referencing:** A person like Akbar may appear in multiple event narratives. The user's spec says **one full-focus panel per entity** — so Akbar's anchor panel lives in his most defining narrative (e.g., "Akbar's accession"); other narratives reference him but don't duplicate the anchor.

3. **Coverage mapping:**
   - Each event/movement/reform JSON node needs metadata: which people, institutions, places it anchors
   - Each person/institution/place JSON node needs metadata: which narrative carries its anchor panel
   - This is a graph problem — building the anchor assignment first, then producing comics with the right anchors baked in

4. **Style budget:** ~11 distinct visual styles (one per era) × consistent anchor density = manageable. Within an era, the style is fixed.

---

## Sourcing Decisions Still Open

### Comic generation
- [ ] AI-generated panels (Flux, SDXL, Midjourney) with era-specific style LoRAs
- [ ] Sourced historical artwork arranged into sequences
- [ ] Hybrid: AI for base panels, sourced for anchor panels of well-documented figures (Babur, Gandhi, etc.)

### Audio generation
- [ ] TTS for all 903 audio files (Coqui, ElevenLabs, Google)
- [ ] Single narrator voice or per-era voice variation?
- [ ] Script generation pipeline: node JSON → LLM-drafted script → TTS

### Anchor panel audio (TBD)
- [ ] Keep biographical audio for the 555 person-anchors?
- [ ] If yes — adds 555 to audio production count (total 1,458)

---

## Next Steps

1. **Resolve anchor-audio question:** Do person-anchor panels carry their own audio?
2. **Build anchor assignment graph:**
   - For each of 674 narratives, list the people/institutions/places that anchor inside it
   - For each of 919 entities, confirm its assigned narrative (its "home")
3. **Pick pilot era for production test:** Mughal (balanced load: 40 narratives, 107 anchors, 107 audio files) is a good fit
4. **Sourcing infrastructure:** Set up AI generation pipeline + TTS pipeline before bulk production
5. **Coverage threshold:** Decide if 100% by exam is realistic or if priority-weighting (PYQ frequency) is needed

---

**See also:**
- [[feedback_chapter_wiring_protocol]] for inserting assets into PWA
- [[project_visual_layer_strategy]] for asset type definitions
- Era JSON files at `surfaces/history-surface/{era}/{era}.json` for node-level data
