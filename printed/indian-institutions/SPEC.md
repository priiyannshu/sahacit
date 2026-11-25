# Book 1 Specification — Indian Institutions (UPSC Prelims 2027 Atlas)

> **Working Directory**: `printed/indian-institutions/` (Canonical home for all research, JSON records, Typst templates, and compiled PDFs)  
> **Planning Manifest**: [book-and-booklets/output.md](../../diary-entries-of-a-champion/2026-11-25/book-and-booklets/output.md)

---

## 1. Governing Architecture & Editorial Rules

| Decision Axis | Locked Choice |
|---|---|
| **Scope & Boundary** | Strictly **Indian Institutions** (~134 bodies across a Tiered Indian Atlas); International Institutions sit in a separate volume. Excludes individual PSUs/CPSEs, individual central universities, and state-specific boards (summarized concisely instead). |
| **Macro Architecture** | **State Anatomy + Functional Pillars + Master Cross-Indexes**: Opens with *The Skeleton of the Indian State* macro-map, organizes entries into **7 Functional Pillars** (so confusable twins sit side-by-side), and closes with auto-generated Master Cross-Indexes. |
| **Physical Format** | **Full A4 Duplex Book** (spiral / comb / ring-binder ready), mirrored binding gutters (`19mm` inside / `11mm` outside), **odd-page (recto) Part starts** so individual parts can be reprinted independently. |
| **Page Span Policy** | **Content-driven, non-deterministic**: Mega organs naturally span 2+ pages; standard bodies take 1–2 pages; focused statutory bodies take compact cards—never truncate authoritative UPSC facts just to squeeze onto 1 page. |
| **Typography & Palette** | `Libertinus Serif` (body) + `Roboto` (headings, labels, tables) + `DejaVu Sans Mono` (index tags). Pure monochrome ink-efficient styling: crisp black/charcoal ink, `0.4pt–1.2pt` rules, ultra-light `4–8%` gray callout tints, zero heavy black blocks. |
| **Incumbent Rules** | **Structural roles & mandatory qualifications only** on permanent pages (plus optional separate detachable/updatable incumbent sheet if needed) so static prints remain evergreen through May 2027. |
| **Source & Print Stack** | Structured JSON per institution (`data/institutions/*.json`) validated against `data/schema.json` → Python index builder (`build.py`) → `Typst 0.15.1` monochrome A4 PDF. |

---

## 2. Pilot Review Refinements (Registered 2026-11-25)

1. **Zero AI / Development Text Artifacts on Printed Pages**:
   - **Strictly forbidden** anywhere in rendered PDF pages: build timestamps/dates, `"Pilot Build"`, `"5 / 134 populated"`, `"PILOT p.X"` badges, `"How This Atlas Is Engineered"` meta-commentary boxes, or internal tool/system slogans in running headers/footers.
   - Printed pages must read strictly like an **authoritative, timeless published reference book** (clean title/subtitle, clean Part/Institution running headers, crisp page numbers, and pure institutional content).
2. **De-Congested Spacing & Visual Breathing Room**:
   - Avoid cramming vertical gaps, table padding, or line leading purely to force tight page counts. Give dense tables, flow strips, and bullet blocks comfortable breathing room (`leading: 0.56em` body prose, airy table cell insets, clean spacing between sections).
3. **Active Two-Column Whitespace Utilization**:
   - Where lists, roadmaps, or trailing dossier blocks would leave awkward single-column white bands (e.g., Atlas contents/index lists or wide trailing sections), flow them cleanly in **two balanced columns** (using explicit `grid(columns: (1fr, 1fr), ...)` rather than Typst's tall single-page `columns(2)` balancer) so every A4 page feels well-proportioned without crowding.

---

## 3. UPSC Prelims 7-Block Entry Schema (`data/schema.json`)

Every institution JSON file (`data/institutions/NNN_<slug>.json`) conforms to these 7 blocks:

1. **Legal Anchor, Nodal Ministry & Amendments (`anchor`)**: `legal_status`, `basis` (Articles / Enabling Act & Sections), `key_amendments` (through 2026), `nodal_ministry`, `established_year`, `headquarters`, `essential_summary`.
2. **Organizational Anatomy & People Inside (`composition`)**: `chairperson`, `members` (exact numerical counts & quotas), `eligibility_rules`, `internal_wings` (sub-boards, secretariats, regional benches).
3. **Appointment, Selection, Tenure & Exit (`lifecycle`)**: `appointing_authority`, `selection_committee`, `tenure`, `age_limit`, `reappointment_and_post_retirement`, `resignation_to`, `removal_procedure`, `funding_and_salary` (plus short index fields `selection_short`, `removal_short`, `reappointment_short`).
4. **Mandate, Statutory Powers, Jurisdiction & Appeal (`mandate`)**: `core_functions`, `power_nature` (Binding vs Advisory), `special_powers` (Civil court / *suo motu* / penal), `jurisdiction_limits_and_exclusions`, `reporting_chain`, `appellate_pathway`.
5. **Genesis & Landmark Supreme Court Jurisprudence (`genesis`)**: `founding_committee`, `landmark_cases`.
6. **Prelims Trap Box & Look-Alike Twins (`traps`)**: `common_traps` (CAN/CANNOT & statement-swap traps), `twin_comparison` (side-by-side table against easily confused sibling bodies).
7. **State Counterparts, UPSC Categories & Ecosystem Links (`links`)**: `state_counterparts`, `upsc_categories` (canonical 7 UPSC labels), `linked_acts_and_missions`.

*Optional mega-dossier fields*: `extra_tables` (structured comparative tables such as Bill Types or Specialized Sub-Boards).

---

## 4. Master Roster Summary (134 Planned Entries across 7 Functional Parts)

Full canonical IDs, order numbers (`#001`–`#134`), and part assignments live in [`data/roster.json`](data/roster.json):

- **Front Matter**: *The Skeleton of the Indian State* (`data/state_skeleton.json`)
- **Part I (`#001`–`#020`)**: Core Constitutional Organs, Executive Machinery & Federal Spine *(20 bodies)*
- **Part II (`#021`–`#043`)**: Elections, Integrity, Audit, Civil Services & Rights Watchdogs *(23 bodies)*
- **Part III (`#044`–`#065`)**: Monetary, Financial, Tax & Capital Market Institutions *(22 bodies)*
- **Part IV (`#066`–`#087`)**: Commerce, Competition, Infrastructure & Sectoral Regulators *(22 bodies)*
- **Part V (`#088`–`#106`)**: Environment, Wildlife, Forests, Water & Disaster Authorities *(19 bodies)*
- **Part VI (`#107`–`#120`)**: Defence, Internal Security, Space, Atomic & Digital/Scientific Bodies *(14 bodies)*
- **Part VII (`#121`–`#134`)**: Tribunals, Education, Culture, Media & Statutory Professions *(14 bodies)*
- **Back Matter**: Auto-Generated Master Cross-Indexes (Legal Origin, Ministry Matrix, Lifecycle/Selection Matrix, Appellate Matrix, Alphabetical Lookup)
