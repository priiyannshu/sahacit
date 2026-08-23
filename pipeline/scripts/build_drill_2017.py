#!/usr/bin/env python3
"""
Generate app/pwa/data/drill_clusters_2017.json
       + app/pwa/data/discrimination_cards_2017.json

Cluster map covers all 98 GS1 2017 PYQs. Clusters + trap tags drafted by
Sonnet Phase 1 (in-conv, v2.1 workflow). Opus consolidation pass: zero
cluster merges (32 within 30-42 target; the three singletons — 359 Ryotwari,
558 freedom-chronology, 1013 Chabahar — are each topically distinct enough
that a forced merge would dilute discrimination focus). Zero trap retags
after QC (Sonnet correctly applied the all-true → statement_partial_truth
rule on 868/1294/1604/1635/1636/2303/2334/2490/2595/2627/2648/2677).

DQ flag deferred: #1463 (APMCHUD S1 plausibly true → official ans=d may be
erroneous). Card drafted to official d; entry to be added to
reference_pyq_data_quality_fixes.md after Phase 2.

Discrimination cards drafted by sequential Sonnet batches; auto-overlay loader
picks up wave1*.json + wave2*.json from .scratch/drill_2017/.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "pwa" / "data" / "pyq_index.json"
OUT_CLUSTERS = ROOT / "pwa" / "data" / "drill_clusters_2017.json"
OUT_CARDS = ROOT / "pwa" / "data" / "discrimination_cards_2017.json"

YEAR = 2017

# Cluster definitions for all 98 2017 PYQs.
# Format: (cluster_id, title, subject_focus, study_keywords[], common_traps[], pyq_ids[])
CLUSTERS: list = [
    # --- Ancient Indian History (4 PYQs, 2 clusters) ---
    ("anc_vedic_ivc_sects", "Ancient India: Vedic-IVC Contrasts & Buddhist Philosophical Schools — Rigvedic Aryans vs IVC; Sautrantika/Sarvastivadin", "Ancient Indian History",
     ["Rigvedic Aryans vs Indus Valley Civilization differences horse iron gold",
      "Sautrantika Sammitiya Buddhist schools not Jainism",
      "Sarvastivadin Hinayana school phenomena latent form permanence",
      "IVC Harappan civilization metals used copper bronze no iron"],
     ["statement_subtle_inversion", "overlapping_categories"],
     [75, 218]),
    ("anc_art_temples", "Ancient India: Buddhist Art & Sun Temples — Bodhisattva Padmapani at Ajanta; Arasavalli vs Amarakantak vs Omkareshwar", "Ancient Indian History",
     ["Bodhisattva Padmapani painting Ajanta caves location",
      "Arasavalli Sun temple Andhra Pradesh Srikakulam",
      "Amarakantak Narmada origin Shiva temple not Sun temple",
      "Omkareshwar Jyotirlinga Shiva temple Madhya Pradesh not Sun"],
     ["famous_association_bias", "overlapping_categories"],
     [138, 139]),

    # --- Art and Culture (2 PYQs, 1 cluster) ---
    ("ca_traditions_festivals", "Art & Culture: Regional Traditions & Festivals — Manipuri Sankirtana; Chaliha Sahib/Sindhis, Nanda Raj Jaat Yatra/Uttarakhand, Wari-Warkari/Maharashtra", "Art and Culture",
     ["Manipuri Sankirtana UNESCO intangible heritage pung drum cymbals",
      "Chaliha Sahib Festival Sindhi community",
      "Nanda Raj Jaat Yatra Uttarakhand pilgrimage not Gonds",
      "Wari-Warkari Vitthal Pandharpur Maharashtra not Santhals"],
     ["statement_overgeneralization", "geographic_attribution"],
     [8, 40]),

    # --- Modern Indian History (7 PYQs, 4 clusters) ---
    ("mod_land_revenue_ryotwari", "Modern India: Revenue Settlements — Ryotwari (Alexander Read + Thomas Munro; Cornwallis = Permanent Settlement, NOT Ryotwari)", "Modern Indian History",
     ["Ryotwari Settlement Alexander Read Thomas Munro Madras",
      "Permanent Settlement Lord Cornwallis Zamindari Bengal 1793",
      "land revenue systems British India comparative mahalwari ryotwari permanent"],
     ["person_attribution"],
     [359]),
    ("mod_colonial_orgs_labour", "Modern India: Early Colonial Organizations & Labour — Factories Act 1881 (NOT wages/TU); Radhakanta Deb, Lakshminarasu Chetty (Madras Native Association not Mahajana Sabha), Surendranath Banerjee", "Modern Indian History",
     ["Factories Act 1881 child labour working hours not wages not trade unions",
      "N.M. Lokhande labour movement British India pioneer",
      "Radhakanta Deb British Indian Association first president",
      "Gazulu Lakshminarasu Chetty Madras Native Association not Mahajana Sabha",
      "Surendranath Banerjee Indian Association founder 1876"],
     ["statement_subtle_inversion", "person_attribution"],
     [404, 405]),
    ("mod_colonial_acts_dyarchy", "Modern India: Colonial Constitutional Acts — Dyarchy (GoI 1919: reserved/transferred subjects); Trade Disputes Act 1929 (tribunals + ban on strikes); Butler Committee 1927 (princely states relation)", "Modern Indian History",
     ["Dyarchy diarchy Montagu-Chelmsford 1919 reserved transferred subjects provinces",
      "Trade Disputes Act 1929 tribunals ban on strikes industrial disputes",
      "Butler Committee 1927 Indian princely states Crown paramountcy relationship"],
     ["technical_vs_common_meaning", "distractor_by_topic_association"],
     [467, 506, 507]),
    ("mod_freedom_chronology", "Modern India: Freedom Movement Chronology — 2nd Round Table Conference (1931) → Quit India (1942) → Royal Indian Navy Mutiny (1946)", "Modern Indian History",
     ["Second Round Table Conference 1931 Gandhi London",
      "Quit India Movement 1942 August Kranti",
      "Royal Indian Navy Mutiny 1946 Bombay chronology"],
     ["period_attribution"],
     [558]),

    # --- Indian Polity (23 PYQs, 7 clusters) ---
    ("pol_political_theory_basics", "Polity: Political Theory Fundamentals — Equality (absence of privileges); Rights as citizens' claims against State; Local self-government = democratic decentralisation; Parliamentary government = executive responsible to legislature", "Indian Polity",
     ["equality absence of privilege political theory",
      "rights claims citizens against state liberal theory",
      "local self-government democratic decentralisation not federalism",
      "parliamentary government collective responsibility executive legislature",
      "cabinet government collective responsibility principle"],
     ["technical_vs_common_meaning", "distractor_by_topic_association"],
     [678, 679, 680, 681, 682, 683]),
    ("pol_constitution_preamble", "Polity: Constitution Fundamentals — Preamble does NOT include economic liberty; Preamble reflects constitution-makers' intent; Judicial Review = constitutionality test (not wisdom, not pre-assent)", "Indian Polity",
     ["Preamble Constitution India liberty thought expression belief not economic liberty",
      "Preamble mind makers constitution vision soul",
      "Judicial Review India constitutionality laws executive orders not wisdom"],
     ["negation_trap", "technical_vs_common_meaning"],
     [721, 722, 723]),
    ("pol_federalism_presidents_rule", "Polity: Federalism & President's Rule — Indian federation NOT result of agreement among states; Article 356 consequences: Council of Ministers removal YES, Legislative Assembly dissolution + local bodies NOT necessarily", "Indian Polity",
     ["Indian federalism not agreement among states Constituent Assembly top-down",
      "Article 356 President's Rule consequences state assembly dissolution not necessary",
      "President's Rule Council of Ministers removal automatic"],
     ["negation_trap", "statement_subtle_inversion"],
     [698, 724]),
    ("pol_fr_dpsp_duties", "Polity: FR, DPSPs & Fundamental Duties — Right to vote = Constitutional (not FR); Right against Exploitation (Articles 23-24, NOT untouchability/minorities); 42nd Amendment added worker management participation; DPSPs not legal limitations; FDs non-justiciable", "Indian Polity",
     ["Right to vote constitutional right not fundamental Article 326",
      "Right against Exploitation Article 23 24 forced labour child labour factories",
      "Abolition untouchability Article 17 Right to Equality not Right against Exploitation",
      "42nd Amendment Directive Principles worker participation management industry Article 43A",
      "DPSP Directive Principles non-justiciable not limitation on legislature executive",
      "Fundamental Duties non-justiciable no enforcement mechanism correlative legal duties"],
     ["overlapping_categories", "statement_subtle_inversion"],
     [760, 761, 777, 778, 779, 780]),
    ("pol_parliament_legislature", "Polity: Parliament & Legislature — Private member's bill (any non-minister MP, NOT only nominated); Parliament control via adjournment motion + question hour + supplementary questions (all three); Lok Sabha FPTP — no 50% threshold; Deputy Speaker post not constitutionally fixed to opposition", "Indian Polity",
     ["private member's bill Parliament India any MP not minister not nominated",
      "Parliament control Council of Ministers adjournment motion question hour",
      "Lok Sabha FPTP first past the post no 50 percent majority required",
      "Speaker Deputy Speaker post Lok Sabha constitutional provision convention"],
     ["statement_subtle_inversion", "statement_partial_truth"],
     [867, 868, 869]),
    ("pol_elections_ec", "Polity: Elections & Election Commission — Lok Sabha nomination: any citizen on any constituency's electoral roll (not resident-only); ECI resolves party split/merger disputes; NOT 5-member body; schedule decided by ECI not Home Ministry", "Indian Polity",
     ["Lok Sabha nomination paper any citizen electoral roll any constituency",
      "Election Commission India composition Chief Election Commissioner members",
      "ECI political party split merger recognition dispute resolution",
      "election schedule general elections bye-elections ECI not Home Ministry"],
     ["statement_subtle_inversion", "technical_vs_common_meaning"],
     [956, 957]),
    ("pol_foreign_geostrategy", "Polity/IR: Foreign Relations — Chabahar Port (Iran): India bypasses Pakistan for Afghanistan and Central Asia access", "Indian Polity",
     ["Chabahar Port Iran India strategic importance Afghanistan Central Asia",
      "India Pakistan bypass overland trade route Chabahar",
      "International North South Transport Corridor INSTC Chabahar"],
     ["distractor_by_topic_association"],
     [1013]),

    # --- Indian Economy (27 PYQs, 7 clusters) ---
    ("eco_macro_liberalization", "Economy: Macroeconomics — Post-1991 liberalization (agriculture GDP share DECLINED); GST advantages (unified market yes; reduce CAD/overtake China = overblown); Tax-revenue and fiscal deficit both did NOT steadily increase", "Indian Economy",
     ["1991 liberalization India agriculture GDP share declined services manufacturing increased",
      "GST Goods Services Tax unified market single tax not reduce current account deficit",
      "India tax revenue GDP fiscal deficit trends decade not steady increase"],
     ["statement_subtle_inversion", "statement_overgeneralization"],
     [1105, 1183, 1184]),
    ("eco_banking_fintech", "Economy: Banking & Fintech — MPC (6-member not 12; chaired by RBI Governor not Finance Minister); Small Finance Banks (credit to small business + marginal farmers; NOT young entrepreneurs); UPI; S4A stressed assets; NPS (state govt employees); NPCI/RuPay", "Indian Economy",
     ["Monetary Policy Committee MPC 6 members RBI Governor chairman not Finance Minister not 12",
      "Small Finance Banks financial inclusion credit small business marginal farmers",
      "National Pension System NPS state government employees",
      "S4A Scheme Sustainable Structuring Stressed Assets RBI corporate debt resolution",
      "NPCI National Payments Corporation India RuPay card financial inclusion",
      "UPI Unified Payments Interface direct bank transfer mobile wallet"],
     ["numerical_proximity", "statement_subtle_inversion", "statement_partial_truth"],
     [1216, 1290, 1291, 1292, 1293, 1294]),
    ("eco_international_orgs", "Economy: International Economic Orgs — APMCHUD; Global Infrastructure Facility (World Bank PPP); UN-Habitat (partners not only governments); BTIA (India-EU); WTO TFA (Bali 2013; in force Feb 2017 not Jan 2016)", "Indian Economy",
     ["Global Infrastructure Facility World Bank PPP private sector institutional investors",
      "UN-Habitat sustainable towns cities not only governments civil society partners",
      "BTIA Broad-based Trade Investment Agreement India European Union",
      "WTO Trade Facilitation Agreement Bali 2013 India ratification entry into force 2017"],
     ["overlapping_categories", "statement_subtle_inversion"],
     [1463, 1464, 1465, 1466, 1467]),
    ("eco_social_welfare_schemes", "Economy: Social Welfare Schemes — National Nutrition Mission (awareness + anaemia reduction; NOT millets promotion/poultry eggs); Vidyanjali Yojana (private sector help to govt schools; NOT foreign campuses); Unnat Bharat Abhiyan (HEIs + local communities)", "Indian Economy",
     ["National Nutrition Mission POSHAN objectives anaemia pregnant women lactating mothers",
      "Vidyanjali Yojana government schools private sector community volunteers not foreign institutions",
      "Unnat Bharat Abhiyan higher education institutions rural development challenges technology"],
     ["statement_partial_truth", "distractor_by_topic_association"],
     [1535, 1536, 1537]),
    ("eco_skills_employment", "Economy: Skills & Employment — NSQF (certification via formal AND non-formal learning, not only formal); National Career Service (Ministry of Labour not DoPT; for all job seekers not uneducated only); Recognition of Prior Learning (construction workers' traditional skills)", "Indian Economy",
     ["National Skills Qualification Framework NSQF formal non-formal learning mobility vocational general education",
      "National Career Service NCS Ministry Labour Employment all job seekers",
      "Recognition of Prior Learning RPL construction workers informal traditional skills certification"],
     ["statement_subtle_inversion", "distractor_by_topic_association"],
     [1575, 1576, 1577]),
    ("eco_agriculture_schemes", "Economy: Agriculture Schemes — National Agriculture Market e-NAM (pan-India electronic portal + quality-based pricing); Soil Health Card (checking fertilizer overuse only; NOT expanding irrigation, NOT bank loan assessment)", "Indian Economy",
     ["National Agriculture Market e-NAM electronic trading portal farmers price quality",
      "Soil Health Card Scheme fertilizer overuse checking not irrigation expansion",
      "Soil Health Card not used by banks for loan assessment"],
     ["statement_partial_truth"],
     [1604, 1605]),
    ("eco_economic_laws_institutions", "Economy: Economic Laws & Institutions — BIS mandatory for auto tyres; AGMARK by Indian DMI NOT FAO; QCI jointly GoI + industry; National IPR Policy (TRIPS + DIPP nodal); NIIF NOT NITI Aayog organ; Benami Property Act (confiscation YES; appellate mechanism EXISTS)", "Indian Economy",
     ["BIS Bureau Indian Standards mandatory automotive tyres tubes",
      "AGMARK quality certification Directorate Marketing Inspection not FAO",
      "Quality Council India QCI joint government industry Prime Minister chairman",
      "National IPR Policy DIPP nodal agency TRIPS Doha Development Agenda",
      "NIIF National Investment Infrastructure Fund Ministry Finance not NITI Aayog",
      "Prohibition Benami Property Transactions Act confiscation appellate tribunal"],
     ["overlapping_categories", "statement_subtle_inversion"],
     [1634, 1635, 1636, 1637, 1638]),

    # --- Geography (7 PYQs, 3 clusters) ---
    ("geo_india_physical", "Geography: India Physical — Kohima to Kottayam: 7 states minimum; Great Nicobar closest to Sumatra (not Borneo/Java); Chandipur (Odisha) tidal bore phenomenon", "Geography",
     ["Kohima Kottayam road minimum states India Nagaland Assam West Bengal Odisha Andhra Tamil Nadu Kerala",
      "Great Nicobar Island closest island Sumatra Indonesia not Borneo Java",
      "Chandipur Odisha tidal bore sea recedes kilometres walk sea floor phenomenon"],
     ["numerical_proximity", "geographic_attribution"],
     [1808, 1809, 1921]),
    ("geo_rivers_climate_iod", "Geography: Indian Rivers & Climate — IOD (Western Indian Ocean vs Eastern Indian Ocean SST difference; NOT Eastern Pacific which is ENSO); River Teesta (source ≠ Brahmaputra; Rangeet is tributary; flows to Brahmaputra not Bay of Bengal directly)", "Geography",
     ["Indian Ocean Dipole IOD sea surface temperature western eastern Indian Ocean not Pacific",
      "IOD El Nino ENSO distinction Indian monsoon",
      "River Teesta source Gurudongmar Lake Sikkim not same as Brahmaputra",
      "River Rangeet Sikkim tributary Teesta",
      "Teesta River flows into Brahmaputra Bangladesh not Bay of Bengal directly"],
     ["geographic_attribution", "statement_subtle_inversion"],
     [1732, 1886]),
    ("geo_world_agriculture", "Geography: World Map & Agriculture Water Conservation — Mediterranean Sea borders Lebanon+Syria (Jordan and Iraq do NOT border Mediterranean); reduced tillage + crop residue for water conservation (gypsum = sodic soil, NOT water conservation)", "Geography",
     ["Mediterranean Sea border countries Lebanon Syria Jordan Iraq landlocked",
      "Jordan landlocked Dead Sea Gulf of Aqaba not Mediterranean",
      "Iraq landlocked Persian Gulf not Mediterranean",
      "zero tillage reduced tillage crop residue water conservation soil moisture",
      "gypsum application sodic soil reclamation not water conservation"],
     ["geographic_attribution", "statement_partial_truth"],
     [1961, 2082]),

    # --- Environment (14 PYQs, 4 clusters) ---
    ("env_biodiversity_wildlife", "Environment: Biodiversity & Wildlife Protection — Butterfly trophic cascade (pollination + predator populations, NOT fungal infections); Gharial in Chambal; WPA animals (gharial + wild ass + wild buffalo = all three); M-STrIPES tiger reserve monitoring; Schedule I = highest protection; Kuno Palpur lion translocation; Sathyamangalam as Eastern-Western Ghats corridor", "Environment",
     ["butterfly population fall pollination pollinator trophic cascade wasps spiders birds",
      "Gharial Chambal River natural habitat not mangroves not lake",
      "Wildlife Protection Act 1972 Schedule I animals gharial wild ass wild buffalo cannot hunt",
      "M-STrIPES Monitoring System Tigers Intensive Protection Ecological Status tiger reserve",
      "Schedule I Wildlife Protection Act highest protection same as tiger",
      "Kuno Palpur Wildlife Sanctuary Madhya Pradesh Asiatic lion translocation from Gujarat",
      "Sathyamangalam Tiger Reserve Tamil Nadu Karnataka Eastern Western Ghats corridor link"],
     ["statement_partial_truth", "geographic_attribution", "distractor_by_topic_association"],
     [2137, 2183, 2334, 2335, 2336, 2337, 2338]),
    ("env_pollution_bioremediation", "Environment: Pollution & Bioremediation — Bioremediation enhances natural biodegradation; heavy metals NOT readily/completely treated; genetic engineering possible; BOD = aquatic pollution measure (NOT blood/forest/altitude)", "Environment",
     ["bioremediation natural biodegradation process pollution cleanup microorganisms",
      "heavy metals cadmium lead bioremediation limitation not readily completely treated",
      "genetic engineering microorganisms bioremediation specifically designed",
      "Biological Oxygen Demand BOD aquatic ecosystem water pollution organic matter"],
     ["statement_subtle_inversion", "distractor_by_topic_association"],
     [2264, 2265]),
    ("env_climate_carbon_energy", "Environment: Climate Change & Clean Energy — Carbon sequestration: abandoned coal seams + depleted oil/gas reservoirs + deep saline formations (all three); Algae biofuels: NOT only in seas (photobioreactors on land), requires high expertise AND large scale creates concerns", "Environment",
     ["carbon sequestration coal seams depleted oil gas reservoirs saline formations CCS",
      "algae biofuel photobioreactor not only in seas freshwater land possible",
      "algae biofuel high technology expertise large scale ecological social concerns"],
     ["statement_partial_truth", "statement_subtle_inversion"],
     [2303, 2455]),
    ("env_global_initiatives", "Environment: Global Environmental Initiatives — Global Climate Change Alliance (EU initiative, coordinated by EU not WRI/WBCSD); CCAC (multi-stakeholder NOT G20; focuses methane+black carbon+HFCs); TRAFFIC (IUCN+WWF joint program, NOT UNEP bureau)", "Environment",
     ["Global Climate Change Alliance GCCA European Union initiative developing countries climate finance",
      "Climate Clean Air Coalition CCAC methane black carbon HFCs not G20 initiative",
      "TRAFFIC wildlife trade IUCN WWF joint program not UNEP bureau"],
     ["overlapping_categories", "statement_subtle_inversion"],
     [2393, 2394, 2395]),

    # --- Science and Technology (8 PYQs, 3 clusters) ---
    ("sci_space_physics_displays", "S&T: Physics, Space & Displays — Event Horizon/Singularity/String Theory/Standard Model = universe study; eLISA = gravitational waves detector; OLED: flexible substrates + roll-up + transparent = all three advantages over LCD", "Science and Technology",
     ["Event Horizon Singularity String Theory Standard Model cosmology universe observation",
      "eLISA evolved Laser Interferometer Space Antenna gravitational waves detection",
      "OLED Organic Light Emitting Diode advantages LCD flexible plastic transparent roll-up"],
     ["distractor_by_topic_association", "statement_partial_truth"],
     [2521, 2522, 2627]),
    ("sci_biotech_genetics", "S&T: Biotech & Genetics — Genome sequencing: disease resistance markers + reduce breeding time + host-pathogen (all three valid); Somatic Cell Nuclear Transfer = reproductive cloning; Zika: Aedes mosquito (same as dengue) + sexual transmission (both correct)", "Science and Technology",
     ["genome sequencing agriculture disease resistance drought tolerance breeding time host-pathogen",
      "Somatic Cell Nuclear Transfer SCNT reproductive cloning animals Dolly sheep",
      "Zika virus Aedes mosquito dengue same vector sexual transmission possible"],
     ["statement_partial_truth", "distractor_by_topic_association"],
     [2595, 2596, 2677]),
    ("sci_chemistry_cyber", "S&T: Consumer Chemicals & Cybersecurity — Lead in lipstick + brominated vegetable oils in soft drinks + MSG in Chinese food (all three matched); Cyber security incident reporting mandatory for service providers + data centres + body corporate (all three)", "Science and Technology",
     ["lead lipstick brominated vegetable oil soft drink MSG Chinese food controversial chemicals",
      "cyber security incident reporting India mandatory service providers data centres body corporate IT Act"],
     ["statement_partial_truth"],
     [2490, 2648]),

    # --- Current Affairs and GK (6 PYQs, 1 cluster) ---
    ("ca_intl_orgs_gk", "Current Affairs & GK: International Organizations — Nuclear Security Summits (NOT under UN; IPFM NOT IAEA organ); Global Gender Gap Index (WEF); Digital Single Market Strategy (EU); IONS inaugural 2008 not 2015; Domestic Content Requirement (solar); Smart India Hackathon (digital innovation, NOT Smart Cities/digital-only economy)", "Current Affairs and GK",
     ["Nuclear Security Summit not United Nations aegis Obama initiative",
      "IPFM International Panel Fissile Materials Princeton independent not IAEA",
      "Global Gender Gap Index World Economic Forum WEF annual report",
      "Digital Single Market Strategy European Union e-commerce data free flow",
      "Indian Ocean Naval Symposium IONS inaugural 2008 India voluntary maritime cooperation",
      "Domestic Content Requirement DCR solar power cells modules India manufacturing",
      "Smart India Hackathon digital technology innovation problem solving not smart cities"],
     ["overlapping_categories", "period_attribution", "distractor_by_topic_association"],
     [2727, 2752, 2753, 2754, 2812, 2813]),
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
# QC notes: All-true-answer cases (868, 1294, 1604, 1635, 1636, 2303, 2334,
# 2490, 2595, 2627, 2648, 2677) correctly tagged statement_partial_truth — the
# 2428 (2020) lesson stuck. Negation traps (698, 721, 724) flagged via NOT/which-
# is-not framing. No retags applied. Pre-2023: zero explanatory_chain.
TRAP_TAGS: dict = {
    "8":    "statement_overgeneralization",
    "40":   "geographic_attribution",
    "75":   "statement_subtle_inversion",
    "138":  "famous_association_bias",
    "139":  "overlapping_categories",
    "218":  "overlapping_categories",
    "359":  "person_attribution",
    "404":  "statement_subtle_inversion",
    "405":  "person_attribution",
    "467":  "technical_vs_common_meaning",
    "506":  "distractor_by_topic_association",
    "507":  "distractor_by_topic_association",
    "558":  "period_attribution",
    "678":  "technical_vs_common_meaning",
    "679":  "statement_subtle_inversion",
    "680":  "technical_vs_common_meaning",
    "681":  "distractor_by_topic_association",
    "682":  "distractor_by_topic_association",
    "683":  "technical_vs_common_meaning",
    "698":  "negation_trap",
    "721":  "negation_trap",
    "722":  "distractor_by_topic_association",
    "723":  "technical_vs_common_meaning",
    "724":  "negation_trap",
    "760":  "overlapping_categories",
    "761":  "overlapping_categories",
    "777":  "period_attribution",
    "778":  "statement_subtle_inversion",
    "779":  "statement_subtle_inversion",
    "780":  "distractor_by_topic_association",
    "867":  "statement_subtle_inversion",
    "868":  "statement_partial_truth",
    "869":  "statement_subtle_inversion",
    "956":  "technical_vs_common_meaning",
    "957":  "statement_subtle_inversion",
    "1013": "distractor_by_topic_association",
    "1105": "statement_subtle_inversion",
    "1183": "statement_overgeneralization",
    "1184": "statement_subtle_inversion",
    "1216": "numerical_proximity",
    "1290": "distractor_by_topic_association",
    "1291": "statement_partial_truth",
    "1292": "distractor_by_topic_association",
    "1293": "distractor_by_topic_association",
    "1294": "statement_partial_truth",
    "1463": "statement_subtle_inversion",
    "1464": "overlapping_categories",
    "1465": "statement_overgeneralization",
    "1466": "distractor_by_topic_association",
    "1467": "statement_subtle_inversion",
    "1535": "statement_partial_truth",
    "1536": "distractor_by_topic_association",
    "1537": "distractor_by_topic_association",
    "1575": "statement_subtle_inversion",
    "1576": "statement_subtle_inversion",
    "1577": "distractor_by_topic_association",
    "1604": "statement_partial_truth",
    "1605": "statement_partial_truth",
    "1634": "overlapping_categories",
    "1635": "statement_partial_truth",
    "1636": "statement_partial_truth",
    "1637": "overlapping_categories",
    "1638": "statement_subtle_inversion",
    "1732": "geographic_attribution",
    "1808": "numerical_proximity",
    "1809": "geographic_attribution",
    "1886": "geographic_attribution",
    "1921": "geographic_attribution",
    "1961": "statement_partial_truth",
    "2082": "geographic_attribution",
    "2137": "statement_partial_truth",
    "2183": "geographic_attribution",
    "2264": "statement_subtle_inversion",
    "2265": "distractor_by_topic_association",
    "2303": "statement_partial_truth",
    "2334": "statement_partial_truth",
    "2335": "distractor_by_topic_association",
    "2336": "overlapping_categories",
    "2337": "geographic_attribution",
    "2338": "geographic_attribution",
    "2393": "overlapping_categories",
    "2394": "statement_subtle_inversion",
    "2395": "overlapping_categories",
    "2455": "statement_subtle_inversion",
    "2490": "statement_partial_truth",
    "2521": "distractor_by_topic_association",
    "2522": "distractor_by_topic_association",
    "2595": "statement_partial_truth",
    "2596": "distractor_by_topic_association",
    "2627": "statement_partial_truth",
    "2648": "statement_partial_truth",
    "2677": "statement_partial_truth",
    "2727": "overlapping_categories",
    "2752": "overlapping_categories",
    "2753": "distractor_by_topic_association",
    "2754": "period_attribution",
    "2812": "distractor_by_topic_association",
    "2813": "distractor_by_topic_association",
}


# Discrimination cards — drafted by Sonnet agents, merged by Opus.
DISCRIMINATION_CARDS: dict = {
}


# Merge overlays (cards drafted by Sonnet, written to scratch JSON). Any
# wave1_*.json / wave2_*.json picked up automatically.
_SCRATCH = ROOT / ".scratch" / "drill_2017"
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
