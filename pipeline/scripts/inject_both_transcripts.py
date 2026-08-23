import json, re

html_path = "evs/downstream/unit_1/index.html"
artifact_path = "/home/deadpool/.gemini/antigravity-cli/brain/6e481f7f-9ebe-4bf4-8c7f-99d6d1b3697d/unit_1_living_world.html"

with open(".scratch/transcript_english.json", "r", encoding="utf-8") as f:
    en_trans = json.load(f)

with open(".scratch/transcript_hindi.json", "r", encoding="utf-8") as f:
    hi_trans = json.load(f)

print(f"Injecting: {len(en_trans)} English segments and {len(hi_trans)} Hindi segments")

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the realTranscripts JS object
js_database = f"""const realTranscripts = {{
  en: {json.dumps(en_trans, ensure_ascii=False)},
  hi: {json.dumps(hi_trans, ensure_ascii=False)}
}};"""

content = re.sub(r'const realTranscripts\s*=\s*\{.*?\n\};', js_database, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

with open(artifact_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Both English and Hindi real transcripts injected successfully!")
