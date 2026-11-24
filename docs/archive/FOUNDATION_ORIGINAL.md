# Virtual University — Foundation

> **Created**: 2026-08-23 · **Repo**: `vu` · **Status**: Architectural seed
> This document is deliberately lean. It captures enough to start building the library and the ritual journey. The full vision grows as we build.

---

## 1. The Metaphor

The application is a **Virtual University**. Everything the user interacts with maps to a university concept:

| Real University | Virtual University | System Role |
|---|---|---|
| **Library** | The global knowledge store | All processed source material, organized by Dewey Decimal Classification |
| **Courses** | Learning trajectories | Generated from library material, personalized per learner |
| **Lectures / Notes** | Daily generated content | Produced nightly based on strategy + learner state |
| **Student journal** | Audio thought capture | Ambient + explicit recordings throughout the day |
| **Registrar** | Personal state engine | Tracks mastery, metaphors, doubts, psych profile |
| **Faculty** | The nightly pipeline | Processes student input, updates notes, generates next day |
| **Admissions** | The ritual journey (Classes 1–10) | Calibration phase that builds the learner's contextual world |

---

## 2. The Library (Global Knowledge State)

### 2.1 Organization: Dewey Decimal Classification

All knowledge in the system is mapped to the **Dewey Decimal Classification (DDC)** system. This provides:

- A universal, hierarchical, well-understood taxonomy
- Natural categorization for Indian govt source material
- Extensibility as new subjects / exams are added

**Initial DDC mapping for Classes 1–10 NCERT corpus:**

| DDC Class | Range | Relevant NCERT Subjects |
|---|---|---|
| 000 | Computer Science, Information | Computer literacy (Class 6+) |
| 100 | Philosophy & Psychology | Moral science, value education |
| 200 | Religion | — (not in NCERT secular curriculum) |
| 300 | Social Sciences | Social Studies, Civics, Economics, EVS (social) |
| 400 | Language | Hindi, English, Sanskrit |
| 500 | Science | Science, Mathematics, EVS (natural) |
| 600 | Technology | Applied science chapters |
| 700 | Arts & Recreation | Art education, physical education |
| 800 | Literature | Hindi/English literature, poetry |
| 900 | History & Geography | History, Geography, map skills |

### 2.2 Source Material

**Phase 1 sources** — Indian Government educational material, Classes 1–10:

- **NCERT textbooks** (all subjects, all classes)
- **State board equivalents** where NCERT gaps exist
- **EVS (Environmental Studies)** — Classes 1–5 (already processed in `preach/evs/`)

The library displays source material categorically. Raw data sources that were processed remain browsable — the user can always see _where_ knowledge came from.

### 2.3 Processing Pipeline

Source → Library follows the zero-loss methodology proven in `preach/evs/`:

1. **Deterministic extraction** — atomic factual schemas per chapter
2. **Entity ledger** — every concept catalogued with bilingual anchoring
3. **Verification gates** — keyword diffing, PYQ back-testing, zero-orphan audit
4. **DDC classification** — each extracted entity tagged with its Dewey number

---

## 3. Courses (Learning Trajectories)

### 3.1 Course Lifecycle

A course does **not** exist fully generated when created. It follows this lifecycle:

```
CREATE → STRATEGIZE → WEEKLY TRAJECTORY → NIGHTLY GENERATION → DAILY LEARNING
```

1. **Creation**: A course is instantiated from a library subset (e.g., "Class 3 EVS" or "Indian Polity fundamentals")
2. **Strategy**: Deterministic code harnesses + human oversight define the pedagogical arc — what concepts in what order, at what depth, with what dependencies
3. **Weekly trajectory**: Each week's learning path is computed — which topics, which progression, what milestones
4. **Nightly generation**: Each night, the next day's content is generated based on:
   - The weekly trajectory plan
   - The learner's personal state (updated from today's audio)
   - Doubts identified → addressed in updated notes
   - Metaphor corrections → woven into new explanations
5. **Daily learning**: The learner engages with generated content and records thoughts

### 3.2 Content Generation — Gemini NotebookLM

All learning content is generated through **Gemini NotebookLM**, which produces:

- Audio overviews / conversational podcasts (steered with manifests)
- Study guides and structured notes
- Visual aids (diagrams, mind maps)
- Formative checks / inline questions

NotebookLM is the content engine. It does NOT interact with the learner in real-time. It generates artifacts that the learner consumes.

### 3.3 Strategy — Deterministic + Human-in-Loop

Course strategy is NOT AI-driven. It is:

- **Code harnesses**: deterministic pipelines that sequence concepts based on dependency graphs, DDC hierarchy, and pedagogical principles
- **Weekly human oversight**: the system operator (you) reviews and adjusts weekly trajectories via in-app questionnaires
- **Learner intent funneling**: weekly in-app questionnaires capture what the learner wants to focus on, what felt hard, what felt easy

Over time, the deterministic pipelines mature to the point where they only require the weekly learner questionnaire input to produce the next week's trajectory.

---

## 4. The Daily Cycle (No Real-Time AI)

The fundamental UX loop is **asynchronous**. There is no real-time AI chat, no live Socratic tutor, no instant-response LLM.

```
╔═══════════════════════════════════════════════════════════════╗
║                        ONE DAY                                ║
║                                                               ║
║  MORNING                                                      ║
║  ├─ Learner opens app                                        ║
║  ├─ Yesterday's doubts → addressed in updated notes          ║
║  ├─ New content generated overnight is ready                 ║
║  └─ Metaphor corrections woven into today's material         ║
║                                                               ║
║  DAY (learning time)                                          ║
║  ├─ Learner engages with generated content                   ║
║  ├─ Audio capture: AMBIENT mode (always-listening companion) ║
║  ├─ Audio capture: EXPLICIT mode (tap to record a thought)   ║
║  └─ All audio queued locally throughout the day              ║
║                                                               ║
║  NIGHT (pipeline runs)                                        ║
║  ├─ Audio queue → transcription (speech-to-text)             ║
║  ├─ Transcripts → LLM reasoning pass                        ║
║  │   ├─ Extract: doubts, confusions, "aha" moments           ║
║  │   ├─ Extract: personal metaphors (how they describe it)   ║
║  │   ├─ Update: learner personal state                       ║
║  │   └─ Flag: metaphor corrections needed                    ║
║  ├─ Updated state + weekly trajectory → generate Day N+1     ║
║  └─ Content artifacts placed for morning consumption         ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

### Why no real-time AI?

- **Quality over speed**: overnight processing can use stronger models, longer reasoning, more context
- **Learner reflection**: real-time answers short-circuit the struggle that builds understanding
- **Cost efficiency**: batch processing is dramatically cheaper than per-interaction inference
- **The teacher metaphor**: a good teacher listens all day, reflects overnight, comes back tomorrow with better notes — not instant answers

---

## 5. The Ritual Journey (Classes 1–10)

### 5.1 Purpose

Before learning "truly unknown things," the system needs to build an accurate model of the learner. The Classes 1–10 journey is **not** about teaching — it's about **calibration and extraction**:

- **Contextual world**: what does the learner already know? What's their frame of reference?
- **Metaphors**: how do they describe concepts? What analogies do they naturally reach for?
- **Metaphor corrections**: where are their intuitive models _wrong_? Establish correct foundations now.
- **Learning patterns**: how fast? What modalities work? When do they get confused?
- **Doubt patterns**: what kinds of things trip them up?

### 5.2 Pace

**~1–2 months total.** One class level per week, deliberate engagement.

| Week | Class Level | Focus |
|---|---|---|
| 1 | Class 1–2 | Baseline extraction. Language, basic numeracy, environmental awareness |
| 2 | Class 3 | EVS spiral begins. Factual entity extraction at learner level |
| 3 | Class 4 | Deeper EVS. Social structures, geography, basic science |
| 4 | Class 5 | EVS completion. History threads, civic concepts |
| 5 | Class 6 | Subject specialization begins. Separate Science, Social Studies, Maths |
| 6 | Class 7 | Intermediate concepts. Abstract reasoning emerges |
| 7 | Class 8 | Complex topics. Constitution basics, chemical reactions |
| 8 | Class 9 | Pre-board depth. Formal proofs, historical analysis |
| 9 | Class 10 | Board-level synthesis. Full subject integration |
| 10 | Assessment | Psych/behavioral/intelligence profiling. Personal state finalization |

### 5.3 Profiling Tests

Interspersed through the ritual journey:

- **Learning style assessment** — visual / auditory / kinesthetic preferences
- **Cognitive load tolerance** — how much complexity before confusion
- **Prior knowledge mapping** — surprising gaps or unexpected strengths
- **Metacognitive awareness** — does the learner know what they don't know?

Output: a robust **personal state** that all future course generation builds upon.

---

## 6. The Personal State

The personal state is the system's model of the learner. It is updated every night.

**Components:**

| Component | Source | Purpose |
|---|---|---|
| **Mastery map** | Daily engagement + nightly analysis | What concepts are known, learning, unknown |
| **Metaphor registry** | Audio extraction + correction | How the learner understands concepts, in their own words |
| **Doubt log** | Audio extraction | What confuses them — addressed in next day's content |
| **Learning velocity** | Engagement patterns over time | How fast they absorb different types of material |
| **Modality preferences** | Profiling tests + engagement data | Audio vs. visual vs. text preferences |
| **Cognitive profile** | Psych/behavioral tests | Working memory, attention patterns, abstraction level |
| **Intent history** | Weekly questionnaires | What they want to learn, shifting interests |

---

## 7. Language

**English + Hinglish.**

Not pure Hindi in Devanagari. Hinglish — the natural spoken register of urban/semi-urban Indian learners — is the second language of the app.

- UI chrome: English
- Content: English with Hinglish explanations where natural
- Audio capture: accepts English, Hindi, and Hinglish (the transcription pipeline must handle code-switching)
- Generated content: can be in either register based on learner preference / detected language use

---

## 8. Government Exam Integration

Government of India exam syllabuses serve as the **starting global state** — the library's initial catalog.

The DDC-organized library is seeded by mapping exam syllabuses to Dewey classes:

- **UPSC** (Civil Services) → spans DDC 100–900 (broadest)
- **SSC** → DDC 300, 400, 500, 900 primarily
- **Banking** → DDC 300 (economics, reasoning), 500 (quant)
- **State PSCs** → regional variants of UPSC mapping
- **CTET** → DDC 100 (child psychology), 300 (social studies), 500 (science/math), 400 (language)

Exam syllabuses define what the library _must_ contain. The ritual journey (Classes 1–10) builds the _foundation_ that all exam-specific learning is scaffolded upon.

---

## 9. Two LLM Domains (Separation of Concerns)

| Domain | Engine | Interaction Model | Human Role |
|---|---|---|---|
| **Content Generation** | Gemini NotebookLM | Batch. Nightly. Steered by manifests. | Review output quality periodically |
| **Strategy & Orchestration** | Deterministic code + weekly human input | Pipelines. Weekly cycle. Learner questionnaires. | Active weekly oversight, intent funneling |

These two domains do NOT mix. Content generation never makes strategic decisions. Strategy never generates learning material. The boundary is strict.

---

## 10. What Carries Forward from `22` and `preach`

### From `22` (archived as reference):
- **D1 knowledge data**: 7,547 master_nodes, edges, PYQ corpus → seeds the library's DDC 300/900 sections
- **Personal metaphor concept** → now extracted via audio pipeline instead of session-end LLM calls
- **Spaced repetition / forgetting curves** → inform the mastery map component of personal state
- **Cloudflare edge infra patterns** → Workers, D1, R2 remain relevant

### From `preach`:
- **Zero-loss extraction pipeline** → the methodology for building the library from NCERT sources
- **EVS processed corpus** → 77 chapters already extracted, verified, bilingual-anchored (Classes 3–6)
- **NotebookLM tooling research** → `notebooklm-py` and `notebooklm-mcp-cli` already evaluated
- **Thematic spiral synthesis** → informs course structure design

---

## 11. What's NOT Decided Yet

- [ ] **Nightly pipeline infrastructure** — where it runs (local / cloud / hybrid). TBD.
- [ ] **App platform** — PWA? Native? React Native? Flutter?
- [ ] **Storage architecture** — D1 again? Postgres? SQLite local-first?
- [ ] **Audio handling** — on-device processing? Cloud transcription API? Local Whisper?
- [ ] **Deployment topology** — edge-first (Cloudflare) vs. traditional server vs. hybrid
- [ ] **Exam-specific course design** — how exam syllabuses map to course creation UX

These will be decided as we build, not upfront.
