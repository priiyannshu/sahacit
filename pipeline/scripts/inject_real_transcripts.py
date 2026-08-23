import json, os, re

def build_teleprompter_html(transcript_path, default_fallback):
    if not os.path.exists(transcript_path):
        return default_fallback
    with open(transcript_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not data:
        return default_fallback
    
    html_lines = []
    for idx, item in enumerate(data):
        sec = int(item["start"])
        ts = item["timestamp"]
        txt = item["text"]
        active_cls = " cue-active" if idx == 0 else ""
        # Escape quotes
        txt_escaped = txt.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        html_lines.append(f'<div class="cue-line{active_cls}" data-time="{sec}" onclick="jumpCue({sec})"><span class="cue-time">[{ts}]</span> {txt_escaped}</div>')
    return "\n".join(html_lines)

print("Inject helper script ready.")
