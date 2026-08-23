import json, os, re

def load_transcript(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

en_data = load_transcript(".scratch/transcript_english.json")
hi_data = load_transcript(".scratch/transcript_hindi.json")

print(f"Loaded {len(en_data)} English segments and {len(hi_data)} Hindi segments.")

# Read unit_1_living_world.html
html_path = "/home/deadpool/.gemini/antigravity-cli/brain/6e481f7f-9ebe-4bf4-8c7f-99d6d1b3697d/unit_1_living_world.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Store transcripts directly as JSON objects inside a <script> block in the HTML
# so the UI can dynamically render the full real transcript when switching tabs and track audio progress!

js_injection = f"""
// Real NotebookLM Spoken Transcripts
const realTranscripts = {{
  en: {json.dumps(en_data, ensure_ascii=False)},
  hi: {json.dumps(hi_data, ensure_ascii=False)}
}};

function renderRealTeleprompter(lang) {{
  const container = document.getElementById("teleprompter");
  const data = realTranscripts[lang] || [];
  if (data.length === 0) return;
  
  let html = "";
  data.forEach((item, idx) => {{
    const sec = Math.floor(item.start);
    const ts = item.timestamp;
    const txt = item.text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    const activeCls = idx === 0 ? " cue-active" : "";
    html += `<div class="cue-line${{activeCls}}" data-time="${{sec}}" onclick="jumpCue(${{sec}})">` +
            `<span class="cue-time">[${{ts}}]</span> ${{txt}}` +
            `</div>`;
  }});
  container.innerHTML = html;
}}
"""

# Replace in content or append to script
if "// Real NotebookLM Spoken Transcripts" in content:
    content = re.sub(r"// Real NotebookLM Spoken Transcripts.*?function renderRealTeleprompter\(lang\) \{.*?\n\}", js_injection.strip(), content, flags=re.DOTALL)
else:
    content = content.replace("let currentAudioLang = 'en';", js_injection + "\nlet currentAudioLang = 'en';")

# Ensure switchAudioTab calls renderRealTeleprompter(lang)
content = content.replace("function switchAudioTab(lang) {", "function switchAudioTab(lang) {\n  renderRealTeleprompter(lang);")

# Update updateAudioProgress to dynamically highlight current cue line in teleprompter
old_update = """function updateAudioProgress() {
  if (audioEl.duration) {
    const p = (audioEl.currentTime / audioEl.duration) * 100;
    document.getElementById("audioScrubber").value = p;
    const m = Math.floor(audioEl.currentTime / 60);
    const s = Math.floor(audioEl.currentTime % 60).toString().padStart(2, '0');
    const dm = Math.floor(audioEl.duration / 60);
    const ds = Math.floor(audioEl.duration % 60).toString().padStart(2, '0');
    document.getElementById("audioCurTime").textContent = `${m}:${s}`;
    document.getElementById("audioDuration").textContent = `${dm}:${ds}`;
  }
}"""

new_update = """function updateAudioProgress() {
  if (audioEl.duration) {
    const p = (audioEl.currentTime / audioEl.duration) * 100;
    document.getElementById("audioScrubber").value = p;
    const m = Math.floor(audioEl.currentTime / 60);
    const s = Math.floor(audioEl.currentTime % 60).toString().padStart(2, '0');
    const dm = Math.floor(audioEl.duration / 60);
    const ds = Math.floor(audioEl.duration % 60).toString().padStart(2, '0');
    document.getElementById("audioCurTime").textContent = `${m}:${s}`;
    document.getElementById("audioDuration").textContent = `${dm}:${ds}`;
    
    // Highlight active cue in teleprompter
    const curSec = audioEl.currentTime;
    const cueLines = document.querySelectorAll("#teleprompter .cue-line");
    let activeFound = false;
    for (let i = cueLines.length - 1; i >= 0; i--) {
      const lineSec = parseFloat(cueLines[i].getAttribute("data-time"));
      if (!activeFound && curSec >= lineSec) {
        cueLines[i].classList.add("cue-active");
        activeFound = true;
        // Scroll into view if needed
        const tp = document.getElementById("teleprompter");
        const lineTop = cueLines[i].offsetTop - tp.offsetTop;
        if (lineTop < tp.scrollTop || lineTop > tp.scrollTop + tp.clientHeight - 40) {
          tp.scrollTop = lineTop - 40;
        }
      } else {
        cueLines[i].classList.remove("cue-active");
      }
    }
  }
}"""

if old_update in content:
    content = content.replace(old_update, new_update)

# Initial render of teleprompter on load
if "renderRealTeleprompter('en');" not in content:
    content = content.replace("renderHfScene();", "renderHfScene();\nrenderRealTeleprompter('en');")

# Write out updated artifact
with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

# Copy to downstream index.html
with open("/home/deadpool/omniverse/preach/evs/downstream/unit_1/index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully injected real transcripts into unit_1_living_world.html and downstream/unit_1/index.html!")
