import json, re, os

html_path = "evs/downstream/unit_1/index.html"
artifact_path = "/home/deadpool/.gemini/antigravity-cli/brain/6e481f7f-9ebe-4bf4-8c7f-99d6d1b3697d/unit_1_living_world.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Clean JS section for PYQ diagnostics and zoom
js_fix = """
// --- Granular Option-by-Option PYQ Diagnostics ---
const pyqDiagnostics = {
  1: {
    'A': {
      correct: false,
      text: "❌ <b>Option A is Incomplete:</b> Statement 3 is also factually true according to NCERT Class 5 Ch 1. Sloths are strict folivores that eat the leaves of the same tree on which they live before migrating."
    },
    'B': {
      correct: false,
      text: "❌ <b>Option B is Incomplete:</b> Statement 1 is also factually true. Sloths sleep approx 17 hours a day suspended upside down from branches."
    },
    'C': {
      correct: false,
      text: "❌ <b>Option C is Incomplete:</b> Statement 2 is also an exact invariant. A sloth lives ~40 years and visits only about 8 trees in its entire lifespan."
    },
    'D': {
      correct: true,
      text: "✓ <b>Option D is CORRECT:</b> All three statements are exact NCERT Class 5 Ch 1 (<i>Super Senses</i>) invariants: 17 hours upside-down sleep, 40-year life across ~8 trees, and eating leaves of the host tree."
    }
  },
  2: {
    'A': {
      correct: true,
      text: "✓ <b>Option A is CORRECT:</b> NCERT Class 5 Ch 2 (<i>A Snake Charmer's Story</i>) defines strictly four poisonous snakes in India: Spectacled Cobra (नाग), Common Krait (करैत), Russell's Viper (दुबोइया), and Saw-scaled Viper (अफ़ई)."
    },
    'B': {
      correct: false,
      text: "❌ <b>Option B is INCORRECT:</b> Pythons (अजगर) and Rat snakes (धामन) are non-venomous constrictors. They do not possess venom or venom-injecting fangs."
    },
    'C': {
      correct: false,
      text: "❌ <b>Option C is INCORRECT:</b> Python is a non-venomous constrictor. Coral snakes are not among the 4 NCERT-designated syllabus species."
    },
    'D': {
      correct: false,
      text: "❌ <b>Option D is INCORRECT:</b> Water snakes (चेकर्ड कीलबैक) and Pythons are completely non-venomous."
    }
  },
  3: {
    'A': {
      correct: false,
      text: "❌ <b>Option A is INCORRECT:</b> The Owl (उल्लू) rotates its neck backward up to approximately 270 degrees in a smooth rotational arc, but does NOT flick its neck back and forth with a jerk."
    },
    'B': {
      correct: true,
      text: "✓ <b>Option B is CORRECT:</b> NCERT Class 3 Ch 8 (<i>Flying High</i>) specifically notes that the Myna (मैना) moves its neck back and forth with a distinct, sudden jerk."
    },
    'C': {
      correct: false,
      text: "❌ <b>Option C is INCORRECT:</b> The Crow (कौआ) builds nests high in trees using iron wire and twigs, but does not move its neck with a characteristic jerk."
    },
    'D': {
      correct: false,
      text: "❌ <b>Option D is INCORRECT:</b> The Koel (कोयल) is a brood parasite that lays eggs in crow nests; it does not exhibit the jerky cervical flick."
    }
  }
};

function evaluatePyq(qNum, optKey, isCorrect, btn) {
  const parent = btn.parentElement;
  parent.querySelectorAll('.pyq-opt').forEach(b => b.classList.remove('correct', 'wrong'));
  
  if (isCorrect) {
    btn.classList.add('correct');
  } else {
    btn.classList.add('wrong');
  }
  
  const diag = pyqDiagnostics[qNum][optKey];
  const expBox = document.getElementById("pyqExp" + qNum);
  if (expBox && diag) {
    expBox.innerHTML = diag.text;
    expBox.style.display = 'block';
    if (isCorrect) {
      expBox.style.borderLeftColor = 'var(--green)';
      expBox.style.background = 'rgba(46, 107, 63, 0.08)';
    } else {
      expBox.style.borderLeftColor = 'var(--red)';
      expBox.style.background = 'rgba(168, 50, 38, 0.08)';
    }
  }
}

// Fix zoomMm to target #mmSvgWrapper directly
function applyMmZoom() {
  const target = document.getElementById('mmSvgWrapper');
  if (target) {
    target.style.transform = 'scale(' + mmZoomLevel + ')';
    const ind = document.getElementById('mmZoomIndicator');
    if (ind) ind.textContent = Math.round(mmZoomLevel * 100) + '%';
  }
}
"""

if "// --- Granular Option-by-Option PYQ Diagnostics ---" in content:
    content = re.sub(r'// --- Granular Option-by-Option PYQ Diagnostics ---.*?(?=</script>)', js_fix.strip() + "\n", content, flags=re.DOTALL)
else:
    content = content.replace("</script>", js_fix + "\n</script>")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

with open(artifact_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Clean update completed successfully.")
