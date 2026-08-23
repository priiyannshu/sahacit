# CTET EVS Zero-Loss Extraction & Synthesis Pipeline

This document serves as the master execution plan for processing the raw NCERT corpus into downstream-ready thematic artifacts. This ensures the raw textbooks become 100% redundant while providing steering documents for NotebookLM and Hyperframes HTML video generation.

## 1. The 7 Thematic Spiral Units
The raw NCERT chapters (Class 3 to 6) and CTET PYQs (2018-2024) will be synthesized into these 7 Master Units:
1. **Unit 1: Living World, Animal Behavior & Adaptations**
2. **Unit 2: Flora, Seeds, Forest Rights & Agriculture**
3. **Unit 3: Food, Digestion, Cooking & Vector Diseases**
4. **Unit 4: Shelter, Architecture & Climatic Adaptations**
5. **Unit 5: Water Systems, Conservation & Historical Science**
6. **Unit 6: Travel, Culture, Traditional Arts & Space**
7. **Unit 7: Quantitative & Spatial Bridge (Map scales, direction, time/speed)**

---

## 2. Execution Sprints (For Subagents)

### Sprint 1: Deterministic Extraction (The Ingestion Ledger)
**Goal:** Parse all 77 NCERT chapters into atomic JSON/YAML factual schemas.
- **Action:** Spawn parallel subagents to process raw PDFs (`evs/raw/ncert_textbooks/`).
- **Output:** A strict extraction schema for each chapter containing:
  - `factual_entities` (e.g., Sloth, Tiger, Khejadi tree)
  - `historical_figures_and_travelers`
  - `geographical_locations_and_tribes`
  - `scientific_experiments_and_processes`
  - `cultural_customs_foods_and_tools`
  - `numerical_data_and_measurements`
  - `visual_assets_and_diagram_cues`
- **Verification:** Generate `LEDGER.md` to track the extraction status of all 77 chapters.

### Sprint 2: Master Ledger & Coverage Audit Matrix
**Goal:** Prove zero-loss before synthesis begins.
- **Action:** Extract all CTET PYQs (2018–2024 content questions) and categorize them into the 7 themes.
- **Action:** Run a keyword/entity diffing script to ensure every term in the raw PDFs is captured in the extracted ledger.
- **Gate:** Pass the **100% PYQ Back-Testing** rule (every PYQ must be solvable using *only* the extracted ledger facts).

### Sprint 3: Thematic Spiral Synthesis (Artifact Generation)
**Goal:** Compile the ledger facts into the 7 Master Markdown Artifacts.
- **Action:** Subagents generate the 7 `unit_X.md` files.
- **Format:** Each artifact must include:
  1. Encyclopedic Theory & Concept Evolution (Spiral progression)
  2. Zero-Hallucination Entity Vault
  3. Hyperframes HTML Video Storyboards & Scene Specs (CSS/Timeline cues)
  4. NotebookLM Audio Overview Steering Cue Cards
  5. Formative Inline PYQ Grounding Bank

### Sprint 4: Multi-Modal Downstream Integration
**Goal:** Wire the artifacts to downstream generators.
- **Action:** Pass the steered cue cards to NotebookLM via programmatic API (`notebooklm-py` or `notebooklm-mcp-cli`) to generate localized Audio Overviews and podcasts.
- **Action:** Feed the Hyperframes specs to the UI framework to generate interactive HTML videos and visual state machines.
- **Action:** Generate 15-mark full-spectrum mock exams drawing randomly from the 7 units for interactive PWA quiz widgets.

---

## 3. The 4-Way Redundancy & Verification Gate
Before closing this pipeline, the following conditions must be met to safely deprecate the raw NCERTs:
1. **Chapter-to-Unit Ledger Check:** 100% of the 77 chapters are marked 'Synthesized'.
2. **Keyword Diffing:** 0 orphaned entities (no concept present in raw PDF that is missing in artifacts).
3. **100% PYQ Back-Testing:** 100% of PYQs are answerable purely from the generated artifacts.
4. **Bilingual Anchor:** Technical/Cultural terms are captured in both English and Hindi.
