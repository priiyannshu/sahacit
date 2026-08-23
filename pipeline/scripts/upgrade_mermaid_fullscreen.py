import re

html_path = "/home/deadpool/omniverse/preach/evs/downstream/unit_1/index.html"
artifact_path = "/home/deadpool/.gemini/antigravity-cli/brain/6e481f7f-9ebe-4bf4-8c7f-99d6d1b3697d/unit_1_living_world.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update CSS for Mermaid Fullscreen and Tall Canvas
old_css_pattern = r"/\* Mermaid Mind Map Diagram Container \(§ 05\) \*/.*?(?=/\* Audio Station \(§ 08\) \*/)"
new_css = """/* Mermaid Mind Map Diagram Container (§ 05) */
.mm-wrapper{background:var(--paper2);border:2px solid var(--ink);border-radius:4px;padding:22px;margin:20px 0;box-shadow:4px 4px 0 rgba(28,25,20,.15);transition:all .3s ease;position:relative}
.mm-wrapper.is-fullscreen{position:fixed!important;inset:0!important;z-index:99999!important;width:100vw!important;height:100vh!important;max-width:100vw!important;margin:0!important;border-radius:0!important;padding:18px 24px!important;background:var(--paper)!important;display:flex!important;flex-direction:column!important;overflow:hidden!important}
.mm-toolbar{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;padding-bottom:14px;margin-bottom:16px;border-bottom:1px solid var(--rule)}
.mm-title{font-family:var(--serif);font-size:19px;font-weight:700;color:var(--ink);display:flex;align-items:center;gap:8px}
.mm-actions{display:flex;gap:6px;align-items:center;flex-wrap:wrap}
.mm-btn{background:var(--paper);color:var(--ink);border:1.4px solid var(--ink);padding:5px 12px;border-radius:3px;font:700 11px var(--mono);cursor:pointer;display:inline-flex;align-items:center;gap:5px;transition:all .15s ease;box-shadow:1.5px 1.5px 0 var(--ink)}
.mm-btn:hover{background:var(--ink);color:var(--paper);transform:translate(-1px,-1px);box-shadow:2px 2px 0 var(--ink)}
.mm-btn.active{background:var(--red);color:var(--paper);border-color:var(--red)}
.mm-legend{display:flex;flex-wrap:wrap;gap:8px;font-size:11px}
.mm-leg-item{display:inline-flex;align-items:center;gap:5px;padding:2px 8px;border-radius:3px;border:1px solid var(--rule);background:var(--paper);font-family:var(--mono);font-size:10px;text-transform:uppercase;letter-spacing:.05em}
.leg-dot{width:10px;height:10px;border-radius:2px;border:1px solid var(--ink);display:inline-block}
.leg-dot.pillar{background:#e0d8c3}
.leg-dot.core{background:#d8e2ec}
.leg-dot.inv{background:#d4e8d4;border-color:#2e6b3f}
.leg-dot.trap{background:#fce4e4;border-color:var(--red)}
.mm-canvas-container{overflow:auto;padding:24px 16px;display:flex;justify-content:center;align-items:flex-start;background:var(--paper);border:1.5px solid var(--rule);border-radius:3px;min-height:740px;height:820px;position:relative;cursor:grab;user-select:none}
.mm-wrapper.is-fullscreen .mm-canvas-container{flex:1;height:calc(100vh - 130px)!important;min-height:0!important;border:2px solid var(--ink)}
.mm-canvas-container:active{cursor:grabbing}
.mermaid{min-width:820px;width:100%;max-width:1080px;display:flex;justify-content:center;transform-origin:top center;transition:transform .15s ease}
.mermaid svg{max-width:100%!important;height:auto!important;min-height:720px!important;font-family:var(--mono)!important}
.mm-text-details{margin-top:14px;background:var(--paper);border:1px solid var(--rule);border-radius:3px;padding:10px 14px;font-size:12.5px}
.mm-text-details summary{cursor:pointer;font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--blue)}
.mm-tree{background:var(--paper2);border:1px solid var(--rule);border-radius:3px;padding:14px;margin:12px 0 4px;font-size:12.5px}
.mm-node{margin:6px 0;padding-left:14px;border-left:1.5px solid var(--rule)}
.mm-header{font-weight:700;cursor:pointer;color:var(--blue);display:inline-block;padding:2px 6px;border-radius:2px}
.mm-header:hover{background:rgba(49,84,122,.08)}
.mm-content{margin-left:12px;color:var(--ink2);margin-top:4px}

"""

content = re.sub(old_css_pattern, new_css, content, flags=re.DOTALL)

# 2. Update HTML markup for Section 5: Vertical Multitier Diagram + Fullscreen & Zoom Toolbar
old_section5_pattern = r'<section id="mindmap">.*?</section>'
new_section5 = """<section id="mindmap">
  <div class="wrap">
    <div class="shead">
      <span class="snum">§ 05</span>
      <h2>Concept Hierarchy &amp; Mind Map</h2>
    </div>
    <p class="lede readable-block" id="sec5Lede"
       data-en="The Concept Graph maps animal adaptations into locomotion, classification rules, social structures, nesting habits, super senses, and herpetology rendered via Mermaid.js."
       data-hi="Concept Graph animal adaptations ko locomotion, reproduction rules, social structures, nesting habits, super senses, aur herpetology me Mermaid.js dwara visualize karta hai.">
      Hierarchical taxonomic blueprint rendered via Mermaid.js with fullscreen expansion and interactive pan-zoom controls.
    </p>

    <!-- Themed Mermaid Diagram Card with Fullscreen & Zoom Controls -->
    <div class="mm-wrapper" id="mmWrapper">
      <div class="mm-toolbar">
        <div class="mm-title">🌳 Unit 01 Synthesis Concept Graph</div>
        
        <div class="mm-legend">
          <span class="mm-leg-item"><span class="leg-dot pillar"></span> Topic Pillar</span>
          <span class="mm-leg-item"><span class="leg-dot core"></span> Concept Node</span>
          <span class="mm-leg-item"><span class="leg-dot inv"></span> Invariant Fact</span>
          <span class="mm-leg-item"><span class="leg-dot trap"></span> Exam Trap</span>
        </div>

        <div class="mm-actions">
          <button class="mm-btn" onclick="zoomMm(1.15)" title="Zoom In">🔍+ In</button>
          <button class="mm-btn" onclick="zoomMm(0.85)" title="Zoom Out">🔍- Out</button>
          <button class="mm-btn" onclick="resetMmZoom()" title="Reset Zoom">↺ <span id="mmZoomIndicator">100%</span></button>
          <button class="mm-btn" id="btnMmFullscreen" onclick="toggleMmFullscreen()" title="Toggle Fullscreen">⛶ Fullscreen</button>
        </div>
      </div>

      <div class="mm-canvas-container" id="mmCanvasContainer">
        <div class="mermaid" id="unit1Mindmap">
flowchart TB
  classDef root fill:#1c1914,stroke:#1c1914,stroke-width:2px,color:#f4f1e8,font-weight:bold;
  classDef pillar fill:#e0d8c3,stroke:#1c1914,stroke-width:2px,color:#1c1914,font-weight:bold;
  classDef core fill:#d8e2ec,stroke:#1c1914,stroke-width:1.5px,color:#1c1914,font-weight:bold;
  classDef inv fill:#d4e8d4,stroke:#2e6b3f,stroke-width:1.5px,color:#1c1914;
  classDef trap fill:#fce4e4,stroke:#a83226,stroke-width:1.5px,color:#1c1914;

  ROOT["🌳 <b>UNIT 1: LIVING WORLD & ANIMAL ADAPTATIONS</b><br/><i>CTET Paper 1 · Deterministic Invariant Blueprint</i>"]:::root

  subgraph T1 ["<b>TIER 1 · MORPHOLOGY & REPRODUCTION RULES</b>"]
    direction TB
    B1["🦅 <b>1. Locomotion & Morphology</b>"]:::pillar
    B1 --> B1_A["Avian Flight Dynamics<br/><i>Hollow Bones & Shed Feathers</i>"]:::core
    B1 --> B1_B["Reptilian Crawling<br/><i>Ventral Scales & Body Waves</i>"]:::core
    B1 --> B1_C["Avian Beak Morphologies"]:::core
    B1_C --> B1_C1["Hooked Beak: Eagle/Vulture (Tearing Flesh)"]:::inv
    B1_C --> B1_C2["Chisel Beak: Woodpecker (Boring Wood)"]:::inv
    B1_C --> B1_C3["Short Cone: Sparrow/Pigeon (Cracking Seeds)"]:::inv
    B1_C --> B1_C4["Slender Probe: Sunbird (Nectar Sucking)"]:::inv

    B2["🐾 <b>2. Reproduction Rules (Ear to Ear)</b>"]:::pillar
    B2 --> B2_VIV["<b>Viviparous (जरायुज):</b> Visible Pinnae + Hair on Skin ➔ Live Birth"]:::inv
    B2 --> B2_OVI["<b>Oviparous (अंडज):</b> Hidden Ear Holes + No Hair ➔ Lay Eggs"]:::inv
    B2 --> B2_HAIR["Coat Patterns: Spots & Stripes exist purely due to <b>Hair Color</b>"]:::core
    B2_HAIR --> B2_TRAP["❌ Exam Trap: Animals without hair have NO pattern stripes;<br/>Whales & Bats are viviparous mammals"]:::trap
  end

  subgraph T2 ["<b>TIER 2 · EUSOCIALITY & NEST ARCHITECTURE</b>"]
    direction TB
    B3["🐘 <b>3. Eusociality & Herds</b>"]:::pillar
    B3 --> B3_ELE["Asian Elephant Matriarchy<br/><i>Herd: 10–12 Females & Calves</i>"]:::core
    B3_ELE --> B3_ELE1["Oldest Female Leads | Males Exit at 14–15 yrs"]:::inv
    B3_ELE --> B3_ELE2[">100 kg Daily Foliage | 2–4 hrs Sleep | ~200 kg 3-mo Calf"]:::inv
    B3_ELE --> B3_ELE_TRAP["❌ Exam Trap: Male elephants NEVER lead herd"]:::trap
    B3 --> B3_BEE["Honeybee Colonies (Apiculture)"]:::core
    B3_BEE --> B3_BEE1["Queen (Eggs) | Drones | Workers (Waggle Dance)"]:::inv
    B3_BEE --> B3_BEE2["Peak Bihar Season: Oct to Dec"]:::inv

    B4["🪺 <b>4. Avian Nest Architecture</b>"]:::pillar
    B4 --> B4_TAILOR["Tailorbird: Stitches 2 living leaves with plant fiber"]:::inv
    B4 --> B4_WEAVER["Weaver Bird: Male weaves hanging nest; Female selects"]:::inv
    B4 --> B4_ROBIN["Indian Robin: Roadside stone crevices with wool & grass"]:::inv
    B4 --> B4_CROW["Crow: High canopy nest with twigs & <b>iron wire</b>"]:::inv
    B4_CROW --> B4_KOEL["Koel Brood Parasite<br/>❌ Exam Trap: Builds NO nest; lays eggs in crow's nest"]:::trap
  end

  subgraph T3 ["<b>TIER 3 · EXTREME SENSES & HERPETOLOGY</b>"]
    direction TB
    B5["⚡ <b>5. Super Senses & Chronobiology</b>"]:::pillar
    B5 --> B5_SLOTH["Sloth Chronobiology (17h Sleep & 40y Lifespan)"]:::core
    B5_SLOTH --> B5_SLOTH1["17h Upside-Down Sleep | ~8 Trees Total | 1x/wk Defecation"]:::inv
    B5_SLOTH --> B5_SLOTH_TRAP["❌ Exam Trap: NOT a bear; does not sleep 24h; excellent swimmer"]:::trap
    B5 --> B5_TIGER["Tiger Apex Senses"]:::core
    B5_TIGER --> B5_TIGER1["6x Night Vision vs Humans | Whiskers Sense Air Waves | 3 km Roar"]:::inv
    B5 --> B5_RAPTOR["Raptor 4x Distance Acuity (8m vs 2m)"]:::inv
    B5 --> B5_CERV["Cervical Mobility: Owl ~270° Neck Rotation vs Myna Jerky Flick"]:::inv

    B6["🐍 <b>6. Herpetology & Venom Invariants</b>"]:::pillar
    B6 --> B6_SNAKES["Big 4 Venomous Snakes of India"]:::core
    B6_SNAKES --> B6_SP1["1. Cobra (नाग) · 2. Krait (करैत)<br/>3. Russell's Viper (दुबोइया) · 4. Saw-scaled Viper (अफ़ई)"]:::inv
    B6_SNAKES --> B6_FANGS["2 Hollow Anterior Fangs for Venom Injection"]:::inv
    B6_SNAKES --> B6_MED["Clinical Anti-Venom Serum (Made from Snake Venom)"]:::inv
    B6_SNAKES --> B6_TRAP["❌ Exam Trap: Pythons & Rat snakes are non-venomous;<br/>Snakes sense sound via ground acoustic vibrations"]:::trap
  end

  ROOT ==> T1
  T1 ==> T2
  T2 ==> T3
        </div>
      </div>

      <!-- Collapsible Text Outline Backup -->
      <details class="mm-text-details">
        <summary><b>📋 View Collapsible Outline Hierarchy</b></summary>
        <div class="mm-tree">
          <div class="mm-node">
            <span class="mm-header" onclick="toggleMm(this)">▼ 🌳 Living World: Animals and Adaptations</span>
            <div class="mm-content">
              <div class="mm-node">
                <span class="mm-header" onclick="toggleMm(this)">▼ 🦅 1. Locomotion &amp; Morphology</span>
                <div class="mm-content">
                  <div>• Flying: Birds with hollow bones and flight/down feathers</div>
                  <div>• Slithering: Reptiles with ventral scales &amp; abdominal muscles</div>
                  <div>• Beaks: Hooked (meat), Chisel (wood), Cone (seeds), Slender (nectar)</div>
                </div>
              </div>
              <div class="mm-node">
                <span class="mm-header" onclick="toggleMm(this)">▼ 🐾 2. Mammalian vs. Avian Rules</span>
                <div class="mm-content">
                  <div>• <b>Viviparous:</b> Visible external pinnae + Hair on skin $\rightarrow$ Live birth</div>
                  <div>• <b>Oviparous:</b> Hidden ear holes + No hair $\rightarrow$ Lay eggs</div>
                </div>
              </div>
              <div class="mm-node">
                <span class="mm-header" onclick="toggleMm(this)">▼ 🐘 3. Eusociality &amp; Herds</span>
                <div class="mm-content">
                  <div>• <b>Elephant Herds:</b> Oldest female leader; 10–12 members; males leave at 14–15y</div>
                  <div>• <b>Honeybees:</b> Queen, Workers (waggle dance), Drones; Peak: Oct–Dec</div>
                </div>
              </div>
              <div class="mm-node">
                <span class="mm-header" onclick="toggleMm(this)">▼ 🪺 4. Avian Nest Architecture</span>
                <div class="mm-content">
                  <div>• <b>Robin:</b> Stone crevices | <b>Crow:</b> Twigs &amp; wire | <b>Koel:</b> Brood parasite</div>
                  <div>• <b>Tailorbird:</b> Leaf stitching | <b>Weaver Bird:</b> Male weaves hanging nest</div>
                </div>
              </div>
              <div class="mm-node">
                <span class="mm-header" onclick="toggleMm(this)">▼ ⚡ 5. Super Senses &amp; Chronobiology</span>
                <div class="mm-content">
                  <div>• <b>Sloth:</b> 17h upside-down sleep, 40y life, ~8 trees, 1x/wk defecation</div>
                  <div>• <b>Tiger:</b> 6x night vision, whiskers sense air waves | <b>Raptor:</b> 4x distance (8m vs 2m)</div>
                </div>
              </div>
              <div class="mm-node">
                <span class="mm-header" onclick="toggleMm(this)">▼ 🐍 6. Herpetology &amp; Venom</span>
                <div class="mm-content">
                  <div>• 4 poisonous snakes: Cobra, Krait, Russell's Viper, Saw-scaled Viper</div>
                  <div>• 2 hollow fangs; clinical anti-venom made directly from venom</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </details>
    </div>
  </div>
</section>"""

content = re.sub(old_section5_pattern, new_section5, content, flags=re.DOTALL)

# 3. Add JS Fullscreen & Pan/Zoom Handlers
js_handlers = """
// --- Mermaid Fullscreen & Pan-Zoom Engine ---
let mmZoomLevel = 1.0;
let mmIsDragging = false;
let mmStartX = 0, mmStartY = 0, mmScrollLeft = 0, mmScrollTop = 0;

function toggleMmFullscreen() {
  const wrapper = document.getElementById("mmWrapper");
  if (!wrapper) return;
  const isFs = wrapper.classList.toggle("is-fullscreen");
  const fsBtn = document.getElementById("btnMmFullscreen");
  if (fsBtn) {
    fsBtn.innerHTML = isFs ? "✕ Exit Fullscreen <code>[ESC]</code>" : "⛶ Fullscreen";
    fsBtn.classList.toggle("active", isFs);
  }
  document.body.style.overflow = isFs ? "hidden" : "";
  if (isFs) resetMmZoom();
}

function zoomMm(factor) {
  mmZoomLevel = Math.max(0.4, Math.min(2.5, mmZoomLevel * factor));
  applyMmZoom();
}

function resetMmZoom() {
  mmZoomLevel = 1.0;
  applyMmZoom();
  const container = document.getElementById("mmCanvasContainer");
  if (container) {
    container.scrollLeft = (container.scrollWidth - container.clientWidth) / 2;
    container.scrollTop = 0;
  }
}

function applyMmZoom() {
  const el = document.getElementById("unit1Mindmap");
  if (el) {
    el.style.transform = `scale(${mmZoomLevel})`;
    const ind = document.getElementById("mmZoomIndicator");
    if (ind) ind.textContent = `${Math.round(mmZoomLevel * 100)}%`;
  }
}

// Drag to pan setup
document.addEventListener("DOMContentLoaded", () => {
  const mmContainer = document.getElementById("mmCanvasContainer");
  if (mmContainer) {
    mmContainer.addEventListener("mousedown", (e) => {
      if (e.target.closest("button") || e.target.closest("a") || e.target.closest("summary")) return;
      mmIsDragging = true;
      mmStartX = e.pageX - mmContainer.offsetLeft;
      mmStartY = e.pageY - mmContainer.offsetTop;
      mmScrollLeft = mmContainer.scrollLeft;
      mmScrollTop = mmContainer.scrollTop;
    });
    mmContainer.addEventListener("mouseleave", () => mmIsDragging = false);
    mmContainer.addEventListener("mouseup", () => mmIsDragging = false);
    mmContainer.addEventListener("mousemove", (e) => {
      if (!mmIsDragging) return;
      e.preventDefault();
      const x = e.pageX - mmContainer.offsetLeft;
      const y = e.pageY - mmContainer.offsetTop;
      const walkX = (x - mmStartX) * 1.3;
      const walkY = (y - mmStartY) * 1.3;
      mmContainer.scrollLeft = mmScrollLeft - walkX;
      mmContainer.scrollTop = mmScrollTop - walkY;
    });
    mmContainer.addEventListener("wheel", (e) => {
      if (e.ctrlKey || e.metaKey) {
        e.preventDefault();
        if (e.deltaY < 0) zoomMm(1.1);
        else zoomMm(0.9);
      }
    }, { passive: false });
  }
});

// ESC key listener for Fullscreen
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    const wrapper = document.getElementById("mmWrapper");
    if (wrapper && wrapper.classList.contains("is-fullscreen")) {
      toggleMmFullscreen();
    }
  }
});
"""

if "// --- Mermaid Fullscreen & Pan-Zoom Engine ---" in content:
    content = re.sub(r"// --- Mermaid Fullscreen & Pan-Zoom Engine ---.*?(?=</script>)", js_handlers.strip() + "\n", content, flags=re.DOTALL)
else:
    content = content.replace("</script>", js_handlers + "\n</script>")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

with open(artifact_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Upgraded Mermaid Diagram to Vertically-Stretched Layout + Fullscreen + Pan/Zoom engine!")
