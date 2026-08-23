#!/usr/bin/env python3
"""
Generate app/pwa/data/drill_clusters_2023.json
       + app/pwa/data/discrimination_cards_2023.json

Cluster map covers all 100 GS1 2023 PYQs. Clusters + trap tags drafted by
Sonnet (pre-step agents 2026-04-25); Opus consolidated 53 → 43 clusters.
Discrimination cards drafted by parallel Sonnet batches.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "pwa" / "data" / "pyq_index.json"
OUT_CLUSTERS = ROOT / "pwa" / "data" / "drill_clusters_2023.json"
OUT_CARDS = ROOT / "pwa" / "data" / "discrimination_cards_2023.json"

YEAR = 2023

# Cluster definitions for all 100 2023 PYQs. 43 clusters after Opus consolidation.
# Format: (cluster_id, title, subject_focus, study_keywords[], common_traps[], pyq_ids[])
CLUSTERS = [
    # --- Ancient History (9 PYQs) ---
    ("anc_south_polities_dynasties", "Ancient/Early Medieval: Ports, Polities & Dynasty Dating", "Ancient Indian History",
     ["Korkai Poompuhar Muchiri ancient Tamil ports",
      "Sangam age trade South India",
      "Hoysala Kakatiya Yadava Gahadavala founding periods",
      "early medieval Indian dynasties 8th-12th century timeline"],
     ["geographic_attribution", "period_attribution"],
     [66, 67]),
    ("anc_cave_shrines_sites", "Ancient India: Cave Shrines & Archaeological Sites", "Ancient Indian History",
     ["Besnagar Bhaja Sittanavasal cave shrines religious identity",
      "Buddhist Jain Vaishnava Shaivite cave temples India",
      "Heliodorus pillar Besnagar Vidisha"],
     ["geographic_attribution", "statement_subtle_inversion"],
     [129, 130]),
    ("anc_literature_authorship", "Ancient India: Literary Works & Authors", "Ancient Indian History",
     ["Devichandragupta Hammira-Mahakavya Milinda-panha authors",
      "Bilhana Nayachandra Suri Nagarjuna Somadeva Suri works",
      "ancient Indian literary text author matching"],
     ["person_attribution", "famous_association_bias"],
     [179, 180]),
    ("anc_religion_buddhism_jainism", "Ancient India: Buddhism, Jainism & Stupa Architecture", "Ancient Indian History",
     ["Stupa origin Buddhist tradition relics votive",
      "Jain animism souls doctrine",
      "Dhanyakataka Mahasanghika Buddhist centre Andhra",
      "Buddhist architecture stupa chaitya vihara"],
     ["statement_partial_truth", "overlapping_categories"],
     [131, 206, 207]),

    # --- Medieval History (2 PYQs) ---
    ("med_vijayanagara_irrigation", "Medieval India: Vijayanagara Empire & Hydraulic Works", "Medieval Indian History",
     ["Devaraya I Tungabhadra dam Vijayanagara",
      "Vijayanagara rulers irrigation canal aqueduct"],
     ["person_attribution", "period_attribution"],
     [247]),
    ("med_advent_europeans", "Medieval India: Advent of Europeans & Portuguese", "Medieval Indian History",
     ["Bahadur Shah Gujarat Portuguese Diu surrender",
      "Portuguese India medieval period Diu Goa"],
     ["person_attribution", "period_attribution"],
     [311]),

    # --- Modern History (2 PYQs) ---
    ("mod_colonial_acts_and_movement", "Modern India: Charter Acts & Swadeshi Movement", "Modern Indian History",
     ["Charter Act 1833 Governor General of India designation",
      "Regulating Act Pitt's India Act Charter Acts comparison",
      "Swadeshi Movement 1905 Bengal Partition",
      "National Handloom Day August 7 origin"],
     ["period_attribution", "causal_correlation"],
     [353, 421]),

    # --- Indian Polity (15 PYQs) ---
    ("pol_constitutional_theory_day", "Indian Polity: Constitutional Theory, Due Process & Constitution Day", "Indian Polity",
     ["Due Process of Law vs Procedure Established by Law India",
      "purpose of Constitution limiting government powers",
      "Constitution Day November 26 Constituent Assembly Drafting Committee"],
     ["technical_vs_common_meaning", "statement_subtle_inversion"],
     [667, 668, 710]),
    ("pol_reservations_article16_335", "Indian Polity: Reservations, Article 16 & Article 335", "Indian Polity",
     ["Article 16(4) reservation Article 335 efficiency of administration",
      "Supreme Court reservation jurisprudence India",
      "SC ST reservation constitutional provisions Article 335"],
     ["statement_subtle_inversion", "explanatory_chain"],
     [750]),
    ("pol_president_election", "Indian Polity: Presidential Election & Electoral College", "Indian Polity",
     ["Presidential election Electoral College nominated members",
      "MLA vote value formula President election India",
      "President election void consequences assent time limit"],
     ["statement_subtle_inversion", "numerical_proximity"],
     [827, 828]),
    ("pol_parliament_money_bill", "Indian Polity: Finance Bill vs Money Bill", "Indian Polity",
     ["Finance Bill vs Money Bill Rajya Sabha powers India",
      "Money Bill joint sitting Parliament India",
      "Article 110 Money Bill definition"],
     ["overlapping_categories", "negation_trap"],
     [853]),
    ("pol_constitutional_vs_statutory_bodies", "Indian Polity: Constitutional vs Statutory Bodies", "Indian Polity",
     ["NCBC NHRC NLC NCDRC constitutional vs statutory",
      "National Commission Backward Classes 102nd Amendment",
      "constitutional body examples India"],
     ["overlapping_categories", "famous_association_bias"],
     [976]),
    ("pol_finance_commission_devolution", "Indian Polity: Finance Commission & Tax Devolution", "Indian Polity",
     ["15th Finance Commission horizontal devolution criteria",
      "demographic performance forest governance tax criteria",
      "Finance Commission tax devolution India"],
     ["numerical_proximity", "statement_partial_truth"],
     [977]),
    ("pol_amendments_flag_symbols", "Indian Polity: Key Amendments & National Flag Code", "Indian Polity",
     ["1st Amendment 1951 judicial review fundamental rights",
      "Flag Code India 2002 standard sizes ratio",
      "National Flag India dimensions 3:2 ratio"],
     ["first_or_only", "explanatory_chain"],
     [1029, 1034]),
    ("pol_security_law_acts", "Indian Polity: Security Laws & Acts", "Indian Polity",
     ["Prisons India state subject Prison Act 1894",
      "preventive detention legal counsel Constitution India",
      "POTA 2002 confession police evidence",
      "Home Guards Act Central vs State government",
      "Official Secrets Act Arms Amendment Act India"],
     ["statement_subtle_inversion", "explanatory_chain"],
     [1030, 1031, 1032, 1033]),

    # --- Indian Economy (16 PYQs) ---
    ("eco_monetary_policy_inflation", "Indian Economy: Monetary Policy & Inflation Control", "Indian Economy",
     ["Central bank interest rate hikes post-pandemic inflation",
      "RBI monetary policy transmission India",
      "RBI sterilization Open Market Operations"],
     ["causal_correlation", "explanatory_chain"],
     [1095, 1200]),
    ("eco_banking_msme_shg_cbdc", "Indian Economy: Banking — MSME, SHG & CBDC", "Indian Economy",
     ["MSMED Act 2006 medium enterprise investment limit",
      "Self-Help Group SHG NABARD microcredit origin",
      "Central Bank Digital Currency CBDC programmable money",
      "Priority sector lending India"],
     ["statement_subtle_inversion", "statement_partial_truth"],
     [1271, 1272, 1273]),
    ("eco_capital_markets_instruments", "Indian Economy: Capital Markets & Financial Instruments", "Indian Economy",
     ["Capital market vs money market: G-Secs treasury bills",
      "Beta volatility measure stock market",
      "Capital market instrument classification India"],
     ["overlapping_categories", "technical_vs_common_meaning"],
     [1337, 1338]),
    ("eco_infra_intangibles_pli", "Indian Economy: Infrastructure, Intangibles & PLI", "Indian Economy",
     ["InvIT Infrastructure Investment Trust tax dividend",
      "Intangible investments brand IP mailing list",
      "Coal thermal power seawater water-stressed districts",
      "Production Linked Incentive PLI scheme exports"],
     ["technical_vs_common_meaning", "overlapping_categories"],
     [1374, 1375, 1376, 1430]),
    ("eco_health_welfare_schemes", "Indian Economy: Health Policy & Welfare Schemes", "Indian Economy",
     ["India public health curative vs preventive care",
      "Janani Suraksha Yojana JSY neonatal maternal mortality",
      "Anaemia Mukt Bharat calcium cord clamping deworming"],
     ["statement_partial_truth", "statement_overgeneralization"],
     [1527, 1528, 1529]),
    ("eco_agriculture_farming", "Indian Economy: Agriculture — Farming Models & Crops", "Indian Economy",
     ["Small Farmer Large Field synchronized operations",
      "Niger seed Guizotia abyssinica MSP kharif",
      "Cooperative collective farming India"],
     ["technical_vs_common_meaning", "statement_partial_truth"],
     [1591, 1592]),

    # --- Geography (15 PYQs) ---
    ("geo_minerals_seismic", "Physical Geography: Coastal Minerals & Seismic Waves", "Geography",
     ["Ilmenite rutile titanium coastal India heavy minerals",
      "P waves S waves seismograph earthquake",
      "Coastal placer deposits India"],
     ["technical_vs_common_meaning", "famous_association_bias"],
     [1680, 1681]),
    ("geo_climatology_atmosphere_ocean", "Climatology & Oceanography: Atmosphere, Insolation & Heat Capacity", "Geography",
     ["Insolation equator poles distribution infrared",
      "Infrared waves water vapour atmospheric absorption",
      "Tropical rainforest soil nutrients decomposition",
      "Specific heat water land continent ocean temperature"],
     ["statement_subtle_inversion", "explanatory_chain"],
     [1724, 1725, 1788]),
    ("geo_indian_hills_landforms", "Indian Geography: Hills, Ranges & Marshlands", "Geography",
     ["Amarkantak Vindhya Satpura junction",
      "Biligirirangan Seshachalam hills location",
      "Rann of Kutch sea level marsh formation"],
     ["geographic_attribution", "technical_vs_common_meaning"],
     [1825, 1919]),
    ("geo_rivers_lakes_india", "Indian Geography: Rivers & Lakes", "Geography",
     ["Jhelum Wular Krishna Kolleru Gandak Kanwar",
      "Indian lakes feeder rivers"],
     ["geographic_attribution", "famous_association_bias"],
     [1875]),
    ("geo_india_china_world_map", "Geography: India-China Comparison & World Borders", "Geography",
     ["India China arable land irrigated area productivity",
      "Ukraine land border EU member countries",
      "Europe map borders geography"],
     ["statement_subtle_inversion", "numerical_proximity"],
     [1950, 2077]),
    ("geo_connectivity_corridors", "Indian Geography: Highways, Corridors & Ports", "Geography",
     ["East-West Corridor Golden Quadrilateral Dibrugarh Surat",
      "Trilateral Highway Moreh Manipur Myanmar Thailand",
      "BCIM Corridor Kunming Varanasi",
      "Kamarajar Mundra Vishakhapatnam ports"],
     ["geographic_attribution", "famous_association_bias"],
     [1994, 1995]),
    ("geo_world_resources_countries", "World Geography: Critical Minerals & Country Resources", "Geography",
     ["Congo DRC cobalt EV batteries",
      "Congo Basin countries Cameroon",
      "Switzerland gold refining reserves"],
     ["geographic_attribution", "explanatory_chain"],
     [2038, 2039, 2040]),

    # --- Environment (18 PYQs) ---
    ("env_animal_behaviour_tooluse", "Ecology: Animal Behaviour & Mushrooms", "Environment",
     ["Waggle dance honeybees food direction",
      "Orangutan tool use insects",
      "Mushrooms medicinal psychoactive bioluminescent"],
     ["famous_association_bias", "statement_overgeneralization"],
     [2127, 2128, 2129]),
    ("env_biodiversity_flora_fauna", "Biodiversity: Trees, Marsupials & Indian Fauna", "Environment",
     ["Jackfruit Mahua Teak deciduous",
      "Marsupials India habitat distribution",
      "Lion-tailed Macaque Malabar Civet Sambar nocturnal",
      "Indian squirrels nesting food storage"],
     ["overlapping_categories", "statement_subtle_inversion"],
     [2163, 2164, 2165, 2166]),
    ("env_pollution_aquaculture_mercury", "Environment: Biofilters, Mercury & Aquaculture", "Environment",
     ["Biofilter recirculating aquaculture ammonia nitrate",
      "Mercury pollution gold mining coal thermal",
      "Safe mercury exposure pollution sources"],
     ["statement_subtle_inversion", "statement_overgeneralization"],
     [2246, 2247]),
    ("env_climate_hfc_carbon_capture", "Environment: HFCs, Carbon Capture & Sequestration", "Environment",
     ["Hydrofluorocarbons HFC uses aerosols foam",
      "Carbon capture basalt ocean alkalinity subterranean",
      "Enhanced rock weathering CO2 removal"],
     ["overlapping_categories", "technical_vs_common_meaning"],
     [2291, 2292]),
    ("env_conservation_law_india", "Environment: Community Reserves & Scheduled Areas", "Environment",
     ["Community Reserve Wildlife Protection Act Chief Wildlife Warden",
      "Scheduled Areas President notification PESA",
      "Biodiversity Management Committees Nagoya Protocol ABS"],
     ["statement_subtle_inversion", "overlapping_categories"],
     [2318, 2319, 2320]),
    ("env_global_biodiversity_carbon_orgs", "Environment: IUCN & Carbon Markets", "Environment",
     ["Invasive Species Specialist Group IUCN Global Invasive Species Database",
      "Carbon markets private sector public sector",
      "IUCN conservation organisations"],
     ["overlapping_categories", "explanatory_chain"],
     [2384, 2385]),
    ("env_green_hydrogen", "Environment: Green Hydrogen & Decarbonisation", "Environment",
     ["Green hydrogen fuel cell IC engine natural gas blending",
      "Green hydrogen decarbonising fertilizer refinery steel",
      "Hydrogen economy India clean energy"],
     ["statement_subtle_inversion", "overlapping_categories"],
     [2450, 2451]),

    # --- Science & Technology (9 PYQs) ---
    ("sci_space_astronomy", "Science & Technology: Space & Astrophysics", "Science and Technology",
     ["Cepheids Nebulae Pulsars neutron stars",
      "Satellite navigation systems QZSS NavIC Japan India",
      "Space objects classification UPSC"],
     ["famous_association_bias", "statement_subtle_inversion"],
     [2508, 2509]),
    ("sci_biotech_genomics", "Science & Technology: Biotechnology & Genomics", "Science and Technology",
     ["Aerial metagenomics environmental DNA air sampling",
      "Microsatellite DNA forensic evolutionary biology",
      "Environmental DNA eDNA applications"],
     ["technical_vs_common_meaning", "distractor_by_topic_association"],
     [2580, 2581]),
    ("sci_materials_nuclear_sensors_bio", "Science & Technology: Materials, Nuclear, Sensors & Extremophiles", "Science and Technology",
     ["Accelerometer applications airbag smartphone HDD",
      "Uranium enrichment reactor grade 3-5% weapons 90%",
      "Carbon fibre automotive aerospace",
      "Extremophile microorganisms thermophiles acidophiles",
      "Wolbachia mosquito-borne disease control"],
     ["overlapping_categories", "explanatory_chain"],
     [2469, 2623, 2643, 2656, 2675]),

    # --- Current Affairs and GK (14 PYQs) ---
    ("ca_defence_missiles", "Current Affairs: Missiles & Military Tech", "Current Affairs and GK",
     ["Ballistic vs cruise missile propulsion phases",
      "Agni-V ICBM BrahMos supersonic cruise",
      "Missile classification India defence"],
     ["statement_subtle_inversion", "technical_vs_common_meaning"],
     [2707]),
    ("ca_international_orgs_treaties", "Current Affairs: International Organisations & Multilateral Frameworks", "Current Affairs and GK",
     ["G20 origin Finance Ministers Central Bank Governors India presidency",
      "UNOPS S3i Sustainable Infrastructure Investment sectors",
      "Global Compact Safe Migration GCM binding nature",
      "EU Stability Growth Pact deficit limits",
      "India groundwater UN World Water Development Report",
      "US EU Trade and Technology Council TTC goals"],
     ["statement_subtle_inversion", "explanatory_chain"],
     [2739, 2740, 2741, 2742, 2743, 2785]),
    ("ca_geopolitics_conflicts", "Current Affairs: Global Geopolitics & Conflicts", "Current Affairs and GK",
     ["Africa military coups Chad Guinea Mali Sudan",
      "Somalia famine civil strife",
      "Donbas Kachin Tigray conflict regions",
      "North Kivu Ituri Nagorno-Karabakh Kherson",
      "Israel Arab diplomatic relations Abraham Accords"],
     ["geographic_attribution", "distractor_by_topic_association"],
     [2786, 2787, 2788, 2789, 2790]),
    ("ca_sports_awards_events", "Current Affairs: Sports Awards & Events", "Current Affairs and GK",
     ["Khel Ratna Arjuna Dronacharya Rashtriya Khel Protsahan",
      "44th Chess Olympiad 2022 Thambi mascot Hamilton-Russell cup",
      "Indian sports awards criteria periods"],
     ["statement_subtle_inversion", "famous_association_bias"],
     [2791, 2792]),
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


# ---- Trap-pattern tagging (Sonnet-drafted 2026-04-25, Opus-reviewed) ----
TRAP_TAGS = {
    "66": "geographic_attribution", "67": "period_attribution",
    "129": "statement_subtle_inversion", "130": "famous_association_bias", "131": "statement_subtle_inversion",
    "179": "person_attribution", "180": "technical_vs_common_meaning",
    "206": "overlapping_categories", "207": "geographic_attribution",
    "247": "person_attribution", "311": "person_attribution",
    "353": "period_attribution", "421": "explanatory_chain",
    "667": "technical_vs_common_meaning", "668": "overlapping_categories",
    "710": "explanatory_chain", "750": "explanatory_chain",
    "827": "statement_subtle_inversion", "828": "statement_subtle_inversion",
    "853": "statement_subtle_inversion",
    "976": "overlapping_categories", "977": "numerical_proximity",
    "1029": "first_or_only", "1030": "explanatory_chain",
    "1031": "statement_subtle_inversion", "1032": "statement_subtle_inversion", "1033": "statement_subtle_inversion",
    "1034": "explanatory_chain",
    "1095": "explanatory_chain", "1200": "technical_vs_common_meaning",
    "1271": "statement_subtle_inversion", "1272": "statement_subtle_inversion", "1273": "statement_partial_truth",
    "1337": "overlapping_categories", "1338": "technical_vs_common_meaning",
    "1374": "explanatory_chain", "1375": "overlapping_categories", "1376": "statement_overgeneralization",
    "1430": "explanatory_chain",
    "1527": "explanatory_chain", "1528": "statement_subtle_inversion", "1529": "statement_subtle_inversion",
    "1591": "technical_vs_common_meaning", "1592": "statement_partial_truth",
    "1680": "famous_association_bias", "1681": "statement_subtle_inversion",
    "1724": "statement_subtle_inversion", "1725": "explanatory_chain",
    "1788": "explanatory_chain",
    "1825": "geographic_attribution", "1875": "statement_subtle_inversion",
    "1919": "technical_vs_common_meaning",
    "1950": "statement_subtle_inversion",
    "1994": "geographic_attribution", "1995": "famous_association_bias",
    "2038": "geographic_attribution", "2039": "geographic_attribution", "2040": "explanatory_chain",
    "2077": "numerical_proximity",
    "2127": "famous_association_bias", "2128": "distractor_by_topic_association", "2129": "statement_overgeneralization",
    "2163": "overlapping_categories", "2164": "explanatory_chain", "2165": "overlapping_categories", "2166": "statement_subtle_inversion",
    "2246": "statement_subtle_inversion", "2247": "statement_overgeneralization",
    "2291": "overlapping_categories", "2292": "technical_vs_common_meaning",
    "2318": "statement_subtle_inversion", "2319": "statement_subtle_inversion", "2320": "statement_subtle_inversion",
    "2384": "overlapping_categories", "2385": "explanatory_chain",
    "2450": "statement_subtle_inversion", "2451": "overlapping_categories",
    "2469": "overlapping_categories",
    "2508": "statement_subtle_inversion", "2509": "geographic_attribution",
    "2580": "technical_vs_common_meaning", "2581": "technical_vs_common_meaning",
    "2623": "explanatory_chain",
    "2643": "statement_subtle_inversion", "2656": "statement_overgeneralization", "2675": "distractor_by_topic_association",
    "2707": "statement_subtle_inversion",
    "2739": "statement_partial_truth", "2740": "numerical_proximity", "2741": "explanatory_chain",
    "2742": "statement_subtle_inversion", "2743": "statement_subtle_inversion",
    "2785": "explanatory_chain",
    "2786": "geographic_attribution", "2787": "distractor_by_topic_association", "2788": "distractor_by_topic_association",
    "2789": "geographic_attribution", "2790": "explanatory_chain",
    "2791": "statement_subtle_inversion", "2792": "statement_subtle_inversion",
}


# Discrimination cards — drafted by Sonnet agents, merged by Opus.
DISCRIMINATION_CARDS: dict = {
}


# Merge overlays (cards drafted by Sonnet, written to scratch JSON). Any wave_*.json / calibration_cards.json / wave1_*.json / wave2_*.json picked up automatically.
_SCRATCH = ROOT / ".scratch" / "drill_2023"
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
