#!/usr/bin/env python3
"""
Generate app/pwa/data/drill_clusters_2021.json
       + app/pwa/data/discrimination_cards_2021.json

Cluster map covers all 101 GS1 2021 PYQs. Clusters + trap tags drafted by
Sonnet pre-step agents (cluster + trap-tag), Opus consolidated 41→36 clusters.
Discrimination cards drafted by parallel Sonnet batches; auto-overlay loader
picks up calibration_cards.json + wave1*.json + wave2*.json from
.scratch/drill_2021/.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "pwa" / "data" / "pyq_index.json"
OUT_CLUSTERS = ROOT / "pwa" / "data" / "drill_clusters_2021.json"
OUT_CARDS = ROOT / "pwa" / "data" / "discrimination_cards_2021.json"

YEAR = 2021

# Cluster definitions for all 101 2021 PYQs.
# Format: (cluster_id, title, subject_focus, study_keywords[], common_traps[], pyq_ids[])
CLUSTERS: list = [
    # --- Art and Culture (3 PYQs, 1 cluster) ---
    ("art_tribal_languages_awards", "Art & Culture: Tribal Languages, National Awards & International Language Day", "Art and Culture",
     ["tribal languages India Halbi Ho Kui Oraon",
      "Bharat Ratna Padma Awards Article 18 titles constitution",
      "International Mother Language Day UNESCO February 21 Bengali Pakistan"],
     ["statement_partial_truth", "famous_association_bias"],
     [37, 38, 39]),

    # --- Ancient Indian History (7 PYQs, 4 clusters) ---
    ("anc_archaeological_sites_architecture", "Ancient India: Archaeological Sites & Architecture — Burzahom, Ajanta, Chausath Yogini, Dholavira", "Ancient Indian History",
     ["Burzahom neolithic site Kashmir pit dwellings",
      "Chandraketugarh terracotta Bengal ancient art",
      "Ganeshwar copper hoard Rajasthan chalcolithic",
      "Ajanta Caves Waghora river Maharashtra Buddhist",
      "Chausath Yogini Temple Morena Kachchhapaghata circular",
      "Dholavira Harappan water harvesting reservoirs"],
     ["geographic_attribution", "statement_partial_truth", "famous_association_bias"],
     [68, 134, 135, 136]),
    ("anc_post_gupta_kingdoms", "Ancient India: Post-Gupta Northern Kingdoms — Pushyabhutis, Maukharis, Maitrakas", "Ancient Indian History",
     ["post-Gupta kingdoms North India Harshavardhana",
      "Pushyabhuti dynasty Thanesar Maukhari Kanauj",
      "Maitraka dynasty Valabhi Gujarat early medieval"],
     ["period_attribution", "overlapping_categories"],
     [112]),
    ("anc_literature_law", "Ancient India: Literature, Drama & Inheritance Law — Bhavabhuti, Mitakshara vs Dayabhaga", "Ancient Indian History",
     ["Bhavabhuti Hastimalla Kshemeshvara ancient Indian playwrights",
      "Mitakshara Dayabhaga Hindu law inheritance property rights",
      "joint family property sons right lifetime death"],
     ["statement_partial_truth", "statement_subtle_inversion"],
     [182, 211]),

    # --- Medieval Indian History (5 PYQs, 2 clusters) ---
    ("med_mughal_admin_invasions", "Medieval India: Mughal Administrative Units & Mongol/Timurid Invasions", "Medieval Indian History",
     ["Mughal administrative divisions Paragana Sarkar Suba hierarchy",
      "Chengiz Khan Khwarezm Iltutmish Delhi Sultanate",
      "Taimur invasion Multan Muhammad bin Tughluq"],
     ["period_attribution", "overlapping_categories"],
     [251, 252]),
    ("med_european_contact_travellers", "Medieval India: European Contact, Travellers & Accounts — EIC Factories, Francis Xavier, Vijayanagara per Nuniz", "Medieval Indian History",
     ["English East India Company factories Broach 17th century",
      "Francis Xavier Jesuit Order Goa founding members",
      "St Francis Xavier feast Goa church death",
      "Vijayanagara Empire women roles Portuguese account Nuniz",
      "Domingo Paes Nuniz Portuguese travellers Vijayanagara"],
     ["person_attribution", "statement_partial_truth", "statement_subtle_inversion"],
     [313, 314, 324]),

    # --- Modern Indian History (8 PYQs, 4 clusters) ---
    ("mod_successor_states_18c", "Modern India: Successor States — Arcot, Mysore, Rohilkhand Origins", "Modern Indian History",
     ["Nizamat Arcot Hyderabad Mughal successor states",
      "Mysore Kingdom Vijayanagara Empire origin",
      "Rohilkhand Ahmad Shah Durrani Afghan territories"],
     ["statement_subtle_inversion", "geographic_attribution"],
     [354]),
    ("mod_constitutional_acts_women", "Modern India: Constitutional Acts — Montagu-Chelmsford Reforms & Women's Representation", "Modern Indian History",
     ["Montagu-Chelmsford Reforms 1919 women voting rights",
      "Government of India Act 1935 women reserved seats legislature",
      "dyarchy provincial subjects transferred reserved"],
     ["statement_overgeneralization", "statement_partial_truth"],
     [463, 536]),
    ("mod_quit_india_ina", "Modern India: Quit India Movement & Indian National Army", "Modern Indian History",
     ["Quit India Resolution August 8 1942 AICC Bombay",
      "Indian National Army INA officers Shah Nawaz Prem Kumar Gurbaksh",
      "INA trials Red Fort 1945 colonial India"],
     ["period_attribution", "distractor_by_topic_association"],
     [554, 555]),
    ("mod_nationalism_literature", "Modern India: Nationalist Literature & Personalities — Gandhi, Tagore, Vidyasagar", "Modern Indian History",
     ["Gandhi Songs from Prison ancient Indian religious lyrics translation",
      "Rabindranath Tagore Jana Gana Mana English translation Madanapalle",
      "Ishwar Chandra Vidyasagar Bethune Female School Hindu Female School"],
     ["person_attribution", "geographic_attribution", "famous_association_bias"],
     [617, 618, 650]),

    # --- Indian Polity (18 PYQs, 7 clusters) ---
    ("pol_political_theory", "Indian Polity: Political Theory — Definition of State, Liberty & Constitutional Government", "Indian Polity",
     ["definition of state political science territory sovereignty government",
      "safeguard of liberty separation of powers democracy",
      "constitutional government limited government definition"],
     ["technical_vs_common_meaning", "famous_association_bias"],
     [669, 670, 671]),
    ("pol_federal_parliamentary_preamble", "Indian Polity: Federal & Parliamentary Structure — Britain Comparison, Citizenship & Preamble", "Indian Polity",
     ["India vs British Parliament supremacy limited powers Constitution",
      "federal character India independent judiciary essential feature",
      "Indian citizenship single domicile foreigner deprivation",
      "India constitutional status January 26 1950 sovereign democratic republic",
      "Preamble India socialist secular 42nd amendment 1976"],
     ["statement_subtle_inversion", "overlapping_categories", "period_attribution"],
     [694, 695, 696, 713]),
    ("pol_fundamental_rights_articles", "Indian Polity: Fundamental Rights — Articles 14, 21, Property Right & Judicial Custody", "Indian Polity",
     ["Right to Privacy Article 21 Constitution India Puttaswamy judgment",
      "judicial custody police custody magistrate remand",
      "Right to Property Article 300A legal right not fundamental",
      "Article 14 equality arbitrary legislation unguided discretion"],
     ["overlapping_categories", "statement_subtle_inversion", "technical_vs_common_meaning"],
     [751, 752, 754, 755]),
    ("pol_parole_dpsp", "Indian Polity: Parole Rules, DPSPs & Concentration of Wealth", "Indian Polity",
     ["parole prisoner right state rules Prisoners Release on Parole",
      "DPSP Directive Principles concentration of wealth Article 39",
      "welfare state DPSP vs Fundamental Rights"],
     ["statement_subtle_inversion", "overlapping_categories"],
     [753, 773]),
    ("pol_executive_forest_rights", "Indian Polity: Union Executive — Administrative Reform & Forest Rights Act Ministry", "Indian Polity",
     ["Gopalaswamy Iyengar Committee administrative reform India",
      "Department of Personnel Administrative Reforms Commission 1966",
      "Forest Rights Act 2006 nodal ministry Tribal Affairs"],
     ["person_attribution", "distractor_by_topic_association"],
     [794, 795]),
    ("pol_judiciary_elections", "Indian Polity: Judiciary — Retired SC Judges, HC Review Powers & Lok Sabha Constituencies", "Indian Polity",
     ["retired Supreme Court judge recalled ad hoc Chief Justice President",
      "High Court review own judgment power India",
      "Lok Sabha election constituencies candidate limit ROPA"],
     ["statement_subtle_inversion"],
     [919, 954]),
    ("pol_international_rights", "Indian Polity: International Human Rights — Right to the City & UN-Habitat", "Indian Polity",
     ["Right to the City UN-Habitat human rights urban spaces",
      "public spaces participation unauthorised colonies services city",
      "UN-Habitat commitments monitoring countries urban rights"],
     ["statement_overgeneralization"],
     [1007]),

    # --- Indian Economy (15 PYQs, 6 clusters) ---
    ("eco_macroeconomy_demand", "Indian Economy: Macroeconomics — Recession Policy & Market Demand Determinants", "Indian Economy",
     ["economic recession fiscal policy public expenditure monetary response",
      "market demand substitute complement inferior good price changes",
      "demand-supply curve determinants macroeconomic theory"],
     ["technical_vs_common_meaning", "statement_subtle_inversion"],
     [1097, 1098]),
    ("eco_taxation_black_money", "Indian Economy: Taxation — Black Money & Tax Evasion", "Indian Economy",
     ["black money India tax evasion revenue loss state exchequer",
      "parallel economy unaccounted money real estate investments",
      "demonetisation black money elimination India"],
     ["distractor_by_topic_association"],
     [1180]),
    ("eco_monetary_inflation", "Indian Economy: Monetary Policy — Currency Devaluation, Inflation & Money Multiplier", "Indian Economy",
     ["currency devaluation exports competitiveness trade balance India",
      "inflationary effects money creation budget deficit public debt",
      "money multiplier cash reserve ratio banking habit India",
      "demand-pull inflation fiscal stimulus purchasing power"],
     ["statement_subtle_inversion", "technical_vs_common_meaning"],
     [1205, 1206, 1207, 1208]),
    ("eco_banking_rbi", "Indian Economy: Banking — RBI Powers, Urban Cooperative Banks & Lender of Last Resort", "Indian Economy",
     ["RBI Governor appointment Central Government powers RBI Act",
      "urban cooperative banks SEBI RBI Banking Regulation Act 1966",
      "lender of last resort RBI liquidity banks emergency"],
     ["statement_subtle_inversion", "technical_vs_common_meaning"],
     [1276, 1277, 1278]),
    ("eco_capital_markets_bonds", "Indian Economy: Capital Markets — Bond Yields, FDI Instruments & Government Securities", "Indian Economy",
     ["government bond yields US Federal Reserve RBI inflation factors",
      "FDI foreign direct investment FCCB GDR FII instruments",
      "Treasury Bills retail investors demat NDS-OM RBI CDSL"],
     ["statement_partial_truth", "technical_vs_common_meaning", "statement_subtle_inversion"],
     [1342, 1343, 1344]),
    ("eco_international_labour", "Indian Economy: International Finance & Labour — Water Credit & Casual Workers", "Indian Economy",
     ["Water Credit microfinance water sanitation sector poor",
      "casual workers India EPF provident fund overtime rights",
      "wage payment bank account government notification"],
     ["statement_subtle_inversion", "statement_overgeneralization"],
     [1456, 1572]),

    # --- Geography (12 PYQs, 4 clusters) ---
    ("geo_biomes_vegetation", "Geography: Biomes & Vegetation — Savannah, Tropical Rainforest", "Geography",
     ["savannah grassland scattered trees fire grazing seasonal rainfall",
      "tropical rainforest leaf litter epiphytes climbers canopy",
      "biome characteristics vegetation types world geography"],
     ["statement_partial_truth", "overlapping_categories"],
     [1727, 1728]),
    ("geo_oceanography_water", "Geography: Oceanography — Hydrological Distribution, Ocean Minerals & Ocean Currents", "Geography",
     ["groundwater polar ice caps glaciers water distribution Earth",
      "seabed mineral exploration ISBA rare earth metals international waters",
      "ocean currents trade winds westerlies temperature eastern western"],
     ["statement_subtle_inversion", "person_attribution", "statement_partial_truth"],
     [1789, 1790, 1791]),
    ("geo_indian_landforms_rivers", "Indian Geography: Soils, Rivers & Lakes — Black Cotton Soil, Indus System, Saline Lakes, Eastern Ghats", "Geography",
     ["black cotton soil regur fissure volcanic basalt Deccan",
      "Indus river system Sutlej Chenab Jhelum Ravi tributary",
      "saline lakes Rajasthan Didwana Kuchaman Sambhar",
      "Eastern Ghats rivers Nagavali Vamsadhara origin"],
     ["geographic_attribution", "causal_correlation"],
     [1850, 1878, 1879, 1880]),
    ("geo_agriculture_crops", "Geography: Agricultural Crops — Moringa, Tamarind, Permaculture & Water Use", "Geography",
     ["moringa drumstick tree leguminous properties biofuel seeds",
      "tamarind tree origin South Asia endemic minor forest produce",
      "permaculture farming vs conventional chemical farming monoculture",
      "water-efficient crops sugarcane millet water footprint"],
     ["statement_subtle_inversion", "distractor_by_topic_association"],
     [1952, 1953, 1954]),

    # --- Environment (15 PYQs, 4 clusters) ---
    ("env_ecology_food_chains", "Environment: Ecology — Ocean Primary Producers, Biogeochemical Cycles & Detritivores", "Environment",
     ["phytoplankton cyanobacteria diatoms ocean primary producers food chain",
      "phosphorus cycle biogeochemical weathering rocks nutrient release",
      "detritivores earthworms millipedes woodlice decomposers"],
     ["overlapping_categories"],
     [2131, 2132, 2133]),
    ("env_biodiversity_organisms", "Environment: Biodiversity — Symbiosis, Defensive Behaviour, Plant ID & Filter Feeders", "Environment",
     ["symbiotic relationship cnidarians fungi protozoa lichens corals",
      "hedgehog pangolin roll up defence mechanism predators",
      "lemon grass citronella mosquito repellent natural plants",
      "filter feeder oyster bivalve aquatic organisms"],
     ["statement_partial_truth", "famous_association_bias", "overlapping_categories", "distractor_by_topic_association"],
     [2134, 2171, 2172, 2173]),
    ("env_pollution_industrial", "Environment: Industrial Pollution — Magnetite, E-waste, Copper Smelting & Furnace Oil", "Environment",
     ["magnetite particles air pollution motor vehicles brain neurodegenerative",
      "R2 Code electronics recycling responsible e-waste practices",
      "copper smelting sulphur dioxide heavy metal leaching slag",
      "furnace oil refinery sulphur emissions air pollution power plants"],
     ["statement_subtle_inversion", "technical_vs_common_meaning", "statement_partial_truth"],
     [2251, 2252, 2253, 2254]),
    ("env_climate_action", "Environment: Climate Action — Blue Carbon, NY Forest Declaration, Common Carbon Metric & Climate-Smart Agriculture", "Environment",
     ["blue carbon coastal ecosystems mangroves seagrass carbon sequestration",
      "Common Carbon Metric UNEP building operations carbon footprint",
      "New York Declaration on Forests 2014 UN Climate Summit legally binding",
      "Climate-Smart Village CCAFS climate change agriculture food security",
      "CGIAR ICRISAT Consultative Group International Agricultural Research"],
     ["technical_vs_common_meaning", "statement_subtle_inversion", "statement_partial_truth", "distractor_by_topic_association"],
     [2294, 2389, 2390, 2425]),

    # --- Science and Technology (11 PYQs, 3 clusters) ---
    ("sci_space_biotech_vaccines", "Sci-Tech: Space Measurement & Biotechnology — Light-Years, Bt Cotton & Recombinant Vaccines", "Science and Technology",
     ["light-year astronomical unit distance speed of light constant",
      "Bollgard Bt cotton genetically modified Bacillus thuringiensis",
      "recombinant vector vaccine genetic engineering bacteria virus vectors"],
     ["technical_vs_common_meaning", "distractor_by_topic_association", "statement_partial_truth"],
     [2512, 2585, 2586]),
    ("sci_physics_chemistry", "Sci-Tech: Physics & Chemistry — Sodium vs LED Lamps, Pressure Cooker, BPA & Water", "Science and Technology",
     ["sodium lamp LED street light monochromatic spectrum comparison",
      "pressure cooker steam temperature weight lid area hole",
      "Bisphenol A BPA polycarbonate plastic health concern",
      "water solvent dipolar nature hydrogen bonding chemistry"],
     ["statement_subtle_inversion", "causal_correlation", "overlapping_categories", "technical_vs_common_meaning"],
     [2625, 2626, 2645, 2646]),
    ("sci_biology_diseases", "Sci-Tech: Biology & Diseases — Microbes, Lichens, Adenovirus/Retrovirus & Mitochondrial Disease", "Science and Technology",
     ["bacteria fungi virus artificial medium culture characteristics",
      "lichen moss soil-free surface survival pioneer organisms",
      "adenovirus retrovirus DNA genome single double stranded",
      "mitochondrial disease inheritance maternal hereditary replacement therapy"],
     ["technical_vs_common_meaning", "overlapping_categories", "statement_subtle_inversion"],
     [2659, 2660, 2661, 2676]),

    # --- Current Affairs and GK (7 PYQs, 2 clusters) ---
    ("ca_international_substances", "Current Affairs & GK: International Recognition & Chemical Substances — Hyderabad Trees, Palm Oil, ACE2, Triclosan", "Current Affairs and GK",
     ["Hyderabad Tree City of the World Arbor Day Foundation FAO",
      "palm oil origin Southeast Africa biodiesel cosmetics industry",
      "ACE2 angiotensin converting enzyme COVID-19 viral entry receptor",
      "Triclosan antibacterial toiletries health risk exposure"],
     ["person_attribution", "geographic_attribution", "distractor_by_topic_association", "overlapping_categories"],
     [2749, 2800, 2801, 2802]),
    ("ca_sports_gk", "Current Affairs & GK: Sports — Laureus Awards, Tokyo Olympics & ICC Test Championship", "Current Affairs and GK",
     ["Laureus World Sports Award Tiger Woods Roger Federer Formula One",
      "Tokyo Olympics 2020 new sports climbing surfing skateboarding karate",
      "ICC World Test Championship 2021 finalists points percentage"],
     ["statement_subtle_inversion"],
     [2803, 2804, 2805]),
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
    # 2021 introduces "1)"-style numbering (vs 2022+'s "1." style); also "2 ."
    # with stray whitespace appears in some 2021 questions. Accept all three.
    has_list = (re.search(r"(^|\s)1\s*[\.\)]\s*\S", q_norm) and re.search(r"(^|\s)2\s*[\.\)]\s*\S", q_norm))
    # Multi-select options either contain "only" (2022+ style) OR digit-comma
    # patterns like "1, 2 and 5" (2021 style without the "only" qualifier).
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
TRAP_TAGS: dict = {
    "37": "distractor_by_topic_association",
    "38": "statement_subtle_inversion",
    "39": "statement_subtle_inversion",
    "68": "geographic_attribution",
    "112": "period_attribution",
    "134": "geographic_attribution",
    "135": "statement_subtle_inversion",
    "136": "famous_association_bias",
    "182": "distractor_by_topic_association",
    "211": "statement_subtle_inversion",
    "251": "overlapping_categories",
    "252": "period_attribution",
    "313": "period_attribution",
    "314": "statement_subtle_inversion",
    "324": "statement_partial_truth",
    "354": "statement_subtle_inversion",
    "463": "statement_overgeneralization",
    "536": "statement_overgeneralization",
    "554": "period_attribution",
    "555": "distractor_by_topic_association",
    "617": "person_attribution",
    "618": "geographic_attribution",
    "650": "famous_association_bias",
    "669": "technical_vs_common_meaning",
    "670": "famous_association_bias",
    "671": "technical_vs_common_meaning",
    "694": "statement_partial_truth",
    "695": "overlapping_categories",
    "696": "statement_subtle_inversion",
    "713": "period_attribution",
    "751": "overlapping_categories",
    "752": "statement_subtle_inversion",
    "753": "statement_subtle_inversion",
    "754": "overlapping_categories",
    "755": "technical_vs_common_meaning",
    "773": "overlapping_categories",
    "794": "person_attribution",
    "795": "distractor_by_topic_association",
    "919": "statement_subtle_inversion",
    "954": "statement_subtle_inversion",
    "1007": "statement_overgeneralization",
    "1097": "technical_vs_common_meaning",
    "1098": "statement_subtle_inversion",
    "1180": "distractor_by_topic_association",
    "1205": "statement_subtle_inversion",
    "1206": "technical_vs_common_meaning",
    "1207": "statement_subtle_inversion",
    "1208": "statement_subtle_inversion",
    "1276": "statement_subtle_inversion",
    "1277": "statement_subtle_inversion",
    "1278": "technical_vs_common_meaning",
    "1342": "statement_partial_truth",
    "1343": "technical_vs_common_meaning",
    "1344": "statement_subtle_inversion",
    "1456": "statement_subtle_inversion",
    "1572": "statement_overgeneralization",
    "1727": "statement_partial_truth",
    "1728": "overlapping_categories",
    "1789": "statement_subtle_inversion",
    "1790": "person_attribution",
    "1791": "statement_partial_truth",
    "1850": "causal_correlation",
    "1878": "geographic_attribution",
    "1879": "geographic_attribution",
    "1880": "geographic_attribution",
    "1952": "statement_subtle_inversion",
    "1953": "statement_subtle_inversion",
    "1954": "distractor_by_topic_association",
    "2131": "overlapping_categories",
    "2132": "overlapping_categories",
    "2133": "overlapping_categories",
    "2134": "statement_partial_truth",
    "2171": "famous_association_bias",
    "2172": "distractor_by_topic_association",
    "2173": "overlapping_categories",
    "2251": "statement_subtle_inversion",
    "2252": "technical_vs_common_meaning",
    "2253": "statement_subtle_inversion",
    "2254": "statement_partial_truth",
    "2294": "technical_vs_common_meaning",
    "2389": "distractor_by_topic_association",
    "2390": "statement_subtle_inversion",
    "2425": "statement_partial_truth",
    "2512": "technical_vs_common_meaning",
    "2585": "distractor_by_topic_association",
    "2586": "statement_partial_truth",
    "2625": "statement_subtle_inversion",
    "2626": "causal_correlation",
    "2645": "overlapping_categories",
    "2646": "technical_vs_common_meaning",
    "2659": "technical_vs_common_meaning",
    "2660": "overlapping_categories",
    "2661": "statement_subtle_inversion",
    "2676": "statement_subtle_inversion",
    "2749": "person_attribution",
    "2800": "geographic_attribution",
    "2801": "distractor_by_topic_association",
    "2802": "overlapping_categories",
    "2803": "statement_subtle_inversion",
    "2804": "statement_subtle_inversion",
    "2805": "statement_subtle_inversion",
}


# Discrimination cards — drafted by Sonnet agents, merged by Opus.
DISCRIMINATION_CARDS: dict = {
}


# Merge overlays (cards drafted by Sonnet, written to scratch JSON). Any
# calibration_cards.json / wave1_*.json / wave2_*.json picked up automatically.
_SCRATCH = ROOT / ".scratch" / "drill_2021"
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
