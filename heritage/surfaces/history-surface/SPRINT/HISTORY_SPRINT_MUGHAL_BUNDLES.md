# Task 2 Output — Mughal Bundle Plan

**Generated:** by `history-surface/SPRINT/_task2_mughal_bundles/build_bundles.py` (re-run to regenerate)
**Companion JSON:** [`HISTORY_SPRINT_MUGHAL_BUNDLES.json`](HISTORY_SPRINT_MUGHAL_BUNDLES.json) — Task-4-consumable structured form
**Input pool:** 263 era nodes (`surfaces/history-surface/6.mughal/mughal.json`)
**Anchor input:** 36 PYQ-earned + narrative-anchors added per architecture §10 ('threshold is a proposal, not a lock')

---

## What this is

Task 2's deliverable: Mughal's 263 nodes grouped into short stories that pass the *embodied-episode test* (architecture §4). Each story is a single witnessed scene — not a multi-decade arc — with one set of anchored entities (each entity gets exactly one home story) and a fly-by mention set typed by entity (cameo / background / caption / connective / stage).

This output is the input to Task 3 (style — pilot story for image generation), Task 4 (schema — formalises the entity/relationship vocabulary you see exemplified here), and Task 5 (PWA scaffolding — designs the components that will render these stories).

---

## Findings (top-line)

- **19 short stories** (76 anchors total: 31 PYQ-earned, 2 PYQ-suggestive, 43 narrative). Above the 10–15 architectural target. Forwarded to convergence as a finding: faithfully applying the embodied-episode test (one scene per story) pushed the count up. Splitting Aurangzeb's reign into three scenes (Jizya 1679, Aurangabad 1707, Anandpur 1699) and splitting the economy stage into Surat-port + Bihar-village added 4 stories beyond a force-collapsed 15.
- **Mansab twin merge** resolved: `hist_mansab_system` is canonical; `hist_mansabdari_system` aliased to it (era-JSON pyq_count = 7 on the institution node; Task 1's regex caught only the `-dari` concept variant).
- **`period_*` nodes** (Akbar, Aurangzeb, Shah Jahan, Babur-Humayun, Jahangir-Nur-Jahan, etc.) are NOT anchor-candidates — they're timeline-stage constructs that live in the timeline view. Marked `timeline-only` where they appear in story fly-bys, to keep them visible without claiming anchor space.
- **PYQ-suggestive anchors flagged**: `hist_abdul_hamid_lahori` (s07 Shahjahanabad) and `hist_thomas_roe` (s06 Chain of Justice) — their PYQ evidence is list-question-only, so the visual budget for these anchor panels should be lighter than for high-PYQ entities.
- **Story 19 (Six Courts) is a meta-scene** by design — a split-screen rather than a single embodied moment. Flagged as a bundling-method edge case: parallel-world content (parallel_europe / parallel_islamic_west / parallel_east_asia stages) does not naturally yield to one-scene-per-story. Task 4/5 may want a distinct container convention for it.

---

## Anchor home index

Each anchor's home story. Sorted by source (PYQ-earned first by count desc, then PYQ-suggestive, then narrative).

| Anchor | type | pyq_count | source | Home story |
|---|---|--:|---|---|
| `hist_akbar` — Akbar (1556-1605) | person | 17 | pyq | [s04_ibadat_khana_1578](#s04-ibadat-khana-1578) |
| `hist_aurangzeb` — Aurangzeb (1658-1707) | person | 10 | pyq | [s08_delhi_jizya_1679](#s08-delhi-jizya-1679) |
| `hist_jahangir` — Jahangir (1605-1627) | person | 6 | pyq | [s06_chain_of_justice_1617](#s06-chain-of-justice-1617) |
| `hist_mughal_empire` — Mughal Empire | empire | 4 | pyq | [s01_panipat_1526](#s01-panipat-1526) |
| `hist_fatehpur_sikri` — Fatehpur Sikri | place | 3 | pyq | [s04_ibadat_khana_1578](#s04-ibadat-khana-1578) |
| `hist_humayun` — Humayun | person | 3 | pyq | [s02_library_stairs_1556](#s02-library-stairs-1556) |
| `hist_shah_jahan` — Shah Jahan (1628-1658) | person | 3 | pyq | [s07_shahjahanabad_1656](#s07-shahjahanabad-1656) |
| `hist_shivaji` — Shivaji | person | 3 | pyq | [s11_pratapgarh_1659](#s11-pratapgarh-1659) |
| `hist_babur` — Babur (1526-1530) | person | 2 | pyq | [s01_panipat_1526](#s01-panipat-1526) |
| `hist_guru_arjan` — Guru Arjan Dev | person | 2 | pyq | [s05_lahore_1606](#s05-lahore-1606) |
| `hist_jama_masjid_delhi` — Jama Masjid (Delhi) | concept | 2 | pyq | [s07_shahjahanabad_1656](#s07-shahjahanabad-1656) |
| `hist_surat` — Surat | place | 2 | pyq | [s14_surat_port_1670](#s14-surat-port-1670) |
| `hist_tulsidas` — Tulsidas | person | 2 | pyq | [s05_lahore_1606](#s05-lahore-1606) |
| `hist_abul_fazl` — Abu'l Fazl | person | 1 | pyq | [s04_ibadat_khana_1578](#s04-ibadat-khana-1578) |
| `hist_banda_bahadur` — Banda Bahadur | person | 1 | pyq | [s18_jaipur_1734](#s18-jaipur-1734) |
| `hist_dadu_dayal` — Dadu Dayal | person | 1 | pyq | [s05_lahore_1606](#s05-lahore-1606) |
| `hist_mughal_decline` — Decline of Mughal Empire | event | 1 | pyq | [s17_karnal_1739](#s17-karnal-1739) |
| `hist_battle_panipat_1526` — First Battle of Panipat (1526) | event | 1 | pyq | [s01_panipat_1526](#s01-panipat-1526) |
| `hist_gol_gumbaz` — Gol Gumbaz (Bijapur) | concept | 1 | pyq | [s13_ahmadnagar_1595](#s13-ahmadnagar-1595) |
| `hist_guru_gobind_singh` — Guru Gobind Singh | person | 1 | pyq | [s10_anandpur_1699](#s10-anandpur-1699) |
| `hist_guru_tegh_bahadur` — Guru Tegh Bahadur | person | 1 | pyq | [s10_anandpur_1699](#s10-anandpur-1699) |
| `hist_hyderabad_state` — Hyderabad State | empire | 1 | pyq | [s18_jaipur_1734](#s18-jaipur-1734) |
| `hist_ibadat_khana` — Ibadat Khana (House of Worship) | institution | 1 | pyq | [s04_ibadat_khana_1578](#s04-ibadat-khana-1578) |
| `hist_khalsa` — Khalsa | concept | 1 | pyq | [s10_anandpur_1699](#s10-anandpur-1699) |
| `hist_malik_ambar` — Malik Ambar | person | 1 | pyq | [s13_ahmadnagar_1595](#s13-ahmadnagar-1595) |
| `hist_mansab_system` — Mansab System | institution | 1 | pyq | [s03_mansab_day_1580](#s03-mansab-day-1580) |
| `hist_tansen` — Mian Tansen | person | 1 | pyq | [s04_ibadat_khana_1578](#s04-ibadat-khana-1578) |
| `hist_mirabai` — Mirabai | person | 1 | pyq | [s05_lahore_1606](#s05-lahore-1606) |
| `hist_sambhaji` — Sambhaji | person | 1 | pyq | [s09_aurangabad_1707](#s09-aurangabad-1707) |
| `hist_sawai_jai_singh` — Sawai Jai Singh | person | 1 | pyq | [s18_jaipur_1734](#s18-jaipur-1734) |
| `hist_shaikh_ahmad_sirhindi` — Shaikh Ahmad Sirhindi | person | 1 | pyq | [s08_delhi_jizya_1679](#s08-delhi-jizya-1679) |
| `hist_abdul_hamid_lahori` — Abdul Hamid Lahori | person | 1 | pyq_suggestive | [s07_shahjahanabad_1656](#s07-shahjahanabad-1656) |
| `hist_thomas_roe` — Sir Thomas Roe | person | 1 | pyq_suggestive | [s06_chain_of_justice_1617](#s06-chain-of-justice-1617) |
| `hist_afzal_khan` — Afzal Khan | person | — | narrative | [s11_pratapgarh_1659](#s11-pratapgarh-1659) |
| `hist_badshah_nama` — Badshah Nama | concept | — | narrative | [s07_shahjahanabad_1656](#s07-shahjahanabad-1656) |
| `hist_basohli_painting` — Basohli School of Painting | concept | — | narrative | [s16_kitabkhana_c1700](#s16-kitabkhana-c1700) |
| `hist_battle_pratapgarh_1659` — Battle of Pratapgarh (1659) | event | — | narrative | [s11_pratapgarh_1659](#s11-pratapgarh-1659) |
| `hist_bibi_ka_maqbara` — Bibi-ka-Maqbara (Aurangabad) | concept | — | narrative | [s09_aurangabad_1707](#s09-aurangabad-1707) |
| `hist_chand_bibi` — Chand Bibi | person | — | narrative | [s13_ahmadnagar_1595](#s13-ahmadnagar-1595) |
| `hist_char_minar` — Char Minar (Hyderabad) | concept | — | narrative | [s13_ahmadnagar_1595](#s13-ahmadnagar-1595) |
| `hist_dara_shukoh` — Dara Shukoh | person | — | narrative | [s08_delhi_jizya_1679](#s08-delhi-jizya-1679) |
| `hist_fatawa_i_alamgiri` — Fatawa-i-Alamgiri | institution | — | narrative | [s08_delhi_jizya_1679](#s08-delhi-jizya-1679) |
| `hist_francois_bernier` — Francois Bernier | person | — | narrative | [s08_delhi_jizya_1679](#s08-delhi-jizya-1679) |
| `hist_silver_flow_mughal` — Global Silver Flow into Mughal India | concept | — | narrative | [s14_surat_port_1670](#s14-surat-port-1670) |
| `hist_guru_granth_sahib` — Guru Granth Sahib | concept | — | narrative | [s05_lahore_1606](#s05-lahore-1606) |
| `hist_guru_har_govind` — Guru Har Govind | person | — | narrative | [s05_lahore_1606](#s05-lahore-1606) |
| `hist_hundi_system` — Hundi System | concept | — | narrative | [s14_surat_port_1670](#s14-surat-port-1670) |
| `hist_indian_textile_trade` — Indian Textile Trade | concept | — | narrative | [s14_surat_port_1670](#s14-surat-port-1670) |
| `hist_jaimal_patta` — Jaimal Rathore and Patta Sisodiya | person | — | narrative | [s03_mansab_day_1580](#s03-mansab-day-1580) |
| `hist_jesuits` — Jesuits (Society of Jesus) | institution | — | narrative | [s19_six_courts_parallel](#s19-six-courts-parallel) |
| `hist_kangra_school` — Kangra School of Painting | concept | — | narrative | [s16_kitabkhana_c1700](#s16-kitabkhana-c1700) |
| `hist_kathak` — Kathak Dance | concept | — | narrative | [s16_kitabkhana_c1700](#s16-kitabkhana-c1700) |
| `hist_khud_kashta_pahi_kashta` — Khud-kashta vs Pahi-kashta (Peasant Categories) | concept | — | narrative | [s15_bihar_village_c1650](#s15-bihar-village-c1650) |
| `hist_rana_pratap` — Maharana Pratap | person | — | narrative | [s03_mansab_day_1580](#s03-mansab-day-1580) |
| `hist_maratha_empire` — Maratha Empire | empire | — | narrative | [s12_raigarh_1674](#s12-raigarh-1674) |
| `hist_mughal_agrarian_system` — Mughal Agrarian System | concept | — | narrative | [s15_bihar_village_c1650](#s15-bihar-village-c1650) |
| `hist_mughal_irrigation` — Mughal Irrigation | concept | — | narrative | [s15_bihar_village_c1650](#s15-bihar-village-c1650) |
| `hist_mughal_painting` — Mughal Painting Tradition | concept | — | narrative | [s04_ibadat_khana_1578](#s04-ibadat-khana-1578) |
| `hist_mughal_revenue_system` — Mughal Revenue System | concept | — | narrative | [s15_bihar_village_c1650](#s15-bihar-village-c1650) |
| `hist_mughal_zamindars` — Mughal Zamindars | concept | — | narrative | [s15_bihar_village_c1650](#s15-bihar-village-c1650) |
| `hist_muhtasib` — Muhtasib (Aurangzeb's Morality Police) | institution | — | narrative | [s08_delhi_jizya_1679](#s08-delhi-jizya-1679) |
| `hist_nadir_shah_invasion` — Nadir Shah's Invasion | event | — | narrative | [s17_karnal_1739](#s17-karnal-1739) |
| `hist_new_world_crops` — New World Crops in India | concept | — | narrative | [s14_surat_port_1670](#s14-surat-port-1670) |
| `hist_nur_jahan` — Nur Jahan | person | — | narrative | [s06_chain_of_justice_1617](#s06-chain-of-justice-1617) |
| `hist_peacock_throne` — Peacock Throne (Takht-i-Tawus) | concept | — | narrative | [s07_shahjahanabad_1656](#s07-shahjahanabad-1656) |
| `hist_peshwas` — Peshwas | concept | — | narrative | [s12_raigarh_1674](#s12-raigarh-1674) |
| `hist_proto_industrialisation` — Proto-Industrialisation | concept | — | narrative | [s19_six_courts_parallel](#s19-six-courts-parallel) |
| `hist_raja_man_singh` — Raja Man Singh I of Amber | person | — | narrative | [s03_mansab_day_1580](#s03-mansab-day-1580) |
| `hist_shahjahanabad` — Shahjahanabad (Old Delhi) | place | — | narrative | [s07_shahjahanabad_1656](#s07-shahjahanabad-1656) |
| `hist_shahu` — Shahu I | person | — | narrative | [s18_jaipur_1734](#s18-jaipur-1734) |
| `hist_ashtapradhan` — Shivaji's Ashtapradhan (Eight Ministers) | institution | — | narrative | [s12_raigarh_1674](#s12-raigarh-1674) |
| `hist_shivaji_coronation_1674` — Shivaji's Coronation at Raigarh (1674) | event | — | narrative | [s12_raigarh_1674](#s12-raigarh-1674) |
| `hist_sulh_i_kul` — Sulh-i Kul (Absolute Peace) | concept | — | narrative | [s04_ibadat_khana_1578](#s04-ibadat-khana-1578) |
| `hist_taj_mahal` — Taj Mahal | concept | — | narrative | [s07_shahjahanabad_1656](#s07-shahjahanabad-1656) |
| `hist_todar_mal` — Todar Mal | person | — | narrative | [s03_mansab_day_1580](#s03-mansab-day-1580) |
| `hist_ustad_mansur` — Ustad Mansur | person | — | narrative | [s06_chain_of_justice_1617](#s06-chain-of-justice-1617) |

---

## Stories

Stories are sequenced roughly chronologically by their anchoring moment. Read them as a comic anthology, not as a continuous narrative — the era's narrative chapter at `surfaces/history-surface/6.mughal/narrative.md` carries the synthesis; these stories carry the embodied episodes.

### 01. The Field of Panipat — 21 April 1526 <a id='s01-panipat-1526'></a>

- **Story ID:** `s01_panipat_1526`
- **Scene:** Panipat battlefield, north India · 1526
- **Stages bundled:** babur_humayun

**Moment.** Midday — Babur's tulughma curls around Ibrahim Lodi's wings; Ottoman gunners Ustad Ali and Mustafa light the matchlocks; Lodi dies before nightfall.

**Synopsis.** Foundation moment. Gunpowder + flanking divisions decide north India. Babur's foothold becomes the Mughal Empire.

**Anchors (3):**

| node_id | label | type | source | pyq |
|---|---|---|---|--:|
| `hist_babur` | Babur (1526-1530) | person | pyq | 2 |
| `hist_mughal_empire` | Mughal Empire | empire | pyq | 4 |
| `hist_battle_panipat_1526` | First Battle of Panipat (1526) | event | pyq | 1 |

**Fly-by mentions (7):**

| node_id | label | type | mention_shape |
|---|---|---|---|
| `hist_babur_nama` | Babur Nama | concept | caption |
| `hist_chahar_bagh` | Chahar Bagh Garden | concept | caption |
| `hist_bangla_dome` | Bangla Dome | concept | caption |
| `hist_battle_khanwa_1527` | Battle of Khanwa (1527) | event | connective |
| `hist_battle_chanderi_1528` | Battle of Chanderi (1528) | event | connective |
| `hist_battle_ghagra_1529` | Battle of Ghagra (1529) | event | connective |
| `hist_bahadur_shah_gujarat` | Bahadur Shah of Gujarat | person | cameo |

---

### 02. The Library Stairs — Delhi, January 1556 <a id='s02-library-stairs-1556'></a>

- **Story ID:** `s02_library_stairs_1556`
- **Scene:** Din Panah, Delhi · 1556
- **Stages bundled:** babur_humayun

**Moment.** Humayun, having just recaptured Delhi the year before, falls down the staircase of his library on hearing the muezzin. Memory tableaux around him: swimming the Ganga at Chausa 1539, exile at Tahmasp's Safavid court, the painters Mir Sayyid Ali and Khwaja Abdus Samad returning with him from Iran.

**Synopsis.** The exile that becomes inheritance. Humayun's fifteen lost years let Sher Shah build the institutional spine (rupiya, GT Road, sarai, zabt prototype) that Akbar will use.

**Anchors (1):**

| node_id | label | type | source | pyq |
|---|---|---|---|--:|
| `hist_humayun` | Humayun | person | pyq | 3 |

**Fly-by mentions (5):**

| node_id | label | type | mention_shape |
|---|---|---|---|
| `hist_battle_chausa_1539` | Battle of Chausa (1539) | event | connective |
| `hist_battle_kanauj_1540` | Battle of Kanauj / Bilgram (1540) | event | connective |
| `hist_mir_sayyid_ali` | Mir Sayyid Ali Tabrizi | person | cameo |
| `hist_abdus_samad` | Khwaja Abdus Samad | person | cameo |
| `period_babur_humayun` | Babur & Humayun | period | timeline-only |

---

### 03. Mansab Day — Akbar's Court, c.1580 <a id='s03-mansab-day-1580'></a>

- **Story ID:** `s03_mansab_day_1580`
- **Scene:** Diwan-i-Khas, Fatehpur Sikri · 1580
- **Stages bundled:** akbar

**Moment.** Todar Mal presents the zabt revenue sheet; mansab ranks are being inscribed for Iranis, Turanis, Afghans, and Rajputs; Raja Man Singh stands at his 7,000-rank station; through the open gate, the stone elephant statues of Jaimal Rathore and Patta Sisodiya — defenders of Chittor — face the court.

**Synopsis.** The composite-nobility machine assembled in one room. Mansabdari + zabt + watan jagirs + subadari operating together; the conquest map (Gujarat→Bengal→Kashmir→Sindh→Berar→Khandesh) is the result.

**Anchors (5):**

| node_id | label | type | source | pyq |
|---|---|---|---|--:|
| `hist_mansab_system` | Mansab System | institution | pyq | 1 |
| `hist_todar_mal` | Todar Mal | person | narrative | — |
| `hist_raja_man_singh` | Raja Man Singh I of Amber | person | narrative | — |
| `hist_jaimal_patta` | Jaimal Rathore and Patta Sisodiya | person | narrative | — |
| `hist_rana_pratap` | Maharana Pratap | person | narrative | — |

**Fly-by mentions (22):**

| node_id | label | type | mention_shape |
|---|---|---|---|
| `hist_zabt_system` | Zabt Revenue System | concept | caption |
| `hist_subadari_system` | Mughal Provincial Administration (Subadari) | concept | caption |
| `hist_akbar_social_reforms` | Akbar's Social Reforms | reform | connective |
| `hist_battle_second_panipat_1556` | Second Battle of Panipat (1556) | event | connective |
| `hist_hemu` | Hemu (Hem Chandra Vikramaditya) | person | cameo |
| `hist_bairam_khan` | Bairam Khan | person | cameo |
| `hist_adham_khan` | Adham Khan | person | cameo |
| `hist_maham_anaga` | Maham Anaga | person | cameo |
| `hist_mirza_hakim` | Mirza Hakim | person | cameo |
| `hist_raja_bharmal_kachhwaha` | Raja Bharmal Kachhwaha of Amber | person | cameo |
| `hist_bhagwant_das` | Raja Bhagwant Das | person | cameo |
| `hist_siege_chittor_1568` | Siege of Chittor (1568) | event | connective |
| `hist_siege_ranthambhor_1569` | Siege of Ranthambhor (1569) | event | connective |
| `hist_battle_haldighati_1576` | Battle of Haldighati (1576) | event | connective |
| `hist_conquest_gujarat_1572` | Akbar's Conquest of Gujarat (1572-1573) | event | connective |
| `hist_bengal_conquest_1576` | Conquest of Bengal & End of Afghan Rule (1574-1576) | event | connective |
| `hist_kashmir_annexation_1586` | Kashmir Annexation (1586) | event | connective |
| `hist_sindh_annexation_1590` | Sindh Annexation (1590) | event | connective |
| `hist_berar_annexation_1596` | Berar Annexation (1596) | event | connective |
| `hist_khandesh_annexation_1601` | Khandesh Annexation — Asirgarh Siege (1601) | event | connective |
| `hist_rajput_watan_jagirs` | Rajput Watan Jagirs | concept | caption |
| `period_akbar` | Akbar | period | timeline-only |

---

### 04. The Ibadat Khana — Thursday Night, 1578 <a id='s04-ibadat-khana-1578'></a>

- **Story ID:** `s04_ibadat_khana_1578`
- **Scene:** Ibadat Khana, Fatehpur Sikri · 1578
- **Stages bundled:** akbar

**Moment.** A Sunni theologian and a Shia theologian argue at volume about the Imamate; a Jain monk from Kathiawar waits his turn; Rodolfo Acquaviva and Antonio Monserrate sit with illustrated Gospels for the emperor; Abu'l Fazl writes in the corner; Birbal sits across; outside the window, Salim Chishti's white tomb glows; in the adjoining courtyard, Mian Tansen tunes for Darbari Kanada.

**Synopsis.** The architecture of synthesis given a single embodied evening. *Sulh-i-kul* is the operating logic; the Mughal painting tradition is being born in the workshop next door; the *Akbarnama* is being drafted in this same hall.

**Anchors (7):**

| node_id | label | type | source | pyq |
|---|---|---|---|--:|
| `hist_fatehpur_sikri` | Fatehpur Sikri | place | pyq | 3 |
| `hist_ibadat_khana` | Ibadat Khana (House of Worship) | institution | pyq | 1 |
| `hist_akbar` | Akbar (1556-1605) | person | pyq | 17 |
| `hist_abul_fazl` | Abu'l Fazl | person | pyq | 1 |
| `hist_tansen` | Mian Tansen | person | pyq | 1 |
| `hist_sulh_i_kul` | Sulh-i Kul (Absolute Peace) | concept | narrative | — |
| `hist_mughal_painting` | Mughal Painting Tradition | concept | narrative | — |

**Fly-by mentions (23):**

| node_id | label | type | mention_shape |
|---|---|---|---|
| `hist_din_i_ilahi` | Din-i-Ilahi / Tauhid-i-Ilahi | concept | caption |
| `hist_mahzar_1579` | Mahzar (Infallibility Decree, 1579) | concept | caption |
| `hist_first_jesuit_mission_1580` | First Jesuit Mission to Akbar's Court (1580-1583) | event | connective |
| `hist_rodolfo_acquaviva` | Rodolfo Acquaviva | person | cameo |
| `hist_antonio_monserrate` | Antonio Monserrate | person | cameo |
| `hist_faizi` | Faizi (Abu'l Faiz Faizi) | person | cameo |
| `hist_badauni` | Abdul Qadir Badauni | person | cameo |
| `hist_gulbadan_begum` | Gulbadan Begum | person | cameo |
| `hist_birbal_raja` | Raja Birbal (Mahesh Das) | person | cameo |
| `hist_abdur_rahim_khanan` | Abdur Rahim Khan-i-Khanan | person | cameo |
| `hist_farr_i_izadi` | Farr-i Izadi (Divine Light) | concept | caption |
| `hist_akbar_nama` | Akbar Nama | concept | caption |
| `hist_ain_i_akbari` | Ain-i Akbari | concept | caption |
| `hist_hamzanama` | Hamzanama | concept | caption |
| `hist_tutinama` | Tutinama | concept | caption |
| `hist_maktab_khana` | Maktab Khana (Translation Bureau) | institution | caption |
| `hist_mughal_information_system` | Mughal Imperial Information System | institution | caption |
| `hist_tudor_arch` | Tudor Arch (Akbari Architecture) | concept | caption |
| `hist_humayun_tomb` | Humayun's Tomb | concept | caption |
| `hist_persian_language_mughals` | Persian as Court Language | concept | caption |
| `hist_navaratna` | Akbar's Navaratna (Nine Jewels) | concept | caption |
| `hist_mughal_court` | Mughal Court Culture | concept | caption |
| `hist_mughal_court_etiquette` | Mughal Court Etiquette | concept | caption |

---

### 05. Lahore 1606 — The Wound Opens <a id='s05-lahore-1606'></a>

- **Story ID:** `s05_lahore_1606`
- **Scene:** Lahore Fort + Vrindavan memory panel · 1606
- **Stages bundled:** akbar, jahangir_nur_jahan, mughal_culture

**Moment.** Guru Arjan is dragged from Lahore Fort and tortured on Jahangir's order; the *Adi Granth* — which he compiled two years earlier at Amritsar — lies open on a table beside him, its pages showing the verses of Kabir, Namdev, Farid, Surdas; a foreground panel shows Hargobind donning two swords (the doctrine of *miri-piri*); a memory tableau within the scene shows Tulsidas at Varanasi finishing the *Ramcharitmanas*, Mirabai singing in Mewar, Dadu Dayal teaching in Rajasthan; Miyan Mir (the Qadariya sufi who laid the Harmandir Sahib's foundation stone) stands at the edge of the scene in grief.

**Synopsis.** The first Mughal-Sikh fracture, framed against the same century's bhakti compilation that the Adi Granth absorbed. The scripture and the martyrdom in one scene.

**Anchors (6):**

| node_id | label | type | source | pyq |
|---|---|---|---|--:|
| `hist_guru_arjan` | Guru Arjan Dev | person | pyq | 2 |
| `hist_tulsidas` | Tulsidas | person | pyq | 2 |
| `hist_mirabai` | Mirabai | person | pyq | 1 |
| `hist_dadu_dayal` | Dadu Dayal | person | pyq | 1 |
| `hist_guru_har_govind` | Guru Har Govind | person | narrative | — |
| `hist_guru_granth_sahib` | Guru Granth Sahib | concept | narrative | — |

**Fly-by mentions (7):**

| node_id | label | type | mention_shape |
|---|---|---|---|
| `hist_surdas` | Surdas | person | cameo |
| `hist_eknath` | Sant Eknath | person | cameo |
| `hist_tukaram` | Sant Tukaram | person | cameo |
| `hist_ram_das_samarth` | Samarth Ramdas | person | cameo |
| `hist_miyan_mir` | Miyan Mir | person | cameo |
| `hist_qadariya_silsila` | Qadariya Silsila | institution | caption |
| `hist_khusrau` | Prince Khusrau | person | cameo |

---

### 06. The Chain of Justice — Agra Fort, c.1617 <a id='s06-chain-of-justice-1617'></a>

- **Story ID:** `s06_chain_of_justice_1617`
- **Scene:** Agra Fort, riverbank · 1617
- **Stages bundled:** jahangir_nur_jahan

**Moment.** The thirty-yard gold chain hangs from the fort wall to the Yamuna bank, its sixty bells catching the river breeze; Jahangir watches from the jharoka; Nur Jahan inscribes a farman under her own seal at a side desk; Sir Thomas Roe waits in the audience corridor with his East India Company petition; in the open courtyard studio, Ustad Mansur paints a Siberian crane from life; Mirza Ghiyas Beg (Itimad-ud-Daulah) reviews accounts; on the riverbank behind, his own marble tomb is rising under Nur Jahan's commission.

**Synopsis.** Mughal sovereignty presented as personally accountable; a Persian-émigré finance family at the empire's centre; the first English ambassador watching effective power held by a woman.

**Anchors (4):**

| node_id | label | type | source | pyq |
|---|---|---|---|--:|
| `hist_jahangir` | Jahangir (1605-1627) | person | pyq | 6 |
| `hist_thomas_roe` | Sir Thomas Roe | person | pyq_suggestive | 1 |
| `hist_nur_jahan` | Nur Jahan | person | narrative | — |
| `hist_ustad_mansur` | Ustad Mansur | person | narrative | — |

**Fly-by mentions (13):**

| node_id | label | type | mention_shape |
|---|---|---|---|
| `hist_chain_of_justice` | Chain of Justice (Zanjir-i-Adl) | concept | caption |
| `hist_du_aspah_sih_aspah` | Du-aspah Sih-aspah System | concept | caption |
| `hist_itmad_ud_daulah_tomb` | Itmad-ud-Daulah's Tomb (Baby Taj) | concept | caption |
| `hist_itimad_ud_daulah` | Mirza Ghiyas Beg (Itimad-ud-Daulah) | person | cameo |
| `hist_asaf_khan` | Asaf Khan (Mirza Abul Hasan) | person | cameo |
| `hist_islam_khan_chishti` | Islam Khan Chishti | person | cameo |
| `hist_shalimar_bagh_kashmir` | Shalimar Bagh (Kashmir) | concept | caption |
| `hist_akbar_tomb_sikandra` | Akbar's Tomb at Sikandra | concept | caption |
| `hist_amar_singh_mewar` | Amar Singh I of Mewar | person | cameo |
| `hist_shah_jahan_rebellion_1622` | Shah Jahan's Rebellion (1622-1626) | event | connective |
| `hist_mahabat_khan` | Mahabat Khan | person | cameo |
| `hist_jharoka_darshan` | Jharoka Darshan | concept | caption |
| `period_jahangir_nur_jahan` | Jahangir & Nur Jahan | period | timeline-only |

---

### 07. Shahjahanabad, 1656 — The Marble Capital Complete <a id='s07-shahjahanabad-1656'></a>

- **Story ID:** `s07_shahjahanabad_1656`
- **Scene:** Friday-prayer plaza of the Jama Masjid, Old Delhi · 1656
- **Stages bundled:** shah_jahan

**Moment.** The newly opened Jama Masjid catches Friday light; the planned grid of Shahjahanabad spreads beyond; up the Yamuna at Agra, the Taj Mahal (now thirteen years complete) is visible as a marble glimmer; in the adjacent Diwan-i-Khas of the Red Fort, the Peacock Throne sits beneath the inlaid couplet '*Agar firdaus bar roo-e zameen ast…*'; Abdul Hamid Lahori finalizes a *Badshah Nama* folio on a portable desk in the courtyard; Dara Shukoh walks past with his *Sirr-i-Akbar* manuscript open, Jahanara at his side.

**Synopsis.** Shah Jahan's full vision in a single afternoon — Taj, Peacock Throne, Jama Masjid, Shahjahanabad all complete; the Deccan formally vassal since 1636; Dara's Sufi-Vedanta program present but already vulnerable.

**Anchors (7):**

| node_id | label | type | source | pyq |
|---|---|---|---|--:|
| `hist_shahjahanabad` | Shahjahanabad (Old Delhi) | place | narrative | — |
| `hist_shah_jahan` | Shah Jahan (1628-1658) | person | pyq | 3 |
| `hist_abdul_hamid_lahori` | Abdul Hamid Lahori | person | pyq_suggestive | 1 |
| `hist_jama_masjid_delhi` | Jama Masjid (Delhi) | concept | pyq | 2 |
| `hist_taj_mahal` | Taj Mahal | concept | narrative | — |
| `hist_peacock_throne` | Peacock Throne (Takht-i-Tawus) | concept | narrative | — |
| `hist_badshah_nama` | Badshah Nama | concept | narrative | — |

**Fly-by mentions (10):**

| node_id | label | type | mention_shape |
|---|---|---|---|
| `hist_pietra_dura` | Pietra Dura | concept | caption |
| `hist_diwan_i_khas` | Diwan-i Khas | concept | caption |
| `hist_moti_masjid_agra` | Moti Masjid (Agra Fort) | concept | caption |
| `hist_qandahar_question` | Qandahar — Mughal-Safavid Contest | concept | caption |
| `hist_jahangir_tomb` | Jahangir's Tomb at Shahdara (Lahore) | concept | caption |
| `hist_balkh_campaign_1646` | Shah Jahan's Balkh Campaign (1646-1647) | event | connective |
| `hist_treaty_1636_deccan` | Shah Jahan's Deccan Treaty (1636) | event | connective |
| `hist_ahmadnagar_fall_1633` | Extinction of Ahmadnagar (1633) | event | connective |
| `hist_jahanara` | Jahanara Begum | person | cameo |
| `period_shah_jahan` | Shah Jahan | period | timeline-only |

---

### 08. Delhi, March 1679 — The Jizya Proclamation <a id='s08-delhi-jizya-1679'></a>

- **Story ID:** `s08_delhi_jizya_1679`
- **Scene:** Chowk in front of the Red Fort, Delhi · 1679
- **Stages bundled:** aurangzeb, mughal_culture

**Moment.** Aurangzeb's *jizya* farman is read out from the Naubat Khana; the Hindu merchants of Delhi sit in a circle blocking the imperial procession; muhtasibs with whips push at the perimeter; François Bernier watches from a balcony, his notebook open showing the half-drafted theory of imperial land ownership; a courtier's desk holds Shaikh Ahmad Sirhindi's letters arguing *wahdat-ul-shuhud* against the older Chishti *wahdat-ul-wujud*; the Fatawa-i-Alamgiri compilation team works in a side room; Dara Shukoh's portrait hangs in memorial.

**Synopsis.** The reversal at its most legible moment. Theological policy, juridical compendium, observer's theory of despotism, and the Naqshbandi-over-Chishti doctrinal victory all sit in one square.

**Anchors (6):**

| node_id | label | type | source | pyq |
|---|---|---|---|--:|
| `hist_muhtasib` | Muhtasib (Aurangzeb's Morality Police) | institution | narrative | — |
| `hist_fatawa_i_alamgiri` | Fatawa-i-Alamgiri | institution | narrative | — |
| `hist_aurangzeb` | Aurangzeb (1658-1707) | person | pyq | 10 |
| `hist_shaikh_ahmad_sirhindi` | Shaikh Ahmad Sirhindi | person | pyq | 1 |
| `hist_dara_shukoh` | Dara Shukoh | person | narrative | — |
| `hist_francois_bernier` | Francois Bernier | person | narrative | — |

**Fly-by mentions (11):**

| node_id | label | type | mention_shape |
|---|---|---|---|
| `hist_jizya_policy` | Jizya Policy (Abolition → Reimposition → Final Abolition) | concept | caption |
| `hist_bernier_land_ownership` | Bernier's Land Ownership Theory | concept | caption |
| `hist_oriental_despotism` | Oriental Despotism Concept | concept | caption |
| `hist_war_of_succession_1658` | Mughal War of Succession (1657-1658) | event | connective |
| `hist_wahdat_ul_wujud_vs_shuhud` | Wahdat-ul-Wujud vs Wahdat-ul-Shuhud | concept | caption |
| `hist_naqshbandi_silsila` | Naqshbandi Silsila | institution | caption |
| `hist_tavernier` | Jean-Baptiste Tavernier | person | cameo |
| `hist_manucci` | Niccolao Manucci | person | cameo |
| `hist_giovanni_careri` | Giovanni Francesco Gemelli Careri | person | cameo |
| `hist_satnami_revolt_1672` | Satnami Revolt (1672) | event | connective |
| `hist_marwar_mewar_war_1679` | Marwar-Mewar Rajput War (1679-1698) | event | connective |

---

### 09. Aurangabad 1707 — The Empire's Last Camp <a id='s09-aurangabad-1707'></a>

- **Story ID:** `s09_aurangabad_1707`
- **Scene:** Aurangzeb's military camp at Ahmadnagar/Aurangabad · 1707
- **Stages bundled:** aurangzeb

**Moment.** Aurangzeb at 88 lies dying in his campaign tent, dictating his final testament; a campaign map showing eight years of Rajaram's hold at Jinji is pinned to the wall; couriers bring news from the Marwar-Mewar front; in a memory panel, Sambhaji is led to his execution at Tulapur 1689; Bibi-ka-Maqbara — the 'poor man's Taj' — rises in the middle distance; Mir Jumla's old shaft-mining gear lies in a corner.

**Synopsis.** Territorial maximum, institutional minimum. Bijapur (1685) and Golconda (1687) fell, but their fall unleashed the Marathas; Aurangzeb is in the Deccan from 1698 onward and will die there.

**Anchors (2):**

| node_id | label | type | source | pyq |
|---|---|---|---|--:|
| `hist_sambhaji` | Sambhaji | person | pyq | 1 |
| `hist_bibi_ka_maqbara` | Bibi-ka-Maqbara (Aurangabad) | concept | narrative | — |

**Fly-by mentions (13):**

| node_id | label | type | mention_shape |
|---|---|---|---|
| `hist_bijapur_annexation_1685` | Annexation of Bijapur (1685) | event | connective |
| `hist_golconda_annexation_1687` | Annexation of Golconda (1687) | event | connective |
| `hist_ahom_mughal_wars` | Ahom-Mughal Wars (1615-1682) | event | connective |
| `hist_jinji_siege_1690` | Siege of Jinji (1690-1698) | event | connective |
| `hist_rajaram` | Rajaram | person | cameo |
| `hist_ajit_singh_marwar` | Ajit Singh of Marwar | person | cameo |
| `hist_durgadas_rathore` | Durgadas Rathore | person | cameo |
| `hist_jaswant_singh_marwar` | Maharaja Jaswant Singh of Marwar | person | cameo |
| `hist_mir_jumla` | Mir Jumla (Mohammad Syed) | person | cameo |
| `hist_madanna_akkanna` | Madanna and Akkanna (Golconda) | person | cameo |
| `hist_shaista_khan` | Shaista Khan | person | cameo |
| `hist_raja_jai_singh_amber` | Mirza Raja Jai Singh I of Amber | person | cameo |
| `period_aurangzeb` | Aurangzeb | period | timeline-only |

---

### 10. Anandpur, Baisakhi 1699 — The Khalsa Is Born <a id='s10-anandpur-1699'></a>

- **Story ID:** `s10_anandpur_1699`
- **Scene:** Anandpur Sahib, foothills of Punjab · 1699
- **Stages bundled:** aurangzeb, mughal_culture

**Moment.** Guru Gobind Singh under the saffron banner; five volunteers from disparate castes drink amrit from a single iron bowl and emerge as the panj pyaare; the five Ks visible on each; a memory panel within the scene shows Tegh Bahadur's execution at Chandni Chowk in 1675; a forward shadow shows the four sahibzadas' coming deaths (Chamkaur 1705 and the bricking at Sirhind).

**Synopsis.** The Sikh community ceases to be primarily devotional. The Khalsa institution arrives as the direct radicalising response to Aurangzeb's Delhi execution of Tegh Bahadur.

**Anchors (3):**

| node_id | label | type | source | pyq |
|---|---|---|---|--:|
| `hist_guru_gobind_singh` | Guru Gobind Singh | person | pyq | 1 |
| `hist_guru_tegh_bahadur` | Guru Tegh Bahadur | person | pyq | 1 |
| `hist_khalsa` | Khalsa | concept | pyq | 1 |

**Fly-by mentions (2):**

| node_id | label | type | mention_shape |
|---|---|---|---|
| `hist_guru_har_rai` | Guru Har Rai | person | cameo |
| `hist_guru_har_kishan` | Guru Har Kishan | person | cameo |

---

### 11. Pratapgarh, 10 November 1659 — The Bagh-Nakh <a id='s11-pratapgarh-1659'></a>

- **Story ID:** `s11_pratapgarh_1659`
- **Scene:** Forest-pavilion meeting point below Pratapgarh fort, Western Ghats · 1659
- **Stages bundled:** maratha_rise, aurangzeb

**Moment.** Shivaji and Bijapur's general Afzal Khan embrace; the concealed tiger-claw strikes; the Bijapuri retinue is ambushed by Maratha cavalry already deployed in the hills; in a memory panel, Jijabai instructs the young Shivaji in dharma at Poona; his father Shahji Bhonsle's portrait hangs in a corner.

**Synopsis.** Shivaji's signature deed — the moment Mughal contemporaries first recognise him as a sovereign actor, not a raider.

**Anchors (3):**

| node_id | label | type | source | pyq |
|---|---|---|---|--:|
| `hist_shivaji` | Shivaji | person | pyq | 3 |
| `hist_afzal_khan` | Afzal Khan | person | narrative | — |
| `hist_battle_pratapgarh_1659` | Battle of Pratapgarh (1659) | event | narrative | — |

**Fly-by mentions (2):**

| node_id | label | type | mention_shape |
|---|---|---|---|
| `hist_shahji_bhonsle` | Shahji Bhonsle | person | cameo |
| `hist_jijabai` | Jijabai | person | cameo |

---

### 12. Raigarh, 6 June 1674 — Chhatrapati <a id='s12-raigarh-1674'></a>

- **Story ID:** `s12_raigarh_1674`
- **Scene:** Coronation hall, Raigarh fort · 1674
- **Stages bundled:** maratha_rise, aurangzeb

**Moment.** Shivaji is consecrated *Chhatrapati* by Pandit Gagabhatt; the eight ministers of the Ashtapradhan stand each at their station with their books of office; revenue scrolls inscribed *chauth* and *sardeshmukhi* are laid before the throne; memory tableaux show the 1664 sack of Surat, the Treaty of Purandar 1665, and the 1666 escape from Aurangzeb's Agra court; forward shadows show Sambhaji and the future Peshwas.

**Synopsis.** Maratha state-formation made explicit. The Ashtapradhan + chauth/sardeshmukhi system are not raiding but rational bureaucracy.

**Anchors (4):**

| node_id | label | type | source | pyq |
|---|---|---|---|--:|
| `hist_ashtapradhan` | Shivaji's Ashtapradhan (Eight Ministers) | institution | narrative | — |
| `hist_maratha_empire` | Maratha Empire | empire | narrative | — |
| `hist_shivaji_coronation_1674` | Shivaji's Coronation at Raigarh (1674) | event | narrative | — |
| `hist_peshwas` | Peshwas | concept | narrative | — |

**Fly-by mentions (7):**

| node_id | label | type | mention_shape |
|---|---|---|---|
| `hist_chauth` | Chauth | concept | caption |
| `hist_sardeshmukhi` | Sardeshmukhi | concept | caption |
| `hist_surat_sack_1664` | Sack of Surat (1664, 1670) | event | connective |
| `hist_treaty_purandar_1665` | Treaty of Purandar (1665) | event | connective |
| `hist_shivaji_agra_escape_1666` | Shivaji's Agra Visit and Escape (1666) | event | connective |
| `hist_battle_salher_1672` | Battle of Salher (1672) | event | connective |
| `period_maratha_rise` | Maratha Rise | period | timeline-only |

---

### 13. Ahmadnagar 1595 — Chand Bibi at the Walls <a id='s13-ahmadnagar-1595'></a>

- **Story ID:** `s13_ahmadnagar_1595`
- **Scene:** Ramparts of Ahmadnagar Fort · 1595
- **Stages bundled:** deccan_sultanates_tail

**Moment.** Chand Bibi, regent of Ahmadnagar, in armour on the wall directing the defence against Akbar's besieging army; Malik Ambar — the Ethiopian-born vizier who will pioneer Maratha-cavalry guerrilla warfare — coordinates from horseback; in framed inset panels, Muhammad Quli Qutb Shah founds Hyderabad (1591) with the Char Minar at its centre, Ibrahim Adil Shah II composes Dakhini music at Bijapur, and Gol Gumbaz's dome is taking shape; Ibrahim Rauza sits in the same Bijapuri skyline.

**Synopsis.** The Deccan's own synthesis question, running parallel to the Mughal one — multilingual courts, women as effective commanders, African vizier-strategists, an architectural language entirely its own.

**Anchors (4):**

| node_id | label | type | source | pyq |
|---|---|---|---|--:|
| `hist_malik_ambar` | Malik Ambar | person | pyq | 1 |
| `hist_chand_bibi` | Chand Bibi | person | narrative | — |
| `hist_gol_gumbaz` | Gol Gumbaz (Bijapur) | concept | pyq | 1 |
| `hist_char_minar` | Char Minar (Hyderabad) | concept | narrative | — |

**Fly-by mentions (7):**

| node_id | label | type | mention_shape |
|---|---|---|---|
| `hist_bijapur_sultanate` | Bijapur Sultanate (Adil Shahi) | empire | caption |
| `hist_golconda_sultanate` | Golconda Sultanate (Qutb Shahi) | empire | caption |
| `hist_ahmadnagar_sultanate` | Ahmadnagar Sultanate (Nizam Shahi) | empire | caption |
| `hist_ibrahim_adil_shah_ii` | Ibrahim Adil Shah II of Bijapur | person | cameo |
| `hist_muhammad_quli_qutb_shah` | Muhammad Quli Qutb Shah | person | cameo |
| `hist_ibrahim_rauza` | Ibrahim Rauza (Bijapur) | concept | caption |
| `period_deccan_sultanates_tail` | Deccan Sultanates (post-Talikota) | period | timeline-only |

---

### 14. Surat Port, October 1670 — The Second Sack <a id='s14-surat-port-1670'></a>

- **Story ID:** `s14_surat_port_1670`
- **Scene:** Surat harbour, Gujarat · 1670
- **Stages bundled:** mughal_economy

**Moment.** Shivaji's second raid is in progress: customs houses burn; Mughal officials flee; merchants tear hundi paper bills they cannot collect on; bales of *muslin* from Dacca and *chintz* from the Coromandel coast lie split on the quayside; Spanish reales and Mexican 8-real silver coins spill from a money-changer's chest; tomatoes, chillies, and tobacco from American imports sit in a bazaar stall; an English East India Company factor watches from the factory roof.

**Synopsis.** The commercial empire visible at its key port: silver flowing in, cloth flowing out, hundi credit binding it together — and a Maratha raider exposing how thin the imperial military shield over the trade has become.

**Anchors (5):**

| node_id | label | type | source | pyq |
|---|---|---|---|--:|
| `hist_surat` | Surat | place | pyq | 2 |
| `hist_hundi_system` | Hundi System | concept | narrative | — |
| `hist_silver_flow_mughal` | Global Silver Flow into Mughal India | concept | narrative | — |
| `hist_indian_textile_trade` | Indian Textile Trade | concept | narrative | — |
| `hist_new_world_crops` | New World Crops in India | concept | narrative | — |

**Fly-by mentions (6):**

| node_id | label | type | mention_shape |
|---|---|---|---|
| `hist_muslin` | Muslin | concept | caption |
| `hist_chintz` | Chintz | concept | caption |
| `hist_cotton_textile_mughal` | Cotton and Textile Production | concept | caption |
| `hist_masulipatnam` | Masulipatnam (Machlipatnam) | place | background |
| `hist_dacca_textile_centre` | Dacca Textile Centre | place | background |
| `hist_proto_industrialisation` | Proto-Industrialisation | concept | caption |

---

### 15. A Bihar Village — Harvest Day, c.1650 <a id='s15-bihar-village-c1650'></a>

- **Story ID:** `s15_bihar_village_c1650`
- **Scene:** An open-field Mughal-era village, lower Bihar (suba of Bihar) · 1650
- **Stages bundled:** mughal_economy

**Moment.** The *qanungo* records this year's yield against the zabt-fixed assessment; *khud-kashta* resident peasants and *pahi-kashta* outsiders work different strips of the same field; women in the rear cleaning *jins-i-kamil* cash crops (cotton, indigo, sugarcane); zamindar's agents and the village panchayat negotiate the headman's share at a separate corner; a Persian-wheel irrigation device turns above an open well; a small forest community at the field's edge sells honey and lac.

**Synopsis.** The agrarian engine that finances everything else — Akbar's *zabt* still working, layered with caste, gender, kinship, and the slow shift toward revenue-farming that will become *ijaradari* under decline.

**Anchors (5):**

| node_id | label | type | source | pyq |
|---|---|---|---|--:|
| `hist_mughal_revenue_system` | Mughal Revenue System | concept | narrative | — |
| `hist_mughal_agrarian_system` | Mughal Agrarian System | concept | narrative | — |
| `hist_mughal_zamindars` | Mughal Zamindars | concept | narrative | — |
| `hist_mughal_irrigation` | Mughal Irrigation | concept | narrative | — |
| `hist_khud_kashta_pahi_kashta` | Khud-kashta vs Pahi-kashta (Peasant Categories) | concept | narrative | — |

**Fly-by mentions (11):**

| node_id | label | type | mention_shape |
|---|---|---|---|
| `hist_village_panchayat_mughal` | Village Panchayat (Mughal Era) | institution | caption |
| `hist_jins_i_kamil` | Jins-i Kamil (Perfect Crops) | concept | caption |
| `hist_women_agrarian_society` | Women in Mughal Agrarian Society | concept | caption |
| `hist_caste_rural_mughal` | Caste in Mughal Rural Society | concept | caption |
| `hist_jajmani_system` | Jajmani System | concept | caption |
| `hist_tribal_forest_communities` | Forest and Tribal Communities | concept | caption |
| `hist_mughal_population_growth` | Mughal Era Population Growth | concept | caption |
| `hist_coparcenary_inheritance` | Coparcenary Inheritance | concept | caption |
| `hist_peasant_resistance_mughal` | Peasant Resistance | concept | caption |
| `hist_ijaradari` | Ijaradari (Revenue Farming) | concept | caption |
| `period_mughal_economy` | Economy, Society & Trade | period | timeline-only |

---

### 16. The Kitabkhana — A Mughal Studio, c.1700 <a id='s16-kitabkhana-c1700'></a>

- **Story ID:** `s16_kitabkhana_c1700`
- **Scene:** Imperial Kitabkhana, late Mughal Lahore / Delhi; with a side-panel of a Pahari hill studio at Basohli · 1700
- **Stages bundled:** mughal_culture

**Moment.** A master painter finishes a Mughal-style portrait of an Aurangzeb-era noble; in an adjoining panel, a Pahari artist from Basohli works in bold red ground with the new Krishna iconography; further panels: a Kangra atelier under the Katoch rajas in green hills; a Kathak performance in a Rajput courtyard; bound copies of the *Hamzanama* and *Tutinama* on a workshop shelf; Ragamala painting cycles arranged for inspection.

**Synopsis.** The painting tradition Akbar founded has diffused — into Pahari schools, into Rajasthani courts, and into the choreography of court dance. One scene captures the entire post-Akbar visual ecology.

**Anchors (3):**

| node_id | label | type | source | pyq |
|---|---|---|---|--:|
| `hist_kathak` | Kathak Dance | concept | narrative | — |
| `hist_basohli_painting` | Basohli School of Painting | concept | narrative | — |
| `hist_kangra_school` | Kangra School of Painting | concept | narrative | — |

**Fly-by mentions (10):**

| node_id | label | type | mention_shape |
|---|---|---|---|
| `hist_mewar_painting` | Mewar School of Painting | concept | caption |
| `hist_kishangarh_painting` | Kishangarh School — Bani Thani | concept | caption |
| `hist_ragamala_paintings` | Ragamala Paintings | concept | caption |
| `hist_bundi_painting` | Bundi-Kota School (Hadoti) | concept | caption |
| `hist_amber_jaipur_painting` | Amber-Jaipur (Dhundar) School | concept | caption |
| `hist_marwar_painting` | Marwar-Jodhpur School | concept | caption |
| `hist_mughal_manuscripts` | Mughal Manuscript Production | concept | caption |
| `hist_printing_india` | Printing in India | concept | caption |
| `hist_kitabkhana` | Imperial Kitabkhana (Mughal Scriptorium) | institution | caption |
| `period_mughal_culture` | Culture, Art & Religion | period | timeline-only |

---

### 17. Karnal, February 1739 — Nadir Shah's Camp <a id='s17-karnal-1739'></a>

- **Story ID:** `s17_karnal_1739`
- **Scene:** Nadir Shah's tent at Karnal, just after the rout of Muhammad Shah's Mughal army · 1739
- **Stages bundled:** mughal_decline

**Moment.** The Peacock Throne is being loaded onto Persian carts; the Koh-i-Noor changes hands in close-up; in the distance, Delhi burns under the *qatl-e-aam* massacre; a memory panel shows Khafi Khan's 'one pomegranate among a hundred sick' as a caption; Suraj Mal at Bharatpur is sheltering fleeing Mughal nobles in a side-panel; revenue-farming *ijaradari* contracts blow across the camp floor.

**Synopsis.** The structural collapse made spectacular. The jagirdari crisis behind the throne was the deep cause; Nadir's loot is its visible expression.

**Anchors (2):**

| node_id | label | type | source | pyq |
|---|---|---|---|--:|
| `hist_mughal_decline` | Decline of Mughal Empire | event | pyq | 1 |
| `hist_nadir_shah_invasion` | Nadir Shah's Invasion | event | narrative | — |

**Fly-by mentions (3):**

| node_id | label | type | mention_shape |
|---|---|---|---|
| `hist_ijaradari` | Ijaradari (Revenue Farming) | concept | caption |
| `hist_suraj_mal` | Suraj Mal | person | cameo |
| `period_mughal_decline` | Mughal Decline & Successor States | period | timeline-only |

---

### 18. Jaipur 1734 — Sawai Jai Singh at the Jantar Mantar <a id='s18-jaipur-1734'></a>

- **Story ID:** `s18_jaipur_1734`
- **Scene:** Jantar Mantar observatory courtyard, newly founded city of Jaipur · 1734
- **Stages bundled:** mughal_decline

**Moment.** Sawai Jai Singh II at the great Samrat Yantra sundial; on a stone table beside him, a political map of India c.1734 with five highlighted capitals — Murshidabad (Murshid Quli Khan's Bengal), Lucknow/Faizabad (Saadat Khan's Awadh), Hyderabad (Nizam Asaf Jah), Bharatpur (Suraj Mal's Jat state), Anandpur/Sirhind (the Sikh territories where Banda Bahadur had struck sovereign coins); a Maratha cavalry stream pushes north (Bajirao's expansion) as a background tableau; a smudge on the Bengal coast marks the East India Company's growing factories.

**Synopsis.** The successor states presented as a single moment of pluralising sovereignty — not collapse but reformation. Jaipur the planned city is itself an instance of this new political form.

**Anchors (4):**

| node_id | label | type | source | pyq |
|---|---|---|---|--:|
| `hist_sawai_jai_singh` | Sawai Jai Singh | person | pyq | 1 |
| `hist_banda_bahadur` | Banda Bahadur | person | pyq | 1 |
| `hist_shahu` | Shahu I | person | narrative | — |
| `hist_hyderabad_state` | Hyderabad State | empire | pyq | 1 |

**Fly-by mentions (4):**

| node_id | label | type | mention_shape |
|---|---|---|---|
| `hist_bengal_state` | Bengal State | empire | caption |
| `hist_awadh_state` | Awadh State | empire | caption |
| `hist_jat_state` | Jat State | concept | caption |
| `hist_sikh_state` | Sikh Political Formation | concept | caption |

---

### 19. Six Courts, One Hour — Eurasia c.1640 <a id='s19-six-courts-parallel'></a>

- **Story ID:** `s19_six_courts_parallel`
- **Scene:** Split-screen meta-tableau: six framed windows of one composite illustration · 1640
- **Stages bundled:** parallel_europe, parallel_islamic_west, parallel_east_asia

**Moment.** Six contemporaneous courts, all visible at once: (i) Galileo at his telescope in Arcetri (already silenced by the Council of Trent's heirs); (ii) Suleyman's successor era in Istanbul; (iii) Shah Abbas I's Naqsh-i-Jahan square at Isfahan; (iv) the late-Tudor court at Greenwich (Queen Elizabeth's now-historical reign); (v) Tokugawa Iemitsu issuing the *sakoku* seclusion edicts at Edo; (vi) the early-Qing court at Beijing. A village English cricket green and an enclosed field hover at the meta-edge as captions on the era's quiet structural changes.

**Synopsis.** Meta-scene by design (flagged as a bundling-method edge case for convergence): when the cognitive task is 'simultaneity', the embodied-episode test relaxes to split-screen rather than single-stage.

**Anchors (2):**

| node_id | label | type | source | pyq |
|---|---|---|---|--:|
| `hist_jesuits` | Jesuits (Society of Jesus) | institution | narrative | — |
| `hist_proto_industrialisation` | Proto-Industrialisation | concept | narrative | — |

**Fly-by mentions (25):**

| node_id | label | type | mention_shape |
|---|---|---|---|
| `hist_galileo` | Galileo Galilei | person | cameo |
| `hist_copernicus` | Nicolaus Copernicus | person | cameo |
| `hist_council_of_trent` | Council of Trent | event | connective |
| `hist_counter_reformation` | Counter-Reformation | movement | connective |
| `hist_scientific_revolution` | Scientific Revolution | period | stage |
| `hist_queen_elizabeth_i` | Queen Elizabeth I of England | person | cameo |
| `hist_ivan_iv_russia` | Ivan IV "the Terrible" of Russia | person | cameo |
| `pol_hobbes` | Thomas Hobbes | person | cameo |
| `pol_locke` | John Locke | person | cameo |
| `pol_rousseau` | Jean-Jacques Rousseau | person | cameo |
| `hist_enclosure_movement` | Enclosure Movement | concept | caption |
| `hist_agricultural_revolution` | Agricultural Revolution | concept | caption |
| `hist_english_agricultural_revolution` | English Agricultural Revolution | concept | caption |
| `hist_coal_iron` | Coal and Iron Industries | concept | caption |
| `hist_diseases_and_depopulation` | Diseases and Indigenous Depopulation | concept | caption |
| `hist_paper_spread` | Spread of Paper | concept | caption |
| `hist_cricket_origins` | Origins of Cricket | concept | caption |
| `hist_rise_of_novel` | Rise of the Novel in Europe | concept | caption |
| `hist_calico_act_1720` | Calico Act 1720 | reform | connective |
| `hist_suleyman_magnificent` | Suleyman the Magnificent | person | cameo |
| `hist_shah_abbas_safavid` | Shah Abbas I (Safavid) | person | cameo |
| `hist_samurai` | Samurai | concept | caption |
| `hist_qing_dynasty` | Qing Dynasty | empire | caption |
| `hist_tokugawa_japan` | Tokugawa Shogunate | period | stage |
| `period_parallel_islamic_west` | Safavid Persia & Ottoman Empire (parallel) | period | timeline-only |

---

## Coverage audit

- **Era nodes total:** 263
- **Placed as anchor:** 76
- **Placed as fly-by:** 187
- **Resolved via alias** (do not appear directly): 1 — ['hist_mansabdari_system']
- **Unplaced:** 0  ✓

Coverage is verified by the build script — re-running it asserts (a) every era-JSON node is placed exactly once or aliased, and (b) every anchor has exactly one home story.

## Hand-offs

- **Task 3 (Style):** Pilot story for image generation = `s04_ibadat_khana_1578`. Most narratively dense, highest PYQ-count anchors, richest cameo palette (Sunni/Shia/Jain/Jesuit + Abu'l Fazl + Tansen + Birbal + Akbarnama folios). Generating one full short-story comic from this bundle stress-tests the base style and the per-story reference-image method.
- **Task 4 (Schema):** The JSON companion is the structured input. Entity types observed in this era: person, place, concept, event, movement, reform, institution, empire, period. Relationship types implicit here: `era contains stage`, `stage bundled-into story`, `entity has-anchor-home-in story` (1:1), `entity appears-in story as <mention_shape>` (1:N), `story adjacent-to story` (TBD — derive from shared fly-bys + chronological succession).
- **Task 5 (PWA scaffolding):** Per-era home screen must render 19 short-story cards in a gallery; the comic viewer needs anchor-panel + cameo + caption + background + connective primitives; the timeline view continues to use `stage_ids` (every period_* node lives there).
