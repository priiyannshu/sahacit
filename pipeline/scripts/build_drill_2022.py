#!/usr/bin/env python3
"""
Generate app/pwa/data/drill_clusters_2022.json
       + app/pwa/data/discrimination_cards_2022.json

Cluster map covers all 100 GS1 2022 PYQs. Clusters + trap tags drafted by
Sonnet pre-step agents (cluster + trap-tag), Opus consolidated and merged.
Discrimination cards drafted by parallel Sonnet batches; auto-overlay loader
picks up calibration_cards.json + wave1*.json + wave2*.json from
.scratch/drill_2022/.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "pwa" / "data" / "pyq_index.json"
OUT_CLUSTERS = ROOT / "pwa" / "data" / "drill_clusters_2022.json"
OUT_CARDS = ROOT / "pwa" / "data" / "discrimination_cards_2022.json"

YEAR = 2022

# Cluster definitions for all 100 2022 PYQs.
# Format: (cluster_id, title, subject_focus, study_keywords[], common_traps[], pyq_ids[])
CLUSTERS: list = [
    # --- Ancient Indian History (8 PYQs, 4 clusters) ---
    ("anc_early_society_law", "Ancient India: Early Society — Arthashastra & Sangam Literature", "Ancient Indian History",
     ["Kautilya Arthashastra slavery female slave legal status",
      "Sangam literature ancient South India material culture Varna",
      "Mauryan vs Sangam-era social structure"],
     ["statement_partial_truth", "statement_overgeneralization"],
     [90, 181]),
    ("anc_dynasties_kings_matching", "Ancient India: Post-Gupta Dynasties & King-Dynasty Matching", "Ancient Indian History",
     ["Chandela Paramar Gurjara-Pratihara Rashtrakuta kings",
      "Nannuka Jayashakti Nagabhata Bhoja dynasty matching"],
     ["person_attribution", "famous_association_bias"],
     [124]),
    ("anc_ashokan_edicts_sites", "Ancient India: Ashokan Rock Edicts — Sites & Locations", "Ancient Indian History",
     ["Ashoka major rock edicts Dhauli Erragudi Jaugada Kalsi locations",
      "Ashokan inscriptions state-wise distribution India"],
     ["geographic_attribution", "statement_partial_truth"],
     [132]),
    ("anc_religion_philosophy_temples", "Ancient India: Religion, Philosophy & Sacred Sites — Somnath, Ramanuja, Jaina Texts", "Ancient Indian History",
     ["Somnath Temple Jyotirlinga Al-Biruni Pran Pratishtha 1951",
      "Ramanuja Vishishtadvaita bhakti salvation devotion",
      "Jaina texts Nettipakarana Parishishtaparvan Avadanashataka Trishashtilakshana",
      "Aryadeva Dignaga Nathamuni scholar identity Buddhism Jainism Vaishnavism"],
     ["person_attribution", "overlapping_categories", "famous_association_bias"],
     [133, 208, 209, 210]),

    # --- Medieval Indian History (5 PYQs, 2 clusters) ---
    ("med_delhi_sultanate_rulers", "Medieval India: Delhi Sultanate — Mongol Invasions & Terminology", "Medieval Indian History",
     ["Mongol invasion India Jalal-ud-din Khalji Ala-ud-din Delhi siege",
      "Fanam medieval India coins currency",
      "Kulah-Daran Sayyids medieval India"],
     ["period_attribution", "person_attribution", "technical_vs_common_meaning"],
     [248, 249, 250]),
    ("med_advent_europeans_mughal", "Medieval India: Advent of Europeans & Mughal Court Literature", "Medieval Indian History",
     ["Dutch factories Gajapati rulers east coast India",
      "Albuquerque Goa Bijapur Sultanate EIC Madras Vijayanagara",
      "Yogavasistha Persian translation Nizamuddin Panipati Akbar"],
     ["geographic_attribution", "person_attribution", "period_attribution"],
     [312, 323]),

    # --- Modern Indian History (3 PYQs, 2 clusters) ---
    ("mod_constitutional_acts", "Modern India: Constitutional Acts — Montagu-Chelmsford & Dyarchy", "Modern Indian History",
     ["Government of India Act 1919 Reserved Transferred subjects dyarchy",
      "Montagu-Chelmsford reforms provincial government functions"],
     ["overlapping_categories", "statement_subtle_inversion"],
     [462]),
    ("mod_nationalist_movements", "Modern India: Cripps Mission & Ghadar Party", "Modern Indian History",
     ["Cripps Mission 1942 Constituent Assembly Princely States opt-out",
      "Ghadar Party Rash Behari Bose Barindra Kumar Ghosh Jogesh Chatterjee"],
     ["person_attribution", "statement_subtle_inversion"],
     [553, 638]),

    # --- Indian Polity (11 PYQs, 5 clusters) ---
    ("pol_constitutional_structure", "Indian Polity: Constitutional Structure — Amendment Procedure & Fifth Schedule", "Indian Polity",
     ["Constitutional Amendment Bill President assent mandatory Article 368",
      "Amendment Bill joint sitting special majority Rajya Sabha",
      "Fifth Schedule Constitution India tribal areas land transfer",
      "Schedule Five provisions consequences tribal protection"],
     ["statement_subtle_inversion", "overlapping_categories"],
     [711, 712]),
    ("pol_executive_offices", "Indian Polity: Executive Offices — Council of Ministers & Attorney General", "Indian Polity",
     ["Council of Ministers ranks Cabinet MoS Deputy Minister Constitution",
      "15 percent cap total ministers Lok Sabha 91st Amendment",
      "Attorney General India Solicitor General Parliament meetings resignation",
      "Constitutional body vs statutory body India examples"],
     ["statement_subtle_inversion", "statement_overgeneralization"],
     [793, 978]),
    ("pol_parliament_lok_sabha", "Indian Polity: Lok Sabha — Exclusive Powers, Deputy Speaker & Anti-Defection", "Indian Polity",
     ["Lok Sabha exclusive powers no-confidence motion Emergency ratification",
      "Deputy Speaker Lok Sabha election rules presiding powers",
      "Anti-defection law Tenth Schedule nominated legislators time-frame"],
     ["statement_subtle_inversion", "statement_overgeneralization"],
     [854, 855, 856]),
    ("pol_judiciary_contempt_writs", "Indian Polity: Judiciary — Contempt of Court, Writs & Bar Council", "Indian Polity",
     ["Contempt of Courts Act 1971 HN Sanyal Committee civil criminal contempt",
      "Mandamus Quo Warranto writs India private organisation government company",
      "Bar Council legal education advocates recognition India"],
     ["statement_subtle_inversion", "overlapping_categories", "technical_vs_common_meaning"],
     [916, 917, 918]),
    ("pol_india_international_membership", "Indian Polity: India's International Memberships — AIIB, MTCR, SCO", "Indian Polity",
     ["India AIIB MTCR SCO membership",
      "Asian Infrastructure Investment Bank Missile Technology Control Regime Shanghai Cooperation Organisation India"],
     ["overlapping_categories", "distractor_by_topic_association"],
     [1006]),

    # --- Indian Economy (20 PYQs, 8 clusters) ---
    ("eco_real_sector_macroeconomy", "Indian Economy: Real Sector vs Financial Sector — Macroeconomic Concepts", "Indian Economy",
     ["Real sector economy agriculture manufacturing vs financial sector",
      "Household financial savings government borrowing dated securities"],
     ["technical_vs_common_meaning", "statement_partial_truth"],
     [1096, 1142]),
    ("eco_rbi_monetary_exchange", "Indian Economy: RBI Monetary Policy, Exchange Rates & Inflation", "Indian Economy",
     ["RBI inflation control price stability Open Market Operations",
      "NEER REER rupee appreciation trade competitiveness",
      "US Federal Reserve tight monetary policy capital flight ECB",
      "RBI sell dollars rupee depreciation interest rates"],
     ["statement_subtle_inversion", "distractor_by_topic_association"],
     [1201, 1202, 1203, 1204]),
    ("eco_banking_credit_institutions", "Indian Economy: Banking — Credit Rating Agencies & Banks Board Bureau", "Indian Economy",
     ["Credit rating agencies ICRA Brickwork Ratings SEBI vs RBI regulation",
      "Banks Board Bureau BBB chairman RBI governor public sector banks"],
     ["overlapping_categories", "person_attribution"],
     [1274, 1275]),
    ("eco_capital_markets_bonds", "Indian Economy: Capital Markets — Inflation-Indexed Bonds, Indirect Transfers & Convertible Bonds", "Indian Economy",
     ["Inflation-Indexed Bonds IIB coupon rates tax treatment",
      "Indirect transfer shares substantial value India tax",
      "Convertible bonds equity conversion lower interest rate"],
     ["statement_partial_truth", "technical_vs_common_meaning", "statement_subtle_inversion"],
     [1339, 1340, 1341]),
    ("eco_industries_expenditure_labour", "Indian Economy: Industries — Capital Expenditure, Labour Bureau & Coal Controller", "Indian Economy",
     ["Capital expenditure vs revenue expenditure technology acquisition",
      "Labour Bureau industrial disputes retrenchments closures India",
      "Coal Controller Organisation CCO coal statistics captive blocks"],
     ["statement_subtle_inversion", "distractor_by_topic_association", "overlapping_categories"],
     [1377, 1378, 1379]),
    ("eco_international_orgs_imf_g20", "Indian Economy: International Economic Organisations — IMF & G20 Framework", "Indian Economy",
     ["IMF Rapid Financing Instrument Rapid Credit Facility",
      "G20 Common Framework Paris Club low income countries debt"],
     ["distractor_by_topic_association", "statement_partial_truth"],
     [1454, 1455]),
    ("eco_welfare_schemes_health", "Indian Economy: Welfare Schemes — Ayushman Bharat Digital & India Sanitation Coalition", "Indian Economy",
     ["Ayushman Bharat Digital Mission ABDM portability universal coverage",
      "India Sanitation Coalition funding National Institute of Urban Affairs Ministry"],
     ["statement_overgeneralization", "statement_subtle_inversion"],
     [1530, 1531]),
    ("eco_agriculture_commodities", "Indian Economy: Agriculture — Tea Board & E-commerce Regulation", "Indian Economy",
     ["Tea Board India statutory body Ministry Commerce headquarters Kolkata",
      "Foreign-owned e-commerce firms India marketplace own goods FDI policy"],
     ["geographic_attribution", "technical_vs_common_meaning"],
     [1593, 1630]),

    # --- Geography (10 PYQs, 3 clusters) ---
    ("geo_celestial_atmosphere", "Geography: Celestial Mechanics & Atmospheric Physics — Solstice & Clouds", "Geography",
     ["Longest day northern hemisphere summer solstice June",
      "Solar declination June 21 equinox solstice",
      "High clouds low clouds solar radiation infrared absorption warming cooling Earth",
      "Cloud albedo greenhouse effect atmosphere climatology"],
     ["numerical_proximity", "statement_subtle_inversion"],
     [1682, 1726]),
    ("geo_indian_landforms_resources", "Indian Geography: Peaks, Minerals, Wetlands & Crop Belts", "Geography",
     ["Namcha Barwa Nanda Devi Nokrek mountain range matching",
      "Monazite rare earths thorium coastal sand India distribution",
      "Hokera Renuka Rudrasagar Sasthamkotta wetland lake state matching",
      "Ghataprabha Gandhi Sagar Indira Sagar Maithon reservoir state",
      "Tea producing states India Andhra Pradesh Kerala Himachal Tripura"],
     ["geographic_attribution", "famous_association_bias", "statement_overgeneralization"],
     [1826, 1849, 1876, 1877, 1951]),
    ("geo_world_features_borders", "World Geography: African Lakes, Indian Canyons & Central Asian Borders", "Geography",
     ["Lake Faguibine West Africa desertification",
      "Gandikota canyon Pennar river South India",
      "Afghanistan borders Tajikistan Turkmenistan Uzbekistan Central Asia"],
     ["famous_association_bias", "geographic_attribution"],
     [2041, 2042, 2078]),

    # --- Environment (17 PYQs, 6 clusters) ---
    ("env_aquatic_ecosystems_conservation", "Environment: Aquatic Ecosystems — Wetland Functions & Coral Reef Restoration", "Environment",
     ["Wetlands kidneys of Earth heavy metals nutrient absorption aquatic plants",
      "Wetland functions filtration sedimentation nutrient cycling",
      "Biorock technology coral reef restoration electrolytic deposition",
      "Coral reef restoration techniques marine conservation"],
     ["distractor_by_topic_association", "technical_vs_common_meaning"],
     [2130, 2170]),
    ("env_biodiversity_species", "Environment: Biodiversity — Fungi Cultivators, Gucchi & Species Identification", "Environment",
     ["Ants fungi cultivators leafcutter ants",
      "Gucchi Morchella fungus Himalayan forest commercial cultivation",
      "Golden Mahseer fish bird identification"],
     ["famous_association_bias", "statement_subtle_inversion", "negation_trap"],
     [2167, 2168, 2169]),
    ("env_pollution_air_nanoparticles", "Environment: Air Pollution — Acid Rain, WHO Air Quality & Nanoparticles", "Environment",
     ["Acid rain nitrogen oxide sulphur dioxide causes",
      "WHO Air Quality Guidelines PM2.5 PM10 ozone standards",
      "Nanoparticles natural vs synthetic metallic oxides cosmetics safety"],
     ["technical_vs_common_meaning", "statement_subtle_inversion", "statement_overgeneralization"],
     [2248, 2249, 2250]),
    ("env_agriculture_climate_nitrogen", "Environment: Agriculture-Climate Interactions — GHGs, SRI & Nitrogen-Fixing Plants", "Environment",
     ["Rice methane nitrous oxide anthropogenic GHG emissions",
      "System of Rice Intensification SRI alternate wetting drying methane seed",
      "Nitrogen-fixing plants legumes alfalfa chickpea clover",
      "Biological nitrogen fixation nodules symbiosis"],
     ["overlapping_categories", "statement_partial_truth", "technical_vs_common_meaning"],
     [2293, 2423, 2424]),
    ("env_conservation_law_india", "Environment: Indian Conservation Laws — Environment Protection Act & Wildlife Protection", "Environment",
     ["Environment Protection Act 1986 Central Ground Water Authority",
      "Wildlife Protection Act India protected animals outside protected areas"],
     ["overlapping_categories", "statement_overgeneralization"],
     [2321, 2322]),
    ("env_climate_action_renewables", "Environment: Climate Action & Renewables — CAT, EP100, Miyawaki & Solar Power", "Environment",
     ["Climate Action Tracker research coalition emission reduction monitoring",
      "EP100 International Energy Agency Climate Group energy efficiency",
      "Miyawaki method mini forests urban areas",
      "Largest solar park India Gujarat Kerala Rajasthan",
      "Solar powered airport India Cochin Kerala floating solar photovoltaic"],
     ["overlapping_categories", "person_attribution", "geographic_attribution"],
     [2386, 2387, 2388, 2452]),

    # --- Science and Technology (14 PYQs, 5 clusters) ---
    ("sci_digital_tech_blockchain", "Sci-Tech: Digital Technology — NFTs, Web 3.0 & Open-Source Platforms", "Science and Technology",
     ["NFT Non-Fungible Token blockchain cryptocurrency fungible",
      "Web 3.0 decentralized user-controlled data blockchain social networks",
      "Aarogya Setu CoWIN DigiLocker DIKSHA open-source digital platforms"],
     ["statement_subtle_inversion", "statement_partial_truth"],
     [2470, 2471, 2472]),
    ("sci_saas_communication_tech", "Sci-Tech: SaaS, RFID & Short-Range Communication Technologies", "Science and Technology",
     ["Software as a Service SaaS customisation data access examples",
      "RFID CCTV WLAN short-range communication devices classification"],
     ["technical_vs_common_meaning"],
     [2473, 2474]),
    ("sci_space_defence", "Sci-Tech: Space Science & Defence — Solar Flares & FOBS", "Science and Technology",
     ["Solar flare effects GPS power grids aurora satellite orbits polar radio",
      "Fractional Orbital Bombardment System FOBS missile orbit deorbit"],
     ["distractor_by_topic_association", "technical_vs_common_meaning"],
     [2510, 2511]),
    ("sci_biotechnology_genomics", "Sci-Tech: Biotechnology — DNA Barcoding, COVID Vaccines & Biofilms", "Science and Technology",
     ["DNA barcoding species identification food authentication age",
      "COVID-19 vaccines Covishield mRNA Sputnik V vector COVAXIN inactivated",
      "Biofilms medical implants antibiotic resistance food surfaces"],
     ["statement_subtle_inversion", "person_attribution", "statement_partial_truth"],
     [2582, 2583, 2584]),
    ("sci_physics_chemistry_biology", "Sci-Tech: Physics, Chemistry & Biology — Qubit, PET & Immune Cells", "Science and Technology",
     ["Qubit quantum computing superposition",
      "Polyethylene terephthalate PET fibres recycling incineration alcohol",
      "B cells T cells immunity pathogens",
      "Probiotics bacteria yeast gut microbiome lactose digestion"],
     ["distractor_by_topic_association", "statement_overgeneralization", "statement_subtle_inversion"],
     [2624, 2644, 2657, 2658]),

    # --- Current Affairs and GK (12 PYQs, 3 clusters) ---
    ("ca_international_orgs_memberships", "Current Affairs: International Organisations & Maritime Law", "Current Affairs and GK",
     ["UN Credentials Committee General Assembly Security Council meetings",
      "Polar Code IMO ships polar waters safety",
      "UN General Assembly observer status inter-governmental organisations",
      "UNCLOS territorial sea EEZ innocent passage 12 200 nautical miles",
      "Organization of Turkic States members Azerbaijan Uzbekistan Kazakhstan"],
     ["statement_subtle_inversion", "statement_partial_truth", "geographic_attribution"],
     [2744, 2745, 2746, 2747, 2748]),
    ("ca_global_geopolitics_gk", "Current Affairs: Global Geopolitics & Geographic Knowledge", "Current Affairs and GK",
     ["Vietnam economy Communist single-party supply chains",
      "Levant eastern Mediterranean region geography",
      "Global events Chad Guinea Lebanon Tunisia 2021 country-pair matching",
      "Anatolia Amhara Cabo Delgado Catalonia region-country matching",
      "Senkaku Islands East China Sea Japan China dispute",
      "Bidibidi refugee settlement Uganda South Sudan Dadaab Somalia Kenya"],
     ["geographic_attribution", "statement_overgeneralization", "statement_partial_truth"],
     [2793, 2794, 2795, 2796, 2797, 2798]),
    ("ca_environment_gk", "Current Affairs: Corporate Sustainability — Greenwashing", "Current Affairs and GK",
     ["Greenwashing false eco-friendly claims corporate sustainability",
      "Green marketing misleading environmental claims"],
     ["technical_vs_common_meaning"],
     [2799]),
]



def detect_question_type(question: str, options: dict) -> str:
    import re
    q_norm = ((question or "")
              .replace("Statement-I", "Statement I")
              .replace("Statement-II", "Statement II")
              .replace("Statement-III", "Statement III"))
    qlow = q_norm.lower()
    opt_vals = " ".join(str(v).lower() for v in (options or {}).values())
    if ("statement i" in qlow and "statement ii" in qlow and
        ("explanation" in opt_vals or "explains" in opt_vals)):
        return "assertion_reason"
    if "following pairs" in qlow or "pairs:" in qlow:
        return "matching"
    if "statement i" in qlow and "statement ii" in qlow:
        return "statement_eval"
    if "consider the following statements" in qlow or "consider the following information" in qlow:
        return "statement_eval"
    has_list = (re.search(r"(^|\s)1\.\s*\S", q_norm) and re.search(r"(^|\s)2\.\s*\S", q_norm))
    multi_select = "only" in opt_vals and ("and" in opt_vals or "," in opt_vals)
    if "consider the following" in qlow and has_list:
        return "statement_eval"
    if has_list and multi_select:
        return "statement_eval"
    if re.search(r"\bI\.\s", q_norm) and re.search(r"\bII\.\s", q_norm):
        return "statement_eval"
    return "standard"


def load_year_pyqs():
    idx = json.load(open(INDEX))
    return [p for p in idx["pyqs"] if p.get("year") == YEAR]


# ---- Trap-pattern tagging (Sonnet-drafted, Opus-reviewed) ----
TRAP_TAGS: dict = {
    "90": "statement_partial_truth",
    "124": "person_attribution",
    "132": "geographic_attribution",
    "133": "person_attribution",
    "181": "statement_overgeneralization",
    "208": "famous_association_bias",
    "209": "overlapping_categories",
    "210": "person_attribution",
    "248": "technical_vs_common_meaning",
    "249": "period_attribution",
    "250": "technical_vs_common_meaning",
    "312": "geographic_attribution",
    "323": "period_attribution",
    "462": "statement_subtle_inversion",
    "553": "statement_subtle_inversion",
    "638": "famous_association_bias",
    "711": "statement_subtle_inversion",
    "712": "overlapping_categories",
    "793": "statement_subtle_inversion",
    "854": "statement_subtle_inversion",
    "855": "statement_overgeneralization",
    "856": "statement_subtle_inversion",
    "916": "statement_subtle_inversion",
    "917": "statement_subtle_inversion",
    "918": "statement_subtle_inversion",
    "978": "statement_overgeneralization",
    "1006": "overlapping_categories",
    "1096": "technical_vs_common_meaning",
    "1142": "statement_partial_truth",
    "1201": "distractor_by_topic_association",
    "1202": "statement_subtle_inversion",
    "1203": "statement_subtle_inversion",
    "1204": "statement_subtle_inversion",
    "1274": "overlapping_categories",
    "1275": "person_attribution",
    "1339": "statement_partial_truth",
    "1340": "technical_vs_common_meaning",
    "1341": "statement_subtle_inversion",
    "1377": "statement_subtle_inversion",
    "1378": "distractor_by_topic_association",
    "1379": "overlapping_categories",
    "1454": "distractor_by_topic_association",
    "1455": "statement_partial_truth",
    "1530": "statement_overgeneralization",
    "1531": "statement_subtle_inversion",
    "1593": "geographic_attribution",
    "1630": "technical_vs_common_meaning",
    "1682": "numerical_proximity",
    "1726": "statement_subtle_inversion",
    "1826": "geographic_attribution",
    "1849": "statement_overgeneralization",
    "1876": "geographic_attribution",
    "1877": "geographic_attribution",
    "1951": "famous_association_bias",
    "2041": "famous_association_bias",
    "2042": "famous_association_bias",
    "2078": "geographic_attribution",
    "2130": "distractor_by_topic_association",
    "2167": "famous_association_bias",
    "2168": "statement_subtle_inversion",
    "2169": "negation_trap",
    "2170": "distractor_by_topic_association",
    "2248": "technical_vs_common_meaning",
    "2249": "statement_subtle_inversion",
    "2250": "statement_overgeneralization",
    "2293": "overlapping_categories",
    "2321": "overlapping_categories",
    "2322": "statement_overgeneralization",
    "2386": "overlapping_categories",
    "2387": "person_attribution",
    "2388": "distractor_by_topic_association",
    "2423": "technical_vs_common_meaning",
    "2424": "statement_partial_truth",
    "2452": "geographic_attribution",
    "2470": "statement_subtle_inversion",
    "2471": "statement_partial_truth",
    "2472": "statement_partial_truth",
    "2473": "technical_vs_common_meaning",
    "2474": "technical_vs_common_meaning",
    "2510": "distractor_by_topic_association",
    "2511": "technical_vs_common_meaning",
    "2582": "statement_subtle_inversion",
    "2583": "person_attribution",
    "2584": "statement_partial_truth",
    "2624": "distractor_by_topic_association",
    "2644": "statement_overgeneralization",
    "2657": "distractor_by_topic_association",
    "2658": "statement_subtle_inversion",
    "2744": "statement_subtle_inversion",
    "2745": "technical_vs_common_meaning",
    "2746": "statement_partial_truth",
    "2747": "geographic_attribution",
    "2748": "statement_partial_truth",
    "2793": "statement_overgeneralization",
    "2794": "geographic_attribution",
    "2795": "statement_partial_truth",
    "2796": "geographic_attribution",
    "2797": "geographic_attribution",
    "2798": "geographic_attribution",
    "2799": "technical_vs_common_meaning",
}


# Discrimination cards — drafted by Sonnet agents, merged by Opus.
DISCRIMINATION_CARDS: dict = {
}


# Merge overlays (cards drafted by Sonnet, written to scratch JSON). Any
# calibration_cards.json / wave1_*.json / wave2_*.json picked up automatically.
_SCRATCH = ROOT / ".scratch" / "drill_2022"
if _SCRATCH.exists():
    for _f in sorted(_SCRATCH.glob("calibration_cards.json")):
        DISCRIMINATION_CARDS.update(json.loads(_f.read_text()))
    for _f in sorted(_SCRATCH.glob("wave1*.json")):
        DISCRIMINATION_CARDS.update(json.loads(_f.read_text()))
    for _f in sorted(_SCRATCH.glob("wave2*.json")):
        DISCRIMINATION_CARDS.update(json.loads(_f.read_text()))


def build_clusters_json(pyq_meta):
    out = {
        "metadata": {
            "year": YEAR,
            "subject_filter": "GS Paper 1",
            "n_clusters": len(CLUSTERS),
            "n_pyqs": sum(len(c[5]) for c in CLUSTERS),
        },
        "clusters": [
            {"cluster_id": cid, "title": title, "subject_focus": subj,
             "study_keywords": kws, "common_traps": traps, "linked_pyqs": pyqs}
            for cid, title, subj, kws, traps, pyqs in CLUSTERS
        ],
        "pyq_meta": pyq_meta,
    }
    OUT_CLUSTERS.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    return out


def build_pyq_meta(pyqs):
    out = {}
    for p in pyqs:
        pid = str(p["pyq_id"])
        qtype = detect_question_type(p.get("question", ""), p.get("options", {}))
        out[pid] = {
            "question_type": qtype,
            "trap_pattern": TRAP_TAGS.get(pid),
        }
    for pid, card in DISCRIMINATION_CARDS.items():
        if pid in out:
            out[pid]["question_type"] = card.get("question_type", out[pid]["question_type"])
            out[pid]["trap_pattern"] = card.get("trap_pattern", out[pid]["trap_pattern"])
    return out


def build_cards_json():
    out = {
        "metadata": {
            "drafted_count": len(DISCRIMINATION_CARDS),
            "drafted_by": "pending",
            "year": YEAR,
        },
        "cards": DISCRIMINATION_CARDS,
    }
    OUT_CARDS.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    return out


def main():
    idx = json.load(open(INDEX))
    valid = {p["pyq_id"] for p in idx["pyqs"] if p.get("year") == YEAR}
    clustered = set()
    for c in CLUSTERS:
        for pid in c[5]:
            if pid in clustered:
                raise SystemExit(f"PYQ {pid} clustered twice")
            if pid not in valid:
                raise SystemExit(f"PYQ {pid} not in {YEAR} index")
            clustered.add(pid)
    missing = valid - clustered
    if missing:
        print(f"WARNING: {len(missing)} {YEAR} PYQs not clustered: {sorted(missing)}")
    print(f"clustered {len(clustered)}/{len(valid)} {YEAR} PYQs into {len(CLUSTERS)} clusters")

    pyqs = load_year_pyqs()
    pyq_meta = build_pyq_meta(pyqs)
    co = build_clusters_json(pyq_meta)
    cards = build_cards_json()

    from collections import Counter
    qtype_dist = Counter(m["question_type"] for m in pyq_meta.values())
    trap_dist = Counter(m.get("trap_pattern") for m in pyq_meta.values())
    trap_tagged = sum(1 for m in pyq_meta.values() if m.get("trap_pattern"))

    print(f"wrote {OUT_CLUSTERS} ({co['metadata']['n_clusters']} clusters, {co['metadata']['n_pyqs']} pyqs)")
    print(f"wrote {OUT_CARDS} ({cards['metadata']['drafted_count']} discrimination cards)")
    print(f"question_type distribution: {dict(qtype_dist)}")
    print(f"trap_pattern tagged: {trap_tagged}/{len(pyq_meta)}")
    print("trap_pattern distribution:")
    for tag, n in trap_dist.most_common():
        print(f"  {n:3d}  {tag}")


if __name__ == "__main__":
    main()
