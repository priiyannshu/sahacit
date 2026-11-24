# A. Canonical Branch Taxonomy — CS Surface

*Foundational draft. Opinionated. Intent: force design choices, not be exhaustive.*

## Stance

ACM CCS 2012 has 13 top-level categories arranged for bibliographic classification, not for love. It buries AI inside "Computing methodologies," makes "General and reference" a peer of "Hardware," and lacks any sense of which subfields are *alive*. This draft proposes a re-organized **7-trunk model** with **4 orthogonal cross-cutting lenses**, marked for vitality.

The trunks are the "what" of CS. The lenses cut through every trunk.

---

## The 7 Trunks

Each trunk has a one-line essence, limbs (sub-branches), and vitality tags:
- **alive** — active research frontier, rapidly changing
- **matured** — stable canon, occasionally extended
- **historical-foundational** — important to know, no longer the active site

---

### 1. Theory — what can be computed, how hard, in what languages

- Computability — *matured-foundational.* Turing machines, decidability, the Halting problem, Rice's theorem, Church-Turing thesis.
- Complexity — *alive.* P vs NP, NP-completeness, randomized & average-case complexity, fine-grained complexity, quantum complexity classes (BQP), circuit complexity.
- Formal languages & automata — *matured.* Chomsky hierarchy, regular/CF/CS/recursive, pumping lemmas, pushdown automata.
- Logic in computation — *alive.* Descriptive complexity, finite model theory, SAT/SMT, model checking.
- Information theory — *matured-foundational with alive offshoots.* Shannon entropy, channel capacity, error-correcting codes; algorithmic information theory (Kolmogorov).

### 2. Hardware & Architecture — from atoms (transistors) to organisms (datacenters)

- Digital logic — *matured.* Gates, flip-flops, FSMs, HDLs.
- Computer architecture — *alive.* RISC-V momentum, accelerators, GPU as general compute, TPU/NPU/specialized AI silicon, memory-disaggregation.
- Memory hierarchy — *alive.* NVRAM, CXL, near-memory & in-memory compute, persistent memory programming.
- Parallel & distributed hardware — *alive.* Many-core, interconnects, RDMA, NoCs.
- Quantum hardware — *alive-frontier.* Superconducting, trapped-ion, photonic, neutral-atom.
- Neuromorphic — *alive-frontier.* Spiking neural nets in silicon (Loihi, TrueNorth).

### 3. Systems — making collections of hardware behave like coherent things

- Operating systems — *mostly matured, alive in pockets.* Unikernels, library OS, serverless runtimes, OS for accelerators (CUDA/ROCm runtimes as quasi-OS).
- Concurrency & parallelism — *alive.* Lock-free structures, transactional memory, async runtimes, structured concurrency.
- Distributed systems — *alive.* Consensus (Paxos/Raft), CRDTs, geo-distributed databases, blockchain protocols.
- Databases — *alive.* NewSQL, vector DBs, time-series, embedded analytics (DuckDB), HTAP.
- Virtualization & containers — *alive.* Hypervisors, microVMs (Firecracker), WASM as a runtime substrate.
- Real-time & embedded — *alive in safety-critical niches.* Hard/soft RT, RTOS.
- Storage — *alive.* NVMe, object storage, log-structured systems, persistent data structures.

### 4. Languages & Compilers — how humans speak to machines, and how that speech is translated

- Language design — *alive.* Rust, Zig, Swift, Roc, modern type-system experiments.
- Compilers — *alive.* LLVM, MLIR, eBPF, JITs, polyhedral optimizers, ML-compiler stacks (XLA, TVM).
- Type theory — *alive.* Dependent types (Lean/Idris), gradual typing, refinement types, effects.
- Semantics — *alive in formal-methods corners.* Operational, denotational, separation logic, game semantics.
- Runtimes & VMs — *alive.* WASM, JS engines (V8/JSC/SpiderMonkey), JVM evolution, BEAM.
- Formal methods & verification — *alive.* Coq, Lean, Isabelle, TLA+, F*, model checking at scale.
- Programming paradigms — *matured.* FP, OOP, logic, dataflow, actor, array-oriented.

### 5. Networks — the physical-and-logical fabric

- Internet protocols — *matured (TCP/IP), alive frontiers (QUIC, HTTP/3, BBR congestion control).*
- Routing & switching — *matured.*
- Wireless — *alive.* 5G/6G, satellite mesh (Starlink-class), LPWAN, mesh networks.
- Network security — *alive.* TLS evolution, post-quantum migration, zero-trust architectures.
- Programmable networks — *alive.* P4, SDN, eBPF in networking, smart NICs.
- Content distribution — *alive.* CDNs, edge compute, P2P revivals (IPFS-class systems).

### 6. Intelligence — getting machines to do tasks we associate with thought

*The trunk that seeps into every other trunk.*

- Symbolic AI — *historical-foundational.* Rule-based, expert systems, GOFAI, logic programming as AI.
- Search & planning — *matured (A*, MCTS), alive (LLM-driven planners, hybrid neuro-symbolic).*
- Knowledge representation — *matured with alive revival.* Knowledge graphs, ontologies, semantic web echoes inside retrieval.
- Classical ML — *matured.* Linear models, SVMs, trees, ensembles (XGBoost still dominates tabular).
- Deep learning — *alive.* Architectures, training methods, optimization, scaling laws.
- NLP — *alive.* Foundation models, multilingual, multimodal grounding.
- Vision — *alive.* Foundation models, generative imagery, 3D vision, video understanding.
- Robotics — *alive.* Manipulation, learning-from-demo, sim-to-real, foundation models for control.
- Reinforcement learning — *alive.* Model-based, offline RL, multi-agent, RLHF, RLVR.
- Generative models — *alive.* Diffusion, GANs, autoregressive, flow matching, consistency models.
- Foundation models — *alive-frontier.* Pre-training, post-training, scaling, mixture of experts.
- Alignment & interpretability — *alive-frontier.* Mechanistic interpretability, RLHF/DPO/Constitutional AI, evals, safety cases.

### 7. Interface — where humans, the physical world, and computation meet

- HCI — *alive.*
- Graphics — *alive.* Real-time rendering, ray/path tracing, neural rendering (NeRF/Gaussian splatting).
- Computational photography & video — *alive.*
- Visualization — *alive.* Information viz, scientific viz, interactive notebooks.
- Spatial / XR — *alive.* AR/VR/MR, spatial computing platforms.
- Audio / speech UX — *alive.*
- Accessibility — *alive.*
- Brain-computer interfaces — *alive-frontier.*

---

## The 4 Cross-Cutting Lenses (orthogonal to trunks)

These are not trunks — they cut *through* every trunk:

1. **Security & Cryptography** — sites are systems, networks, languages, hardware. Canon: Schneier, Stallings, Boneh-Shoup, Katz-Lindell.
2. **Software Engineering** — methodologies, testing, version control, code quality, dev tooling, project management of software. Cuts every trunk.
3. **Data / Information Systems** — data engineering, ETL, IR, recommender systems, data governance, data lakes/warehouses/lakehouses.
4. **Computing & Society** — ethics, alignment, fairness, sustainability (green computing), privacy, policy, the politics of computation.

---

## Decisions this draft forces into the open

Drafting the taxonomy made the following implicit choices visible. Each is a real fork.

### Fork A1: Is AI a trunk or a lens?

This draft puts AI as a trunk ("Intelligence") AND notes its seepage into Hardware (ML silicon), Systems (vector DBs), Languages (ML-compiler stacks), Interface (neural rendering). That seepage is real and unique — no other trunk seeps like this. Two options:

- **A1a (this draft):** Trunk + acknowledged seepage. AI gets its own dedicated section; cross-references mark where it has invaded other trunks.
- **A1b:** Lens, not trunk. AI becomes a fifth cross-cutting lens like Security; ML systems live under Systems, ML hardware under Hardware, etc.

A1a honors how *practitioners* talk about AI (as a field). A1b honors how AI *behaves* in the codebase of CS (as a contagion). **Pick.**

### Fork A2: Vitality tags or no?

Tagging alive/matured/historical creates a "frontier map" the user can scan to decide where to spend learning hours. It also dates: in 5 years, today's "alive" becomes "matured." If we keep tags, the surface should expose them as a *visible filter* — otherwise they're decoration. If we drop them, the surface loses the "what should I obsess over now" signal.

### Fork A3: Depth-budget selection rule

"Every branch gets a node, only N get full descent." Three plausible selection rules:

- **Frontier-first:** descend only into *alive* and *alive-frontier* branches.
- **Love-first:** user picks ~10-12 branches to descend regardless of vitality (e.g., lambda calculus + Smalltalk are beautiful even though matured).
- **Coverage-first:** at least one full-descent branch per trunk for proportional representation.

Love-first is most consonant with the project's "for the love of CS" framing. Recommend that, with the user picking the descent list before any per-branch work begins.

### Fork A4: Where does software engineering live?

This draft makes it a lens, not a trunk. Some curricula make it a trunk peer. The lens choice means SWE never gets a "front page" of its own; it shows up as practices/concerns *inside* the systems and languages trunks. If you want a place for "this is how to ship software," it needs to be a trunk.

---

## Open: what this taxonomy is NOT trying to be

- Not a curriculum. Order of learning is a separate question.
- Not a reading list. That's artifact (E).
- Not a syllabus map. The vitality tags are descriptive, not prescriptive.
- Not stable. Expect to revise after first descent attempt reveals what's missing.
