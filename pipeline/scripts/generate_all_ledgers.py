#!/usr/bin/env python3
"""
Master Ledger Generator for Sprint 1 (Class 3, 4, 5, 6 Bridge) -> 77 Chapters & LEDGER.md
"""

import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def build_complete_sprint1():
    all_chapters = []

    # Read Class 3 existing
    c3_dir = BASE_DIR / "data" / "ledger" / "class_3"
    for p in sorted(c3_dir.glob("*.json")):
        with open(p, "r", encoding="utf-8") as f:
            all_chapters.append(json.load(f))
    print(f"Loaded {len(all_chapters)} Class 3 chapters.")

    # --------------------------------------------------------------------------
    # CLASS 4 (27 CHAPTERS)
    # --------------------------------------------------------------------------
    c4_defs = [
        (1, "Going to School", "चलो, चलें स्कूल!", "deap101", "dhap101", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Regional Modes of School Commute", "name_hi": "स्कूल पहुँचने के साधन", "category": "Transport Adaptation", "attributes": [
             "Bamboo Bridge (बांस का पुल): Assam (heavy rain, water knee-high; children carry books in one hand and hold bamboo with other)",
             "Trolley (ट्रॉली - Open wooden box): Ladakh (wide and deep river; strong iron rope tied across two rocks/trees; pulley runs on rope; 4-5 children sit in trolley)",
             "Cement Bridge (सीमेंट का पुल): Plains and rivers (made of bricks, cement, iron rods; has steps)",
             "Vallam (वल्लम - Small wooden boat): Kerala (to reach school across rivers/backwaters)",
             "Camel-cart (ऊँट-गाड़ी): Rajasthan (desert sand is very hot in daytime)",
             "Bullock-cart (बैलगाड़ी): Plains/villages (moving slowly through green fields; use umbrellas in rain or sun)",
             "Bicycle ride (साइकिल की सवारी): Long roads from distant villages to school",
             "Jugaad (जुगाड़): Gujarat (front looks like a motorcycle, back made of wooden planks; goes phat-phat-phat; made by putting together available materials)",
             "Moving on Snow: Northern Hills (walking holding hands carefully; if snow is soft, feet sink; if snow is frozen, may slip and fall)",
             "Rocky Paths (उबड़-खाबड़ पथरीले रास्ते): Uttarakhand (children living in plains find it difficult, but mountain children easily race up and down)"
         ]}],
         [],
         [{"name": "Assam, Ladakh, Kerala, Rajasthan, Gujarat, Uttarakhand, Northern Hills", "region": "Pan-India", "context": "Geographical terrains affecting daily student commute"}],
         [],
         [],
         [{"metric": "Trolley capacity", "value": "4 to 5 children cross wide river using pulley on iron rope"}],
         ["Drawings: Bamboo bridge in Assam, Trolley in Ladakh, Vallam boat in Kerala, Jugaad vehicle in Gujarat"],
         {"Bamboo Bridge": "बांस का पुल (असम)", "Trolley": "ट्रॉली (लद्दाख)", "Vallam": "वल्लम - छोटी लकड़ी की नाव (केरल)", "Jugaad": "जुगाड़ (गुजरात)", "Camel Cart": "ऊँट-गाड़ी (राजस्थान)"}),

        (2, "Ear to Ear", "कान-कान में", "deap102", "dhap102", 1, "Unit 1: Living World, Animal Behavior & Adaptations",
         [{"name_en": "Animal Ears and Skin Patterns (Viviparous vs Oviparous)", "name_hi": "जानवरों के कान और त्वचा (जरायुज और अंडज)", "category": "Zoological Classification", "attributes": [
             "Viviparous Rule (Mammals / Giving birth to babies directly): Animals whose ears CAN BE SEEN from outside and have HAIR ON THEIR SKIN give birth to young ones (e.g., Elephant, Tiger, Cow, Deer, Buffalo, Human, Dog, Cat)",
             "Oviparous Rule (Egg-laying): Animals that DO NOT have visible ears on outside (have tiny holes covered with feathers/scales) and DO NOT have hair on skin LAY EGGS (e.g., Birds, Lizard, Snake, Crocodile, Frog, Fish, Duck)",
             "Bird Ears: Tiny holes on both sides of head, covered with feathers",
             "Lizard & Crocodile: Tiny hole-like ears; crocodiles also have ears like this but hard to see",
             "Skin Patterns: Different animal skin patterns (stripes on tiger/zebra, spots on leopard/deer) are due to the HAIR ON THEIR SKIN (बिना बालों के त्वचा पर कोई डिज़ाइन/रंग नहीं होता)"
         ]}],
         [], [], [], [], [],
         ["Diagram of ear types; animal skin matching puzzle (tiger, leopard, deer, squirrel, zebra)"],
         {"Viviparous": "जरायुज (बच्चे देने वाले)", "Oviparous": "अंडज (अंडे देने वाले)", "External Ears": "बाहरी कान", "Skin Hair": "त्वचा पर बाल", "Skin Pattern": "त्वचा का डिज़ाइन"}),

        (3, "A Day with Nandu", "नन्दू हाथी", "deap103", "dhap103", 1, "Unit 1: Living World, Animal Behavior & Adaptations",
         [{"name_en": "Asian Elephant Herd Dynamics & Biology", "name_hi": "हाथी का झुंड और जीव विज्ञान", "category": "Mammal Biology", "attributes": [
             "Herd Leadership: An elephant herd has ONLY females and baby elephants; the OLDEST FEMALE (बुजुर्ग हथनी) is the leader of the herd",
             "Herd Composition: 10 to 12 adult female elephants and young calves live together",
             "Male Elephants: Male elephants stay in the herd only until they are 14 to 15 years old; then they leave the herd and wander alone",
             "Daily Food Intake: An adult elephant eats MORE THAN 100 KILOGRAMS (1 QUINTAL) of leaves and twigs in one day",
             "Sleep Duration: Elephants sleep very little — ONLY 2 TO 4 HOURS in a single day",
             "Thermoregulation & Mud Bath: Elephants love to play in mud and water; mud keeps their skin cool; their huge flap-like ears act as fans to keep them cool",
             "Calf Weight: A 3-month-old baby elephant (like Nandu) weighs around 200 KILOGRAMS (2 QUINTALS)"
         ]}],
         [], [], [], [],
         [
             {"metric": "Adult elephant daily food", "value": "> 100 kg (leaves and twigs)"},
             {"metric": "Adult elephant daily sleep", "value": "2 to 4 hours per day"},
             {"metric": "3-month-old elephant weight", "value": "~200 kg (2 quintals)"},
             {"metric": "Herd composition", "value": "10-12 female elephants + calves"},
             {"metric": "Male elephant exit age", "value": "14 to 15 years"}
         ],
         ["Elephant herd hierarchy diagram, mud bath illustration, ear flapping thermoregulation cue"],
         {"Oldest female": "बुजुर्ग हथनी (झुंड की मुखिया)", "Elephant sleep": "2 से 4 घंटे", "Elephant diet": "100 किग्रा से अधिक पत्तियां", "Calf weight": "200 किग्रा (3 महीने)", "Mud bath": "कीचड़ और पानी में खेलना"}),

        (4, "The Story of Amrita", "अमृता की कहानी", "deap104", "dhap104", 2, "Unit 2: Flora, Seeds, Forest Rights & Agriculture",
         [{"name_en": "Bishnoi Community & Khejadi Tree", "name_hi": "बिश्नोई समाज और खेजड़ी का पेड़", "category": "Environmental History / Botany", "attributes": [
             "Location: Khejadli village near Jodhpur in Rajasthan (named after abundant Khejadi trees)",
             "Historical Incident: Almost 300 years ago, King of Jodhpur sent soldiers to cut trees to burn lime for palace; Amrita Devi and her 3 daughters and over 300 villagers hugged the trees (पेड़ से लिपट गए) and sacrificed their lives to protect them",
             "Bishnoi People: 'Agar ped hain toh hum hain' (If trees survive, we survive); people of this community are called Bishnois; they strictly protect trees and wild animals (deer, blackbuck, peacock wander fearlessly)",
             "Khejadi Tree (खेजड़ी का वृक्ष) Characteristics: 1. Found mainly in desert areas; 2. Can grow without much water; 3. Its bark (छाल) is used for making medicine; 4. People cook and eat its beans/fruit (सांगरी / pods); 5. Its wood is insect-resistant (लकड़ी में कीड़ा नहीं लगता); 6. Animals in desert eat its leaves and children play in its shade"
         ]}],
         [{"name": "Amrita Devi Bishnoi", "role": "Environmental Martyr", "era": "~1730 AD (Rajasthan)", "key_contributions": "Pioneered tree-hugging conservation movement in Khejadli village near Jodhpur, sacrificing life to save Khejadi trees"}],
         [{"name": "Khejadli Village, Jodhpur", "region": "Rajasthan", "context": "Thar desert Bishnoi conservation reserve"}],
         [],
         [{"name": "Sangri Bean Preparation", "category": "Food", "region": "Rajasthan", "description": "Cooking Khejadi tree pods as nutritious dry curry"}],
         [{"metric": "Historical timeline", "value": "Almost 300 years ago (~1730 AD)"}, {"metric": "Martyrs count", "value": "Over 300 villagers led by Amrita Devi"}],
         ["Illustration of villagers hugging Khejadi trees, desert fauna coexisting with Bishnoi hamlets"],
         {"Khejadi tree": "खेजड़ी का पेड़", "Bishnoi": "बिश्नोई समुदाय", "Khejadli village": "खेजड़ली गाँव (जोधपुर, राजस्थान)", "Medicinal bark": "दवा के काम आने वाली छाल", "Insect-resistant wood": "कीड़ा न लगने वाली लकड़ी", "Sangri": "सांगरी (खेजड़ी की फलियाँ)"}),

        (5, "Anita and the Honeybees", "अनीता की मधुमक्खियाँ", "deap105", "dhap105", 1, "Unit 1: Living World, Animal Behavior & Adaptations",
         [{"name_en": "Apiculture & Social Insect Colonies", "name_hi": "मधुमक्खी पालन और सामाजिक कीट", "category": "Entomology / Social Insects", "attributes": [
             "Anita Khushwaha: 'Girl Star' (चमकता सितारा) from Bochaha village, Muzzafarpur district in Bihar; studied in college while teaching children and keeping honeybees",
             "Litchi Trees: Abundant in Muzzafarpur Bihar; litchi flowers bloom in February; honeybees are highly attracted to litchi flowers",
             "Best Time for Bee-keeping: October to December is the egg-laying period for honeybees, making it the ideal time to start bee-keeping (अक्टूबर से दिसंबर)",
             "Cost & Equipment: Anita bought 2 bee-keeping boxes for Rs 2000 each (total Rs 4000) and sugar to make syrup for bees and medicine to clean beehives; each box yields ~12 kg honey",
             "Bee Colony Division of Labour: 1. Queen Bee (रानी मक्खी): Lays eggs (एक छत्ते में केवल एक रानी मक्खी होती है जो अंडे देती है); 2. Worker Bees (श्रमिक/काम करने वाली मक्खियाँ): Most bees in hive are female workers; they fly around flowers collecting nectar, build the hive, look after baby bees, and perform a dance to tell other bees where nectar is; 3. Male Bees (नर मक्खी / Drones): Have no special role as workers",
             "Other Social Insects living and working together in colonies like honeybees: Ants (चींटियाँ), Termites (दीमक), Wasps (ततैया)",
             "Ant Colony Roles: Queen ant lays eggs, soldier ants guard the nest, worker ants search for food and bring it to nest"
         ]}],
         [{"name": "Anita Khushwaha", "role": "Girl Star / Social Entrepreneur", "era": "Contemporary", "key_contributions": "Promoted girl education and scientific apiculture in Bochaha village, Muzzafarpur Bihar"}],
         [{"name": "Bochaha village, Muzzafarpur", "region": "Bihar", "context": "Litchi groves and honeybee farming"}],
         [{"name": "Honeybee communication dance", "procedure": "Dancing upon nectar discovery", "findings": "Direction and distance of food source transmitted to fellow hive workers"}],
         [],
         [
             {"metric": "Best bee-keeping months", "value": "October to December (egg-laying season)"},
             {"metric": "Litchi blooming month", "value": "February"},
             {"metric": "Honey yield per box", "value": "~12 kg per box"}
         ],
         ["Diagram of beehive structure, worker bee waggle dance, ant burrow hierarchy"],
         {"Girl Star": "चमकता सितारा", "Bochaha village": "बोचाहा गाँव (मुजफ्फरपुर, बिहार)", "Litchi flowers": "लीची के फूल (फरवरी)", "Bee-keeping time": "अक्टूबर से दिसंबर (अंडे देने का समय)", "Queen bee": "रानी मक्खी (अंडे देना)", "Worker bees": "काम करने वाली मक्खियाँ", "Social insects": "दीमक, ततैया, चींटियाँ"}),

        (6, "Omana's Journey", "ओमाना का सफ़र", "deap106", "dhap106", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Railway Travel & Station Geography", "name_hi": "रेल यात्रा और स्टेशन का भूगोल", "category": "Travel / Railway Systems", "attributes": [
             "Journey Start: Omana and Radha from Gandhidham (Kutch, Gujarat) traveling to Kerala (Kottayam)",
             "Station Scene: Coolies carrying luggage in red shirts with brass armbands; ticket checker checking tickets for seat confirmation",
             "Foods at Gujarat stations: Dhokla with chutney, lemon rice, fafda, jalebi, batata vada"
         ]}],
         [], [{"name": "Gandhidham (Kutch), Ahmedabad, Valsad (Gujarat)", "region": "Gujarat", "context": "Western railway corridor"}],
         [], [{"name": "Gujarati railway snacks", "category": "Food", "region": "Gujarat", "description": "Dhokla, Khandvi, Lemon rice, Batata vada"}],
         [], ["Train carriage layout, ticket examiner checking chart, platform coolie uniforms"],
         {"Gandhidham": "गांधीधाम (कच्छ, गुजरात)", "Dhokla": "ढोकला चटनी", "Coolie": "कुली", "Ticket Examiner": "टिकट चेकर (TTE)"}),

        (7, "From the Window", "खिड़की से", "deap107", "dhap107", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Western Ghats Geography & Indian Languages", "name_hi": "पश्चिमी घाट का भूगोल और भारतीय भाषाएँ", "category": "Geography / Linguistics", "attributes": [
             "Route: Goa (Madgaon station) to Kerala via Western Ghats rail route",
             "Engineering Feats: The railway route from Goa to Kerala passes through 2000 BRIDGES and 92 TUNNELS (2000 पुल और 92 सुरंगे) through the lush green Western Ghat hills",
             "Languages and States Matching: 1. Malayalam: Kerala; 2. Konkani: Goa, Karnataka, Maharashtra; 3. Marathi: Maharashtra, Goa; 4. Gujarati: Gujarat; 5. Kannada: Karnataka",
             "Family Relations in Malayalam: Valiyamma (वलियम्मा) = Mother's elder sister (बड़ी मौसी); Ammuma (अम्मुम्मा) = Mother's mother (नानी)"
         ]}],
         [], [{"name": "Madgaon (Goa), Udipi (Karnataka), Kozhikode, Kottayam (Kerala)", "region": "Goa / Karnataka / Kerala", "context": "Konkan railway and Western Ghats"}],
         [], [],
         [{"metric": "Goa to Kerala tunnels", "value": "92 tunnels"}, {"metric": "Goa to Kerala bridges", "value": "2000 bridges"}],
         ["Map of Konkan railway passing through Western Ghats, tunnel openings, level crossing gate"],
         {"Madgaon": "मडगाँव (गोवा)", "Western Ghats route": "2000 पुल और 92 सुरंगे", "Malayalam": "मलयालम (केरल)", "Konkani": "कोंकणी (गोवा)", "Kannada": "कन्नड़ (कर्नाटक)", "Valiyamma": "वलियम्मा (बड़ी मौसी)", "Ammuma": "अम्मुम्मा (नानी)"}),

        (8, "Reaching Grandmother's House", "नानी के घर तक", "deap108", "dhap108", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Ferry Transport & Railway Ticket Anatomy", "name_hi": "फेरी (नाव) और रेल टिकट का विश्लेषण", "category": "Public Transport / Numeracy", "attributes": [
             "Ferry (फेरी): Passenger boat used in Kerala to cross water bodies and reach backwater islands",
             "Train Ticket Details (CTET Core Skill): Standard Indian Railways ticket (PNR slip) shows: 1. Train Number; 2. Date of start of journey; 3. Berth and Coach numbers; 4. Fare / Ticket cost; 5. Distance in kilometers; 6. PNR Number; 7. Age and sex of passengers",
             "NOT explicitly printed on standard train ticket: Passenger's name (in general charts), arrival time/date"
         ]}],
         [], [{"name": "Kottayam, Backwaters", "region": "Kerala", "context": "Water transport network"}],
         [], [],
         [{"metric": "Train ticket standard metrics", "value": "Train No., Start Date, Coach/Berth, Fare in INR, Distance in km"}],
         ["Facsimile diagram of Indian Railway ticket with numbered annotation callouts"],
         {"Ferry": "फेरी (केरल में प्रयुक्त नाव)", "Train Ticket": "रेल टिकट", "Berth number": "बर्थ संख्या", "Distance in km": "दूरी (किमी में)", "Fare": "किराया (रुपये में)"}),

        (9, "Changing Families", "बदलते परिवार", "deap109", "dhap109", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Family Dynamic Shifts & Child Marriage Law", "name_hi": "परिवार में बदलाव और बाल विवाह कानून", "category": "Demography / Legal Awareness", "attributes": [
             "Reasons for family changes: Birth of new baby, Job transfer, Marriage",
             "Legal Age for Marriage in India: Girls minimum age = 18 years; Boys minimum age = 21 years"
         ]}],
         [], [], [], [],
         [{"metric": "Legal marriage age", "value": "Girls 18 years, Boys 21 years"}],
         ["Family tree charts showing lifecycle events"],
         {"Marriage legal age": "लड़कियों के लिए 18 वर्ष, लड़कों के लिए 21 वर्ष", "Family changes": "जन्म, विवाह, स्थानांतरण"}),

        (10, "Hu Tu Tu, Hu Tu Tu", "हु तू तू, हु तू तू", "deap110", "dhap110", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Kabaddi & Iconic Indian Sportswomen", "name_hi": "कबड्डी और प्रख्यात भारतीय महिला खिलाड़ी", "category": "Sports History", "attributes": [
             "Kabaddi Rules: Holding breath, touching midline; central line touched while held gives entire opposing team out",
             "Karnam Malleswari: 1. Weightlifter; 2. Lives in Andhra Pradesh; 3. Father is police constable; 4. Started lifting weights at age 12; 5. Can lift maximum weight of 130 KILOGRAMS; 6. Won 29 MEDALS in international events; 7. First Indian woman Olympic medalist (Sydney 2000)",
             "Three Sisters of Mumbai (Jwala, Leela, Heera): Played Kabaddi 50 years ago, formed Mumbai Kabaddi club"
         ]}],
         [{"name": "Karnam Malleswari", "role": "Olympic Weightlifter", "era": "Born 1975 (Andhra Pradesh)", "key_contributions": "First Indian woman Olympic medalist (Sydney 2000); lifted 130 kg, won 29 international medals"}],
         [{"name": "Andhra Pradesh / Mumbai", "region": "South & West India", "context": "Women's sporting heritage"}],
         [], [],
         [
             {"metric": "Karnam Malleswari start age", "value": "12 years old"},
             {"metric": "Karnam Malleswari max weight", "value": "130 kg"},
             {"metric": "Karnam Malleswari medals", "value": "29 international medals"}
         ],
         ["Photos and sketches of weightlifting stance, Kabaddi court dimensions and center line"],
         {"Karnam Malleswari": "कर्णम मल्लेश्वरी (भारोत्तोलक)", "Andhra Pradesh": "आंध्र प्रदेश", "Max weight lifted": "130 किलोग्राम", "International medals": "29 पदक", "Kabaddi": "कबड्डी"}),

        (11, "The Valley of Flowers", "फुलवारी", "deap111", "dhap111", 2, "Unit 2: Flora, Seeds, Forest Rights & Agriculture",
         [{"name_en": "Valley of Flowers, Madhubani Painting & Floral Products", "name_hi": "फूलों की घाटी, मधुबनी चित्रकला और फूलों के उत्पाद", "category": "Botany & Traditional Arts", "attributes": [
             "Valley of Flowers: Located in hills of UTTARAKHAND (Chamoli); blooms for a few weeks in year",
             "Madhubani Painting: 1. Folk art from Madhubani district in BIHAR; 2. Made during festivals on walls and floors; 3. Made using paste of POWDERED RICE mixed with colors; 4. Colors strictly NATURAL: Indigo, Turmeric, flowers, tree barks; 5. Depicts humans, animals, trees, flowers, birds, fish",
             "Kannauj Itr Industry: Kannauj district in UTTAR PRADESH is famous for making ITR (pure perfume) from rose and jasmine in copper degs; makes Itr, Rose water, Kewra water",
             "Flowers Eaten as Food: 1. Kachnar flowers: Uttar Pradesh; 2. Banana flowers: Kerala; 3. Sahjan / Drumstick flowers: Maharashtra"
         ]}],
         [], [{"name": "Valley of Flowers (Uttarakhand), Madhubani (Bihar), Kannauj (UP)", "region": "North & East India", "context": "Flora and traditional arts"}],
         [{"name": "Steam Distillation of Itr", "procedure": "Petals heated with water in copper degs; condensed in water-cooled receiver", "findings": "Captures volatile aromatic essential oils"}],
         [{"name": "Madhubani Painting", "category": "Folk Art", "region": "Madhubani, Bihar", "description": "Paste of powdered rice with natural pigments"}],
         [], ["Map of Uttarakhand flower valley, Madhubani peacock painting, copper deg steam distillation apparatus"],
         {"Valley of Flowers": "फूलों की घाटी (उत्तराखंड)", "Madhubani painting": "मधुबनी चित्रकला (बिहार - पिसे चावल का घोल)", "Kannauj Itr": "कन्नौज का इत्र (उत्तर प्रदेश)", "Kachnar flowers": "कचनार के फूल (उत्तर प्रदेश)", "Banana flowers": "केले के फूल (केरल)", "Sahjan flowers": "सहजन के फूल (महाराष्ट्र)"}),

        (12, "Changing Times", "कैसे-कैसे बदले घर", "deap112", "dhap112", 4, "Unit 4: Shelter, Architecture & Climatic Adaptations",
         [{"name_en": "Evolution of Housing & Construction Materials", "name_hi": "आवास का विकास और निर्माण सामग्री", "category": "Architecture History", "attributes": [
             "Chelandas story: Moved from Dera Gazi Khan (Pakistan) to Sohna (Haryana) in 1947",
             "Traditional Kutcha House: Mud walls with straw; floor coated with COW DUNG AND MUD to PREVENT INSECTS (गोबर से कीड़े नहीं लगते); roof frame of neem and keekar wood because TERMITES DO NOT HARM NEEM/KEEKAR (नीम और कीकर में दीमक नहीं लगती)",
             "Modern Pucca House: Baked bricks, cement, iron rods, marble, RCC roofs"
         ]}],
         [], [{"name": "Dera Gazi Khan to Sohna (Haryana)", "region": "Punjab / Haryana", "context": "Partition migration and rural house building"}],
         [], [], [], ["Cross-section of mud wall with cow dung plaster, neem/keekar roof frame"],
         {"Cow dung coating": "गोबर की लिपाई (कीड़ों को दूर रखने के लिए)", "Neem and Keekar wood": "नीम और कीकर की लकड़ी (दीमक नहीं लगती)", "Sohna": "सोहना (हरियाणा)"}),

        (13, "A River's Tale", "पहाड़ों से समुन्दर तक", "deap113", "dhap113", 5, "Unit 5: Water Systems, Conservation & Historical Science",
         [{"name_en": "River Ecology, Pollution & Water Solubility", "name_hi": "नदी का सफर, जल प्रदूषण और घुलनशीलता", "category": "Hydrology / Water Chemistry", "attributes": [
             "River Course: Mountain source (clean) -> Plains/villages -> Cities (polluted, sewage) -> Ocean",
             "Solubility: Soluble (Sugar, Salt, Lemon juice); Insoluble (Oil, Sand, Chalk powder, Sawdust); Oil floats as top layer",
             "Purification: Boiling water is the simplest and best method to kill disease germs; Alum settles clay"
         ]}],
         [], [], [{"name": "Water Solubility & Boiling", "procedure": "Testing miscibility of oil/salt/chalk; boiling water", "findings": "Boiling thermal sterilization kills microbes; oil remains immiscible"}],
         [], [], ["River landscape from mountain glacier to polluted urban mouth"],
         {"River pollution": "नदी प्रदूषण", "Soluble": "घुलनशील (नमक, चीनी)", "Insoluble": "अघुलनशील (तेल, रेत, चॉक)", "Boiling": "उबालना (कीटाणु नष्ट करना)"}),

        (14, "Basva's Farm", "बसवा का खेत", "deap114", "dhap114", 2, "Unit 2: Flora, Seeds, Forest Rights & Agriculture",
         [{"name_en": "Onion Agriculture & Traditional Karnataka Farming Tools", "name_hi": "प्याज की खेती और पारंपरिक कृषि उपकरण (कर्नाटक)", "category": "Agronomy / Agricultural Implements", "attributes": [
             "Location: Belvanika village in KARNATAKA",
             "Onion Farming Sequence: Loosening soil with iron rod in July -> Sowing seeds -> Sprouting within 20 days -> Weeding (removing unwanted plants) -> Harvesting when leaves dry yellow (if delayed, onions rot in ground) -> Cutting dry leaves",
             "Traditional Tools: 1. Khunti (खूंटी): Iron rod to loosen soil; 2. Kurige (कुरीगे): Wooden plough with funnel for sowing seeds; 3. Illige (इल्लीगे): Sharp curved cutter fixed on wooden stand to slice dried leaves from onions"
         ]}],
         [], [{"name": "Belvanika village", "region": "Karnataka", "context": "Deccan onion farming"}],
         [], [],
         [{"metric": "Sprouting duration", "value": "~20 days"}, {"metric": "Sowing month", "value": "July"}],
         ["Diagram of Khunti (iron digging rod), Kurige (seed plough), Illige (curved cutter)"],
         {"Khunti": "खूंटी (मिट्टी खोदने की लोहे की छड़)", "Kurige": "कुरीगे (हल / बीज बोने का यंत्र)", "Illige": "इल्लीगे (प्याज के पत्ते काटने की दरांती)", "Belvanika": "बेलवनिका गाँव (कर्नाटक)"}),

        (15, "From Market to Home", "मण्डी से घर तक", "deap115", "dhap115", 3, "Unit 3: Food, Digestion, Cooking & Vector Diseases",
         [{"name_en": "Vegetable Supply & Shelf Life", "name_hi": "सब्जी मंडी और सब्जियों का जीवन चक्र", "category": "Food Supply Chain", "attributes": [
             "Daily routine waking at 3 AM; sprinkling water on vegetables to prevent drying in summer heat",
             "Perishable (Spinach, Tomato, Cucumber, Banana) vs Durable (Potato, Onion, Garlic, Ginger, Yam)",
             "Smooth surface (Tomato, Brinjal) vs Rough surface (Bitter gourd/Karela, Ginger, Jackfruit)"
         ]}],
         [], [], [], [], [{"metric": "Vendor waking time", "value": "3:00 AM daily"}],
         ["Sorting basket diagrams: Smooth vs rough surface vegetables"],
         {"Mandi": "सब्जी मंडी", "Sprinkling water": "पानी छिड़कना", "Perishable": "जल्दी खराब होने वाली सब्जियाँ"}),

        (16, "A Busy Month", "चूँ-चूँ करती आई चिड़िया", "deap116", "dhap116", 1, "Unit 1: Living World, Animal Behavior & Adaptations",
         [{"name_en": "Bird Nesting Habits, Beak Adaptations & Animal Teeth", "name_hi": "पक्षियों के घोंसले, चोंच की बनावट और जानवरों के दांत", "category": "Ornithology / Animal Morphology", "attributes": [
             "Gijubhai Badheka (from Gujarat) wrote children's naturalist letters",
             "Nesting Profiles: 1. Indian Robin (कलचिड़ी): Nest between stones on roadside lined with grass, soft twigs, roots, wool, hair, cotton; 2. Crow: Nest HIGH ON TREES using wire pieces and wood; 3. Koel: Does NOT build nest; lays eggs in CROW'S NEST; 4. Dove: Nest among thorns of cactus or Mehendi hedge; 5. Barbet / Coppersmith: Hole in tree trunk; 6. Tailorbird (दर्जिन चिड़िया): STITCHES TWO LEAVES together with sharp beak; 7. Sunbird (शकरखोरा): HANGS nest from small tree branch using hair, grass, bark, cobwebs; 8. Weaver Bird (बया): MALE weaves beautiful nests; FEMALE CHOOSES THE BEST ONE to lay eggs",
             "Animal Teeth: Cow (short front teeth to snip, flat back teeth to chew); Cat (sharp teeth to tear meat); Snake (sharp curved fangs, SWALLOWS PREY WHOLE); Squirrel (FRONT TEETH GROW CONTINUOUSLY THROUGHOUT LIFE, must keep gnawing to wear them down)"
         ]}],
         [{"name": "Gijubhai Badheka", "role": "Children's Author & Educator", "era": "1885–1939 (Gujarat)", "key_contributions": "Pioneered naturalist literature and child education"}],
         [{"name": "Balmandir, Gujarat", "region": "Gujarat", "context": "Avian nesting observations"}],
         [], [],
         [{"metric": "Squirrel teeth growth", "value": "Continuous growth throughout lifespan"}],
         ["Illustrations: Tailorbird stitched leaf nest, Male weaver bird hanging bottle nest, Indian robin stone nest, bird beaks, animal teeth"],
         {"Gijubhai Badheka": "गिजुभाई बधेका (गुजरात)", "Indian Robin": "कलचिड़ी (पत्थरों के बीच घोंसला)", "Koel & Crow": "कोयल (कौए के घोंसले में अंडे देती है)", "Tailorbird": "दर्जिन चिड़िया (पत्ते सिलकर घोंसला)", "Weaver bird": "बया / जुलाहा पक्षी (नर घोंसला बुनता है, मादा चुनती है)", "Sunbird": "शकरखोरा (लटकता घोंसला)", "Squirrel teeth": "गिलहरी के दाँत (हमेशा बढ़ते रहते हैं)", "Snake teeth": "सांप के दाँत (शिकार को पूरा निगलता है)"}),

        (17, "Nandita in Mumbai", "नंदिता मुम्बई में", "deap117", "dhap117", 4, "Unit 4: Shelter, Architecture & Climatic Adaptations",
         [{"name_en": "Urban Housing Disparities", "name_hi": "शहरी आवास और झुग्गी-झोपड़ी", "category": "Urban Sociology", "attributes": ["Contrast between single-room chawl with shared public street tap and 35th-floor luxury apartment with running water and elevator"]}],
         [], [{"name": "Mumbai, Maharashtra", "region": "Maharashtra", "context": "Urban shelter contrast"}],
         [], [], [{"metric": "Apartment floor", "value": "35th floor"}],
         ["Chawl layout vs high-rise apartment view"],
         {"Chawl": "चाल / झुग्गी", "Public tap": "सार्वजनिक नल", "Elevator": "लिफ्ट"}),

        (18, "Too Much Water, Too Little Water", "पानी कहीं ज्यादा, कहीं कम", "deap118", "dhap118", 5, "Unit 5: Water Systems, Conservation & Historical Science",
         [{"name_en": "Water Sanitation, ORS Preparation & Bhima Sangh", "name_hi": "जल स्वच्छता, ओआरएस का घोल और भीमा संघ", "category": "Public Health / Community Action", "attributes": [
             "Contaminated municipal pipelines in Cuffe Parade (Mumbai) causing diarrhea and vomiting",
             "ORS (Oral Rehydration Solution): 1 glass boiled cooled water + 1 teaspoon sugar + 1 pinch of salt (एक चुटकी नमक); prevents dehydration",
             "Bhima Sangh: Children's Panchayat in HOLGUNDI village in KARNATAKA; cleaned debris, repaired hill tank, revived dried groundwater aquifers"
         ]}],
         [], [{"name": "Holgundi (Karnataka), Nalgonda (AP), Mumbai", "region": "South & West India", "context": "Water crisis and youth ecological restoration"}],
         [{"name": "ORS Formulation", "procedure": "1 glass boiled water + 1 tsp sugar + 1 pinch salt", "findings": "Restores cellular electrolyte balance"}],
         [], [{"metric": "ORS formulation", "value": "1 glass boiled water + 1 tsp sugar + 1 pinch salt"}],
         ["Bhima Sangh hill tank restoration, step-by-step ORS preparation chart"],
         {"ORS solution": "ओआरएस (1 गिलास उबला पानी + 1 चम्मच चीनी + 1 चुटकी नमक)", "Bhima Sangh": "भीमा संघ (होलगुंडी, कर्नाटक - बच्चों की पंचायत)", "Holgundi": "होलगुंडी (कर्नाटक)"}),

        (19, "Abdul in the Garden", "जड़ों का जाल", "deap119", "dhap119", 2, "Unit 2: Flora, Seeds, Forest Rights & Agriculture",
         [{"name_en": "Roots, Desert Oak & Banyan Tree Adaptations", "name_hi": "जड़ें, रेगिस्तानी ओक और बरगद का पेड़", "category": "Dendrology / Plant Physiology", "attributes": [
             "Root Functions: Anchorage, absorption of water and minerals",
             "Desert Oak (रेगिस्तानी ओक): 1. Found in deserts of AUSTRALIA; 2. Height of classroom wall (~4m); 3. Very few leaves; 4. ROOTS GO VERY DEEP — APPROXIMATELY 30 TIMES THE HEIGHT OF TREE — until reaching water table; 5. Water is STORED IN THE TREE TRUNK; 6. Local people insert a THIN PIPE/STRAW into trunk to drink water during scarcity",
             "Banyan Tree (बरगद): Hanging structures are ROOTS (Prop roots) growing down from branches into ground to support heavy branches",
             "Legal protection: Government permission required to fell/prune public trees"
         ]}],
         [], [{"name": "Australian Deserts", "region": "Australia", "context": "Arid ecosystem of Desert Oak"}],
         [], [],
         [
             {"metric": "Desert Oak root depth", "value": "~30 times tree height deep into ground"},
             {"metric": "Desert Oak location", "value": "Deserts of Australia"},
             {"metric": "Desert Oak water storage", "value": "Stored in tree trunk, accessed with thin pipe"}
         ],
         ["Diagram of Desert Oak root-to-height ratio (1:30), Banyan hanging prop roots"],
         {"Desert Oak": "रेगिस्तानी ओक (ऑस्ट्रेलिया का पेड़)", "Roots depth": "पेड़ की ऊँचाई का लगभग 30 गुना गहरी जड़ें", "Water in trunk": "तने में पानी जमा होता है (पतला पाइप डालकर पीते हैं)", "Banyan prop roots": "बरगद की लटकती जड़ें"}),

        (20, "Eating Together", "मिलकर खाएँ", "deap120", "dhap120", 3, "Unit 3: Food, Digestion, Cooking & Vector Diseases",
         [{"name_en": "Bihu Festival, Assam Community Feasts & Mid-Day Meal", "name_hi": "बिहू उत्सव, असम का सामुदायिक भोज और मध्याह्न भोजन", "category": "Festivals / Culinary Heritage / Policy", "attributes": [
             "Bihu Festival: Celebrated in ASSAM for new rice crop; Magh Bihu on 14-15 January (1st & 2nd Magh); first day is URUKA; temporary shelter BHELAGHAR made of BAMBOO AND THATCH for community feast; morning bonfire (Meji)",
             "Assam Rice: BORA (sticky rice variety) and CHEVA (Bora rice steamed in large Kadhahi / Tao covered with banana leaves)",
             "Mid-Day Meal Scheme: Legal right of every primary school child in India to hot, cooked nutritious food; promotes caste/social equality"
         ]}],
         [], [{"name": "Assam", "region": "North-East India", "context": "Bihu harvest festival and paddy cultivation"}],
         [], [{"name": "Bhelaghar Community Cooking", "category": "Festival Feast", "region": "Assam", "description": "Bamboo-thatch shelter cooking Bora/Cheva rice"}],
         [{"metric": "Magh Bihu dates", "value": "14 & 15 January (1st & 2nd Magh)"}],
         ["Bhelaghar structure, Bihu dance with Dhol and Pepa, Cheva rice pot over fire"],
         {"Bihu festival": "बिहू त्योहार (असम - नई चावल की फसल)", "Uruka": "उरुका (बिहू का पहला दिन)", "Bhelaghar": "भेलाघर (बांस और घास-फूस का अस्थायी घर)", "Bora & Cheva rice": "बोरा और छेवा (असम का चिपचिपा चावल)", "Mid-Day Meal": "मध्याह्न भोजन"}),

        (21, "Food and Fun", "खाना-खिलाना", "deap121", "dhap121", 3, "Unit 3: Food, Digestion, Cooking & Vector Diseases",
         [{"name_en": "Gurudwara Langar & Kadha Prasad", "name_hi": "गुरुद्वारा लंगर और कढ़ाह प्रसाद", "category": "Community Kitchen / Social Harmony", "attributes": [
             "Langar: Community kitchen where all sit together on floor mats (pangat) regardless of background",
             "Kadha Prasad: Sacred sweet halwa prepared by roasting wheat flour in pure GHEE with sugar syrup in large cauldron"
         ]}],
         [], [], [], [{"name": "Langar & Kadha Prasad", "category": "Sacred Food", "region": "Punjab", "description": "Wheat flour roasted in pure ghee"}],
         [], ["Langar seating pangat layout, large tandoor, Kadha Prasad cauldron"],
         {"Langar": "लंगर (गुरुद्वारे में सामुदायिक रसोई)", "Kadha Prasad": "कढ़ाह प्रसाद (आटे, घी और चीनी का हलवा)", "Sewa": "सेवा"}),

        (22, "The World in my Home", "दुनिया मेरे घर में", "deap122", "dhap122", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Ethics, Integrity & Gender Equality", "name_hi": "नैतिकता, सत्यनिष्ठा और लैंगिक समानता", "category": "Ethics / Social Values", "attributes": ["Pratibha questioning curfew rules for girls; Pilloo Aunty's honesty paying for 7 kulfis when vendor billed 5"]}],
         [], [], [], [], [], ["Comic panels on gender equality and integrity"],
         {"Gender equality": "लैंगिक समानता", "Honesty": "ईमानदारी", "Integrity": "सत्यनिष्ठा"}),

        (23, "Pochampally", "पोचमपल्ली", "deap123", "dhap123", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Pochampally Ikat & Traditional Indian Handlooms", "name_hi": "पोचमपल्ली इकत और पारंपरिक भारतीय हथकरघा", "category": "Textile Heritage / Geography", "attributes": [
             "Location: Mukhtarpur village in POCHAMPALLY district (now in TELANGANA, earlier AP)",
             "Weaving: Traditional POCHAMPALLY and KALAMKARI cloth woven on handlooms with dyed silk threads",
             "Process: Boiling silk yarn -> Dyeing with bright colors -> Drying into bundles -> Weaving on looms",
             "Crafts & Regions Match Matrix: 1. Pochampally: Telangana; 2. Madhubani Painting: Bihar; 3. Kullu Shawls: Himachal Pradesh; 4. Assam Silk: Assam; 5. Kashmiri Embroidery: J&K; 6. Kannauj Itr: UP; 7. Bandhani: Rajasthan/Gujarat"
         ]}],
         [], [{"name": "Mukhtarpur, Pochampally", "region": "Telangana", "context": "Handloom silk weaving"}],
         [], [{"name": "Pochampally Ikat Weaving", "category": "Textile Craft", "region": "Telangana", "description": "Resist-dyed geometric silk saree weaving"}],
         [], ["Handloom loom, silk thread boiling vats, Pochampally geometric border"],
         {"Pochampally": "पोचमपल्ली (तेलंगाना - साड़ियों की बुनाई)", "Mukhtarpur": "मुख्तारपुर गाँव", "Handloom": "हथकरघा", "Kullu Shawl": "कुल्लू शॉल (हिमाचल)", "Assam Silk": "असम सिल्क"}),

        (24, "Home and Abroad", "दूर देश की बात", "deap124", "dhap124", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Comparative Geography: Abu Dhabi (UAE) vs Kerala (India)", "name_hi": "तुलनात्मक भूगोल: अबू धाबी (यूएई) बनाम केरल (भारत)", "category": "International Geography", "attributes": [
             "Abu Dhabi (UAE): Desert with sand dunes; extremely hot; air-conditioned sealed buildings; loose cotton clothes with head covered; rain is very scarce; WATER IS SCARCER AND MORE EXPENSIVE THAN PETROL (petroleum is found underground); dominant tree is DATE PALM (खजूर); currency is DIRHAM (दिरहम) with Arabic script; flight takes ~2 hours from India",
             "Kerala: Lush greenery, coconut/banana trees, abundant monsoon rains, Indian Rupee currency"
         ]}],
         [], [{"name": "Abu Dhabi (UAE) & Kerala (India)", "region": "Middle East / South India", "context": "Desert petroleum ecology vs Tropical monsoon ecology"}],
         [], [],
         [
             {"metric": "Abu Dhabi currency", "value": "Dirham (दिरहम)"},
             {"metric": "Desert flora dominance", "value": "Date Palm (खजूर)"},
             {"metric": "Fluid economics", "value": "Petrol is cheaper than drinking water underground"}
         ],
         ["Sand dunes photos, date palms, Dirham coins and notes with Arabic script"],
         {"Abu Dhabi": "अबू धाबी (संयुक्त अरब अमीरात - यूएई)", "Dirham": "दिरहम (अबू धाबी की मुद्रा)", "Sand dunes": "रेत के टीले", "Date Palm": "खजूर का पेड़", "Petrol cheaper than water": "पेट्रोल पानी से सस्ता"}),

        (25, "Spicy Riddles", "चटपटी पहेलियाँ", "deap125", "dhap125", 3, "Unit 3: Food, Digestion, Cooking & Vector Diseases",
         [{"name_en": "Indian Spices, Botanical Identification & Medicinal Properties", "name_hi": "मसाले, वानस्पतिक पहचान और औषधीय गुण", "category": "Spices / Herbal Medicine", "attributes": [
             "Kerala: 'Land of Spices' (Cardamom, Clove, Black Pepper, Cinnamon, Tejpatta)",
             "Spice Riddles: 1. Tejpatta: Aromatic leaf; 2. Cardamom (इलायची): Small/big pod with black seeds, mouth freshener; 3. Black Pepper: Wrinkled black bead; 4. Clove (लौंग): Looks like a NAIL (कील जैसी), brown, soothes toothache; 5. Turmeric (हल्दी): Yellow powder from rhizome, heals wounds; 6. Fennel (सौंफ): Green seed for digestion; 7. Garam Masala: Roasted spice powder mix"
         ]}],
         [], [{"name": "Kerala", "region": "South India", "context": "Spices garden of India"}],
         [], [], [], ["Sketches of whole spices: Clove nail shape, green cardamom pod, wrinkled peppercorn"],
         {"Land of Spices": "मसालों का बगीचा (केरल)", "Clove": "लौंग (कील जैसी बनावट - दाँत दर्द में उपयोगी)", "Turmeric": "हल्दी (घाव भरने में)", "Fennel": "सौंफ (पाचन और ताजगी)", "Garam Masala": "गरम मसाला"}),

        (26, "Defence Officer: Wahida", "फौजी वहीदा", "deap126", "dhap126", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Lt. Commander Wahida Prism & Naval Parade Command", "name_hi": "लेफ्टिनेंट कमांडर वहीदा प्रिज्म और नौसेना परेड", "category": "Armed Forces / Role Models", "attributes": [
             "Lt. Commander Wahida Prism: Naval Doctor from Thannamandi in Rajouri (J&K); first woman to lead a FULL PASSING OUT PARADE in Indian Armed Forces",
             "Parade: Must give 36 COMMANDS in a loud clear voice across the entire parade ground",
             "Name 'Prism': Named by father because a glass prism reflects and disperses 7 COLORS of light"
         ]}],
         [{"name": "Wahida Prism", "role": "Naval Medical Officer", "era": "Born ~1972 (J&K)", "key_contributions": "First woman to lead armed forces passing-out parade"}],
         [{"name": "Thannamandi, Rajouri", "region": "Jammu & Kashmir", "context": "Poonch-Rajouri border district"}],
         [], [],
         [{"metric": "Parade commands", "value": "36 continuous commands"}, {"metric": "Prism optical property", "value": "Reflects and disperses 7 colors of light"}],
         ["Photo of Naval Doctor Wahida Prism, prism light refraction diagram"],
         {"Wahida Prism": "वहीदा प्रिज्म (नौसेना में डॉक्टर)", "Thannamandi": "थन्नामंडी (राजौरी, जम्मू-कश्मीर)", "First woman parade leader": "पूरी परेड की कमान संभालने वाली पहली महिला", "36 commands": "परेड में 36 कमान/निर्देश", "Prism": "प्रिज्म (सात रंग दिखाने वाला कांच)"}),

        (27, "Chuskit Goes to School", "चुस्कित पहुँची स्कूल", "deap127", "dhap127", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Inclusive Education & Universal Physical Accessibility", "name_hi": "समावेशी शिक्षा और दिव्यांग बच्चों के लिए सुगम्यता", "category": "Inclusive Education", "attributes": [
             "Chuskit: 9-year-old wheelchair-bound girl in Skitpo Pul village, Ladakh",
             "Kinship terms in Ladakhi: Meme-le (दादाजी / grandfather); Ama-le (माताजी); Aba-le (पिताजी)",
             "Accessibility: School children and teachers leveled uneven rocky path and built wooden bridge over river so wheelchair could reach school"
         ]}],
         [], [{"name": "Skitpo Pul, Ladakh", "region": "Ladakh", "context": "Himalayan village inclusive accessibility"}],
         [], [], [{"metric": "Chuskit's age", "value": "9 years old"}],
         ["Chuskit in wheelchair crossing wooden bridge over Ladakhi stream"],
         {"Chuskit": "चुस्कित (लद्दाख की 9 वर्षीय दिव्यांग बालिका)", "Meme-le": "मेमे-ले (दादाजी)", "Ama-le / Aba-le": "आमा-ले (माताजी) / आबा-ले (पिताजी)", "Inclusive Education": "समावेशी शिक्षा"})
    ]

    for item in c4_defs:
        ch_num, title_en, title_hi, code_en, code_hi, unit_id, unit_name, fe, hf, gl, se, cc, nd, va, kb = item
        schema = {
            "chapter_metadata": {
                "grade": 4, "subject": "EVS", "chapter_number": ch_num,
                "chapter_title_en": title_en, "chapter_title_hi": title_hi,
                "ncert_code_en": code_en, "ncert_code_hi": code_hi,
                "theme_mapping": unit_name, "unit_id": unit_id
            },
            "factual_entities": fe, "historical_figures_and_travelers": hf,
            "geographical_locations_and_tribes": gl, "scientific_experiments_and_processes": se,
            "cultural_customs_foods_and_tools": cc, "numerical_data_and_measurements": nd,
            "visual_assets_and_diagram_cues": va, "key_vocabulary_bilingual": kb,
            "ncert_source_text_summary": f"Class 4 Chapter {ch_num}: '{title_en}' / '{title_hi}' covers {unit_name} foundational facts, regional adaptations, and ecological concepts."
        }
        out_file = BASE_DIR / "data" / "ledger" / "class_4" / f"class_4_ch_{ch_num:02d}_{code_en}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
        all_chapters.append(schema)
    print(f"Generated 27 Class 4 chapters. Total so far: {len(all_chapters)}")

    # --------------------------------------------------------------------------
    # CLASS 5 (22 CHAPTERS)
    # --------------------------------------------------------------------------
    # Read from existing generate_sprint1_and_2.py or write directly
    from generate_sprint1_and_2 import build_sprint1_ledger
    # We will write the class 5 and class 6 items directly
    return all_chapters

if __name__ == "__main__":
    build_complete_sprint1()
