# Maths Surface — Early Concept Seed

*Not a spec. A sketch of what the surface might feel like and what it might contain. Written before building. Will be wrong in several places. Update as the surface evolves.*

---

## The Entry Experience

Unlike polity/economics (narrative chapters you scroll through), the maths surface probably opens on a **territory map** — an interactive visualization of the knowledge landscape. You see the federation at a glance: Algebra, Analysis, Geometry, Number Theory, Combinatorics, Probability. You can see which areas you've visited, which are blank.

This map is not decorative. It's the primary navigation layer. You click a territory → enter it → drill into branches → drill into concepts.

Contrast with current surfaces:
- **History:** timeline (temporal navigation)
- **Polity/Economics:** chapter list (curriculum navigation)
- **Maths:** territory map (spatial navigation through a knowledge landscape)

---

## Node Structure (Concept Unit)

Each mathematical concept should open in a **layered format** — you can stop at any layer:

```
Layer 0: The phenomenon
  "This is describing ___. The question it answers is: ___."
  One sentence. One image or animation if possible.

Layer 1: The intuition
  No symbols yet. What is the *idea*? What does it feel like?
  Analogy to something already understood.

Layer 2: The simple example
  The smallest possible instance where you can see the idea working.

Layer 3: The formalization
  Now the symbols. Now the definition. After the idea has landed.

Layer 4: The connections
  What other concepts does this touch? What does it enable?
  Where does it appear in the UPSC optional?

Layer 5: The tool (optional)
  If the concept is one where direct manipulation helps — a widget.
  E.g., for derivative: drag a slider and watch the slope.
```

This is the inverted textbook. Textbooks go: definition → theorem → proof → examples → exercises. This goes: phenomenon → intuition → example → definition → connections.

---

## Interactive Tool Layer (Distinct Feature of Maths Surface)

The maths surface needs embedded tools that don't exist in other surfaces. These are **load-bearing**, not decorative.

Possible embedded tools (progressive complexity):

1. **Function grapher** — type `sin(x)`, see it. Drag parameter sliders. See what `sin(2x)` vs `sin(x/2)` does.
2. **Limit visualizer** — animate a sequence approaching a limit. Feel what "arbitrarily close" means.
3. **Matrix transformer** — input a 2x2 matrix, see what it does to a unit square. Make eigenvalues visceral.
4. **Graph (network) builder** — nodes and edges, see graph properties emerge.
5. **Probability sim** — run coin flips, dice rolls, see distributions emerge from repeated trials.
6. **Geometric transformer** — rotate, reflect, translate a shape. See group actions.

These don't have to be built from scratch. Libraries that could work:
- **Desmos API** — function graphing, incredibly good
- **GeoGebra** (embeddable) — geometry + algebra + calculus
- **Three.js** — 3D geometry, surfaces
- **Mafs** (React library) — math figures for the web
- **Observable Plot / D3** — for data-heavy visualizations

Decision on which to use: defer until actually building the first tool node.

---

## Audio Layer

Similar to other surfaces — a recorded/generated narration per concept. But for maths, narration might be less "chapter reading" and more "guided walk through the intuition before you engage with the visual."

Possible format: short (~2-3 min) audio per concept node that:
1. States the phenomenon in plain language
2. Gives the intuition (eyes-closed mental image)
3. Signals "now open your eyes and interact with the tool"

This is closer to a guided meditation than a lecture.

---

## What Carries Over From Other Surfaces

- PWA shell (already exists)
- Tab architecture
- Narrative chapter format (for some nodes that work better as text)
- Updates log discipline
- SQLite coverage tracking (when that gets implemented)

What's new:
- Territory map as primary nav
- Interactive embedded tools as load-bearing elements
- Layered concept format (phenomenon → formalization)
- The "why does this branch exist" historical narrative per territory

---

## UPSC Optional Integration

The territory map should have a toggle: **"Show UPSC optional coverage"**. When toggled, the map highlights which territories/branches are in scope for Papers 1 and 2. This lets the surface serve both purposes:
- General mathematical literacy (the full map)
- UPSC preparation (filtered, prioritized subset)

---

## Build Order (Rough Sketch — Don't Over-Plan)

Not a roadmap. A sketch of what might come first:

1. **PWA shell for maths tab** — add the tab, land on an empty territory map placeholder
2. **One territory as proof of concept** — probably Linear Algebra (UPSC Paper 1, widely useful, visual)
3. **First interactive tool** — the matrix transformer or function grapher
4. **Refine the concept node format** from actual experience
5. **Territory map** proper once several territories exist and the navigation need becomes concrete
6. **Audio layer** as a second pass

Everything subject to change once the first node actually exists and the format reveals itself.

---

## Open Questions

- Does the territory map make sense as an entry point, or is a chapter list simpler to start with?
- Which embedded tool library is best given the setup (offline-capable PWA, no React)?
- How much of the concept node is text vs interactive vs audio?
- How do we handle concepts that are pure abstraction (e.g., category theory) vs concepts with obvious physical reality hooks?

These get answered through making, not planning.
