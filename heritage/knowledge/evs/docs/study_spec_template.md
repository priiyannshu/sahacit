# Personal Learning Spec & Feedback Contract (Template)

This document serves as the "Anchor Spec" or "Steering Source" for the daily adaptive learning loop. The CLI AI writes to this file, the user adds reflections, and `nlm` uploads it to steering-guide the NotebookLM generation for the next cycle.

---

## 1. Meta Parameters & Context
* **Current Date:** {{date}}
* **Current Core Topic:** {{core_topic}}
* **Current Cognitive Level (Bloom's Taxonomy Target):** [Application / Analysis / Synthesis / Evaluation]
* **Target Audience Persona:** [Expert Practitioner / Conceptual Beginner / Skeptical Researcher]

---

## 2. Ingestion Scaffolding (Active Sources)
List of sources the synthesizer is directed to focus on for this run:
1. `source_1.pdf` (Primary Focus)
2. `source_2.url` (Secondary context)

---

## 3. Cognitive Baseline (Yesterday's Knowledge State)
* **What I understand well:**
  * [Concept A]
  * [Concept B]
* **What is still high-entropy (confusing/unresolved):**
  * [Concept C - specifically why X leads to Y]
  * [Concept D - how this integrates with yesterday's thesis]

---

## 4. Today's Steering Directives
Instructions to the synthesis engine on how to shape today's artifacts (Briefing Docs, FAQs, Audio Overviews):
* **Steering Prompt:** 
  > *"Focus heavily on resolving the confusion around Concept C. Do not repeat basic definitions for Concept A. Keep the technical depth high and use LaTeX notation for mathematical proofs."*
* **Tone & Speed for Audio Overview:** [Fast-paced, highly technical, debate-style / Conversational, example-heavy]
* **Artifacts to Generate:**
  * [x] Study Guide
  * [x] Entailment Mesh (Concept Map)
  * [ ] FAQ
  * [x] Steered Audio Overview

---

## 5. Daily Feedback Log (Reflections Recorded Today)
*As you study today, write or speak your notes here. The CLI pipeline will scrape these notes to compute tomorrow's spec:*
* **Reflections & Thoughts during study:**
  * *"I noticed that when we compressed Concept D, it looked like a classic Shannon entropy minimization problem, but Pask's conversation theory applies better to how the machine adapts to it."*
* **Areas of Friction (Noise):**
  * *"The math on channel capacity in source 2 was too dense without a step-by-step breakdown."*
