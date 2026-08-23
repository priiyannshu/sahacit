import os
#!/usr/bin/env python3
"""
Sprint 4 Downstream Generator: Builds NotebookLM manifests, Hyperframes Player, and PWA Quiz Engine.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DOWNSTREAM_DIR = BASE_DIR / "downstream"

def build_notebooklm_assets():
    nlm_dir = DOWNSTREAM_DIR / "notebooklm"
    manifests_dir = nlm_dir / "steering_manifests"
    manifests_dir.mkdir(parents=True, exist_ok=True)

    units_meta = [
        (1, "Living World & Animals", "unit_1_living_world_animals.md",
         "Lead Comparative Biologist", "Skeptical Naturalist",
         "Debate animal sleeping extremes (Sloth 17h vs Elephant 2-4h), tiger night vision (6x), and only 4 poisonous snake species in India."),
        (2, "Flora, Seeds & Forests", "unit_2_flora_seeds_forests.md",
         "Environmental Historian", "Agronomy Analyst",
         "Examine Desert Oak root depth (30x), Pitcher plant sweet scent mechanism, Velcro invention (1948), and Jhum cultivation rules."),
        (3, "Food, Digestion & Diseases", "unit_3_food_digestion_diseases.md",
         "Clinical Epidemiologist", "Culinary Anthropologist",
         "Deep dive into Dr. Beaumont's gastric fistula discoveries, Ronald Ross's 1902 malaria vector breakthrough, and Anaemia hemoglobin levels (12-16 g/dL)."),
        (4, "Shelter & Architecture", "unit_4_shelter_architecture_climate.md",
         "Vernacular Architectural Engineer", "Cultural Geographer",
         "Contrast Leh two-storey stone houses (windowless ground floor) with Assam 10-12ft bamboo stilt houses and Changpa Rebo yak-hair tents."),
        (5, "Water Systems & History", "unit_5_water_systems_conservation.md",
         "Civil Hydraulic Historian", "Fluid Physicist",
         "Explore Al-Biruni's stepwell accounts from 11th century Uzbekistan, Ghadsisar 9-lake network, and Dead Sea 300g salt/L flotation."),
        (6, "Travel, Culture & Space", "unit_6_travel_culture_space.md",
         "Cultural Historian", "Spaceflight Biographer",
         "Profile Bachendri Pal's Everest summit (8848m on 23 May 1984), Sunita Williams zero gravity in orbit, and Pochampally silk weaving."),
        (7, "Quantitative & Spatial Bridge", "unit_7_quantitative_spatial_bridge.md",
         "Cartography Specialist", "Quantitative Logic Coach",
         "Guide through step-by-step map scale calculation (1 cm = 110 m), train average speed formulas, and Indian coastal states geography.")
    ]

    for uid, utitle, ufile, persona_a, persona_b, focus_prompt in units_meta:
        manifest = {
            "unit_id": uid,
            "unit_title": utitle,
            "source_document": f"units/{ufile}",
            "audio_overview_spec": {
                "podcast_title": f"CTET EVS Master Class — Unit {uid}: {utitle}",
                "hosts": {
                    "host_a": persona_a,
                    "host_b": persona_b
                },
                "tone": "Conversational, highly factual, zero-hallucination, interactive debate",
                "steering_prompt": focus_prompt,
                "language_pair": "Bilingual (English with authentic Hindi NCERT terminology anchors)",
                "anti_hallucination_guardrails": [
                    "Adhere strictly to canonical NCERT numerical invariants.",
                    "Do not extrapolate or introduce speculative biology.",
                    "State specific units of measurement clearly."
                ]
            }
        }
        mfile = manifests_dir / f"unit_{uid}_steering_manifest.json"
        with open(mfile, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)

    # Sync runner script
    sync_script = '''#!/usr/bin/env python3
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
    print(f"\\n--- Staging Unit {unit_id}: {spec['unit_title']} ---")
    print(f"Source Document: {source_path} ({source_path.stat().st_size} bytes)")
    print(f"Steering Prompt: {spec['audio_overview_spec']['steering_prompt']}")
    print("Ready for automated upload & Audio Overview generation.")
    return True

if __name__ == "__main__":
    check_cli_tools()
    for u in range(1, 8):
        sync_unit(u)
'''
    with open(nlm_dir / "run_notebooklm_sync.py", "w", encoding="utf-8") as f:
        f.write(sync_script)
    os.chmod(nlm_dir / "run_notebooklm_sync.py", 0o755)
    print("NotebookLM manifests and sync script created.")

def build_hyperframes_player():
    hf_dir = DOWNSTREAM_DIR / "hyperframes"
    hf_dir.mkdir(parents=True, exist_ok=True)

    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hyperframes Interactive EVS Visual State Machine</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="app-container">
    <header class="app-header">
      <h1>🎬 Hyperframes HTML5 Interactive Video & State Machine</h1>
      <p class="subtitle">Zero-Loss CTET EVS Thematic Storyboards (Units 1 to 7)</p>
    </header>

    <main class="main-layout">
      <!-- Unit Selection Bar -->
      <nav class="unit-nav" id="unitNav">
        <button class="unit-btn active" data-unit="1">Unit 1: Animals</button>
        <button class="unit-btn" data-unit="2">Unit 2: Flora & Forests</button>
        <button class="unit-btn" data-unit="3">Unit 3: Food & Health</button>
        <button class="unit-btn" data-unit="4">Unit 4: Shelter</button>
        <button class="unit-btn" data-unit="5">Unit 5: Water Systems</button>
        <button class="unit-btn" data-unit="6">Unit 6: Travel & Space</button>
        <button class="unit-btn" data-unit="7">Unit 7: Quantitative</button>
      </nav>

      <!-- Interactive Scene Player Viewport -->
      <div class="player-container">
        <div class="viewport" id="playerViewport">
          <!-- Dynamic Scene Content Injected by JS -->
        </div>

        <!-- Video Timeline Controls -->
        <div class="player-controls">
          <button id="btnPrev" class="ctrl-btn">⏮ Prev Scene</button>
          <button id="btnPlayPause" class="ctrl-btn play-btn">▶ Play Animation</button>
          <button id="btnNext" class="ctrl-btn">Next Scene ⏭</button>
          <div class="timeline-bar">
            <div class="timeline-progress" id="timelineProgress"></div>
          </div>
          <span class="scene-counter" id="sceneCounter">Scene 1 / 4</span>
        </div>
      </div>

      <!-- Bilingual Script & Narration Teleprompter -->
      <section class="teleprompter-card">
        <h3>🎙️ Synchronized Bilingual Audio Narration Script</h3>
        <p id="narrationTextEn" class="narration-en"></p>
        <p id="narrationTextHi" class="narration-hi"></p>
      </section>
    </main>
  </div>
  <script src="player.js"></script>
</body>
</html>'''

    css_content = '''* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background: #0b0f19; color: #f8fafc; line-height: 1.5; }
.app-container { max-width: 1200px; margin: 0 auto; padding: 20px; }
.app-header { text-align: center; margin-bottom: 20px; border-bottom: 1px solid #1e293b; padding-bottom: 15px; }
.app-header h1 { font-size: 26px; color: #38bdf8; }
.subtitle { font-size: 14px; color: #94a3b8; }
.unit-nav { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 20px; justify-content: center; }
.unit-btn { background: #1e293b; color: #cbd5e1; border: 1px solid #334155; padding: 8px 16px; border-radius: 20px; cursor: pointer; font-size: 13px; font-weight: 500; transition: all 0.2s; }
.unit-btn:hover { background: #334155; }
.unit-btn.active { background: #0284c7; color: #fff; border-color: #38bdf8; box-shadow: 0 0 10px rgba(56, 189, 248, 0.4); }
.player-container { background: #020617; border: 2px solid #1e293b; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
.viewport { height: 420px; position: relative; padding: 30px; display: flex; flex-direction: column; justify-content: center; align-items: center; background: radial-gradient(circle at center, #1e293b 0%, #020617 100%); }
.player-controls { display: flex; align-items: center; gap: 15px; background: #0f172a; padding: 12px 20px; border-top: 1px solid #1e293b; }
.ctrl-btn { background: #1e293b; color: #fff; border: 1px solid #334155; padding: 6px 14px; border-radius: 6px; cursor: pointer; font-size: 13px; font-weight: 600; }
.ctrl-btn:hover { background: #334155; }
.play-btn { background: #0284c7; border-color: #38bdf8; }
.timeline-bar { flex: 1; height: 6px; background: #334155; border-radius: 3px; overflow: hidden; cursor: pointer; }
.timeline-progress { width: 25%; height: 100%; background: #38bdf8; transition: width 0.3s; }
.scene-counter { font-size: 12px; color: #94a3b8; font-weight: bold; }
.teleprompter-card { background: #0f172a; border: 1px solid #1e293b; border-radius: 12px; padding: 20px; margin-top: 20px; }
.teleprompter-card h3 { font-size: 16px; color: #38bdf8; margin-bottom: 10px; }
.narration-en { font-size: 15px; color: #f1f5f9; margin-bottom: 8px; font-weight: 500; }
.narration-hi { font-size: 15px; color: #cbd5e1; font-style: italic; }
.visual-card { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 25px; max-width: 650px; width: 100%; text-align: center; animation: fadeIn 0.5s ease-out; }
.card-title { font-size: 22px; color: #38bdf8; margin-bottom: 12px; font-weight: bold; }
.card-badge { display: inline-block; background: #0369a1; color: #e0f2fe; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: bold; margin-bottom: 15px; }
.card-facts { text-align: left; margin: 15px 0; font-size: 14px; color: #e2e8f0; line-height: 1.8; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }'''

    js_content = '''const scenesData = {
  1: [
    { title: "Sloth Chronobiology", badge: "Unit 1 Invariant", facts: ["• Sleeps 17 hours upside down on tree branches", "• Lifespan ~40 years; moves to only ~8 trees", "• Descends once weekly to relieve itself", "• Proficient swimmer"], en: "The sloth is an arboreal folivore that sleeps for almost 17 hours hanging upside down. It lives for about 40 years, moving to only about 8 trees in its lifetime.", hi: "स्लॉथ भालू जैसा दिखता है पर भालू नहीं है। यह लगभग 17 घंटे पेड़ से उल्टा लटककर सोता है और 40 वर्ष के जीवन में केवल 8 पेड़ों पर ही जाता है।" },
    { title: "Elephant Matriarchy", badge: "Unit 1 Invariant", facts: ["• Herd led by oldest female (10-12 members)", "• Adult eats >100 kg leaves/day; sleeps 2-4 hrs", "• 3-month calf weighs ~200 kg", "• Males leave at 14-15 years"], en: "An elephant herd consists only of adult females and calves, guided by the oldest matriarch. Adults eat over 100 kg of foliage and sleep just 2 to 4 hours daily.", hi: "हाथियों के झुंड में केवल हथनियां और बच्चे होते हैं। झुंड की मुखिया सबसे बुजुर्ग हथनी होती है। बड़ा हाथी एक दिन में 100 किग्रा से ज्यादा पत्ते खाता है।" }
  ],
  2: [
    { title: "Desert Oak Ecology", badge: "Unit 2 Invariant", facts: ["• Found in Australian deserts", "• Roots reach ~30x tree height to water table", "• Water stored in tree trunk", "• Locals use thin pipes to drink"], en: "The Desert Oak grows in Australian deserts with sparse foliage. Its taproots penetrate 30 times its height deep into the ground until they reach water.", hi: "रेगिस्तानी ओक ऑस्ट्रेलिया के रेगिस्तान में पाया जाता है। इसकी जड़ें पेड़ की ऊँचाई से लगभग 30 गुना गहराई तक जमीन में जाती हैं और तने में पानी जमा होता है।" },
    { title: "Jhum Cultivation Rules", badge: "Unit 2 Invariant", facts: ["• Practiced in hilly Mizoram", "• Weeds are CUT and BURNT (never uprooted)", "• Ash enriches soil minerals", "• Soil is lightly furrowed, never ploughed"], en: "In Mizoram's Jhum farming, weeds and bamboos are cut and burnt to create mineral-rich ash. The soil is lightly furrowed without heavy ploughing.", hi: "मिज़ोरम की झूम खेती में खरपतवार को उखाड़ते नहीं, काटकर जला देते हैं। राख जमीन को उपजाऊ बनाती है और जमीन को जोता नहीं, सिर्फ हल्का हिलाया जाता है।" }
  ],
  3: [
    { title: "Malaria & Ronald Ross", badge: "Unit 3 Invariant", facts: ["• Transmitted by Female Anopheles mosquito", "• Causes shivering chills and high fever", "• Cured by Cinchona tree bark (Quinine)", "• Ronald Ross 1902 Nobel Prize"], en: "Ronald Ross discovered that malaria is spread by the female Anopheles mosquito. The historic cure is derived from the bark of the Cinchona tree.", hi: "रोनाल्ड रॉस ने 1902 में साबित किया कि मलेरिया मादा एनाफिलीज़ मच्छर से फैलता है। इसका पारंपरिक उपचार सिनकोना पेड़ की छाल से किया जाता है।" },
    { title: "Anaemia & Iron Vault", badge: "Unit 3 Invariant", facts: ["• Normal Haemoglobin: 12 to 16 g/dL", "• Caused by deficiency of iron", "• Dietary remedies: Amla, Jaggery, Spinach", "• Starch test: Iodine -> Blue-Black"], en: "Anaemia is caused by low haemoglobin or iron deficiency. Standard remedies include consuming Amla, Jaggery, and green leafy vegetables.", hi: "एनीमिया खून में हीमोग्लोबिन या आयरन की कमी से होता है। सामान्य स्तर 12 से 16 g/dL होता है और इसका मुख्य उपचार आंवला, गुड़ और हरी पत्तेदार सब्जियाँ हैं।" }
  ],
  4: [
    { title: "Assam vs Leh Shelters", badge: "Unit 4 Invariant", facts: ["• Assam: 10-12 ft on bamboo pillars (sloping roof)", "• Leh: 2-storey stone houses (windowless ground floor)", "• Changpa Rebo: Yak hair conical tents at 5000m", "• Pashmina: Warmth of 6 sweaters (250 hrs weaving)"], en: "Assam houses stand 10 to 12 feet high on bamboo stilts, while Leh houses feature two-storey stone construction with windowless livestock ground floors.", hi: "असम में घर 10-12 फीट ऊँचे बांस के खंभों पर बनते हैं। लेह में दो मंजिला पत्थर के मकान होते हैं जिनकी निचली मंजिल पर कोई खिड़की नहीं होती।" }
  ],
  5: [
    { title: "Ghadsisar & Dead Sea", badge: "Unit 5 Invariant", facts: ["• Ghadsisar: 9 interconnected lakes in Jaisalmer", "• Al-Biruni: Documented stepwells from Uzbekistan", "• Dead Sea: 300g salt per 1 liter water", "• Humans float comfortably without sinking"], en: "The Dead Sea contains approximately 300 grams of salt per liter of water, allowing humans to float buoyant on its surface.", hi: "मृत सागर दुनिया का सबसे नमकीन सागर है जिसमें 1 लीटर पानी में 300 ग्राम नमक होता है। इसमें मनुष्य पानी पर तैरता रहता है।" }
  ],
  6: [
    { title: "Bachendri Pal Summit", badge: "Unit 6 Invariant", facts: ["• Reached Everest (Sagarmatha) 23 May 1984 1:07 PM", "• Altitude 8848 meters (43 mins on peak)", "• 1st Indian woman / 5th in the world", "• Karnam Malleswari: 130 kg lift, 29 medals"], en: "Bachendri Pal summited Mount Everest on 23 May 1984 at 1:07 PM, standing on the 8848-meter peak for 43 minutes as the first Indian woman.", hi: "बछेंद्री पाल 23 मई 1984 को दोपहर 1:07 बजे माउंट एवरेस्ट (सागरमाथा - 8848 मीटर) पर कदम रखने वाली पहली भारतीय महिला बनीं।" }
  ],
  7: [
    { title: "Map Scales & Coastal Vectors", badge: "Unit 7 Invariant", facts: ["• Scale Formula: Distance = cm × (m/cm) ÷ 1000", "• Example: 15 cm × 110 m = 1.65 km", "• Arabian Sea: Gujarat, Maharashtra, Goa, Karnataka, Kerala", "• Speed: Distance / Time; km/h to m/s = × 5/18"], en: "Map distances convert directly to ground kilometers using scale factors. The Arabian Sea coastline spans Gujarat, Maharashtra, Goa, Karnataka, and Kerala.", hi: "मानचित्र पैमाना जमीन की वास्तविक दूरी को दर्शाता है। अरब सागर के तटवर्ती राज्यों में गुजरात, महाराष्ट्र, गोवा, कर्नाटक और केरल शामिल हैं।" }
  ]
};

let currentUnit = 1;
let currentSceneIdx = 0;

function renderScene() {
  const scenes = scenesData[currentUnit] || scenesData[1];
  if (currentSceneIdx >= scenes.length) currentSceneIdx = 0;
  const s = scenes[currentSceneIdx];

  const vp = document.getElementById("playerViewport");
  vp.innerHTML = `
    <div class="visual-card">
      <span class="card-badge">${s.badge}</span>
      <h2 class="card-title">${s.title}</h2>
      <div class="card-facts">
        ${s.facts.map(f => `<div>${f}</div>`).join('')}
      </div>
    </div>
  `;

  document.getElementById("narrationTextEn").textContent = s.en;
  document.getElementById("narrationTextHi").textContent = s.hi;
  document.getElementById("sceneCounter").textContent = `Scene ${currentSceneIdx + 1} / ${scenes.length}`;
  document.getElementById("timelineProgress").style.width = `${((currentSceneIdx + 1) / scenes.length) * 100}%`;
}

document.querySelectorAll(".unit-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".unit-btn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    currentUnit = parseInt(btn.dataset.unit);
    currentSceneIdx = 0;
    renderScene();
  });
});

document.getElementById("btnNext").addEventListener("click", () => {
  const scenes = scenesData[currentUnit];
  currentSceneIdx = (currentSceneIdx + 1) % scenes.length;
  renderScene();
});

document.getElementById("btnPrev").addEventListener("click", () => {
  const scenes = scenesData[currentUnit];
  currentSceneIdx = (currentSceneIdx - 1 + scenes.length) % scenes.length;
  renderScene();
});

renderScene();
'''

    with open(hf_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(hf_dir / "styles.css", "w", encoding="utf-8") as f:
        f.write(css_content)
    with open(hf_dir / "player.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    print("Hyperframes player HTML/CSS/JS built.")

def build_pwa_quiz_engine():
    quiz_dir = DOWNSTREAM_DIR / "pwa_quiz"
    quiz_dir.mkdir(parents=True, exist_ok=True)

    # Load master PYQs
    with open(BASE_DIR / "data" / "pyq_bank" / "pyq_master_bank.json", "r", encoding="utf-8") as f:
        pyqs = json.load(f)

    with open(quiz_dir / "questions.json", "w", encoding="utf-8") as f:
        json.dump(pyqs, f, indent=2, ensure_ascii=False)

    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CTET EVS 15-Mark Interactive Mock Exam</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="quiz-container">
    <header class="quiz-header">
      <div class="header-left">
        <h1>🎯 CTET EVS Paper-1 Content Mock Exam</h1>
        <span class="exam-tag">Section III Non-Pedagogy (15 Marks Standard)</span>
      </div>
      <div class="header-right">
        <div class="timer" id="timer">⏱ 15:00</div>
      </div>
    </header>

    <div class="quiz-body" id="quizBody">
      <div class="question-card" id="questionCard">
        <!-- Question injected here -->
      </div>
      
      <div class="navigation-bar">
        <button class="nav-btn" id="btnPrevQ" disabled>← Previous</button>
        <div class="progress-indicator" id="progressIndicator">Question 1 of 15</div>
        <button class="nav-btn" id="btnNextQ">Next →</button>
        <button class="submit-btn" id="btnSubmit">Submit Exam 🏁</button>
      </div>
    </div>

    <div class="result-modal hidden" id="resultModal">
      <!-- Exam Results Summary -->
    </div>
  </div>
  <script src="quiz_engine.js"></script>
</body>
</html>'''

    css_content = '''* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0f172a; color: #f8fafc; min-height: 100vh; padding: 20px; display: flex; justify-content: center; }
.quiz-container { max-width: 900px; width: 100%; background: #1e293b; border-radius: 16px; border: 1px solid #334155; padding: 25px; box-shadow: 0 15px 35px rgba(0,0,0,0.4); display: flex; flex-direction: column; }
.quiz-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #334155; padding-bottom: 15px; margin-bottom: 20px; }
.quiz-header h1 { font-size: 20px; color: #38bdf8; }
.exam-tag { font-size: 12px; color: #94a3b8; }
.timer { background: #0284c7; color: #fff; font-weight: bold; font-size: 18px; padding: 6px 14px; border-radius: 8px; font-family: monospace; }
.question-card { background: #0f172a; border-radius: 12px; padding: 25px; border: 1px solid #334155; margin-bottom: 20px; min-height: 350px; }
.q-title-en { font-size: 16px; font-weight: 600; color: #f8fafc; margin-bottom: 8px; line-height: 1.5; }
.q-title-hi { font-size: 15px; color: #cbd5e1; margin-bottom: 20px; font-style: italic; border-bottom: 1px dashed #334155; padding-bottom: 12px; }
.options-list { display: flex; flex-direction: column; gap: 12px; }
.option-item { background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 12px 16px; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; gap: 12px; font-size: 14px; }
.option-item:hover { background: #334155; }
.option-item.selected { background: #0369a1; border-color: #38bdf8; color: #fff; }
.opt-radio { width: 18px; height: 18px; accent-color: #38bdf8; }
.navigation-bar { display: flex; justify-content: space-between; align-items: center; }
.nav-btn { background: #334155; color: #f8fafc; border: none; padding: 8px 16px; border-radius: 6px; cursor: pointer; font-weight: 600; }
.nav-btn:disabled { opacity: 0.4; cursor: not-allowed; }
.submit-btn { background: #16a34a; color: #fff; border: none; padding: 8px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; }
.submit-btn:hover { background: #15803d; }
.progress-indicator { font-size: 13px; color: #94a3b8; font-weight: bold; }
.result-modal { background: #0f172a; padding: 30px; border-radius: 12px; text-align: center; border: 2px solid #38bdf8; }
.hidden { display: none; }
.score-badge { font-size: 42px; font-weight: bold; color: #4ade80; margin: 15px 0; }'''

    js_content = '''let questions = [];
let currentIdx = 0;
let userAnswers = {};
let timerSeconds = 900; // 15 mins

async function initQuiz() {
  const resp = await fetch("questions.json");
  const allQ = await resp.json();
  // Select first 15 or slice
  questions = allQ.slice(0, 15);
  renderQuestion();
  startTimer();
}

function renderQuestion() {
  const q = questions[currentIdx];
  const card = document.getElementById("questionCard");
  
  card.innerHTML = `
    <div style="font-size:12px; color:#38bdf8; font-weight:bold; margin-bottom:6px;">${q.id} • ${q.unit_name}</div>
    <div class="q-title-en">Q${currentIdx + 1}. ${q.question_en}</div>
    <div class="q-title-hi">प्र.${currentIdx + 1}. ${q.question_hi}</div>
    <div class="options-list">
      ${q.options_en.map((opt, idx) => `
        <div class="option-item ${userAnswers[currentIdx] === (idx + 1) ? 'selected' : ''}" onclick="selectOption(${idx + 1})">
          <input type="radio" class="opt-radio" name="qOpt" ${userAnswers[currentIdx] === (idx + 1) ? 'checked' : ''}>
          <span><strong>(${idx + 1})</strong> ${opt} <br><em style="color:#94a3b8; font-size:13px;">${q.options_hi[idx] || ''}</em></span>
        </div>
      `).join('')}
    </div>
  `;

  document.getElementById("progressIndicator").textContent = `Question ${currentIdx + 1} of ${questions.length}`;
  document.getElementById("btnPrevQ").disabled = currentIdx === 0;
  document.getElementById("btnNextQ").disabled = currentIdx === questions.length - 1;
}

window.selectOption = function(optIdx) {
  userAnswers[currentIdx] = optIdx;
  renderQuestion();
};

document.getElementById("btnPrevQ").addEventListener("click", () => {
  if (currentIdx > 0) { currentIdx--; renderQuestion(); }
});

document.getElementById("btnNextQ").addEventListener("click", () => {
  if (currentIdx < questions.length - 1) { currentIdx++; renderQuestion(); }
});

document.getElementById("btnSubmit").addEventListener("click", submitExam);

function submitExam() {
  let score = 0;
  questions.forEach((q, idx) => {
    if (userAnswers[idx] === q.correct_option) score++;
  });

  const body = document.getElementById("quizBody");
  body.classList.add("hidden");

  const modal = document.getElementById("resultModal");
  modal.classList.remove("hidden");
  modal.innerHTML = `
    <h2>🎉 CTET EVS Paper-1 Content Scorecard</h2>
    <div class="score-badge">${score} / ${questions.length}</div>
    <p style="color:#94a3b8; margin-bottom:20px;">Percentage: ${((score / questions.length) * 100).toFixed(1)}% | Rubric: ${score >= 12 ? '🌟 Outstanding Mastery' : score >= 9 ? '👍 Passing Standard' : '⚠️ Remedial Revision Required'}</p>
    <button class="nav-btn" onclick="location.reload()" style="background:#0284c7;">🔄 Retake Mock Exam</button>
  `;
}

function startTimer() {
  const timerEl = document.getElementById("timer");
  setInterval(() => {
    if (timerSeconds > 0) {
      timerSeconds--;
      const m = Math.floor(timerSeconds / 60);
      const s = timerSeconds % 60;
      timerEl.textContent = `⏱ ${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
    }
  }, 1000);
}

initQuiz();'''

    with open(quiz_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(quiz_dir / "styles.css", "w", encoding="utf-8") as f:
        f.write(css_content)
    with open(quiz_dir / "quiz_engine.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    print("PWA Quiz Engine HTML/CSS/JS/JSON built.")

if __name__ == "__main__":
    build_notebooklm_assets()
    build_hyperframes_player()
    build_pwa_quiz_engine()
    print("Sprint 4 Downstream Integration Complete!")
