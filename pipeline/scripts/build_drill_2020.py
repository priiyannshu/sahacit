#!/usr/bin/env python3
"""
Generate app/pwa/data/drill_clusters_2020.json
       + app/pwa/data/discrimination_cards_2020.json

Cluster map covers all 100 GS1 2020 PYQs. Clusters + trap tags drafted by
Sonnet pre-step agents (cluster + trap-tag), Opus consolidated 39→35 clusters
(3 merges: anc rulers/dynasties/scholars singletons unified; mod_literature_swadeshi
into mod_events_movements; sci_biology into sci_space_biotech_biology).

Discrimination cards drafted by parallel Sonnet batches; auto-overlay loader
picks up wave1*.json + wave2*.json from .scratch/drill_2020/.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "pwa" / "data" / "pyq_index.json"
OUT_CLUSTERS = ROOT / "pwa" / "data" / "drill_clusters_2020.json"
OUT_CARDS = ROOT / "pwa" / "data" / "discrimination_cards_2020.json"

YEAR = 2020

# Cluster definitions for all 100 2020 PYQs.
# Format: (cluster_id, title, subject_focus, study_keywords[], common_traps[], pyq_ids[])
CLUSTERS: list = [
    # --- Ancient Indian History (10 PYQs, 4 clusters) ---
    ("anc_places_polities", "Ancient India: Famous Places, Ports & Geographic Identification", "Ancient Indian History",
     ["ancient India famous places present states Bhilsa Dwarasamudra Girinagar Sthanesvara",
      "Gupta period ports Ghantasala Kadura Chaul foreign trade"],
     ["geographic_attribution", "statement_partial_truth"],
     [82, 103]),
    ("anc_rulers_dynasties_scholars", "Ancient India: Rulers, Edicts, Dynastic Chronology & Scholar-Patron Pairs", "Ancient Indian History",
     ["Ashoka edicts religious tolerance inscriptions",
      "Pratiharas Pallavas Cholas Palas chronological order founding",
      "Mahendravarman Parantaka Gopala Bhoja dynastic timeline",
      "Panini Pushyamitra Amarasimha Harshavardhana Kalidasa Chandragupta II patrons",
      "ancient India scholars rulers association literature"],
     ["person_attribution", "period_attribution", "famous_association_bias"],
     [91, 125, 183]),
    ("anc_terms_concepts", "Ancient India: Technical Terms & Economic Concepts — Kulyavapa, Hundi", "Ancient Indian History",
     ["kulyavapa dronavapa adhavapa pataka ancient India land measurement",
      "Hundi bill of exchange post-Harsha period medieval origin",
      "ancient agrarian terms technical vs everyday meaning"],
     ["technical_vs_common_meaning", "overlapping_categories"],
     [102, 126]),
    ("anc_religion_philosophy", "Ancient India: Buddhism, Jainism & Religious Philosophy — Paramitas, Sthaviravadins, Shramana", "Ancient Indian History",
     ["paramitas Bodhisattva Buddhism perfections virtues",
      "Sthaviravadins Theravada Mahayana Lokottaravadin Mahasanghika sects",
      "Parivrajaka Shramana Upasaka Buddhist terminology wandering ascetic"],
     ["technical_vs_common_meaning", "statement_subtle_inversion"],
     [212, 213, 214]),

    # --- Medieval Indian History (1 PYQ, 1 cluster) ---
    ("med_terms_officials", "Medieval India: Administrative Terms & Officials — Aurang, Banian, Mirasidar", "Medieval Indian History",
     ["Aurang warehouse market officer East India Company",
      "Banian Indian agent intermediary trader colonial",
      "Mirasidar revenue payer hereditary land right"],
     ["overlapping_categories", "statement_partial_truth"],
     [253]),

    # --- Modern Indian History (8 PYQs, 3 clusters) ---
    ("mod_british_economic_impact", "Modern India: British Economic Policies & Industrial Revolution Impact", "Modern Indian History",
     ["Industrial Revolution impact India handicrafts ruin destruction",
      "indigo cultivation decline 20th century synthetic dye invention Germany",
      "British colonial economic policy India 19th 20th century"],
     ["causal_correlation", "famous_association_bias"],
     [355, 660]),
    ("mod_social_reform_education", "Modern India: Social Reforms, Education & Colonial Institutions — Fort William, Vital-Vidhwansak", "Modern Indian History",
     ["Fort William College Wellesley administrative training Calcutta civilians",
      "Vital-Vidhwansak Gopal Baba Walangkar untouchable journal Maharashtra",
      "social reform education colonial India 19th century"],
     ["person_attribution", "famous_association_bias"],
     [608, 651]),
    ("mod_events_movements", "Modern India: Key Events, Movements, Legal Cases & Nationalist Literature", "Modern Indian History",
     ["Rakhmabai case 1884 age of consent conjugal rights women's education",
      "Gandhi-Irwin Pact 1931 Civil Disobedience RTC ordinances police excesses",
      "Ulgulan Birsa Munda revolt 1899-1900 tribal uprising Munda",
      "Desher Katha Sakharam Ganesh Deuskar swadeshi Bengal nationalist literature"],
     ["statement_partial_truth", "statement_subtle_inversion", "geographic_attribution"],
     [402, 504, 619, 661]),

    # --- Indian Polity (18 PYQs, 7 clusters) ---
    ("pol_political_theory", "Indian Polity: Political Theory — Parliamentary System, Gandhism, Marxism, Constitutional Government", "Indian Polity",
     ["parliamentary system government definition features executive",
      "Gandhism Marxism stateless society class struggle private property comparison",
      "constitutional government limited government rule of law"],
     ["technical_vs_common_meaning", "overlapping_categories"],
     [672, 673, 674]),
    ("pol_constitution_basics", "Indian Polity: Constitution — Basic Structure, Preamble & Judicial Evolution", "Indian Polity",
     ["basic structure doctrine Kesavananda Bharati judicial evolution",
      "Preamble Constitution India legal effect part interpretation",
      "Constitution India parts schedules judicial review"],
     ["statement_subtle_inversion", "technical_vs_common_meaning"],
     [714, 715]),
    ("pol_dpsp_fundamental", "Indian Polity: DPSPs, Fundamental Rights, Welfare State & Article 17", "Indian Polity",
     ["DPSP Part IV Constitution Welfare State enforceability courts",
      "Right to Equality Article 17 untouchability Fundamental Rights category",
      "UDHR 1948 Preamble DPSPs Fundamental Duties reflection comparison"],
     ["statement_subtle_inversion", "statement_partial_truth", "overlapping_categories"],
     [756, 774, 775, 776]),
    ("pol_constitution_provisions", "Indian Polity: Constitutional Provisions — Bureaucracy, Separation of Judiciary (Article 50)", "Indian Polity",
     ["bureaucracy India characteristics public policy implementation Weber",
      "separation judiciary executive Article 50 DPSP not Preamble Seventh Schedule"],
     ["overlapping_categories", "technical_vs_common_meaning"],
     [697, 716]),
    ("pol_legislature_parliament", "Indian Polity: Parliament — Sessions, Rajya Sabha Powers, MPLADS", "Indian Polity",
     ["Parliament sessions President summon Constitution Article 85",
      "Rajya Sabha Lok Sabha equal powers amendment cut motion no-confidence",
      "MPLADS funds durable assets carry forward SC ST inspection"],
     ["statement_partial_truth", "statement_subtle_inversion"],
     [857, 858, 859]),
    ("pol_elections_bodies", "Indian Polity: Elections, Minister Eligibility & Legal Services Authority", "Indian Polity",
     ["Constitution India minister eligibility 6 months state legislature",
      "Representation People Act criminal conviction disqualification term",
      "Legal Services Authority free legal aid eligibility income threshold categories"],
     ["statement_subtle_inversion", "statement_partial_truth"],
     [955, 979]),
    ("pol_international_acts", "Indian Polity: International Agreements, Conventions & Important Acts — Hague, Aadhaar", "Indian Polity",
     ["Alma-Ata Declaration Hague Convention child abduction Talanoa Dialogue Under2 Coalition",
      "Aadhaar UIDAI metadata Consolidated Fund insurance mandatory voluntary"],
     ["overlapping_categories", "statement_subtle_inversion"],
     [1008, 1035]),

    # --- Indian Economy (20 PYQs, 7 clusters) ---
    ("eco_macroeconomy_liberalization", "Indian Economy: Post-1991 Liberalization & Rural-Urban Workforce Dynamics", "Indian Economy",
     ["1991 economic liberalization India rural urban workforce productivity shift",
      "non-farm rural economy employment post-liberalization structural change"],
     ["statement_subtle_inversion", "causal_correlation"],
     [1099]),
    ("eco_budget_fiscal", "Indian Economy: Government Budgeting & Fiscal Policy — FRBM, Non-Financial Debt", "Indian Economy",
     ["Macro Economic Framework Statement FRBM Act 2003 Parliament budget",
      "non-financial debt India housing loans credit cards treasury bills classification"],
     ["technical_vs_common_meaning", "overlapping_categories"],
     [1143, 1144]),
    ("eco_rbi_monetary", "Indian Economy: RBI & Monetary Policy — SLR/MSF, CPI vs WPI, Money Supply", "Indian Economy",
     ["RBI expansionist monetary policy SLR MSF repo rate tools",
      "global financial crisis India immunity capital account convertibility foreign banks",
      "demand deposit withdrawal aggregate money supply M1 M2",
      "CPI WPI weightage food services inflation RBI anchor"],
     ["statement_subtle_inversion", "technical_vs_common_meaning", "negation_trap"],
     [1209, 1210, 1211, 1212]),
    ("eco_banking_capital", "Indian Economy: Banking, Capital Markets & Financial Instruments — DCCB, CD, FDI, ICR", "Indian Economy",
     ["DCCB short-term credit agriculture cooperative banks SCBs comparison",
      "Certificate of Deposit Commercial Paper call money zero coupon bonds short-term",
      "FDI India non-debt creating capital flow vs FII portfolio",
      "Interest Coverage Ratio firm loan risk debt servicing ability"],
     ["statement_subtle_inversion", "technical_vs_common_meaning"],
     [1279, 1345, 1346, 1380]),
    ("eco_international_trade", "Indian Economy: International Trade, WTO & Trade Policy — TRIMS, CAD", "Indian Economy",
     ["Indo-Sri Lanka trade Bangladesh India textiles Nepal trading partner",
      "India merchandise exports imports services current account deficit CAD",
      "TRIMS WTO trade-related investment measures goods not services"],
     ["statement_partial_truth", "recency_bias", "statement_subtle_inversion"],
     [1431, 1432, 1433]),
    ("eco_international_orgs", "Indian Economy: International Economic Organisations — IMF Gold Tranche, G20", "Indian Economy",
     ["Gold Tranche Reserve Tranche IMF SDR credit facility",
      "G20 members G7 plus emerging economies Argentina Mexico South Africa Turkey"],
     ["overlapping_categories", "distractor_by_topic_association"],
     [1457, 1458]),
    ("eco_agriculture_policy", "Indian Economy: Agricultural Policy — MSP, Kisan Credit Card, Public Investment", "Indian Economy",
     ["MSP minimum support price cereals pulses oilseeds procurement limits",
      "Kisan Credit Card short-term credit working capital consumption post-harvest",
      "public investment agriculture cold storage social capital vs price support",
      "rice price MSP government stockpiling consumer subsidies"],
     ["statement_subtle_inversion", "overlapping_categories", "statement_overgeneralization", "statement_partial_truth"],
     [1594, 1595, 1596, 1597]),

    # --- Geography (10 PYQs, 4 clusters) ---
    ("geo_climatology_oceanography", "Geography: Climatology — Jet Streams & Ocean Mean Temperature (OMT)", "Geography",
     ["jet streams Northern Southern Hemisphere westerlies cyclone formation",
      "Ocean Mean Temperature OMT Indian Ocean monsoon prediction 26C isotherm depth"],
     ["statement_overgeneralization", "statement_subtle_inversion"],
     [1729, 1792]),
    ("geo_landforms_minerals", "Geography: Landforms, Glaciers & Major vs Minor Minerals — Siachen, Kyanite", "Geography",
     ["Siachen Glacier location Nubra Valley Ladakh Aksai Chin Karakoram",
      "major minerals India Kyanite Sillimanite vs Bentonite Chromite minor classification"],
     ["geographic_attribution", "overlapping_categories"],
     [1827, 1851]),
    ("geo_rivers_water", "Geography: Rivers, Groundwater & Water Resources — CGWA, World Rivers", "Geography",
     ["India groundwater irrigation overexploited districts CGWA Environment Protection Act",
      "world rivers Mekong Thames Volga Zambezi outlets seas oceans"],
     ["geographic_attribution", "statement_partial_truth"],
     [1881, 2079]),
    ("geo_agriculture_crops", "Geography: Agriculture — Fertigation, Pulses, Cotton & Sugarcane Cultivation", "Geography",
     ["fertigation efficiency soluble nutrients rock phosphate alkalinity",
      "pulse production India black gram green gram kharif rabi proportion",
      "cotton subtropical crop frost-free days light well-drained soil",
      "sugarcane cultivation single-budded multi-budded setts germination tissue culture"],
     ["statement_subtle_inversion", "distractor_by_topic_association", "statement_partial_truth"],
     [1955, 1956, 1957, 1958]),

    # --- Environment (18 PYQs, 6 clusters) ---
    ("env_biodiversity_wildlife", "Environment: Biodiversity — Indian Elephants, Birds & Musk Deer Habitat", "Environment",
     ["Indian elephants gestation 22 months calving population Kerala Karnataka Tamil Nadu",
      "Ceylon frogmouth Coppersmith barbet Indian roller Spotbilled pelican birds identification",
      "musk deer habitat Askot Gangotri high Himalayan alpine zone"],
     ["statement_subtle_inversion", "overlapping_categories", "geographic_attribution"],
     [2174, 2175, 2176]),
    ("env_pollution_waste", "Environment: Pollution, Industrial By-products — Benzene, Coal Ash, Steel Slag", "Environment",
     ["benzene pollution sources automobile exhaust tobacco wood-burning polyurethane",
      "coal ash arsenic lead mercury power plant pollutants sulphur",
      "steel slag uses road construction agricultural soil cement industry"],
     ["statement_partial_truth", "overlapping_categories"],
     [2255, 2256, 2257]),
    ("env_climate_green", "Environment: Climate Change, Carbon Footprint & Social Cost of Carbon", "Environment",
     ["rural road construction copper slag cold mix asphalt geotextiles low-carbon vs Portland cement",
      "Social Cost of Carbon SCC CO2 emissions monetary economic value definition"],
     ["overlapping_categories", "technical_vs_common_meaning"],
     [2295, 2296]),
    ("env_protected_areas", "Environment: Protected Areas, Tiger Reserves, Schedule VI Plants & Critical Habitats", "Environment",
     ["Desert National Park Rajasthan Great Indian Bustard Jaisalmer villages",
      "Critical Tiger Habitat Nagarjunasagar-Srisailam largest Sundarbans Corbett Ranthambore",
      "Schedule VI Wildlife Protection Act plants licence cultivation",
      "Cauvery basin protected areas Nagarhole Sathyamangalam Mudumalai not Papikonda Godavari",
      "barasingha swamp deer Kanha graminivorous hard ground subspecies"],
     ["statement_partial_truth", "famous_association_bias", "geographic_attribution", "technical_vs_common_meaning"],
     [2323, 2324, 2325, 2326, 2327]),
    ("env_sustainable_agriculture", "Environment: Sustainable Agriculture — Zero Tillage, Eco-Farming, Biochar", "Environment",
     ["zero tillage agriculture wheat paddy carbon sequestration direct planting",
      "eco-friendly agriculture crop diversification legume tensiometer vertical farming",
      "biochar growing medium soil structure water retention nitrogen-fixing microorganisms"],
     ["statement_partial_truth", "statement_subtle_inversion"],
     [2426, 2427, 2428]),
    ("env_renewable_biofuel", "Environment: Renewable Energy — Biofuels & Solar Pumps", "Environment",
     ["National Policy Biofuels India raw materials non-food cassava sugar beet damaged crops",
      "solar water pumps surface submersible centrifugal piston suitability"],
     ["overlapping_categories", "statement_subtle_inversion"],
     [2453, 2454]),

    # --- Science and Technology (11 PYQs, 2 clusters) ---
    ("sci_electronics_it", "S&T: Electronics, AI, Drones, Blockchain, VLC & Cyber Insurance", "Science and Technology",
     ["drones UAV pesticide spraying volcano inspection whale DNA recovery",
      "Artificial Intelligence capabilities disease diagnosis text-to-speech wireless energy",
      "Visible Light Communication VLC short-range optical wireless spectrum",
      "Blockchain technology distributed ledger cryptocurrency general-purpose",
      "cyber insurance India coverage malware extortion physical damage exclusions"],
     ["statement_partial_truth", "statement_subtle_inversion", "technical_vs_common_meaning"],
     [2475, 2476, 2477, 2478, 2479]),
    ("sci_space_biotech_biology", "S&T: Space (LISA), Biotech (Carbon Nanotubes, Genome Editing, Vaccines, Pronuclear Transfer) & Cell Biology", "Science and Technology",
     ["LISA Pathfinder Evolved LISA gravitational waves spacecraft trio laser triangle",
      "carbon nanotubes drug delivery blood capillary biodegradable property",
      "genome editing germline cells embryo stem cells pig reproductive",
      "Pneumococcal Conjugate Vaccine pneumonia meningitis sepsis side effects",
      "Pronuclear Transfer mitochondrial disease prevention IVF defective DNA",
      "plant cell animal cell differences cellulose plasma membrane vacuole"],
     ["famous_association_bias", "statement_subtle_inversion", "statement_overgeneralization", "technical_vs_common_meaning", "statement_partial_truth"],
     [2513, 2587, 2588, 2589, 2590, 2662]),

    # --- Current Affairs and GK (4 PYQs, 1 cluster) ---
    ("ca_nuclear_security_commodities", "Current Affairs: IAEA Nuclear Safeguards, PKI Security, WTI Crude & Chemical Fertilizers", "Current Affairs and GK",
     ["IAEA safeguards nuclear reactors India imported domestic uranium NPT non-proliferation",
      "Public Key Infrastructure PKI digital security cryptography",
      "West Texas Intermediate WTI crude oil grade benchmark Brent comparison",
      "chemical fertilizers India urea ammonia natural gas DAP government-administered price"],
     ["technical_vs_common_meaning", "distractor_by_topic_association", "statement_subtle_inversion"],
     [2724, 2806, 2807, 2808]),
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
# Opus retags applied: 716 (geographic_attribution → overlapping_categories;
# trap is Preamble vs Seventh Schedule vs Article 50 — categorical confusion,
# not geographic), 2589 (statement_partial_truth → statement_overgeneralization;
# the false statement is the absolute "no side effects, no allergic reactions"
# overreach pattern, sharper than partial_truth structural tag), 2428
# (statement_subtle_inversion → statement_partial_truth; UPSC ans (d) treats
# all three biochar statements as true, so the trap is subset-selection, not
# inversion — caught during Phase 2 QC of Sonnet's drafted card).
TRAP_TAGS: dict = {
    "82": "geographic_attribution",
    "91": "person_attribution",
    "102": "technical_vs_common_meaning",
    "103": "overlapping_categories",
    "125": "period_attribution",
    "126": "technical_vs_common_meaning",
    "183": "person_attribution",
    "212": "technical_vs_common_meaning",
    "213": "statement_subtle_inversion",
    "214": "statement_subtle_inversion",
    "253": "overlapping_categories",
    "355": "statement_subtle_inversion",
    "402": "statement_partial_truth",
    "504": "statement_partial_truth",
    "608": "person_attribution",
    "619": "statement_partial_truth",
    "651": "person_attribution",
    "660": "causal_correlation",
    "661": "distractor_by_topic_association",
    "672": "technical_vs_common_meaning",
    "673": "overlapping_categories",
    "674": "technical_vs_common_meaning",
    "697": "technical_vs_common_meaning",
    "714": "statement_subtle_inversion",
    "715": "statement_subtle_inversion",
    "716": "overlapping_categories",
    "756": "overlapping_categories",
    "774": "overlapping_categories",
    "775": "statement_subtle_inversion",
    "776": "statement_partial_truth",
    "857": "statement_partial_truth",
    "858": "overlapping_categories",
    "859": "statement_partial_truth",
    "955": "statement_subtle_inversion",
    "979": "statement_partial_truth",
    "1008": "geographic_attribution",
    "1035": "statement_subtle_inversion",
    "1099": "statement_subtle_inversion",
    "1143": "technical_vs_common_meaning",
    "1144": "overlapping_categories",
    "1209": "statement_partial_truth",
    "1210": "technical_vs_common_meaning",
    "1211": "statement_subtle_inversion",
    "1212": "negation_trap",
    "1279": "statement_subtle_inversion",
    "1345": "statement_subtle_inversion",
    "1346": "technical_vs_common_meaning",
    "1380": "statement_subtle_inversion",
    "1431": "recency_bias",
    "1432": "statement_partial_truth",
    "1433": "statement_subtle_inversion",
    "1457": "overlapping_categories",
    "1458": "distractor_by_topic_association",
    "1594": "overlapping_categories",
    "1595": "statement_partial_truth",
    "1596": "statement_partial_truth",
    "1597": "statement_overgeneralization",
    "1729": "statement_overgeneralization",
    "1792": "statement_subtle_inversion",
    "1827": "geographic_attribution",
    "1851": "overlapping_categories",
    "1881": "statement_partial_truth",
    "1955": "statement_subtle_inversion",
    "1956": "statement_subtle_inversion",
    "1957": "distractor_by_topic_association",
    "1958": "statement_partial_truth",
    "2079": "geographic_attribution",
    "2174": "statement_subtle_inversion",
    "2175": "overlapping_categories",
    "2176": "geographic_attribution",
    "2255": "statement_partial_truth",
    "2256": "statement_partial_truth",
    "2257": "statement_partial_truth",
    "2295": "overlapping_categories",
    "2296": "technical_vs_common_meaning",
    "2323": "statement_partial_truth",
    "2324": "famous_association_bias",
    "2325": "technical_vs_common_meaning",
    "2326": "geographic_attribution",
    "2327": "famous_association_bias",
    "2426": "statement_partial_truth",
    "2427": "statement_partial_truth",
    "2428": "statement_partial_truth",
    "2453": "overlapping_categories",
    "2454": "statement_subtle_inversion",
    "2475": "statement_partial_truth",
    "2476": "statement_subtle_inversion",
    "2477": "statement_subtle_inversion",
    "2478": "statement_subtle_inversion",
    "2479": "statement_partial_truth",
    "2513": "famous_association_bias",
    "2587": "statement_subtle_inversion",
    "2588": "statement_partial_truth",
    "2589": "statement_overgeneralization",
    "2590": "technical_vs_common_meaning",
    "2662": "statement_subtle_inversion",
    "2724": "technical_vs_common_meaning",
    "2806": "technical_vs_common_meaning",
    "2807": "distractor_by_topic_association",
    "2808": "statement_subtle_inversion",
}


# Discrimination cards — drafted by Sonnet agents, merged by Opus.
DISCRIMINATION_CARDS: dict = {
}


# Merge overlays (cards drafted by Sonnet, written to scratch JSON). Any
# wave1_*.json / wave2_*.json picked up automatically.
_SCRATCH = ROOT / ".scratch" / "drill_2020"
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
