# Heritage Assets Manifest

> **Virtual University (`vu`) Heritage Repository**
> All retained knowledge, content, pipelines, and reference artifacts migrated from predecessor systems `22` and `preach`.

---

## Directory Structure

```
vu/
├── docs/
│   ├── FOUNDATION.md                    # Virtual University architectural seed
│   └── archive/                         # Archived 22 blueprints (VISION, MASTER_PLAN, KG_APPROACH, STATE, EXPERIMENTS)
├── heritage/
│   ├── knowledge/
│   │   ├── pyq/                         # UPSC Prelims PYQ corpus + links, CTET PYQ master bank (JSON & MD)
│   │   ├── subjects/                    # Subject taxonomies (economics, history, polity)
│   │   ├── ontologies/                  # InPhO (Indiana Philosophy Ontology) OWL dataset
│   │   ├── non-temporal/                # Timeless & parked subject extractions (Geography, Science, History, Polity, Econ)
│   │   └── evs/                         # 77 chapter JSON ledgers (Classes 3-6), 7 thematic unit MDs, audit/verification matrices
│   ├── library/
│   │   ├── ncert/                       # 357 NCERT HTML chapters across Economics, Geography, History, Polity, Science
│   │   ├── ref/                         # 314 Reference Book HTML chapters (Laxmikanth, Bipin Chandra, Ramesh Singh, etc.)
│   │   └── manifest.json                # Complete offline reader library catalog
│   ├── surfaces/
│   │   ├── history-surface/             # 11 Chronological era packages (narratives, html, json, pyqs) + SPRINT specs
│   │   ├── economics-surface/           # 12 Chapter authored markdown chapters
│   │   ├── polity-surface/              # 11 Chapter authored markdown chapters
│   │   └── geography-surface/           # 12 Chapter authored markdown chapters, manifests, & high-res concept illustrations
│   ├── frontend-data/                   # In-memory node lookups, drill clusters, discrimination cards, and timeline bundles
│   └── downstream/
│       ├── unit_1/                      # Standalone interactive ledger application & visual infographic assets
│       ├── hyperframes/                 # Visual state machine player engine
│       ├── pwa_quiz/                    # PWA quiz widget engine & question dataset
│       └── transcripts/                 # Bilingual timestamped transcripts & study guide artifacts
├── pipeline/
│   ├── schemas/                         # D1 database migrations (0001-0004)
│   ├── scripts/                         # Extraction, build, aggregation, timeline, drill, and transcript scripts
│   └── notebooklm/                      # 7 Unit steering manifests & NotebookLM sync automation
├── reference-code/
│   └── cf-worker/                       # Cloudflare Worker, Durable Object (UPSCTutorAgent), and pipeline handlers
└── tooling/
    └── notebooklm-tools.md              # NotebookLM programmatic access tools & comparison guide
```

---

## Ingested Quantities

- **NCERT & Reference Library**: 671 structured HTML chapters + complete catalog manifest
- **Curated Knowledge Ledgers**: 77 atomic JSON chapter ledgers (Classes 3–6 EVS & Bridge Science/Geography)
- **Thematic Spiral Units**: 7 master Markdown unit synthesis documents
- **Question Banks**: Complete UPSC Prelims PYQ corpus (with topic node links) + CTET PYQ master bank
- **Narrative Surfaces**: 11 History eras, 12 Economics chapters, 11 Polity chapters, 12 Geography chapters
- **Ontologies & Taxonomies**: InPhO OWL philosophy ontology, Indian Constitution mappings, and subject taxonomies
- **Pipelines & Generators**: Full suite of Python/TypeScript extraction scripts, NotebookLM steering manifests, and D1 schemas
- **Audio Files**: Excluded (to be freshly regenerated on-demand via NotebookLM pipelines)
