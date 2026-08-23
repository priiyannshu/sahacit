#!/usr/bin/env python3
"""Aggregate upstream era + PYQ data into app/pwa/data/ for the client to fetch.

Reads from:
  - eras/<N.era-name>/<era>.json      (11 era graphs)
  - eras/_pyq_interface/gap_fill_nodes.json
  - eras/_pyq_interface/pyq_index.json
  - eras/_pyq_interface/pyq_links.json

Writes to:
  - app/pwa/data/node_lookup.json
  - app/pwa/data/pyq_index.json
  - app/pwa/data/pyq_links.json
  - app/pwa/data/meta.json         (subject/era roster for thrones, counts)

Run whenever upstream changes.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
ERAS_DIR = REPO_ROOT / "app" / "content" / "surfaces" / "history-surface"
PYQI_DIR = REPO_ROOT / "archive" / "_pyq_interface"
OUT_DIR = REPO_ROOT / "app" / "pwa" / "data"

ERAS = [
    ("1.prehistoric",        "prehistoric"),
    ("2.ancient-indus",      "ancient-indus"),
    ("3.ancient-classical",  "ancient-classical"),
    ("4.early-medieval",     "early-medieval"),
    ("5.delhi-sultanate",    "delhi-sultanate"),
    ("6.mughal",             "mughal"),
    ("7.early-colonial",     "early-colonial"),
    ("8.high-colonial",      "high-colonial"),
    ("9.freedom-struggle",   "freedom-struggle"),
    ("10.post-independence", "post-independence"),
    ("11.contemporary",      "contemporary"),
]

# Subject thrones — the 5 live non-era surfaces.
SUBJECT_THRONES = ["polity", "map", "economy", "environment", "science"]
SUBJECT_SURFACE_FILES = {
    "polity":      "pyqs_polity.json",
    "map":         "pyqs_map.json",
    "economy":     "pyqs_economy.json",
    "environment": "pyqs_environment.json",
    "science":     "pyqs_science.json",
}


def build_node_lookup() -> dict:
    """Flatten 11 era JSONs + gap_fill into one {node_id: {...}} lookup."""
    lookup: dict[str, dict] = {}
    total_raw = 0
    dup_count = 0
    for folder, era_key in ERAS:
        path = ERAS_DIR / folder / f"{era_key}.json"
        if not path.exists():
            print(f"  warn: {path} missing, skipping era")
            continue
        data = json.loads(path.read_text())
        stages = {s["id"]: s.get("label", s["id"]) for s in data.get("stages", [])}
        for n in data.get("nodes", []):
            total_raw += 1
            node_id = n["id"]
            prior = lookup.get(node_id)
            entry = {
                "label":   n.get("label", node_id),
                "era":     era_key,
                "stage":   stages.get(n.get("stage"), n.get("stage")),
                "year":    n.get("year"),
                "subject": n.get("subject"),
                "detail":  n.get("detail", ""),
                "also_in_eras": prior["also_in_eras"] + [prior["era"]] if prior else [],
            }
            if prior:
                dup_count += 1
            lookup[node_id] = entry

    gap_path = PYQI_DIR / "gap_fill_nodes.json"
    gap_count = 0
    if gap_path.exists():
        gap_data = json.loads(gap_path.read_text())
        for n in gap_data.get("nodes", []):
            node_id = n["id"]
            lookup[node_id] = {
                "label":   n.get("label", node_id),
                "era":     n.get("era") or "staged",
                "stage":   n.get("stage"),
                "year":    n.get("year"),
                "subject": n.get("subject"),
                "detail":  n.get("detail", ""),
                "also_in_eras": [],
                "_staged":  True,
                "candidate_eras": n.get("candidate_eras", []),
            }
            gap_count += 1
    print(f"  node lookup: {len(lookup)} unique / {total_raw} raw era-nodes "
          f"({dup_count} cross-era dupes; +{gap_count} staged)")
    return lookup


def build_meta(pyq_index: dict, pyq_links: dict) -> dict:
    """Summary for the client: era roster, subject roster, coverage rollup."""
    per_era = {e: 0 for _, e in ERAS}
    per_subject: dict[str, int] = {}
    statuses = {"covered": 0, "partial": 0, "uncovered": 0, "uncurated": 0}
    for p in pyq_index.get("pyqs", []):
        for e in p.get("source_eras", []):
            if e in per_era:
                per_era[e] += 1
        subj = p.get("subject") or "unknown"
        per_subject[subj] = per_subject.get(subj, 0) + 1
        link = pyq_links.get("pyqs", {}).get(str(p["pyq_id"]))
        st = (link or {}).get("status", "uncurated")
        statuses[st] = statuses.get(st, 0) + 1
    return {
        "eras": [e for _, e in ERAS],
        "subject_thrones": SUBJECT_THRONES,
        "per_era_counts": per_era,
        "per_subject_counts": per_subject,
        "coverage_rollup": statuses,
        "total_pyqs": len(pyq_index.get("pyqs", [])),
    }


def build_area_pools(pyq_index: dict) -> dict:
    """Map each area key (era:... / subject:... / corpus) to the list of pyq_ids in it."""
    pools: dict[str, list[str]] = {}
    all_ids = []
    for p in pyq_index.get("pyqs", []):
        pid = str(p["pyq_id"])
        all_ids.append(pid)
        for era in p.get("source_eras", []):
            key = f"era:{era}"
            pools.setdefault(key, []).append(pid)
    for subj, fname in SUBJECT_SURFACE_FILES.items():
        path = PYQI_DIR / fname
        if not path.exists():
            continue
        data = json.loads(path.read_text())
        key = f"subject:{subj}"
        pools[key] = [str(x.get("id")) for x in data.get("pyqs", []) if x.get("id") is not None]
    pools["corpus"] = all_ids
    return pools


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print("==> building game data")
    nodes = build_node_lookup()
    pyq_index = json.loads((PYQI_DIR / "pyq_index.json").read_text())
    pyq_links = json.loads((PYQI_DIR / "pyq_links.json").read_text())
    meta = build_meta(pyq_index, pyq_links)
    areas = build_area_pools(pyq_index)

    (OUT_DIR / "node_lookup.json").write_text(json.dumps(nodes, separators=(",", ":")))
    (OUT_DIR / "pyq_index.json").write_text(json.dumps(pyq_index, separators=(",", ":")))
    (OUT_DIR / "pyq_links.json").write_text(json.dumps(pyq_links, separators=(",", ":")))
    (OUT_DIR / "meta.json").write_text(json.dumps(meta, indent=2))
    (OUT_DIR / "area_pools.json").write_text(json.dumps(areas, separators=(",", ":")))

    total_bytes = sum((OUT_DIR / f).stat().st_size for f in (
        "node_lookup.json", "pyq_index.json", "pyq_links.json", "meta.json", "area_pools.json"))
    print(f"  wrote {OUT_DIR} ({total_bytes/1024:.0f} KB)")
    print(f"  {meta['total_pyqs']} PYQs, coverage {meta['coverage_rollup']}")
    print(f"  areas: {len(areas)} "
          f"(era: {sum(1 for k in areas if k.startswith('era:'))}, "
          f"subject: {sum(1 for k in areas if k.startswith('subject:'))}, "
          f"corpus: 1)")
    sizes = {k: len(v) for k, v in areas.items()}
    print(f"  sample pool sizes: corpus={sizes['corpus']}, "
          f"era:prehistoric={sizes.get('era:prehistoric', 0)}, "
          f"subject:polity={sizes.get('subject:polity', 0)}")


if __name__ == "__main__":
    main()
