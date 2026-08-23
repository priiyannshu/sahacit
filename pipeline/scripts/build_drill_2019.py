#!/usr/bin/env python3
"""
Generate app/pwa/data/drill_clusters_2019.json
       + app/pwa/data/discrimination_cards_2019.json

Cluster map covers all 101 GS1 2019 PYQs. Clusters + trap tags drafted by
Sonnet pre-step agents (cluster + trap-tag), Opus consolidated 37→33 clusters
(4 merges:
  - med_delhi_sultanate_admin + med_mughal_admin_land  → med_admin_revenue_systems
  - eco_planning_fiveyear [1661]                       → eco_macro_external
  - geo_world_map_seas    [2080]                       → geo_rivers_glaciers_india
  - env_ecology_food_web  [2135]                       → env_biodiversity_species
2 singletons retained: geo_anthropology_human [1684] (Denisovan; doesn't fit
elsewhere coherently), mod_colonial_laws_acts [356] (Charter Act 1813;
constitutionally distinct from Gandhi-era movements).

Discrimination cards drafted by parallel Sonnet batches; auto-overlay loader
picks up wave1*.json + wave2*.json from .scratch/drill_2019/.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "pwa" / "data" / "pyq_index.json"
OUT_CLUSTERS = ROOT / "pwa" / "data" / "drill_clusters_2019.json"
OUT_CARDS = ROOT / "pwa" / "data" / "discrimination_cards_2019.json"

YEAR = 2019

# Cluster definitions for all 101 2019 PYQs.
# Format: (cluster_id, title, subject_focus, study_keywords[], common_traps[], pyq_ids[])
CLUSTERS: list = [
    # --- Ancient Indian History (4 PYQs, 2 clusters) ---
    ("anc_harappan_mauryan", "Ancient India: Harappan Sites & Mauryan-Era Inscriptions — Sohgaura, Kanganahalli", "Ancient Indian History",
     ["Harappan sites Chanhudaro Kot Diji Desalpur Sohgaura identification",
      "Sohgaura Mauryan inscription vs Harappan IVC site distinction",
      "Kanganahalli Karnataka relief sculpture Ashoka portrait Ranyo Ashoka"],
     ["geographic_attribution", "negation_trap", "famous_association_bias"],
     [70, 137]),
    ("anc_society_religion", "Ancient India: Gupta Society (Vishti) & Buddhist Schools (Mahayana Features)", "Ancient Indian History",
     ["Vishti forced labour Gupta period state revenue tax not wage",
      "Mahayana Buddhism Bodhisattva deification image worship features",
      "Hinayana Mahayana Theravada schools doctrinal differences"],
     ["statement_subtle_inversion", "statement_partial_truth"],
     [104, 215]),

    # --- Medieval Indian History (6 PYQs, 3 clusters) ---
    ("med_admin_revenue_systems", "Medieval India: Administrative & Revenue Systems — Sultanate (Iqta, Mir Bakshi) and Mughal (Jagirdar vs Zamindar)", "Medieval Indian History",
     ["Delhi Sultanate revenue Amil collector Iqta system origin foreign import",
      "Mir Bakshi Mughal office not Khalji or Tughlaq creation",
      "Jagirdar Zamindar Mughal land assignments hereditary military duties",
      "medieval Indian land revenue administrative apparatus comparative"],
     ["statement_subtle_inversion", "overlapping_categories", "period_attribution"],
     [254, 255]),
    ("med_mughal_art_bhakti", "Medieval India: Mughal Music/Painting, Vijayanagara Temples & Bhakti Saints — Tansen, Kalyana Mandapa, Nimbarka/Sirhindi", "Medieval Indian History",
     ["Mian Tansen Dhrupads Akbar Hindu gods title Gwalior Raja not emperor",
      "Mughal painting album portrait shift Jahangir not Akbar pre-eminent",
      "Vijayanagara Kalyana Mandapa temple feature not Chalukya Rashtrakuta",
      "Bhakti saint Nimbarka pre-Akbar Kabir Shaikh Ahmad Sirhindi influence"],
     ["negation_trap", "famous_association_bias", "period_attribution", "statement_subtle_inversion"],
     [325, 326, 327, 341]),

    # --- Modern Indian History (6 PYQs, 3 clusters) ---
    ("mod_colonial_laws_acts", "Modern India: Charter Act 1813 — EIC Trade Monopoly & Crown Sovereignty", "Modern Indian History",
     ["Charter Act 1813 East India Company tea China trade monopoly retained",
      "British Crown sovereignty Indian territories Company assertion 1813",
      "Charter Acts sequence 1793 1813 1833 1853 revenue Parliament control"],
     ["statement_subtle_inversion"],
     [356]),
    ("mod_gandhi_mass_movements", "Modern India: Gandhi & Mass Movements — Indentured Labour, Salt Law 1930, Swadeshi NCE, Chelmsford War Conference", "Modern Indian History",
     ["Mahatma Gandhi indentured labour abolition Fiji plantation petition",
      "Salt Law breaking 1930 Indian National Congress declared illegal",
      "Swadeshi Movement 1905 National Council of Education artisan revival",
      "Lord Chelmsford War Conference 1918 Gandhi recruitment resolution support"],
     ["statement_partial_truth", "statement_subtle_inversion"],
     [422, 464, 505]),
    ("mod_organisations_leaders", "Modern India: National Movement Organisations & Leaders — All India Liberal Federation, Kisan Sabha, Self-Respect, Anti-Untouchability League", "Modern Indian History",
     ["All India Liberal Federation Tej Bahadur Sapru president founder",
      "All India Kisan Sabha Swami Sahajanand Saraswati founder 1929",
      "Self-Respect Movement E.V. Ramaswami Periyar Naicker Tamil Nadu",
      "Anti-Untouchability League Gandhi P.C. Joshi Communist Party positions"],
     ["statement_partial_truth"],
     [556, 609]),

    # --- Indian Polity (15 PYQs, 5 clusters) ---
    ("pol_constitutional_theory", "Polity: Constitutional Theory — Liberty Definition, Ninth/Fifth Schedules, Article 21 Personal Liberty", "Indian Polity",
     ["definition liberty opportunity self-development political philosophical",
      "Ninth Schedule first amendment Nehru 1951 introduction not Indira",
      "Fifth Schedule tribal land mining protection scope categorisation",
      "Article 21 right to marry personal liberty Supreme Court interpretation"],
     ["technical_vs_common_meaning", "person_attribution", "overlapping_categories"],
     [675, 717, 718, 757]),
    ("pol_amendments_acts", "Polity: Constitutional Amendments (44th, 99th NJAC) & Forest Rights Act — Bamboo Classification", "Indian Polity",
     ["44th Amendment PM election judicial review beyond not 39th",
      "99th Amendment NJAC National Judicial Appointments Commission struck down",
      "Forest Rights Act 2006 bamboo minor forest produce ownership dwellers",
      "Indian Forest Act 1927 bamboo reclassification timber felling right"],
     ["statement_subtle_inversion", "overlapping_categories"],
     [1036, 1037]),
    ("pol_legislature_parliament", "Polity: Parliament & State Legislature — Office of Profit, Lok Sabha Rules Adoption, Standing Committees", "Indian Polity",
     ["Office of Profit Parliament Prevention Disqualification Act 1959 not constitution",
      "State Legislature rules silent Lok Sabha procedure adopted",
      "Parliamentary Standing Committees Ad Hoc independent regulators review"],
     ["statement_subtle_inversion", "statement_partial_truth", "overlapping_categories"],
     [860, 861, 862]),
    ("pol_judiciary", "Polity: Supreme Court & High Courts — Judges Inquiry Act 1968, Article 142, Basic Structure Review", "Indian Polity",
     ["Supreme Court judge impeachment Judges Inquiry Act 1968 Speaker process",
      "Article 142 Supreme Court complete justice Parliament laws not bind",
      "High Court central law strike down jurisdiction constitutional amendment"],
     ["statement_subtle_inversion", "technical_vs_common_meaning"],
     [920, 921, 922]),
    ("pol_executive_federalism_intl", "Polity: Executive, Federalism & International Governance — Sarkaria, UNCAC vs UNTOC, GDPR", "Indian Polity",
     ["Sarkaria Commission 1983 Governor eminent detached criteria not Rajamannar",
      "UNCAC UNTOC migrants smuggling protocol asset recovery distinction",
      "GDPR General Data Protection Regulation EU April 2016 implementation"],
     ["person_attribution", "statement_subtle_inversion", "geographic_attribution"],
     [829, 1009, 1010]),

    # --- Indian Economy (28 PYQs, 8 clusters) ---
    ("eco_macro_external", "Economy: Macroeconomics & Plan Strategy — PPP/GDP Rankings, External Debt USD Mix, 5th Plan Financial Sector", "Indian Economy",
     ["Purchasing Power Parity PPP basket goods exchange rate India third largest",
      "India external debt government private USD denomination mixed not all",
      "Second Five Year Plan Mahalanobis capital goods basic industries import substitution",
      "Fourth Plan wealth concentration reduction Fifth Plan financial sector inclusion claim"],
     ["statement_subtle_inversion", "statement_overgeneralization"],
     [1100, 1145, 1661]),
    ("eco_monetary_forex", "Economy: Monetary Policy & Forex — Currency Crisis Reducers, Rupee Slide Measures, Money Multiplier", "Indian Economy",
     ["currency crisis India IT sector remittances foreign exchange stabilisation",
      "rupee depreciation RBI measures Masala Bonds ECB expansionary monetary not",
      "money multiplier CRR SLR banking habits formula not population increase"],
     ["statement_subtle_inversion", "negation_trap", "technical_vs_common_meaning"],
     [1213, 1214, 1215]),
    ("eco_banking_capital_markets", "Economy: Banking, Finance & Capital Markets — Lead Bank, Balance Sheet, Inter-Creditor, BBB, RBI Data, P-Notes", "Indian Economy",
     ["Lead Bank Scheme Service Area Approach priority sector rural banking",
      "commercial bank balance sheet deposits liabilities not assets",
      "Inter-Creditor Agreement NPA stressed assets resolution 50 crore consortium",
      "Banks Board Bureau public sector bank chairman selection not RBI",
      "RBI payment data localisation storage diktat fintech not CAG audit",
      "Participatory Notes P-Notes FPIs overseas investors not registered"],
     ["distractor_by_topic_association", "technical_vs_common_meaning", "statement_subtle_inversion", "overlapping_categories"],
     [1280, 1281, 1282, 1283, 1284, 1347]),
    ("eco_industries_minerals", "Economy: Industry, Energy & Minerals — PNGRB, Coal Nationalisation, Sand/Minor Minerals", "Indian Economy",
     ["PNGRB Petroleum Natural Gas Regulatory Board not first regulator gas market",
      "coal nationalisation India Indira Gandhi 1973 not lottery allocation self-sufficient",
      "minor minerals sand state government rules central illegal mining federal"],
     ["statement_subtle_inversion"],
     [1381, 1382, 1383]),
    ("eco_international_trade_orgs", "Economy: International Trade, AIIB & Global Indices — Rice Exports, AIIB Shareholders, Ease of Doing Business", "Indian Economy",
     ["India agricultural imports vegetable oils pulses spices value largest rice exporter",
      "AIIB Asian Infrastructure Investment Bank China largest shareholder not India",
      "World Bank Ease of Doing Business sub-indices law order not included"],
     ["famous_association_bias", "statement_subtle_inversion", "negation_trap"],
     [1434, 1459, 1460]),
    ("eco_welfare_social_capital", "Economy: Welfare, Poverty, PVTGs, AIM, Social Capital", "Indian Economy",
     ["social capital trust harmony society not physical not human capital",
      "Particularly Vulnerable Tribal Groups PVTGs 75 states one UT count",
      "Atal Innovation Mission AIM NITI Aayog not DST Skill Development",
      "poverty line state variation price level cost of living Tendulkar"],
     ["technical_vs_common_meaning", "statement_subtle_inversion", "distractor_by_topic_association"],
     [1484, 1485, 1532, 1533]),
    ("eco_labour_ip_laws", "Economy: Labour Law, Maternity Benefits & Patent Act — Fixed-Term Employment, 26 Weeks Leave, Biological Process", "Indian Economy",
     ["fixed-term employment Industrial Employment Standing Orders 2018 layoff easier",
      "Maternity Benefit Amendment 2017 26 weeks pre-post delivery creche",
      "Indian Patents Act biological process seed patent plant varieties exclusion"],
     ["statement_partial_truth", "statement_subtle_inversion"],
     [1573, 1631, 1632]),
    ("eco_agriculture_fci", "Economy: Agriculture — Land Reform Aim, FCI Economic Cost, Kharif Crop Area Comparison", "Indian Economy",
     ["land reforms ceiling laws aim landless not profit",
      "FCI economic cost MSP procurement incidentals plus distribution charges",
      "Kharif rice cotton sugarcane jowar oilseeds area comparison data"],
     ["statement_subtle_inversion", "technical_vs_common_meaning"],
     [1598, 1599, 1600]),

    # --- Geography (10 PYQs, 4 clusters) ---
    ("geo_physical_climatology", "Geography: Physical — June 21 Solstice (Arctic Midnight Sun), Cirrus Cloud Geoengineering, Dewdrop Formation", "Geography",
     ["June 21 summer solstice Arctic Circle midnight sun not Antarctic",
      "geoengineering cirrus cloud thinning sulphate aerosol global warming reduction",
      "dewdrop cloudy night cloud reflection back radiation warmth retention"],
     ["statement_subtle_inversion", "distractor_by_topic_association"],
     [1683, 1730, 1731]),
    ("geo_anthropology_human", "Geography: Human Origins — Denisovans (Early Hominid Species)", "Geography",
     ["Denisovan early human species hominid Siberia cave archaeological",
      "Denisovan species not region not period nor monument distinction",
      "human evolution Neanderthal Denisovan Homo sapiens fossil DNA"],
     ["distractor_by_topic_association"],
     [1684]),
    ("geo_rivers_glaciers_india", "Geography: Indian Rivers & World Seas — Reservoirs, Pilgrim-River Pairs, Glacier Sources, Adriatic/Black Sea Borders", "Geography",
     ["Aliyar Isapur Kangsabati water reservoirs not minerals dams India",
      "Pandharpur Chandrabhaga Hampi Tungabhadra not Malaprabha river-place",
      "Bandarpunch Yamuna Bara Shigri Chenab Milam Gori Ganga glacier-river",
      "Adriatic Albania Croatia Black Sea borders not Croatia Red Sea Syria"],
     ["distractor_by_topic_association", "geographic_attribution"],
     [1882, 1883, 1884, 2080]),
    ("geo_india_resources_forests", "Geography: India Forest Cover Order & Largest Rice Exporter", "Geography",
     ["forest cover Chhattisgarh Madhya Pradesh Maharashtra Odisha ascending order",
      "largest rice exporter world India not China Vietnam Myanmar value"],
     ["numerical_proximity", "famous_association_bias"],
     [1920, 1959]),

    # --- Environment (18 PYQs, 4 clusters) ---
    ("env_biodiversity_species", "Environment: Biodiversity, Endemic Species & Animal Ecology — Asiatic Lion/Rhino, Irrawaddy Dolphin, Old/New World Crops, Himalayan Nettle, Marine Herbivores", "Environment",
     ["Asiatic lion Gir naturally found rhinoceros camel endemic range",
      "Blue-finned Mahseer Cauvery Irrawaddy Dolphin Chilika not Chambal habitat",
      "New World tobacco cocoa rubber not cotton Old World crops origin",
      "Himalayan nettle Girardinia diversifolia textile fibre not medicine",
      "marine mammals manatee dugong herbivorous viviparous snakes ecology"],
     ["statement_partial_truth", "geographic_attribution", "overlapping_categories", "distractor_by_topic_association"],
     [2135, 2177, 2178, 2179, 2180]),
    ("env_pollution_waste_management", "Environment: Pollution & Waste Management Laws — Microbeads, Organophosphates, EPA 1986, SWM 2016, e-Waste EPR 2011", "Environment",
     ["microbeads plastic marine ecosystem cosmetics personal care not cancer",
      "carbofuran methyl parathion phorate organophosphate pesticides not preservatives",
      "Environment Protection Act 1986 emission discharge standards no public participation mandate",
      "Solid Waste Management Rules 2016 census towns scope not urban only",
      "e-Waste Management Rules 2011 extended producer responsibility EPR introduced"],
     ["distractor_by_topic_association", "statement_subtle_inversion", "period_attribution"],
     [2258, 2259, 2260, 2261, 2262]),
    ("env_climate_change_ghg", "Environment: Climate, GHG & Clean Fuels — Methane Hydrate, Crop Residue Burning, Reactive Nitrogen, H-CNG", "Environment",
     ["methane hydrate Arctic tundra seafloor global warming feedback release",
      "crop residue biomass burning CO methane ozone SO2 atmosphere all",
      "agriculture livestock poultry nitrogen oxides ammonia reactive nitrogen",
      "H-CNG hydrogen enriched CNG buses CO reduction not eliminate CO2 cost"],
     ["statement_partial_truth", "statement_subtle_inversion"],
     [2297, 2298, 2299, 2300]),
    ("env_protected_areas_laws", "Environment: Protected Areas, Wetlands & Forest Laws — Valley of Flowers, Agasthyamala, Ramsar/Wetlands Rules 2010, CAMPA 2016", "Environment",
     ["Valley of Flowers National Park temperate alpine zone Uttarakhand UNESCO",
      "Agasthyamala Biosphere Reserve Neyyar Peppara Shendurney Kalakad Mundanthurai",
      "Ramsar Convention Wetlands Rules 2010 listed wetlands not all mandatory",
      "CAMPA Compensatory Afforestation 2016 dual authority no people participation mandate"],
     ["overlapping_categories", "statement_subtle_inversion"],
     [2328, 2329, 2330, 2331]),

    # --- Science and Technology (12 PYQs, 4 clusters) ---
    ("sci_electronics_digital", "S&T: Digital — LTE/VoLTE 4G, AR vs VR Definitions, Digital Signature Function, Wearables", "Science and Technology",
     ["LTE VoLTE 4G voice over LTE data voice not 3G technology",
      "Augmented Reality AR overlay real world Virtual Reality VR simulation distinction",
      "digital signature electronic record content unchanged identity proof not certificate",
      "wearable technology location sleep monitoring hearing impaired assistive all"],
     ["statement_subtle_inversion", "statement_partial_truth"],
     [2480, 2481, 2482, 2483]),
    ("sci_space_remote_sensing", "S&T: Space — Remote Sensing (Chlorophyll, GHG, Paddy Methane), Black Hole Merger Gravitational Waves", "Science and Technology",
     ["satellite remote sensing chlorophyll vegetation greenhouse gas paddy land temperature all",
      "black hole merger gravitational waves LIGO detection not Higgs not singularity",
      "remote sensing applications agriculture GHG climate measurement"],
     ["statement_partial_truth", "famous_association_bias"],
     [2514, 2515]),
    ("sci_biotech_genetics", "S&T: Biotech — Synthetic Chromosomes, RNAi Gene Silencing, CRISPR-Cas9 Scissors", "Science and Technology",
     ["functional chromosomes synthetic DNA cross-species cannot create laboratory",
      "RNA interference RNAi gene silencing therapy not hormone replacement",
      "Cas9 protein CRISPR molecular scissors gene editing not biosensor"],
     ["negation_trap", "statement_subtle_inversion", "technical_vs_common_meaning"],
     [2591, 2592, 2593]),
    ("sci_health_energy_tech", "S&T: Health & Energy — AMR Causes, Hepatitis B/C Vaccine, Pyrolysis Waste-to-Energy", "Science and Technology",
     ["antibiotic resistance multi-drug livestock incorrect dose not genetic chronic",
      "Hepatitis B vaccine HIV transmission Hepatitis C no vaccine global",
      "pyrolysis plasma gasification waste-to-energy not gas extraction technology"],
     ["distractor_by_topic_association", "statement_subtle_inversion", "negation_trap"],
     [2647, 2663, 2699]),

    # --- Current Affairs and GK (2 PYQs, 1 cluster) ---
    ("ca_international_orgs", "Current Affairs: India-Russia Nuclear Action Plan & WEF Global Competitiveness Report", "Current Affairs and GK",
     ["India Russia nuclear cooperation action plan signed not US UK",
      "Global Competitiveness Report World Economic Forum WEF publisher not IMF World Bank",
      "international nuclear agreement global competitiveness publishing body identification"],
     ["geographic_attribution", "distractor_by_topic_association"],
     [2725, 2750]),
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
    # Carry-forward from 2021: accept "1)"-style + "2 ." numbering + digit-comma
    # multi-select option patterns ("1, 2 and 5") in addition to the "only" qualifier.
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
# QC notes: All-true-answer cases (215, 422, 556, 609, 861, 1573, 2135, 2297,
# 2298, 2299, 2483, 2514) correctly tagged as statement_partial_truth — the
# 2428 (2020) lesson stuck. Negation traps (70, 325, 1214, 1460, 2591, 2699)
# correctly identified by NOT/which-is-not framing. No retags applied.
TRAP_TAGS: dict = {
    "70": "negation_trap",
    "104": "statement_subtle_inversion",
    "137": "geographic_attribution",
    "215": "statement_partial_truth",
    "254": "statement_subtle_inversion",
    "255": "statement_subtle_inversion",
    "325": "negation_trap",
    "326": "famous_association_bias",
    "327": "period_attribution",
    "341": "statement_subtle_inversion",
    "356": "statement_subtle_inversion",
    "422": "statement_partial_truth",
    "464": "statement_subtle_inversion",
    "505": "statement_subtle_inversion",
    "556": "statement_partial_truth",
    "609": "statement_partial_truth",
    "675": "technical_vs_common_meaning",
    "717": "person_attribution",
    "718": "overlapping_categories",
    "757": "overlapping_categories",
    "829": "person_attribution",
    "860": "statement_subtle_inversion",
    "861": "statement_partial_truth",
    "862": "overlapping_categories",
    "920": "statement_subtle_inversion",
    "921": "technical_vs_common_meaning",
    "922": "statement_subtle_inversion",
    "1009": "statement_subtle_inversion",
    "1010": "geographic_attribution",
    "1036": "statement_subtle_inversion",
    "1037": "overlapping_categories",
    "1100": "statement_subtle_inversion",
    "1145": "statement_overgeneralization",
    "1213": "statement_subtle_inversion",
    "1214": "negation_trap",
    "1215": "technical_vs_common_meaning",
    "1280": "distractor_by_topic_association",
    "1281": "technical_vs_common_meaning",
    "1282": "distractor_by_topic_association",
    "1283": "distractor_by_topic_association",
    "1284": "statement_subtle_inversion",
    "1347": "overlapping_categories",
    "1381": "statement_subtle_inversion",
    "1382": "statement_subtle_inversion",
    "1383": "statement_subtle_inversion",
    "1434": "famous_association_bias",
    "1459": "statement_subtle_inversion",
    "1460": "negation_trap",
    "1484": "technical_vs_common_meaning",
    "1485": "statement_subtle_inversion",
    "1532": "distractor_by_topic_association",
    "1533": "technical_vs_common_meaning",
    "1573": "statement_partial_truth",
    "1598": "statement_subtle_inversion",
    "1599": "technical_vs_common_meaning",
    "1600": "statement_subtle_inversion",
    "1631": "statement_subtle_inversion",
    "1632": "statement_subtle_inversion",
    "1661": "statement_subtle_inversion",
    "1683": "statement_subtle_inversion",
    "1684": "distractor_by_topic_association",
    "1730": "distractor_by_topic_association",
    "1731": "statement_subtle_inversion",
    "1882": "distractor_by_topic_association",
    "1883": "geographic_attribution",
    "1884": "geographic_attribution",
    "1920": "numerical_proximity",
    "1959": "famous_association_bias",
    "2080": "geographic_attribution",
    "2135": "statement_partial_truth",
    "2177": "overlapping_categories",
    "2178": "statement_subtle_inversion",
    "2179": "geographic_attribution",
    "2180": "distractor_by_topic_association",
    "2258": "distractor_by_topic_association",
    "2259": "distractor_by_topic_association",
    "2260": "statement_subtle_inversion",
    "2261": "statement_subtle_inversion",
    "2262": "period_attribution",
    "2297": "statement_partial_truth",
    "2298": "statement_partial_truth",
    "2299": "statement_partial_truth",
    "2300": "statement_subtle_inversion",
    "2328": "overlapping_categories",
    "2329": "overlapping_categories",
    "2330": "statement_subtle_inversion",
    "2331": "statement_subtle_inversion",
    "2480": "statement_subtle_inversion",
    "2481": "statement_subtle_inversion",
    "2482": "statement_subtle_inversion",
    "2483": "statement_partial_truth",
    "2514": "statement_partial_truth",
    "2515": "famous_association_bias",
    "2591": "negation_trap",
    "2592": "statement_subtle_inversion",
    "2593": "technical_vs_common_meaning",
    "2647": "distractor_by_topic_association",
    "2663": "statement_subtle_inversion",
    "2699": "negation_trap",
    "2725": "geographic_attribution",
    "2750": "distractor_by_topic_association",
}


# Discrimination cards — drafted by Sonnet agents, merged by Opus.
DISCRIMINATION_CARDS: dict = {
}


# Merge overlays (cards drafted by Sonnet, written to scratch JSON). Any
# wave1_*.json / wave2_*.json picked up automatically.
_SCRATCH = ROOT / ".scratch" / "drill_2019"
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
