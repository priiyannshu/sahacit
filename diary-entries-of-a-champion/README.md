# Diary Entries of a Champion

Daily study log, ideation workspace, and structured ingestion ledger targeting **UPSC Prelims (23 May 2027)**.

## Directory & Ownership Convention

- **Dated Workspace (`YYYY-MM-DD/`)**: One folder per IST study day (e.g., `2026-11-25/`).
  - `entry.md` — **Canonical daily log** (structured YAML frontmatter + concise Markdown) built for downstream software (Study Time Recorder analytics, weekly/monthly evaluator, and 2027 AI Examiner Board).
  - Subfolders as needed for that day's ideation, manifests, or diagnostics (e.g., `book-and-booklets/`, `character-sheets/`, `timeline-badges-and-cutouts/`, `digital/`, `ai-examiner-board/`, `CSAT_First_Attempt/`, `GS_First_Attempt/`).
- **Canonical Artifact Boundary**:
  - `diary-entries-of-a-champion/YYYY-MM-DD/` holds **daily logs, ideas (`idea.md`), planning manifests (`output.md`), ingestion logs, and diagnostics**.
  - `booklets/` (at repo root) holds **canonical reproducible print generators and final PDFs**.
  - `apps/` (at repo root, Phase 2 / when requested) holds **downstream software applications**.

---

## Agent Interview Protocol (When Inside This Directory)

Whenever a session takes place in `diary-entries-of-a-champion/` (or a dated folder), the agent should **ask the user concisely** for any missing daily log details needed to populate or update `YYYY-MM-DD/entry.md`:

1. **Study Time**: Total hours/minutes studied today, plus any session breakdown (printed reading, memorization, PYQ observation, college commitments).
2. **Material Ingested**: Which printed books, booklets, dictionaries, character sheets, or timeline packets were studied—scope/pages, repetition `pass_number`, which of the **7 UPSC categories** apply, and digital mirror path (if tracked).
3. **PYQ Observations (if any)**: Any past paper explored today and patterns, trap structures, or multi-category conjunctions noticed.
4. **New Print Ideas / Gaps**: Any new printable artifacts or revisions identified while studying.

> **2026 Phase Guardrail**: Through the end of 2026, focus stays on building the multi-hour daily reading/memorization habit with printed artifacts and occasional PYQs for observations. **Do not push CSAT Maths or AI Examiner Board workflows during 2026.** Never fabricate unprovided minutes, scores, or pages—use `null` or ask.

---

## Standard Daily `entry.md` Schema

Every daily `entry.md` uses **YAML frontmatter** followed by clean human-readable sections:

```yaml
---
date: "YYYY-MM-DD"
phase: "2026-print-habit" # or "2027-consolidation"
target_exam: "UPSC Prelims 2027-05-23"
study_time:
  total_minutes: null # integer; e.g., 360
  college_minutes: 0 # optional integer
  sessions:
    - topic_or_artifact: ""
      minutes: null
      mode: "printed-read" # printed-read | memorization | pyq-observation | build | other
ingested:
  - title: ""
    categories: [] # Environment and Ecology | Economics | History and Art and Culture | Geography | Current Affairs | Science and Technology | Polity
    medium: "printed" # printed | digital | audio
    digital_mirror: null # repo path to digital source, e.g., booklets/...
    scope: "" # pages, sections, or count covered
    pass_number: 1 # repetition count for spaced-retention tracking
pyq_sessions: []
  # - paper: "2026 GS Paper 1"
  #   purpose: "pattern-observation" # pattern-observation | timed-mock | diagnostic
  #   attempted: null
  #   correct: null
  #   wrong: null
  #   conjunctions_or_patterns: []
new_print_ideas: []
tags: []
---

# Daily Log — YYYY-MM-DD

## Study Time & Rhythm
- Total studied: ...

## Content Ingested (Print & Digital)
- ...

## PYQ Observations & Patterns (if any)
- ...

## Reflections & Next Session
- ...
```

### Valid 7-Category Labels
Use exact canonical names when tagging `categories`:
1. `Environment and Ecology`
2. `Economics`
3. `History and Art and Culture`
4. `Geography`
5. `Current Affairs`
6. `Science and Technology`
7. `Polity`
