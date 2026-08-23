#!/usr/bin/env python3
"""
Sprint 3 Master Synthesizer: Generates the 7 Master Thematic Spiral Unit Artifacts
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
UNITS_DIR = BASE_DIR / "units"
UNITS_DIR.mkdir(parents=True, exist_ok=True)

def write_unit(filename, content):
    p = UNITS_DIR / filename
    with open(p, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated: {p}")

def generate_units():
    # --------------------------------------------------------------------------
    # UNIT 1: Living World, Animal Behavior & Adaptations
    # --------------------------------------------------------------------------
    unit_1 = """# Unit 1: Living World, Animal Behavior & Adaptations
*(सजीव जगत, पशु व्यवहार एवं पारिस्थितिक अनुकूलन)*

> **NCERT Spiral Mapping**: Class 3 (Ch 1, 8, 19, 24) $\\rightarrow$ Class 4 (Ch 2, 3, 5, 16) $\\rightarrow$ Class 5 (Ch 1, 2, 21) $\\rightarrow$ Class 6 Bridge (Science Ch 9)
> **Target Marks Yield**: 3–5 Marks in CTET Paper-1 Non-Pedagogy EVS Section

---

## 1. Encyclopedic Theory & Concept Evolution (Spiral Progression)

### 1.1 Foundational Layer (Class 3: Sensory & Locomotion Foundations)
Environmental observation begins with the direct sensory identification of animals and their natural habitats (*Poonam's Day Out*). Animals exhibit diverse modes of locomotion:
- **Flying**: Birds (Peacock, Parrot, Crow, Kite) with 2 wings and hollow bones.
- **Crawling/Slithering**: Reptiles (Lizards, Snakes) utilizing abdominal muscles and ventral scales.
- **Walking & Hopping**: Mammals (4 legs) and Amphibians (Frogs with webbed hind feet for hopping and swimming).
- **Avian Morphology (*Flying High*)**: Birds possess distinct feather types (flight feathers for lift, down feathers for thermal insulation) which they shed periodically. Beak shapes directly reflect their trophic niche:
  - *Hooked Sharp Beak* (Eagle, Hawk, Vulture) for tearing mammalian flesh.
  - *Chisel-shaped Strong Beak* (Woodpecker / *कटफोड़वा*) for boring tree trunks to extract insects.
  - *Short Cone Beak* (Sparrow, Pigeon) for cracking hard grains and seeds.
  - *Long Slender Curved Probe Beak* (Sunbird / *शकरखोरा*) for extracting nectar from deep corollas.

### 1.2 Morphological & Social Evolution (Class 4: Mammalian Rules & Social Insects)
- **The Viviparous vs. Oviparous Structural Rule (*Ear to Ear*)**:
  - **Viviparous (जरायुज / Mammals giving live birth)**: Animals with *visible external ears* (pinnae) and *hair on their skin* (e.g., Elephants, Tigers, Deer, Cows, Humans).
  - **Oviparous (अंडज / Egg-layers)**: Animals with *no external ears* (having small hidden tympanic holes covered by feathers/scales) and *no hair on skin* (e.g., Birds, Lizards, Snakes, Crocodiles, Frogs).
  - *Skin Patterns*: Distinctive stripes or spots on animal coats are created purely by the color and arrangement of *hair on their skin*, not bare epidermis.
- **Elephant Herd Dynamics (*A Day with Nandu*)**:
  - Matriarchal structure: The herd consists strictly of *10 to 12 adult females and young calves*, led by the *oldest female* (*बुजुर्ग हथनी*).
  - Male calves leave the herd between *14 to 15 years of age* to wander solitarily.
  - An adult elephant consumes *over 100 kg (1 quintal)* of leaves and twigs daily, sleeping only *2 to 4 hours* per 24-hour cycle.
  - A 3-month-old calf weighs approximately *200 kg (2 quintals)*.
- **Apiculture & Eusocial Insect Colonies (*Anita and the Honeybees*)**:
  - Division of labour in Apis mellifera: A single *Queen Bee* lays eggs; hundreds of *Female Worker Bees* build combs, nurse larvae, collect nectar, and execute a directional *waggle dance*; male drones perform no worker roles.
  - Ideal apiculture season in Bihar (Muzzafarpur litchi belt): *October to December* (peak egg-laying window).
  - Parallel eusocial colonial insects: Ants (Queen, Soldier guards, Worker foragers), Termites (*दीमक*), and Wasps (*ततैया*).
- **Avian Nesting Architecture (*A Busy Month* by Gijubhai Badheka)**:
  - *Indian Robin (कलचिड़ी)*: Roadside stone crevices lined with grass, soft twigs, wool, roots, and cotton.
  - *Crow (कौआ)*: High tree canopy nests utilizing twigs and iron wire pieces.
  - *Koel (कोयल)*: Brood parasite laying eggs in crow nests.
  - *Tailorbird (दर्जिन चिड़िया)*: Stitches together two living bush leaves with its sharp beak.
  - *Sunbird (शकरखोरा)*: Suspended hanging nests of cobwebs, bark flakes, hair, and dry grass.
  - *Weaver Bird (बया / जुलाहा पक्षी)*: Male weaves elaborate bottle-shaped hanging nests; female inspects and selects the best nest.

### 1.3 Advanced Sensory Physiology & Genetics (Class 5 & 6 Bridge)
- **Extreme Sensory Adaptations (*Super Senses*)**:
  - *Sloth (स्लॉथ)*: Arboreal mammal resembling a bear; sleeps *17 hours daily* hanging upside down; life expectancy ~*40 years*; visits only ~*8 trees* total; descends *once weekly* for defecation; proficient swimmer.
  - *Tiger (बाघ)*: Nocturnal visual acuity *6 times superior* to humans; sensitive vibrissae (whiskers) detect minute air pressure fluctuations; roar audible up to *3 km*; territorial scent marking via urine.
  - *Raptor Vision* (Eagle, Kite, Vulture): High visual resolution *4 times farther* than humans (8 meters vs 2 meters).
  - *Silkworm Moth*: Male tracks female pheromones from *several kilometers away*.
  - *Snakes*: Lack external auditory pinnae; perceive ground acoustic vibrations through ventral somatosensory receptors.
- **Herpetology & Indian Venomous Snakes (*A Snake Charmer's Story*)**:
  - Exactly *4 species of venomous snakes* in India: Spectacled Cobra (*नाग*), Common Krait (*करैत*), Russell's Viper (*दुबोइया*), Saw-scaled Viper (*अफ़ई*).
  - Possess *2 hollow venom-injecting fangs*; clinical anti-venom serum is manufactured directly from *extracted snake venom*.
  - *Kalbeliyas*: Traditional sapera community; craft musical instruments (*Been, Tumba, Khanjiri*) from dried bottle gourds (*lauki*).
- **Genetics & Trait Inheritance (*Like Father, Like Daughter*)**:
  - Gregor Johann Mendel (Austria, 1822): Investigated *28,000 pea plants* across 7 years to prove particulate paired-allele inheritance (smooth/rough, yellow/green seeds).
  - Disease clarity: *Polio is an infectious viral disease* caused by poliovirus, *never an inherited genetic condition*.

---

## 2. Zero-Hallucination Entity Vault

| Entity (Bilingual) | Core Taxonomic Traits | Exact Numerical Invariants | Anti-Hallucination Exam Traps |
| :--- | :--- | :--- | :--- |
| **Sloth**<br>*(स्लॉथ)* | Arboreal folivore resembling bear; nocturnal | **17 hrs/day** upside down sleep; **40-yr** lifespan; **~8 trees** visited; **1/week** defecation | ❌ *Trap*: Sloth is NOT a bear; does not sleep 24 hours; moves to few trees. |
| **Asian Elephant**<br>*(एशियाई हाथी)* | Matriarchal megaherbivore; mud bath thermoregulation | **>100 kg** foliage/day; **2–4 hrs** daily sleep; **200 kg** 3-mo calf; **10–12** females/herd; **14–15 yrs** male departure | ❌ *Trap*: Male elephants do NOT lead the herd; calves do not sleep all day. |
| **Tiger**<br>*(बाघ)* | Apex predator; sensitive facial vibrissae | **6x** night vision vs humans; **3 km** roar audibility radius; **several km** territory | ❌ *Trap*: Whiskers sense vibrations in air, not just touch. |
| **Venomous Snakes**<br>*(जहरीले सांप)* | Only 4 species: Cobra, Krait, Russell's Viper, Saw-scaled Viper | **4 species** total; **2 hollow fangs**; Anti-venom made from snake venom | ❌ *Trap*: Pythons, Rat snakes, and Water snakes are non-venomous. |
| **Birds of Prey**<br>*(चील, बाज, गिद्ध)* | High-altitude raptors with grooved tails | **4x** human viewing distance (**8 meters** vs 2 meters) | ❌ *Trap*: They see 4x farther, not 6x (6x is Tiger night vision). |
| **Owl vs Myna**<br>*(उल्लू एवं मैना)* | Avian cervical mobility | Owl: **~270° backward rotation**; Myna: **Jerky back-and-forth neck flick** | ❌ *Trap*: Myna moves neck with jerk; Owl rotates backwards. |
| **Squirrel**<br>*(गिलहरी)* | Rodent gnawing adaptation | Front incisors **grow continuously** throughout lifespan | ❌ *Trap*: Squirrel front teeth never stop growing; worn down by gnawing. |

---

## 3. Hyperframes HTML Video Storyboards & Scene Specs

```html
<!-- Hyperframes Scene 1: The Sloth Arboreal Clock -->
<div class="hyperframe-scene" data-scene="sloth-circadian" style="width: 100%; height: 540px; background: #1a2f1a; color: #fff; position: relative; font-family: sans-serif;">
  <div class="header-overlay" style="padding: 20px; font-size: 24px; font-weight: bold;">
    🦥 Sloth (स्लॉथ) — Invariant Chronobiology
  </div>
  <div class="dial-container" style="position: absolute; left: 100px; top: 100px; width: 300px; height: 300px; border-radius: 50%; border: 8px solid #4caf50; display: flex; align-items: center; justify-content: center; background: conic-gradient(#388e3c 0deg 255deg, #81c784 255deg 360deg);">
    <div class="dial-center" style="width: 180px; height: 180px; background: #1a2f1a; border-radius: 50%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
      <span style="font-size: 32px; font-weight: bold; color: #a5d6a7;">17 hrs</span>
      <span style="font-size: 14px; color: #ccc;">Upside Down Sleep</span>
    </div>
  </div>
  <div class="stats-card" style="position: absolute; right: 80px; top: 120px; width: 420px; background: rgba(255,255,255,0.08); padding: 25px; border-radius: 12px; line-height: 1.8;">
    <h3 style="color: #81c784; margin-top: 0;">Factual Invariants Ledger:</h3>
    <ul>
      <li><strong>Lifespan:</strong> ~40 Years (लगभग 40 वर्ष)</li>
      <li><strong>Habitat Mobility:</strong> Visits only ~8 trees in entire life</li>
      <li><strong>Excretion:</strong> Descends once weekly (सप्ताह में एक बार)</li>
      <li><strong>Locomotion:</strong> Tree hanging & strong swimming</li>
    </ul>
  </div>
</div>
```

---

## 4. NotebookLM Audio Overview Steering Cue Cards

```markdown
[NOTEBOOKLM STEERING DIRECTIVE: UNIT 1 ANIMAL BEHAVIOR]
- Role: Lead Comparative Biologist (Host A) & Skeptical Naturalist Co-Host (Host B)
- Focus: Contrast the extreme sleeping adaptations (Sloth 17 hrs vs Elephant 2-4 hrs).
- Debater Cue: Have Host B challenge whether sloths are bears; Host A strictly corrects using NCERT facts (looks like bear, lives 40 years, visits 8 trees).
- Terminology Anchor: Explicitly articulate both English and Hindi names: "Spectacled Cobra (नाग), Common Krait (करैत), Russell's Viper (दुबोइया), Saw-scaled Viper (अफ़ई)".
- Guardrail: Absolutely do NOT hallucinate that sloths sleep 24 hours or that male elephants lead the herd.
```

---

## 5. Formative Inline PYQ Grounding Bank

### Item 1: CTET Dec 2022 CBT / Jan 2023 Shift 1
**Question (Bilingual):**
Consider the following statements about Sloths:
1. A sloth sleeps for almost 17 hours a day hanging upside down on a tree branch.
2. A sloth lives for about 40 years and moves to only about 8 trees in its lifetime.
3. A sloth eats the leaves of the same tree on which it lives.
Which of the above statements are correct?
*(स्लॉथ के बारे में कथनों पर विचार कीजिए: 1. यह लगभग 17 घंटे पेड़ से उल्टा लटककर सोता है; 2. यह लगभग 40 वर्ष जीता है और केवल 8 पेड़ों पर जाता है; 3. यह उसी पेड़ की पत्तियाँ खाता है।)*

- Options:
  1. 1 and 2 only
  2. 2 and 3 only
  3. 1 and 3 only
  4. 1, 2 and 3 (Correct)
- **Official Answer**: `Option 4`
- **Grounding Explanation**: Directly verifiable from Class 5 Chapter 1 (*Super Senses*). Sloths exhibit extreme metabolic conservation: 17h sleep, 40y lifespan, 8 trees total.

### Item 2: CTET July 2024 Paper 1 (Q62)
**Question (Bilingual):**
Which of the following sets represents ONLY poisonous snakes found in India?
*(निम्नलिखित में से कौन सा समूह भारत में पाए जाने वाले केवल जहरीले सांपों को दर्शाता है?)*

- Options:
  1. Cobra, Krait, Russell's Viper, Saw-scaled Viper (नाग, करैत, दुबोइया, अफ़ई) (Correct)
  2. Python, Cobra, Krait, Rat snake
  3. Russell's Viper, Viper, Python, Coral
  4. Cobra, Krait, Water snake, Python
- **Official Answer**: `Option 1`
- **Grounding Explanation**: Grounded in Class 5 Chapter 2 (*A Snake Charmer's Story*). India has strictly 4 venomous snakes; Pythons (*अजगर*) and Rat snakes (*धामन*) are non-venomous constrictors.
"""
    write_unit("unit_1_living_world_animals.md", unit_1)

    # --------------------------------------------------------------------------
    # UNIT 2: Flora, Seeds, Forest Rights & Agriculture
    # --------------------------------------------------------------------------
    unit_2 = """# Unit 2: Flora, Seeds, Forest Rights & Agriculture
*(पादप, बीज, वन अधिकार एवं कृषि प्रणालियाँ)*

> **NCERT Spiral Mapping**: Class 3 (Ch 2, 14) $\\rightarrow$ Class 4 (Ch 4, 11, 14, 19) $\\rightarrow$ Class 5 (Ch 5, 19, 20) $\\rightarrow$ Class 6 Bridge (Science Ch 7)
> **Target Marks Yield**: 3–4 Marks in CTET Paper-1 Non-Pedagogy EVS Section

---

## 1. Encyclopedic Theory & Concept Evolution (Spiral Progression)

### 1.1 Leaf Morphology, Medicinal Flora & Ethnobotany (Class 3)
- **Leaf Diversity & Identification (*The Plant Fairy*)**: Leaves exhibit diverse geometric configurations:
  - *Margins*: Smooth (entire), serrated (saw-toothed as in rose/neem), and lobed (papaya/oak).
  - *Essential Oil Smells*: Crushing leaves of Lemon, Mango, Neem, Basil (*Tulsi*), Mint (*Pudina*), and Coriander (*Dhaniya*) enables blindfold identification.
  - *Artist Tribute*: **Vishnu Chinchalkar** (Indore, Madhya Pradesh) revolutionized Indian folk collage by crafting exquisite animal portraits entirely from dried fallen leaves.
- **Traditional Herbal Pharmacopoeia (*The Story of Food*)**:
  - *Cough & Cold*: Decoction of Tulsi leaves, Ginger (*Adrak*), and Honey.
  - *Stomach Ache*: Carom seeds (*Ajwain*) swallowed with warm water.
  - *Toothache*: Direct application of Clove (*Laung*) oil on the cavity.
  - *Skin Injuries & Bruises*: Topical application of Turmeric (*Haldi*) paste in warm mustard oil or milk.

### 1.2 Desert Trees, Farming Implements & Floral Craft (Class 4)
- **Khejadi Tree & The Bishnoi Conservation Martyrdom (*The Story of Amrita*)**:
  - *Geography*: Khejadli village near Jodhpur, Rajasthan (~1730 AD).
  - *Martyrdom*: Amrita Devi Bishnoi, her three daughters, and over 300 Bishnoi villagers hugged Khejadi trees (*पेड़ से चिपकना*) to protect them from the King's woodcutters.
  - *Khejadi Tree Invariants*: Grows in arid deserts with minimal water; its *bark is used as medicine*; its wood is *naturally insect-resistant*; its pods (*Sangri*) are cooked as nutritious vegetables; provides dense shade for desert children and fodder for blackbucks.
- **Desert Oak of Australia (*Abdul in the Garden*)**:
  - *Location*: Deserts of Australia.
  - *Anatomy*: Height equal to a standard classroom wall (~4 meters) with very sparse foliage.
  - *Root Invariant*: Deep taproots penetrate **almost 30 times the tree's height** into the ground until reaching the water table.
  - *Trunk Reservoir*: Excess water is stored inside the tree trunk; during desert droughts, indigenous people insert thin pipes/straws into the trunk to drink water.
- **Karnataka Agrarian Tools (*Basva's Farm*)**:
  - *Khunti (खूंटी)*: Iron digging rod used to loosen hard soil prior to tilling.
  - *Kurige (कुरीगे)*: Wooden plough equipped with a seed-dropping funnel drawn by bullocks.
  - *Illige (इल्लीगे)*: Sharp curved blade mounted on a wooden base for slicing dry onion leaves.
  - *Weeding*: Essential extraction of unwanted wild plants (*खरपतवार*) that rob crops of water and fertilizer.

### 1.3 Seed Dispersal, Forest Rights & Agrarian Ecology (Class 5 & 6 Bridge)
- **Seed Mechanics, Carnivorous Plants & Velcro (*Seeds and Seeds*)**:
  - *Germination Requirements*: Simultaneous presence of **Air, Water, and Warmth** (seeds submerged in boiled de-aerated water or kept dry fail to germinate).
  - *Pitcher Plant (Nepenthes / नेपेंथीस)*: Carnivorous plant native to **Australia, Indonesia, and Meghalaya (India)**; pitcher-shaped modified leaf with a lid; traps frogs, insects, and mice using **sweet aromatic scent** (NOT sound).
  - *Velcro Invention (1948)*: Swiss engineer **George Mestral** examined Xanthium burrs sticking to his coat and dog's fur; microscopic hooks inspired Velcro fasteners.
  - *Global Crop Migration Matrix*:
    - **South America** $\\rightarrow$ Green Chillies, Tomatoes, Potatoes (brought by Portuguese).
    - **Europe** $\\rightarrow$ Cabbage, Peas.
    - **Africa** $\\rightarrow$ Coffee beans, Okra / Bhindi.
    - **China** $\\rightarrow$ Soyabean (explosive pod dehiscence dispersal).
    - **Native to India** $\\rightarrow$ Mango, Orange, Banana, Spinach, Radish, Methi.
- **Suryamani & Right to Forest Act 2007 (*Whose Forests?*)**:
  - *Suryamani*: Tribal activist ('Girl Star') of the **Kudukh tribe** in Jharkhand; established the **Torang Center** ('Torang' means *Jungle* in Kudukh) to protect Adivasi dance, music, herbs, and scripts.
  - *Right to Forest Act, 2007*: Guarantees that tribals living in forests for **at least 25 years** have the legal right over forest land and produce, with conservation managed by the Gram Sabha.
- **Jhum Cultivation in Mizoram (*झूम खेती*)**:
  - Shifting agriculture on hill slopes: Land left fallow for several years after harvest.
  - Weeds and bamboo are **cut and burnt (NEVER pulled out)**; the ash enriches soil minerals.
  - Soil is **lightly dug/furrowed, NEVER deeply ploughed**; mixed seeds (maize, rice, chillies) scattered.
  - *Cheraw Dance*: Post-harvest celebration where dancers rhythmically step between tapped bamboo poles.
  - *Tin of Land*: Area of land required to sow one tin of seeds.
- **Venation-Root Botanical Invariant (Class 6 Bridge Science Ch 7)**:
  - **Reticulate Venation (जालिका शिरा-विन्यास)** $\\leftrightarrow$ **Taproot System (मूसला जड़)** (e.g., Peepal, Neem, Mustard, Rose).
  - **Parallel Venation (समांतर शिरा-विन्यास)** $\\leftrightarrow$ **Fibrous Root System (झकड़ा/रेशेदार जड़)** (e.g., Grass, Banana, Wheat, Maize, Bamboo).

---

## 2. Zero-Hallucination Entity Vault

| Entity (Bilingual) | Core Botanical / Social Traits | Exact Numerical Invariants | Anti-Hallucination Exam Traps |
| :--- | :--- | :--- | :--- |
| **Desert Oak**<br>*(रेगिस्तानी ओक)* | Australian desert tree; stores water in trunk | Roots penetrate **~30 times tree height** to groundwater | ❌ *Trap*: Found in Australia, NOT Abu Dhabi/Rajasthan; has few leaves, NOT dense shade. |
| **Pitcher Plant**<br>*(नेपेंथीस)* | Carnivorous flora in Meghalaya, Australia, Indonesia | Pitcher trap with leaf lid | ❌ *Trap*: Traps by **sweet scent**, NOT by making sounds or singing. |
| **Khejadi Tree**<br>*(खेजड़ी वृक्ष)* | Desert tree of Rajasthan; Bishnoi conservation | **300+ yrs** historical event; medicinal bark; insect-proof | ❌ *Trap*: Wood does NOT rot or get eaten by insects; pods are edible. |
| **Forest Rights Act 2007**<br>*(वन अधिकार अधिनियम)* | Legal protection for traditional forest dwellers | **At least 25 years** forest residency | ❌ *Trap*: Requires 25 years minimum, not 10 or 50 years. |
| **Jhum Farming**<br>*(झूम खेती - मिज़ोरम)* | Shifting hill agriculture with slash-and-burn ash | Weeds **cut & burnt**; soil **lightly furrowed** | ❌ *Trap*: Weeds are NEVER uprooted; fields are NOT ploughed with heavy tractors. |
| **Velcro**<br>*(वेल्क्रो)* | Hook-and-loop fastener inspired by Xanthium burrs | Invented **1948** by **George Mestral** (Switzerland) | ❌ *Trap*: Invented in 1948 by Mestral, NOT Louis Braille or Ronald Ross. |

---

## 3. Hyperframes HTML Video Storyboards & Scene Specs

```html
<!-- Hyperframes Scene 2: Jhum Cultivation Lifecycle -->
<div class="hyperframe-scene" data-scene="jhum-cycle" style="width: 100%; height: 540px; background: #261c14; color: #fff; position: relative; font-family: sans-serif;">
  <div class="header-overlay" style="padding: 20px; font-size: 24px; font-weight: bold; color: #ffb74d;">
    🌾 Jhum Shifting Cultivation (झूम खेती — मिज़ोरम)
  </div>
  <div class="process-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin: 40px 20px;">
    <div class="step-box" style="background: #3e2723; padding: 15px; border-radius: 8px; border-top: 4px solid #ff9800;">
      <h4 style="color: #ffb74d;">1. Fallow Period</h4>
      <p style="font-size: 13px;">Land left untouched for several years after cutting one crop.</p>
    </div>
    <div class="step-box" style="background: #3e2723; padding: 15px; border-radius: 8px; border-top: 4px solid #f44336;">
      <h4 style="color: #ef5350;">2. Slash & Burn</h4>
      <p style="font-size: 13px;">Bamboos and weeds <strong>cut and burnt</strong> (NOT uprooted); ash enriches soil.</p>
    </div>
    <div class="step-box" style="background: #3e2723; padding: 15px; border-radius: 8px; border-top: 4px solid #4caf50;">
      <h4 style="color: #81c784;">3. Light Sowing</h4>
      <p style="font-size: 13px;">Soil is <strong>lightly furrowed</strong>, never ploughed; mixed seeds dropped.</p>
    </div>
    <div class="step-box" style="background: #3e2723; padding: 15px; border-radius: 8px; border-top: 4px solid #ab47bc;">
      <h4 style="color: #ce93d8;">4. Cheraw Dance</h4>
      <p style="font-size: 13px;">Post-harvest festive bamboo dance celebrated across villages.</p>
    </div>
  </div>
</div>
```

---

## 4. NotebookLM Audio Overview Steering Cue Cards

```markdown
[NOTEBOOKLM STEERING DIRECTIVE: UNIT 2 FLORA & FORESTS]
- Role: Environmental Historian (Host A) & Agronomy Analyst (Host B)
- Focus: Unpack the botanical precision of Desert Oak roots (30x depth) and Jhum cultivation rules.
- Debater Cue: Have Host B express surprise that Jhum farmers burn weeds instead of composting them; Host A explains the mineral ash mechanism and erosion prevention of zero-ploughing.
- Terminology Anchor: Pronounce "Torang (तोरांग = Jungle in Kudukh)", "Bishnoi (बिश्नोई)", and "Cheraw (चेराओ नाच)".
- Guardrail: Never claim Pitcher plant sings or makes musical sounds; it traps purely via sweet fragrance.
```

---

## 5. Formative Inline PYQ Grounding Bank

### Item 1: CTET July 2019 Paper 1 (Q65)
**Question (Bilingual):**
Consider the following statements about 'Desert Oak':
1. It is a tree found in Australia.
2. It has very few leaves.
3. Its roots go deep into the ground nearly 30 times its height until they reach water.
4. This water is stored in the tree trunk.
Which of the statements given above are correct?
*(रेगिस्तानी ओक के बारे में कथनों पर विचार कीजिए: 1. ऑस्ट्रेलिया में पाया जाता है; 2. बहुत कम पत्तियां होती हैं; 3. जड़ें 30 गुना गहराई तक जाती हैं; 4. तने में पानी जमा होता है।)*

- Options:
  1. 1, 2 and 3
  2. 1, 3 and 4
  3. 2, 3 and 4
  4. 1, 2, 3 and 4 (Correct)
- **Official Answer**: `Option 4`
- **Grounding Explanation**: Directly grounded in Class 4 Chapter 19 (*Abdul in the Garden*). All four statements are canonical NCERT factual invariants.

### Item 2: CTET August 2023 Paper 1 (Q61)
**Question (Bilingual):**
Consider the following statements about Jhum Cultivation in Mizoram:
A. After cutting one crop, the land is left as it is for some years.
B. The bamboo and weeds that grow on the land are pulled out and burnt.
C. The ash makes the land fertile.
D. When the land is ready for farming, it is ploughed deeply.
The correct statements are:

- Options:
  1. A and C only
  2. A, B and C
  3. A and D only
  4. B and D only
- **Official Answer**: `Option 1` (A and C are correct; B is incorrect because weeds are cut, not pulled out; D is incorrect because land is lightly dug, not deeply ploughed).
- **Grounding Explanation**: Grounded in Class 5 Chapter 20 (*Whose Forests?*).
"""
    write_unit("unit_2_flora_seeds_forests.md", unit_2)

    # --------------------------------------------------------------------------
    # UNIT 3: Food, Digestion, Cooking & Vector Diseases
    # --------------------------------------------------------------------------
    unit_3 = """# Unit 3: Food, Digestion, Cooking & Vector Diseases
*(भोजन, पाचन क्रिया, पाक कला एवं संक्रामक/वेक्टर जनित रोग)*

> **NCERT Spiral Mapping**: Class 3 (Ch 6, 10) $\\rightarrow$ Class 4 (Ch 15, 20, 21, 25) $\\rightarrow$ Class 5 (Ch 3, 4, 8) $\\rightarrow$ Class 6 Bridge (Science Ch 2)
> **Target Marks Yield**: 3–4 Marks in CTET Paper-1 Non-Pedagogy EVS Section

---

## 1. Encyclopedic Theory & Concept Evolution (Spiral Progression)

### 1.1 Regional Dietary Habits & Cooking Technology (Class 3 & 4)
- **Regional Staple Food Anchors (*Foods We Eat*)**:
  - **Hong Kong**: Snake meat delicacies and snake soup called **Ling-hu-fen (लिंग-हू-फेन)**.
  - **Kashmir**: Freshwater fish cooked in **Mustard Oil (सरसों का तेल)**.
  - **Goa**: Marine sea fish cooked in **Coconut Oil (नारियल का तेल)**.
  - **Kerala**: Boiled **Tapioca (कप्पा)** served with curry prepared using grated coconut.
  - **Assam (*Eating Together*)**: Harvest feast during Magh Bihu featuring **Bora** and **Cheva** sticky rice cooked in a large cauldron (*Kadhahi*).
- **Culinary Thermodynamics & Utensils (*What is Cooking*)**:
  - *Cooking Methods*: Roasting (सेंकना - Roti, Bhutta), Boiling (उबालना - Rice, Dal), Frying (तलना - Puri, Pakoda), Baking (बेक करना - Bati, Bread).
  - *Solar Cooker*: Black-lined interior absorbs maximum solar radiation; plane mirror reflector focuses sunlight; glass sheet prevents convective heat dissipation (greenhouse effect).
- **Spices of Kerala (*Spicy Riddles*)**:
  - *Clove (लौंग)*: Resembles a small nail (*कील जैसी*); highly effective in soothing dental toothaches.
  - *Turmeric (हल्दी)*: Antiseptic rhizome paste used to treat wounds and bruises.
  - *Fennel Seeds (सौंफ)*: Chewed post-meals to aid digestion and provide mouth freshness.
  - *Black Pepper (काली मिर्च)*: Pungent wrinkled black berry.

### 1.2 Digestive Physiology & Food Preservation (Class 5)
- **Gustatory Anatomy & Digestive Mechanics (*From Tasting to Digesting*)**:
  - *Tongue Taste Map*: Sweet receptors at anterior tip; salty and sour on lateral edges; bitter at the posterior base.
  - *Salivary Digestion*: Chewing starchy foods (roti, rice) 30 to 32 times mixes salivary amylase (*ptyalin*), converting complex polysaccharides into sweet maltose.
  - *Dr. William Beaumont & Alexis St. Martin (1822)*: Army surgeon Dr. Beaumont investigated gastric fistula over 9 years:
    - Digestion proceeds **faster inside the human stomach** than in external test tubes due to constant peristaltic churning.
    - Gastric digestive juices are **acidic in nature**.
    - Mental distress, sadness, or fever significantly retards the rate of food digestion.
- **Food Spoilage & Preservation (*Mangoes Round the Year*)**:
  - *Mamidi Tandra (मामिडी तांड्रा / Aam Papad)*: Specialized in **Atreyapuram village (Andhra Pradesh)**; ripe mango pulp blended with equal parts jaggery and sugar, spread in thin daily layers on palm mats in the sun for **4 weeks** until forming a 4 cm golden jelly slab.
  - *Glass Jar Sun Sterilization*: Glass pickle bottles are **dried thoroughly in direct sunlight** to eliminate latent moisture, preventing fungal mold (*spores*) and bacterial colonization.

### 1.3 Vector Biology & Nutritional Deficiencies (Class 5 & 6 Bridge)
- **Malaria & Ronald Ross's Breakthrough (*A Treat for Mosquitoes*)**:
  - *Vector*: Transmitted exclusively by the **Female Anopheles Mosquito** (characterized by brownish body and spotted wings).
  - *Symptoms*: High fever accompanied by severe **chills and shivering (कंपकंपी)**.
  - *Historical Medicine*: Decoction and powder from the **bark of the Cinchona tree (सिनकोना पेड़ की छाल)**; modern Quinine.
  - *Dr. Ronald Ross*: Discovered the mosquito-malaria transmission cycle in Secunderabad/Kolkata; awarded the **Nobel Prize in Physiology or Medicine in 1902**.
- **Anaemia Etiology & Nutrition**:
  - *Cause*: Deficiency of **Haemoglobin or Iron** in blood.
  - *Clinical Normal Range*: **12 to 16 g/dL**.
  - *Prescribed Dietary Remedy*: Daily intake of **Amla (आंवला), Jaggery (गुड़), and Green Leafy Vegetables (पालक, मेथी)**.
- **Vector Eradication Protocols**:
  - Stagnant water oiling: Pouring kerosene forms a thin surface film, increasing surface tension and blocking atmospheric oxygen to mosquito larvae (*larvicidal suffocation*).
  - Biological control: Introducing *Gambusia* fish into ornamental ponds to consume larvae.
- **Biochemical Nutrient Tests & Deficiencies (Class 6 Bridge Science Ch 2)**:
  - *Starch Test*: Sample + Dilute Iodine Solution $\\rightarrow$ **Blue-Black Color**.
  - *Protein Test*: Mashed sample + 2 drops Copper Sulphate ($CuSO_4$) + 10 drops Caustic Soda ($NaOH$) $\\rightarrow$ **Violet Color**.
  - *Fat Test*: Crushed sample on filter paper $\\rightarrow$ **Translucent Greasy Spot**.
  - *Deficiency Diseases*: Vitamin A $\\rightarrow$ Night Blindness; Vitamin B1 $\\rightarrow$ Beriberi; Vitamin C $\\rightarrow$ Scurvy (bleeding gums); Vitamin D $\\rightarrow$ Rickets (soft/bent bones); Iodine $\\rightarrow$ Goitre; Iron $\\rightarrow$ Anaemia.

---

## 2. Zero-Hallucination Entity Vault

| Entity / Concept (Bilingual) | Biological / Nutritional Traits | Exact Invariant Values | Anti-Hallucination Exam Traps |
| :--- | :--- | :--- | :--- |
| **Malaria Vector**<br>*(मलेरिया वाहक)* | Parasitic protozoan (*Plasmodium*) | Transmitted by **Female Anopheles**; treated by **Cinchona bark** | ❌ *Trap*: Male mosquitoes do NOT transmit malaria; Houseflies spread cholera/diarrhea. |
| **Ronald Ross**<br>*(रोनाल्ड रॉस)* | British-Indian army physician | **1902 Nobel Prize** for malaria vector discovery | ❌ *Trap*: Discovered in Secunderabad/Kolkata, NOT in England. |
| **Anaemia Treatment**<br>*(एनीमिया उपचार)* | Iron/haemoglobin deficiency | Normal Hb = **12 to 16 g/dL**; Diet = **Amla + Jaggery + Green Veggies** | ❌ *Trap*: Milk and bananas alone are NOT high-iron anchor answers. |
| **Ling-hu-fen**<br>*(लिंग-हू-फेन)* | Snake meat delicacy | Staple food of **Hong Kong** | ❌ *Trap*: Eaten in Hong Kong, NOT China mainland/Japan in CTET keys. |
| **Starch & Protein Tests**<br>*(खाद्य रासायनिक परीक्षण)* | Biochemical diagnostic assays | Starch = **Iodine $\\rightarrow$ Blue-Black**; Protein = **$CuSO_4 + NaOH \\rightarrow$ Violet** | ❌ *Trap*: Iodine does NOT turn protein violet; Caustic soda is used for protein. |

---

## 3. Hyperframes HTML Video Storyboards & Scene Specs

```html
<!-- Hyperframes Scene 3: Biochemical Food Detection Lab -->
<div class="hyperframe-scene" data-scene="biochem-lab" style="width: 100%; height: 540px; background: #0d1b2a; color: #fff; position: relative; font-family: sans-serif;">
  <div class="header-overlay" style="padding: 20px; font-size: 24px; font-weight: bold; color: #90e0ef;">
    🧪 Biochemical Food Reagents Laboratory
  </div>
  <div class="tubes-container" style="display: flex; justify-content: space-around; margin-top: 60px;">
    <!-- Tube 1: Starch -->
    <div class="test-tube" style="width: 220px; background: #1b263b; border-radius: 12px; padding: 20px; text-align: center; border: 2px solid #0077b6;">
      <h3 style="color: #48cae4;">Starch Test (मंड)</h3>
      <div class="reagent" style="font-size: 13px; color: #ccc; margin: 10px 0;">Reagent: Dilute Iodine</div>
      <div class="color-badge" style="background: #03045e; color: #90e0ef; padding: 10px; border-radius: 6px; font-weight: bold; border: 1px solid #0096c7;">
        🔵 Blue-Black (नीला-काला)
      </div>
    </div>
    <!-- Tube 2: Protein -->
    <div class="test-tube" style="width: 220px; background: #1b263b; border-radius: 12px; padding: 20px; text-align: center; border: 2px solid #7209b7;">
      <h3 style="color: #b5179e;">Protein Test (प्रोटीन)</h3>
      <div class="reagent" style="font-size: 13px; color: #ccc; margin: 10px 0;">Reagents: $CuSO_4$ + $NaOH$</div>
      <div class="color-badge" style="background: #560bad; color: #f72585; padding: 10px; border-radius: 6px; font-weight: bold; border: 1px solid #7209b7;">
        🟣 Violet (बैंगनी)
      </div>
    </div>
    <!-- Tube 3: Anaemia -->
    <div class="test-tube" style="width: 220px; background: #1b263b; border-radius: 12px; padding: 20px; text-align: center; border: 2px solid #38b000;">
      <h3 style="color: #70e000;">Iron Vault (आयरन)</h3>
      <div class="reagent" style="font-size: 13px; color: #ccc; margin: 10px 0;">Target: 12–16 g/dL</div>
      <div class="color-badge" style="background: #007200; color: #ccff33; padding: 10px; border-radius: 6px; font-weight: bold; border: 1px solid #38b000;">
        🌿 Amla + Jaggery + Spinach
      </div>
    </div>
  </div>
</div>
```

---

## 4. NotebookLM Audio Overview Steering Cue Cards

```markdown
[NOTEBOOKLM STEERING DIRECTIVE: UNIT 3 FOOD & DISEASES]
- Role: Clinical Epidemiologist (Host A) & Culinary Anthropologist (Host B)
- Focus: Dialogue exploring Ronald Ross's 1902 discovery and the exact physiological reasons why Dr. Beaumont found stomach digestion faster inside the body.
- Debater Cue: Have Host B inquire about fish cooked in mustard oil vs coconut oil; Host A explains the geographic ecology of Kashmir (mustard) vs Goa (coconut).
- Terminology Anchor: Pronounce "Ling-hu-fen (लिंग-हू-फेन)", "Cinchona (सिनकोना)", "Mamidi Tandra (मामिडी तांड्रा)".
- Guardrail: Always maintain that normal Haemoglobin is 12-16 g/dL and Iron sources are strictly Amla, Jaggery, and Green Leafy Vegetables.
```

---

## 5. Formative Inline PYQ Grounding Bank

### Item 1: CTET Jan 2021 Paper 1 (Q63)
**Question (Bilingual):**
Which one of the following groups of eatables is rich in Iron?
*(निम्नलिखित में से कौन सा खाद्य पदार्थों का समूह आयरन (लौह तत्व) से भरपूर है?)*

- Options:
  1. Amla, Spinach, Jaggery (आंवला, पालक, गुड़) (Correct)
  2. Amla, Tomato, Jaggery
  3. Spinach, Onion, Tomato
  4. Cabbage, Amla, Spinach
- **Official Answer**: `Option 1`
- **Grounding Explanation**: Grounded in Class 5 Chapter 8 (*A Treat for Mosquitoes*). NCERT explicitly prescribes Amla, Jaggery, and green leafy vegetables (spinach) to elevate hemoglobin.

### Item 2: CTET July 2024 Paper 1 (Q61)
**Question (Bilingual):**
In Kerala, boiled tapioca (kappa) is most commonly consumed with:
*(केरल में टैपियोका (कप्पा) मुख्य रूप से किसके साथ खाया जाता है?)*

- Options:
  1. Curry made using coconut (नारियल की करी) (Correct)
  2. Mustard fish curry
  3. Sweetened dal
  4. Puran Poli
- **Official Answer**: `Option 1`
- **Grounding Explanation**: Directly verifiable from Class 3 Chapter 6 (*Foods We Eat*).
"""
    write_unit("unit_3_food_digestion_diseases.md", unit_3)

    # --------------------------------------------------------------------------
    # UNIT 4: Shelter, Architecture & Climatic Adaptations
    # --------------------------------------------------------------------------
    unit_4 = """# Unit 4: Shelter, Architecture & Climatic Adaptations
*(आवास, स्थापत्य कला एवं जलवायु आधारित अनुकूलन)*

> **NCERT Spiral Mapping**: Class 3 (Ch 5, 18) $\\rightarrow$ Class 4 (Ch 12, 17) $\\rightarrow$ Class 5 (Ch 13, 14, 15, 18)
> **Target Marks Yield**: 2–3 Marks in CTET Paper-1 Non-Pedagogy EVS Section

---

## 1. Encyclopedic Theory & Concept Evolution (Spiral Progression)

### 1.1 Climatic Vernacular Typologies of India (Class 3 & 4)
- **Regional House Typologies (*A House Like This*)**:
  - **Assam (Molan Village / Extreme Rain)**: Houses elevated **10 to 12 feet (3 to 3.5 meters)** above ground on robust **bamboo pillars (बांस के खंभे)**; steep sloping roofs constructed from bamboo and thatch to shed torrential monsoon rains rapidly; interiors made of wood.
  - **Manali (Himachal Pradesh / Mountain Snow)**: Mountainous terrain with dual precipitation of heavy rainfall and snowfall; houses built of **stone and wood with sloping roofs**.
  - **Rajasthan (Arid Thar Desert / Extreme Heat)**: Houses engineered with **extremely thick mud walls** that insulate interior living spaces from exterior heat; plastered smoothly with **cow dung and mud**; thatched roofs constructed of **thorny Keekar bushes (कंटीली झाड़ियाँ)**.
  - **Delhi / Urban Plains**: Dense multi-storey high-rises constructed from kiln-fired bricks, cement, sand, steel rods, and glass.
  - **Polar Zones**: Dome-shaped **Igloos** crafted from compressed snow blocks; trapped indoor body heat creates a warm microclimate.
- **Traditional Mud Plastering Chemistry (*Changing Times*)**:
  - Adding **cow dung to mud plaster** prevents insect, termite, and microbial infestation in dirt floors.
  - Roof framing constructed from **Neem and Keekar wood** because their bitter alkaloids protect rafters from wood-boring termites.

### 1.2 High-Altitude Nomadic Architecture & Lacustrine Living (Class 5)
- **Leh & Ladakh Cold Desert Architecture (*A Shelter so High!*)**:
  - *Leh Two-Storey Stone Houses*: Built of rough stone blocks plastered with thick mud and white lime; **ground floor has NO WINDOWS** and serves as livestock pen and winter grain storage; family resides on the upper floor; roof is completely **flat, made of thick poplar tree trunks**, utilized in summer to dry red chillies, sweet corn, pumpkins, and paddy.
- **Changpa Nomadic Architecture (Changthang Plateau at 5000m)**:
  - *Rebo (रेबो)*: Conical tents woven from **strips of coarse Yak hair** stitched together; ground is dug 2 feet deep and tent is pitched over the pit; yak hair provides windproof warmth against $-40^\\circ\\text{C}$ gales.
  - *Lekha (लेखा)*: Open stone-walled enclosure erected adjacent to Rebo to secure goats and sheep; each nomad marks their livestock with unique family pigment stamps.
  - *Pashmina Invariants*: Yielded by **Changthangi goats** pastured at 5000 meters; **6 pashmina hairs equal the thickness of 1 human hair**; provides the warmth of **6 standard sweaters**; requiring **250 hours of handloom weaving** per plain shawl.
- **Kashmiri Lacustrine & Urban Architecture (Srinagar)**:
  - *Houseboats (हाउसबोट)*: Floating vessels on Dal Lake and Jhelum river extending up to **80 feet in length** and 8–9 feet in width.
  - *Donga (डोंगा)*: Wooden riverboats divided into separate residential rooms for local Kashmiri families.
  - *Khatamband (खत्मबंद)*: Intricate ceiling woodwork carvings interlocking like a **jigsaw puzzle**.
  - *Mehraab (मेहराब)*: Semicircular pointed architectural arches framing doorways and windows.
  - *Dab (डब)*: Overhanging wooden bay lattice windows projecting outward from brick walls.

### 1.3 Disaster Architecture & Thermodynamics (Class 5)
- **Earthquake-Resistant Vernacular Architecture (*When the Earth Shook!*)**:
  - *Bhuj Earthquake (26 January 2001, Kutch, Gujarat)*: Vernacular round clay houses (*Bhungas*) decorated with mirror inlays withstood seismic tremors far better than rigid concrete structures.
  - *Safety Protocol*: Drop, Cover, and Hold beneath a sturdy table or bed in an interior room corner.
- **Thermal Respiration Thermodynamics (*Blow Hot, Blow Cold* by Dr. Zakir Hussain)**:
  - Exhaled breath warms cold hands in winter (body core temperature $\\approx 37^\\circ\\text{C}$ vs near-freezing ambient air).
  - Exhaled breath cools steaming hot potatoes via forced convective heat loss.

---

## 2. Zero-Hallucination Entity Vault

| Architecture / Shelter (Bilingual) | Structural Material & Mechanism | Exact Invariant Values | Anti-Hallucination Exam Traps |
| :--- | :--- | :--- | :--- |
| **Assam Stilt House**<br>*(असम के बांस के घर)* | Bamboo pillars + Sloping roof + Wood interior | **10 to 12 feet** (**3 to 3.5 m**) above ground | ❌ *Trap*: Assam houses have sloping roofs, NOT flat roofs; on bamboo, not stone pillars. |
| **Leh Two-Storey House**<br>*(लेह के पत्थर के घर)* | Stone coated with mud/lime + Poplar flat roof | **2 storeys**; **Ground floor has NO windows** | ❌ *Trap*: Ground floor is for animals/storage without windows; roofs are FLAT, not sloping. |
| **Changpa Rebo Tent**<br>*(चांगपा का रेबो तंबू)* | Woven Yak hair strips stitched into cone | Pit dug **2 feet deep**; altitude **5000 m** | ❌ *Trap*: Made of Yak hair, NOT camel or sheep hair; Rebo is tent, Lekha is animal pen. |
| **Kashmir Houseboat**<br>*(कश्मीर की हाउसबोट)* | Cedar wood on Dal lake / Jhelum river | Up to **80 feet long**, 8–9 feet wide | ❌ *Trap*: Khatamband is ceiling puzzle woodwork, NOT a boat type. |
| **Rajasthan Mud Hut**<br>*(राजस्थान के मिट्टी के घर)* | Thick mud walls + Cow dung plaster | Roofs of **thorny Keekar bushes** | ❌ *Trap*: Roofs are thorny bushes/thatch, NOT sloping slate tiles. |

---

## 3. Hyperframes HTML Video Storyboards & Scene Specs

```html
<!-- Hyperframes Scene 4: Comparative Architectural Matrix -->
<div class="hyperframe-scene" data-scene="shelter-matrix" style="width: 100%; height: 540px; background: #1e293b; color: #fff; position: relative; font-family: sans-serif;">
  <div class="header-overlay" style="padding: 20px; font-size: 24px; font-weight: bold; color: #38bdf8;">
    🏠 Vernacular Climatic Architecture of India
  </div>
  <div class="shelter-grid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin: 40px 20px;">
    <!-- Assam -->
    <div class="shelter-card" style="background: #0f172a; padding: 15px; border-radius: 10px; border-left: 5px solid #22c55e;">
      <h3 style="color: #4ade80; margin: 0 0 10px 0;">Assam (असम)</h3>
      <p style="font-size: 13px; line-height: 1.6;">• 10–12 feet on bamboo pillars<br>• Sloping roof for heavy rains<br>• Made of wood and bamboo</p>
    </div>
    <!-- Leh -->
    <div class="shelter-card" style="background: #0f172a; padding: 15px; border-radius: 10px; border-left: 5px solid #0ea5e9;">
      <h3 style="color: #38bdf8; margin: 0 0 10px 0;">Leh (लद्दाख)</h3>
      <p style="font-size: 13px; line-height: 1.6;">• Two-storey stone & mud walls<br>• Ground floor has NO windows<br>• Flat poplar wood roofs</p>
    </div>
    <!-- Rajasthan -->
    <div class="shelter-card" style="background: #0f172a; padding: 15px; border-radius: 10px; border-left: 5px solid #f59e0b;">
      <h3 style="color: #fbbf24; margin: 0 0 10px 0;">Rajasthan (राजस्थान)</h3>
      <p style="font-size: 13px; line-height: 1.6;">• Thick insulating mud walls<br>• Cow dung protective plaster<br>• Thorny Keekar bush roofs</p>
    </div>
  </div>
</div>
```

---

## 4. NotebookLM Audio Overview Steering Cue Cards

```markdown
[NOTEBOOKLM STEERING DIRECTIVE: UNIT 4 SHELTER & CLIMATE]
- Role: Vernacular Architectural Engineer (Host A) & Cultural Geographer (Host B)
- Focus: Highlight the architectural brilliance of Leh two-storey houses and the 10-12 feet bamboo stilt houses of Assam.
- Debater Cue: Have Host B question why Leh roofs are flat while Manali roofs are sloping; Host A clarifies that Leh is a dry cold desert where roofs are used to dry winter food in sunlight, whereas Manali receives heavy snow and rain.
- Terminology Anchor: Pronounce "Rebo (रेबो)", "Lekha (लेखा)", "Khatamband (खत्मबंद)", "Mehraab (मेहराब)", "Dab (डब)".
- Guardrail: Do not confuse Rebo (tent) with Lekha (pen).
```

---

## 5. Formative Inline PYQ Grounding Bank

### Item 1: CTET August 2023 Paper 1 (Q62)
**Question (Bilingual):**
"It rains heavily in our village. Our houses are made almost 10 to 12 feet above the ground on strong bamboo pillars. The inside of our houses is also made of wood." Which state does this village belong to?
*('हमारे गाँव में बहुत वर्षा होती है। हमारे घर जमीन से लगभग 10 से 12 फीट ऊँचे मजबूत बांस के खंभों पर बनाए जाते हैं। अंदर से भी घर लकड़ी के बने होते हैं।' यह गाँव किस राज्य में है?)*

- Options:
  1. Tamil Nadu
  2. Assam (असम) (Correct)
  3. Uttarakhand
  4. Rajasthan
- **Official Answer**: `Option 2`
- **Grounding Explanation**: Direct quote from Class 3 Chapter 18 (*A House Like This*) describing Molan village in Assam.

### Item 2: CTET Dec 2022 CBT Paper 1
**Question (Bilingual):**
The Changpa nomadic tribe of Ladakh pitches their large cone-shaped tents called:
*(लद्दाख की चांगपा जनजाति अपने बड़े शंक्वाकार तंबू को क्या कहती है?)*

- Options:
  1. Lekha
  2. Rebo (रेबो) (Correct)
  3. Khatamband
  4. Donga
- **Official Answer**: `Option 2`
- **Grounding Explanation**: Grounded in Class 5 Chapter 13 (*A Shelter so High!*).
"""
    write_unit("unit_4_shelter_architecture_climate.md", unit_4)

    # --------------------------------------------------------------------------
    # UNIT 5: Water Systems, Conservation & Historical Science
    # --------------------------------------------------------------------------
    unit_5 = """# Unit 5: Water Systems, Conservation & Historical Science
*(जल प्रणालियाँ, ऐतिहासिक जल संरक्षण एवं जल विज्ञान)*

> **NCERT Spiral Mapping**: Class 3 (Ch 3, 9, 20) $\\rightarrow$ Class 4 (Ch 13, 18) $\\rightarrow$ Class 5 (Ch 6, 7) $\\rightarrow$ Class 6 Bridge (Science Ch 14)
> **Target Marks Yield**: 2–3 Marks in CTET Paper-1 Non-Pedagogy EVS Section

---

## 1. Encyclopedic Theory & Concept Evolution (Spiral Progression)

### 1.1 Hydrological Cycles & Arid Rainwater Catchment (Class 3 & 4)
- **States of Water & Rainfall Mechanics (*Water O' Water!* & *It's Raining*)**:
  - Reversible physical transitions between solid (ice/snow), liquid (freshwater bodies), and vapor (steam/clouds).
- **Courtyard Tanka Architecture (*Drop by Drop*)**:
  - *Location*: Bajju village in Rajasthan.
  - *Structure*: Underground cemented cistern (*टांका*) excavated in the central courtyard; courtyard floor paved with a gradient sloping towards the tanka aperture; rainfall collected on sloping roofs flows down an inlet pipe fitted with a fine mesh/sieve filter into the covered cistern for multi-month drought storage.
- **Hydrological Rehabilitation & Youth Governance (*Too Much Water, Too Little Water*)**:
  - *Bhima Sangh (भीमा संघ)*: Revolutionary Children's Panchayat established in **Holgundi village (Karnataka)**; mapped historical hill tanks, cleared silt, rebuilt stone check dams, and permanently re-established groundwater levels.
  - *Clinical ORS Formulation*: Prepared by dissolving **1 teaspoon of sugar + 1 pinch of salt** in **1 glass of boiled and cooled water** to combat dehydration from diarrhea and vomiting.

### 1.2 Medieval Hydraulic Civil Engineering & Travelers (Class 5)
- **Ghadsisar 9-Lake Interconnected Network (*Every Drop Counts*)**:
  - Commissioned 650 years ago by King Ghadsi of **Jaisalmer (Rajasthan)**.
  - Engineered as **9 interconnected lakes**: Rain runoff filled the first lake; excess overflow channeled through sluice gates to fill the second, continuing sequentially down all 9 reservoirs.
- **Al-Biruni's 11th-Century Hydraulic Chronicles**:
  - Polymath traveler from **Uzbekistan** visiting India in the 11th century; celebrated Indian masonry, reservoirs, and stepwells in *Kitab al-Hind*:
  - *"They pile huge rocks and join them with iron rods to build platforms (chabutras) all around lakes. Between these, there are long staircases going up and down. The steps for going up and coming down are separate, preventing crowd congestion."*
  - Commemorative postage stamp issued by the Indian Postal Department in **1973** (1000th birth anniversary).
- **Tarun Bharat Sangh & Darki Mai (Alwar, Rajasthan)**:
  - Revival of dried aquifers through community construction of crescent earthen check dams (**Johads / जोहड़**).

### 1.3 Fluid Mechanics, Salinity & Historical Satyagraha (Class 5 & 6 Bridge)
- **Buoyancy & Fluid Density (*Experiments with Water*)**:
  - *Archimedes Principle in Practice*: Solid iron nail sinks because it displaces a water weight less than its own mass; hollow steel bowl/ship floats because broad volume displaces water weight exceeding vessel mass.
  - *Egg Salt Flotation*: Fresh egg sinks in pure water, but floats buoyant when sufficient salt is dissolved (dissolved salt raises liquid density above egg density).
  - *Dead Sea (मृत सागर)*: Saltiest water body on Earth containing **300 grams of salt per 1 liter of water** ($30\\%\\text{ salinity}$); human beings float comfortably on the surface without sinking.
- **Dandi Salt March (1930)**:
  - Historic freedom campaign led by **Mahatma Gandhi** from Sabarmati Ashram (Ahmedabad) to Dandi seashore (Gujarat), defying the British salt monopoly.
- **Hydrological Cycle Thermodynamics (Class 6 Bridge Science Ch 14)**:
  - Evaporation rate directly proportional to **surface area, ambient temperature, and wind speed**.
  - Evaporation $\\rightarrow$ Transpiration $\\rightarrow$ Adiabatic High-Altitude Condensation $\\rightarrow$ Precipitation $\\rightarrow$ Infiltration.

---

## 2. Zero-Hallucination Entity Vault

| Entity / System (Bilingual) | Hydraulic Mechanism & Heritage | Exact Invariant Values | Anti-Hallucination Exam Traps |
| :--- | :--- | :--- | :--- |
| **Dead Sea**<br>*(मृत सागर)* | Hypersaline inland body where humans float | **300 grams salt per 1 liter water** | ❌ *Trap*: Dead Sea has 300g salt/L, NOT 30g or 500g; humans do NOT sink. |
| **Ghadsisar Lake**<br>*(घड़सीसर झील)* | Jaisalmer rainwater reservoir network | **650 years old**; **9 interconnected lakes** | ❌ *Trap*: Built by King Ghadsi in Jaisalmer, NOT Jaipur or Udaipur. |
| **Al-Biruni**<br>*(अल-बिरूनी)* | Historian who documented Indian stepwells | Came from **Uzbekistan** >1000 yrs ago (11th c.); **1973 stamp** | ❌ *Trap*: Traveled from Uzbekistan, NOT Afghanistan, Persia, or Morocco. |
| **Bhima Sangh**<br>*(भीमा संघ)* | Children's Panchayat water revival | Located in **Holgundi village, Karnataka** | ❌ *Trap*: Children's panchayat in Karnataka, NOT Rajasthan or Maharashtra. |
| **Dandi March**<br>*(दांडी यात्रा)* | Salt Satyagraha against British salt taxation | **1930 AD**; Sabarmati to Dandi (Gujarat) | ❌ *Trap*: Took place in 1930, NOT 1942 or 1920. |

---

## 3. Hyperframes HTML Video Storyboards & Scene Specs

```html
<!-- Hyperframes Scene 5: Ghadsisar Sequential Overflow System -->
<div class="hyperframe-scene" data-scene="ghadsisar-cascade" style="width: 100%; height: 540px; background: #0c4a6e; color: #fff; position: relative; font-family: sans-serif;">
  <div class="header-overlay" style="padding: 20px; font-size: 24px; font-weight: bold; color: #7dd3fc;">
    💧 Ghadsisar 9-Lake Interconnected Hydraulic Cascade (Jaisalmer)
  </div>
  <div class="cascade-flow" style="display: flex; align-items: center; justify-content: space-around; margin-top: 80px;">
    <div class="lake-node" style="width: 160px; height: 140px; background: #0369a1; border-radius: 12px; border: 3px solid #38bdf8; display: flex; flex-direction: column; align-items: center; justify-content: center;">
      <span style="font-size: 20px; font-weight: bold;">Lake 1</span>
      <span style="font-size: 12px; color: #bae6fd;">Rain Catchment</span>
    </div>
    <div class="overflow-arrow" style="font-size: 36px; color: #7dd3fc;">➔</div>
    <div class="lake-node" style="width: 160px; height: 140px; background: #0284c7; border-radius: 12px; border: 3px solid #38bdf8; display: flex; flex-direction: column; align-items: center; justify-content: center;">
      <span style="font-size: 20px; font-weight: bold;">Lake 2</span>
      <span style="font-size: 12px; color: #bae6fd;">Overflow Gate</span>
    </div>
    <div class="overflow-arrow" style="font-size: 36px; color: #7dd3fc;">➔ ... ➔</div>
    <div class="lake-node" style="width: 160px; height: 140px; background: #0ea5e9; border-radius: 12px; border: 3px solid #38bdf8; display: flex; flex-direction: column; align-items: center; justify-content: center;">
      <span style="font-size: 20px; font-weight: bold;">Lake 9</span>
      <span style="font-size: 12px; color: #bae6fd;">Year-Round Store</span>
    </div>
  </div>
</div>
```

---

## 4. NotebookLM Audio Overview Steering Cue Cards

```markdown
[NOTEBOOKLM STEERING DIRECTIVE: UNIT 5 WATER SYSTEMS]
- Role: Civil Hydraulic Historian (Host A) & Fluid Physicist (Host B)
- Focus: Analyze Al-Biruni's accounts of Indian stepwells with separate entrance/exit staircases and the physics of Dead Sea flotation (300g salt/L).
- Debater Cue: Have Host B challenge how human bodies float on the Dead Sea without life jackets; Host A explains the specific gravity equation.
- Terminology Anchor: Pronounce "Al-Biruni (अल-बिरूनी - उज्बेकिस्तान)", "Bawri (बावड़ी)", "Ghadsisar (घड़सीसर)", "Johad (जोहड़)".
- Guardrail: Explicitly confirm that Bhima Sangh is in Holgundi, Karnataka.
```

---

## 5. Formative Inline PYQ Grounding Bank

### Item 1: CTET July 2019 Paper 1 (Q63)
**Question (Bilingual):**
Consider the following statements about Stepwells (Bawris):
1. They are traditional systems of water storage and conservation.
2. They were used as community centers.
3. They have staircases going down several storeys.
4. Only contaminated water is stored in them.
Which of the statements given above are correct?
*(बावड़ी के बारे में कथनों पर विचार कीजिए: 1. जल संरक्षण की पारंपरिक प्रणाली हैं; 2. सामुदायिक केंद्रों के रूप में प्रयुक्त होते थे; 3. कई मंजिल नीचे जाने वाली सीढ़ियाँ होती हैं; 4. केवल गंदा पानी होता है।)*

- Options:
  1. 1 and 2 only
  2. 1, 2 and 3 (Correct)
  3. 2 and 4 only
  4. 1, 2, 3 and 4
- **Official Answer**: `Option 2`
- **Grounding Explanation**: Grounded in Class 5 Chapter 6 (*Every Drop Counts*). Statements 1, 2, 3 are historically accurate; 4 is false.
"""
    write_unit("unit_5_water_systems_conservation.md", unit_5)

    # --------------------------------------------------------------------------
    # UNIT 6: Travel, Culture, Traditional Arts & Space
    # --------------------------------------------------------------------------
    unit_6 = """# Unit 6: Travel, Culture, Traditional Arts & Space
*(यात्रा, संस्कृति, पारंपरिक कलाएं, अंतरिक्ष एवं ऐतिहासिक धरोहर)*

> **NCERT Spiral Mapping**: Class 3 (Ch 4, 7, 11, 12, 13, 15, 16, 17, 21, 23) $\\rightarrow$ Class 4 (Ch 1, 6, 7, 8, 9, 10, 22, 23, 24, 26, 27) $\\rightarrow$ Class 5 (Ch 9, 10, 11, 12, 16, 17, 22)
> **Target Marks Yield**: 4–5 Marks in CTET Paper-1 Non-Pedagogy EVS Section

---

## 1. Encyclopedic Theory & Concept Evolution (Spiral Progression)

### 1.1 Tactile Writing, Postal Networks & Regional Handlooms (Class 3 & 4)
- **Braille Tactile Code (*Sharing Our Feelings*)**:
  - Invented by **Louis Braille** (France, 1809–1852).
  - Code matrix: Standard Braille characters are embossed on thick cardstock using **6 raised dots arranged in a 2x3 matrix cell**. Read by tactile finger scanning.
- **Traditional Handlooms & Folk Art Matrix (*Pochampally* & *The Valley of Flowers*)**:
  - **Pochampally & Kalamkari**: Mukhtarpur village in **Pochampally district (Telangana)**; geometric silk sarees dyed and woven on pit looms.
  - **Madhubani Folk Art**: Ancient painting tradition from Madhubani district (**Bihar**); made from a paste of **powdered rice mixed with natural dyes** (Indigo, Turmeric, floral pigments); portrays humans, animals, birds, and fish.
  - **Kannauj Itr Industry**: Kannauj (**Uttar Pradesh**) steam-distills truckloads of rose and jasmine blossoms in copper cauldrons (*degs*) to craft pure Itr, Rose water, and Kewra water.
  - **Kullu Shawls**: Hand-woven woolens from **Himachal Pradesh**.
- **Railway Infrastructure & Ticket Numeracy (*Omana's Journey* & *From the Window*)**:
  - Konkan Railway route from Goa to Kerala passes through **2000 bridges and 92 tunnels** through the Western Ghats.
  - *Standard Train Ticket (PNR) Data*: Explicitly displays Train Number, Journey Start Date, Coach and Berth Numbers, Total Fare (INR), and Exact Distance in Kilometers (km).

### 1.2 Trailblazing Heroines & Sports History (Class 4 & 5)
- **Karnam Malleswari (*Hu Tu Tu, Hu Tu Tu*)**:
  - International Olympic weightlifter from **Andhra Pradesh**; father is a police constable; commenced weight training at **age 12**; lifted up to **130 kg**; earned **29 international medals**; first Indian woman to secure an Olympic medal (Sydney 2000).
- **Lt. Commander Wahida Prism (*Defence Officer: Wahida*)**:
  - Naval surgeon from Thannamandi (Rajouri, Jammu & Kashmir); **first woman in Indian military history to lead a full armed forces passing-out parade**; delivered **36 platoon commands**; named 'Prism' because glass prisms refract and disperse 7 colors of light.
- **Bachendri Pal's Everest Ascent (*Up You Go!*)**:
  - Grew up in Nakuri village (Garhwal, Uttarakhand); trained under Brigadier Gyan Singh at NIM Uttarkashi.
  - Conquered the summit of **Mount Everest (known as Sagarmatha in Nepal - 8848 meters)** on **23 May 1984 at 1:07 PM**; planted the Indian tricolor and remained on the summit for **43 minutes**; **first Indian woman and 5th woman in the world** to summit Everest.

### 1.3 Spaceflight Microgravity & Medieval Fortifications (Class 5)
- **Sunita Williams & Zero-Gravity Spaceflight (*Sunita in Space*)**:
  - NASA astronaut spending **over 6 months in low Earth orbit (ISS at ~360 km)**.
  - *Microgravity Phenomena*: Food and water float as globules; hair stays standing upright; astronauts tether themselves to workstations.
  - *Planetary Perspective*: Earth viewed from space shows no artificial political borderlines.
- **Golconda Fort Metallurgy & Fortifications (*Walls Tell Stories*)**:
  - Ruled by Qutb Shahi Sultans (1518–1687) in Hyderabad (Telangana); constructed with **87 high surveillance bastions (बुर्ज)**.
  - Mughal Emperor Aurangzeb besieged the fort with cannons for **8 months** without breaching the deep moats.
  - *Bronze Metallurgy*: **Bronze is an alloy of Copper and Tin (Cu + Sn)**.

---

## 2. Zero-Hallucination Entity Vault

| Trailblazer / Entity (Bilingual) | Domain & Cultural Geography | Exact Invariant Values | Anti-Hallucination Exam Traps |
| :--- | :--- | :--- | :--- |
| **Bachendri Pal**<br>*(बछेंद्री पाल)* | Mountaineering (Everest / Sagarmatha) | Summit: **23 May 1984, 1:07 PM**; Alt: **8848 m**; Peak stay: **43 min** | ❌ *Trap*: First Indian woman (5th in world), NOT first woman in world; Everest is Sagarmatha in Nepal. |
| **Karnam Malleswari**<br>*(कर्णम मल्लेश्वरी)* | Olympic Weightlifting (Andhra Pradesh) | Started at **12 yrs**; Max lift: **130 kg**; **29 medals** | ❌ *Trap*: From Andhra Pradesh, NOT Karnataka; lifted 130kg, not 200kg. |
| **Wahida Prism**<br>*(वहीदा प्रिज्म)* | Naval Surgeon (Rajouri, J&K) | **First woman parade commander**; **36 commands** | ❌ *Trap*: Naval surgeon, NOT air force pilot; parade has 36 commands. |
| **Sunita Williams**<br>*(सुनीता विलियम्स)* | NASA Spaceflight Astronaut | **>6 months in space**; **360 km orbit** | ❌ *Trap*: Neil Armstrong walked on Moon (1969); Sunita flew in ISS. |
| **Braille Script**<br>*(ब्रेल लिपि)* | Embossed blind reading system (Louis Braille) | **6 raised dots** in 2x3 matrix | ❌ *Trap*: Based on 6 dots, NOT 8 dots. |
| **Pochampally**<br>*(पोचमपल्ली)* | Traditional Ikat silk handlooms | Mukhtarpur village, **Telangana** | ❌ *Trap*: Pochampally is in Telangana (earlier AP), not Kerala or Tamil Nadu. |
| **Madhubani**<br>*(मधुबनी चित्रकला)* | Natural paste of powdered rice folk art | Madhubani district, **Bihar** | ❌ *Trap*: Made of powdered rice with natural dyes; depicts flora, fauna, and humans. |

---

## 3. Hyperframes HTML Video Storyboards & Scene Specs

```html
<!-- Hyperframes Scene 6: Trailblazing Women of India Showcase -->
<div class="hyperframe-scene" data-scene="women-trailblazers" style="width: 100%; height: 540px; background: #311042; color: #fff; position: relative; font-family: sans-serif;">
  <div class="header-overlay" style="padding: 20px; font-size: 24px; font-weight: bold; color: #f472b6;">
    ⭐ Indian Trailblazers (चमकते सितारे)
  </div>
  <div class="trailblazers-grid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin: 40px 20px;">
    <!-- Bachendri Pal -->
    <div class="profile-card" style="background: #4c1d95; padding: 20px; border-radius: 12px; border-top: 4px solid #ec4899;">
      <h3 style="color: #fbcfe8; margin: 0 0 8px 0;">Bachendri Pal</h3>
      <p style="font-size: 13px; line-height: 1.6;">• 1st Indian woman on Everest<br>• 23 May 1984 at 1:07 PM<br>• Altitude: 8848m (43 mins)</p>
    </div>
    <!-- Karnam Malleswari -->
    <div class="profile-card" style="background: #4c1d95; padding: 20px; border-radius: 12px; border-top: 4px solid #a855f7;">
      <h3 style="color: #fbcfe8; margin: 0 0 8px 0;">Karnam Malleswari</h3>
      <p style="font-size: 13px; line-height: 1.6;">• Olympic Weightlifter (AP)<br>• Max lift: 130 kg (started age 12)<br>• 29 International medals</p>
    </div>
    <!-- Wahida Prism -->
    <div class="profile-card" style="background: #4c1d95; padding: 20px; border-radius: 12px; border-top: 4px solid #6366f1;">
      <h3 style="color: #fbcfe8; margin: 0 0 8px 0;">Wahida Prism</h3>
      <p style="font-size: 13px; line-height: 1.6;">• Naval Medical Officer (J&K)<br>• 1st woman to lead parade<br>• Shouted 36 parade commands</p>
    </div>
  </div>
</div>
```

---

## 4. NotebookLM Audio Overview Steering Cue Cards

```markdown
[NOTEBOOKLM STEERING DIRECTIVE: UNIT 6 CULTURE & SPACE]
- Role: Cultural Historian (Host A) & Space/Aviation Biographer (Host B)
- Focus: Highlight the biographical milestones of Bachendri Pal (Everest 8848m), Karnam Malleswari (130 kg), and Sunita Williams (>6 mo in orbit).
- Debater Cue: Have Host B challenge the composition of Bronze; Host A confirms it is strictly an alloy of Copper and Tin used in Golconda cannons.
- Terminology Anchor: Pronounce "Sagarmatha (सागरमाथा)", "Pochampally (पोचमपल्ली)", "Madhubani (मधुबनी)", "Wahida Prism (वहीदा प्रिज्म)".
- Guardrail: Emphasize that Braille is 6 dots, never 8.
```

---

## 5. Formative Inline PYQ Grounding Bank

### Item 1: CTET July 2019 Paper 1 (Q62)
**Question (Bilingual):**
Consider the following statements about Karnam Malleswari:
1. She is a weightlifter of international fame.
2. She is from Andhra Pradesh.
3. She has many records to her credit. She could lift weights up to 130 kg.
4. She started lifting weights when she was 12 years old.
Which of the statements given above are correct?
*(कर्णम मल्लेश्वरी के विषय में विचार कीजिए: 1. अंतरराष्ट्रीय भारोत्तोलक; 2. आंध्र प्रदेश की हैं; 3. 130 किग्रा भार उठाया; 4. 12 वर्ष की आयु में शुरुआत की।)*

- Options:
  1. 1, 2 and 3
  2. 1, 2 and 4
  3. 1 and 4 only
  4. 1, 2, 3 and 4 (Correct)
- **Official Answer**: `Option 4`
- **Grounding Explanation**: All 4 statements are direct verbatim facts from Class 4 Chapter 10 (*Hu Tu Tu, Hu Tu Tu*).

### Item 2: CTET Jan 2024 Paper 1 (Q61)
**Question (Bilingual):**
Bachendri Pal reached the summit of Mount Everest on 23 May 1984. Mount Everest is known as Sagarmatha in:
*(माउंट एवरेस्ट को 'सागरमाथा' कहाँ कहा जाता है?)*

- Options:
  1. Tibet
  2. Nepal (नेपाल) (Correct)
  3. Bhutan
  4. India
- **Official Answer**: `Option 2`
- **Grounding Explanation**: Verifiable from Class 5 Chapter 9 (*Up You Go!*).
"""
    write_unit("unit_6_travel_culture_space.md", unit_6)

    # --------------------------------------------------------------------------
    # UNIT 7: Quantitative & Spatial Bridge
    # --------------------------------------------------------------------------
    unit_7 = """# Unit 7: Quantitative & Spatial Bridge
*(मात्रात्मक एवं स्थानिक सेतु: मानचित्र पैमाना, दिशा बोध एवं चाल-दूरी-समय)*

> **NCERT Spiral Mapping**: Class 3 (Ch 22) $\\rightarrow$ Class 4 (Ch 6, 8) $\\rightarrow$ Class 5 (Ch 1, 13) $\\rightarrow$ Class 6 Bridge (Geography Ch 4)
> **Target Marks Yield**: 2–3 Marks in CTET Paper-1 Non-Pedagogy EVS Section

---

## 1. Encyclopedic Theory & Concept Evolution (Spiral Progression)

### 1.1 Cardinal Directions & Relative Geographic Positioning
- **Cartesian Compass Framework (Class 6 Geography Ch 4)**:
  - *Four Cardinal Directions*: North (top of map / $0^\\circ$), South (bottom / $180^\\circ$), East (right / $90^\\circ$), West (left / $270^\\circ$).
  - *Four Intermediate Directions*: North-East (NE), South-East (SE), South-West (SW), North-West (NW).
- **Indian Maritime Border & Coastal States Matrix**:
  - **Arabian Sea Coastal States (अरब सागर के तटवर्ती राज्य)**: Gujarat, Maharashtra, Goa, Karnataka, Kerala, Tamil Nadu (southern apex).
  - **Bay of Bengal Coastal States (बंगाल की खाड़ी के तटवर्ती राज्य)**: West Bengal, Odisha, Andhra Pradesh, Tamil Nadu.
  - **Landlocked Strategic Reference Points**: New Delhi, Bhopal (Madhya Pradesh), Ranchi (Jharkhand), Patna (Bihar), Gandhinagar (Gujarat).
- **Direction Vector Inversion Rule (Dr. X / Home-Hospital Problems)**:
  - *Algorithm*: Plot sequential movements on Cartesian axes ($X$: East $+$, West $-$; $Y$: North $+$, South $-$). Calculate net displacement vector $\\vec{R} = (\\Delta X, \\Delta Y)$ from Start to End.
  - *Inversion Gate*: When the exam asks "What is the direction of the **Starting Point with respect to the End Point**?", invert both components: $-\\vec{R} = (-\\Delta X, -\\Delta Y)$. (E.g., if End is South-East of Start, Start is strictly **North-West** of End).

### 1.2 Mathematical Map Scale Ratio Reductions
- **Metric Scale Ratio Formula**:
  $$\\text{Actual Ground Distance (km)} = \\frac{\\text{Map Distance (cm)} \\times \\text{Scale Factor (meters/cm)}}{1000}$$
- **Canonical CTET Benchmark Worked Calculations**:
  - *Case 1 ($1\\text{ cm} = 110\\text{ m}$)*: For $15\\text{ cm}$ on map:
    $$15 \\times 110 = 1650\\text{ m} = 1.65\\text{ km}$$
  - *Case 2 ($1\\text{ cm} = 950\\text{ m}$)*: For $16.7\\text{ cm}$ on map:
    $$16.7 \\times 950 = 15865\\text{ m} = 15.865\\text{ km}$$
  - *Case 3 ($1\\text{ cm} = 420\\text{ m}$)*: For $12.5\\text{ cm}$ on map:
    $$12.5 \\times 420 = 5250\\text{ m} = 5.25\\text{ km}$$

### 1.3 Railway Timetable, Duration & Speed Conversions
- **Total Journey Time Across Midnight**:
  $$\\text{Total Duration} = (24:00 - \\text{Departure Day 1}) + (\\text{Intermediate Days} \\times 24\\text{ hrs}) + \\text{Arrival Time Final Day}$$
- **Average Speed Formula**:
  $$\\text{Average Speed (km/h)} = \\frac{\\text{Total Distance (km)}}{\\text{Total Journey Duration (hours)}}$$
- **Unit Conversion Factor**:
  $$\\text{Speed (m/s)} = \\text{Speed (km/h)} \\times \\frac{5}{18}$$

---

## 2. Zero-Hallucination Entity Vault

| Quantitative Concept | Standard Formula / Definition | Canonical Worked Example | Anti-Hallucination Exam Traps |
| :--- | :--- | :--- | :--- |
| **Arabian Sea States**<br>*(अरब सागर के राज्य)* | Gujarat, Maharashtra, Goa, Karnataka, Kerala | 5 Western coastal states | ❌ *Trap*: Odisha and Andhra Pradesh are on Bay of Bengal; Telangana is landlocked. |
| **Bay of Bengal States**<br>*(बंगाल की खाड़ी के राज्य)* | West Bengal, Odisha, Andhra Pradesh, Tamil Nadu | 4 Eastern coastal states | ❌ *Trap*: Kerala and Karnataka are NOT on Bay of Bengal. |
| **Map Scale Formula**<br>*(मानचित्र पैमाना)* | $\\text{km} = \\text{cm} \\times \\text{m/cm} \\div 1000$ | $15\\text{ cm} \\times 110\\text{ m} = 1.65\\text{ km}$ | ❌ *Trap*: Do not forget to divide meters by 1000 to convert to kilometers. |
| **Speed Conversion**<br>*(चाल रूपांतरण)* | $1\\text{ km/h} = \\frac{5}{18}\\text{ m/s}$ | $54\\text{ km/h} \\times \\frac{5}{18} = 15\\text{ m/s}$ | ❌ *Trap*: Multiply by $5/18$ for m/s; multiply by $18/5$ for km/h. |
| **Vector Inversion**<br>*(सापेक्षिक दिशा)* | Direction of Start from End = Opposite of End from Start | Start to End = SE $\\implies$ End to Start = **NW** | ❌ *Trap*: Check whose reference point is requested ("with respect to X"). |

---

## 3. Hyperframes HTML Video Storyboards & Scene Specs

```html
<!-- Hyperframes Scene 7: Indian Coastal Cartography & Speed Engine -->
<div class="hyperframe-scene" data-scene="spatial-engine" style="width: 100%; height: 540px; background: #0f172a; color: #fff; position: relative; font-family: sans-serif;">
  <div class="header-overlay" style="padding: 20px; font-size: 24px; font-weight: bold; color: #38bdf8;">
    🧭 Spatial Positioning & Scale Calculator
  </div>
  <div class="calculator-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin: 40px 20px;">
    <div class="scale-box" style="background: #1e293b; padding: 25px; border-radius: 12px; border: 2px solid #0284c7;">
      <h3 style="color: #38bdf8; margin-top: 0;">Map Scale Algorithm:</h3>
      <p style="font-family: monospace; font-size: 16px; color: #7dd3fc;">Scale: 1 cm = 110 m<br>Map Distance: 15 cm<br>Ground: 15 × 110 = 1650 m<br><strong>Result: 1.65 km</strong></p>
    </div>
    <div class="coastal-box" style="background: #1e293b; padding: 25px; border-radius: 12px; border: 2px solid #059669;">
      <h3 style="color: #34d399; margin-top: 0;">Coastal Alignment:</h3>
      <p style="font-size: 14px; line-height: 1.8;">🌊 <strong>Arabian Sea:</strong> Gujarat, Maharashtra, Goa, Karnataka, Kerala<br>🌅 <strong>Bay of Bengal:</strong> West Bengal, Odisha, Andhra Pradesh, Tamil Nadu</p>
    </div>
  </div>
</div>
```

---

## 4. NotebookLM Audio Overview Steering Cue Cards

```markdown
[NOTEBOOKLM STEERING DIRECTIVE: UNIT 7 QUANTITATIVE BRIDGE]
- Role: Cartography Specialist (Host A) & Quantitative Logic Coach (Host B)
- Focus: Step-by-step calculation breakdown for map scale problems (cm to km) and train average speed across multi-day journeys.
- Debater Cue: Have Host B present a common student error in direction vector inversion (forgetting to reverse the direction when asked from destination); Host A clearly demonstrates the coordinate turnaround.
- Terminology Anchor: Pronounce "Arabian Sea (अरब सागर)", "Bay of Bengal (बंगाल की खाड़ी)", "Average Speed (औसत चाल)".
- Guardrail: Always show intermediate arithmetic steps clearly.
```

---

## 5. Formative Inline PYQ Grounding Bank

### Item 1: CTET July 2024 Paper 1 (Q63)
**Question (Bilingual):**
On a city map, the scale is given as: '1 cm = 110 m'. If the distance between two localities on the map is 15 cm, what is the actual distance between them on the ground?
*(एक शहर के नक्शे पर पैमाना दिया है: '1 सेमी = 110 मीटर'। यदि दो स्थानों के बीच नक्शे पर दूरी 15 सेमी है, तो जमीन पर वास्तविक दूरी क्या है?)*

- Options:
  1. 1.65 km (Correct)
  2. 16.5 km
  3. 1650 km
  4. 1100 m
- **Official Answer**: `Option 1`
- **Grounding Calculation**: $\\text{Actual Distance} = 15 \\times 110 = 1650\\text{ meters} = 1.65\\text{ km}$.

### Item 2: CTET Dec 2018 Paper 1 (Q61)
**Question (Bilingual):**
Which of the following group of states has a coastline on the Arabian Sea?
*(निम्नलिखित में से कौन सा राज्यों का समूह अरब सागर के तट पर स्थित है?)*

- Options:
  1. Andhra Pradesh, Telangana, Odisha
  2. Kerala, Karnataka, Maharashtra (Correct)
  3. Karnataka, Kerala, Gujarat (Also Arabian sea coastal states)
  4. Tamil Nadu, Andhra Pradesh, Karnataka
- **Official Answer**: `Option 2`
- **Grounding Explanation**: Western coastline bordering Arabian Sea comprises Gujarat, Maharashtra, Goa, Karnataka, and Kerala.
"""
    write_unit("unit_7_quantitative_spatial_bridge.md", unit_7)

    print("Sprint 3 Complete: All 7 Master Thematic Spiral Unit Artifacts generated successfully!")

if __name__ == "__main__":
    generate_units()
