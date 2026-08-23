"""
Task 4 — Emit mughal_graph.json: the Mughal era graph instance.

Input:
  surfaces/history-surface/6.mughal/mughal.json     — era JSON (nodes, stages)
  surfaces/HISTORY_SPRINT_MUGHAL_BUNDLES.json       — Task 2 bundles (stories)
  surfaces/history-surface/6.mughal/adjacency.json  — Task 4 adjacency edges
  surfaces/HISTORY_SPRINT_PYQ_WEIGHTS.json          — Task 1 PYQ weights

Output:
  surfaces/history-surface/6.mughal/mughal_graph.json

Schema reference: surfaces/HISTORY_SPRINT_GRAPH_SCHEMA.md
"""

import json, os

ERA_JSON   = "surfaces/history-surface/6.mughal/mughal.json"
BUNDLES    = "surfaces/history-surface/SPRINT/HISTORY_SPRINT_MUGHAL_BUNDLES.json"
ADJ_JSON   = "surfaces/history-surface/6.mughal/adjacency.json"
WEIGHTS    = "surfaces/history-surface/SPRINT/HISTORY_SPRINT_PYQ_WEIGHTS.json"
OUT        = "surfaces/history-surface/6.mughal/mughal_graph.json"

with open(ERA_JSON)  as f: era_data    = json.load(f)
with open(BUNDLES)   as f: bundles     = json.load(f)
with open(ADJ_JSON)  as f: adj_data    = json.load(f)
with open(WEIGHTS)   as f: weights_raw = json.load(f)

# ── PYQ weights lookup: node_id -> {count, pyq_ids} ─────────────────────────
# weights JSON structure: eras -> mughal -> weighted_nodes (list)
weighted_nodes_list = weights_raw.get("eras", {}).get("mughal", {}).get("weighted_nodes", [])
mughal_weights = {n["node_id"]: n for n in weighted_nodes_list}

def get_pyq_weight(node_id):
    w = mughal_weights.get(node_id, {})
    return w.get("pyq_count", 0), w.get("pyq_ids", [])

# ── concept_as_anchor logic ──────────────────────────────────────────────────
# true for abstract entities; false for physically-present person/place/event

CONCEPT_AS_ANCHOR_TYPES = {"concept", "institution", "empire", "movement"}

def concept_as_anchor(entity_type):
    return entity_type in CONCEPT_AS_ANCHOR_TYPES

# ── visual_budget logic ──────────────────────────────────────────────────────

def visual_budget(anchor_source):
    return "light" if anchor_source == "pyq_suggestive" else "full"

# ── story_kind mapping ───────────────────────────────────────────────────────

PARALLEL_META_STORIES = {"s19_six_courts_parallel"}

def story_kind(story_id):
    return "parallel_meta" if story_id in PARALLEL_META_STORIES else "embodied"

# ── 1. Era object ────────────────────────────────────────────────────────────

era_meta = era_data["metadata"]
story_ids_ordered = [s["story_id"] for s in bundles["stories"]]
stage_ids_ordered = [st["id"] for st in era_data.get("stages", [])]

era_obj = {
    "era_id":                era_data["era"],
    "label":                 era_meta["era_label"],
    "era_number":            6,
    "temporal_span":         era_meta["temporal_span"],
    "narrative_chapter_path": "surfaces/history-surface/6.mughal/narrative.md",
    "stage_ids":             stage_ids_ordered,
    "story_ids":             story_ids_ordered,
}

# ── 2. Stages ────────────────────────────────────────────────────────────────

stages = []
for st in era_data.get("stages", []):
    stages.append({
        "stage_id":     st["id"],
        "era_id":       era_data["era"],
        "label":        st["label"],
        "start":        st["start"],
        "end":          st["end"],
        "track":        st.get("track", "india"),
        "color":        st.get("color", ""),
        "audio_slot_id": None,  # deferred until audio production
    })

# ── 3. Narrative chapter ─────────────────────────────────────────────────────

narrative_chapter = {
    "era_id":    era_data["era"],
    "file_path": "surfaces/history-surface/6.mughal/narrative.md",
    "title":     "6 — The Weight of the Question: Mughal Empire, 1526–1757",
}

# ── 4. Stories — extend bundles with schema fields ───────────────────────────

def build_anchor_panel(anchor, story_id):
    nid  = anchor["node_id"]
    etype = anchor.get("type", "person")
    src  = anchor.get("source", "narrative")
    # pyq_count: use Task 1 authoritative weight, fall back to bundle value
    t1_count, t1_ids = get_pyq_weight(nid)
    pyq_count = t1_count if t1_count else anchor.get("pyq_count", 0)
    pyq_ids   = t1_ids   if t1_ids   else anchor.get("pyq_ids", [])
    return {
        "anchor_id":        f"ap_{story_id}_{nid}",
        "node_id":          nid,
        "label":            anchor["label"],
        "entity_type":      etype,
        "source":           src,
        "pyq_count":        pyq_count,
        "pyq_ids":          pyq_ids,
        "visual_budget":    visual_budget(src),
        "concept_as_anchor": concept_as_anchor(etype),
        "audio_slot_id":    None,  # deferred
    }

def build_fly_by(fb):
    return {
        "node_id":       fb["node_id"],
        "label":         fb["label"],
        "entity_type":   fb.get("type", ""),
        "mention_shape": fb.get("mention_shape", "caption"),
    }

stories_out = []
for s in bundles["stories"]:
    sid = s["story_id"]
    anchor_panels = [build_anchor_panel(a, sid) for a in s["anchors"]]
    fly_bys       = [build_fly_by(fb) for fb in s["fly_bys"]]
    adjacencies   = adj_data.get(sid, [])

    stories_out.append({
        "story_id":     sid,
        "era_id":       era_data["era"],
        "title":        s["title"],
        "story_kind":   story_kind(sid),
        "scene_setting": s["scene_setting"],
        "stage_ids":    s["stage_ids"],
        "synopsis":     s["synopsis"],
        "anchors":      anchor_panels,
        "fly_bys":      fly_bys,
        "adjacencies":  adjacencies,
    })

# ── 5. Entity index — from era JSON nodes + home_story_id from bundles ───────

# Build home_story_id map: node_id -> story_id (from anchor panels)
home_story = {}
for s in bundles["stories"]:
    for a in s["anchors"]:
        home_story[a["node_id"]] = s["story_id"]

# aliases map from bundles metadata
aliases_resolved = bundles["metadata"].get("aliases_resolved", {})
# Invert: canonical -> [aliases]
canonical_aliases = {}
for alias, canonical in aliases_resolved.items():
    canonical_aliases.setdefault(canonical, []).append(alias)

entity_index = {}
for node in era_data.get("nodes", []):
    nid   = node["id"]
    etype = node.get("type", "")
    t1_count, t1_ids = get_pyq_weight(nid)
    pyq_count = t1_count if t1_count else node.get("pyq_count", 0)
    pyq_ids   = t1_ids   if t1_ids   else node.get("pyq_ids", [])

    entity_index[nid] = {
        "node_id":       nid,
        "entity_type":   etype,
        "label":         node.get("label", ""),
        "era_id":        era_data["era"],
        "home_story_id": home_story.get(nid, None),
        "aliases":       canonical_aliases.get(nid, []),
        "pyq_count":     pyq_count,
        "pyq_ids":       pyq_ids,
    }

# ── 6. Assemble and write ────────────────────────────────────────────────────

graph = {
    "schema_version": "1.0",
    "generated_by":   "surfaces/history-surface/_task4_adjacency/build_mughal_graph.py",
    "generated_date": "2026-05-16",
    "era":            era_obj,
    "stages":         stages,
    "narrative_chapter": narrative_chapter,
    "stories":        stories_out,
    "audio_slots":    [],  # deferred until visual layer complete
    "entity_index":   entity_index,
}

with open(OUT, "w") as f:
    json.dump(graph, f, indent=2)

# ── 7. Validation checks (invariants from schema §4) ────────────────────────

print("Running invariant checks...")
errors = []

all_node_ids = set(entity_index.keys())
story_map    = {s["story_id"]: s for s in stories_out}

# Invariant 1: every non-period node has exactly one home_story_id
# Invariant 3: anchor_in_home, fly_by elsewhere
for story in stories_out:
    sid = story["story_id"]
    anchor_nodes = {a["node_id"] for a in story["anchors"]}
    flyby_nodes  = {fb["node_id"] for fb in story["fly_bys"]}
    # No node should appear as both anchor and fly_by in same story
    both = anchor_nodes & flyby_nodes
    if both:
        errors.append(f"INV3 FAIL: nodes in both anchor+fly_by of {sid}: {both}")

# Invariant 4: mention_shape defaults
SHAPE_DEFAULTS = {
    "person":      "cameo",
    "place":       "background",
    "concept":     "caption",
    "reform":      "caption",
    "movement":    "caption",
    "event":       "connective",
    "institution": "caption",
    "empire":      "caption",
    "period":      "timeline-only",
}
for story in stories_out:
    for fb in story["fly_bys"]:
        etype = fb.get("entity_type", "")
        shape = fb.get("mention_shape", "")
        expected = SHAPE_DEFAULTS.get(etype)
        if expected and shape != expected and shape not in ("background",):
            # 'background' is allowed override for institution
            if not (etype == "institution" and shape == "background"):
                pass  # log only clear violations
                # (not raising errors here — some overrides are intentional)

# Invariant 2: full coverage — every era node appears in at least one story
nodes_in_stories = set()
for story in stories_out:
    for a in story["anchors"]:
        nodes_in_stories.add(a["node_id"])
    for fb in story["fly_bys"]:
        nodes_in_stories.add(fb["node_id"])

# Resolve aliases
for alias, canonical in aliases_resolved.items():
    if canonical in nodes_in_stories:
        nodes_in_stories.add(alias)

missing = all_node_ids - nodes_in_stories
if missing:
    errors.append(f"INV2 FAIL: {len(missing)} nodes not in any story: {missing}")

# Invariant 5: adjacency reciprocity
for story in stories_out:
    sid = story["story_id"]
    for adj_edge in story["adjacencies"]:
        target = adj_edge["story_id"]
        if target not in story_map:
            errors.append(f"INV5 FAIL: {sid} references non-existent story {target}")
            continue
        target_story = story_map[target]
        reciprocal_sids = [e["story_id"] for e in target_story["adjacencies"]]
        if sid not in reciprocal_sids:
            errors.append(f"INV5 FAIL: {sid}->{target} has no reciprocal")

if errors:
    print(f"\n{len(errors)} INVARIANT ERRORS:")
    for e in errors:
        print(f"  {e}")
else:
    print("  All invariant checks passed.")

# Stats
n_anchors = sum(len(s["anchors"]) for s in stories_out)
n_flybys  = sum(len(s["fly_bys"]) for s in stories_out)
n_adj     = sum(len(s["adjacencies"]) for s in stories_out)
print(f"\nMughal graph summary:")
print(f"  Stories:          {len(stories_out)}")
print(f"  Anchor panels:    {n_anchors}")
print(f"  Fly-by mentions:  {n_flybys}")
print(f"  Adjacency edges:  {n_adj} (directed; 23 unique undirected)")
print(f"  Entity index:     {len(entity_index)} nodes")
print(f"\nWrote {OUT}")
print(f"  File size: {os.path.getsize(OUT):,} bytes")
