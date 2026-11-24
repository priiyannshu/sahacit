# sahacit — Symbiotic Cognition (सहचित्)
### Vision & Philosophical Charter

> **Status**: Active Charter · **Repo**: `sahacit` (formerly `vu`)
> **Implementation Blueprint**: [`MASTER_PLAN.md`](MASTER_PLAN.md)
> **Historical Archive**: [`docs/archive/FOUNDATION_ORIGINAL.md`](archive/FOUNDATION_ORIGINAL.md)

---

## 1. The Soul of sahacit

**sahacit** (सहचित् — Symbiotic Cognition) is not a static content library, an online MOOC, or a generic chat assistant. It is a personal, lifelong cognitive institute built upon the university metaphor.

Everything the learner experiences maps to the living structure of a university:

| University Metaphor | System Role | Living Reality |
|---|---|---|
| **The Library** | Global Knowledge Catalog | Hierarchically structured knowledge (Dewey Decimal Classification) spanning OpenCourseWare, foundational curricula, and reference corpora. |
| **The Classroom / Studio** | The Interactive Workspace | The Jupyter Notebook (`.ipynb`) — a clean, distraction-free cell canvas for code, mathematical derivations, and Socratic inquiry. |
| **The Faculty** | Intelligent Pair Programmer & Tutor | Real-time Socratic feedback in the notebook (`jupyter-tutor` + CLI), coupled with deep overnight batch reasoning. |
| **The Student Journal** | Multimodal Thought Stream | Personal notes, hand-drawn paper sketches, and voice notes captured naturally alongside active work. |
| **The Registrar** | Personal State Engine | An evolving personal knowledge graph tracking conceptual mastery, individual metaphors, cognitive preferences, and forgetting curves. |

---

## 2. Core Pedagogical Principles

### 2.1 The Living Loop: Symbiotic Execution Over Passive Consumption
Deep understanding is forged through active friction, not passive video lectures or encyclopedic walls of text.
* **The Notebook as Substrate**: A notebook is simultaneously a session log, an experimental lab, and an unprocessed cognitive unit.
* **Immediate Verification**: When learning an abstract concept (e.g., backpropagation in neural networks), the learner derives it analytically and verifies it immediately via numerical computation and code execution.
* **The Cell Contract**: Markdown belongs to the human learner (notes, reflections, hypotheses). Code execution triggers the tutor to verify reasoning, answer questions, or challenge assumptions.

### 2.2 Canonical Facts vs. Personal Metaphors
Every human builds an internal model of the world out of metaphors.
* **Canonical Truth**: The objective, factual, mathematical reality of a discipline.
* **Personal Metaphors**: The unique mental analogies the learner uses to make sense of ideas (e.g., understanding an electric circuit as water pipes, or backprop as blame distribution).
* **Role of the System**: The university never forces sterile phrasing onto the learner. It adopts and refines the learner's own vocabulary while actively flagging flawed analogies before they calcify into misconceptions.

### 2.3 Progressive Knowledge Graphification
* **The Catalog is a Tree**: The university offers courses, lectures, and chapters organized in clear, hierarchical structures.
* **The Personal Mind is a Graph**: True mastery occurs when boundaries dissolve—when an algorithm in computer science connects to an optimization problem in economics or an intuition in physics.
* **The Transformation**: Knowledge starts as a structured tree in the library, passes through the learner's notebook, and crystallizes into a progressive personal Knowledge Graph in the Registrar.

```
Catalog (Hierarchical Tree) ──▶ Notebook (Active Session) ──▶ Personal State (Living Graph)
```

---

## 3. Multimodality & Natural Expression

### 3.1 Cognitive Modalities
Learning rarely happens in one format. **sahacit** accommodates the natural human workflow:
1. **Executable Code & Text**: CodeMirror 6 canvas for runnable code and formatted notes.
2. **Paper Sketches (The Paper KG)**: Hand-drawn concept maps and diagrams photographed and ingested into the digital knowledge graph.
3. **Voice & Spoken Thoughts**: Voice recordings ingested directly without requiring tedious manual transcription before comprehension.

### 3.2 Linguistic Register: English & Hinglish
Thought should not be constrained by rigid linguistic boundaries.
* Spoken voice notes and informal reflections fluidly support **Hinglish** alongside **English**, mirroring the natural conversational register of the learner.
* The system understands and respects code-switching, extracting rigorous concepts from colloquial dialogue.

---

## 4. The Twin Operational Cycles

The university operates across two complementary cadences:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        THE DAY CYCLE (Active)                          │
│                                                                        │
│  • The learner works in the notebook canvas.                           │
│  • Code and Socratic `#` questions execute instantly (sub-second).    │
│  • Real-time verification, numerical checks, and pair-programming.    │
│  • Voice thoughts (.mp3) and diagram photos logged in real time.       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                       THE NIGHT CYCLE (Reflective)                     │
│                                                                        │
│  • Notebook sessions and audio artifacts are deeply processed.         │
│  • Concepts, metaphors, and lingering doubts are extracted.            │
│  • Ebbinghaus forgetting curves update mastery scores.                 │
│  • Tomorrow's lecture trajectories and review notebooks are prepared.  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Engineering Architecture & Roadmap

For concrete schemas, component topology, implementation phases, and deliverables, refer to the active engineering blueprint:

👉 **[`MASTER_PLAN.md`](MASTER_PLAN.md)**
