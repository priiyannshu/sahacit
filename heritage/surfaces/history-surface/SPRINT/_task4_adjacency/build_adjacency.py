"""
Task 4 — Adjacency edge computation for Mughal 19 stories.

Three adjacency types (schema §3.6):
  shared_entity  — entity appears in both stories (auto-detected from bundles JSON)
  causal         — story A's events directly enable/cause story B's events (manual)
  parallel       — simultaneous timeframe, different contexts (manual)

Reciprocal edges: both directions recorded per invariant 5 of the schema.
Output: surfaces/history-surface/6.mughal/adjacency.json
"""

import json, os

BUNDLES = "surfaces/history-surface/SPRINT/HISTORY_SPRINT_MUGHAL_BUNDLES.json"
OUT = "surfaces/history-surface/6.mughal/adjacency.json"

with open(BUNDLES) as f:
    data = json.load(f)

story_ids = [s["story_id"] for s in data["stories"]]

# ── 1. Shared-entity edges (auto) ────────────────────────────────────────────

entity_stories = {}  # node_id -> list of story_ids it appears in (non-timeline-only)
for s in data["stories"]:
    sid = s["story_id"]
    for a in s["anchors"]:
        entity_stories.setdefault(a["node_id"], []).append(sid)
    for fb in s["fly_bys"]:
        if fb.get("mention_shape") != "timeline-only":
            entity_stories.setdefault(fb["node_id"], []).append(sid)

# Build label lookup
entity_labels = {}
for s in data["stories"]:
    for a in s["anchors"]:
        entity_labels[a["node_id"]] = a["label"]
    for fb in s["fly_bys"]:
        entity_labels[fb["node_id"]] = fb["label"]

shared_edges = []  # list of (s1, s2, [node_ids])
cross = {nid: sids for nid, sids in entity_stories.items() if len(sids) >= 2}
pair_shared = {}  # (s1,s2) -> [node_ids]
for nid, sids in cross.items():
    for i, s1 in enumerate(sids):
        for s2 in sids[i+1:]:
            key = tuple(sorted([s1, s2]))
            pair_shared.setdefault(key, []).append(nid)

for (s1, s2), nids in pair_shared.items():
    shared_edges.append((s1, s2, nids))

# ── 2. Causal edges (manual) ─────────────────────────────────────────────────
# Format: (from_story, to_story, note)
# Note: written as "A → B" where A is the cause, B is the consequence.

causal_manual = [
    (
        "s01_panipat_1526",
        "s02_library_stairs_1556",
        "Babur's conquest creates the empire; its fragility (contested legitimacy, Afghan rivals) is why Humayun faces Sher Shah and loses — the exile s02 depicts is the direct consequence of s01's incomplete consolidation.",
    ),
    (
        "s02_library_stairs_1556",
        "s03_mansab_day_1580",
        "Sher Shah's institutional spine built during Humayun's exile — the rupiya, zabt prototype, GT Road, sarai network — is the direct administrative substrate Akbar systematises into the mansabdari-zabt machine in s03.",
    ),
    (
        "s04_ibadat_khana_1578",
        "s05_lahore_1606",
        "Akbar's Ibadat Khana debates (s04) embody the synthesis logic; its theological tensions surface in the next generation — Jahangir inherits a court where sulh-i-kul's limits are contested, and executes Guru Arjan in 1606 (s05).",
    ),
    (
        "s05_lahore_1606",
        "s10_anandpur_1699",
        "Guru Arjan's martyrdom (s05, 1606) begins the Sikh community's turn toward armed sovereignty; Guru Tegh Bahadur's execution under Aurangzeb (referenced in s10) accelerates it — the Khalsa institution at Anandpur 1699 is the direct response.",
    ),
    (
        "s06_chain_of_justice_1617",
        "s07_shahjahanabad_1656",
        "Jahangir's reign consolidates Mughal sovereignty and embeds Persian-émigré commercial and court networks; Shah Jahan inherits this consolidated empire and builds its most visible monuments on that foundation.",
    ),
    (
        "s07_shahjahanabad_1656",
        "s08_delhi_jizya_1679",
        "Dara Shukoh's Sufi-Vedanta program (visible in s07 as the vulnerable alternative) is defeated in the succession war — Aurangzeb's victory directly causes the orthodox reversal and jizya reimposition in s08.",
    ),
    (
        "s08_delhi_jizya_1679",
        "s09_aurangabad_1707",
        "Aurangzeb's political centralisation via orthodox authority (s08) enables his extended Deccan campaigns — the territorial maximum s09 depicts is the direct military consequence of the ideological consolidation s08 shows.",
    ),
    (
        "s08_delhi_jizya_1679",
        "s10_anandpur_1699",
        "Aurangzeb executed Guru Tegh Bahadur in Delhi — this event is the explicit trigger for Guru Gobind Singh's radicalisation and the Khalsa formation at Anandpur 1699 that s10 depicts.",
    ),
    (
        "s09_aurangabad_1707",
        "s17_karnal_1739",
        "Aurangzeb's overextension in the Deccan (territorial max + institutional minimum, s09) generates the jagirdari crisis that s17 identifies as the deep structural cause behind Nadir Shah's ability to sack Delhi at Karnal 1739.",
    ),
    (
        "s11_pratapgarh_1659",
        "s12_raigarh_1674",
        "Shivaji's Pratapgarh assertion (1659) establishes him as a sovereign actor — the recognition earned there is what legitimises the Raigarh coronation (1674) and the formal Maratha state-formation in s12.",
    ),
    (
        "s12_raigarh_1674",
        "s14_surat_port_1670",
        "Shivaji's Surat raids (1664 and 1670) — s14 is the 1670 raid — directly expose the thinness of the imperial military shield over Mughal commerce; the Maratha state built in s12 is the actor doing the exposing.",
    ),
    (
        "s13_ahmadnagar_1595",
        "s09_aurangabad_1707",
        "Mughal Deccan pressure from Ahmadnagar onward (s13, c.1595) steadily erodes the Deccan sultanates; Bijapur (1685) and Golconda (1687) fall in Aurangzeb's campaigns that s09 depicts — the end of the arc s13 begins.",
    ),
    (
        "s15_bihar_village_c1650",
        "s17_karnal_1739",
        "The agrarian engine's slow shift toward revenue-farming and ijaradari (s15 synopsis) is the structural fiscal deterioration that becomes the jagirdari crisis s17 identifies as the deep cause of Mughal collapse.",
    ),
]

# ── 3. Parallel edges (manual) ───────────────────────────────────────────────

parallel_manual = [
    (
        "s03_mansab_day_1580",
        "s04_ibadat_khana_1578",
        "Both are Akbar-stage, c.1575–1585 — the administrative machine (mansab/zabt, s03) and the ideological synthesis (sulh-i-kul/Ibadat Khana, s04) are simultaneous faces of the same empire-building project.",
    ),
    (
        "s03_mansab_day_1580",
        "s13_ahmadnagar_1595",
        "While Akbar's composite-nobility machine reaches peak operation (s03), the Deccan sultanates mount their own parallel synthesis of multilingual courts and military innovation (s13) — two contemporaneous answers to plural governance.",
    ),
    (
        "s04_ibadat_khana_1578",
        "s13_ahmadnagar_1595",
        "Akbar's Ibadat Khana (the Mughal answer to plural governance) and Ahmadnagar's court (the Deccan's own multilingual, multi-ethnic synthesis) are contemporary — both asking the same question from different thrones.",
    ),
    (
        "s07_shahjahanabad_1656",
        "s19_six_courts_parallel",
        "The six-courts meta-scene is set c.1640 — squarely Shah Jahan's reign (1628–1658). s19 is the global frame for the same moment s07 depicts at its Mughal centre.",
    ),
    (
        "s10_anandpur_1699",
        "s11_pratapgarh_1659",
        "Khalsa formation in Punjab (s10) and Maratha military assertion in the Deccan (s11) are near-simultaneous Aurangzeb-era challenges from opposite directions — one devotional turned martial, one already explicitly sovereign.",
    ),
    (
        "s14_surat_port_1670",
        "s15_bihar_village_c1650",
        "Port (s14) and village (s15) are two faces of the same Mughal economy at its mid-century peak — both mughal_economy stage, both showing the revenue system that finances the empire.",
    ),
    (
        "s16_kitabkhana_c1700",
        "s08_delhi_jizya_1679",
        "The Mughal cultural ecology continues diffusing outward into Pahari and Rajasthani courts (s16, c.1700) precisely as the imperial state pulls back from cultural patronage under Aurangzeb (s08, jizya 1679) — culture and state moving in opposite directions at the same time.",
    ),
    (
        "s17_karnal_1739",
        "s18_jaipur_1734",
        "Karnal 1739 (the spectacular collapse) and Jaipur 1734 (successor-state reformation already underway) are near-simultaneous — s18 shows the political reformation proceeding before the symbolic final blow of s17.",
    ),
]

# ── 4. Assemble per-story adjacency lists ────────────────────────────────────

adj = {sid: [] for sid in story_ids}

# shared_entity edges (bidirectional)
for s1, s2, nids in shared_edges:
    entity_notes = ", ".join(f"{entity_labels.get(n, n)} ({n})" for n in nids)
    note = f"Shared entity across stories: {entity_notes}."
    adj[s1].append({"story_id": s2, "adjacency_type": "shared_entity", "entities": nids, "note": note})
    adj[s2].append({"story_id": s1, "adjacency_type": "shared_entity", "entities": nids, "note": note})

# causal edges (directional — A→B means A causes B; reciprocal recorded as causal from B's perspective)
for src, tgt, note in causal_manual:
    adj[src].append({"story_id": tgt, "adjacency_type": "causal", "note": note})
    # reciprocal: B's record points back to A as causal origin
    adj[tgt].append({
        "story_id": src,
        "adjacency_type": "causal",
        "note": f"[Causal origin of this story] {note}",
    })

# parallel edges (bidirectional)
for s1, s2, note in parallel_manual:
    adj[s1].append({"story_id": s2, "adjacency_type": "parallel", "note": note})
    adj[s2].append({"story_id": s1, "adjacency_type": "parallel", "note": note})

# ── 5. Stats & output ────────────────────────────────────────────────────────

total_edges = sum(len(v) for v in adj.values()) // 2  # undirected count
print(f"Shared-entity pairs:  {len(shared_edges)}")
print(f"Causal pairs:         {len(causal_manual)}")
print(f"Parallel pairs:       {len(parallel_manual)}")
print(f"Total unique edges:   {total_edges}")
print()
for sid in story_ids:
    edges = adj[sid]
    types = {}
    for e in edges:
        types[e["adjacency_type"]] = types.get(e["adjacency_type"], 0) + 1
    print(f"  {sid}: {len(edges)} edges {types}")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w") as f:
    json.dump(adj, f, indent=2)
print(f"\nWrote {OUT}")
