let questions = [];
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

initQuiz();