# Reference Books Coverage — Prehistoric Era

## Books available in `raw/reference-books/`

| Book | Relevance to prehistoric | Action |
|---|---|---|
| Nitin Singhania — *Indian Art and Culture* | **Medium** — rock art / Bhimbetka / prehistoric paintings chapter | **Done** — Ch 2 (pp 192-250) processed via `pdftotext` |
| **R.S. Sharma — *India's Ancient Past*** (acquired 2026-04-17) | **High** — Ch 7 (Old Stone Age), Ch 8 (Neolithic), Ch 9 (Chalcolithic) | Ch 9 used to re-source Chalcolithic nodes; Ch 7-8 pending for augmenting existing Paleolithic/Neolithic nodes |
| Shankar IAS — *Environment* | Low | Skip |
| Laxmikanth — *Indian Polity* | None | Skip |
| Bipin Chandra — *India's Struggle for Independence* | None (modern history only) | Skip |
| Ramesh Singh — *Indian Economy* | None | Skip |
| *Constitution of India* | None | Skip |

## Nitin Singhania chapters to process

**Chapter 2: Indian Paintings — pages 192–250** (59 pages).
- Bhimbetka rock paintings section: around page 195
- Jogimara cave paintings: also in this chapter
- Chapter also covers later paintings (murals, miniatures) — we'll pull only prehistoric-relevant sections into this era's nodes; the rest will feed later eras (ancient_classical, early_medieval, etc.) when we reach them.

**Shortcut available:** this PDF has a text layer — `pdftotext` works directly, no OCR needed. Options:
1. Run `/ocr nitin_singhania 110` to process pages 86–195 via the OCR skill (catches up through the start of Bhimbetka section)
2. Use raw `pdftotext -f 192 -l 250` to extract the paintings chapter directly (faster, skips OCR entirely)

Current OCR progress: pages 56–85 done (Ch 1 Architecture).

## Books not available but standard for UPSC prehistoric

Consider acquiring (web search pending):
- **R.S. Sharma — *India's Ancient Past*** — standard reference for ancient history including prehistoric. Class 11 old NCERT was based on this.
- **Upinder Singh — *A History of Ancient and Early Medieval India*** — more detailed, possibly overkill

## Depth recommendation for this era

Prehistoric is NCERT-heavy in UPSC. Reference book contribution is small:
- 1 chapter from Nitin Singhania (rock paintings) — directly useful
- 0 from others

Resist the temptation to over-read. The exam's prehistoric questions are almost all site-identification or stage-identification — NCERT covers that.

## Processed

**Nitin Singhania — Chapter 2: Indian Paintings (pages 192-250)** — processed via `pdftotext` (PDF has text layer, OCR not needed).

Prehistoric-relevant sections extracted:
- Introduction to Pre-Historic Paintings
- Three phases (Upper Palaeolithic / Mesolithic / Chalcolithic) with color & theme distinctions
- Dedicated BHIMBETKA ROCK PAINTINGS section
- Secondary sites: Jogimara, Mirzapur, Panchmarhi, Narsinghgarh, Kanker/Koriya district sites
- Mural paintings introduction (for later — murals are ancient_classical territory, not prehistoric)

**4 nodes added** from this chapter:
- `hist_jogimara_caves` (place, Chalcolithic ~1000 BCE) — Chhattisgarh, world's oldest theatre room
- `hist_mirzapur_rock_paintings` (place, Mesolithic) — UP Vindhyan shelters
- `hist_panchmarhi` (place, Mesolithic) — MP Satpura range
- `hist_petroglyphs` (concept) — rock engravings (vs paintings)

**2 nodes augmented** with reference-book detail:
- `hist_bhimbetka` — V.S. Wakankar discovery (1957-58), UNESCO 2003, 100,000 BCE – 1000 CE continuity, "Zoo Rock Shelter" nickname, haematite/ochre pigments, three-phase classification
- `hist_rock_paintings` — three-phase breakdown with distinct colors/themes per phase, petroglyphs vs paintings distinction

## R.S. Sharma — processed 2026-04-17

**Ch 7: Human Evolution: The Old Stone Age**, **Ch 8: The Neolithic Age**, **Ch 9: Chalcolithic Cultures** all processed via `pdftotext`.

**17 existing nodes augmented** with Sharma-sourced detail:
- Period nodes: Lower/Middle/Upper Palaeolithic, Mesolithic, Neolithic, Chalcolithic — now carry Sharma's Indian-specific dates and defining characteristics
- Species nodes: Homo habilis, Homo erectus, Homo sapiens — braincase sizes, Sharma's "fire discovered by Homo erectus" note
- Concepts: Language origins (50,000 BCE), Stone tools (three regional Neolithic axe-types), Pottery, Domestication, Beginning of Agriculture
- Sites: Mehrgarh (Kochi plain, Bolan river, 5500 BCE flood, potter's wheel 4500 BCE), Burzahom ("place of birch", dog burials), Chirand (junction of 4 rivers, bone/antler tools), Bhimbetka (10 sq km, 45 km south of Bhopal)

**16 new nodes added** (from Ch 7 and Ch 8):

| Node | Era phase | Notes |
|---|---|---|
| Ramapithecus & Sivapithecus | pre-cultural | Siwalik hills, Potwar plateau, ~2.2 Mya |
| Hathnora (Narmada Man) | Lower Paleo | archaic H. sapiens skull, MP, 1982 discovery |
| Bori | Lower Paleo | earliest LP site in India, ~600,000 BCE |
| Soan Valley | Lower Paleo | Punjab/Pakistan, Acheulian |
| Belan Valley | Lower+Middle Paleo | UP Vindhyan foothills |
| Didwana (Paleo) | All 3 Paleo phases | Rajasthan, stratified site |
| Fa Hien Cave | Upper Paleo | Sri Lanka, earliest UP site in subcontinent |
| Bagor | Mesolithic | Rajasthan, earliest animal domestication |
| Adamgarh | Mesolithic | MP, earliest animal domestication |
| Sambhar | Mesolithic | Rajasthan salt lake, earliest plant cultivation |
| Gufkral | Neolithic | Kashmir, pairs with Burzahom |
| Piklihal | Neolithic | Karnataka, cattle-herders, ash mounds |
| Brahmagiri | Neolithic | Karnataka, southern Neolithic group |
| Maski | Neolithic | Karnataka, also Ashoka Minor Rock Edict site |
| Hallur | Neolithic | Karnataka, earliest iron in India ~1200 BCE |
| Senuwar | Neolithic | Bihar Rohtas, Kaimur hills |

**3 Chalcolithic site nodes** (added earlier, already Sharma-sourced):
- Inamgaon, Ahar, Kayatha — with Sharma Ch 9 detail

## Counts

- Reference chapters identified as relevant: 4 (Nitin Singhania Ch 2; Sharma Ch 7, 8, 9)
- Chapters processed: 2 (Nitin Singhania Ch 2; Sharma Ch 9)
- Nodes from reference material: 4 (Nitin Singhania) + 4 re-sourced from Sharma
- Existing nodes augmented: 2 (Bhimbetka, Rock Paintings from Nitin Singhania)
