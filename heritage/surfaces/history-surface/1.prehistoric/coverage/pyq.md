# PYQ Coverage — Prehistoric Era

## Sweep methodology

Keyword sweep across all 2,839 PYQs (1995–2025) with ~70 patterns covering:
- Period names (Palaeolithic / Mesolithic / Neolithic / Chalcolithic / Stone Age / prehistoric)
- Tool types (microlith, hand axe, Acheulian, Oldowan)
- Human evolution (Homo sapiens/erectus/habilis, Neanderthal, Australopithecus, Out-of-Africa)
- Indian sites (Bhimbetka, Mehrgarh, Burzahom, Chirand, Koldihwa, Daojali, Hunsgi, Panchmarhi, Jogimara, Inamgaon, Ahar, Jorwe, Malwa, Kayatha, Hallur, etc.)
- World sites (Lascaux, Olduvai)
- Concepts (rock/cave painting, petroglyph, domestication, pottery, pit house, fire)
- Pottery types (PGW, BRW, OCP)

Then manually filtered with the criterion: *"can this question be answered using (or is it primarily testing) the content we've built for the prehistoric era?"*

## Results: 2 confirmed matches / 2,839 PYQs

| PYQ | Year | Linked to | Notes |
|---|---|---|---|
| 68 | 2021 | `hist_burzahom`, `hist_neolithic_revolution` | "Burzahom Rock-cut shrines" pair — tests whether Burzahom is correctly described (it is not — Burzahom = Neolithic pit houses, not rock-cut shrines) |
| 128 | 2024 | `hist_inamgaon`, `hist_chalcolithic_period` | Multi-era pairs — pair 2 "Inamgaon (Maharashtra) — Chalcolithic site" is our era content |

## Rejected as false positives (keyword matched but question not actually about prehistoric)

| PYQ | Year | Why rejected |
|---|---|---|
| 149 | 2010 | "Cave paintings of the Gupta period" — ancient_classical, not prehistoric |
| 2184 | 2016 | Kharai Camel conservation — modern animal husbandry, not prehistoric domestication |
| 2177 | 2019 | New World plant domestication (tobacco/cocoa/rubber) — modern agricultural history |
| 37 | 2021 | Question tests tribal languages; "Pre-historic cave paintings" is a distractor option only |
| 75 | 2017 | Rigvedic vs Indus Valley — belongs to ancient_indus era |

## Saved for later eras

- 8 Indus/Harappan PYQs surfaced by the sweep are stashed in `eras/2.ancient-indus/_pyqs_from_prehistoric_sweep.json` for when that era begins.

## Conclusion

Prehistoric is genuinely a **low-yield era** for UPSC prelims: 2 confirmed PYQs across 30 years. This is expected — UPSC focuses on dynastic history, colonial, economy, polity, environment, current affairs. Prehistoric topics (stone age, human evolution, rock art) appear only occasionally, usually as one pair inside a multi-pair archaeological-sites question.

That said, the era is the **foundation** for everything ahead: it sets up Chalcolithic sites (which recur as distractors/correct options in later archaeology questions) and introduces the UPSC vocabulary around material-culture periods.

## Counts

- PYQs linked to prehistoric nodes: **2** (IDs 68, 128)
- PYQ-bearing nodes: 2 (`hist_burzahom`, `hist_inamgaon`, plus contextual links on `hist_neolithic_revolution` and `hist_chalcolithic_period`)
- PYQs saved for ancient_indus era: 8
- Overall: 2 / 2839 (~0.07%)
