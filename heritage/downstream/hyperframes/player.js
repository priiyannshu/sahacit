const scenesData = {
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
