#!/usr/bin/env python3
"""Extract const DATA from each era HTML and write timeline JSON files.

Outputs:
  app/pwa/data/timeline/era_<N>.json   — per-era node list (minified)
  app/pwa/data/timeline/index.json     — era roster with counts

Run whenever an era HTML is updated.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
SURF_DIR = REPO_ROOT / "app" / "content" / "surfaces" / "history-surface"
OUT_DIR = REPO_ROOT / "app" / "pwa" / "data" / "timeline"

ERAS = [
    (1,  "1.prehistoric",        "prehistoric"),
    (2,  "2.ancient-indus",      "ancient-indus"),
    (3,  "3.ancient-classical",  "ancient-classical"),
    (4,  "4.early-medieval",     "early-medieval"),
    (5,  "5.delhi-sultanate",    "delhi-sultanate"),
    (6,  "6.mughal",             "mughal"),
    (7,  "7.early-colonial",     "early-colonial"),
    (8,  "8.high-colonial",      "high-colonial"),
    (9,  "9.freedom-struggle",   "freedom-struggle"),
    (10, "10.post-independence", "post-independence"),
    (11, "11.contemporary",      "contemporary"),
]

KEEP_FIELDS = {"id", "label", "type", "detail", "importance", "year_approx", "stage",
               "book", "chapter_title", "chapter_file"}


def title_case(s: str) -> str:
    return " ".join(w.capitalize() for w in s.replace("_", " ").replace("-", " ").split())


def extract_data(html_path: Path) -> dict:
    text = html_path.read_text(encoding="utf-8")
    m = re.search(r"const DATA = (\{.*?\});", text, re.DOTALL)
    if not m:
        raise ValueError(f"No DATA found in {html_path}")
    return json.loads(m.group(1))


def normalize_era(raw_era, stages: list) -> dict:
    if isinstance(raw_era, str):
        era_id = raw_era
        start = stages[0]["start"] if stages else 0
        end = stages[-1]["end"] if stages else 0
        color = stages[0].get("color", "#888") if stages else "#888"
        return {
            "id": era_id,
            "label": title_case(era_id),
            "start": start,
            "end": end,
            "color": color,
        }
    return {
        "id": raw_era.get("id", ""),
        "label": raw_era.get("label", ""),
        "start": raw_era.get("start", 0),
        "end": raw_era.get("end", 0),
        "color": raw_era.get("color", "#888"),
    }


def normalize_node(raw: dict) -> dict:
    year_approx = raw.get("year_approx") or raw.get("year")
    importance = raw.get("importance") or "standard"
    node: dict = {
        "id": raw.get("id", ""),
        "label": raw.get("label", ""),
        "type": raw.get("type", ""),
        "detail": raw.get("detail", ""),
        "importance": importance,
        "year_approx": year_approx,
        "stage": raw.get("stage"),
    }
    for f in ("book", "chapter_title", "chapter_file"):
        v = raw.get(f)
        if v:
            node[f] = v
    return node


def build() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    index_eras = []

    for n, folder, fname in ERAS:
        html_path = SURF_DIR / folder / f"{fname}.html"
        if not html_path.exists():
            print(f"  SKIP {folder} (HTML not found)")
            index_eras.append({"n": n, "id": fname, "label": title_case(fname),
                                "start": 0, "end": 0, "color": "#888",
                                "node_count": 0, "available": False})
            continue

        raw = extract_data(html_path)
        stages = raw.get("stages", [])
        era = normalize_era(raw.get("era"), stages)
        all_nodes = [normalize_node(nd) for nd in raw.get("nodes", [])]

        # Separate period nodes; merge their detail into the matching stage.
        stage_by_id = {s["id"]: s for s in stages}
        period_nodes = [nd for nd in all_nodes if nd.get("type") == "period"]
        nodes = [nd for nd in all_nodes if nd.get("type") != "period"]
        for pn in period_nodes:
            s = stage_by_id.get(pn.get("stage", ""))
            if s and pn.get("detail"):
                s["detail"] = pn["detail"]

        available = n != 11

        out = {
            "era": era,
            "stages": stages,
            "nodes": nodes,
        }
        out_path = OUT_DIR / f"era_{n}.json"
        out_path.write_text(json.dumps(out, separators=(",", ":")), encoding="utf-8")

        index_eras.append({
            "n": n,
            "id": era["id"],
            "label": era["label"],
            "start": era["start"],
            "end": era["end"],
            "color": era["color"],
            "node_count": len(nodes),
            "available": available,
        })
        print(f"  era_{n}.json  {era['id']}  {len(nodes)} nodes  ({len(period_nodes)} period nodes merged)  available={available}")

    index_path = OUT_DIR / "index.json"
    index_path.write_text(json.dumps({"eras": index_eras}, separators=(",", ":")), encoding="utf-8")
    print(f"\nWrote {OUT_DIR / 'index.json'} with {len(index_eras)} eras")


if __name__ == "__main__":
    build()
