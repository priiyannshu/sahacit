#!/usr/bin/env python3
"""
Generate app/pwa/data/drill_clusters_2018.json
       + app/pwa/data/discrimination_cards_2018.json

Cluster map covers all 100 GS1 2018 PYQs. Sonnet drafted 35 clusters in-conv
(no singletons, sizes 2-6). Opus consolidation: kept all 35 — within band,
all clusters topically coherent. No merges, no retags.

Discrimination cards drafted by Sonnet in-conv (v2.1 — no sub-agents); auto-
overlay loader picks up wave1*.json + wave2*.json from .scratch/drill_2018/.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "pwa" / "data" / "pyq_index.json"
OUT_CLUSTERS = ROOT / "pwa" / "data" / "drill_clusters_2018.json"
OUT_CARDS = ROOT / "pwa" / "data" / "discrimination_cards_2018.json"

YEAR = 2018

# Cluster definitions for all 100 2018 PYQs.
# Format: (cluster_id, title, subject_focus, study_keywords[], common_traps[], pyq_ids[])
CLUSTERS: list = [
    # --- Art and Culture (4 PYQs, 2 clusters) ---
    ("art_regional_festivals_crafts", "Art & Culture: Regional Festivals, Traditions & Textile Crafts — Chapchar Kut, Thang-Ta, Puthukkuli, Uppada Jamdani", "Art and Culture",
     ["Chapchar Kut festival Mizoram bamboo dance spring harvest",
      "Khongjom Parba ballad Manipur battle folk song",
      "Thang-Ta martial dance Manipur not Sikkim",
      "Puthukkuli shawls Tamil Nadu Nilgiri handloom",
      "Sujni embroidery Bihar not Maharashtra applique quilting",
      "Uppada Jamdani saris Andhra Pradesh not Karnataka"],
     ["geographic_attribution"],
     [4, 7]),
    ("art_music_painting_architecture", "Art & Culture: Carnatic Composers (Tyagaraja/Annamacharya), Miniature Painting Schools (Bani Thani/Kishangarh), Mughal Architecture (Fatehpur Sikri/Lucknow)", "Art and Culture",
     ["Tyagaraja kritis devoted to Rama not Krishna new ragas creation",
      "Annamacharya kirtanas Venkateshwara Tirupati 15th century not contemporary Tyagaraja",
      "Bani Thani painting Kishangarh school Rajasthan Radha-like figure",
      "Miniature painting schools Bundi Jaipur Kangra Kishangarh distinction",
      "Buland Darwaza Khankah Fatehpur Sikri red sandstone not white marble",
      "Bara Imambara Rumi Darwaza Lucknow lime mortar brick not red sandstone marble"],
     ["statement_subtle_inversion", "famous_association_bias"],
     [5, 6, 328]),

    # --- Ancient Indian History (3 PYQs, 1 cluster) ---
    ("anc_religion_travellers", "Ancient/Medieval India: Foreign Travellers (Tavernier/diamonds), Jainism (Sthanakvasi sect), Buddhism (Maitreya future Buddha)", "Ancient Indian History",
     ["Jean-Baptiste Tavernier diamonds mines India French traveller Mughal",
      "Francois Bernier Mughal Empire description medical observations",
      "Sthanakvasi sect Jainism Sthanak worship without idol temple",
      "Maitreya future Buddha Bodhisattva yet to come save world",
      "Avalokiteshvara Padmapani Lokesvara present Bodhisattva compassion"],
     ["famous_association_bias", "overlapping_categories", "distractor_by_topic_association"],
     [184, 216, 217]),

    # --- Modern Indian History (13 PYQs, 5 clusters) ---
    ("mod_colonial_economy_company", "Modern India: EIC Bengal Exports (mid-18th c), Subsidiary Alliance (Wellesley), British Economic Impact (commercialisation of agriculture)", "Modern Indian History",
     ["East India Company Bengal exports cotton silk saltpetre opium mid-18th century",
      "Subsidiary Alliance Lord Wellesley objectives standing army paramountcy not fixed income",
      "British rule India 19th century commercialisation of agriculture indigo jute cotton",
      "de-industrialisation handicrafts decline British economic impact"],
     ["distractor_by_topic_association", "negation_trap"],
     [357, 358, 403]),
    ("mod_gandhian_movements", "Modern India: Champaran Satyagraha (significance) & All India Home Rule League → Swarajya Sabha (1920)", "Modern Indian History",
     ["Champaran Satyagraha 1917 peasant unrest national movement indigo farmers Bihar",
      "All India Home Rule League renamed Swarajya Sabha 1920 Annie Besant Tilak",
      "Swaraj Party Motilal Nehru CR Das distinction from Swarajya Sabha"],
     ["famous_association_bias", "distractor_by_topic_association"],
     [465, 466]),
    ("mod_constitutional_acts_administration", "Modern India: GoI Act 1935 (residuary powers to Governor General) & Post-Santhal Rising Measures (Santhal Paraganas + land transfer restriction)", "Modern Indian History",
     ["Government of India Act 1935 residuary powers Governor General not Federal Legislature",
      "Federal structure GoI 1935 center-state division different from modern Indian constitution",
      "Santhal rising 1855-56 aftermath Santhal Paraganas created land transfer restriction non-Santhal"],
     ["famous_association_bias", "statement_partial_truth"],
     [537, 662]),
    ("mod_leaders_literature", "Modern India: Hind Mazdoor Sabha founders (1948), Lala Lajpat Rai (biographies), Earliest event chronology (Neeldarpan/Arya Samaj/Anandmath)", "Modern Indian History",
     ["Hind Mazdoor Sabha 1948 founders Ashok Mehta T.S Ramanujan G.G Mehta socialists",
      "Lala Lajpat Rai biographies Mazzini Garibaldi Shivaji America Central Assembly",
      "Neeldarpan 1858 Dinabandhu Mitra indigo play earliest before Arya Samaj 1875",
      "Satyendranath Tagore first Indian ICS 1863 chronological order"],
     ["person_attribution", "period_attribution"],
     [557, 620, 621]),
    ("mod_education_colonial", "Modern India: Wood's Dispatch (Grants-in-Aid, universities), Introduction of English Education (Charter 1813 + GCPI + Controversy), Colonial Educational Institutions & Founders", "Modern Indian History",
     ["Wood's Dispatch 1854 Grants-in-Aid universities English not all levels vernacular lower",
      "Charter Act 1813 English education General Committee of Public Instruction 1823",
      "Orientalist Anglicist controversy Macaulay's minute 1835 English medium decision",
      "Calcutta Madrasa Warren Hastings 1780 Fort William College Richard Wellesley not Arthur",
      "Sanskrit College Benares Jonathan Duncan not William Jones"],
     ["statement_subtle_inversion", "person_attribution"],
     [652, 653, 654]),

    # --- Indian Polity (16 PYQs, 7 clusters) ---
    ("pol_political_theory", "Polity: Law-Liberty Relationship (no laws = no liberty) & Rule of Law Features (limitations/equality/civil rights, NOT people's responsibility to govt)", "Indian Polity",
     ["law liberty relationship Hobbesian Lockean social contract no laws no liberty",
      "Rule of Law features Dicey limitations of powers equality before law civil rights",
      "people's responsibility to government NOT a Rule of Law feature inverted"],
     ["technical_vs_common_meaning", "statement_subtle_inversion"],
     [676, 677]),
    ("pol_constitution_schedules", "Polity: Ninth Schedule (Parliament can add laws; post-1973 laws judicially reviewable — IR Coelho 2007) & Article 356 President's Rule (legislature powers to Parliament)", "Indian Polity",
     ["Ninth Schedule Parliament can place laws first amendment 1951 Nehru",
      "IR Coelho case 2007 Supreme Court Ninth Schedule laws post-1973 reviewable not absolute",
      "Article 356 President's Rule state legislature powers exercised by Parliament not President directly",
      "Article 356 state assembly suspended not automatically dissolved"],
     ["statement_subtle_inversion", "technical_vs_common_meaning"],
     [719, 720]),
    ("pol_fundamental_rights", "Polity: RTE Act (TET under NCTE not state council; private institutions majority) & Right to Privacy (Article 21 + Part III, not Article 14/17/24)", "Indian Polity",
     ["RTE Act teacher qualification NCTE guidelines TET Teacher Eligibility Test",
      "teacher education institutions India majority private not state government",
      "Right to Privacy Article 21 personal liberty Part III fundamental rights",
      "Puttaswamy judgement 2017 privacy intrinsic part Article 21"],
     ["statement_subtle_inversion", "overlapping_categories"],
     [758, 759]),
    ("pol_president_governor", "Polity: President Election (MLA vote value varies by state; MP vote equal across houses) & Governor Privileges (Article 361 immunity + emoluments protection)", "Indian Polity",
     ["President election MLA vote value varies state population Lok Sabha Rajya Sabha equal",
      "Article 361 Governor immunity criminal proceedings during tenure",
      "Governor emoluments allowances not diminished during office term"],
     ["statement_subtle_inversion", "statement_partial_truth"],
     [830, 831]),
    ("pol_legislature_parliament", "Polity: Money Bill (Contingency Fund NOT included), Leader of Opposition (first recognised 1969; threshold rules), Subordinate Legislation Committee, Speaker continues after dissolution", "Indian Polity",
     ["Money Bill definition Article 110 Consolidated Fund not Contingency Fund appropriation",
      "Leader of Opposition first recognised Lok Sabha 1969 not first Lok Sabha",
      "Swatantra Party CPI first Lok Sabha opposition largest party",
      "Committee on Subordinate Legislation delegated legislation scrutiny",
      "Speaker Legislative Assembly continues after dissolution until new Assembly first sitting"],
     ["negation_trap", "statement_subtle_inversion", "distractor_by_topic_association"],
     [863, 864, 865, 866]),
    ("pol_international_relations", "Polity: IAEA Additional Protocol (civilian reactors under safeguards, not military) & ASEAN Free Trade Partners (Australia/China/India/Japan; NOT Canada/USA)", "Indian Polity",
     ["IAEA Additional Protocol civilian nuclear reactors safeguards not military installations",
      "India IAEA Additional Protocol 123 Agreement NSG waiver distinction",
      "ASEAN free trade agreements Australia China India Japan not Canada USA",
      "ASEAN FTA partner countries RCEP AIFTA"],
     ["overlapping_categories", "famous_association_bias"],
     [1011, 1012]),
    ("pol_acts_amendments_postind", "Polity: Aadhaar (not citizenship proof; UIDAI can deactivate) & Post-Independence Chronology (Air India 1953 → SBI 1955 → Kerala communist 1957 → Goa 1961)", "Indian Polity",
     ["Aadhaar card not proof of citizenship domicile residency identity only",
      "UIDAI can deactivate Aadhaar not permanent irrevocable",
      "Air India nationalisation 1953 Imperial Bank SBI 1955 Kerala communist govt 1957 Goa 1961",
      "post-independence chronological sequence events India"],
     ["statement_subtle_inversion", "period_attribution"],
     [1038, 1055]),

    # --- Indian Economy (25 PYQs, 7 clusters) ---
    ("eco_macro_fundamentals", "Economy: Macro Fundamentals — Legal Tender (compulsory acceptance), Opportunity Cost (transferred to taxpayers), GNP != Development (poverty/unemployment), High Capital-Output Ratio", "Indian Economy",
     ["legal tender money compulsory acceptance creditor obligated not cheques not metallic only",
      "opportunity cost free government commodity transferred from consumers to taxpayers",
      "economic development vs growth GNP increase poverty unemployment can coexist",
      "capital-output ratio ICOR high ratio means inefficient capital use output not rising"],
     ["technical_vs_common_meaning"],
     [1101, 1102, 1103, 1104]),
    ("eco_fiscal_taxation", "Economy: FRBM Debt Ratios (60% total; 1 and 3 correct), Equalisation Tax 6% (not Income Tax Act; DTAA doesn't cover it), GST Exemptions (cereal/newspaper yes; canned fish no)", "Indian Economy",
     ["FRBM review committee 60% debt GDP 40% central 20% state 2023 target",
      "Article 293 state borrowing central government consent outstanding liabilities",
      "equalisation levy 6% online ads Finance Act not Income Tax Act DTAA excluded",
      "GST exempt cereal grains hulled newspapers fresh eggs not processed canned fish"],
     ["statement_subtle_inversion", "technical_vs_common_meaning"],
     [1146, 1181, 1182]),
    ("eco_banking_capital_markets", "Economy: NPCI links ATMs (NFS), Capital Adequacy Ratio (RBI sets not individual banks), BHIM UPI, Merchant Discount Rate (fee charged TO merchants), PSB mergers, T-Bills (RBI also manages state securities)", "Indian Economy",
     ["NPCI National Payments Corporation India NFS National Financial Switch ATM interoperability",
      "Capital Adequacy Ratio CAR Basel norms RBI sets not individual banks",
      "BHIM app UPI transfer UPI-enabled account authentication factors",
      "Merchant Discount Rate MDR fee charged to merchant by bank not incentive to merchant",
      "SBI associate banks merger 2017 capital infusion PSB recapitalisation",
      "Treasury bills Central Government only no state T-bills RBI manages both central state securities"],
     ["overlapping_categories", "technical_vs_common_meaning", "statement_subtle_inversion"],
     [1285, 1286, 1287, 1288, 1289, 1348]),
    ("eco_industries_resources", "Economy: Solar Power (India not world's largest silicon wafer maker; tariffs by competitive bidding), Mines (States can auction non-coal; AP/Jharkhand have gold; Rajasthan has iron ore), FSSAI (replaced PFA Act 1954; not under DGHS directly)", "Indian Economy",
     ["silicon wafer manufacture China dominates India imports solar photovoltaic",
      "solar tariff competitive bidding SECI facilitates not sets tariffs CERC",
      "MMDR Act state government mining leases non-coal major minerals",
      "Andhra Pradesh Jonnagiri gold mine Jharkhand gold deposits",
      "Rajasthan iron ore mines Bhilwara",
      "FSSAI Food Safety Standards Authority replaced Prevention Food Adulteration Act 1954",
      "FSSAI autonomous body Ministry Health Family Welfare not under DGHS"],
     ["statement_subtle_inversion"],
     [1384, 1385, 1633]),
    ("eco_trade_international_orgs", "Economy: Edible Oil (imports > domestic; customs duty exists), GI Act 1999 → WTO/TRIPS obligation, ILO Conventions 138 & 182 → child labour", "Indian Economy",
     ["edible oil India imports exceed domestic production palm oil Indonesia Malaysia",
      "customs duty edible oils reduced not eliminated special case",
      "Geographical Indications GI Act 1999 WTO TRIPS Agreement compliance not ILO IMF",
      "ILO Convention 138 minimum age employment Convention 182 worst forms child labour"],
     ["statement_subtle_inversion", "overlapping_categories", "distractor_by_topic_association"],
     [1435, 1461, 1462]),
    ("eco_welfare_human_dev", "Economy: Human Capital (knowledge/skills = intangible wealth), NFSA 2013 (not only BPL; eldest woman head; 600 cal not 1600), PMKVY (Skill Ministry not Labour; soft skills + NSQF)", "Indian Economy",
     ["human capital formation knowledge skills intangible wealth not physical tangible capital",
      "National Food Security Act 2013 priority households not just BPL coverage",
      "NFSA eldest woman 18+ head of household ration card issuance",
      "NFSA pregnant lactating mothers 600 calories take-home ration not 1600",
      "PMKVY Pradhan Mantri Kaushal Vikas Yojana Ministry Skill Development Entrepreneurship not Labour",
      "NSQF National Skill Qualification Framework unregulated workforce alignment"],
     ["technical_vs_common_meaning", "statement_subtle_inversion"],
     [1486, 1534, 1574]),
    ("eco_agriculture_land", "Economy: Agricultural Households NSSO 70th Round (Rajasthan highest share; Kerala 60%+ non-farm income), Conservation Agriculture (minimum tillage + residue cover + rotation), MSP Crops (barley/millets/groundnut/sesamum; NOT areca nut/coffee/turmeric)", "Indian Economy",
     ["NSSO 70th round agricultural households Rajasthan highest share Kerala non-farm income OBC share",
      "Conservation Agriculture three principles minimum tillage crop residue soil cover rotation",
      "MSP Minimum Support Price CCEA kharif rabi crops barley finger millet groundnut sesamum",
      "areca nut coffee turmeric NOT under CCEA MSP plantation crops spices"],
     ["numerical_proximity", "distractor_by_topic_association", "overlapping_categories"],
     [1601, 1602, 1603]),

    # --- Geography (7 PYQs, 3 clusters) ---
    ("geo_india_physical", "Geography: Sand Mining Effects (groundwater pollution + water table lowering; NOT salinity decrease), Barren Island Volcano (active; not near Great Nicobar; recent eruptions), Agriculture Soils (organic matter increases WHC; soil crucial to sulphur cycle; irrigation → salinization)", "Geography",
     ["sand mining rivers groundwater pollution water table lowering salinity increase not decrease",
      "Barren Island active volcano Andaman not near Great Nicobar Port Blair northeast",
      "Barren Island volcano eruptions 2017 2018 2019 active not dormant since 1991",
      "soil organic matter water holding capacity increases not decreases",
      "sulphur cycle soil microorganisms crucial not bypassed",
      "irrigation salinization waterlogging evaporation salt accumulation agricultural land"],
     ["statement_subtle_inversion"],
     [1685, 1828, 1960]),
    ("geo_india_map", "Geography: Delhi Longitude (77E — Bengaluru closest, not Hyderabad/Nagpur) & Artificial vs Natural Lakes (Kodaikanal artificial; Kolleru/Nainital/Renuka natural)", "Geography",
     ["Delhi longitude 77 degrees East Bengaluru 77.6E closest not Hyderabad 78.5E Nagpur 79E",
      "Kodaikanal Tamil Nadu artificial lake British constructed 1863",
      "Kolleru Andhra Pradesh natural lake Nainital glacial Renuka natural Himachal Pradesh"],
     ["geographic_attribution", "distractor_by_topic_association"],
     [1807, 1885]),
    ("geo_world_regions", "Geography: World Regions in News — Catalonia/Spain, Mindanao/Philippines correct; Crimea=Ukraine not Hungary; Oromia=Ethiopia not Nigeria — AND Aral Sea dried up (Black Sea/Baikal not)", "Geography",
     ["Catalonia Spain independence movement separatism",
      "Crimea Ukraine Russia annexation 2014 not Hungary",
      "Mindanao Philippines Moro insurgency conflict",
      "Oromia Ethiopia Oromo people largest region not Nigeria",
      "Aral Sea Central Asia shrunk dried up irrigation diversion human activity",
      "Black Sea Lake Baikal not shrunk significantly"],
     ["geographic_attribution", "distractor_by_topic_association"],
     [2043, 2081]),

    # --- Environment (12 PYQs, 5 clusters) ---
    ("env_ecology_biodiversity", "Environment: Desert Leaf Modifications (hard/waxy + tiny + thorns — all three), Coral Reefs (tropical + Australia/Indonesia/Philippines + more phyla than rainforests — all true), Prosopis juliflora (invasive = biodiversity reducer)", "Environment",
     ["desert plants leaf modifications waxy cuticle tiny leaves thorns xerophyte adaptations",
      "coral reefs tropical waters Coral Triangle Australia Indonesia Philippines",
      "coral reefs animal phyla diversity more than tropical rainforests",
      "Prosopis juliflora invasive species biodiversity threat arid India"],
     ["statement_partial_truth", "distractor_by_topic_association"],
     [2136, 2181, 2182]),
    ("env_climate_threats", "Environment: Carbon Fertilization (CO2 → plant growth, not temperature rise) & Sixth Mass Extinction (human overexploitation/habitat loss — NOT meteorite fear)", "Environment",
     ["carbon fertilization increased CO2 concentration plant growth photosynthesis not temperature",
      "sixth mass extinction anthropogenic human overexploitation habitat fragmentation pollution climate",
      "fifth mass extinction Cretaceous meteorite 65 million years ago dinosaurs",
      "biodiversity loss current rate compared to geological past"],
     ["technical_vs_common_meaning", "famous_association_bias"],
     [2301, 2302]),
    ("env_conservation_governance", "Environment: NGT vs CPCB (NGT by NGT Act; CPCB by Water Act 1974 — both Acts), Pakhui Wildlife Sanctuary (Arunachal Pradesh), Forest Rights Act (Critical Wildlife Habitat; Baiga Habitat Rights; state/community role not MoEFCC alone)", "Environment",
     ["National Green Tribunal NGT Act 2010 judicial body not executive order",
      "Central Pollution Control Board CPCB Water Prevention Control Pollution Act 1974 statutory",
      "Pakhui Pakke Wildlife Sanctuary Arunachal Pradesh tiger reserve not Manipur Nagaland",
      "Forest Rights Act 2006 Critical Wildlife Habitat definition schedule",
      "Baiga tribe habitat rights Madhya Pradesh first PVTG habitat rights India",
      "PVTG habitat rights State government gram sabha not MoEFCC unilateral declaration"],
     ["statement_subtle_inversion", "geographic_attribution"],
     [2263, 2332, 2333]),
    ("env_global_initiatives", "Environment: 'Momentum for Change: Climate Neutral Now' (UNFCCC Secretariat, not IPCC/UNEP/WMO) & PAGE (Rio 2012 — not Paris 2015 or Johannesburg 2002)", "Environment",
     ["Momentum for Change Climate Neutral Now UNFCCC Secretariat initiative",
      "IPCC UNEP UNFCCC WMO distinction climate bodies roles",
      "Partnership for Action Green Economy PAGE UNEP Rio 2012 UNCSD not Paris 2015",
      "green economy inclusive economy transition UN mechanism"],
     ["overlapping_categories", "period_attribution"],
     [2391, 2392]),
    ("env_agriculture_organic", "Environment: GACSA (launched NY 2014 not Paris 2015; voluntary; India not instrumental) & Organic Farming NPOP (APEDA/Commerce Ministry, not Rural Development; Sikkim first organic state)", "Environment",
     ["GACSA Global Alliance Climate Smart Agriculture UN Summit New York September 2014 not Paris",
      "GACSA voluntary platform no binding obligations",
      "NPOP National Programme Organic Production Ministry Commerce Industry APEDA secretariat",
      "Sikkim fully organic state 2016 India first"],
     ["statement_subtle_inversion"],
     [2429, 2430]),

    # --- Science and Technology (13 PYQs, 3 clusters) ---
    ("sci_digital_it_applications", "S&T: Digital/IT — Ransomware (WannaCry/Petya), Tech Domain Matching (Belle II=particle physics; CRISPR=gene editing), Aadhaar APIs (biometric auth including iris), Digital India (only village internet/WiFi is stated aim), IoT scenario, 3D Printing (all applications including data processing)", "Science and Technology",
     ["WannaCry Petya EternalBlue ransomware cyber attack not cryptocurrency exoplanet",
      "Belle II experiment KEK Japan particle physics B-meson not AI",
      "CRISPR-Cas9 gene editing molecular scissors not particle physics",
      "Aadhaar open API biometric authentication iris fingerprint integration",
      "Digital India BharatNet village internet WiFi schools not clone Chinese internet companies",
      "Internet of Things IoT connected devices smart home automation",
      "3D printing additive manufacturing food automotive surgery data processing applications"],
     ["statement_subtle_inversion", "distractor_by_topic_association", "technical_vs_common_meaning"],
     [2484, 2485, 2486, 2487, 2488, 2489]),
    ("sci_space_astrophysics", "S&T: Space — GPS (all: mobile/banking/power grids), Earth History (early atmosphere near-zero O2 not 54%), IRNSS/NavIC (3 GEO + 4 GSO; regional not global), General Relativity (light+expansion+spacetime — all three), PSLV/GSLV (PSLV = polar not geostationary; GSLV Mk III staging description wrong)", "Science and Technology",
     ["GPS applications mobile banking time-stamping power grid synchronisation all three",
      "early Earth atmosphere nitrogen CO2 methane near-zero oxygen Great Oxidation Event 2.4 billion",
      "IRNSS NavIC 3 geostationary 4 geosynchronous satellites regional coverage not global",
      "General Theory of Relativity gravitational lensing expanding universe spacetime curvature",
      "PSLV polar sun-synchronous orbit not geostationary GSLV communication satellites",
      "GSLV Mk III three stage S200 L110 C25 cryogenic not four stage"],
     ["statement_partial_truth", "statement_subtle_inversion"],
     [2516, 2517, 2518, 2519, 2520]),
    ("sci_biotech_biology", "S&T: GM Mustard DMH-11 (barnase/barstar = hybridisation not pest resistance; Delhi University not IARI+PAU) & Plant Disease Vectors (birds + dust + rain + wind — all four)", "Science and Technology",
     ["GM Mustard DMH-11 barnase barstar bar genes hybridisation male sterility Delhi University",
      "GM Mustard not pest resistance genes Bacillus amyloliquefaciens hybridisation not Bt",
      "plant disease spread vectors birds dust wind rain splash dispersal spores all"],
     ["statement_subtle_inversion", "statement_partial_truth"],
     [2594, 2664]),

    # --- Current Affairs and GK (6 PYQs, 2 clusters) ---
    ("ca_defence_nuclear", "Current Affairs: THAAD (American anti-missile system, not Israeli/Indian) & NSG Membership (access to nuclear tech ✓; does NOT auto-confer NPT membership ✗)", "Current Affairs and GK",
     ["THAAD Terminal High Altitude Area Defence US Army anti-ballistic missile not Israel India",
      "Iron Dome David's Sling Israeli missile defence distinction from THAAD",
      "NSG Nuclear Suppliers Group membership benefits technology access",
      "NSG membership not automatic NPT Treaty Non-Proliferation membership separate regimes"],
     ["geographic_attribution", "statement_subtle_inversion"],
     [2708, 2726]),
    ("ca_international_governance", "Current Affairs: Rule of Law Index (World Justice Project), Yemen & South Sudan famine 2017-18, Two-State Solution = Israel-Palestine, Town-Country pairs (Kirkuk=Iraq not Yemen; Mosul=Iraq not Palestine)", "Current Affairs and GK",
     ["Rule of Law Index World Justice Project WJP not Amnesty International not ICJ",
      "Yemen South Sudan famine starvation war conflict 2017-18",
      "two state solution Israel Palestine not China not Iraq",
      "Aleppo Syria Kirkuk Iraq not Yemen Mosul Iraq not Palestine Mazar-i-Sharif Afghanistan"],
     ["distractor_by_topic_association", "geographic_attribution"],
     [2751, 2809, 2810, 2811]),
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
# QC notes: All-true-answer cases (653, 662, 831, 2136, 2181, 2486, 2489, 2516,
# 2519, 2664) correctly tagged as statement_partial_truth — the 2428 (2020)
# lesson held. Negation traps (358, 863) correctly identified by NOT framing.
# Borderlines noted by Sonnet (403, 466, 1182): kept as drafted; tags are
# defensible. No retags applied.
TRAP_TAGS: dict = {
    "4": "geographic_attribution",
    "5": "famous_association_bias",
    "6": "statement_subtle_inversion",
    "7": "geographic_attribution",
    "184": "famous_association_bias",
    "216": "overlapping_categories",
    "217": "distractor_by_topic_association",
    "328": "statement_subtle_inversion",
    "357": "distractor_by_topic_association",
    "358": "negation_trap",
    "403": "distractor_by_topic_association",
    "465": "famous_association_bias",
    "466": "distractor_by_topic_association",
    "537": "famous_association_bias",
    "557": "person_attribution",
    "620": "person_attribution",
    "621": "period_attribution",
    "652": "statement_subtle_inversion",
    "653": "statement_partial_truth",
    "654": "person_attribution",
    "662": "statement_partial_truth",
    "676": "technical_vs_common_meaning",
    "677": "statement_subtle_inversion",
    "719": "statement_subtle_inversion",
    "720": "technical_vs_common_meaning",
    "758": "statement_subtle_inversion",
    "759": "overlapping_categories",
    "830": "statement_subtle_inversion",
    "831": "statement_partial_truth",
    "863": "negation_trap",
    "864": "statement_subtle_inversion",
    "865": "distractor_by_topic_association",
    "866": "statement_subtle_inversion",
    "1011": "overlapping_categories",
    "1012": "famous_association_bias",
    "1038": "statement_subtle_inversion",
    "1055": "period_attribution",
    "1101": "technical_vs_common_meaning",
    "1102": "technical_vs_common_meaning",
    "1103": "technical_vs_common_meaning",
    "1104": "technical_vs_common_meaning",
    "1146": "statement_subtle_inversion",
    "1181": "statement_subtle_inversion",
    "1182": "technical_vs_common_meaning",
    "1285": "overlapping_categories",
    "1286": "statement_subtle_inversion",
    "1287": "statement_subtle_inversion",
    "1288": "technical_vs_common_meaning",
    "1289": "statement_overgeneralization",
    "1348": "statement_subtle_inversion",
    "1384": "statement_subtle_inversion",
    "1385": "statement_subtle_inversion",
    "1435": "statement_subtle_inversion",
    "1461": "overlapping_categories",
    "1462": "distractor_by_topic_association",
    "1486": "technical_vs_common_meaning",
    "1534": "statement_subtle_inversion",
    "1574": "statement_subtle_inversion",
    "1601": "numerical_proximity",
    "1602": "distractor_by_topic_association",
    "1603": "overlapping_categories",
    "1633": "statement_subtle_inversion",
    "1685": "statement_subtle_inversion",
    "1807": "geographic_attribution",
    "1828": "statement_subtle_inversion",
    "1885": "distractor_by_topic_association",
    "1960": "statement_subtle_inversion",
    "2043": "geographic_attribution",
    "2081": "distractor_by_topic_association",
    "2136": "statement_partial_truth",
    "2181": "statement_partial_truth",
    "2182": "distractor_by_topic_association",
    "2263": "statement_subtle_inversion",
    "2301": "technical_vs_common_meaning",
    "2302": "famous_association_bias",
    "2332": "geographic_attribution",
    "2333": "statement_subtle_inversion",
    "2391": "overlapping_categories",
    "2392": "period_attribution",
    "2429": "statement_subtle_inversion",
    "2430": "statement_subtle_inversion",
    "2484": "distractor_by_topic_association",
    "2485": "statement_subtle_inversion",
    "2486": "statement_partial_truth",
    "2487": "statement_subtle_inversion",
    "2488": "technical_vs_common_meaning",
    "2489": "statement_partial_truth",
    "2516": "statement_partial_truth",
    "2517": "statement_subtle_inversion",
    "2518": "statement_subtle_inversion",
    "2519": "statement_partial_truth",
    "2520": "statement_subtle_inversion",
    "2594": "statement_subtle_inversion",
    "2664": "statement_partial_truth",
    "2708": "geographic_attribution",
    "2726": "statement_subtle_inversion",
    "2751": "distractor_by_topic_association",
    "2809": "geographic_attribution",
    "2810": "geographic_attribution",
    "2811": "geographic_attribution",
}


# Discrimination cards — drafted by Sonnet in-conv (v2.1, no sub-agents).
DISCRIMINATION_CARDS: dict = {
}


# Merge overlays (cards drafted by Sonnet, written to scratch JSON). Any
# wave1_*.json / wave2_*.json picked up automatically.
_SCRATCH = ROOT / ".scratch" / "drill_2018"
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
