# Design Decisions Surfaced by A + B Drafts

*Companion to A_branch_taxonomy.md and B_eras_timeline.md.*
*Read these three together. This document is the user-facing summary of what the drafts forced into the open.*

The three planning-round tensions and their current status after drafting:

## Tension 1: Lens orthogonality — RESOLVED by drafting

**Original question:** Are pre-AI/post-AI, big-bang origin, and cross-subject metaphor *toggleable alternative views* or a *single layered narrative*?

**Resolution:** Single layered narrative. The era timeline (B) makes pre-AI/post-AI a natural fold-line *on the era spine itself*, not a separate canvas. The big-bang origin is honored by treating Era 1 with disproportionate depth. The cross-subject metaphor lens (future artifact D) will, by extension, also be a cell-annotation layer, not a separate canvas.

**Implication:** the surface is one canvas with stackable annotation layers. Toggle layers on/off, do not toggle canvases.

## Tension 2: Branch-vs-era primacy — RESOLVED by drafting

**Original question:** Era-primary (like history) or branch-primary (like polity)?

**Resolution:** Neither. **Both axes are primary.** The natural data structure is a `branch × era` matrix, where each cell holds "what this branch looked like in this era." The user can read by row (one branch through time — e.g., "Networks across all 8 eras") or by column (one era across all branches — e.g., "what was being invented in 1948-1972").

**Implication:** the surface needs a 2D navigation primitive, not a 1D scroll. This is a structural departure from history (era-scroll) and polity (chapter-scroll).

## Tension 3: Depth-of-coverage budget — STILL OPEN

**Original question:** "Every branch gets a node, only N get full descent" — which N, and how to pick?

**Status:** A surfaces three plausible rules (Fork A3):
- **Frontier-first** — descend only into *alive* branches
- **Love-first** — user picks ~10-12 branches by love, regardless of vitality
- **Coverage-first** — at least one full-descent per trunk for proportional representation

**Recommendation:** Love-first, consistent with the project's framing. **Needs user to actually pick the list before any per-branch work starts.**

---

## New decisions that drafting created

### D1: Is AI a trunk or a lens? (Fork A1)

This draft makes it a trunk with acknowledged seepage. Alternative: make it a fifth cross-cutting lens like Security, dissolving "Intelligence" into the other trunks. The trunk choice honors how practitioners speak; the lens choice honors how AI actually behaves in the field.

### D2: Vitality tags — visible filter or decoration? (Fork A2)

Tags are useful only if exposed as a filter. Otherwise drop them. If exposed: the surface gains a "what should I obsess over now" signal. If dropped: the surface is timeless and ages better.

### D3: Software engineering — lens or trunk? (Fork A4)

Lens-mode means SWE never gets a front page. Trunk-mode means it does. The user's relationship to SWE-as-craft determines this.

### D4: Era boundaries — technology or culture? (Fork B4)

Draft uses technological-availability boundaries (Turing 1936, transistor 1947, ARPANET 1969, AlexNet 2012). Cultural-adoption boundaries would shift several (e.g., 2022 ChatGPT instead of 2017 transformer). Pick one discipline before locking dates.

### D5: How to mark the live edge? (Fork B5)

Era 7 is open-ended. Need a visual/structural convention for "this era is incomplete, the atoms are still forming." Either explicit "Era 8: TBD" or a visible open-right-edge on Era 7.

---

## What's ready for the next planning round

- A + B drafts give a complete *first-cut data model*: 7 trunks × 4 lenses × 8 eras, with a matrix as the navigation primitive.
- The two design tensions that *needed* drafting to resolve are now resolved.
- The third tension (depth budget) and five new decisions (D1-D5) are all user-judgment calls — none of them need more research, they need a sit-down with the user.

## Suggested next work after these decisions land

1. User reviews A + B + this doc, takes positions on Forks A1, A2, A3, A4, B4, B5.
2. Lock the matrix shape: trunks × eras finalized, lenses listed.
3. Pick the depth-budget descent list (~10-12 branches by love).
4. Then move to artifacts C (pre-AI/post-AI essay), D (metaphor catalog), E (source canon) — all of which now have a structural home (cells in the matrix or layers on top of it).
5. Only then begin visual/structural surface design.

## Files in this directory

- `A_branch_taxonomy.md` — 7 trunks, 4 lenses, vitality-tagged
- `B_eras_timeline.md` — 8 eras with first atoms and key works
- `_design_decisions_surfaced.md` — this file
