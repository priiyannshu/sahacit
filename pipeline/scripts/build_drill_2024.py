#!/usr/bin/env python3
"""
Generate app/pwa/data/drill_clusters_2024.json
       + app/pwa/data/discrimination_cards_2024.json

Cluster map covers all 98 GS1 2024 PYQs. Clusters + trap tags drafted by
Sonnet in the leaner 2024 pipeline (pre-step agents); Opus reviews.
Discrimination cards to be drafted by 3 parallel Sonnet batches after
user eyeballs this pre-step output.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "pwa" / "data" / "pyq_index.json"
OUT_CLUSTERS = ROOT / "pwa" / "data" / "drill_clusters_2024.json"
OUT_CARDS = ROOT / "pwa" / "data" / "discrimination_cards_2024.json"

YEAR = 2024

# Cluster definitions for all 98 2024 PYQs.
# Format: (cluster_id, title, subject_focus, study_keywords[], common_traps[], pyq_ids[])
# Source: Sonnet clustering agent 2026-04-24, 37 clusters covering 98 unique PYQs.
CLUSTERS = [
    # --- Art & Culture (2 PYQs) ---
    ("artcul_unesco_heritage", "UNESCO Intangible & World Heritage: India", "Art and Culture",
     ["UNESCO Intangible Cultural Heritage list India: Garba, Chhau, Durga Puja, Kumbh Mela",
      "UNESCO World Heritage Sites India 2023: Shantiniketan, Hoysalas",
      "UNESCO World Heritage List inclusion years India"],
     ["recency_bias", "numerical_proximity"],
     [2, 3]),

    # --- Ancient History (5 PYQs) ---
    ("anc_archaeology_sites", "Ancient India: Archaeological Sites & Classification", "Ancient History",
     ["Chandraketugarh archaeological site West Bengal",
      "Inamgaon Chalcolithic site Maharashtra",
      "Salihundam Buddhist site Andhra Pradesh",
      "Mangadu megalithic Kerala",
      "Ancient Indian archaeological site classification: trading port / Chalcolithic / megalithic"],
     ["geographic_attribution", "period_attribution"],
     [128]),
    ("anc_literature_texts", "Ancient India: Literary Texts & Authorship", "Ancient History",
     ["Upanishads: composition period, content, parables",
      "Playwright Bhasa works: Madhyama-vyayoga, Svapnavasavadatta",
      "Sanghabhuti Buddhist monk — Sarvastivada Vinaya commentary",
      "Ancient Indian literary texts attribution: Natyashastra, Kavyalankara, Mahabhashya"],
     ["person_attribution", "statement_subtle_inversion"],
     [176, 177, 178]),
    ("anc_buddhism_epithets", "Ancient India: Buddhism & Buddha's Epithets", "Ancient History",
     ["Gautama Buddha epithets: Shakyamuni, Tathagata, Nayaputta",
      "Mahavira Jainism epithets: Nayaputta distinction from Buddha",
      "Buddhist terminology ancient India"],
     ["famous_association_bias", "person_attribution"],
     [205]),

    # --- Medieval History (1 PYQ) ---
    ("med_portuguese_vijayanagara", "Medieval India: Vijayanagara & Portuguese", "Medieval History",
     ["Krishnadevaraya — Portuguese relations, Bhatkal fort",
      "Vijayanagara rulers and European contact",
      "Portuguese in India medieval period: Goa, Bhatkal, Calicut"],
     ["person_attribution", "famous_association_bias"],
     [310]),

    # --- Modern History (2 PYQs) ---
    ("mod_constitutional_history", "Modern India: Constitutional Landmarks", "Modern History",
     ["Government of India Act 1935: All-India Federation, defence & foreign affairs",
      "Constituent Assembly of India: Provisional President Sachchidananda Sinha",
      "Indian constitutional history 1935-1950"],
     ["statement_subtle_inversion", "person_attribution"],
     [535, 552]),

    # --- Indian Polity (16 PYQs) ---
    ("pol_constitution_structure", "Indian Constitution: Structure, Parts & Schedules", "Indian Polity",
     ["Constitution of India Parts: Part IX-A municipalities, Part XVIII emergency, Part XX amendment",
      "Article 368 constitutional amendment: addition, variation, repeal",
      "Union List / State List / Concurrent List subjects: inter-state trade, quarantine, corporation tax",
      "Schedules of the Indian Constitution"],
     ["statement_subtle_inversion", "statement_partial_truth"],
     [707, 708, 709]),
    ("pol_fundamental_rights", "Fundamental Rights & Right to Privacy", "Indian Polity",
     ["Right to Privacy — Article 21, Supreme Court Puttaswamy judgment",
      "Fundamental Rights (Articles 14-32) Indian Constitution",
      "Right to Privacy as fundamental right — judicial interpretation"],
     ["famous_association_bias", "overlapping_categories"],
     [749]),
    ("pol_scheduled_tribes", "Scheduled Tribes: Recognition & Constitutional Provisions", "Indian Polity",
     ["Scheduled Tribe recognition India: President's role vs Governor's role",
      "Scheduled Tribes notification process — constitutional provisions",
      "ST list state-specific variation India"],
     ["statement_subtle_inversion", "geographic_attribution"],
     [826]),
    ("pol_legislature_bills", "Parliament: Bills, Dissolution & Prorogation", "Indian Polity",
     ["Money Bill — Article 109, Rajya Sabha powers (reject vs suggest)",
      "Lok Sabha dissolution: fate of pending bills (lapse or survive)",
      "Prorogation vs dissolution vs adjournment sine die — India Parliament",
      "Joint sitting of Parliament: when convened, bill-lapse rules"],
     ["statement_subtle_inversion", "statement_partial_truth"],
     [848, 851, 852]),
    ("pol_lok_sabha_procedures", "Lok Sabha: Speaker, Ethics Committee & Procedures", "Indian Polity",
     ["Speaker of Lok Sabha — removal procedure, Article 94, right to speak & vote",
      "Ethics Committee Lok Sabha: ad-hoc to permanent, complaint eligibility, sub-judice bar",
      "Lok Sabha procedural rules — Speaker's powers"],
     ["statement_subtle_inversion", "negation_trap"],
     [849, 850]),
    ("pol_judiciary_writs", "Indian Judiciary: Writs & Constitutional Remedies", "Indian Polity",
     ["Writ of Prohibition: meaning, scope, issued against lower courts",
      "Five writs — Mandamus, Certiorari, Prohibition, Habeas Corpus, Quo Warranto",
      "Supreme Court and High Court writ jurisdiction"],
     ["technical_vs_common_meaning", "overlapping_categories"],
     [915]),
    ("pol_elections_delimitation", "Elections & Delimitation Commission", "Indian Polity",
     ["Delimitation Commission India: how many constituted — 1952, 1963, 1973, 2002",
      "Delimitation Commission Act India — historical",
      "Election Commission India: structure, delimitation process"],
     ["numerical_proximity", "recency_bias"],
     [953]),
    ("pol_constitutional_bodies_regional", "Constitutional & Statutory Bodies: Regional Councils", "Indian Polity",
     ["North Eastern Council — NEC Act 1971, 2002 amendment, composition",
      "North Eastern Council India: constituent states, Home Minister membership",
      "Inter-State Councils vs Regional Councils India"],
     ["statement_subtle_inversion", "numerical_proximity"],
     [975]),
    ("pol_women_reservation_languages", "Constitutional Amendments: Women's Reservation & 8th Schedule", "Indian Polity",
     ["Nari Shakti Vandan Adhiniyam 2023: 18th Lok Sabha, 15-year sunset, SC women quota",
      "Constitution 71st Amendment 1992: Konkani, Manipuri, Nepali added to 8th Schedule",
      "Women's reservation bill India — 106th Constitutional Amendment",
      "8th Schedule Indian Constitution — 22 languages"],
     ["statement_subtle_inversion", "period_attribution"],
     [1027, 1028]),
    ("pol_political_parties_history", "Post-Independence Political Parties & Leaders", "Indian Polity",
     ["Bharatiya Jana Sangh — founder Shyama Prasad Mukherjee",
      "Swatantra Party — founder C. Rajagopalachari",
      "Congress for Democracy — Jagjivan Ram",
      "Socialist Party — Acharya Narendra Dev / Jayaprakash Narayan",
      "Indian political parties post-independence history"],
     ["person_attribution", "famous_association_bias"],
     [1054]),

    # --- Indian Economy (15 PYQs) ---
    ("eco_sectors_capital", "Economic Sectors & Physical Capital Classification", "Indian Economy",
     ["Primary / secondary / tertiary sector classification India: storage, dairy, mineral, weaving",
      "Fixed capital vs working capital examples: plough, computer, yarn, petrol",
      "Economic sectors classification — NCERT examples"],
     ["overlapping_categories", "technical_vs_common_meaning"],
     [1092, 1093]),
    ("eco_macroeconomics_debt", "Macroeconomics: Sovereign Debt & Credit Concepts", "Indian Economy",
     ["US Treasury bonds — sovereign debt, default risk",
      "Government debt: hard assets backing vs faith-based fiat",
      "Syndicated lending: risk distribution, credit lines vs lump sum",
      "Sovereign debt instruments — macroeconomics"],
     ["causal_correlation", "statement_subtle_inversion"],
     [1094, 1269]),
    ("eco_banking_rbi", "Banking: RBI Regulations & Digital Currency", "Indian Economy",
     ["Foreign banks in India — RBI rules: capital, wholly-owned subsidiaries, board composition",
      "Digital Rupee CBDC India: sovereign currency, RBI liability, balance sheet",
      "RBI regulations for foreign banking subsidiaries India",
      "Central Bank Digital Currency (CBDC) India — features"],
     ["statement_subtle_inversion", "statement_partial_truth"],
     [1268, 1270]),
    ("eco_capital_markets_instruments", "Capital Markets: Instruments & Participants", "Indian Economy",
     ["Collateral Borrowing and Lending Obligations (CBLO) — money market India",
      "NBFC access to RBI Liquidity Adjustment Facility",
      "Foreign Institutional Investors — Government Securities India",
      "Corporate bonds / G-Secs: who can trade (insurance, pension, retail)",
      "Financial instruments: ETF, currency swap, motor vehicles classification"],
     ["overlapping_categories", "technical_vs_common_meaning"],
     [1333, 1334, 1335, 1336]),
    ("eco_csr_industries", "Corporate Social Responsibility & Industry Regulations", "Indian Economy",
     ["CSR rules India Companies Act 2013: employee-benefit exclusion, 2% net-profit mandate",
      "Corporate Social Responsibility mandatory spending India",
      "CSR activities: definition & scope India"],
     ["statement_subtle_inversion", "negation_trap"],
     [1373]),
    ("eco_demography_welfare", "Demography, Labour & Social Welfare Schemes", "Indian Economy",
     ["Total Fertility Rate: definition — live births per woman child-bearing age",
      "Pradhan Mantri Suraksha Matritva Abhiyan: antenatal care, trimester coverage, private sector",
      "Pradhan Mantri Shram Yogi Maan-dhan (PM-SYM): entry age, pension amount, family pension",
      "Demographic indicators India: TFR, birth rate, crude death rate"],
     ["technical_vs_common_meaning", "statement_subtle_inversion"],
     [1483, 1526, 1571]),
    ("eco_agriculture_land", "Agriculture: Land Records & Digitisation", "Indian Economy",
     ["Digital India Land Records Modernization Programme (DILRMP): funding pattern, cadastral maps",
      "Land records digitisation India: Records of Rights, transliteration",
      "DILRMP Central-State funding — 100% Central"],
     ["statement_subtle_inversion", "statement_partial_truth"],
     [1590]),

    # --- Geography (17 PYQs) ---
    ("geo_physical_processes", "Physical Geography: Weathering, Volcanoes & Earth Science", "Geography",
     ["Chemical weathering of rocks: rainfall, carbonic acid, atmospheric oxygen",
      "Volcanic eruption products: pyroclastic debris, ash, nitrogen & sulphur compounds",
      "Physical and chemical weathering agents"],
     ["causal_correlation", "statement_subtle_inversion"],
     [1677, 1678]),
    ("geo_earth_sun_latitude", "Physical Geography: Earth-Sun Relations & Latitude", "Geography",
     ["June 21 summer solstice: sunlight hours at Tropic of Cancer, Arctic Circle, equator",
      "Day length — latitude relationship, solstice",
      "Midnight sun — Arctic Circle, June 21"],
     ["statement_subtle_inversion", "overlapping_categories"],
     [1679]),
    ("geo_climatology_atmosphere", "Climatology: Atmosphere, Heat & Wind", "Geography",
     ["Atmosphere heating: solar vs terrestrial radiation, greenhouse gases",
      "Troposphere thickness: equator vs poles, convectional currents",
      "Water vapour in atmosphere: altitude decrease, polar vs equatorial distribution",
      "Coriolis force: wind-velocity relationship, pole vs equator strength",
      "Marine west-coast climate: precipitation, temperature range"],
     ["statement_subtle_inversion", "explanatory_chain"],
     [1719, 1720, 1721, 1722, 1723]),
    ("geo_oceanography", "Oceanography: Ocean Currents & Isotherms", "Geography",
     ["Isothermal maps January: ocean vs continent isotherm deviation",
      "Gulf Stream / North Atlantic Drift: warming effect on North Atlantic",
      "Ocean currents January Northern Hemisphere — isotherms"],
     ["statement_subtle_inversion", "geographic_attribution"],
     [1787]),
    ("geo_indian_rivers", "Indian Rivers: Tributaries, Sequence & Waterfalls", "Geography",
     ["Ganga tributaries downstream Prayagraj, west-to-east: Gomati, Ghaghara, Gandak, Kosi",
      "Himalayan rivers joining Ganga — sequence",
      "Indian waterfalls: Dhuandhar (Narmada), Hundru (Subarnarekha), Gersoppa (Sharavati)"],
     ["geographic_attribution", "famous_association_bias"],
     [1873, 1874]),
    ("geo_transport_airports", "Indian Infrastructure: Greenfield Airports", "Geography",
     ["Greenfield airports India: Donyi Polo (Arunachal Pradesh), Kushinagar International",
      "New airports India — recent construction 2021-2024",
      "Donyi Polo Airport Itanagar — first airport of Arunachal Pradesh"],
     ["first_or_only", "geographic_attribution"],
     [1993]),
    ("geo_world_resources_countries", "World Geography: Country-Resource Pairs", "Geography",
     ["Cocoa producing countries: Côte d'Ivoire, Ghana — world's largest producers",
      "Mountain ranges world: Vosges (fold/block), Alps, Appalachians, Andes",
      "Country–natural resource matching — world geography"],
     ["geographic_attribution", "famous_association_bias"],
     [2036, 2037]),
    ("geo_world_map_borders", "World Geography: Borders, Seas & Boundaries", "Geography",
     ["Countries bordering North Sea: Finland / Germany / Norway / Russia",
      "Longest international border in the world: Canada–USA",
      "Red Sea: precipitation, river inflow, salinity",
      "European sea borders — world geography"],
     ["geographic_attribution", "famous_association_bias"],
     [2074, 2075, 2076]),

    # --- Environment (19 PYQs) ---
    ("env_ecology_organisms", "Ecology: Species Identification & Classification", "Environment",
     ["Parasitoid organisms: carabid beetles, centipedes, flies, termites, wasps",
      "Leguminosae (pea family) plants: groundnut, horse-gram, soybean",
      "Cicada / froghopper / pond skater — insect classification",
      "Poisonous species: butterflies, fish, frogs — toxic animals"],
     ["technical_vs_common_meaning", "overlapping_categories"],
     [2120, 2121, 2122, 2126]),
    ("env_wildlife_behaviour", "Ecology: Wildlife Behaviour & Animal Geography", "Environment",
     ["Big cats: lion breeding season, cheetah roar, leopard scent marking",
      "Animal native-habitat country pairs: Indri (Madagascar), Bonobo (Congo), Elk",
      "Fig-wasp pollination — co-evolution, mutualism",
      "Wildlife behaviour / ecology facts — UPSC"],
     ["famous_association_bias", "geographic_attribution"],
     [2123, 2124, 2125]),
    ("env_biodiversity_conservation", "Biodiversity: Conservation Status & Native Species", "Environment",
     ["Indian Flying Fox bat — Wildlife Protection Act 1972: vermin category",
      "Native vs introduced trees India: cashew, papaya, red sanders origin",
      "Wildlife Protection Act schedules and vermin category India"],
     ["statement_subtle_inversion", "technical_vs_common_meaning"],
     [2161, 2162]),
    ("env_pollution_chemicals", "Pollution: Chemicals, Plastics & Remediation", "Environment",
     ["Chewing-gum plastic pollution: polyisobutylene gum base, synthetic",
      "PFAS (per- and polyfluoroalkyl substances): persistence, bioaccumulation, drinking water",
      "Sulphur dioxide largest source (EPA): power plants, fossil fuels",
      "Membrane Bioreactors — wastewater treatment technology"],
     ["causal_correlation", "statement_subtle_inversion"],
     [2242, 2243, 2244, 2245]),
    ("env_climate_peatlands", "Climate Change: Carbon Sinks & Peatlands", "Environment",
     ["Congo Basin tropical peatland: world's largest carbon stock",
      "Tropical peatlands — carbon emissions, global climate",
      "Peatland destruction — climate impact, carbon release"],
     ["geographic_attribution", "famous_association_bias"],
     [2290]),
    ("env_global_climate_policy", "Global Environmental Policy: Net-Zero & EU Initiatives", "Environment",
     ["EU Net-Zero Industry Act — European Parliament approval",
      "European Union carbon neutrality target: 2050 vs 2040",
      "EU clean-technology net-zero policy goals"],
     ["statement_subtle_inversion", "numerical_proximity"],
     [2383]),
    ("env_clean_energy_tech", "Renewable & Clean Energy Technologies", "Environment",
     ["Distributed Energy Resources (DER): battery storage, biomass, fuel cells, rooftop solar",
      "Sustainable Aviation Fuel (SAF) feedstocks: agricultural residues, corn, wastewater, wood",
      "Hydrogen Fuel Cell Electric Vehicles (FCEV) exhaust: water vapour",
      "Pumped-storage hydropower — energy storage application"],
     ["technical_vs_common_meaning", "overlapping_categories"],
     [2446, 2447, 2448, 2449]),

    # --- Science & Technology (7 PYQs) ---
    ("sci_electronics_digital", "Science & Tech: Radar, IT & Digital Concepts", "Science and Technology",
     ["Radar applications: narcotics detection, precipitation monitoring, animal migration",
      "Metaverse: interoperable 3D virtual worlds, property rights",
      "Digital technology terminology: big data, cryptography, metaverse"],
     ["technical_vs_common_meaning", "overlapping_categories"],
     [2467, 2468]),
    ("sci_space_astrophysics", "Science & Tech: Astrophysics & Space", "Science and Technology",
     ["Giant stars vs dwarf stars: lifespan, nuclear reaction rate",
      "Stellar evolution: star size and lifespan relationship",
      "Radioisotope Thermoelectric Generators (RTG): fission vs decay, Pu-238 spacecraft"],
     ["statement_subtle_inversion", "causal_correlation"],
     [2507, 2622]),
    ("sci_biotech_gm", "Science & Tech: Biotechnology, Hydrogels & GM Food", "Science and Technology",
     ["Hydrogels uses: drug delivery, air conditioning, industrial lubricants",
      "Genetically Modified food imports India: legal framework, competent authority approval",
      "India GM food import restrictions: apples from USA"],
     ["technical_vs_common_meaning", "statement_subtle_inversion"],
     [2578, 2579]),
    ("sci_biology_chemistry", "Science & Tech: Biology & Chemistry", "Science and Technology",
     ["Nitric oxide vs nitrous oxide: vasodilation, blood flow, human body",
      "Nitrogen compounds in human physiology: NO / NO2 / N2O distinction"],
     ["technical_vs_common_meaning", "overlapping_categories"],
     [2655]),

    # --- Current Affairs (14 PYQs) ---
    ("ca_defence_military", "Current Affairs: Defence Forces & Military Exercises", "Current Affairs and GK",
     ["Fifth generation fighter aircraft: Rafale, MiG-29, Tejas — classification",
      "Indian Defence Forces equivalent ranks: Army / Air Force / Navy",
      "Chief of Defence Staff (CDS): Department of Military Affairs, tri-service advisor",
      "Operation Sadbhavana — Indian Army: remote areas upliftment",
      "Exercise Mitra Shakti 2023: India–Sri Lanka joint military exercise"],
     ["statement_subtle_inversion", "geographic_attribution"],
     [2702, 2703, 2704, 2705, 2706]),
    ("ca_international_orgs", "Current Affairs: International Organisations & Platforms", "Current Affairs and GK",
     ["World Toilet Organization: UN agency or NGO, World Toilet Day",
      "100 Million Farmers platform: net-zero food and water systems",
      "International Grains Council: India membership, rice/wheat export-import requirement"],
     ["famous_association_bias", "overlapping_categories"],
     [2736, 2737, 2738]),
    ("ca_global_events_geopolitics", "Current Affairs: Global Events & Geopolitics", "Current Affairs and GK",
     ["Ageing population countries: Italy, Japan, South Korea — low birth rates",
      "S. Jaishankar books: The India Way, Why Bharat Matters",
      "Country events 2023: Argentina economic crisis, Sudan army war, Turkey NATO",
      "Sumed pipeline: Red Sea–Mediterranean oil route",
      "Sahel region military coups — instability countries",
      "Venezuela economic crisis — oil reserves, emigration"],
     ["recency_bias", "geographic_attribution"],
     [2779, 2780, 2781, 2782, 2783, 2784]),
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


def load_2024_pyqs():
    idx = json.load(open(INDEX))
    return [p for p in idx["pyqs"] if p.get("year") == YEAR]


# ---- Trap-pattern tagging (Sonnet-drafted 2026-04-24, Opus-reviewed) ----
TRAP_TAGS = {
    # Art & Culture
    "2": "first_or_only",
    "3": "first_or_only",
    # Ancient History
    "128": "geographic_attribution",
    "176": "statement_subtle_inversion",
    "177": "person_attribution",
    "178": "person_attribution",
    "205": "person_attribution",
    # Medieval History
    "310": "person_attribution",
    # Modern History
    "535": "statement_subtle_inversion",
    "552": "person_attribution",
    # Indian Polity
    "707": "statement_overgeneralization",
    "708": "statement_subtle_inversion",
    "709": "technical_vs_common_meaning",
    "749": "famous_association_bias",
    "826": "statement_subtle_inversion",
    "848": "statement_subtle_inversion",
    "849": "statement_subtle_inversion",
    "850": "statement_subtle_inversion",
    "851": "statement_subtle_inversion",
    "852": "statement_subtle_inversion",
    "915": "technical_vs_common_meaning",
    "953": "numerical_proximity",
    "975": "statement_subtle_inversion",
    "1027": "statement_subtle_inversion",
    "1028": "period_attribution",
    "1054": "person_attribution",
    # Indian Economy
    "1092": "overlapping_categories",
    "1093": "technical_vs_common_meaning",
    "1094": "explanatory_chain",
    "1268": "statement_subtle_inversion",
    "1269": "explanatory_chain",       # ⚠ null answer in master
    "1270": "statement_subtle_inversion",
    "1333": "overlapping_categories",
    "1334": "statement_subtle_inversion",
    "1335": "statement_overgeneralization",
    "1336": "overlapping_categories",
    "1373": "statement_subtle_inversion",
    "1483": "technical_vs_common_meaning",
    "1526": "statement_subtle_inversion",
    "1571": "statement_subtle_inversion",
    "1590": "statement_subtle_inversion",
    # Geography
    "1677": "explanatory_chain",
    "1678": "statement_overgeneralization",
    "1679": "statement_subtle_inversion",
    "1719": "explanatory_chain",
    "1720": "explanatory_chain",
    "1721": "statement_subtle_inversion",
    "1722": "distractor_by_topic_association",
    "1723": "statement_subtle_inversion",
    "1787": "statement_subtle_inversion",
    "1873": "geographic_attribution",
    "1874": "geographic_attribution",
    "1993": "first_or_only",
    "2036": "geographic_attribution",
    "2037": "geographic_attribution",
    "2074": "geographic_attribution",
    "2075": "famous_association_bias",
    "2076": "statement_subtle_inversion",
    # Environment
    "2120": "overlapping_categories",
    "2121": "overlapping_categories",
    "2122": "distractor_by_topic_association",
    "2123": "geographic_attribution",
    "2124": "statement_subtle_inversion",
    "2125": "famous_association_bias",
    "2126": "statement_overgeneralization",
    "2161": "explanatory_chain",       # ⚠ null answer in master
    "2162": "geographic_attribution",
    "2242": "explanatory_chain",
    "2243": "statement_subtle_inversion",
    "2244": "famous_association_bias",
    "2245": "distractor_by_topic_association",
    "2290": "geographic_attribution",
    "2383": "explanatory_chain",
    "2446": "overlapping_categories",
    "2447": "statement_overgeneralization",
    "2448": "technical_vs_common_meaning",
    "2449": "distractor_by_topic_association",
    # Science & Tech
    "2467": "statement_overgeneralization",
    "2468": "technical_vs_common_meaning",
    "2507": "explanatory_chain",
    "2578": "overlapping_categories",
    "2579": "explanatory_chain",
    "2622": "technical_vs_common_meaning",
    "2655": "technical_vs_common_meaning",
    # Current Affairs
    "2702": "technical_vs_common_meaning",
    "2703": "statement_subtle_inversion",
    "2704": "statement_subtle_inversion",
    "2705": "famous_association_bias",
    "2706": "geographic_attribution",
    "2736": "statement_subtle_inversion",
    "2737": "distractor_by_topic_association",
    "2738": "statement_subtle_inversion",
    "2779": "geographic_attribution",
    "2780": "person_attribution",
    "2781": "statement_subtle_inversion",
    "2782": "explanatory_chain",
    "2783": "explanatory_chain",
    "2784": "explanatory_chain",
}


# Discrimination cards — drafted by Sonnet agents, merged by Opus.
DISCRIMINATION_CARDS: dict = {
    # --- Calibration batch (2026-04-25) ---
    "849": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "Statement 2 inverts the complaint rule — it says 'only a Member' can complain, but any person can complain (non-members route it through an MP). Students mistake the procedural channel requirement for a substantive eligibility bar.",
        "statements": [
            {"id": 1, "text": "Initially it was an ad-hoc Committee.", "verdict": "true",
             "reason": "Speaker G.M.C. Balayogi constituted it as an ad-hoc committee in 2000. It became a permanent Standing Committee only in August 2015 under Rule 316A."},
            {"id": 2, "text": "Only a Member of the Lok Sabha can make a complaint relating to unethical conduct of a member of the Lok Sabha.", "verdict": "false",
             "reason": "Any person can file a complaint. Non-members must route it through a Lok Sabha MP and submit an affidavit. The MP is a conduit, not the sole eligible complainant."},
            {"id": 3, "text": "This Committee cannot take up any matter which is sub-judice.", "verdict": "true",
             "reason": "The Committee explicitly bars sub-judice matters — cases pending before courts are outside its jurisdiction to preserve judicial independence."}
        ],
        "answer_justification": {
            "fact": "Statements 1 and 3 true; 2 false → option (c) 1 and 3 only.",
            "elimination_path": "Kill Statement 2 (any person can complain, not members only) → eliminate (a), (b), (d). Statements 1 (ad-hoc 2000→permanent 2015) and 3 (sub-judice bar) are straightforward."
        },
        "concept_hooks": ["Ethics Committee Lok Sabha Rule 316A", "Lok Sabha Ethics Committee complaint procedure", "Parliamentary sub-judice rule India"]
    },
    "850": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "Statements 2 and 3 invert what Article 96(2) actually grants. The Speaker retains the right to speak AND to vote in the first instance during the removal debate — only tie-breaking is barred. UPSC exploits the intuition that someone facing removal should have no rights.",
        "statements": [
            {"id": 1, "text": "He/She shall not preside.", "verdict": "true",
             "reason": "Article 96(1): while a removal resolution is under consideration, the Speaker shall not preside even if present. The Deputy Speaker or another member chairs."},
            {"id": 2, "text": "He/She shall not have the right to speak.", "verdict": "false",
             "reason": "Article 96(2) explicitly grants the Speaker the right to speak and otherwise take part in proceedings during consideration of the removal resolution."},
            {"id": 3, "text": "He/She shall not be entitled to vote on the resolution in the first instance.", "verdict": "false",
             "reason": "Article 96(2) entitles the Speaker to vote in the first instance. The only restriction: no casting vote in case of equality of votes (tie-breaking is barred)."}
        ],
        "answer_justification": {
            "fact": "Only Statement 1 is true; Statements 2 and 3 both contradict Article 96(2) → option (a) 1 only.",
            "elimination_path": "Article 96(2) is the pivot: it affirmatively grants right to speak AND vote in first instance. Statements 2 and 3 negate both → both false. Only S1 (no presiding, per Art. 96(1)) survives → (a)."
        },
        "concept_hooks": ["Article 96 Constitution India Speaker removal", "Article 94 Speaker removal procedure 14-day notice", "Speaker Lok Sabha casting vote Article 100"]
    },
    # --- Wave 1 / Batch A: Polity (14 cards, 2026-04-25) ---
    "707": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_overgeneralization",
        "trap_explanation": "The trap is doubting 'repeal' — aspirants assume amendment power covers only addition/modification. Article 368 explicitly includes repeal. All three modes are textually present in the article.",
        "statements": [
            {"id": 1, "text": "Addition", "verdict": "true", "reason": "Article 368(1) expressly empowers Parliament to amend the Constitution by way of addition."},
            {"id": 2, "text": "Variation", "verdict": "true", "reason": "Article 368(1) expressly includes variation — i.e., modifying existing provisions."},
            {"id": 3, "text": "Repeal", "verdict": "true", "reason": "Article 368(1) expressly includes repeal. All three modes are listed verbatim in the article."}
        ],
        "answer_justification": {
            "fact": "All three — addition, variation, repeal — are explicitly enumerated in Article 368(1). Answer: D.",
            "elimination_path": "If you recalled any one mode as valid, 'only 1 and 2' or 'only 2 and 3' options fall immediately. Article 368 text is exhaustive — all three."
        },
        "concept_hooks": ["Article 368 amendment procedure", "Kesavananda Bharati basic structure doctrine"]
    },
    "708": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "The trap is misremembering which Part covers which subject — especially conflating Part IX-A (municipalities) with Part IX (panchayats), or misplacing emergency provisions. All three statements are correct.",
        "statements": [
            {"id": 1, "text": "Powers of the Municipalities are given in Part IX A of the Constitution.", "verdict": "true", "reason": "Part IX-A (Articles 243P–243ZG), inserted by 74th Amendment 1992, covers municipalities. Part IX covers panchayats — common confusion."},
            {"id": 2, "text": "Emergency provisions are given in Part XVIII of the Constitution.", "verdict": "true", "reason": "Part XVIII (Articles 352–360) covers National Emergency, President's Rule, and Financial Emergency."},
            {"id": 3, "text": "Provisions related to the amendment of the Constitution are given in Part XX of the Constitution.", "verdict": "true", "reason": "Part XX contains only Article 368 — the amendment procedure. Single-article Part."}
        ],
        "answer_justification": {
            "fact": "All three Parts are correctly stated. Answer: D (1, 2 and 3).",
            "elimination_path": "Anchor on Part IX-A vs IX distinction to confirm statement 1. Part XVIII (emergency) and Part XX (amendment) are standard recall. All three hold."
        },
        "concept_hooks": ["Parts of Indian Constitution list", "74th Amendment municipalities Part IX-A", "Part XVIII emergency provisions"]
    },
    "709": {
        "question_type": "standard",
        "trap_pattern": "technical_vs_common_meaning",
        "trap_explanation": "'Inter-State' prefix makes options sound like they belong to states, not the Union. But inter-state subjects — trade, quarantine, migration — are Union List entries because they cross state lines and require central coordination.",
        "answer_justification": {
            "fact": "Inter-State quarantine is Union List Entry 81. The centre controls cross-border disease prevention.",
            "hook": "Anything 'inter-state' in List I: trade (Entry 42), migration (Entry 81 adjacency), quarantine (Entry 81).",
            "elimination_path": "A: Inter-State trade is Concurrent/Union, not State. B: Migration is Union List. D: Corporation tax is Union List Entry 85. Only C survives."
        },
        "distractor_analysis": [
            {"option": "a", "verdict": "wrong", "reason": "Inter-State trade and commerce is Union List Entry 42, not a State subject.", "confused_with": "Entry 26 State List (intra-state trade)"},
            {"option": "b", "verdict": "wrong", "reason": "Inter-State migration is Union List Entry 81, not State.", "confused_with": None},
            {"option": "d", "verdict": "wrong", "reason": "Corporation tax is Union List Entry 85 — exclusively central revenue.", "confused_with": None}
        ],
        "concept_hooks": ["Union List State List Concurrent List entries", "Inter-State quarantine Entry 81", "Corporation tax Union List"]
    },
    "749": {
        "question_type": "standard",
        "trap_pattern": "famous_association_bias",
        "trap_explanation": "Article 19 (freedom of speech, movement) feels like the natural home for privacy. Article 21's broader 'personal liberty' is the correct anchor per Puttaswamy 2017, but aspirants gravitate to 19.",
        "answer_justification": {
            "fact": "Puttaswamy v. Union of India (2017) — 9-judge bench unanimously placed Right to Privacy under Article 21 (right to life and personal liberty).",
            "hook": "Article 21 expanded by Maneka Gandhi (1978) to cover all personal liberty — Puttaswamy extended this to privacy.",
            "elimination_path": "Articles 15 and 16 are equality/non-discrimination — eliminate immediately. Between 19 and 21: Puttaswamy bench specifically anchored privacy in Article 21, not 19."
        },
        "distractor_analysis": [
            {"option": "a", "verdict": "wrong", "reason": "Article 15 bars discrimination — unrelated to privacy.", "confused_with": None},
            {"option": "b", "verdict": "wrong", "reason": "Article 16 covers equality in public employment — not privacy.", "confused_with": None},
            {"option": "c", "verdict": "wrong", "reason": "Article 19 freedoms contributed to the reasoning but 21 is the primary anchor in Puttaswamy.", "confused_with": "Article 19(1)(a) freedom of speech — partial privacy overlap"}
        ],
        "concept_hooks": ["Puttaswamy judgment 2017 Right to Privacy", "Article 21 personal liberty expansion", "Maneka Gandhi case 1978"]
    },
    "826": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "Statement 1 inverts the constitutional actor: it's the PRESIDENT (Article 342), not the Governor, who notifies STs. The Governor is only consulted. Statement 2 is true — ST lists are state-specific.",
        "statements": [
            {"id": 1, "text": "It is the Governor of the State who recognizes and declares any community of that State as a Scheduled Tribe.", "verdict": "false", "reason": "Article 342: President specifies STs by public notification, after consulting the Governor of that state. Parliament can modify by law. Governor only consulted, not the declaring authority."},
            {"id": 2, "text": "A community declared as a Scheduled Tribe in a State need not be so in another State.", "verdict": "true", "reason": "ST notifications are state-specific — a tribe in Manipur may not appear on Assam's list. Lists vary by state via separate Presidential orders."}
        ],
        "answer_justification": {
            "fact": "Statement 1 false (President, not Governor, declares). Statement 2 true. Answer: B (2 only).",
            "elimination_path": "Article 342 recall kills statement 1 — Governor is only consulted. Once 1 is false, eliminate A and C. Statement 2 is straightforwardly true → B."
        },
        "concept_hooks": ["Article 342 Scheduled Tribes notification", "President Governor role ST recognition", "State-specific ST lists India"]
    },
    "848": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "Statement 4 is the trap: Rajya Sabha suggestions are NOT binding on Lok Sabha. Article 109(2) says Lok Sabha 'may' accept or not. Aspirants conflate 'suggestions' with 'amendments that must be accepted'.",
        "statements": [
            {"id": 1, "text": "Article 109 mentions special procedure in respect of Money Bills.", "verdict": "true", "reason": "Article 109 is titled and dedicated to the special procedure for Money Bills — textually correct."},
            {"id": 2, "text": "A Money Bill shall not be introduced in the Council of States.", "verdict": "true", "reason": "Article 109(1): Money Bills are introduced only in Lok Sabha, never in Rajya Sabha."},
            {"id": 3, "text": "The Rajya Sabha can either approve the Bill or suggest changes but cannot reject it.", "verdict": "true", "reason": "Article 109(2): Rajya Sabha can pass with/without amendments or make suggestions; it cannot reject. If not returned in 14 days, deemed passed."},
            {"id": 4, "text": "Amendments to a Money Bill suggested by the Rajya Sabha have to be accepted by the Lok Sabha.", "verdict": "false", "reason": "Article 109(2): Lok Sabha 'may' accept or reject Rajya Sabha suggestions. Acceptance is discretionary, not mandatory."}
        ],
        "answer_justification": {
            "fact": "Statements 1, 2, 3 true; 4 false. Answer: C (1, 2 and 3).",
            "elimination_path": "Statement 4 kills options A and D. Between B and C: statements 1 and 3 are both correct (Article 109 scope + Rajya Sabha can't reject). Answer C."
        },
        "concept_hooks": ["Article 109 Money Bill procedure", "Rajya Sabha Money Bill powers", "Money Bill vs Financial Bill distinction"]
    },
    "851": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "Statement 3 inverts the rule: a bill for which President has NOTIFIED joint sitting intent does NOT lapse on dissolution (Article 108 explicitly protects it). The opposite is stated — aspirants may assume all pending bills lapse.",
        "statements": [
            {"id": 1, "text": "A bill pending in the Lok Sabha lapses on its dissolution.", "verdict": "true", "reason": "Bills pending only in Lok Sabha (not yet passed by either house) lapse on dissolution — standard rule."},
            {"id": 2, "text": "A bill passed by the Lok Sabha and pending in the Rajya Sabha lapses on the dissolution of the Lok Sabha.", "verdict": "true", "reason": "If Rajya Sabha hasn't yet passed it (and no joint sitting notification), the bill lapses with Lok Sabha dissolution."},
            {"id": 3, "text": "A bill in regard to which the President of India notified his/her intention to summon the Houses to a joint sitting lapses on the dissolution of the Lok Sabha.", "verdict": "false", "reason": "Article 108 proviso: once President notifies joint sitting intent, the bill survives dissolution. Joint sitting can proceed even after Lok Sabha is dissolved."}
        ],
        "answer_justification": {
            "fact": "Statements 1 and 2 true; 3 false — Article 108 protects notified bills from lapsing. Answer: B (1 and 2).",
            "elimination_path": "Statement 3 is the pivot — Article 108 explicitly states joint-sitting-notified bill survives dissolution. Eliminate C and D. Statements 1 and 2 are standard lapse rules → B."
        },
        "concept_hooks": ["Article 108 joint sitting Parliament", "Bill lapse Lok Sabha dissolution rules", "Joint sitting Money Bill exception"]
    },
    "852": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "Statement 1 inverts the rule: prorogation also requires Council of Ministers advice (President acts on aid and advice per Article 74). Aspirants associate 'prorogation' as a purely Presidential/administrative act. Statements 2 and 3 are correct.",
        "statements": [
            {"id": 1, "text": "Prorogation of a House by the President of India does not require the advice of the Council of Ministers.", "verdict": "false", "reason": "Article 74 binds the President to act on Council of Ministers' advice for ALL executive functions including prorogation. No exception exists for prorogation."},
            {"id": 2, "text": "Prorogation of a House is generally done after the House is adjourned sine die but there is no bar to the President of India prorogating the House which is in session.", "verdict": "true", "reason": "Convention: prorogation follows adjournment sine die. But constitutionally, the President can prorogue a House even while it is sitting — no textual bar."},
            {"id": 3, "text": "Dissolution of the Lok Sabha is done by the President of India who, save in exceptional circumstances, does so on the advice of the Council of Ministers.", "verdict": "true", "reason": "Article 85(2): President dissolves Lok Sabha. Convention (Shamsher Singh 1974) binds this to Cabinet advice; President retains discretion only if PM loses majority."}
        ],
        "answer_justification": {
            "fact": "Statement 1 false; statements 2 and 3 true. Answer: C (2 and 3).",
            "elimination_path": "Article 74 kills statement 1 — Cabinet advice applies to prorogation too. Eliminate A and B. Statements 2 and 3 both hold → C."
        },
        "concept_hooks": ["Article 74 aid and advice Council of Ministers", "Prorogation adjournment dissolution distinction", "Shamsher Singh case 1974 President discretion"]
    },
    "915": {
        "question_type": "standard",
        "trap_pattern": "technical_vs_common_meaning",
        "trap_explanation": "Common meaning of 'prohibition' suggests banning a person or policy. Legal writ of Prohibition targets courts/tribunals — it tells a lower court to STOP proceedings, not government officers or legislatures.",
        "answer_justification": {
            "fact": "Writ of Prohibition: issued by superior courts (SC/HC) to lower courts/tribunals to halt proceedings exceeding jurisdiction — before a final order is passed.",
            "hook": "Prohibition = preventive; Certiorari = curative. Both target lower courts, not executive. Prohibition stops before; Certiorari quashes after.",
            "elimination_path": "A and D target government/officers — writs of Mandamus, not Prohibition. B involves legislatures — no writ applies this way. Only C (lower court, stop proceedings) fits."
        },
        "distractor_analysis": [
            {"option": "a", "verdict": "wrong", "reason": "Mandamus directs government officers to perform duty; Prohibition targets courts.", "confused_with": "Writ of Mandamus"},
            {"option": "b", "verdict": "wrong", "reason": "No writ orders Parliament/Legislature to pass or refrain from legislation.", "confused_with": None},
            {"option": "d", "verdict": "wrong", "reason": "Government policy is challenged via Mandamus or Certiorari, not Prohibition.", "confused_with": "Writ of Certiorari"}
        ],
        "concept_hooks": ["Writ of Prohibition vs Certiorari distinction", "Five constitutional writs India", "Article 32 Article 226 writ jurisdiction"]
    },
    "953": {
        "question_type": "standard",
        "trap_pattern": "numerical_proximity",
        "trap_explanation": "Aspirants recall 2 or 3 Delimitation Commissions by memory. The question asks up to December 2023 — four formal Acts (1952, 1963, 1973, 2002) each created a Commission. No fifth was constituted by December 2023.",
        "answer_justification": {
            "fact": "Four Delimitation Commissions: 1952 (under Delimitation Commission Act 1952), 1963, 1973, 2002. No new commission by December 2023.",
            "hook": "Each major Delimitation Act created exactly one Commission. Four Acts = four Commissions.",
            "elimination_path": "Eliminate A (1) and B (2) — multiple commissions are documented. Eliminate C (3) — the 2002 commission is well-established as the fourth. Answer D."
        },
        "distractor_analysis": [
            {"option": "a", "verdict": "wrong", "reason": "First commission was in 1952; multiple subsequent ones are a matter of record.", "confused_with": None},
            {"option": "b", "verdict": "wrong", "reason": "Two is an undercount — 1952, 1963, 1973, 2002 commissions all constituted.", "confused_with": None},
            {"option": "c", "verdict": "wrong", "reason": "Three undercounts — omits either 1952 or 2002 commission.", "confused_with": "numerical_proximity to correct answer"}
        ],
        "concept_hooks": ["Delimitation Commission India history 1952 1963 1973 2002", "Delimitation Act India", "Delimitation freeze 84th Amendment"]
    },
    "975": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "Home Minister is ex-officio Chairman of NEC (post-2018 restructure), but the question asks about MEMBERS per Section 3 of the 2002 amended Act. Chairman ≠ member. Aspirants mark 4 (Home Minister) as a member because he chairs the body.",
        "statements": [
            {"id": 1, "text": "Governor of the Constituent State", "verdict": "true", "reason": "Section 3 of NEC Act (as amended 2002): Governors of the eight constituent NE states are members."},
            {"id": 2, "text": "Chief Minister of the Constituent State", "verdict": "true", "reason": "Section 3: Chief Ministers of the eight constituent states are members of the NEC."},
            {"id": 3, "text": "Three Members to be nominated by the President of India", "verdict": "true", "reason": "Section 3: Up to three members nominated by the President — added by 2002 amendment."},
            {"id": 4, "text": "The Home Minister of India", "verdict": "false", "reason": "Home Minister is ex-officio Chairman (post-2018), not a statutory member under Section 3. Chairman and member are distinct roles under the Act."}
        ],
        "answer_justification": {
            "fact": "Members per Section 3: Governors, Chief Ministers, 3 Presidential nominees. Home Minister = Chairman, not member. Answer: A (1, 2 and 3 only).",
            "elimination_path": "Home Minister is ex-officio Chairman, not Section 3 member — kills options B, C, D. Items 1, 2, 3 are all Section 3 members → A."
        },
        "concept_hooks": ["North Eastern Council composition 2002 amendment", "NEC Act Section 3 members", "NEC Chairman Home Minister distinction"]
    },
    "1027": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "Statement 1 inverts the timeline: implementation requires census + delimitation, targeting the 19th Lok Sabha (post-2029), not the 18th (already elected in 2024). The Act was passed during 18th LS — confusion between enactment and implementation.",
        "statements": [
            {"id": 1, "text": "Provisions will come into effect from the 18th Lok Sabha.", "verdict": "false", "reason": "Article 334A (inserted by 106th Amendment): reservation activates only after first post-commencement census and subsequent delimitation — applicable from 19th Lok Sabha at earliest."},
            {"id": 2, "text": "This will be in force for 15 years after becoming an Act.", "verdict": "true", "reason": "Article 334A: reservation for women operative for 15 years from commencement, extendable by Parliament."},
            {"id": 3, "text": "There are provisions for the reservation of seats for Scheduled Castes Women within the quota reserved for the Scheduled Castes.", "verdict": "true", "reason": "Act provides one-third of SC/ST reserved seats shall be reserved for SC/ST women respectively — sub-quota within existing SC/ST quota."}
        ],
        "answer_justification": {
            "fact": "Statement 1 false (19th LS, not 18th); 2 and 3 true. Answer: C (2 and 3 only).",
            "elimination_path": "Statement 1 fails on Article 334A — census+delimitation gate means 18th LS cannot implement. Eliminate A and B. Statements 2 and 3 are textually in the Act → C."
        },
        "concept_hooks": ["106th Constitutional Amendment Nari Shakti Vandan Adhiniyam", "Article 334A women's reservation trigger", "Women's reservation 15-year duration SC quota"]
    },
    "1028": {
        "question_type": "statement_eval",
        "trap_pattern": "period_attribution",
        "trap_explanation": "Maithili is the distractor — it was added by the 92nd Amendment (2003), not the 71st (1992). UPSC tests whether aspirants conflate two different language-addition amendments.",
        "statements": [
            {"id": 1, "text": "Konkani", "verdict": "true", "reason": "71st Amendment 1992 added Konkani to the Eighth Schedule, raising the total to 18 languages."},
            {"id": 2, "text": "Manipuri", "verdict": "true", "reason": "71st Amendment 1992 added Manipuri (also called Meitei) to the Eighth Schedule."},
            {"id": 3, "text": "Nepali", "verdict": "true", "reason": "71st Amendment 1992 added Nepali to the Eighth Schedule — all three added simultaneously."},
            {"id": 4, "text": "Maithili", "verdict": "false", "reason": "Maithili was added by the 92nd Amendment 2003 (along with Bodo, Dogri, Santhali). Different amendment, different year."}
        ],
        "answer_justification": {
            "fact": "71st Amendment (1992) added exactly Konkani, Manipuri, Nepali — three languages. Maithili came via 92nd Amendment 2003. Answer: A (1, 2 and 3).",
            "elimination_path": "Eliminate any option containing Maithili (4) — that's the 92nd Amendment 2003 intruder. Only option A (1, 2, 3) excludes Maithili."
        },
        "concept_hooks": ["71st Amendment 1992 languages Eighth Schedule", "92nd Amendment 2003 Maithili Bodo Dogri Santhali", "Eighth Schedule 22 languages India"]
    },
    "1054": {
        "question_type": "matching",
        "trap_pattern": "person_attribution",
        "trap_explanation": "Pairs 2 and 4 swap the leaders: C. Rajagopalachari founded the Swatantra Party (not Socialist Party); Acharya Narendra Dev was Socialist Party (not Swatantra). The correct leaders are cross-listed between the wrong parties.",
        "pairs": [
            {"id": 1, "left": "Bharatiya Jana Sangh", "right": "Dr. Shyama Prasad Mukherjee", "verdict": "correct", "reason": "BJS founded 1951 by Shyama Prasad Mukherjee — unambiguous."},
            {"id": 2, "left": "Socialist Party", "right": "C. Rajagopalachari", "verdict": "wrong", "reason": "Rajagopalachari founded Swatantra Party (1959), not Socialist Party. Socialist Party: Acharya Narendra Dev, JP Narayan."},
            {"id": 3, "left": "Congress for Democracy", "right": "Jagjivan Ram", "verdict": "correct", "reason": "Congress for Democracy founded 1977 by Jagjivan Ram (with Bahuguna, Satpathy) after Emergency."},
            {"id": 4, "left": "Swatantra Party", "right": "Acharya Narendra Dev", "verdict": "wrong", "reason": "Swatantra Party (1959) was founded by C. Rajagopalachari. Narendra Dev was associated with Socialist Party."}
        ],
        "answer_justification": {
            "fact": "Pairs 1 and 3 correct; 2 and 4 wrong (Rajagopalachari and Narendra Dev swapped). Only two correct → Answer: B.",
            "elimination_path": "Pairs 2 and 4 are mirror-swapped errors. Rajagopalachari = Swatantra (not Socialist). Narendra Dev = Socialist (not Swatantra). Pairs 1, 3 solid → two correct → B."
        },
        "concept_hooks": ["Swatantra Party founder Rajagopalachari 1959", "Bharatiya Jana Sangh Shyama Prasad Mukherjee", "Congress for Democracy Jagjivan Ram 1977 Emergency"]
    },
    # --- Wave 1 / Batch B: Economy (15 cards, 2026-04-25) ---
    "1092": {
        "question_type": "matching",
        "trap_pattern": "overlapping_categories",
        "trap_explanation": "Storage and mineral exploration are the inversion traps. Storage of agricultural produce is tertiary (service: warehousing), not secondary. Mineral exploration is secondary (extraction), not tertiary. Dairy (production) is primary; weaving is secondary — both correct.",
        "pairs": [
            {"id": 1, "left": "Storage of agricultural produce", "right": "Secondary", "verdict": "wrong", "reason": "Storage is a service (warehousing) → tertiary sector. No transformation of goods occurs."},
            {"id": 2, "left": "Dairy farm", "right": "Primary", "verdict": "correct", "reason": "Dairy farming = animal husbandry; production of raw material → primary sector."},
            {"id": 3, "left": "Mineral exploration", "right": "Tertiary", "verdict": "wrong", "reason": "Mineral extraction from nature → primary sector (not tertiary). Exploration is extraction-adjacent, still primary."},
            {"id": 4, "left": "Weaving cloth", "right": "Secondary", "verdict": "correct", "reason": "Weaving transforms raw yarn into cloth — manufacturing → secondary sector."}
        ],
        "answer_justification": {
            "fact": "Pairs 2 and 4 correct (dairy=primary, weaving=secondary); pairs 1 and 3 wrong → option (b) Only two.",
            "elimination_path": "Eliminate (d) immediately: pair 1 (storage=secondary) is wrong — storage is a service. Eliminate (c)/(a): pair 3 (mineral=tertiary) is wrong — extraction is primary. Pairs 2 and 4 correct → (b)."
        },
        "concept_hooks": ["Three-sector economy NCERT Class 10", "Primary secondary tertiary sector India examples", "Economic activity classification UPSC"]
    },
    "1093": {
        "question_type": "matching",
        "trap_pattern": "technical_vs_common_meaning",
        "trap_explanation": "Common sense says a plough 'does work' (feels active = working capital). Wrong. Fixed vs working capital = durable tool vs consumed-in-production input. Plough lasts years = fixed. Yarn/petrol are consumed in one cycle = working.",
        "pairs": [
            {"id": 1, "left": "Farmer's plough", "right": "Working capital", "verdict": "wrong", "reason": "Plough is durable; used repeatedly over years → fixed capital. Not consumed in one production cycle."},
            {"id": 2, "left": "Computer", "right": "Fixed capital", "verdict": "correct", "reason": "Computer lasts multiple years, not consumed in production → fixed capital. Correct per NCERT Class 10."},
            {"id": 3, "left": "Yarn used by weaver", "right": "Fixed capital", "verdict": "wrong", "reason": "Yarn is entirely consumed in producing cloth → working capital, not fixed."},
            {"id": 4, "left": "Petrol", "right": "Working capital", "verdict": "correct", "reason": "Petrol consumed in one use → working capital. Classic NCERT example."}
        ],
        "answer_justification": {
            "fact": "Pairs 2 and 4 correct (computer=fixed, petrol=working); pairs 1 and 3 wrong → option (b) Only two.",
            "elimination_path": "Key test: is the item consumed in one production cycle? Plough (no) → fixed, not working. Yarn (yes) → working, not fixed. Computer (no) → fixed ✓. Petrol (yes) → working ✓. Two correct → (b)."
        },
        "concept_hooks": ["Fixed capital working capital NCERT", "Physical capital classification India Class 10", "Working capital examples economics"]
    },
    "1094": {
        "question_type": "assertion_reason",
        "trap_pattern": "explanatory_chain",
        "trap_explanation": "Both statements are true. The trap is doubting the explanatory link — students may think US not defaulting is a separate financial fact unconnected to 'full faith and credit.' But the absence of hard-asset backing IS precisely why a default makes bondholder claims unenforceable.",
        "claim_statement": {"id": 1, "text": "If the USA were to default on its debt, holders of US Treasury Bonds will not be able to exercise their claims to receive payment.", "verdict": "true", "reason": "US Treasuries are obligations backed only by the government's promise. Default = government refuses payment; no hard asset for bondholders to seize."},
        "supporting_statements": [
            {"id": 2, "text": "The USA Government debt is not backed by any hard assets, but only by the faith of the Government.", "verdict": "true", "explains_claim": True, "reason": "True. US Treasuries carry 'full faith and credit' — no gold, property, or collateral. Default removes that faith, making bondholder claims unenforceable. Direct causal explanation."}
        ],
        "answer_justification": {
            "fact": "Both I and II true; II (no hard-asset backing) directly explains why default leaves bondholders with no recourse → option (a).",
            "elimination_path": "Verify I (default = no payment, true). Verify II (full faith and credit only, no hard assets — true). Does II explain I? Yes: fiat-only backing means default extinguishes all claims. → (a)."
        },
        "concept_hooks": ["US Treasury bonds full faith and credit", "Sovereign debt default bondholder rights", "Government debt hard asset backing"]
    },
    "1268": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "Both statements sound plausible but are false. WOS in India DO have a minimum paid-up capital of ₹500 crore. The RBI board rule is 'majority Indian nationals + at least one-third independent' — not a simple 50% threshold as stated in Statement 2.",
        "statements": [
            {"id": 1, "text": "There is no minimum capital requirement for wholly owned banking subsidiaries in India.", "verdict": "false", "reason": "RBI mandates minimum paid-up capital of ₹500 crore for foreign bank WOS in India. Statement directly contradicts this requirement."},
            {"id": 2, "text": "For wholly owned banking subsidiaries in India, at least 50% of the board members should be Indian nationals.", "verdict": "false", "reason": "RBI requires majority of directors to be Indian nationals AND at least one-third to be independent directors — not a simple '50%' threshold as stated."}
        ],
        "answer_justification": {
            "fact": "Both statements false → option (d) neither 1 nor 2.",
            "elimination_path": "Statement 1: ₹500 crore minimum capital exists — kills (a) and (c). Statement 2: RBI rule is 'majority Indian + 1/3 independent,' not exactly '50%' — kills (b). → (d)."
        },
        "concept_hooks": ["RBI foreign bank subsidiary rules India", "WOS wholly owned subsidiary banking RBI capital", "Foreign bank board composition RBI guidelines"]
    },
    "1269": {
        "question_type": "assertion_reason",
        "trap_pattern": "explanatory_chain",
        "trap_explanation": "Statement I (risk spreading) is true and the defining feature of syndicated lending. Statement II falsely claims syndicated loans cannot be credit lines — they can be (revolving credit facilities are common). UPSC master was null; coaching consensus settles at (c).",
        "claim_statement": {"id": 1, "text": "Syndicated lending spreads the risk of borrower default across multiple lenders.", "verdict": "true", "reason": "Core feature of syndicated loans: a lead arranger brings in multiple banks, each taking a share, spreading default risk across the syndicate."},
        "supporting_statements": [
            {"id": 2, "text": "The syndicated loan can be a fixed amount/lump sum of funds, but cannot be a credit line.", "verdict": "false", "explains_claim": False, "reason": "False. Syndicated loans routinely take the form of revolving credit facilities (credit lines). The 'cannot be a credit line' restriction does not exist."}
        ],
        "answer_justification": {
            "fact": "Statement I true (risk spreading confirmed); Statement II false (credit lines ARE possible in syndicated lending) → option (c).",
            "elimination_path": "Statement I: risk-spreading is the definition of syndicated lending — true. Statement II: revolving credit facilities exist in syndicated loans — 'cannot be credit line' is false. I correct, II wrong → (c)."
        },
        "concept_hooks": ["Syndicated loan structure banking", "Revolving credit facility syndicated lending", "Syndicated lending risk distribution"]
    },
    "1270": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "Statement 3 is the kill: CBDC is NOT insured against inflation by design — it is a fiat currency subject to the same inflation risks as cash. Statements 1, 2, and 4 are all true. Confusing 'stable by design' with 'inflation-proof' is the trap.",
        "statements": [
            {"id": 1, "text": "It is a sovereign currency issued by the Reserve Bank of India (RBI) in alignment with its monetary policy.", "verdict": "true", "reason": "Digital Rupee (e₹) is sovereign legal tender issued by RBI, integral to monetary policy. RBI Concept Note 2022 explicitly confirms this."},
            {"id": 2, "text": "It appears as a liability on the RBI's balance sheet.", "verdict": "true", "reason": "Like physical currency, e₹ is an RBI liability. This is the defining feature distinguishing CBDC from commercial bank money."},
            {"id": 3, "text": "It is insured against inflation by its very design.", "verdict": "false", "reason": "CBDC is fiat money — its value is not algorithmically fixed or commodity-backed. Inflation affects e₹ identically to physical cash."},
            {"id": 4, "text": "It is freely convertible against commercial bank money and cash.", "verdict": "true", "reason": "e₹ is at par with cash; 1:1 convertibility with bank deposits and physical currency is a core design principle of India's CBDC."}
        ],
        "answer_justification": {
            "fact": "Statements 1, 2, 4 true; Statement 3 false (CBDC is not inflation-proof) → option (d) 1, 2 and 4.",
            "elimination_path": "Eliminate (b) and (c) first: both include statement 3 (inflation-insured) which is false for any fiat currency. Remaining options include (a) and (d); (d) adds statement 4 (convertibility, true) → (d)."
        },
        "concept_hooks": ["Digital Rupee CBDC RBI features", "CBDC vs cryptocurrency inflation", "RBI balance sheet CBDC liability"]
    },
    "1333": {
        "question_type": "standard",
        "trap_pattern": "overlapping_categories",
        "trap_explanation": "CBLO sounds like a bond-market or stock-market instrument given the word 'Obligation.' It is a short-tenor, collateral-backed overnight/near-term instrument — squarely money market. CCIL operated it. Discontinued in 2018 (replaced by TREPS).",
        "answer_justification": {
            "fact": "CBLO = Collateralised Borrowing and Lending Obligation, operated by CCIL. Short-term, overnight to 1-year maturity → money market instrument.",
            "hook": "CCIL is the operator; the collateral is G-Secs/T-Bills. Same-day settlement makes it money market, not bond market.",
            "elimination_path": "Bond market (a): CBLO has no coupon, not tradable like bonds. Forex (b): no currency exchange involved. Stock market (d): not equity. Money market (c): short-term, collateral-backed overnight lending → correct."
        },
        "distractor_analysis": [
            {"option": "a", "verdict": "wrong", "reason": "Bond market instruments are long-tenor coupon-bearing. CBLO is short-tenor collateral repo — no coupon.", "confused_with": "G-Sec repo market"},
            {"option": "b", "verdict": "wrong", "reason": "Forex market involves currency exchange. CBLO is domestic rupee borrowing/lending.", "confused_with": None},
            {"option": "d", "verdict": "wrong", "reason": "Stock market = equity. CBLO involves no equity instruments; operates via G-Sec collateral.", "confused_with": None}
        ],
        "concept_hooks": ["CBLO CCIL money market India", "TREPS replaced CBLO 2018", "Money market instruments India RBI"]
    },
    "1334": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "Statement 1 is the kill-trap: NBFCs do NOT have access to RBI's LAF window — that is exclusively for scheduled commercial banks + primary dealers. FIIs can hold G-Secs (2); stock exchanges can offer debt platforms (3). Students who half-know NBFC regulatory access mark 1 as true.",
        "statements": [
            {"id": 1, "text": "Non-Banking Financial Companies can access the Liquidity Adjustment Facility window of the Reserve Bank of India.", "verdict": "false", "reason": "LAF (repo/reverse repo) is available only to scheduled commercial banks and primary dealers. NBFCs cannot borrow from RBI's LAF window."},
            {"id": 2, "text": "Foreign Institutional Investors can hold Government Securities (G-Secs).", "verdict": "true", "reason": "FIIs/FPIs are permitted to invest in G-Secs under RBI's Foreign Portfolio Investment limits. Investment cap applies but access is permitted."},
            {"id": 3, "text": "Stock Exchanges can offer separate trading platforms for debts.", "verdict": "true", "reason": "BSE and NSE both operate dedicated debt platforms. SEBI-regulated corporate bond trading is active."}
        ],
        "answer_justification": {
            "fact": "Statement 1 false (NBFCs excluded from LAF); 2 and 3 true → option (d) 2 and 3 only.",
            "elimination_path": "LAF exclusion of NBFCs kills statement 1 → eliminates (a) and (c). Statements 2 (FII G-Sec access ✓) and 3 (debt platform ✓) both true → option (d)."
        },
        "concept_hooks": ["NBFC RBI LAF access eligibility", "FII FPI Government Securities India", "Stock exchange debt trading platform India"]
    },
    "1335": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_overgeneralization",
        "trap_explanation": "The trap is assuming retail investors cannot trade corporate bonds or G-Secs — that they are institutional-only markets. RBI Retail Direct (2021) opened G-Sec access directly to individual retail investors. All three categories are permitted.",
        "statements": [
            {"id": 1, "text": "Insurance Companies", "verdict": "true", "reason": "IRDA mandates insurance companies hold G-Secs and corporate bonds as approved investments. They are major institutional participants."},
            {"id": 2, "text": "Pension Funds", "verdict": "true", "reason": "PFRDA-regulated pension funds invest in both G-Secs and corporate bonds as per their investment mandate."},
            {"id": 3, "text": "Retail Investors", "verdict": "true", "reason": "RBI Retail Direct Scheme (Nov 2021) allows individuals to directly buy G-Secs. SEBI also permits retail corporate bond trading on exchanges."}
        ],
        "answer_justification": {
            "fact": "All three — insurance, pension, and retail investors — can trade corporate bonds and G-Secs → option (d) 1, 2 and 3.",
            "elimination_path": "Anchor on retail: RBI Retail Direct (2021) demolished the 'retail can't buy G-Secs' assumption. Once retail (3) is confirmed, all three are in → eliminate (a), (b), (c) → (d)."
        },
        "concept_hooks": ["RBI Retail Direct Scheme G-Secs", "Insurance pension fund G-Sec investment India", "Corporate bond market participants India"]
    },
    "1336": {
        "question_type": "statement_eval",
        "trap_pattern": "overlapping_categories",
        "trap_explanation": "Motor vehicles are real assets (tangible goods), not financial instruments. ETFs and currency swaps are financial instruments — one equity-based, one derivative. The trap is students unsure whether a currency swap qualifies as a 'financial instrument' and hedging to (a) only.",
        "statements": [
            {"id": 1, "text": "Exchange-Traded Funds (ETF)", "verdict": "true", "reason": "ETFs are securities traded on stock exchanges; they are standardised financial instruments representing a basket of assets."},
            {"id": 2, "text": "Motor vehicles", "verdict": "false", "reason": "Motor vehicles are tangible physical assets — goods, not financial instruments. A financial instrument is a contract representing monetary value."},
            {"id": 3, "text": "Currency swap", "verdict": "true", "reason": "Currency swaps are OTC derivative contracts — exchange of principal and interest in different currencies. Clearly a financial instrument."}
        ],
        "answer_justification": {
            "fact": "ETF and currency swap are financial instruments; motor vehicles are not → option (d) 1 and 3 only.",
            "elimination_path": "Kill motor vehicles (2) immediately — physical goods are never financial instruments. Eliminates (b) and (c). ETF (1) and currency swap (3) are both financial instruments → (d)."
        },
        "concept_hooks": ["Financial instruments definition types", "Currency swap derivative instrument", "ETF financial instrument classification"]
    },
    "1373": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "Statement 2 is the inversion trap: Companies Act 2013 Section 135 mandates 2% of average net profit for CSR — there IS a minimum spending requirement. Statement 1 (employee benefits excluded) is correctly stated. Marking 'both' or 'neither' are the likely wrong picks.",
        "statements": [
            {"id": 1, "text": "Expenditures that benefit the company directly or its employees will not be considered as CSR activities.", "verdict": "true", "reason": "Companies Act 2013 CSR rules explicitly exclude activities that benefit only employees or the company itself from the Schedule VII CSR definition."},
            {"id": 2, "text": "CSR rules do not specify minimum spending on CSR activities.", "verdict": "false", "reason": "Section 135 mandates 2% of average net profit of preceding 3 years as minimum CSR spend for eligible companies. A floor clearly exists."}
        ],
        "answer_justification": {
            "fact": "Statement 1 true (employee benefit exclusion is explicit); Statement 2 false (2% net profit mandate exists) → option (a) 1 only.",
            "elimination_path": "Anchor on Section 135: 2% net profit minimum is foundational CSR law. Statement 2 says 'no minimum' — directly false. Eliminate (b), (c). Statement 1 (employee exclusion) is confirmed text of CSR rules → (a)."
        },
        "concept_hooks": ["Companies Act 2013 Section 135 CSR", "CSR 2% net profit India mandatory", "CSR Schedule VII eligible activities India"]
    },
    "1483": {
        "question_type": "standard",
        "trap_pattern": "technical_vs_common_meaning",
        "trap_explanation": "Three distractors use common-sense definitions: births per 1000 people (birth rate), births per couple (not a standard measure), or birth-minus-death (natural growth rate). TFR is a woman-specific, lifetime average — a technical demographic concept distinct from all three.",
        "answer_justification": {
            "fact": "TFR = average number of live births a woman would have over her entire child-bearing period (ages 15-49). India's TFR ~2.0 per NFHS-5.",
            "hook": "TFR is per woman, not per couple, not per 1000 people. Child-bearing age = 15-49. Replacement TFR = 2.1.",
            "elimination_path": "Eliminate (a): births per 1000 = crude birth rate, not TFR. Eliminate (b): 'per couple' is not a demographic measure. Eliminate (c): birth rate minus death rate = natural growth rate. Only (d) matches the technical definition."
        },
        "distractor_analysis": [
            {"option": "a", "verdict": "wrong", "reason": "Births per 1000 people = crude birth rate. TFR is per woman, not per population.", "confused_with": "Crude Birth Rate"},
            {"option": "b", "verdict": "wrong", "reason": "'Per couple' ignores single women and is not a standardised demographic indicator.", "confused_with": None},
            {"option": "c", "verdict": "wrong", "reason": "Birth rate minus death rate = natural rate of population growth, not TFR.", "confused_with": "Natural Growth Rate"}
        ],
        "concept_hooks": ["Total Fertility Rate definition demography", "TFR vs crude birth rate India", "NFHS-5 India fertility data"]
    },
    "1526": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "Statement 1 adds 'six months post-delivery' — PMSMA covers only antenatal care (2nd and 3rd trimester), NOT postnatal care. Statement 2 (voluntary private sector participation) is correctly stated. The postnatal insertion in S1 is the subtle fabrication.",
        "statements": [
            {"id": 1, "text": "This scheme guarantees a minimum package of antenatal care services to women in their second and third trimesters of pregnancy and six months post-delivery health care service.", "verdict": "false", "reason": "PMSMA covers antenatal care on the 9th of every month for 2nd/3rd trimester women only. No postnatal component exists under PMSMA."},
            {"id": 2, "text": "Under this scheme, private sector health care providers of certain specialities can volunteer to provide services at nearby government health facilities.", "verdict": "true", "reason": "PMSMA explicitly invites private/NGO sector obstetricians, gynaecologists, and physicians to volunteer at government health facilities on the 9th of each month."}
        ],
        "answer_justification": {
            "fact": "Statement 1 false (no postnatal component); Statement 2 true (voluntary private sector participation) → option (b) 2 only.",
            "elimination_path": "Test S1 against PMSMA mandate: antenatal only, on 9th of month, 2nd/3rd trimester. 'Six months post-delivery' is a fabrication → eliminates (a) and (c). S2 (private volunteerism) is confirmed PMSMA design → (b)."
        },
        "concept_hooks": ["PMSMA antenatal care scheme India", "Pradhan Mantri Surakshit Matritva Abhiyan 9th", "PMSMA private sector participation"]
    },
    "1571": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "Statement 1 says entry age 21-40; correct is 18-40. Statement 4 says family pension to 'spouse and unmarried daughters'; correct is 50% to spouse only. Statements 2 (age-specific contribution) and 3 (₹3000/month at 60) are correct. Multiple inversions in one question.",
        "statements": [
            {"id": 1, "text": "The entry age group for enrolment in the scheme is 21 to 40 years.", "verdict": "false", "reason": "PM-SYM entry age is 18-40 years, not 21-40. The lower bound of 18 is precise and commonly inverted in exams."},
            {"id": 2, "text": "Age specific contribution shall be made by the beneficiary.", "verdict": "true", "reason": "PM-SYM uses age-based contribution slabs: younger entrants pay lower monthly premiums (₹55-₹200), which government matches 1:1."},
            {"id": 3, "text": "Each subscriber shall receive a minimum pension of ₹3,000 per month after attaining the age of 60 years.", "verdict": "true", "reason": "Guaranteed minimum pension of ₹3,000/month at age 60 is the scheme's core promise, funded by beneficiary + Central Government contributions."},
            {"id": 4, "text": "Family pension is applicable to the spouse and unmarried daughters.", "verdict": "false", "reason": "PM-SYM family pension = 50% of pension to spouse only upon subscriber's death. Unmarried daughters are not beneficiaries under the scheme."}
        ],
        "answer_justification": {
            "fact": "Statements 2 and 3 correct; Statements 1 (age=18 not 21) and 4 (spouse only, not daughters) false → option (b) 2 and 3 only.",
            "elimination_path": "Kill S1: entry age 18, not 21 → eliminates (a) and (d). Kill S4: family pension to spouse only, not daughters → eliminates (a) and (c). Survivors: S2 and S3 → (b)."
        },
        "concept_hooks": ["PM-SYM PM Shram Yogi Maandhan scheme", "Unorganised worker pension scheme India", "PM-SYM entry age contribution pension"]
    },
    "1590": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "All three statements are true. The trap is doubting statement 1 (100% central funding sounds unusually generous) or statement 3 (transliteration sounds like a peripheral detail). DILRMP was restructured as 100% CSS in 2016; all three elements are confirmed programme components.",
        "statements": [
            {"id": 1, "text": "To implement the scheme, the Central Government provides 100% funding.", "verdict": "true", "reason": "DILRMP is a 100% Centrally Sponsored Scheme since its restructuring. States receive full central funding for land record digitisation components."},
            {"id": 2, "text": "Under the Scheme, Cadastral Maps are digitised.", "verdict": "true", "reason": "Cadastral map digitisation is a core DILRMP component alongside computerisation of Records of Rights (RoR)."},
            {"id": 3, "text": "An initiative has been undertaken to transliterate the Records of Rights from local language to any of the languages recognized by the Constitution of India.", "verdict": "true", "reason": "DILRMP includes transliteration of RoR across Scheduled languages to enable inter-state portability and access. Active component of the programme."}
        ],
        "answer_justification": {
            "fact": "All three statements true → option (d) 1, 2 and 3.",
            "elimination_path": "Don't baulk at '100% central' — DILRMP is explicitly a 100% CSS (post-2016). Transliteration (S3) is an active DILRMP sub-component. All three confirmed → (d)."
        },
        "concept_hooks": ["DILRMP land records digitisation India", "Digital India Land Records Modernisation Programme", "DILRMP 100% centrally sponsored scheme"]
    },
    # --- Wave 1 / Batch C: Geography (17 cards, 2026-04-25) ---
    "1677": {
        "question_type": "assertion_reason",
        "trap_pattern": "explanatory_chain",
        "trap_explanation": "Both II and III are factually true AND both independently explain how rainfall weathers rocks — carbonic acid (II) causes carbonation, dissolved oxygen (III) causes oxidation. Students eliminate III thinking only CO2 matters for chemical weathering, picking (b) instead of (a).",
        "claim_statement": {"id": 1, "text": "Rainfall is one of the reasons for weathering of rocks.", "verdict": "true", "reason": "Rain drives chemical weathering via two distinct pathways: carbonic acid (carbonation) and dissolved oxygen (oxidation). Both dissolve and decompose minerals in rocks."},
        "supporting_statements": [
            {"id": 2, "text": "Rain water contains carbon dioxide in solution.", "verdict": "true", "explains_claim": True, "reason": "CO2 + H2O → H2CO3 (carbonic acid). This acid dissolves limestone, feldspar, and other minerals — carbonation is a primary chemical weathering agent."},
            {"id": 3, "text": "Rain water contains atmospheric oxygen.", "verdict": "true", "explains_claim": True, "reason": "Dissolved O2 in rainwater oxidises iron-bearing minerals (e.g., pyrite → limonite/rust). Oxidation is a distinct, real chemical weathering pathway."}
        ],
        "answer_justification": {
            "fact": "Both II (carbonic acid) and III (oxygen-oxidation) are true AND both explain rainfall weathering → option (a).",
            "elimination_path": "Confirm II: rain absorbs CO2 → carbonic acid → carbonation (true, explains). Confirm III: dissolved O2 → oxidation of iron minerals (true, explains). Both explain → (a), not (b)."
        },
        "concept_hooks": ["Chemical weathering carbonation process", "Oxidation weathering iron minerals", "Carbonic acid limestone dissolution"]
    },
    "1678": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_overgeneralization",
        "trap_explanation": "Students confidently include pyroclastic debris and ash but doubt nitrogen compounds — volcanoes are associated with SO2 and CO2, not nitrogen. However, volcanoes emit nitrogen compounds (N2, NOx) from magmatic gas and decomposed crustal material. All four are genuine volcanic products.",
        "statements": [
            {"id": 1, "text": "Pyroclastic debris", "verdict": "true", "reason": "Fragmented rock, lava, and ash ejected explosively. Core solid product of volcanic eruptions — unconditionally correct."},
            {"id": 2, "text": "Ash and dust", "verdict": "true", "reason": "Fine pyroclastic material — volcanic ash is the most widely dispersed eruption product, reaching stratosphere and affecting climate."},
            {"id": 3, "text": "Nitrogen compounds", "verdict": "true", "reason": "Volcanoes emit N2 (dominant atmospheric gas), ammonia, and NOx from magmatic degassing and thermal breakdown of country rock. Less publicised but confirmed."},
            {"id": 4, "text": "Sulphur compounds", "verdict": "true", "reason": "SO2 is the signature volcanic gas; also H2S. SO2 → sulphate aerosols causing volcanic winter and acid rain. Classic eruption product."}
        ],
        "answer_justification": {
            "fact": "All four — pyroclastic debris, ash, nitrogen compounds, sulphur compounds — are genuine volcanic products → option (d) All four.",
            "elimination_path": "Pyroclastic + ash are certain (eliminate 'Only one'/'Only two'). Sulphur (SO2) is famous. Nitrogen compounds are the doubt-seed — but magmatic degassing produces N2 and NOx. All four confirmed → (d)."
        },
        "concept_hooks": ["Volcanic gases composition SO2 CO2 N2", "Pyroclastic debris volcanic eruption products", "Volcanic outgassing atmosphere"]
    },
    "1679": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "June 21 is Northern Hemisphere summer solstice. Equator always gets exactly 12 hours — not more, not less. Tropic of Capricorn gets its shortest day (~10.5h). The trap inverts intuitions: Arctic Circle gets 24h, Tropic of Cancer gets ~13.5h. Equator and Capricorn are the eliminators.",
        "statements": [
            {"id": 1, "text": "Equator", "verdict": "false", "reason": "Equator receives exactly 12h of daylight every day of the year — sun rises due east and sets due west regardless of season."},
            {"id": 2, "text": "Tropic of Cancer", "verdict": "true", "reason": "June 21 = Northern summer solstice. Sun is overhead at Tropic of Cancer — longest day ~13.5 hours. More than 12h confirmed."},
            {"id": 3, "text": "Tropic of Capricorn", "verdict": "false", "reason": "June 21 is Southern Hemisphere winter solstice. Tropic of Capricorn has its shortest day (~10.5h) — well below 12h."},
            {"id": 4, "text": "Arctic Circle", "verdict": "true", "reason": "Arctic Circle on June 21 experiences midnight sun — 24h of daylight. Far more than 12h."}
        ],
        "answer_justification": {
            "fact": "Tropic of Cancer (~13.5h) and Arctic Circle (24h) exceed 12h on June 21. Equator = exactly 12h, Capricorn = ~10.5h → option (d) 2 and 4.",
            "elimination_path": "Eliminate 1 (equator = perpetual 12h). Eliminate 3 (Capricorn = Southern winter, shortest day <12h). 2 and 4 remain → (d)."
        },
        "concept_hooks": ["Summer solstice June 21 day length latitude", "Midnight sun Arctic Circle", "Insolation equinox solstice latitude"]
    },
    "1719": {
        "question_type": "assertion_reason",
        "trap_pattern": "explanatory_chain",
        "trap_explanation": "Statement-I is factually wrong — the atmosphere is heated MORE by terrestrial (long-wave) radiation than by incoming solar (short-wave) radiation, which largely passes through. GHGs are transparent to short-wave but absorb long-wave. Most students mark I as true by intuition — the sun heats everything.",
        "claim_statement": {"id": 1, "text": "The atmosphere is heated more by incoming solar radiation than by terrestrial radiation.", "verdict": "false", "reason": "Solar short-wave radiation largely passes through the atmosphere (transparent to it). The atmosphere is mainly heated by terrestrial long-wave IR radiation absorbed by GHGs and clouds."},
        "supporting_statements": [
            {"id": 2, "text": "Carbon dioxide and other greenhouse gases in the atmosphere are good absorbers of long wave radiation.", "verdict": "true", "explains_claim": False, "reason": "True — GHGs absorb terrestrial IR radiation. But this supports why terrestrial radiation heats the atmosphere, directly contradicting Statement-I rather than explaining it."}
        ],
        "answer_justification": {
            "fact": "Statement-I is false (atmosphere heated by terrestrial long-wave, not solar short-wave). Statement-II is true → option (d).",
            "elimination_path": "Key inversion: solar radiation PASSES THROUGH atmosphere (short-wave, transparent). Terrestrial IR is ABSORBED by GHGs — that heats the atmosphere. I is the inverted statement. II is independently true → (d)."
        },
        "concept_hooks": ["Atmospheric heating terrestrial radiation", "Greenhouse effect long-wave short-wave radiation", "Solar radiation atmospheric transparency"]
    },
    "1720": {
        "question_type": "assertion_reason",
        "trap_pattern": "explanatory_chain",
        "trap_explanation": "Both statements are true AND Statement-II genuinely explains Statement-I. The trap is marking (b) — assuming it's a coincidence rather than a causal chain. Convectional currents at the equator (driven by intense surface heating) physically push the tropopause higher.",
        "claim_statement": {"id": 1, "text": "Thickness of the troposphere at the equator is much greater as compared to poles.", "verdict": "true", "reason": "Troposphere is ~16-18 km at equator, ~8 km at poles. Heat-driven convection at equator raises the tropopause significantly higher."},
        "supporting_statements": [
            {"id": 2, "text": "At the equator, heat is transported to great heights by strong convectional currents.", "verdict": "true", "explains_claim": True, "reason": "Intense solar heating at equator generates vigorous convection — warm air rises to great heights before cooling to lapse rate equilibrium, physically extending the troposphere upward."}
        ],
        "answer_justification": {
            "fact": "Both true; convectional currents directly cause the troposphere to extend higher at equator → option (a) II explains I.",
            "elimination_path": "Verify I (equator ~16-18 km, poles ~8 km — true). Verify II (convection driven by intense equatorial heating — true). Ask: does II cause I? Yes — convection physically lifts the tropopause. → (a)."
        },
        "concept_hooks": ["Troposphere thickness equator vs poles", "Convectional currents troposphere height", "Tropopause altitude latitude"]
    },
    "1721": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "Statement 2 inverts reality: water vapour is MAXIMUM in tropical regions (warm air holds more moisture), not at poles. Polar air is cold and dry — holds very little water vapour. Students may confuse 'ice and snow = water' with atmospheric water vapour content.",
        "statements": [
            {"id": 1, "text": "It is a gas, the amount of which decreases with altitude.", "verdict": "true", "reason": "Water vapour is concentrated in the lower troposphere (bulk in lowest 5 km). It decreases rapidly with altitude as temperature drops and air thins."},
            {"id": 2, "text": "Its percentage is maximum at the poles.", "verdict": "false", "reason": "Water vapour is maximum in warm tropical regions — warm air has higher saturation capacity. Polar air is cold, dry, and holds minimal water vapour."}
        ],
        "answer_justification": {
            "fact": "Statement 1 true (decreases with altitude). Statement 2 false (maximum in tropics, not poles) → option (a) 1 only.",
            "elimination_path": "Statement 1 is basic thermodynamics — water vapour condenses as temperature falls with altitude. Statement 2 inverts the tropical-polar contrast. Poles are dry; tropics are humid → eliminate 2. Answer (a)."
        },
        "concept_hooks": ["Water vapour altitude troposphere distribution", "Atmospheric moisture tropical vs polar", "Saturation vapour pressure temperature"]
    },
    "1722": {
        "question_type": "standard",
        "trap_pattern": "distractor_by_topic_association",
        "trap_explanation": "The description — low temperature range, year-round precipitation, 50-250 cm — fits Marine West Coast exactly. Equatorial climate has higher rainfall (>200 cm) and no winter. China-type and Humid Subtropical have hot summers and drier winters. The distractor pulls toward Equatorial since 'year-round rain' sounds tropical.",
        "answer_justification": {
            "fact": "Marine West Coast: mild winters, cool summers (low range), year-round rain heavier in winter, 50-250 cm total. Matches all three descriptors.",
            "hook": "Marine West Coast is the ONLY mid-latitude climate with year-round precipitation — all others have a dry season.",
            "elimination_path": "Equatorial: rainfall >200 cm, no winter, high temps. China-type/Humid Subtropical: hot humid summers, relatively dry winters. Marine West Coast: cool summers, mild winters, year-round rain → (d)."
        },
        "distractor_analysis": [
            {"option": "a", "verdict": "wrong", "reason": "Equatorial has high temperatures year-round, rainfall often >250 cm, no cool season — temperature range is NOT low in the mid-latitude sense.", "confused_with": "Year-round rainfall pattern"},
            {"option": "b", "verdict": "wrong", "reason": "China-type (Humid Subtropical) has hot, humid summers and mild winters — wider temperature range and less winter precipitation than Marine West Coast.", "confused_with": None},
            {"option": "c", "verdict": "wrong", "reason": "Humid subtropical has marked summer precipitation maximum and hot summers — not a low annual range or year-round uniform distribution.", "confused_with": None}
        ],
        "concept_hooks": ["Marine West Coast climate characteristics", "Koppen climate classification Cfb", "Mid-latitude oceanic climate precipitation"]
    },
    "1723": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "Both statements about Coriolis force are correct. The trap targets Statement 1 — students often think Coriolis is purely latitude-dependent and forget velocity dependence. Coriolis force = 2mΩv·sinφ — both velocity (v) and latitude (sinφ) matter.",
        "statements": [
            {"id": 1, "text": "It increases with increase in wind velocity.", "verdict": "true", "reason": "Coriolis force F = 2mΩv·sinφ — directly proportional to velocity (v). Faster-moving air/objects experience stronger Coriolis deflection."},
            {"id": 2, "text": "It is maximum at the poles and is absent at the equator.", "verdict": "true", "reason": "sinφ = 1 at poles (φ=90°), sinφ = 0 at equator (φ=0°). Maximum deflection at poles; zero deflection at equator — confirmed by the formula."}
        ],
        "answer_justification": {
            "fact": "Both statements correctly describe Coriolis force (F = 2mΩv·sinφ) → option (c) Both 1 and 2.",
            "elimination_path": "Apply F = 2mΩv·sinφ: Statement 1 — v appears (velocity proportional, true). Statement 2 — sinφ: max at pole, zero at equator (true). Both confirmed → (c)."
        },
        "concept_hooks": ["Coriolis force formula derivation", "Coriolis effect latitude velocity dependence", "Geostrophic wind Coriolis balance"]
    },
    "1787": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "Statement 1 is correct (January isotherms bow north over warmer oceans, south over colder continents in Northern Hemisphere). Statement 2 inversion: Gulf Stream and North Atlantic Drift are WARM currents, not cold. Their warmth bends isotherms poleward (north) — the mechanism is right but the current's thermal character is inverted.",
        "statements": [
            {"id": 1, "text": "The isotherms deviate to the north over the ocean and to the south over the continent.", "verdict": "true", "reason": "In January (Northern winter): oceans retain heat, isotherms deflect poleward (north). Continental land is cold; isotherms deflect equatorward (south). Classic ocean-continent isotherm pattern."},
            {"id": 2, "text": "The presence of cold ocean currents, Gulf Stream and North Atlantic Drift make the North Atlantic Ocean colder and the isotherms bend towards the north.", "verdict": "false", "reason": "Gulf Stream and North Atlantic Drift are WARM currents. They warm the North Atlantic, pushing isotherms northward — the effect is right but they are labelled 'cold' (inversion)."}
        ],
        "answer_justification": {
            "fact": "Statement 1 true (correct January isotherm pattern). Statement 2 false (Gulf Stream/NAD are warm, not cold currents) → option (a) 1 only.",
            "elimination_path": "Statement 2 trap: 'cold ocean currents, Gulf Stream' — Gulf Stream is definitively warm (originates in Gulf of Mexico). That one wrong word makes the whole statement false. Statement 1 is textbook correct → (a)."
        },
        "concept_hooks": ["January isotherms ocean continent Northern Hemisphere", "Gulf Stream North Atlantic Drift warm current", "Ocean currents and isotherm deviation"]
    },
    "1873": {
        "question_type": "standard",
        "trap_pattern": "geographic_attribution",
        "trap_explanation": "UPSC tests the exact west-to-east sequence of Himalayan tributaries joining the Ganga after Prayagraj. The trap swaps Gomati and Ghaghara, and also shuffles Gandak-Kosi. Gomati joins first (near Ghazipur), then Ghaghara (Chhapra), Gandak (Hajipur), Kosi (Kursela).",
        "answer_justification": {
            "fact": "West-to-east sequence: Gomati (Ghazipur/UP) → Ghaghara (Chhapra/Bihar) → Gandak (Hajipur/Bihar) → Kosi (Kursela/Bihar) → option (b).",
            "hook": "Mnemonic: Go-Gha-Gan-Ko. Each river lies progressively east and north — Kosi is the easternmost, near the Nepal-Bihar border.",
            "elimination_path": "Eliminate (a): puts Ghaghara before Gomati — wrong. Eliminate (c) and (d): both place Kosi before Gandak — wrong (Gandak meets at Patna/Hajipur, Kosi much further east)."
        },
        "distractor_analysis": [
            {"option": "a", "verdict": "wrong", "reason": "Ghaghara before Gomati is reversed — Gomati joins at Ghazipur (west), Ghaghara at Chhapra (east of Ghazipur).", "confused_with": None},
            {"option": "c", "verdict": "wrong", "reason": "Kosi before Gandak is reversed — Gandak joins at Hajipur/Patna, Kosi joins further east at Kursela.", "confused_with": None},
            {"option": "d", "verdict": "wrong", "reason": "Both errors combined: Ghaghara before Gomati AND Kosi before Gandak — doubly wrong.", "confused_with": None}
        ],
        "concept_hooks": ["Ganga tributaries sequence west east Bihar", "Gomati Ghaghara Gandak Kosi confluence", "Himalayan rivers joining Ganga downstream"]
    },
    "1874": {
        "question_type": "matching",
        "trap_pattern": "geographic_attribution",
        "trap_explanation": "Two of three pairs have geographic errors. Pair 1 misidentifies Dhuandhar's region as Malwa (it's near Jabalpur/Bhedaghat, not the Malwa plateau). Pair 3 misidentifies Gersoppa's river as Netravati (it's the Sharavati). Only Hundru-Subarnarekha-Chota Nagpur is correct.",
        "pairs": [
            {"id": 1, "left": "Dhuandhar – Malwa – Narmada", "right": "Dhuandhar – Malwa – Narmada", "verdict": "wrong", "reason": "Dhuandhar falls are at Bhedaghat near Jabalpur (Mahakoshal/Satpura region), NOT Malwa plateau. River (Narmada) is correct; region is wrong."},
            {"id": 2, "left": "Hundru – Chota Nagpur – Subarnarekha", "right": "Hundru – Chota Nagpur – Subarnarekha", "verdict": "correct", "reason": "Hundru Falls on the Subarnarekha River near Ranchi, Jharkhand — in the Chota Nagpur plateau. All three elements correct."},
            {"id": 3, "left": "Gersoppa – Western Ghats – Netravati", "right": "Gersoppa – Western Ghats – Netravati", "verdict": "wrong", "reason": "Gersoppa (Jog Falls) is on the Sharavati River in Shimoga/Sagar district, Karnataka — NOT the Netravati. Region (Western Ghats) is correct; river is wrong."}
        ],
        "answer_justification": {
            "fact": "Only Pair 2 (Hundru-Subarnarekha-Chota Nagpur) is fully correct → option (a) Only one.",
            "elimination_path": "Confirm Pair 2 first (Hundru on Subarnarekha, Ranchi — unambiguous). Pair 1: region 'Malwa' is wrong (Jabalpur not Malwa). Pair 3: Gersoppa = Sharavati, not Netravati. Two wrong, one right → (a)."
        },
        "concept_hooks": ["Jog Falls Gersoppa Sharavati River Karnataka", "Dhuandhar Falls Narmada Bhedaghat Jabalpur", "Hundru Falls Subarnarekha Ranchi"]
    },
    "1993": {
        "question_type": "statement_eval",
        "trap_pattern": "first_or_only",
        "trap_explanation": "The question asks specifically about Greenfield airports — built on virgin land from scratch. Vijayawada airport is an existing airport that has been upgraded and expanded, NOT built as a Greenfield project. Donyi Polo (2022) and Kushinagar (2021) are the genuine Greenfield constructions.",
        "statements": [
            {"id": 1, "text": "Donyi Polo Airport", "verdict": "true", "reason": "Donyi Polo Airport, Itanagar — inaugurated November 2022. First airport in Arunachal Pradesh; built as a Greenfield project on previously undeveloped land."},
            {"id": 2, "text": "Kushinagar International Airport", "verdict": "true", "reason": "Kushinagar International Airport inaugurated October 2021 as a Greenfield project to serve Buddhist pilgrimage circuit in eastern UP."},
            {"id": 3, "text": "Vijayawada International Airport", "verdict": "false", "reason": "Vijayawada airport (Gannavaram) is an existing airport. It has received upgrades but was NOT constructed as a Greenfield project."}
        ],
        "answer_justification": {
            "fact": "Donyi Polo (Arunachal, 2022) and Kushinagar (UP, 2021) are confirmed Greenfield. Vijayawada is an upgraded legacy airport → option (a) 1 and 2 only.",
            "elimination_path": "Eliminate 3 (Vijayawada = Gannavaram, pre-existing airport). Confirm 1 (first airport of Arunachal Pradesh, entirely new). Confirm 2 (Buddhist circuit, new construction 2021) → (a)."
        },
        "concept_hooks": ["Donyi Polo Airport Arunachal Pradesh first airport", "Kushinagar International Airport Greenfield", "Greenfield airports India list"]
    },
    "2036": {
        "question_type": "standard",
        "trap_pattern": "geographic_attribution",
        "trap_explanation": "All four options are African countries — the trap exploits vague Africa-cocoa association without specificity. Algeria and Morocco are North African (Mediterranean), Botswana and Namibia are southern arid-belt. Cocoa is a humid tropical crop; the correct pair (Côte d'Ivoire + Ghana) lies in West Africa's equatorial zone.",
        "answer_justification": {
            "fact": "Côte d'Ivoire (~40%) and Ghana (~20%) together produce ~60% of world cocoa — first and second globally by volume.",
            "hook": "Both are on the Gulf of Guinea in West Africa — the world's cocoa belt. If one African option has two adjacent coastal West African countries, that's your answer.",
            "elimination_path": "Eliminate (a): Algeria + Morocco = North Africa, arid/Mediterranean — no cocoa. Eliminate (b): Botswana + Namibia = southern arid — no cocoa belt. Eliminate (d): Madagascar + Mozambique = East Africa, not major cocoa. Only (c) is West Africa's humid equatorial zone."
        },
        "distractor_analysis": [
            {"option": "a", "verdict": "wrong", "reason": "Algeria and Morocco are North African, semi-arid to arid. No significant cocoa cultivation — wrong climate zone entirely.", "confused_with": None},
            {"option": "b", "verdict": "wrong", "reason": "Botswana (landlocked, arid Kalahari) and Namibia (Namib Desert) — dry savanna/desert climates, unsuitable for cocoa.", "confused_with": None},
            {"option": "d", "verdict": "wrong", "reason": "Madagascar and Mozambique are East African — minor cocoa producers far behind Côte d'Ivoire and Ghana.", "confused_with": None}
        ],
        "concept_hooks": ["Côte d'Ivoire Ghana cocoa world production", "West Africa cocoa belt climate", "Top cocoa producing countries world"]
    },
    "2037": {
        "question_type": "matching",
        "trap_pattern": "geographic_attribution",
        "trap_explanation": "Pair 1 has two errors: Vosges is in Europe (France-Germany border), not Central Asia, and it's a block/horst mountain not a fold mountain. Pair 2 inverts Alps and block: Alps are young fold mountains, not block. Pairs 3 and 4 are correct.",
        "pairs": [
            {"id": 1, "left": "Central Asia – Vosges – Fold mountain", "right": "Central Asia – Vosges – Fold mountain", "verdict": "wrong", "reason": "Vosges are in northeast France (Alsace), NOT Central Asia. And they are block/horst mountains (fault-bounded), not fold mountains — double error."},
            {"id": 2, "left": "Europe – Alps – Block mountain", "right": "Europe – Alps – Block mountain", "verdict": "wrong", "reason": "Alps are in Europe (correct region) but are classic young FOLD mountains formed by Alpine orogeny — not block mountains. Type is wrong."},
            {"id": 3, "left": "North America – Appalachians – Fold mountain", "right": "North America – Appalachians – Fold mountain", "verdict": "correct", "reason": "Appalachians are old fold mountains in eastern North America — correct on all three: region, name, type."},
            {"id": 4, "left": "South America – Andes – Fold mountain", "right": "South America – Andes – Fold mountain", "verdict": "correct", "reason": "Andes are young fold mountains along western South America, formed by subduction of Nazca Plate — correct on all three."}
        ],
        "answer_justification": {
            "fact": "Pairs 3 (Appalachians, old fold) and 4 (Andes, young fold) correct; pairs 1 and 2 wrong → option (b) Only two.",
            "elimination_path": "Pair 1: 'Central Asia' is wrong (Vosges = France). Pair 2: 'Block mountain' is wrong (Alps = young fold). Pairs 3 and 4 are textbook correct. Two correct → (b)."
        },
        "concept_hooks": ["Vosges mountains block horst France", "Alps fold mountains Alpine orogeny", "Mountain types fold block volcanic UPSC"]
    },
    "2074": {
        "question_type": "statement_eval",
        "trap_pattern": "geographic_attribution",
        "trap_explanation": "Finland borders the Gulf of Bothnia and Baltic Sea — not the North Sea. Russia's western coasts touch the Baltic Sea and Barents Sea — the North Sea border stops at Norway. Only Germany and Norway (of the four listed) actually border the North Sea, making the answer 'Only two'.",
        "statements": [
            {"id": 1, "text": "Finland", "verdict": "false", "reason": "Finland's coastline is on the Gulf of Bothnia and Baltic Sea. It has no border with the North Sea — separated by Norway and Sweden."},
            {"id": 2, "text": "Germany", "verdict": "true", "reason": "Germany has a North Sea coastline in the states of Schleswig-Holstein and Lower Saxony — confirmed North Sea border."},
            {"id": 3, "text": "Norway", "verdict": "true", "reason": "Norway's entire western coastline faces the North Sea — one of its primary maritime boundaries."},
            {"id": 4, "text": "Russia", "verdict": "false", "reason": "Russia borders the Barents Sea (north), Baltic Sea (Kaliningrad enclave) — not the North Sea. The North Sea does not reach Russian territory."}
        ],
        "answer_justification": {
            "fact": "Only Germany and Norway (of the four) border the North Sea → option (b) Only two.",
            "elimination_path": "Eliminate Finland (Baltic/Gulf of Bothnia). Eliminate Russia (Barents Sea/Baltic — not North Sea). Germany and Norway confirmed. Two countries → (b)."
        },
        "concept_hooks": ["North Sea bordering countries Europe", "Finland coastline Baltic vs North Sea", "Russia Baltic Barents Sea coastlines"]
    },
    "2075": {
        "question_type": "standard",
        "trap_pattern": "famous_association_bias",
        "trap_explanation": "Russia-Kazakhstan or China-India feel long because they conjure vast continental imagery. The Canada-USA border (~8,891 km including the Alaska segment) is the world's longest, but test-takers associate 'big borders' with Russia's land mass or the China-India dispute. The answer is counterintuitively the North American pair.",
        "answer_justification": {
            "fact": "Canada-USA border is ~8,891 km (including Alaska-Canada boundary) — the longest international border between any two countries.",
            "hook": "Russia-Kazakhstan is second (~7,644 km). Canada-USA beats it because the Alaska boundary adds ~2,475 km of separate US-Canada border segment.",
            "elimination_path": "Eliminate (c) China-India (~3,488 km, disputed). Eliminate (b) Chile-Argentina (~5,308 km). Eliminate (d) Kazakhstan-Russia (~7,644 km — second longest). Only (a) Canada-USA at ~8,891 km wins."
        },
        "distractor_analysis": [
            {"option": "b", "verdict": "wrong", "reason": "Chile-Argentina border ~5,308 km (Andes spine) — long but well below Canada-USA.", "confused_with": None},
            {"option": "c", "verdict": "wrong", "reason": "China-India border ~3,488 km (disputed LAC) — not even close to the longest.", "confused_with": None},
            {"option": "d", "verdict": "wrong", "reason": "Kazakhstan-Russia border ~7,644 km — second longest globally, but Canada-USA (~8,891 km) exceeds it.", "confused_with": "Russia-Kazakhstan as world's longest (common misconception)"}
        ],
        "concept_hooks": ["Canada USA international border length Alaska", "Longest international borders world ranking", "Russia Kazakhstan border length comparison"]
    },
    "2076": {
        "question_type": "statement_eval",
        "trap_pattern": "statement_subtle_inversion",
        "trap_explanation": "Both statements are correct and less intuitively obvious. Students may doubt statement 2 (expecting some river to drain into the Red Sea) or statement 1 (assuming surrounding countries have some rainfall). The Red Sea is flanked by the Arabian and Saharan deserts — almost no rain, and no major river drains into it.",
        "statements": [
            {"id": 1, "text": "The Red Sea receives very little precipitation in any form.", "verdict": "true", "reason": "Red Sea is surrounded by hyper-arid regions (Arabian Desert, Sahara). Annual rainfall over the Red Sea is extremely low — among lowest globally for any sea body."},
            {"id": 2, "text": "No water enters the Red Sea from rivers.", "verdict": "true", "reason": "No major river drains into the Red Sea. The Nile drains to Mediterranean; Arabian Peninsula rivers are ephemeral wadis that don't reach the Red Sea consistently. No freshwater dilution occurs."}
        ],
        "answer_justification": {
            "fact": "Both true: minimal precipitation AND no river inflow → high evaporation produces ~40 psu salinity. Option (c) Both 1 and 2.",
            "elimination_path": "Statement 1: Red Sea = surrounded by desert — minimal rain (true). Statement 2: Nile drains to Mediterranean; no perennial river reaches Red Sea (true). Both confirmed → (c)."
        },
        "concept_hooks": ["Red Sea salinity high evaporation no rivers", "Red Sea geography hydrology", "Arabian Desert Sahara Red Sea climate"]
    },
}


# Merge Wave 2 overlay (49 cards drafted by Sonnet, written to scratch JSON for sanity).
_WAVE2_PATH = ROOT / ".scratch" / "drill_2024" / "wave2_cards.json"
if _WAVE2_PATH.exists():
    DISCRIMINATION_CARDS.update(json.loads(_WAVE2_PATH.read_text()))


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

    pyqs = load_2024_pyqs()
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
