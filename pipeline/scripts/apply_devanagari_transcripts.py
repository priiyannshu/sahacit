import json, re, os, sys

sys.path.insert(0, os.path.abspath(".scratch/parts"))
from part0 import map_0
from part1 import map_1
from part2 import map_2
from part3 import map_3

full_map = {}
full_map.update(map_0)
full_map.update(map_1)
full_map.update(map_2)
full_map.update(map_3)

print(f"Total entries in combined map: {len(full_map)}")

with open(".scratch/transcript_hindi.json", "r", encoding="utf-8") as f:
    hi_data = json.load(f)

print(f"Loaded {len(hi_data)} segments from .scratch/transcript_hindi.json")

missing = []
for idx in range(len(hi_data)):
    if idx not in full_map:
        missing.append(idx)

if missing:
    print(f"ERROR: Missing mappings for indices: {missing}")
    sys.exit(1)

# Apply mapping
for idx, item in enumerate(hi_data):
    item["text"] = full_map[idx]

# Check for Arabic characters
arabic_pattern = re.compile(r'[\u0600-\u06FF]')
has_arabic = False
for idx, item in enumerate(hi_data):
    if arabic_pattern.search(item["text"]):
        print(f"Warning: Index {idx} still contains Arabic/Urdu characters: {item['text']}")
        has_arabic = True

if not has_arabic:
    print("SUCCESS: 0 Arabic/Urdu characters found in Hindi transcript! All rendered in Devanagari.")

# Save updated JSON
with open(".scratch/transcript_hindi.json", "w", encoding="utf-8") as f:
    json.dump(hi_data, f, indent=2, ensure_ascii=False)

print("Saved .scratch/transcript_hindi.json successfully.")

# Load English transcript
with open(".scratch/transcript_english.json", "r", encoding="utf-8") as f:
    en_data = json.load(f)

# Inject into HTML
html_path = "evs/downstream/unit_1/index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

js_database = f"""const realTranscripts = {{
  en: {json.dumps(en_data, ensure_ascii=False)},
  hi: {json.dumps(hi_data, ensure_ascii=False)}
}};"""

new_content = re.sub(r'const realTranscripts\s*=\s*\{.*?\n\};', js_database, content, flags=re.DOTALL)

if new_content == content:
    print("WARNING: Regex did not match realTranscripts in index.html!")
else:
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated {html_path} with Devanagari Hindi transcript!")

# Also update artifact if present
artifact_path = "/home/deadpool/.gemini/antigravity-cli/brain/6e481f7f-9ebe-4bf4-8c7f-99d6d1b3697d/unit_1_living_world.html"
if os.path.exists(artifact_path):
    with open(artifact_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated artifact at {artifact_path}")

print("All updates completed successfully!")
