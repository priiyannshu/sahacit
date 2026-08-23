# CTET Paper-1 EVS (Non-Pedagogical 15 Marks) Download Manifest & Ingestion Guide

This document lists all canonical sources, direct download links, NCERT book codes, high-yield chapters, and structured reference data needed to prototype the pipeline for NotebookLM, audio/video generation, and interactive PWA notes.

---

## 1. Core Primary Textbooks (NCERT Class 3 to 5)
> **Yield**: Accounts for ~85–90% of all content questions (13–14 out of 15 marks).

### Official Access Portal
* **NCERT Textbooks Portal**: [https://ncert.nic.in/textbook.php](https://ncert.nic.in/textbook.php)
* **ePathshala Portal**: [https://epathshala.nic.in/](https://epathshala.nic.in/)

### Download Matrix

| Grade | Subject & Book Title | NCERT Code (English) | NCERT Code (Hindi) | Total Chapters | Priority High-Yield Chapters |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Class 3** | EVS: *Looking Around* / *आस-पास* | `ceap1` | `chap1` | 24 | Ch 3 (*Water O' Water*), Ch 14 (*The Story of Food*), Ch 16 (*Games We Play*), Ch 18 (*Too Much Water, Too Little Water*), Ch 24 (*Web of Life*) |
| **Class 4** | EVS: *Looking Around* / *आस-पास* | `deap1` | `dhap1` | 27 | Ch 1 (*Going to School*), Ch 2 (*Ear to Ear*), Ch 3 (*A Day with Nandu*), Ch 4 (*The Story of Amrita*), Ch 7 (*From the Window*), Ch 11 (*The Valley of Flowers*), Ch 16 (*A Busy Month*), Ch 20 (*Eating Together*), Ch 23 (*Pochampally*), Ch 24 (*Home and Abroad*) |
| **Class 5** | EVS: *Looking Around* / *आस-पास* | `eeap1` | `ehap1` | 22 | Ch 1 (*Super Senses*), Ch 2 (*A Snake Charmer’s Story*), Ch 3 (*From Tasting to Digesting*), Ch 5 (*Seeds and Seeds*), Ch 6 (*Every Drop Counts*), Ch 7 (*Experiments with Water*), Ch 8 (*A Treat for Mosquitoes*), Ch 9 (*Up You Go!*), Ch 10 (*Walls Tell Stories*), Ch 11 (*Sunita in Space*), Ch 13 (*A Shelter so High!*), Ch 20 (*Whose Forests?*) |

---

## 2. Supplementary Bridge Chapters (NCERT Class 6)
> **Yield**: Accounts for the remaining 10–15% (1–2 recurrent questions per paper on nutrition, plant parts, map directions, and scales).

| Subject & Grade | NCERT Book Code | Target Chapter Title | Specific Concept Tested in CTET |
| :--- | :--- | :--- | :--- |
| **Class 6 Science** | `fesc1` | *Components of Food* | Nutrients, starch/protein tests, vitamins & deficiency diseases (Scurvy, Rickets, Beriberi, Goitre, Anaemia). |
| **Class 6 Science** | `fesc1` | *Getting to Know Plants* | Taproots vs fibrous roots, reticulate vs parallel venation, transpiration, and leaf parts. |
| **Class 6 Science** | `fesc1` | *Water* & *Living Organisms and their Surroundings* | Water cycle, evaporation, condensation, habitat adaptations (Cactus, Camel, Fish). |
| **Class 6 Geography** | `fess2` | *Maps* | Cardinal directions, distance scale calculations, symbols, and Indian coordinate grids. |

---

## 3. Past Year Benchmark Question Papers (PYQ Corpus)
> **Purpose**: Grounding truth for NotebookLM, dynamic quiz generation in PWA, and prompt style calibration.

### Official Portal
* **CTET Official Archives**: [https://ctet.nic.in/archive/](https://ctet.nic.in/archive/)

### Recommended Target Sets (Questions 61 to 75 only)
1. **CTET July 2024 / Jan 2024 Paper-1 (Offline Set A/B/C/D)**
2. **CTET August 2023 Paper-1 (Offline)**
3. **CTET Dec 2022 / Jan 2023 (CBT Online Shifts — pick 5-10 distinct dates)**
4. **CTET Dec 2021 / Jan 2022 (CBT Online Shifts — pick 5-10 distinct dates)**
5. **CTET Dec 2019 & Dec 2018 Paper-1**
* *Accompanying Artifacts*: Official Final Answer Keys for each set.

---

## 4. Curated Ground-Truth Fact & Entity Cheat Sheet

Include this text directly as a source in NotebookLM to ensure zero hallucination across the 6 themes.

```markdown
# CTET EVS Core Content Ground Truth (6 Themes)

### Theme 1: Family & Friends (Animals & Plants)
- **Sloth**:
  - Resembles a bear, sleeps ~17 hours a day hanging upside down on tree branches.
  - Lives for about 40 years; moves to only about 8 trees in its lifetime.
  - Comes down once a week to relieve itself; excellent swimmer.
- **Asian Elephant**:
  - Herd is led by the oldest female (10-12 females and young calves).
  - Adult elephant eats >100 kg of leaves and twigs in a single day.
  - Sleeps only 2 to 4 hours a day; mud and water keep their skin cool; big ears flap like fans.
  - Male elephants stay in the herd only until 14-15 years of age.
- **Tiger**:
  - Night vision is 6 times better than humans.
  - Sensitive whiskers sense movements and vibrations in air (helps hunt in the dark).
  - Roar can be heard up to 3 km away; marks area with urine.
- **Poisonous Snakes of India**:
  - Only 4 types: Spectacled Cobra (नाग), Common Krait (करैत), Russell's Viper (दुबोइया), Saw-scaled Viper (अफ़ई).
  - Two hollow teeth (fangs); anti-venom is made from snake venom.
- **Desert Oak**:
  - Found in Australia; leaves are few; roots reach ~30 times deep into ground until water table.
  - Water is stored in its trunk; locals use thin pipes/straws to drink.
- **Pitcher Plant (Nepenthes)**:
  - Found in Australia, Indonesia, and Meghalaya (India).
  - Traps and consumes frogs, insects, and mice using a pleasant scent (not sound).
- **Khejadi Tree**:
  - Found mainly in desert areas (Rajasthan / Bishnoi community); needs very little water.
  - Bark used for medicine; wood is insect-resistant; beans eaten as vegetables.

### Theme 2: Food & Digestion
- **Ling-hu-fen**: Snake meat delicacy eaten in Hong Kong.
- **Tapioca & Coconut Curry**: Eaten with boiled tapioca (Kappa) with coconut curry in Kerala.
- **Fish in Oils**:
  - Fish cooked in mustard oil: Kashmir.
  - Sea fish cooked in coconut oil: Goa.
- **Assam Foods & Bihu**:
  - *Bora* and *Cheva*: Sticky rice varieties cooked in cauldron (*Kadhahi*).
  - *Bhelaghar*: Temporary shelter made of bamboo and thatch for community feast (*Uruka*).
- **Digestion Experiments**:
  - Dr. William Beaumont studied stomach digestion on soldier Alexis St. Martin.

### Theme 3: Shelter & Architecture
- **Leh & Ladakh**:
  - Two-storey houses made of stone coated with thick mud and lime; flat wooden roofs made of poplar tree trunks.
  - Ground floor has no windows; used for animals and winter storage; roof used for drying vegetables/fruits.
- **Kashmir**:
  - *Houseboats* (up to 80 ft long), *Donga* (boats on Dal lake/Jhelum).
  - *Khatamband*: Woodwork puzzle carvings on ceilings.
  - *Mehraab*: Beautiful arches on doors/windows.
- **Assam**:
  - Houses built 10 to 12 feet above the ground on strong bamboo pillars due to heavy rains.
- **Manali / Himachal**:
  - Stone and wood houses with sloping roofs.
- **Rajasthan**:
  - Mud houses with thick walls and thatched roofs of thorny bushes (*Keekar*).

### Theme 4: Water & Discoveries
- **Al-Biruni**: Traveler from Uzbekistan who documented 11th-century Indian stepwells (*Bawris*) and ponds.
- **Ghadsisar Lake**: Built by King Ghadsi of Jaisalmer (consists of 9 interconnected lakes).
- **Ronald Ross**: Discovered in 1902 that malaria is transmitted by the female *Anopheles* mosquito.
- **Anaemia Remedy**: Jaggery (गुड़), Amla, and green leafy vegetables (rich in Iron).

### Theme 5: Travel, Space & Mountaineering
- **Bachendri Pal**: First Indian woman (and 5th in world) to reach Mount Everest (*Sagarmatha* - 8848m) on 23 May 1984.
- **Changpa Tribe & Pashmina**:
  - Changpa: Nomadic tribe of Ladakh living in cone-shaped tents called *Rebo* at 5000m altitude.
  - *Changthangi* goats live at -40°C; their fine underfur makes Pashmina shawls (warmth of 6 normal sweaters; takes 250 hours of hand weaving).
- **Suryamani & Girl Stars**:
  - Tribal activist from Jharkhand; founded *Torang* center to preserve Kudukh language and forest culture.

### Theme 6: Traditional Crafts & Geography
- **Pochampally & Kalamkari**: Traditional woven cloth / sarees from Telangana / Andhra Pradesh.
- **Madhubani Painting**: Folk art from Bihar; made from paste of powdered rice mixed with natural colors (indigo, turmeric, flowers).
- **Direction & Coastlines**:
  - *Arabian Sea Coastal States*: Gujarat, Maharashtra, Goa, Karnataka, Kerala.
  - *Bay of Bengal Coastal States*: West Bengal, Odisha, Andhra Pradesh, Tamil Nadu.
```

---

## 5. Recommended Directory Layout for Your Pipeline

```
evs/
├── DOWNLOAD_LIST.md                  <-- This master reference
├── data/
│   ├── raw_ncert/
│   │   ├── class_3_looking_around/   # PDFs
│   │   ├── class_4_looking_around/   # PDFs
│   │   ├── class_5_looking_around/   # PDFs
│   │   └── class_6_bridge/           # Science & Geo chapters
│   ├── pyq_benchmark/
│   │   ├── ctet_2021_2024_content/   # Extracted Q61-Q75 items
│   │   └── answer_keys/
│   └── knowledge_matrix/
│       └── evs_fact_matrix.md        # Seed grounding document
├── notebooklm_artifacts/
│   ├── audio_overviews/              # Generated audio/podcasts
│   ├── transcripts/                  # Clean text dumps
│   └── image_prompts/                # Prompts for visual assets
└── pwa_frontend/
    ├── public/audio/                 # Streamed audio overviews
    └── src/notes/                    # Interactive HTML / Markdown widgets
```
