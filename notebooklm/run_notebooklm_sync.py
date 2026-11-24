#!/usr/bin/env python3
"""
NotebookLM Automation & Programmatic Sync Utility
Supports both `notebooklm-py` and `notebooklm-mcp-cli` (`nlm`).
"""

import sys
import os
import json
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

def check_cli_tools():
    print("=== Checking NotebookLM Programmatic CLI Tools ===")
    has_nlm = subprocess.run(["which", "nlm"], capture_output=True).returncode == 0
    has_notebooklm = subprocess.run(["which", "notebooklm"], capture_output=True).returncode == 0
    
    print(f"nlm (notebooklm-mcp-cli): {'Available' if has_nlm else 'Not in PATH'}")
    print(f"notebooklm (notebooklm-py): {'Available' if has_notebooklm else 'Not in PATH'}")
    return has_nlm, has_notebooklm

def sync_unit(unit_id):
    manifest_path = BASE_DIR / "downstream" / "notebooklm" / "steering_manifests" / f"unit_{unit_id}_steering_manifest.json"
    if not manifest_path.exists():
        print(f"Error: Manifest for Unit {unit_id} not found.")
        return False

    with open(manifest_path, "r", encoding="utf-8") as f:
        spec = json.load(f)

    source_path = BASE_DIR / spec["source_document"]
    print(f"\n--- Staging Unit {unit_id}: {spec['unit_title']} ---")
    print(f"Source Document: {source_path} ({source_path.stat().st_size} bytes)")
    print(f"Steering Prompt: {spec['audio_overview_spec']['steering_prompt']}")
    print("Ready for automated upload & Audio Overview generation.")
    return True

if __name__ == "__main__":
    check_cli_tools()
    for u in range(1, 8):
        sync_unit(u)
