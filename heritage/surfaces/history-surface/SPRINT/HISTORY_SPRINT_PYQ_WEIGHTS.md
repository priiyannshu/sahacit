# Task 1 Output — PYQ-Entity Frequency Weighting

**Generated:** 2026-05-16
**Companion data:** [`HISTORY_SPRINT_PYQ_WEIGHTS.json`](HISTORY_SPRINT_PYQ_WEIGHTS.json)
**Script:** [`history-surface/_task1_pyq_weights.py`](history-surface/_task1_pyq_weights.py)

---

## What this is

The Tier-2 anchor filter for the history sprint. For every era node, we counted how many era-pool PYQs reference it. Counts feed Task 2 (bundling) — the entities above each era's threshold are the anchor-deserving set: every story should land at least one of them as an anchor panel, and *every* anchored entity should have exactly one home story.

---

## Method

1. **PYQ pool normalization.** Each era's PYQ JSON has a different shape (`pyqs[]`, `questions[]`, split `high/medium/boundary/slip_through[]`). All buckets flattened into a single pool per era — including boundary and slip-through, per user direction.
2. **Label normalization.** Strip year-parens (`Akbar (1556-1605)` → `Akbar`) and trailing non-year qualifier parens. Conservative aliasing — only generated a punctuation-stripped variant (`Akbar's Tomb` → `Akbars Tomb`). No surname / "of X" / inside-paren aliases (early run had those; they bled "Akbar" into every `hist_akbar_*` node, producing six tied counts at 17 — fixed).
3. **Matching.** Word-boundary regex of `(primary | aliases)` against `question + " " + options text`, IGNORECASE. Each PYQ contributes +1 to every distinct node it touches.
4. **Aggregation.** Per node, `pyq_count = |distinct PYQ ids matched|`; full `pyq_ids[]` retained in JSON as audit trail for Task 2.

---

## Results

| Era | PYQ pool | Nodes matched / total | Zero-hit PYQs | List-question PYQs (>5 hits) |
|---|--:|--:|--:|--:|
| prehistoric | 2 | 3 / 71 | 0 | 0 |
| ancient-indus | 18 | 13 / 115 | 10 | 0 |
| ancient-classical | 127 | 71 / 266 | 58 | 0 |
| early-medieval | 48 | 12 / 214 | 37 | 0 |
| delhi-sultanate | 85 | 25 / 204 | 50 | 0 |
| mughal | 72 | 36 / 263 | 29 | 4 |
| early-colonial | 188 | 34 / 283 | 143 | 0 |
| high-colonial | 176 | 44 / 233 | 88 | 0 |
| freedom-struggle | 248 | 76 / 389 | 115 | 5 |
| post-independence | 259 | 70 / 516 | 147 | 1 |
| contemporary | 773 | 45 / 542 | 697 | 0 |
| **TOTAL** | **1996** | **507** unique (node,era) pairs | | |

**Zero-hit signal.** High zero-hit rates (contemporary 90%, early-colonial 76%, post-independence 57%) confirm what the architecture already assumed: many PYQs test themes / policies / current-affairs rather than named entities the era graph captures. These PYQs will be served by narrative-chapter coverage, not by anchored short-story panels.

---

## Anchor-deserving thresholds (per era)

Threshold chosen so the anchor set lands in the [20, 50] band — architecture target of ~10–15 stories × ~3 anchors per story. Where the PYQ pool is too small for that band, the threshold defaults to ≥1 and the full PYQ-matched set is the anchor pool.

| Era | Threshold (≥) | Anchor count | Dominant types |
|---|--:|--:|---|
| prehistoric | 1 | 3 | place, period |
| ancient-indus | 1 | 13 | place, concept |
| ancient-classical | 2 | 20 | person, concept |
| early-medieval | 1 | 12 | person, place, institution |
| delhi-sultanate | 1 | 25 | person (17/25) |
| **mughal (pilot)** | **1** | **36** | **person (22/36), concept, period, empire, event** |
| early-colonial | 2 | 22 | person, event, law |
| high-colonial | 2 | 23 | person, institution, event |
| freedom-struggle | 5 | 20 | movement, event, person |
| post-independence | 3 | 20 | institution (12/20) |
| contemporary | 1 | 45 | institution, policy, treaty, scheme |

**Reading note.** Thresholds are a *proposal*, not a lock. Task 2 (Mughal bundling) may push back: e.g., if an entity at count = 0 still belongs in a story for narrative coherence, anchor it. The threshold is meant to surface the strong PYQ-backed candidates so they don't get missed, not to gate the rest.

---

## Pilot era (Mughal) — top 25

```
17  person       Akbar (1556-1605)
17  period       Akbar
10  person       Aurangzeb (1658-1707)
10  period       Aurangzeb
 6  person       Jahangir (1605-1627)
 4  empire       Mughal Empire
 3  place        Fatehpur Sikri
 3  person       Humayun
 3  person       Shah Jahan (1628-1658)
 3  person       Shivaji
 3  period       Shah Jahan
 2  person       Babur (1526-1530)
 2  person       Guru Arjan Dev
 2  concept      Jama Masjid (Delhi)
 2  place        Surat
 2  person       Tulsidas
 1  person       Abdul Hamid Lahori
 1  person       Abu'l Fazl
 1  person       Banda Bahadur
 1  event        First Battle of Panipat (1526)
 1  person       Dadu Dayal
 1  concept      Gol Gumbaz (Bijapur)
 1  person       Guru Gobind Singh
 1  person       Guru Tegh Bahadur
 1  empire       Hyderabad State
```

(Full anchor list of 36 entries: see `HISTORY_SPRINT_PYQ_WEIGHTS.json` → `eras.mughal.weighted_nodes`, take entries with `pyq_count ≥ 1`.)

Type mix for Mughal anchors: **person 22, concept 4, period 3, empire 2, place 2, event 2, institution 1**. Person-heavy is good for the embodied-episode test — most anchors are humans you can show in a witnessed scene. The 4 concept anchors (Mughal-Mughal Empire, Jama Masjid, Gol Gumbaz, Sufism) will need either a person/place piggy-back or a tight conceptual anchor panel.

---

## Known limitations & flags for Task 2

1. **Duplicate nodes inside era JSONs.** Freedom-struggle has at least 5 duplicate pairs (e.g., `hist_constituent_assembly` × 2, `Quit India Movement` and `Quit India Movement (1942)` as separate nodes). Same in Mughal (`hist_akbar` person vs. `period_akbar`). Both halves of the duplicate appear in the weighted list at the same count, inflating the apparent anchor coverage. Task 2 needs to merge or pick one home before assigning anchors.
2. **Person/period twin nodes.** `Akbar` exists twice (the person + the period named after him). For anchoring, treat the person node as the anchor home; the period is a stage/timeline construct, not an anchor candidate. Same for Aurangzeb, Shah Jahan.
3. **Concept-label nodes under-match.** Descriptive labels like *Akbar's Social Reforms*, *Bernier's Land Ownership Theory*, *Mughal Court Etiquette* require the PYQ to contain the full phrase. PYQs rarely quote labels verbatim, so these nodes show pyq_count = 0 even when the question is "about" them. Acceptable for Tier-2: concepts mostly live as captions / embedded-audio in stories, not as anchor panels.
4. **List questions.** Mughal has 4 PYQs that match >5 nodes ("Match the following…" style). Counted as full hits for each; effectively dilutes each anchor by ~1/N. Not severe enough to warrant per-PYQ down-weighting — flagged in JSON (`pyqs_likely_list_questions`) for Task 2 review.
   - **List-question-only anchors in Mughal:** `hist_abdul_hamid_lahori` (Abdul Hamid Lahori) and `hist_thomas_roe` (Sir Thomas Roe). Their entire pyq_ids evidence is list-questions — treat as **suggestive, not PYQ-earned**. They may still deserve anchor status on narrative grounds (Padshahnama chronicler / Jahangir's court diplomacy), but the count alone doesn't carry it. All other ≥1-threshold eras came back clean on this check.
5. **Cross-era PYQ counting.** Same PYQ id may appear in multiple era pools (border questions) and contributes to each era's weights independently. This is intentional — a PYQ that touches both Delhi-Sultanate and Mughal genuinely tests entities in both surfaces.
6. **Contemporary era is the outlier.** 697/773 PYQs are zero-hit — the contemporary node graph is built around abstract policy/institution clusters that PYQs don't name verbatim. Anchor selection there will lean heavily on narrative-chapter coverage rather than entity-frequency.

7. **Pool size vs. canonical 2,839 corpus — non-history-subject PYQs in late eras are mostly legitimate, not contamination.** Sum of per-era pools is 1996, large because the corpus is 2,839 PYQs total and we cross-counted (a border-question can belong to two eras). The bigger optical surprise — post-independence has 51/259 history-subject PYQs, contemporary has 2/773 — is *not* contamination: the late-era node graphs deliberately include temporal-polity, temporal-economy, environment-treaty, and current-affairs entities that were *born in that era* (Finance Commission 1951, NDC 1952, Planning Commission, Fundamental Duties 1976, Disinvestment, NITI Aayog 2015, Kyoto Protocol 1997, European Union, etc.). PYQs about these entities — under any subject label — legitimately weight them, because the entity sits in the era graph's narrative by design.

   What *is* still noise: PYQs that name-drop an entity in passing while actually testing something else (e.g., an RBI PYQ that mentions the EU as a comparison). Spot-checking the top contemporary anchors found this is a minority across Kyoto / NITI / Finance Commission / NDC etc. Same noise rate as the regex's general failure mode in pure-history eras — manageable at bundling time by reading the actual PYQ text behind a count.

   **Mughal-and-earlier eras are 100% history-subject** (pool composition: prehistoric→mughal all Ancient/Medieval/Art-and-Culture). Mughal pilot weights are unaffected by this concern. Early-colonial / high-colonial / freedom-struggle are ≥85% history-subject; the small non-history slice in those eras follows the same legitimate-temporal-polity pattern.

---

## Hand-off to Task 2

Read `HISTORY_SPRINT_PYQ_WEIGHTS.json` → `eras.mughal.weighted_nodes`. Take entries with `pyq_count ≥ 1` (threshold for Mughal) → that's the anchor-deserving set, 36 entries. Bundle them into ~10–15 short stories using the embodied-episode test. Each anchored entity = one home story.

The `pyq_ids[]` field on each weighted node lets you cross-check *why* a node has its count — useful when deciding which two competing nodes (say `hist_akbar` and `hist_akbar_social_reforms`) better serves as an anchor home.
