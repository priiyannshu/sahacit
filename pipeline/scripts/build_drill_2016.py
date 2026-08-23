#!/usr/bin/env python3
"""
Generate app/pwa/data/drill_clusters_2016.json
       + app/pwa/data/discrimination_cards_2016.json

Cluster map covers all 100 GS1 2016 PYQs. Sonnet drafted 30 clusters in-conv;
Opus QC'd at STOP-1 with no merges. The 30-cluster count sits at the bottom of
the 30-42 target band — driven by 2016's heavily skewed subject distribution
(28 Economy, 17 CA, 17 Environment, only 3 Geography, only 4 Medieval). Sonnet
flagged three 2-PYQ singleton-ish clusters (anc_places_regions [83,117],
anc_monuments_epigraphy [140,141], pol_parliament_bills [870,871],
ca_communities_persons [2823,2824]) with merge suggestions; Opus declined all
merges as the singletons capture genuinely distinct skill classes (places vs
monuments-and-inscriptions; parliamentary-procedure vs admin-and-local;
community-ID is its own discrimination skill). No singletons retained
(every cluster has ≥2 PYQs). All 100 PYQs covered.

Trap-tag QC: 16 all-true-answer cases (117, 258, 342, 1148, 1297, 1350, 1473,
1539, 1852, 1887, 2397, 2491, 2665, 2758, 2818, 2819) correctly tagged
statement_partial_truth — the 2428 (2020) lesson held. No retags applied.

Pre-2023 year, no assertion_reason questions — explanatory_chain count = 0.

Discrimination cards drafted by Sonnet in-conv (v2.1, no sub-agents); merged
via auto-overlay glob (wave1*.json + wave2*.json from .scratch/drill_2016/).
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "pwa" / "data" / "pyq_index.json"
OUT_CLUSTERS = ROOT / "pwa" / "data" / "drill_clusters_2016.json"
OUT_CARDS = ROOT / "pwa" / "data" / "discrimination_cards_2016.json"

YEAR = 2016

# Cluster definitions for all 100 2016 PYQs.
# Format: (cluster_id, title, subject_focus, study_keywords[], common_traps[], pyq_ids[])
CLUSTERS: list = [
    # --- Ancient Indian History (7 PYQs, 3 clusters) ---
    ("anc_places_regions", "Ancient India: Famous Places-Regions & South Indian Administrative Terms — Bodhgaya, Khajuraho, Eripatti, Taniyurs, Ghatikas", "Ancient Indian History",
     ["Bodhgaya Khajuraho Shirdi Nasik Tirupati regional geography",
      "Eripatti village tank land revenue South India",
      "Taniyurs Brahmin settlements Tamil Nadu ancient",
      "Ghatikas temple colleges ancient India education",
      "Chola Pallava administrative terms South India"],
     ["geographic_attribution", "statement_partial_truth"],
     [83, 117]),
    ("anc_monuments_epigraphy", "Ancient India: Ashoka Epigraphy (Prinsep) & Rock-Cut Monuments (Ajanta vs Mahabalipuram)", "Ancient Indian History",
     ["James Prinsep Ashoka edicts Brahmi script decipherment 1837",
      "Ajanta caves Buddhist Mahayana Maharashtra Vakataka",
      "Mahabalipuram Pallava rock-cut temples Shore Temple",
      "Ajanta Mahabalipuram comparison period denomination rock-cut"],
     ["famous_association_bias", "statement_subtle_inversion"],
     [140, 141]),
    ("anc_religion_literature", "Ancient India: Sunga Literature (Malavikagnimitra), Bodhisattva Concept & Maagadha Profession", "Ancient Indian History",
     ["Malavikagnimitra Kalidasa Agnimitra Sunga dynasty love story",
      "Bodhisattva Mahayana Buddhism compassionate enlightenment Hinayana distinction",
      "Maagadha bard chronicler dynastic histories ancient India profession",
      "Shramana Parivrajaka wandering ascetics ancient social roles"],
     ["distractor_by_topic_association", "statement_subtle_inversion"],
     [185, 219, 220]),

    # --- Medieval Indian History (4 PYQs, 1 cluster) ---
    ("med_society_economy", "Medieval India: Banjaras (Traders), Araghatta (Waterwheel), Vijayanagar Tax & Siddhas/Lingayats", "Medieval Indian History",
     ["Banjaras medieval traders transport merchants India",
      "Araghatta waterwheel irrigation medieval India technology",
      "Krishnadeva Raya Vijayanagar tax system land quality industries tax",
      "Siddhas Tamil monotheism idolatry Lingayats Kannada rebirth caste"],
     ["distractor_by_topic_association", "technical_vs_common_meaning", "statement_partial_truth"],
     [256, 257, 258, 342]),

    # --- Modern Indian History (6 PYQs, 2 clusters) ---
    ("mod_social_reform", "Modern India: Keshab Chandra Sen's Organisations & Satya Shodhak Samaj (Phule, Maharashtra)", "Modern Indian History",
     ["Keshab Chandra Sen Tabernacle New Dispensation Indian Reform Association",
      "Calcutta Unitarian Committee Rammohun Roy not Keshab",
      "Satya Shodhak Samaj Jyotirao Phule Maharashtra anti-caste movement",
      "Brahmo Samaj splinter factions 19th century social reform"],
     ["person_attribution", "geographic_attribution"],
     [406, 610]),
    ("mod_political_events", "Modern India: Swadeshi/Boycott Origins, Surat Split 1907, Montagu-Chelmsford & Cripps Mission", "Modern Indian History",
     ["Swadeshi Boycott Partition Bengal 1905 first time agitation",
      "Surat Split 1907 INC Extremists Moderates Tilak Gokhale",
      "Montagu-Chelmsford Proposals 1919 constitutional reforms dyarchy",
      "Cripps Mission 1942 Dominion status not independence Stafford Cripps"],
     ["first_or_only", "distractor_by_topic_association", "famous_association_bias"],
     [423, 424, 468, 559]),

    # --- Indian Polity (11 PYQs, 4 clusters) ---
    ("pol_parliament_bills", "Polity: Parliament — State List Legislation (Rajya Sabha 2/3) & Bill Lapse Rules (Prorogation vs Dissolution)", "Indian Polity",
     ["Parliament State List Article 249 Rajya Sabha two-thirds majority present voting",
      "Bill lapse Lok Sabha prorogation dissolution difference",
      "Rajya Sabha pending bill does not lapse Lok Sabha dissolution",
      "parliamentary procedure lapsing bills India Constitution"],
     ["statement_subtle_inversion"],
     [870, 871]),
    ("pol_local_bodies_admin", "Polity: Chief Secretary Appointment, Gram Nyayalaya Act & Panchayat Member Age/Tenure", "Indian Polity",
     ["Chief Secretary appointment state Governor Chief Minister no fixed tenure",
      "Gram Nyayalaya Act civil criminal cases mediators local activists",
      "Panchayat member minimum age 21 years Constitution 73rd Amendment",
      "reconstituted Panchayat premature dissolution remainder period"],
     ["statement_subtle_inversion"],
     [796, 923, 1073]),
    ("pol_india_multilateral", "Polity/IR: Trans-Pacific Partnership, India-Africa Forum Summit & International Solar Alliance", "Indian Polity",
     ["Trans-Pacific Partnership TPP not all Pacific Rim China Russia not maritime security",
      "India-Africa Forum Summit 2015 third summit history 2008 not Nehru",
      "International Solar Alliance ISA UNFCCC Paris 2015 tropical countries not all UN"],
     ["statement_subtle_inversion", "statement_overgeneralization"],
     [1014, 1015, 1019]),
    ("pol_intl_orgs_terms", "Polity/IR: Gulf Cooperation Council, Belt & Road Initiative & RCEP — Who Belongs Where", "Indian Polity",
     ["Gulf Cooperation Council GCC members Iran not included Saudi Arabia Oman Kuwait",
      "Belt Road Initiative BRI China One Belt One Road",
      "Regional Comprehensive Economic Partnership RCEP ASEAN led not G20 SCO SAARC"],
     ["negation_trap", "distractor_by_topic_association"],
     [1016, 1017, 1018]),

    # --- Indian Economy (28 PYQs, 8 clusters) ---
    ("eco_budget_fiscal", "Economy: Government Budget — Deficit Reduction Measures, Capital Budget Components & BEPS", "Indian Economy",
     ["fiscal deficit reduction revenue expenditure subsidy rationalization India",
      "capital budget expenditure assets foreign loans advances states India",
      "Base Erosion Profit Shifting BEPS OECD multinational tax evasion not mining"],
     ["statement_subtle_inversion", "technical_vs_common_meaning", "statement_partial_truth"],
     [1147, 1148, 1185]),
    ("eco_monetary_bonds", "Economy: Import Cover (RBI), MCLR, Sovereign Gold Bonds & IFC Masala Bonds", "Indian Economy",
     ["import cover months imports international reserves definition RBI",
      "MCLR Marginal Cost Funds Lending Rate transparency fair rate borrowers banks",
      "Sovereign Gold Bond Scheme Gold Monetization Scheme reduce imports idle gold",
      "IFC Masala Bonds World Bank rupee denominated debt financing"],
     ["technical_vs_common_meaning", "statement_subtle_inversion", "statement_partial_truth"],
     [1217, 1297, 1349, 1350]),
    ("eco_banking_inclusion", "Economy: Core Banking, Atal Pension Yojana, MUDRA & Payment Banks", "Indian Economy",
     ["Core Banking Solutions networking branches anywhere not RBI control not NPA",
      "Atal Pension Yojana unorganized sector spouse pension not both-spouse exclusion",
      "MUDRA Micro Units Development Refinance Agency small entrepreneurs formal system",
      "Payment Banks debit card only no credit cards no lending mobile supermarket"],
     ["distractor_by_topic_association", "statement_subtle_inversion"],
     [1295, 1296, 1298, 1299]),
    ("eco_industries_agri", "Economy: NIMZ Andhra Pradesh, UDAY Power Discoms, Millets INSIMP & PMFBY Crop Insurance", "Indian Economy",
     ["National Investment Manufacturing Zone NIMZ first Andhra Pradesh not Gujarat Maharashtra",
      "UDAY financial turnaround power distribution companies discoms not renewable energy",
      "INSIMP millets promotion cluster approach small tribal farmers post-harvest",
      "Pradhan Mantri Fasal Bima Yojana PMFBY non-uniform premium post-harvest cyclone"],
     ["geographic_attribution", "distractor_by_topic_association", "statement_subtle_inversion"],
     [1386, 1387, 1606, 1607]),
    ("eco_intl_trade_development", "Economy: GIAHS FAO Heritage Farming, New Development Bank (BRICS not APEC) & Global Financial Stability Report", "Indian Economy",
     ["GIAHS Globally Important Agricultural Heritage System FAO safeguard not modernize not GI",
      "New Development Bank NDB BRICS not APEC Shanghai headquarters",
      "Global Financial Stability Report GFSR IMF not ECB not World Bank not OECD"],
     ["distractor_by_topic_association", "statement_subtle_inversion"],
     [1468, 1469, 1470]),
    ("eco_intl_monetary_finance", "Economy: WTO Amber/Blue/Green Boxes, SDR Yuan Addition & IMFC — IMF Governance Bodies", "Indian Economy",
     ["WTO amber box blue box green box agricultural subsidies trade distorting",
      "IMF Special Drawing Rights SDR basket Yuan Renminbi 2015 addition",
      "IMFC International Monetary Financial Committee advises IMF World Bank observer"],
     ["distractor_by_topic_association", "statement_partial_truth"],
     [1471, 1472, 1473]),
    ("eco_welfare_schemes", "Economy: SWAYAM (Education), Stand Up India, Mission Indradhanush & Rashtriya Garima Abhiyan", "Indian Economy",
     ["SWAYAM free online education MOOCs Digital India not SHG not start-up",
      "Stand Up India SC ST women entrepreneurs SIDBI refinance",
      "Mission Indradhanush immunization children pregnant women not smart cities",
      "Rashtriya Garima Abhiyan manual scavenging eradication rehabilitation"],
     ["distractor_by_topic_association", "statement_partial_truth"],
     [1538, 1539, 1540, 1541]),
    ("eco_institutions_laws", "Economy: Food Labelling Mandatory Items, District Mineral Foundations & FSDC", "Indian Economy",
     ["Food Safety Standards Packaging Labelling 2011 mandatory ingredients nutrition veg non-veg",
      "District Mineral Foundations DMF protect mining-affected persons not exploration not licensing",
      "Financial Stability Development Council FSDC Finance Minister head not NITI Aayog macro-prudential"],
     ["distractor_by_topic_association", "statement_subtle_inversion"],
     [1639, 1640, 1641]),

    # --- Geography (3 PYQs, 1 cluster) ---
    ("geo_india_physical", "Geography: Gadgil/Kasturirangan Western Ghats, Shale Gas Basins & Brahmaputra Tributaries", "Geography",
     ["Gadgil Committee Kasturirangan Committee Western Ghats protection environment",
      "shale gas India Cambay Cauvery Krishna-Godavari Basin unconventional energy",
      "Brahmaputra tributaries Dibang Kameng Lohit rivers Arunachal Pradesh"],
     ["distractor_by_topic_association", "statement_partial_truth"],
     [1829, 1852, 1887]),

    # --- Environment (17 PYQs, 4 clusters) ---
    ("env_biodiversity_species", "Environment: Kharai Camel, New Banana Species, Red Sanders Forest Type & Great Indian Hornbill", "Environment",
     ["Kharai camel swimming mangroves Gujarat Kutch domesticated not wild only",
      "new banana species Musa flaviflora Andaman orange pulp 11 metre",
      "Red Sanders Pterocarpus santalinus South India dry deciduous not rainforest",
      "Great Indian Hornbill Western Ghats habitat Buceros bicornis"],
     ["statement_subtle_inversion", "geographic_attribution"],
     [2184, 2185, 2186, 2187]),
    ("env_pollution_conservation", "Environment: AQI Gases (Not CO2/CH4), NGRBA Chairman (PM not CM), Green India Mission & Drip Irrigation/Neem Urea", "Environment",
     ["Air Quality Index AQI parameters CO NO2 SO2 not CO2 not methane CPCB",
      "National Ganga River Basin Authority NGRBA PM chairman not rotating CM river basin",
      "Green India Mission restore forest cover climate adaptation mitigation not green accounting",
      "drip irrigation weed reduction erosion reduction not salinity reduction",
      "neem-coated urea slow dissolution not nitrogen fixation"],
     ["technical_vs_common_meaning", "statement_subtle_inversion", "distractor_by_topic_association"],
     [2266, 2339, 2340, 2431, 2432]),
    ("env_global_climate_protocols", "Environment: TEEB (UNEP not IMF), UN-REDD+ Benefits, CER/CDM/Annex-I Protocol Pairs & GHG Protocol", "Environment",
     ["TEEB Economics Ecosystems Biodiversity UNEP hosted not IMF not WEF",
      "UN-REDD+ biodiversity resilience poverty reduction deforestation",
      "Annex-I countries UNFCCC Certified Emissions Reductions CDM Kyoto Protocol origin",
      "Greenhouse Gas Protocol private accounting standard not inter-government treaty"],
     ["statement_subtle_inversion", "overlapping_categories", "technical_vs_common_meaning"],
     [2396, 2397, 2398, 2399]),
    ("env_paris_sdgs", "Environment: Agenda 21 (Rio 1992 not Johannesburg), Paris Agreement Details, SDGs Origin & INDC Meaning", "Environment",
     ["Agenda 21 Rio Earth Summit 1992 not Johannesburg 2002 sustainable development plan",
      "Paris Agreement 2015 2 degree 1.5 degree not all UN members $100 billion not $1000 billion",
      "Sustainable Development Goals SDGs 2030 UN Rio+20 2012 not Club of Rome 1972",
      "Intended Nationally Determined Contributions INDC climate action pledges countries"],
     ["statement_subtle_inversion", "distractor_by_topic_association"],
     [2400, 2401, 2402, 2403]),

    # --- Science and Technology (7 PYQs, 2 clusters) ---
    ("sci_space", "S&T: GL-10 NASA Electric Plane, Astrosat (Neither Statement), Mangalyaan 4th Country (Not 2nd)", "Science and Technology",
     ["Greased Lightning GL-10 NASA electric propulsion tilt-rotor aircraft not Japan not ISRO",
      "Astrosat India space observatory other countries also have not unique 1650 kg not 2000 kg",
      "Mangalyaan Mars Orbiter Mission MOM India 4th not 2nd after USA USSR ESA first attempt"],
     ["distractor_by_topic_association", "statement_subtle_inversion"],
     [2523, 2524, 2525]),
    ("sci_tech_life_sciences", "S&T: Li-Fi (Light Wireless), Transcriptome (mRNA), ITER Fusion Reactor & Viruses (Bacteria/Fungi/Plants)", "Science and Technology",
     ["Li-Fi light fidelity wireless data transmission faster than WiFi both statements true",
      "transcriptome mRNA molecules expressed organism not genome editing not mutation",
      "ITER International Thermonuclear Experimental Reactor fusion reactor India advantage",
      "viruses infect bacteria bacteriophage fungi mycovirus plants all three true"],
     ["statement_partial_truth", "technical_vs_common_meaning", "distractor_by_topic_association"],
     [2491, 2597, 2628, 2665]),

    # --- Current Affairs and GK (17 PYQs, 5 clusters) ---
    ("ca_india_defence_events", "Current Affairs: INS Astradharini, Godavari-Krishna River Linking, Maharashtra State Butterfly & Rajasthan Inland Port", "Current Affairs and GK",
     ["INS Astradharini torpedo launch recovery vessel Indian Navy not submarine not warship",
      "Godavari Krishna river linking recently undertaken not Cauvery Tungabhadra",
      "Maharashtra first state butterfly Blue Mormon state symbol",
      "Rajasthan artificial inland port navigational channel not Andhra Chhattisgarh Karnataka"],
     ["distractor_by_topic_association", "geographic_attribution"],
     [2722, 2820, 2821, 2822]),
    ("ca_communities_persons", "Current Affairs: Kurd/Madhesi/Rohingya Country Pairs & Ramanujan Biography Film", "Current Affairs and GK",
     ["Kurd Iraq Syria Turkey not Bangladesh Madhesi Nepal Tarai plains Rohingya Myanmar Rakhine",
      "Man Who Knew Infinity Ramanujan biography film not Chandrasekhar not Bose not Raman"],
     ["geographic_attribution", "famous_association_bias"],
     [2823, 2824]),
    ("ca_international_orgs", "Current Affairs: Ease of Doing Business (World Bank), ESM, UNCCD (Not South Asia Focus), GHI Indicators & OPCW", "Current Affairs and GK",
     ["Ease of Doing Business index World Bank not OECD not WEF not WTO",
      "European Stability Mechanism ESM EU eurozone financial assistance not refugee",
      "UNCCD desertification national programmes bottom-up not special South Asia focus",
      "Global Hunger Index IFPRI undernourishment child stunting child mortality indicators",
      "OPCW independent multilateral not EU not NATO chemical weapons monitoring assistance"],
     ["distractor_by_topic_association", "statement_subtle_inversion"],
     [2755, 2756, 2757, 2758, 2759]),
    ("ca_digital_govt_initiatives", "Current Affairs: Net Metering (Solar), DigiLocker (Digital India) & BEE Star Label Products", "Current Affairs and GK",
     ["net metering solar energy households consumers grid feed-in not water gas CNG",
      "DigiLocker Digital India Programme e-documents anywhere access government",
      "Bureau of Energy Efficiency BEE Star Label ceiling fans geysers fluorescent lamps"],
     ["technical_vs_common_meaning", "statement_partial_truth"],
     [2815, 2818, 2819]),
    ("ca_emerging_tech_orgs", "Current Affairs: Project Loon (Wireless), Doctors Without Borders (NGO not UN) & Bitcoin Decentralization", "Current Affairs and GK",
     ["Project Loon Google stratospheric balloons wireless internet not solar not waste",
      "Medecins Sans Frontieres MSF Doctors Without Borders NGO not WHO not UN not EU",
      "Bitcoin cryptocurrency central bank tracking peer-to-peer anonymous transactions"],
     ["distractor_by_topic_association", "statement_subtle_inversion"],
     [2814, 2816, 2817]),
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
    has_list = (re.search(r"(^|\s)1\s*[\.\)]\s*\S", q_norm) and re.search(r"(^|\s)2\s*[\.\)]\s*\S", q_norm))
    multi_select = ("only" in opt_vals) or bool(re.search(r"\b\d\s*(?:,|and)\s*\d", opt_vals))
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
# QC notes: 16 all-true-answer cases (117, 258, 342, 1148, 1297, 1350, 1473,
# 1539, 1852, 1887, 2397, 2491, 2665, 2758, 2818, 2819) correctly tagged
# statement_partial_truth — the 2428 (2020) lesson held. Negation traps (1016)
# correctly identified. Pre-2023 year, no assertion_reason — explanatory_chain
# count = 0. No retags applied.
TRAP_TAGS: dict = {
    "83": "geographic_attribution",
    "117": "statement_partial_truth",
    "140": "famous_association_bias",
    "141": "statement_subtle_inversion",
    "185": "distractor_by_topic_association",
    "219": "statement_subtle_inversion",
    "220": "distractor_by_topic_association",
    "256": "distractor_by_topic_association",
    "257": "technical_vs_common_meaning",
    "258": "statement_partial_truth",
    "342": "statement_partial_truth",
    "406": "person_attribution",
    "423": "first_or_only",
    "424": "distractor_by_topic_association",
    "468": "distractor_by_topic_association",
    "559": "famous_association_bias",
    "610": "geographic_attribution",
    "796": "statement_subtle_inversion",
    "870": "statement_subtle_inversion",
    "871": "statement_subtle_inversion",
    "923": "statement_subtle_inversion",
    "1014": "statement_subtle_inversion",
    "1015": "statement_subtle_inversion",
    "1016": "negation_trap",
    "1017": "distractor_by_topic_association",
    "1018": "distractor_by_topic_association",
    "1019": "statement_overgeneralization",
    "1073": "statement_subtle_inversion",
    "1147": "statement_subtle_inversion",
    "1148": "statement_partial_truth",
    "1185": "technical_vs_common_meaning",
    "1217": "technical_vs_common_meaning",
    "1295": "distractor_by_topic_association",
    "1296": "statement_subtle_inversion",
    "1297": "statement_partial_truth",
    "1298": "distractor_by_topic_association",
    "1299": "statement_subtle_inversion",
    "1349": "statement_subtle_inversion",
    "1350": "statement_partial_truth",
    "1386": "geographic_attribution",
    "1387": "distractor_by_topic_association",
    "1468": "distractor_by_topic_association",
    "1469": "statement_subtle_inversion",
    "1470": "distractor_by_topic_association",
    "1471": "distractor_by_topic_association",
    "1472": "distractor_by_topic_association",
    "1473": "statement_partial_truth",
    "1538": "distractor_by_topic_association",
    "1539": "statement_partial_truth",
    "1540": "distractor_by_topic_association",
    "1541": "distractor_by_topic_association",
    "1606": "statement_subtle_inversion",
    "1607": "statement_subtle_inversion",
    "1639": "distractor_by_topic_association",
    "1640": "distractor_by_topic_association",
    "1641": "statement_subtle_inversion",
    "1829": "distractor_by_topic_association",
    "1852": "statement_partial_truth",
    "1887": "statement_partial_truth",
    "2184": "statement_subtle_inversion",
    "2185": "geographic_attribution",
    "2186": "statement_subtle_inversion",
    "2187": "geographic_attribution",
    "2266": "technical_vs_common_meaning",
    "2339": "statement_subtle_inversion",
    "2340": "distractor_by_topic_association",
    "2396": "statement_subtle_inversion",
    "2397": "statement_partial_truth",
    "2398": "overlapping_categories",
    "2399": "technical_vs_common_meaning",
    "2400": "statement_subtle_inversion",
    "2401": "statement_subtle_inversion",
    "2402": "statement_subtle_inversion",
    "2403": "distractor_by_topic_association",
    "2431": "statement_subtle_inversion",
    "2432": "technical_vs_common_meaning",
    "2491": "statement_partial_truth",
    "2523": "distractor_by_topic_association",
    "2524": "statement_subtle_inversion",
    "2525": "statement_subtle_inversion",
    "2597": "technical_vs_common_meaning",
    "2628": "distractor_by_topic_association",
    "2665": "statement_partial_truth",
    "2722": "distractor_by_topic_association",
    "2755": "distractor_by_topic_association",
    "2756": "distractor_by_topic_association",
    "2757": "statement_subtle_inversion",
    "2758": "statement_partial_truth",
    "2759": "statement_subtle_inversion",
    "2814": "distractor_by_topic_association",
    "2815": "technical_vs_common_meaning",
    "2816": "distractor_by_topic_association",
    "2817": "statement_subtle_inversion",
    "2818": "statement_partial_truth",
    "2819": "statement_partial_truth",
    "2820": "geographic_attribution",
    "2821": "geographic_attribution",
    "2822": "geographic_attribution",
    "2823": "geographic_attribution",
    "2824": "famous_association_bias",
}


# Discrimination cards — drafted by Sonnet in-conv (v2.1), merged via overlay.
DISCRIMINATION_CARDS: dict = {
}


# Merge overlays (cards drafted by Sonnet, written to scratch JSON). Any
# wave1_*.json / wave2_*.json picked up automatically.
_SCRATCH = ROOT / ".scratch" / "drill_2016"
if _SCRATCH.exists():
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
