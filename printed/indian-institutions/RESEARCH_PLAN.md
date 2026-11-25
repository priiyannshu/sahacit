# Research & Production Plan — Indian Institutions (All 134 Entries)

Working roadmap for researching, verifying, and generating all **134 institution dossiers** inside `printed/indian-institutions/` in upcoming sessions.

---

## 1. Ground Rules for Research & Authoring

1. **Verify Against Primary Statutes & 2023–2026 Amendments**:
   - Never rely purely on outdated coaching memory. Verify every institution's enabling Act/Article, exact amendments (e.g., *CEC & ECs Act 2023*, *Bharatiya Nyaya/Nagarik/Sakshya Sanhitas*, *Anusandhan NRF Act 2023*, *DPDP Act 2023*, *Biological Diversity Amendment 2023*, *Forest Conservation Amendment 2023*, *Jan Vishwas Act 2023*, *Telecommunications Act 2023*, *Payments Regulatory Board 2025*, *Madras Bar Association Nov 2025* tribunal ruling, *106th Constitutional Amendment 2023*), exact **Nodal Ministry**, exact **Selection Committee**, **Tenure/Age cap**, **Removal grounds**, and **Appellate Tribunal**.
2. **File Naming & Schema Compliance**:
   - Name files `data/institutions/NNN_<short_slug>.json` matching `order` and `id` in `data/roster.json` (e.g. `001_president-of-india.json` through `134_epfo-and-esic.json`).
   - Validate strictly against `data/schema.json` using `python3 printed/indian-institutions/build.py --no-compile`.
3. **Self-Contained Prelims Quality Bar**:
   - Every entry must answer *who handles what*, *who sits inside*, *how they get appointed & removed*, *what they explicitly CANNOT do*, and *which look-alike twin traps candidates*.
   - Keep main pages free of volatile personal incumbent names (structural roles only) and free of any AI/dev build metadata.
4. **Layout Assignment**:
   - Use `"dossier"` for deep constitutional/apex organs spanning 1.5–2+ pages with rich comparison sub-tables (`Parliament`, `Supreme Court`, `President/Governor`, `PRIs/ULBs`, `RBI`, `SEBI`, `CAG`, `UPSC`, `Lokpal`, etc.).
   - Use `"blueprint"` for 1–1.5 page structured institutions benefiting from vector lifecycle/appeal flow strips + 2-column grids (`ECI`, `NGT`, `Finance Commission`, `NHRC`, `CVC`, `CCI`, `TRAI`, `NBWL`, `NTCA`, `NBA`, `UIDAI`, `DPBI`, etc.).
   - Use `"compact"` for crisp, focused statutory/advisory bodies where ~1/2 page covers all 7 blocks cleanly (`WCCB`, `CZA`, `AWBI`, `WDRA`, `BEE`, `CCPD`, etc.).

---

## 2. Batch Execution Plan (Next Sessions)

| Batch | Scope | Target Entries | Status |
|---|---|---:|---|
| **Batch 0 (Done)** | Spec, Typst Engine & 5 Pilot Benchmarks (`#005`, `#021`, `#044`, `#088`, `#092`) | 5 | Complete |
| **Batch 1 — Part I** | Core Constitutional Organs, Executive Machinery & Federal Spine (`#001`–`#020`, remaining 19) | 19 | Pending |
| **Batch 2 — Part II** | Elections, Integrity, Audit, Civil Services & Rights Watchdogs (`#022`–`#043`, remaining 22) | 22 | Pending |
| **Batch 3 — Part V** | Environment, Wildlife, Forests, Water & Disaster Authorities *(high-yield Prelims sprint!)* (`#089`–`#106`, remaining 17) | 17 | Pending |
| **Batch 4 — Part III** | Monetary, Financial, Tax & Capital Market Institutions (`#045`–`#065`, remaining 21) | 21 | Pending |
| **Batch 5 — Part IV** | Commerce, Competition, Infrastructure & Sectoral Regulators (`#066`–`#087`) | 22 | Pending |
| **Batch 6 — Part VI** | Defence, Internal Security, Space, Atomic & Digital/Scientific Bodies (`#107`–`#120`) | 14 | Pending |
| **Batch 7 — Part VII** | Tribunals, Education, Culture, Media & Statutory Professions (`#121`–`#134`) | 14 | Pending |
| **Batch 8 — Final Polish** | Full 134-entry Typst compile (`indian_institutions.pdf`), visual spread check, empty-space audit & Master Cross-Indexes verification | All 134 | Pending |

---

## 3. Verification Command Per Batch

```bash
python3 printed/indian-institutions/build.py --output indian_institutions.pdf
```
Inspect rendered PNGs via `typst compile --format png` on newly added pages to verify zero overflow, balanced two-column utilization, and generous reading whitespace.
