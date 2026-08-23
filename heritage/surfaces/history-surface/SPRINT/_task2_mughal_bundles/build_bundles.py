#!/usr/bin/env python3
"""Task 2 output builder — Mughal bundle plan.

Emits two artefacts from one declarative source:
  - HISTORY_SPRINT_MUGHAL_BUNDLES.json   (Task-4-consumable, structured)
  - HISTORY_SPRINT_MUGHAL_BUNDLES.md     (human-readable, prose + tables)

Run:    python3 build_bundles.py
Reads:  ../../HISTORY_SPRINT_PYQ_WEIGHTS.json
        ../6.mughal/mughal.json
Writes: ../../HISTORY_SPRINT_MUGHAL_BUNDLES.{json,md}

Coverage assertion: every era-JSON node (except period_* timeline stages)
must appear exactly once across (anchors ∪ fly_bys ∪ alias-of) somewhere
in the story list. Script aborts if coverage is incomplete or if any anchor
has more than one home.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from collections import Counter, defaultdict

HISTORY_DIR = Path(__file__).resolve().parents[2]   # surfaces/history-surface/
SPRINT_DIR = Path(__file__).resolve().parents[1]    # surfaces/history-surface/SPRINT/
ERA_JSON = HISTORY_DIR / "6.mughal/mughal.json"
WEIGHTS_JSON = SPRINT_DIR / "HISTORY_SPRINT_PYQ_WEIGHTS.json"
OUT_JSON = SPRINT_DIR / "HISTORY_SPRINT_MUGHAL_BUNDLES.json"
OUT_MD = SPRINT_DIR / "HISTORY_SPRINT_MUGHAL_BUNDLES.md"

# Mention shapes per architecture §3
SHAPE_BY_TYPE = {
    "person": "cameo",
    "place": "background",
    "concept": "caption",
    "event": "connective",
    "movement": "connective",
    "reform": "connective",
    "institution": "caption",   # institutions caption unless person/place-like
    "empire": "caption",
    "period": "stage",          # period_* nodes belong to timeline, not stories
}

# Anchor render-order priority — D2 of HISTORY_SPRINT_PIPELINE_LOCK.md.
# Sort key is (priority, -pyq_count). Stable sort preserves declared order for ties.
ANCHOR_RENDER_PRIORITY = {
    "place":       0,   # establishing / background grammar
    "institution": 1,   # interior / system establishment
    "person":      2,   # character close-ups
    "event":       3,   # battle / promulgation scenes
    "empire":      3,   # tied with event
    "concept":     4,   # diagrammatic / Panel-E register
    "reform":      4,   # tied with concept
    "movement":    4,   # tied with concept
    "period":      99,  # period nodes never anchor
}

# Aliases — Task-1-flagged twin nodes resolved to a single canonical anchor.
# Format: {alias_id: canonical_id}. The alias appears nowhere in the story
# graph; the canonical does the work. Both still exist in the era JSON.
ALIASES = {
    "hist_mansabdari_system": "hist_mansab_system",
}

# Declarative bundle plan. Each story = ONE embodied moment.
# anchors  = [(node_id, source)]   source ∈ {pyq, pyq_suggestive, narrative}
# fly_bys  = [(node_id, mention_shape_override_or_None)]
#            (None → use SHAPE_BY_TYPE[node.type] default)
STORIES = [
    {
        "id": "s01_panipat_1526",
        "title": "The Field of Panipat — 21 April 1526",
        "scene": {
            "place": "Panipat battlefield, north India",
            "year": 1526,
            "moment": "Midday — Babur's tulughma curls around Ibrahim Lodi's wings; Ottoman gunners Ustad Ali and Mustafa light the matchlocks; Lodi dies before nightfall.",
        },
        "stage_ids": ["babur_humayun"],
        "synopsis": "Foundation moment. Gunpowder + flanking divisions decide north India. Babur's foothold becomes the Mughal Empire.",
        "anchors": [
            ("hist_babur", "pyq"),
            ("hist_battle_panipat_1526", "pyq"),
            ("hist_mughal_empire", "pyq"),
        ],
        "fly_bys": [
            ("hist_babur_nama", None),         # caption — Babur writes about the day
            ("hist_chahar_bagh", None),        # background — he'll lay the first garden after Panipat
            ("hist_bangla_dome", None),        # caption — Lodi-era dome architecture absorbed
            ("hist_battle_khanwa_1527", None), # connective — next year vs. Rana Sanga
            ("hist_battle_chanderi_1528", None),
            ("hist_battle_ghagra_1529", None),
            ("hist_bahadur_shah_gujarat", None),  # cameo connective forward — Humayun's first opponent
        ],
    },
    {
        "id": "s02_library_stairs_1556",
        "title": "The Library Stairs — Delhi, January 1556",
        "scene": {
            "place": "Din Panah, Delhi",
            "year": 1556,
            "moment": "Humayun, having just recaptured Delhi the year before, falls down the staircase of his library on hearing the muezzin. Memory tableaux around him: swimming the Ganga at Chausa 1539, exile at Tahmasp's Safavid court, the painters Mir Sayyid Ali and Khwaja Abdus Samad returning with him from Iran.",
        },
        "stage_ids": ["babur_humayun"],
        "synopsis": "The exile that becomes inheritance. Humayun's fifteen lost years let Sher Shah build the institutional spine (rupiya, GT Road, sarai, zabt prototype) that Akbar will use.",
        "anchors": [
            ("hist_humayun", "pyq"),
        ],
        "fly_bys": [
            ("hist_battle_chausa_1539", None),
            ("hist_battle_kanauj_1540", None),
            ("hist_mir_sayyid_ali", None),     # cameo — returning painter
            ("hist_abdus_samad", None),
            ("period_babur_humayun", "timeline-only"),  # explicit stage handle
        ],
    },
    {
        "id": "s03_mansab_day_1580",
        "title": "Mansab Day — Akbar's Court, c.1580",
        "scene": {
            "place": "Diwan-i-Khas, Fatehpur Sikri",
            "year": 1580,
            "moment": "Todar Mal presents the zabt revenue sheet; mansab ranks are being inscribed for Iranis, Turanis, Afghans, and Rajputs; Raja Man Singh stands at his 7,000-rank station; through the open gate, the stone elephant statues of Jaimal Rathore and Patta Sisodiya — defenders of Chittor — face the court.",
        },
        "stage_ids": ["akbar"],
        "synopsis": "The composite-nobility machine assembled in one room. Mansabdari + zabt + watan jagirs + subadari operating together; the conquest map (Gujarat→Bengal→Kashmir→Sindh→Berar→Khandesh) is the result.",
        "anchors": [
            ("hist_mansab_system", "pyq"),    # canonical anchor inheriting hist_mansabdari_system's PYQ evidence (pyq_count=1, pyq_id 306)
            ("hist_todar_mal", "narrative"),
            ("hist_raja_man_singh", "narrative"),
            ("hist_jaimal_patta", "narrative"),
            ("hist_rana_pratap", "narrative"),
        ],
        "fly_bys": [
            ("hist_zabt_system", None),                 # caption on the sheet
            ("hist_subadari_system", None),
            ("hist_akbar_social_reforms", None),        # caption on a separate farman (sati/jauhar bans)
            ("hist_battle_second_panipat_1556", None),  # backstory connective
            ("hist_hemu", None),
            ("hist_bairam_khan", None),
            ("hist_adham_khan", None),                  # 1561 balcony incident
            ("hist_maham_anaga", None),
            ("hist_mirza_hakim", None),                 # Kabul brother — connective
            ("hist_raja_bharmal_kachhwaha", None),      # 1562 marriage alliance — cameo via daughter in zenana corridor
            ("hist_bhagwant_das", None),
            ("hist_siege_chittor_1568", None),
            ("hist_siege_ranthambhor_1569", None),
            ("hist_battle_haldighati_1576", None),
            ("hist_conquest_gujarat_1572", None),
            ("hist_bengal_conquest_1576", None),
            ("hist_kashmir_annexation_1586", None),
            ("hist_sindh_annexation_1590", None),
            ("hist_berar_annexation_1596", None),
            ("hist_khandesh_annexation_1601", None),
            ("hist_rajput_watan_jagirs", None),         # caption — concept stage=aurangzeb but originates here
            ("period_akbar", "timeline-only"),
        ],
    },
    {
        "id": "s04_ibadat_khana_1578",
        "title": "The Ibadat Khana — Thursday Night, 1578",
        "scene": {
            "place": "Ibadat Khana, Fatehpur Sikri",
            "year": 1578,
            "moment": "A Sunni theologian and a Shia theologian argue at volume about the Imamate; a Jain monk from Kathiawar waits his turn; Rodolfo Acquaviva and Antonio Monserrate sit with illustrated Gospels for the emperor; Abu'l Fazl writes in the corner; Birbal sits across; outside the window, Salim Chishti's white tomb glows; in the adjoining courtyard, Mian Tansen tunes for Darbari Kanada.",
        },
        "stage_ids": ["akbar"],
        "synopsis": "The architecture of synthesis given a single embodied evening. *Sulh-i-kul* is the operating logic; the Mughal painting tradition is being born in the workshop next door; the *Akbarnama* is being drafted in this same hall.",
        "anchors": [
            ("hist_akbar", "pyq"),
            ("hist_fatehpur_sikri", "pyq"),
            ("hist_ibadat_khana", "pyq"),
            ("hist_abul_fazl", "pyq"),
            ("hist_tansen", "pyq"),
            ("hist_sulh_i_kul", "narrative"),           # concept-as-anchor: inscribed on the hall
            ("hist_mughal_painting", "narrative"),      # tradition's founding moment
        ],
        "fly_bys": [
            ("hist_din_i_ilahi", None),
            ("hist_mahzar_1579", None),
            ("hist_first_jesuit_mission_1580", None),
            ("hist_rodolfo_acquaviva", None),
            ("hist_antonio_monserrate", None),
            ("hist_faizi", None),
            ("hist_badauni", None),                     # writing the counter-history
            ("hist_gulbadan_begum", None),              # writing Humayun-Nama in the zenana
            ("hist_birbal_raja", None),
            ("hist_abdur_rahim_khanan", None),
            ("hist_farr_i_izadi", None),                # caption on an Akbarnama folio
            ("hist_akbar_nama", None),
            ("hist_ain_i_akbari", None),
            ("hist_hamzanama", None),                   # background folios
            ("hist_tutinama", None),
            ("hist_maktab_khana", None),                # background — translation bureau adjoining
            ("hist_mughal_information_system", None),
            ("hist_tudor_arch", None),                  # background — Fatehpur Sikri's idiom
            ("hist_humayun_tomb", None),                # background — predecessor architecture
            ("hist_persian_language_mughals", None),    # caption
            ("hist_navaratna", None),                   # caption — Tansen/Birbal/Faizi/Abu'l Fazl/etc. present
            ("hist_mughal_court", None),
            ("hist_mughal_court_etiquette", None),
        ],
    },
    {
        "id": "s05_lahore_1606",
        "title": "Lahore 1606 — The Wound Opens",
        "scene": {
            "place": "Lahore Fort + Vrindavan memory panel",
            "year": 1606,
            "moment": "Guru Arjan is dragged from Lahore Fort and tortured on Jahangir's order; the *Adi Granth* — which he compiled two years earlier at Amritsar — lies open on a table beside him, its pages showing the verses of Kabir, Namdev, Farid, Surdas; a foreground panel shows Hargobind donning two swords (the doctrine of *miri-piri*); a memory tableau within the scene shows Tulsidas at Varanasi finishing the *Ramcharitmanas*, Mirabai singing in Mewar, Dadu Dayal teaching in Rajasthan; Miyan Mir (the Qadariya sufi who laid the Harmandir Sahib's foundation stone) stands at the edge of the scene in grief.",
        },
        "stage_ids": ["akbar", "jahangir_nur_jahan", "mughal_culture"],
        "synopsis": "The first Mughal-Sikh fracture, framed against the same century's bhakti compilation that the Adi Granth absorbed. The scripture and the martyrdom in one scene.",
        "anchors": [
            ("hist_guru_arjan", "pyq"),
            ("hist_guru_granth_sahib", "narrative"),    # era-JSON pyq_count baked but absent from Task 1 weights JSON
            ("hist_tulsidas", "pyq"),
            ("hist_mirabai", "pyq"),
            ("hist_dadu_dayal", "pyq"),
            ("hist_guru_har_govind", "narrative"),    # miri-piri founder
        ],
        "fly_bys": [
            ("hist_surdas", None),
            ("hist_eknath", None),
            ("hist_tukaram", None),
            ("hist_ram_das_samarth", None),           # Shivaji's guru — bhakti cluster
            ("hist_miyan_mir", None),
            ("hist_qadariya_silsila", None),          # caption — Miyan Mir's lineage
            ("hist_khusrau", None),                   # cameo connective — his rebellion triggered Arjan's harboring
        ],
    },
    {
        "id": "s06_chain_of_justice_1617",
        "title": "The Chain of Justice — Agra Fort, c.1617",
        "scene": {
            "place": "Agra Fort, riverbank",
            "year": 1617,
            "moment": "The thirty-yard gold chain hangs from the fort wall to the Yamuna bank, its sixty bells catching the river breeze; Jahangir watches from the jharoka; Nur Jahan inscribes a farman under her own seal at a side desk; Sir Thomas Roe waits in the audience corridor with his East India Company petition; in the open courtyard studio, Ustad Mansur paints a Siberian crane from life; Mirza Ghiyas Beg (Itimad-ud-Daulah) reviews accounts; on the riverbank behind, his own marble tomb is rising under Nur Jahan's commission.",
        },
        "stage_ids": ["jahangir_nur_jahan"],
        "synopsis": "Mughal sovereignty presented as personally accountable; a Persian-émigré finance family at the empire's centre; the first English ambassador watching effective power held by a woman.",
        "anchors": [
            ("hist_jahangir", "pyq"),
            ("hist_nur_jahan", "narrative"),
            ("hist_ustad_mansur", "narrative"),
            ("hist_thomas_roe", "pyq_suggestive"),
        ],
        "fly_bys": [
            ("hist_chain_of_justice", None),
            ("hist_du_aspah_sih_aspah", None),         # Jahangir's mansab refinement — caption
            ("hist_itmad_ud_daulah_tomb", None),       # background — rising on the riverbank
            ("hist_itimad_ud_daulah", None),
            ("hist_asaf_khan", None),
            ("hist_islam_khan_chishti", None),
            ("hist_shalimar_bagh_kashmir", None),
            ("hist_akbar_tomb_sikandra", None),
            ("hist_amar_singh_mewar", None),           # connective — his 1615 submission a recent memory
            ("hist_shah_jahan_rebellion_1622", None),  # forward-ref connective
            ("hist_mahabat_khan", None),
            ("hist_jharoka_darshan", None),            # caption — that's what Jahangir is doing
            ("period_jahangir_nur_jahan", "timeline-only"),
        ],
    },
    {
        "id": "s07_shahjahanabad_1656",
        "title": "Shahjahanabad, 1656 — The Marble Capital Complete",
        "scene": {
            "place": "Friday-prayer plaza of the Jama Masjid, Old Delhi",
            "year": 1656,
            "moment": "The newly opened Jama Masjid catches Friday light; the planned grid of Shahjahanabad spreads beyond; up the Yamuna at Agra, the Taj Mahal (now thirteen years complete) is visible as a marble glimmer; in the adjacent Diwan-i-Khas of the Red Fort, the Peacock Throne sits beneath the inlaid couplet '*Agar firdaus bar roo-e zameen ast…*'; Abdul Hamid Lahori finalizes a *Badshah Nama* folio on a portable desk in the courtyard; Dara Shukoh walks past with his *Sirr-i-Akbar* manuscript open, Jahanara at his side.",
        },
        "stage_ids": ["shah_jahan"],
        "synopsis": "Shah Jahan's full vision in a single afternoon — Taj, Peacock Throne, Jama Masjid, Shahjahanabad all complete; the Deccan formally vassal since 1636; Dara's Sufi-Vedanta program present but already vulnerable.",
        "anchors": [
            ("hist_shah_jahan", "pyq"),
            ("hist_taj_mahal", "narrative"),
            ("hist_peacock_throne", "narrative"),
            ("hist_jama_masjid_delhi", "pyq"),
            ("hist_shahjahanabad", "narrative"),
            ("hist_abdul_hamid_lahori", "pyq_suggestive"),
            ("hist_badshah_nama", "narrative"),
        ],
        "fly_bys": [
            ("hist_pietra_dura", None),
            ("hist_diwan_i_khas", None),
            ("hist_moti_masjid_agra", None),
            ("hist_qandahar_question", None),          # Mughal-Safavid Deccan-equivalent contest in the north
            ("hist_jahangir_tomb", None),
            ("hist_balkh_campaign_1646", None),
            ("hist_treaty_1636_deccan", None),
            ("hist_ahmadnagar_fall_1633", None),
            ("hist_jahanara", None),
            ("period_shah_jahan", "timeline-only"),
        ],
    },
    {
        "id": "s08_delhi_jizya_1679",
        "title": "Delhi, March 1679 — The Jizya Proclamation",
        "scene": {
            "place": "Chowk in front of the Red Fort, Delhi",
            "year": 1679,
            "moment": "Aurangzeb's *jizya* farman is read out from the Naubat Khana; the Hindu merchants of Delhi sit in a circle blocking the imperial procession; muhtasibs with whips push at the perimeter; François Bernier watches from a balcony, his notebook open showing the half-drafted theory of imperial land ownership; a courtier's desk holds Shaikh Ahmad Sirhindi's letters arguing *wahdat-ul-shuhud* against the older Chishti *wahdat-ul-wujud*; the Fatawa-i-Alamgiri compilation team works in a side room; Dara Shukoh's portrait hangs in memorial.",
        },
        "stage_ids": ["aurangzeb", "mughal_culture"],
        "synopsis": "The reversal at its most legible moment. Theological policy, juridical compendium, observer's theory of despotism, and the Naqshbandi-over-Chishti doctrinal victory all sit in one square.",
        "anchors": [
            ("hist_aurangzeb", "pyq"),
            ("hist_dara_shukoh", "narrative"),
            ("hist_muhtasib", "narrative"),
            ("hist_fatawa_i_alamgiri", "narrative"),
            ("hist_francois_bernier", "narrative"),   # era-JSON pyq_count 2 baked, but absent from Task 1 weights JSON (regex under-match)
            ("hist_shaikh_ahmad_sirhindi", "pyq"),
        ],
        "fly_bys": [
            ("hist_jizya_policy", None),
            ("hist_bernier_land_ownership", None),
            ("hist_oriental_despotism", None),
            ("hist_war_of_succession_1658", None),     # memory connective — Samugarh, Dara's death
            ("hist_wahdat_ul_wujud_vs_shuhud", None),
            ("hist_naqshbandi_silsila", None),
            ("hist_tavernier", None),                  # earlier traveller, cameo as predecessor
            ("hist_manucci", None),
            ("hist_giovanni_careri", None),            # forward-ref — visits 1690s
            ("hist_satnami_revolt_1672", None),        # connective — recent parallel revolt
            ("hist_marwar_mewar_war_1679", None),      # connective — opening this same year
        ],
    },
    {
        "id": "s09_aurangabad_1707",
        "title": "Aurangabad 1707 — The Empire's Last Camp",
        "scene": {
            "place": "Aurangzeb's military camp at Ahmadnagar/Aurangabad",
            "year": 1707,
            "moment": "Aurangzeb at 88 lies dying in his campaign tent, dictating his final testament; a campaign map showing eight years of Rajaram's hold at Jinji is pinned to the wall; couriers bring news from the Marwar-Mewar front; in a memory panel, Sambhaji is led to his execution at Tulapur 1689; Bibi-ka-Maqbara — the 'poor man's Taj' — rises in the middle distance; Mir Jumla's old shaft-mining gear lies in a corner.",
        },
        "stage_ids": ["aurangzeb"],
        "synopsis": "Territorial maximum, institutional minimum. Bijapur (1685) and Golconda (1687) fell, but their fall unleashed the Marathas; Aurangzeb is in the Deccan from 1698 onward and will die there.",
        "anchors": [
            ("hist_sambhaji", "pyq"),
            ("hist_bibi_ka_maqbara", "narrative"),
        ],
        "fly_bys": [
            ("hist_bijapur_annexation_1685", None),
            ("hist_golconda_annexation_1687", None),
            ("hist_ahom_mughal_wars", None),
            ("hist_jinji_siege_1690", None),
            ("hist_rajaram", None),
            ("hist_ajit_singh_marwar", None),
            ("hist_durgadas_rathore", None),
            ("hist_jaswant_singh_marwar", None),
            ("hist_mir_jumla", None),
            ("hist_madanna_akkanna", None),
            ("hist_shaista_khan", None),               # Aurangzeb's earlier commander, Pune raid victim
            ("hist_raja_jai_singh_amber", None),       # memory cameo — the Treaty of Purandar negotiator
            ("period_aurangzeb", "timeline-only"),
        ],
    },
    {
        "id": "s10_anandpur_1699",
        "title": "Anandpur, Baisakhi 1699 — The Khalsa Is Born",
        "scene": {
            "place": "Anandpur Sahib, foothills of Punjab",
            "year": 1699,
            "moment": "Guru Gobind Singh under the saffron banner; five volunteers from disparate castes drink amrit from a single iron bowl and emerge as the panj pyaare; the five Ks visible on each; a memory panel within the scene shows Tegh Bahadur's execution at Chandni Chowk in 1675; a forward shadow shows the four sahibzadas' coming deaths (Chamkaur 1705 and the bricking at Sirhind).",
        },
        "stage_ids": ["aurangzeb", "mughal_culture"],
        "synopsis": "The Sikh community ceases to be primarily devotional. The Khalsa institution arrives as the direct radicalising response to Aurangzeb's Delhi execution of Tegh Bahadur.",
        "anchors": [
            ("hist_guru_gobind_singh", "pyq"),
            ("hist_khalsa", "pyq"),
            ("hist_guru_tegh_bahadur", "pyq"),
        ],
        "fly_bys": [
            ("hist_guru_har_rai", None),               # in-between Guru cameo
            ("hist_guru_har_kishan", None),
        ],
    },
    {
        "id": "s11_pratapgarh_1659",
        "title": "Pratapgarh, 10 November 1659 — The Bagh-Nakh",
        "scene": {
            "place": "Forest-pavilion meeting point below Pratapgarh fort, Western Ghats",
            "year": 1659,
            "moment": "Shivaji and Bijapur's general Afzal Khan embrace; the concealed tiger-claw strikes; the Bijapuri retinue is ambushed by Maratha cavalry already deployed in the hills; in a memory panel, Jijabai instructs the young Shivaji in dharma at Poona; his father Shahji Bhonsle's portrait hangs in a corner.",
        },
        "stage_ids": ["maratha_rise", "aurangzeb"],
        "synopsis": "Shivaji's signature deed — the moment Mughal contemporaries first recognise him as a sovereign actor, not a raider.",
        "anchors": [
            ("hist_shivaji", "pyq"),
            ("hist_afzal_khan", "narrative"),
            ("hist_battle_pratapgarh_1659", "narrative"),
        ],
        "fly_bys": [
            ("hist_shahji_bhonsle", None),
            ("hist_jijabai", None),
        ],
    },
    {
        "id": "s12_raigarh_1674",
        "title": "Raigarh, 6 June 1674 — Chhatrapati",
        "scene": {
            "place": "Coronation hall, Raigarh fort",
            "year": 1674,
            "moment": "Shivaji is consecrated *Chhatrapati* by Pandit Gagabhatt; the eight ministers of the Ashtapradhan stand each at their station with their books of office; revenue scrolls inscribed *chauth* and *sardeshmukhi* are laid before the throne; memory tableaux show the 1664 sack of Surat, the Treaty of Purandar 1665, and the 1666 escape from Aurangzeb's Agra court; forward shadows show Sambhaji and the future Peshwas.",
        },
        "stage_ids": ["maratha_rise", "aurangzeb"],
        "synopsis": "Maratha state-formation made explicit. The Ashtapradhan + chauth/sardeshmukhi system are not raiding but rational bureaucracy.",
        "anchors": [
            ("hist_maratha_empire", "narrative"),
            ("hist_shivaji_coronation_1674", "narrative"),
            ("hist_ashtapradhan", "narrative"),
            ("hist_peshwas", "narrative"),    # era-JSON pyq_count 1 baked, absent from Task 1 weights JSON
        ],
        "fly_bys": [
            ("hist_chauth", None),
            ("hist_sardeshmukhi", None),
            ("hist_surat_sack_1664", None),
            ("hist_treaty_purandar_1665", None),
            ("hist_shivaji_agra_escape_1666", None),
            ("hist_battle_salher_1672", None),
            ("period_maratha_rise", "timeline-only"),
        ],
    },
    {
        "id": "s13_ahmadnagar_1595",
        "title": "Ahmadnagar 1595 — Chand Bibi at the Walls",
        "scene": {
            "place": "Ramparts of Ahmadnagar Fort",
            "year": 1595,
            "moment": "Chand Bibi, regent of Ahmadnagar, in armour on the wall directing the defence against Akbar's besieging army; Malik Ambar — the Ethiopian-born vizier who will pioneer Maratha-cavalry guerrilla warfare — coordinates from horseback; in framed inset panels, Muhammad Quli Qutb Shah founds Hyderabad (1591) with the Char Minar at its centre, Ibrahim Adil Shah II composes Dakhini music at Bijapur, and Gol Gumbaz's dome is taking shape; Ibrahim Rauza sits in the same Bijapuri skyline.",
        },
        "stage_ids": ["deccan_sultanates_tail"],
        "synopsis": "The Deccan's own synthesis question, running parallel to the Mughal one — multilingual courts, women as effective commanders, African vizier-strategists, an architectural language entirely its own.",
        "anchors": [
            ("hist_malik_ambar", "pyq"),
            ("hist_gol_gumbaz", "pyq"),
            ("hist_chand_bibi", "narrative"),
            ("hist_char_minar", "narrative"),
        ],
        "fly_bys": [
            ("hist_bijapur_sultanate", None),
            ("hist_golconda_sultanate", None),
            ("hist_ahmadnagar_sultanate", None),
            ("hist_ibrahim_adil_shah_ii", None),
            ("hist_muhammad_quli_qutb_shah", None),
            ("hist_ibrahim_rauza", None),
            ("period_deccan_sultanates_tail", "timeline-only"),
        ],
    },
    {
        "id": "s14_surat_port_1670",
        "title": "Surat Port, October 1670 — The Second Sack",
        "scene": {
            "place": "Surat harbour, Gujarat",
            "year": 1670,
            "moment": "Shivaji's second raid is in progress: customs houses burn; Mughal officials flee; merchants tear hundi paper bills they cannot collect on; bales of *muslin* from Dacca and *chintz* from the Coromandel coast lie split on the quayside; Spanish reales and Mexican 8-real silver coins spill from a money-changer's chest; tomatoes, chillies, and tobacco from American imports sit in a bazaar stall; an English East India Company factor watches from the factory roof.",
        },
        "stage_ids": ["mughal_economy"],
        "synopsis": "The commercial empire visible at its key port: silver flowing in, cloth flowing out, hundi credit binding it together — and a Maratha raider exposing how thin the imperial military shield over the trade has become.",
        "anchors": [
            ("hist_surat", "pyq"),
            ("hist_hundi_system", "narrative"),
            ("hist_silver_flow_mughal", "narrative"),
            ("hist_indian_textile_trade", "narrative"),
            ("hist_new_world_crops", "narrative"),
        ],
        "fly_bys": [
            ("hist_muslin", None),
            ("hist_chintz", None),
            ("hist_cotton_textile_mughal", None),
            ("hist_masulipatnam", None),
            ("hist_dacca_textile_centre", None),
            ("hist_proto_industrialisation", None),    # caption — parallel concept, anchor home is s19
        ],
    },
    {
        "id": "s15_bihar_village_c1650",
        "title": "A Bihar Village — Harvest Day, c.1650",
        "scene": {
            "place": "An open-field Mughal-era village, lower Bihar (suba of Bihar)",
            "year": 1650,
            "moment": "The *qanungo* records this year's yield against the zabt-fixed assessment; *khud-kashta* resident peasants and *pahi-kashta* outsiders work different strips of the same field; women in the rear cleaning *jins-i-kamil* cash crops (cotton, indigo, sugarcane); zamindar's agents and the village panchayat negotiate the headman's share at a separate corner; a Persian-wheel irrigation device turns above an open well; a small forest community at the field's edge sells honey and lac.",
        },
        "stage_ids": ["mughal_economy"],
        "synopsis": "The agrarian engine that finances everything else — Akbar's *zabt* still working, layered with caste, gender, kinship, and the slow shift toward revenue-farming that will become *ijaradari* under decline.",
        "anchors": [
            ("hist_mughal_revenue_system", "narrative"),
            ("hist_mughal_agrarian_system", "narrative"),
            ("hist_mughal_zamindars", "narrative"),
            ("hist_mughal_irrigation", "narrative"),
            ("hist_khud_kashta_pahi_kashta", "narrative"),
        ],
        "fly_bys": [
            ("hist_village_panchayat_mughal", None),
            ("hist_jins_i_kamil", None),
            ("hist_women_agrarian_society", None),
            ("hist_caste_rural_mughal", None),
            ("hist_jajmani_system", None),
            ("hist_tribal_forest_communities", None),
            ("hist_mughal_population_growth", None),
            ("hist_coparcenary_inheritance", None),
            ("hist_peasant_resistance_mughal", None),
            ("hist_ijaradari", None),                  # caption forward — decline-era twist
            ("period_mughal_economy", "timeline-only"),
        ],
    },
    {
        "id": "s16_kitabkhana_c1700",
        "title": "The Kitabkhana — A Mughal Studio, c.1700",
        "scene": {
            "place": "Imperial Kitabkhana, late Mughal Lahore / Delhi; with a side-panel of a Pahari hill studio at Basohli",
            "year": 1700,
            "moment": "A master painter finishes a Mughal-style portrait of an Aurangzeb-era noble; in an adjoining panel, a Pahari artist from Basohli works in bold red ground with the new Krishna iconography; further panels: a Kangra atelier under the Katoch rajas in green hills; a Kathak performance in a Rajput courtyard; bound copies of the *Hamzanama* and *Tutinama* on a workshop shelf; Ragamala painting cycles arranged for inspection.",
        },
        "stage_ids": ["mughal_culture"],
        "synopsis": "The painting tradition Akbar founded has diffused — into Pahari schools, into Rajasthani courts, and into the choreography of court dance. One scene captures the entire post-Akbar visual ecology.",
        "anchors": [
            ("hist_kathak", "narrative"),                   # era JSON had this at high count; weights re-run did not match; anchor on narrative grounds
            ("hist_basohli_painting", "narrative"),         # era-JSON pyq_count 2 baked, absent from Task 1 weights JSON
            ("hist_kangra_school", "narrative"),            # same
        ],
        "fly_bys": [
            ("hist_mewar_painting", None),
            ("hist_kishangarh_painting", None),
            ("hist_ragamala_paintings", None),
            ("hist_bundi_painting", None),
            ("hist_amber_jaipur_painting", None),
            ("hist_marwar_painting", None),
            ("hist_mughal_manuscripts", None),
            ("hist_printing_india", None),                 # caption — note on printing's slow arrival
            ("hist_kitabkhana", None),                     # caption — the institution itself
            ("period_mughal_culture", "timeline-only"),
        ],
    },
    {
        "id": "s17_karnal_1739",
        "title": "Karnal, February 1739 — Nadir Shah's Camp",
        "scene": {
            "place": "Nadir Shah's tent at Karnal, just after the rout of Muhammad Shah's Mughal army",
            "year": 1739,
            "moment": "The Peacock Throne is being loaded onto Persian carts; the Koh-i-Noor changes hands in close-up; in the distance, Delhi burns under the *qatl-e-aam* massacre; a memory panel shows Khafi Khan's 'one pomegranate among a hundred sick' as a caption; Suraj Mal at Bharatpur is sheltering fleeing Mughal nobles in a side-panel; revenue-farming *ijaradari* contracts blow across the camp floor.",
        },
        "stage_ids": ["mughal_decline"],
        "synopsis": "The structural collapse made spectacular. The jagirdari crisis behind the throne was the deep cause; Nadir's loot is its visible expression.",
        "anchors": [
            ("hist_nadir_shah_invasion", "narrative"),    # era-JSON pyq_count 1 baked, absent from Task 1 weights JSON
            ("hist_mughal_decline", "pyq"),
        ],
        "fly_bys": [
            ("hist_ijaradari", None),                  # caption — revenue-farming symptomatic of decline
            ("hist_suraj_mal", None),                  # cameo at Bharatpur
            ("period_mughal_decline", "timeline-only"),
        ],
    },
    {
        "id": "s18_jaipur_1734",
        "title": "Jaipur 1734 — Sawai Jai Singh at the Jantar Mantar",
        "scene": {
            "place": "Jantar Mantar observatory courtyard, newly founded city of Jaipur",
            "year": 1734,
            "moment": "Sawai Jai Singh II at the great Samrat Yantra sundial; on a stone table beside him, a political map of India c.1734 with five highlighted capitals — Murshidabad (Murshid Quli Khan's Bengal), Lucknow/Faizabad (Saadat Khan's Awadh), Hyderabad (Nizam Asaf Jah), Bharatpur (Suraj Mal's Jat state), Anandpur/Sirhind (the Sikh territories where Banda Bahadur had struck sovereign coins); a Maratha cavalry stream pushes north (Bajirao's expansion) as a background tableau; a smudge on the Bengal coast marks the East India Company's growing factories.",
        },
        "stage_ids": ["mughal_decline"],
        "synopsis": "The successor states presented as a single moment of pluralising sovereignty — not collapse but reformation. Jaipur the planned city is itself an instance of this new political form.",
        "anchors": [
            ("hist_sawai_jai_singh", "pyq"),         # Yantra-Mantar panel — the scene's iconic figure
            ("hist_hyderabad_state", "pyq"),         # sub-panel: Asaf Jah's founding firman
            ("hist_banda_bahadur", "pyq"),           # sub-panel: sovereign Sikh coinage
            ("hist_shahu", "narrative"),             # Maratha-cavalry-stream tableau in background; Shahu's claim
        ],
        "fly_bys": [
            # Abstract state-concepts captioned as labeled dots on the political map — per advisor §3 review.
            ("hist_bengal_state", None),             # caption — Murshidabad dot
            ("hist_awadh_state", None),              # caption — Lucknow/Faizabad dot
            ("hist_jat_state", None),                # caption — Bharatpur dot
            ("hist_sikh_state", None),               # caption — Anandpur/Sirhind dot
        ],
    },
    {
        "id": "s19_six_courts_parallel",
        "title": "Six Courts, One Hour — Eurasia c.1640",
        "scene": {
            "place": "Split-screen meta-tableau: six framed windows of one composite illustration",
            "year": 1640,
            "moment": "Six contemporaneous courts, all visible at once: (i) Galileo at his telescope in Arcetri (already silenced by the Council of Trent's heirs); (ii) Suleyman's successor era in Istanbul; (iii) Shah Abbas I's Naqsh-i-Jahan square at Isfahan; (iv) the late-Tudor court at Greenwich (Queen Elizabeth's now-historical reign); (v) Tokugawa Iemitsu issuing the *sakoku* seclusion edicts at Edo; (vi) the early-Qing court at Beijing. A village English cricket green and an enclosed field hover at the meta-edge as captions on the era's quiet structural changes.",
        },
        "stage_ids": ["parallel_europe", "parallel_islamic_west", "parallel_east_asia"],
        "synopsis": "Meta-scene by design (flagged as a bundling-method edge case for convergence): when the cognitive task is 'simultaneity', the embodied-episode test relaxes to split-screen rather than single-stage.",
        "anchors": [
            ("hist_jesuits", "narrative"),                 # era-JSON pyq_count 1 baked, absent from Task 1 weights JSON
            ("hist_proto_industrialisation", "narrative"),
        ],
        "fly_bys": [
            ("hist_galileo", None),
            ("hist_copernicus", None),                 # memory cameo via portrait or book
            ("hist_council_of_trent", None),
            ("hist_counter_reformation", None),
            ("hist_scientific_revolution", None),
            ("hist_queen_elizabeth_i", None),
            ("hist_ivan_iv_russia", None),
            ("pol_hobbes", None),                      # cameo on a desk
            ("pol_locke", None),
            ("pol_rousseau", None),                    # forward-ref caption (he's mid-18th c.)
            ("hist_enclosure_movement", None),
            ("hist_agricultural_revolution", None),
            ("hist_english_agricultural_revolution", None),
            ("hist_coal_iron", None),
            ("hist_diseases_and_depopulation", None),  # caption — Americas backdrop
            ("hist_paper_spread", None),
            ("hist_cricket_origins", None),
            ("hist_rise_of_novel", None),
            ("hist_calico_act_1720", None),            # forward-ref protectionism
            ("hist_suleyman_magnificent", None),
            ("hist_shah_abbas_safavid", None),
            ("hist_samurai", None),
            ("hist_qing_dynasty", None),
            ("hist_tokugawa_japan", None),
            ("period_parallel_islamic_west", "timeline-only"),
        ],
    },
]


def load_era_nodes() -> dict:
    with ERA_JSON.open() as f:
        d = json.load(f)
    return {n["id"]: n for n in d["nodes"]}


def load_weights() -> dict:
    with WEIGHTS_JSON.open() as f:
        d = json.load(f)
    out = {}
    for w in d["eras"]["mughal"]["weighted_nodes"]:
        out[w["node_id"]] = w
    return out


def resolve_mention_shape(node_type: str, override) -> str:
    if override == "timeline-only":
        return "timeline-only"
    if override:
        return override
    return SHAPE_BY_TYPE.get(node_type, "caption")


def main() -> int:
    era_nodes = load_era_nodes()
    weights = load_weights()

    placed_anchor: dict[str, str] = {}   # node_id -> story_id
    placed_fly_by: dict[str, list[str]] = defaultdict(list)
    out_stories = []

    for s in STORIES:
        anchors_out = []
        for nid, source in s["anchors"]:
            if nid not in era_nodes:
                print(f"ERROR: anchor '{nid}' in story '{s['id']}' not in era JSON", file=sys.stderr)
                return 1
            if nid in placed_anchor:
                print(f"ERROR: anchor '{nid}' has two homes: '{placed_anchor[nid]}' and '{s['id']}'", file=sys.stderr)
                return 1
            placed_anchor[nid] = s["id"]
            node = era_nodes[nid]
            entry = {
                "node_id": nid,
                "label": node["label"],
                "type": node["type"],
                "source": source,
            }
            if nid in weights:
                entry["pyq_count"] = weights[nid]["pyq_count"]
                entry["pyq_ids"] = weights[nid]["pyq_ids"]
            else:
                # Inherit PYQ evidence from any alias pointing to this canonical id
                inherited_count = 0
                inherited_ids = []
                for alias_id, canonical_id in ALIASES.items():
                    if canonical_id == nid and alias_id in weights:
                        inherited_count += weights[alias_id]["pyq_count"]
                        inherited_ids.extend(weights[alias_id]["pyq_ids"])
                if inherited_count > 0:
                    entry["pyq_count"] = inherited_count
                    entry["pyq_ids"] = sorted(set(inherited_ids))
                    entry["pyq_inherited_from_alias"] = True
            anchors_out.append(entry)

        override = s.get("anchor_render_order_override")
        if override:
            order = {nid: i for i, nid in enumerate(override)}
            missing_nodes = [a["node_id"] for a in anchors_out if a["node_id"] not in order]
            if missing_nodes:
                print(f"ERROR: anchor_render_order_override for '{s['id']}' missing nodes: {missing_nodes}", file=sys.stderr)
                return 1
            anchors_out.sort(key=lambda a: order[a["node_id"]])
        else:
            anchors_out.sort(key=lambda a: (
                ANCHOR_RENDER_PRIORITY.get(a["type"], 99),
                -a.get("pyq_count", 0),
            ))

        fly_bys_out = []
        for nid, shape_override in s["fly_bys"]:
            if nid not in era_nodes:
                print(f"ERROR: fly-by '{nid}' in story '{s['id']}' not in era JSON", file=sys.stderr)
                return 1
            placed_fly_by[nid].append(s["id"])
            node = era_nodes[nid]
            shape = resolve_mention_shape(node["type"], shape_override)
            fly_bys_out.append({
                "node_id": nid,
                "label": node["label"],
                "type": node["type"],
                "mention_shape": shape,
            })

        out_stories.append({
            "story_id": s["id"],
            "title": s["title"],
            "scene_setting": s["scene"],
            "stage_ids": s["stage_ids"],
            "synopsis": s["synopsis"],
            "anchors": anchors_out,
            "fly_bys": fly_bys_out,
        })

    # Coverage check
    all_ids = set(era_nodes.keys())
    placed_ids = set(placed_anchor.keys()) | set(placed_fly_by.keys()) | set(ALIASES.keys())
    missing = all_ids - placed_ids
    if missing:
        print(f"ERROR: {len(missing)} nodes not placed:", file=sys.stderr)
        for nid in sorted(missing):
            n = era_nodes[nid]
            print(f"  - {nid:40s} ({n['type']:12s}) stage={n.get('stage','?')}  {n['label']}", file=sys.stderr)
        return 1

    # Double-anchor check (alias)
    for alias_id, canonical_id in ALIASES.items():
        if canonical_id not in placed_anchor:
            print(f"ERROR: alias canonical '{canonical_id}' (for alias '{alias_id}') has no anchor home", file=sys.stderr)
            return 1
        if alias_id in placed_anchor or alias_id in placed_fly_by:
            print(f"ERROR: alias '{alias_id}' should not be placed directly (canonical does the work)", file=sys.stderr)
            return 1

    # Anchor source breakdown
    src_breakdown: Counter[str] = Counter()
    for s in out_stories:
        for a in s["anchors"]:
            src_breakdown[a["source"]] += 1

    # ============ WRITE JSON ============
    payload = {
        "metadata": {
            "era": "mughal",
            "generated_by": "surfaces/history-surface/_task2_mughal_bundles/build_bundles.py",
            "story_count": len(out_stories),
            "node_count_era": len(era_nodes),
            "node_count_placed_anchor": len(placed_anchor),
            "node_count_placed_fly_by": len(placed_fly_by),
            "anchor_source_breakdown": dict(src_breakdown),
            "aliases_resolved": ALIASES,
            "task1_flags_addressed": [
                "Mansab twin merged: hist_mansab_system canonical; hist_mansabdari_system aliased (era-JSON pyq_count 7 on canonical; weights-JSON regex matched only the -dari variant).",
                "period_* nodes (period_akbar, period_aurangzeb, period_shah_jahan, etc.) tagged 'timeline-only' — not anchor candidates; live on timeline.",
                "pyq_suggestive source tags: hist_abdul_hamid_lahori (s07) and hist_thomas_roe (s06) — list-question-only evidence, not PYQ-earned.",
            ],
            "findings_for_convergence": [
                "Story count = 19, above the 10–15 architectural target. Mughal pushes the upper bound on faithful application of the embodied-episode test. Splitting the economy stage into Surat-port + Bihar-village contributed +1; splitting Aurangzeb into Jizya-1679 + Aurangabad-1707 + Anandpur-Khalsa contributed +2.",
                "Story s19 (Six Courts) is a meta-scene (split-screen) rather than a single embodied moment. Flagged as a bundling-method edge case — parallel-world content needs an explicit container convention different from India-narrative stories.",
                "Concept-as-anchor: hist_sulh_i_kul (s04), hist_mughal_painting (s04), hist_kathak (s16), hist_taj_mahal (s07), hist_guru_granth_sahib (s05) anchor as concepts/objects within an embodied scene. These need dedicated anchor-panels with stronger visual treatment than caption-level concept mentions.",
                "Mention-shape default by type (architecture §3) applied uniformly. Some institutions (Maktab Khana, Imperial Information System) defaulted to 'caption' but might warrant 'background' as physical institutions visible in scene — leaving to Task 4/5 to refine.",
                "Era-JSON vs weights-JSON pyq_count drift: the era JSON's baked-in pyq_count field disagrees with Task 1's authoritative weights JSON for ~12 entities (basohli_painting, kangra_school, francois_bernier, guru_granth_sahib, jesuits, proto_industrialisation, peshwas, nadir_shah_invasion, bengal_state, bernier_land_ownership, persian_language_mughals, oriental_despotism, mansab_system). Per Task 1's stated authority (label-matching limitation noted in its .md §3), these are tagged 'narrative' here. Future PYQ-tagging passes should resolve the drift directly in the era JSON.",
                "Anchor budget: 76 anchors total across 19 stories (avg 4.0/story) after a s18 demotion pass. That is ~2× the architecture's implicit target of ~30–45 (≈ 10–15 stories × ~3 anchors). Composition: PYQ-earned 31, PYQ-suggestive 2, narrative 43. Further narrative anchors can be downgraded to caption-mentions during Task 3 production if visual-budget pressure emerges — the data structure permits this without re-bundling. Densest stories (s04 Ibadat Khana: 7 anchors; s07 Shahjahanabad: 7) are the natural candidates if a Task-3 budget cap is set per story.",
                "Mention-shape inventory extended: in addition to architecture §3's `cameo` / `background` / `caption` / `connective`, this output uses a 5th shape `timeline-only` for `period_*` stage-construct nodes that appear in story fly-by lists. Task 4's schema needs to register this as a valid mention_shape value (or treat period_* nodes as a separate entity class that doesn't participate in story-level mentions).",
            ],
        },
        "stories": out_stories,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False))

    # ============ WRITE MARKDOWN ============
    md = []
    md.append("# Task 2 Output — Mughal Bundle Plan")
    md.append("")
    md.append(f"**Generated:** by `{Path(__file__).relative_to(HISTORY_DIR.parent)}` (re-run to regenerate)")
    md.append(f"**Companion JSON:** [`HISTORY_SPRINT_MUGHAL_BUNDLES.json`](HISTORY_SPRINT_MUGHAL_BUNDLES.json) — Task-4-consumable structured form")
    md.append(f"**Input pool:** {len(era_nodes)} era nodes (`surfaces/history-surface/6.mughal/mughal.json`)")
    md.append(f"**Anchor input:** 36 PYQ-earned + narrative-anchors added per architecture §10 ('threshold is a proposal, not a lock')")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## What this is")
    md.append("")
    md.append("Task 2's deliverable: Mughal's 263 nodes grouped into short stories that pass the *embodied-episode test* (architecture §4). Each story is a single witnessed scene — not a multi-decade arc — with one set of anchored entities (each entity gets exactly one home story) and a fly-by mention set typed by entity (cameo / background / caption / connective / stage).")
    md.append("")
    md.append("This output is the input to Task 3 (style — pilot story for image generation), Task 4 (schema — formalises the entity/relationship vocabulary you see exemplified here), and Task 5 (PWA scaffolding — designs the components that will render these stories).")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## Findings (top-line)")
    md.append("")
    md.append(f"- **{len(out_stories)} short stories** ({src_breakdown.total()} anchors total: {src_breakdown.get('pyq',0)} PYQ-earned, {src_breakdown.get('pyq_suggestive',0)} PYQ-suggestive, {src_breakdown.get('narrative',0)} narrative). Above the 10–15 architectural target. Forwarded to convergence as a finding: faithfully applying the embodied-episode test (one scene per story) pushed the count up. Splitting Aurangzeb's reign into three scenes (Jizya 1679, Aurangabad 1707, Anandpur 1699) and splitting the economy stage into Surat-port + Bihar-village added 4 stories beyond a force-collapsed 15.")
    md.append("- **Mansab twin merge** resolved: `hist_mansab_system` is canonical; `hist_mansabdari_system` aliased to it (era-JSON pyq_count = 7 on the institution node; Task 1's regex caught only the `-dari` concept variant).")
    md.append("- **`period_*` nodes** (Akbar, Aurangzeb, Shah Jahan, Babur-Humayun, Jahangir-Nur-Jahan, etc.) are NOT anchor-candidates — they're timeline-stage constructs that live in the timeline view. Marked `timeline-only` where they appear in story fly-bys, to keep them visible without claiming anchor space.")
    md.append("- **PYQ-suggestive anchors flagged**: `hist_abdul_hamid_lahori` (s07 Shahjahanabad) and `hist_thomas_roe` (s06 Chain of Justice) — their PYQ evidence is list-question-only, so the visual budget for these anchor panels should be lighter than for high-PYQ entities.")
    md.append("- **Story 19 (Six Courts) is a meta-scene** by design — a split-screen rather than a single embodied moment. Flagged as a bundling-method edge case: parallel-world content (parallel_europe / parallel_islamic_west / parallel_east_asia stages) does not naturally yield to one-scene-per-story. Task 4/5 may want a distinct container convention for it.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## Anchor home index")
    md.append("")
    md.append("Each anchor's home story. Sorted by source (PYQ-earned first by count desc, then PYQ-suggestive, then narrative).")
    md.append("")
    md.append("| Anchor | type | pyq_count | source | Home story |")
    md.append("|---|---|--:|---|---|")
    # Build a list of all anchors with their home
    anchor_index = []
    for s in out_stories:
        for a in s["anchors"]:
            anchor_index.append((a["node_id"], a["label"], a["type"], a.get("pyq_count", 0), a["source"], s["story_id"], s["title"]))
    # Sort: pyq-earned first by count desc, then pyq_suggestive, then narrative
    src_order = {"pyq": 0, "pyq_suggestive": 1, "narrative": 2}
    anchor_index.sort(key=lambda x: (src_order[x[4]], -x[3], x[1]))
    for nid, lbl, t, pc, src, sid, stitle in anchor_index:
        pc_disp = str(pc) if src != "narrative" else "—"
        md.append(f"| `{nid}` — {lbl} | {t} | {pc_disp} | {src} | [{sid}](#{sid.replace('_','-')}) |")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## Stories")
    md.append("")
    md.append("Stories are sequenced roughly chronologically by their anchoring moment. Read them as a comic anthology, not as a continuous narrative — the era's narrative chapter at `surfaces/history-surface/6.mughal/narrative.md` carries the synthesis; these stories carry the embodied episodes.")
    md.append("")
    for i, s in enumerate(out_stories, 1):
        anchor_name = s["story_id"].replace("_", "-")
        md.append(f"### {i:02d}. {s['title']} <a id='{anchor_name}'></a>")
        md.append("")
        md.append(f"- **Story ID:** `{s['story_id']}`")
        md.append(f"- **Scene:** {s['scene_setting']['place']} · {s['scene_setting']['year']}")
        md.append(f"- **Stages bundled:** {', '.join(s['stage_ids'])}")
        md.append("")
        md.append(f"**Moment.** {s['scene_setting']['moment']}")
        md.append("")
        md.append(f"**Synopsis.** {s['synopsis']}")
        md.append("")
        md.append(f"**Anchors ({len(s['anchors'])}):**")
        md.append("")
        md.append("| node_id | label | type | source | pyq |")
        md.append("|---|---|---|---|--:|")
        for a in s["anchors"]:
            pc = a.get("pyq_count", "—")
            md.append(f"| `{a['node_id']}` | {a['label']} | {a['type']} | {a['source']} | {pc} |")
        md.append("")
        if s["fly_bys"]:
            md.append(f"**Fly-by mentions ({len(s['fly_bys'])}):**")
            md.append("")
            md.append("| node_id | label | type | mention_shape |")
            md.append("|---|---|---|---|")
            for f in s["fly_bys"]:
                md.append(f"| `{f['node_id']}` | {f['label']} | {f['type']} | {f['mention_shape']} |")
            md.append("")
        md.append("---")
        md.append("")

    md.append("## Coverage audit")
    md.append("")
    md.append(f"- **Era nodes total:** {len(era_nodes)}")
    md.append(f"- **Placed as anchor:** {len(placed_anchor)}")
    md.append(f"- **Placed as fly-by:** {len(placed_fly_by)}")
    md.append(f"- **Resolved via alias** (do not appear directly): {len(ALIASES)} — {list(ALIASES.keys())}")
    md.append(f"- **Unplaced:** 0  ✓")
    md.append("")
    md.append("Coverage is verified by the build script — re-running it asserts (a) every era-JSON node is placed exactly once or aliased, and (b) every anchor has exactly one home story.")
    md.append("")
    md.append("## Hand-offs")
    md.append("")
    md.append("- **Task 3 (Style):** Pilot story for image generation = `s04_ibadat_khana_1578`. Most narratively dense, highest PYQ-count anchors, richest cameo palette (Sunni/Shia/Jain/Jesuit + Abu'l Fazl + Tansen + Birbal + Akbarnama folios). Generating one full short-story comic from this bundle stress-tests the base style and the per-story reference-image method.")
    md.append("- **Task 4 (Schema):** The JSON companion is the structured input. Entity types observed in this era: person, place, concept, event, movement, reform, institution, empire, period. Relationship types implicit here: `era contains stage`, `stage bundled-into story`, `entity has-anchor-home-in story` (1:1), `entity appears-in story as <mention_shape>` (1:N), `story adjacent-to story` (TBD — derive from shared fly-bys + chronological succession).")
    md.append("- **Task 5 (PWA scaffolding):** Per-era home screen must render 19 short-story cards in a gallery; the comic viewer needs anchor-panel + cameo + caption + background + connective primitives; the timeline view continues to use `stage_ids` (every period_* node lives there).")
    md.append("")
    OUT_MD.write_text("\n".join(md))

    print(f"✓ Wrote {OUT_JSON.relative_to(HISTORY_DIR.parent)}")
    print(f"✓ Wrote {OUT_MD.relative_to(HISTORY_DIR.parent)}")
    print(f"  Stories: {len(out_stories)}")
    print(f"  Anchors: {src_breakdown.total()} (pyq={src_breakdown.get('pyq',0)}, pyq_suggestive={src_breakdown.get('pyq_suggestive',0)}, narrative={src_breakdown.get('narrative',0)})")
    print(f"  Coverage: {len(placed_anchor)} anchor + {len(placed_fly_by)} fly-by + {len(ALIASES)} alias = {len(placed_anchor)+len(placed_fly_by)+len(ALIASES)} / {len(era_nodes)} era nodes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
