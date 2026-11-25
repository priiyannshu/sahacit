# B. Eras-of-Computing Timeline — CS Surface

*Foundational draft. Modeled on the history-surface era spine. Intent: anchor the "digital big bang" narrative and stress-test era-vs-branch primacy.*

## Stance

Computing has a clear narrative arc: math precedes machines, machines precede systems, systems precede networks, networks precede cloud, cloud precedes the AI inflection. Eight eras (0-7), each with **first atoms** (the things that did not exist before that era and never stopped mattering after) and **key figures/works** that anchor it.

The eras have a clear pre-AI/post-AI cut — Era 6 is the ramp, Era 7 is the inflection.

---

## Era 0 — Pre-Digital Foundations (1830s – 1935)

*The math without machines.*

The Victorian and early-modern century in which computation existed only as a mathematical concept and a few brass-and-gear prototypes. The era ends when Gödel proves the limits of formal systems — the negative result that paradoxically clears the ground for what comes next.

**First atoms:**
- Mechanical general-purpose computation (as a concept)
- Algebra of logic
- Algorithm (the word "algorithm" enters as a name for what Lovelace wrote)

**Key works & figures:**
- Charles Babbage — *Analytical Engine* design (1837)
- Ada Lovelace — *Notes on the Analytical Engine* (1843): the first program; the first speculation that machines could manipulate symbols, not just numbers
- George Boole — *The Laws of Thought* (1854)
- Gottlob Frege — *Begriffsschrift* (1879)
- David Hilbert — formalist program (1900s-1920s)
- Bertrand Russell & Alfred Whitehead — *Principia Mathematica* (1910-1913)
- Kurt Gödel — incompleteness theorems (1931)

---

## Era 1 — The First Atoms (1936 – 1948)

*The theoretical big bang. The vocabulary of the digital realm gets invented in a single decade.*

This is the era to honor with disproportionate depth. Within twelve years, computation, information, and stored-program architecture all become real. Every later era inherits the words coined here.

**First atoms:**
- Turing machine
- λ-calculus
- Church-Turing thesis
- Stored-program architecture (von Neumann)
- Boolean algebra realized in electrical switching (Shannon)
- The *transistor*
- The *bit*
- Channel capacity (information as a measurable quantity)

**Key works & figures:**
- Alan Turing — *On Computable Numbers* (1936)
- Alonzo Church — λ-calculus (1936)
- Claude Shannon — *A Symbolic Analysis of Relay and Switching Circuits* (MIT MS thesis, 1937): boolean algebra = digital circuits
- Konrad Zuse — Z3 (1941), first programmable computer
- ENIAC (1945)
- John von Neumann — *First Draft of a Report on the EDVAC* (1945): stored-program concept
- Bardeen, Brattain, Shockley — transistor at Bell Labs (1947)
- Claude Shannon — *A Mathematical Theory of Communication* (1948): information theory founded
- Norbert Wiener — *Cybernetics* (1948)

---

## Era 2 — The Founding (1948 – 1972)

*Systems and abstractions get named.*

Every core abstraction of CS — high-level languages, operating systems, time-sharing, structured programming, packet switching, relational algebra, AI as a discipline — is named in this quarter-century. The grammar of the field is set.

**First atoms:**
- High-level programming language (FORTRAN)
- Symbolic/recursive language (LISP)
- Operating system as a stable concept
- Time-sharing
- Structured programming
- Packet switching
- Relational data model
- Unix philosophy
- AI as a named discipline

**Key works & figures:**
- John Backus — FORTRAN (1957)
- John McCarthy — LISP (1958); coins "Artificial Intelligence" at Dartmouth (1956)
- Frank Rosenblatt — Perceptron (1958)
- ALGOL 60 — BNF, scope rules
- Edsger Dijkstra — *Go To Statement Considered Harmful* (1968); semaphores; THE OS
- IBM System/360 (1964) — first binary-compatible computer family
- Multics (1965)
- ARPANET (1969)
- Ken Thompson & Dennis Ritchie — Unix (1969)
- Edgar Codd — *A Relational Model of Data for Large Shared Data Banks* (1970)
- Dennis Ritchie — C (1972)

---

## Era 3 — The Personal Era (1972 – 1989)

*Computation becomes individual.*

The microprocessor arrives, then the PC, then the GUI. Computation leaves the priesthood of operators and lands on desks. Xerox PARC invents most of the next 30 years in one building, and almost none of it commercializes there.

**First atoms:**
- Microprocessor
- Personal computer
- Graphical user interface
- WYSIWYG
- Ethernet
- Object-oriented programming (Smalltalk → C++)
- TCP/IP as the internet's standard
- DNS
- Free software ideology

**Key works & figures:**
- Intel 4004 (1971)
- Xerox PARC — Alto (1973), GUI, mouse, Ethernet, Smalltalk, laser printer
- Apple II (1977), IBM PC (1981), Macintosh (1984)
- Bjarne Stroustrup — C++ (1983)
- Vint Cerf & Bob Kahn — TCP/IP, standardized on ARPANET (1983)
- Paul Mockapetris — DNS (1983)
- Richard Stallman — GNU project (1983), GPL (1989)
- First AI winter (mid-1980s) after expert-systems hype collapse

---

## Era 4 — The Network Era (1989 – 2004)

*The web, open source, and a cambrian explosion of languages.*

Berners-Lee writes a memo. Torvalds posts to a mailing list. Within a decade, the internet is a consumer phenomenon, Linux runs the world's servers, and the dot-com boom rewires capital flows around the web.

**First atoms:**
- World Wide Web (URL + HTTP + HTML)
- Open-source kernel running production systems
- Dynamic web languages
- Search-as-default interface
- The hyperlink as global addressing scheme

**Key works & figures:**
- Tim Berners-Lee — WWW proposal (1989), first browser & server (1990)
- Linus Torvalds — Linux (1991)
- Python (1991), Java (1995), JavaScript (1995), PHP (1995), Ruby (1995)
- Marc Andreessen — Mosaic (1993), Netscape (1994)
- Larry Page & Sergey Brin — Google (1998), PageRank
- Dot-com boom (1995-2000) and crash (2000-2002)
- Jimmy Wales — Wikipedia (2001)
- Bram Cohen — BitTorrent (2001)
- Roy Fielding — REST dissertation (2000)

---

## Era 5 — Cloud & Mobile (2004 – 2012)

*Computation becomes ambient.*

The two-handed transformation: cloud puts compute behind an API and you stop owning servers; the smartphone puts a Unix box in every pocket. Together they end the "your computer" metaphor.

**First atoms:**
- Cloud as utility (compute, storage, queues as APIs)
- Smartphone as primary personal computer
- App store as software-distribution channel
- Big-data processing on commodity clusters
- NoSQL as a legitimate alternative
- Decentralized consensus in the wild (Bitcoin)
- Distributed version control as default (Git)

**Key works & figures:**
- DHH — Rails (2004), Web 2.0
- Jeff Dean & Sanjay Ghemawat — MapReduce (2004), Bigtable (2006)
- AWS — EC2 + S3 (2006)
- Steve Jobs — iPhone (2007)
- Andy Rubin — Android (2008)
- Linus Torvalds — Git (2005); GitHub launches (2008)
- Satoshi Nakamoto — Bitcoin whitepaper (2008), genesis block (2009)
- Ryan Dahl — Node.js (2009)
- NoSQL movement: Dynamo, Cassandra, MongoDB, Redis (2007-2010)

---

## Era 6 — The Deep Learning Renaissance (2012 – 2022)

*The pre-AI ramp. Cloud-native matures in parallel.*

A single ImageNet result in 2012 changes which functions get computed and which hardware computes them. By 2017, the transformer architecture is in place. By 2020, scale is the recipe. By late 2022, the public has not yet noticed — but the substrate of the next era is fully built.

**First atoms:**
- GPU as default ML compute
- Deep learning as default ML approach
- Attention / transformer architecture
- Foundation models
- Containers + orchestration as default deployment substrate
- The scaling-laws recipe (more data, more params, more compute)
- Self-supervised learning at scale

**Key works & figures:**
- Krizhevsky, Sutskever, Hinton — AlexNet (2012). *The moment.*
- Mikolov et al. — word2vec (2013)
- Solomon Hykes — Docker (2013)
- Joe Beda et al. (Google) — Kubernetes (2014)
- Ian Goodfellow — GANs (2014)
- He et al. — ResNet (2015)
- Vaswani et al. — *Attention Is All You Need* (2017). *In retrospect: the actual big bang of the modern AI era.*
- Devlin et al. — BERT (2018)
- OpenAI — GPT-2 (2019), GPT-3 (2020)
- Jumper et al. (DeepMind) — AlphaFold 2 (2020)
- Stable Diffusion, DALL-E 2 (2022) — generative imagery enters consumer experience
- AlphaGo (2016): symbolic-vs-learned hybrid; Lee Sedol defeated

---

## Era 7 — The Post-AI Era (2022 – present)

*Generative cambrian explosion. Atoms still forming.*

The public-perception inflection: ChatGPT in November 2022 forces every layer of the stack to reorganize around a new primitive — the foundation model as a software component. Alignment, agent design, AI-native tooling, and sovereign-AI concerns shift from niche to first-class.

**First atoms (still hardening):**
- Foundation model as a primitive software component
- Prompt → context → agent design as a discipline
- Open-weights model ecosystem as a counterweight to closed labs
- RAG / vector retrieval as a default architectural pattern
- AI-native developer tools
- Alignment / interpretability / evals as engineering disciplines (not just academic ones)
- Multimodal-by-default models

**Key works & figures:**
- OpenAI — ChatGPT (Nov 2022)
- The LLM proliferation: GPT-4, Claude (Anthropic), Gemini (Google), Llama (Meta), Mistral, Qwen, DeepSeek
- Multimodal foundation models: GPT-4V, Claude 3, Gemini 1.5+
- Agent frameworks: AutoGPT (2023) as the early-naive form; Claude Code, Cursor, Windsurf as mature AI-native IDEs
- Sovereign / national AI stack concerns (post-2023)
- Alignment literature explosion: RLHF refinements, Constitutional AI, mech-interp, evals

---

## Pre-AI / Post-AI Layer (lens annotation, not a separate axis)

A second-layer annotation on the same timeline:

- **Pre-AI epoch:** Eras 0 – 5
- **AI ramp:** Era 6
- **Post-AI epoch:** Era 7+

The cut works in two ways the surface should expose:
1. **Public-perception cut:** Nov 2022 (ChatGPT). What the world saw.
2. **Technical cut:** 2012 (AlexNet) or 2017 (transformer). What actually changed.

The surface might let the user toggle which cut is foregrounded.

---

## Decisions this draft forces into the open

### Fork B1: Era-vs-branch primacy resolved → 2D matrix

Drafting the eras makes it obvious that each era *births or matures* specific branches from Taxonomy A. The natural data structure is not "era list" or "branch list" — it's a **branch × era matrix**, with cells holding "what this branch looked like in this era." Examples:

- Networks × Era 2: ARPANET, packet switching invented
- Networks × Era 4: TCP/IP wins, web layers on top
- Networks × Era 6: cloud-native networking, eBPF, service mesh
- AI × Era 2: founded as discipline, perceptron
- AI × Era 3: expert systems peak, first winter
- AI × Era 6: deep learning, transformer
- AI × Era 7: foundation models, generative

This resolves design tension #2 from the planning round: **both axes are primary**, and the cells are the actual reading material.

### Fork B2: Era 1 (1936–1948) gets disproportionate depth

If the surface honors the "first atoms" framing, Era 1 is a privileged origin chapter — the digital field's "ancient-classical." Every vocabulary item invented here echoes through every later era. Recommend: budget 2-3x the cell-depth for Era 1 cells compared to other eras.

### Fork B3: Pre-AI/post-AI is a layer, not a lens

Drafting the timeline makes it clear that pre-AI/post-AI is a **temporal annotation on the era spine**, not a separate viewing mode. It's a *fold-line* on the existing canvas, not an alternative canvas. This resolves design tension #1: **lenses layer onto one canvas**, they don't toggle between alternative canvases.

This also implies the "cross-subject metaphor" lens (artifact D, future work) will also be a *layer annotation*, not a separate view — metaphors annotate cells in the matrix, not replace the matrix.

### Fork B4: Era boundaries are arguable

Several boundaries here are real judgment calls:
- Is 1972 (microprocessor + Unix + C) really the founding-era close, or is 1969 (ARPANET + Unix + Multics' end)?
- Is 1989 the right close for the personal era, or 1991 (WWW + Linux)?
- Is 2012 the right open for Era 6, or 2017 (transformer)?

The choices in this draft prioritize *technological availability* over *cultural adoption*. The user may prefer cultural-adoption cuts. **Pick a discipline before locking eras.**

### Fork B5: Where does "still-uninvented" go?

Era 7 is open-ended and the atoms are still hardening. The surface needs a convention for "this era is live and incomplete" — either an explicit "Era 8: TBD" placeholder, or a visual marker that Era 7's right edge is open. **Pick one before any visual design starts.**
