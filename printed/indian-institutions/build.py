#!/usr/bin/env python3
"""Schema validator, cross-index generator, and Typst PDF compiler for Indian Institutions."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
INST_DIR = DATA_DIR / "institutions"
GEN_DIR = ROOT / "generated"
TYPST_MAIN = ROOT / "typst" / "main.typ"

VALID_CATEGORIES = {
    "Environment and Ecology",
    "Economics",
    "History and Art and Culture",
    "Geography",
    "Current Affairs",
    "Science and Technology",
    "Polity",
}

VALID_LAYOUT_MODES = {"blueprint", "dossier", "compact"}

REQUIRED_TOP_KEYS = {
    "id",
    "order",
    "part",
    "name",
    "acronym",
    "layout_mode",
    "anchor",
    "composition",
    "lifecycle",
    "mandate",
    "genesis",
    "traps",
    "links",
}

REQUIRED_SUBKEYS = {
    "anchor": {
        "legal_status",
        "basis",
        "key_amendments",
        "nodal_ministry",
        "established_year",
        "headquarters",
        "essential_summary",
    },
    "composition": {
        "chairperson",
        "members",
        "eligibility_rules",
        "internal_wings",
    },
    "lifecycle": {
        "appointing_authority",
        "selection_committee",
        "tenure",
        "age_limit",
        "reappointment_and_post_retirement",
        "resignation_to",
        "removal_procedure",
        "funding_and_salary",
    },
    "mandate": {
        "core_functions",
        "power_nature",
        "special_powers",
        "jurisdiction_limits_and_exclusions",
        "reporting_chain",
        "appellate_pathway",
    },
    "genesis": {
        "founding_committee",
        "landmark_cases",
    },
    "traps": {
        "common_traps",
        "twin_comparison",
    },
    "links": {
        "state_counterparts",
        "upsc_categories",
        "linked_acts_and_missions",
    },
}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def validate_institution(record: dict, source_path: Path) -> list[str]:
    errors: list[str] = []
    missing_top = sorted(REQUIRED_TOP_KEYS - set(record.keys()))
    if missing_top:
        errors.append(f"{source_path.name}: missing top keys {missing_top}")
        return errors

    if record["layout_mode"] not in VALID_LAYOUT_MODES:
        errors.append(f"{source_path.name}: invalid layout_mode {record['layout_mode']!r}")

    for block, keys in REQUIRED_SUBKEYS.items():
        if not isinstance(record[block], dict):
            errors.append(f"{source_path.name}: block {block!r} must be an object")
            continue
        missing = sorted(keys - set(record[block].keys()))
        if missing:
            errors.append(f"{source_path.name}: block {block!r} missing keys {missing}")

    cats = record.get("links", {}).get("upsc_categories", [])
    bad_cats = [c for c in cats if c not in VALID_CATEGORIES]
    if not cats:
        errors.append(f"{source_path.name}: links.upsc_categories must be non-empty")
    if bad_cats:
        errors.append(f"{source_path.name}: invalid upsc_categories {bad_cats}")

    return errors


def build_indexes(institutions: list[dict]) -> dict:
    by_legal_status: dict[str, list[dict]] = defaultdict(list)
    by_ministry: dict[str, list[dict]] = defaultdict(list)
    lifecycle_matrix: list[dict] = []
    appellate_matrix: list[dict] = []
    alphabetical: list[dict] = []

    for inst in institutions:
        anchor = inst["anchor"]
        lifecycle = inst["lifecycle"]
        mandate = inst["mandate"]
        ref = {
            "id": inst["id"],
            "order": inst["order"],
            "name": inst["name"],
            "acronym": inst["acronym"],
            "part": inst["part"],
            "legal_status": anchor["legal_status"],
            "basis": anchor["basis"],
            "nodal_ministry": anchor["nodal_ministry"],
        }
        by_legal_status[anchor["legal_status"]].append(ref)
        by_ministry[anchor["nodal_ministry"]].append(ref)
        lifecycle_matrix.append(
            {
                "id": inst["id"],
                "order": inst["order"],
                "name": inst["name"],
                "acronym": inst["acronym"],
                "selection_committee": lifecycle.get("selection_short") or lifecycle["selection_committee"],
                "appointing_authority": lifecycle["appointing_authority"],
                "tenure": lifecycle["tenure"],
                "age_limit": lifecycle["age_limit"],
                "removal": lifecycle.get("removal_short") or lifecycle["removal_procedure"],
                "reappointment": lifecycle.get("reappointment_short") or lifecycle["reappointment_and_post_retirement"],
            }
        )
        appellate_matrix.append(
            {
                "id": inst["id"],
                "order": inst["order"],
                "name": inst["name"],
                "acronym": inst["acronym"],
                "power_nature": mandate["power_nature"],
                "appellate_pathway": mandate["appellate_pathway"],
                "reporting_chain": mandate["reporting_chain"],
            }
        )
        alphabetical.append(ref)

    legal_groups = [
        {"status": status, "items": sorted(items, key=lambda x: x["order"])}
        for status, items in sorted(by_legal_status.items())
    ]
    ministry_groups = [
        {"ministry": ministry, "items": sorted(items, key=lambda x: x["order"])}
        for ministry, items in sorted(by_ministry.items())
    ]
    alphabetical.sort(key=lambda x: x["name"].lower())

    return {
        "legal_status_groups": legal_groups,
        "ministry_groups": ministry_groups,
        "lifecycle_matrix": lifecycle_matrix,
        "appellate_matrix": appellate_matrix,
        "alphabetical": alphabetical,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Indian Institutions Print Atlas PDF")
    parser.add_argument(
        "--output",
        default="indian_institutions.pdf",
        help="Output PDF filename inside generated/",
    )
    parser.add_argument("--no-compile", action="store_true", help="Validate and generate JSON payload only")
    args = parser.parse_args()

    roster = load_json(DATA_DIR / "roster.json")
    skeleton = load_json(DATA_DIR / "state_skeleton.json")

    inst_files = sorted(INST_DIR.glob("*.json"))
    if not inst_files:
        print("Error: no institution JSON files found in data/institutions/", file=sys.stderr)
        return 1

    institutions: list[dict] = []
    all_errors: list[str] = []
    for path in inst_files:
        record = load_json(path)
        all_errors.extend(validate_institution(record, path))
        institutions.append(record)

    if all_errors:
        print("Validation errors:", file=sys.stderr)
        for err in all_errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    institutions.sort(key=lambda r: (r["part"], r["order"]))
    populated_ids = {inst["id"] for inst in institutions}

    # Annotate roster entries with built status so the front roadmap renders live progress cleanly
    for part in roster["parts"]:
        for entry in part["entries"]:
            entry["populated"] = entry["id"] in populated_ids

    payload = {
        "meta": {
            "title": "Indian Institutions",
            "subtitle": "Institutional Architecture, Mandates, Appointments & Jurisdictional Boundaries of the Republic of India",
            "header_right": "Constitutional, Statutory & Regulatory Reference Atlas",
            "total_roster_count": sum(len(p["entries"]) for p in roster["parts"]),
            "populated_count": len(institutions),
        },
        "roster": roster,
        "state_skeleton": skeleton,
        "institutions": institutions,
        "indexes": build_indexes(institutions),
    }

    GEN_DIR.mkdir(parents=True, exist_ok=True)
    payload_path = GEN_DIR / "book_payload.json"
    with payload_path.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)

    print(f"Validated {len(institutions)} institution(s); wrote {payload_path.relative_to(ROOT)}")

    if args.no_compile:
        return 0

    out_pdf = GEN_DIR / args.output
    cmd = [
        "typst",
        "compile",
        "--root",
        str(ROOT),
        "--font-path",
        "/system/fonts",
        str(TYPST_MAIN),
        str(out_pdf),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Typst compile failed:", file=sys.stderr)
        print(res.stdout, file=sys.stderr)
        print(res.stderr, file=sys.stderr)
        return res.returncode

    if res.stderr.strip():
        print("Typst warnings:\n" + res.stderr.strip())
    print(f"Compiled PDF: {out_pdf.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
