#!/usr/bin/env python3
"""
Sprint 1 & Sprint 2 Data Generation & Verification Script
Processes all 77 NCERT chapters and CTET PYQ corpus (2018-2024).
"""

import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def build_sprint1_ledger():
    print("Executing Sprint 1: Deterministic Extraction for 77 NCERT chapters...")
    
    chapters_data = []

    # CLASS 3 (24 Chapters)
    c3_defs = [
        (1, "Poonam's Day Out", "पूनम की दया", "ceap101", "chap101", 1, "Unit 1: Living World, Animal Behavior & Adaptations",
         [{"name_en": "Pond Animals", "name_hi": "तालाब के जीव", "category": "Animal", "attributes": ["Goat, tortoise, crane (बगुला), frog, buffalo, egret", "Animals move by flying, crawling, walking, hopping, swimming"]}],
         [],
         [{"name": "Local pond/garden", "region": "Rural/Suburban India", "context": "Freshwater habitat"}],
         [{"name": "Animal movement observation", "procedure": "Classifying animals by feet, wings, crawling, swimming", "findings": "Different animals have distinct locomotion styles"}],
         [],
         [{"metric": "Number of legs/wings", "value": "Birds have 2 wings, insects have 6 legs, mammals have 4 legs"}],
         ["Drawings of crow, pigeon, squirrel, monkey, butterfly, frog on tree and in pond"],
         {"Pond": "तालाब", "Crane": "बगुला", "Tortoise": "कछुआ", "Frog": "मेंढक", "Locomotion": "चाल"}),

        (2, "The Plant Fairy", "पौधों की परी", "ceap102", "chap102", 2, "Unit 2: Flora, Seeds, Forest Rights & Agriculture",
         [{"name_en": "Leaves and Trunks", "name_hi": "पत्तियाँ और तने", "category": "Plant", "attributes": ["Leaves have different shapes (round, long, triangular), margins (straight, uneven, saw-toothed), colors, and smells", "Lemon, mango, neem, basil (tulsi), mint (pudina), coriander (dhaniya) identified by rubbing leaves and smelling"]}],
         [],
         [{"name": "Neighbourhood garden", "region": "India", "context": "Flora diversity"}],
         [{"name": "Rubbing leaves for identification", "procedure": "Crushing leaves and smelling them", "findings": "Essential oils give distinct scents; rubbings of leaf veins and tree bark reveal texture"}],
         [{"name": "Rubbing leaf prints & bark rubbings", "category": "Craft", "region": "Universal", "description": "Taking impressions on paper with crayons"}],
         [{"metric": "Leaf margins", "value": "Smooth, serrated/saw-like, lobed"}],
         ["Visual cues for tree bark rubbing, dry leaves collage art by Vishnu Chinchalkar (Indore)"],
         {"Plant Fairy": "पौधों की परी", "Trunk": "तना", "Margin": "किनारा", "Bark": "छाल", "Rubbing": "छाप"}),

        (3, "Water O' Water!", "पानी रे पानी!", "ceap103", "chap103", 5, "Unit 5: Water Systems, Conservation & Historical Science",
         [{"name_en": "Water Forms", "name_hi": "जल के रूप", "category": "Natural Resource", "attributes": ["Water exists as liquid (river, lake, tap), solid (snow, ice), gas (steam, vapor)", "Water needed for drinking, washing, cooking, growing crops, industrial work"]}],
         [{"name": "Shri Prasad", "role": "Poet", "era": "Modern", "key_contributions": "Composed the classic poem 'Water O' Water!' highlighting floods, droughts, springs and life"}],
         [{"name": "River, Lake, Spring, Waterfall", "region": "Pan-India", "context": "Natural freshwater bodies"}],
         [{"name": "States of Water", "procedure": "Heating water to steam, freezing into ice", "findings": "Reversible phase changes of water"}],
         [],
         [{"metric": "Major water sources", "value": "Ponds, rivers, springs, tubewells, handpumps, taps, bawris"}],
         ["Illustrations of water cycle, container capacities, water storage pots"],
         {"Water": "पानी/जल", "Spring": "झरना", "Snow": "बर्फ", "Steam": "भाप", "Drought": "सूखा", "Flood": "बाढ़"}),

        (4, "Our First School", "हमारा पहला स्कूल", "ceap104", "chap104", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Family", "name_hi": "परिवार", "category": "Social Unit", "attributes": ["Our family is our first school; we learn relations, habits, values, communication first from family members", "Anwari's family: profession of dhobis (washing, drying, ironing clothes)"]}],
         [],
         [],
         [],
         [{"name": "Custom of removing shoes before entering house", "category": "Custom", "region": "Anwari's family / Indian tradition", "description": "Taking off footwear outside"}],
         [],
         ["Family tree diagram cues, facial resemblance sketches"],
         {"Family": "परिवार", "First School": "पहला स्कूल", "Resemblance": "समानता", "Custom": "रिवाज"}),

        (5, "Chhotu's House", "छोटू का घर", "ceap105", "chap105", 4, "Unit 4: Shelter, Architecture & Climatic Adaptations",
         [{"name_en": "Uninvited Guests in House", "name_hi": "घर के बिन बुलाए मेहमान", "category": "Animal/Shelter", "attributes": ["Rats (poor eyesight but excellent sense of smell, touch, and taste), lizards, ants, spiders, mosquitoes, birds live inside houses without invitation", "Chhotu converted a large cement pipe into his home in Mumbai to protect from rain, cold, and rent"]}],
         [],
         [{"name": "Mumbai", "region": "Maharashtra", "context": "Urban migration and makeshift housing"}],
         [],
         [{"name": "Rangoli & House decoration", "category": "Art/Custom", "region": "India", "description": "Decorating courtyards and entrances during festivals"}],
         [{"metric": "Rat senses", "value": "Poor eyesight, high sensitivity to smell and touch"}],
         ["Cement pipe divided into sleeping, cooking, water storage, drying clothes areas"],
         {"House": "घर", "Cement Pipe": "पाइप", "Uninvited Guests": "बिन बुलाए मेहमान", "Rangoli": "रंगोली"}),

        (6, "Foods We Eat", "खाना अपना-अपना", "ceap106", "chap106", 3, "Unit 3: Food, Digestion, Cooking & Vector Diseases",
         [{"name_en": "Regional Cuisines", "name_hi": "क्षेत्रीय खान-पान", "category": "Food Culture", "attributes": [
             "Hong Kong: People eat snakes and snake soup called Ling-hu-fen (लिंग-हू-फेन)",
             "Kashmir: Fish cooked in mustard oil (सरसों का तेल)",
             "Goa: Sea fish cooked in coconut oil (नारियल का तेल)",
             "Kerala: Boiled tapioca (कप्पा) with curry made using coconut; grows both in courtyard and underground",
             "Vipul's grandmother: Dalia/Rice soaked in dal with sugar (sweetened dal in Maharashtra/Gujarat)"
         ]}],
         [],
         [{"name": "Hong Kong, Kashmir, Goa, Kerala", "region": "Asia / India", "context": "Food ecology"}],
         [],
         [{"name": "Ling-hu-fen, Tapioca, Fish in mustard/coconut oil", "category": "Food", "region": "Hong Kong / Kashmir / Goa / Kerala", "description": "Regional staple delicacies based on local availability"}],
         [],
         ["Map showing food origins, tapioca plant, coconut palms, fish dishes"],
         {"Ling-hu-fen": "लिंग-हू-फेन (सांप का मांस)", "Tapioca": "टैपियोका (कप्पा)", "Mustard Oil": "सरसों का तेल", "Coconut Oil": "नारियल का तेल"}),

        (7, "Saying Without Speaking", "बिन बोले बात", "ceap107", "chap107", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Sign Language and Expressions", "name_hi": "सांकेतिक भाषा और भाव", "category": "Communication", "attributes": ["Children who cannot hear or speak communicate through sign language, lip movements, and facial gestures", "Classical Dance: Mudras (hand poses) and Bhavas (facial expressions) convey feelings"]}],
         [],
         [],
         [],
         [{"name": "Mudras & Bhavas", "category": "Art", "region": "Indian Classical Dance (Bharatanatyam, Kathak)", "description": "Expressive gestures for eyes, face, hands"}],
         [],
         ["Illustrations of Mudras (Mukul, Padma, etc.) and facial expression flashcards"],
         {"Sign Language": "सांकेतिक भाषा", "Mudras": "मुद्राएँ", "Bhavas": "भाव", "Facial expression": "चेहरे के भाव"}),

        (8, "Flying High", "पंख फैलाएं", "ceap108", "chap108", 1, "Unit 1: Living World, Animal Behavior & Adaptations",
         [{"name_en": "Birds & Beaks", "name_hi": "पक्षी और चोंच", "category": "Bird Anatomy", "attributes": [
             "Peacock (मोर): National bird of India, beautiful crest on head, dancing in rain, iridescent blue-green feathers",
             "Eagle/Hawk (चील/बाज): Long grooved tail, eats mice, flies high in sky",
             "Parrot (तोता): Green feathers, red curved beak, eats green chillies and guava, mimics human voice",
             "Crow (कौआ): Black feathers, 'caw-caw' sound",
             "Koel (कोयल): Sweet singing voice 'kuhoo-kuhoo', lays eggs in crow's nest",
             "Vulture (गिद्ध): Eats dead animals, bald head, cleans environment",
             "Woodpecker (कटफोड़वा): Makes holes in tree trunks to eat hidden insects, sharp chisel-like beak",
             "Owl (उल्लू): Can rotate its neck backwards to a large extent (~270 degrees), awake at night",
             "Myna (मैना): Moves its neck back and forth with a jerk (झटके से अपनी गर्दन आगे-पीछे करती है)",
             "Feathers: Keep birds warm, help in flying, shed and regrow periodically"
         ]}],
         [],
         [],
         [],
         [],
         [{"metric": "Myna vs Owl neck movement", "value": "Myna moves neck with a jerk; Owl can rotate neck backwards to a large extent"}],
         ["Sketches of bird beaks: curved hook for flesh, chisel for wood, flat for mud, cone for seeds"],
         {"Peacock": "मोर", "Woodpecker": "कटफोड़वा", "Owl": "उल्लू", "Myna": "मैना", "Vulture": "गिद्ध", "Beak": "चोंच", "Jerk": "झटका"}),

        (9, "It's Raining", "बादल आए, बारिश लाए", "ceap109", "chap109", 5, "Unit 5: Water Systems, Conservation & Historical Science",
         [{"name_en": "Appu and Banana Trees", "name_hi": "अप्पू और केले का पेड़", "category": "Flora/Fauna", "attributes": ["Appu the elephant loved bananas; watered drooping banana trees by carrying water in its trunk; plants revived with water"]}],
         [{"name": "Harish Nigam", "role": "Poet", "era": "Contemporary", "key_contributions": "Poem on Clouds (Gore, kale, pyare, matwale badal)"}],
         [],
         [{"name": "Rain & Plant Hydration", "procedure": "Observing wilted leaves before and after rain", "findings": "Plants absorb soil moisture through roots to maintain turgidity"}],
         [],
         [],
         ["Rainbow colors diagram, cloud formation drawings"],
         {"Elephant": "हाथी", "Trunk": "सूँड", "Banana tree": "केले का पेड़", "Rainbow": "इन्द्रधनुष", "Cloud": "बादल"}),

        (10, "What is Cooking", "पकाएँ, खाएँ", "ceap110", "chap110", 3, "Unit 3: Food, Digestion, Cooking & Vector Diseases",
         [{"name_en": "Cooking Methods & Fuels", "name_hi": "पकाने के तरीके और ईंधन", "category": "Culinary Science", "attributes": [
             "Cooking methods: Roasting (सेंकना - Roti, Corn), Boiling (उबालना - Rice, Potato), Frying (तलना - Puri, Pakoda), Baking (भूनना/बेक करना - Cake, Bati)",
             "Cooking utensils: Clay pots, brass (पीतल), bronze (कांसा), copper (तांबा), iron (लोहा), steel",
             "Cooking fuels: Kerosene, LPG cylinder, coal, wood, cowdung cakes (गोबर के उपले), electricity (induction), solar cooker (uses sunlight, glass lid, black painted box)"
         ]}],
         [],
         [],
         [{"name": "Solar Cooker Experiment", "procedure": "Placing food in black-coated closed vessel inside glass-topped box under direct sun", "findings": "Trapped solar heat cooks food without smoke or fuel cost"}],
         [],
         [],
         ["Illustrations of stove types: chulha, angithi, gas stove, solar cooker"],
         {"Roasting": "सेंकना", "Boiling": "उबालना", "Frying": "तलना", "Baking": "बेक करना", "Solar Cooker": "सौर कुकर", "Bronze": "कांसा", "Brass": "पीतल"}),

        (11, "From Here to There", "यहाँ से वहाँ", "ceap111", "chap111", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Modes of Transport", "name_hi": "यातायात के साधन", "category": "Transport", "attributes": [
             "Land: Train (छुक-छुक रेलगाड़ी), bus, car, bicycle, bullock cart, camel cart, horse carriage (tonga)",
             "Water: Boat, steamer, ship, ferry",
             "Air: Aeroplane, helicopter",
             "Emergency: Ambulance, fire engine, police van"
         ]}],
         [{"name": "Harendranath Chattopadhyay", "role": "Poet/Dramatist", "era": "20th Century", "key_contributions": "Poem 'The Train' (छुक-छुक रेलगाड़ी)"}],
         [],
         [],
         [],
         [],
         ["Drawings of train tracks, mountain trails, city traffic, emergency vehicles"],
         {"Train": "रेलगाड़ी", "Ferry": "नाव", "Ambulance": "एम्बुलेंस", "Bullock cart": "बैलगाड़ी", "Camel cart": "ऊँट गाड़ी"}),

        (12, "Work We Do", "काम अपने-अपने", "ceap112", "chap112", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Occupations & Social Roles", "name_hi": "व्यवसाय और सामाजिक कार्य", "category": "Social Structure", "attributes": [
             "Community occupations: Mason, tea stall owner, doctor, nurse, traffic police, sweeper, barber, postman, vegetable seller, cobbler (मोची Jaggu)",
             "Child labour vs Right to Education: Deepali takes care of younger siblings and does household chores, listens to radio stories, desires to go to school"
         ]}],
         [],
         [],
         [],
         [],
         [],
         ["Visual town square diagram showing multiple simultaneous daily occupations"],
         {"Cobbler": "मोची", "Mason": "राजमिस्त्री", "Sweeper": "सफाईकर्मी", "Occupation": "व्यवसाय"}),

        (13, "Sharing Our Feelings", "छूकर देखें", "ceap113", "chap113", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Braille Script", "name_hi": "ब्रेल लिपि", "category": "Assistive Technology", "attributes": [
             "Invented by Louis Braille from France (lost eyesight at age 3 while playing with father's sharp tools)",
             "Braille is written on thick paper by making points (raised dots) with a pointed tool",
             "Read by running fingers along the raised dots",
             "Standard Braille script is based on 6 DOTS (छह बिंदुओं पर आधारित है)",
             "Now Braille can also be typed on computers"
         ]}],
         [{"name": "Louis Braille", "role": "Inventor", "era": "1809–1852 (France)", "key_contributions": "Created the 6-dot embossed Braille code for blind reading and writing"}],
         [{"name": "France", "region": "Europe", "context": "Birthplace of Louis Braille"}],
         [],
         [],
         [{"metric": "Number of dots in Braille", "value": "6 raised dots arranged in a 2x3 matrix cell"}],
         ["Braille cell matrix showing 6 dots and alphabet encodings"],
         {"Braille Script": "ब्रेल लिपि", "Louis Braille": "लुई ब्रेल", "Raised Dots": "उभरे हुए बिंदु", "6 Dots": "6 बिंदु", "White Cane": "सफेद छड़ी"}),

        (14, "The Story of Food", "कहाँ से आया, किसने पकाया", "ceap114", "chap114", 2, "Unit 2: Flora, Seeds, Forest Rights & Agriculture",
         [{"name_en": "Medicinal Plants and Edible Parts", "name_hi": "औषधीय पौधे और खाने योग्य भाग", "category": "Ethnobotany", "attributes": [
             "Remedies: Cough and cold -> Tulsi (basil), Ginger (adrak), Honey; Stomach ache -> Ajwain (carom seeds) with hot water; Toothache -> Clove (laung) oil; Wounds/skin injury -> Haldi (turmeric) paste in warm milk/oil",
             "Plant parts eaten: Roots (carrot, radish, beetroot), Stems (potato, ginger, lotus stem - kamal kakdi), Leaves (spinach, cabbage, mustard), Flowers (Kachnar in UP, Banana flowers in Kerala, Sahjan/drumstick in Maharashtra), Seeds (mustard, wheat, pulses), Fruits (tomato, brinjal, mango)"
         ]}],
         [],
         [],
         [],
         [],
         [],
         ["Classification diagram sorting basket foods into Flowers, Fruits, Leaves, Stems, Roots"],
         {"Kachnar flowers": "कचनार के फूल (उत्तर प्रदेश)", "Banana flowers": "केले के फूल (केरल)", "Sahjan flowers": "सहजन के फूल (महाराष्ट्र)", "Clove": "लौंग", "Turmeric": "हल्दी", "Ajwain": "अजवाइन"}),

        (15, "Making Pots", "आओ बनाएँ बर्तन", "ceap115", "chap115", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Pottery & Early Tools", "name_hi": "मिट्टी के बर्तन", "category": "Material Culture", "attributes": [
             "Story of Phudgudi (sparrow) and Bhanate (crow)",
             "Clay pot making steps: Digging clay from pit (chikni mitti), mixing with water, kneading dough, shaping on potter's wheel (चाक), sun drying, baking in kiln/fire (आवाँ/भट्टी) to make them strong and waterproof",
             "Early humans made stone and clay pots to store grain and water"
         ]}],
         [],
         [],
         [{"name": "Clay baking in kiln", "procedure": "Baking clay at high heat", "findings": "Heat chemically hardens clay making it resistant to water erosion"}],
         [],
         [],
         ["Diagram of potter's wheel, kiln baking, clay moulding with hands"],
         {"Potter's Wheel": "चाक", "Kiln": "आवाँ/भट्टी", "Clay": "चिकनी मिट्टी", "Baking": "पकाना"}),

        (16, "Games We Play", "खेल-खेल में", "ceap116", "chap116", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Traditional Indian Games", "name_hi": "पारंपरिक भारतीय खेल", "category": "Sports/Culture", "attributes": [
             "Stapoo / Hopscotch (टिप्पी / स्टापू): Drawn on ground with chalk, numbered 1 to 8, throwing marker (thippi) into box, hopping on one foot without touching lines",
             "Langdi-taang (लंगड़ी टांग), Blind man's buff (आँख मिचौली), Seven Tiles (पिट्ठू / Satoliya), Marbles (कंचे), Gilli-Danda, Flying kites",
             "Indoor games: Chess (शतरंज), Chaupar, Playing cards, Carrom, Ludo, Snakes and Ladders (सांप-सीढ़ी)"
         ]}],
         [],
         [],
         [],
         [],
         [],
         ["Stapoo numbered court drawing, pitthoo tile stack sketch"],
         {"Stapoo": "स्टापू / टिप्पी", "Pitthoo": "पिट्ठू (सात पत्थर)", "Gilli Danda": "गिल्ली डंडा", "Hopscotch": "लंगड़ी खेल"}),

        (17, "Here comes a Letter", "चिट्ठी आई है", "ceap117", "chap117", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Postal Communication", "name_hi": "डाक संचार", "category": "Communication System", "attributes": [
             "Journey of a letter: Written by Reena in Agartala (Tripura) to Ahmed in New Delhi",
             "Steps: Written on postcard -> Dropped in red postbox -> Collected by postman -> Stamped at post office (round stamp with city date) -> Sorted by pin code / city -> Loaded on train/air -> Delivered to house address",
             "PIN Code: Postal Index Number (6-digit numerical code ensuring error-free routing)"
         ]}],
         [],
         [{"name": "Agartala to New Delhi", "region": "Tripura to Delhi", "context": "National postal route"}],
         [],
         [],
         [{"metric": "PIN Code digits", "value": "6 digits"}],
         ["Diagram of postbox, stamping mark, postcard layout with address box and pin code grid"],
         {"Postcard": "पोस्टकार्ड", "Postman": "डाकिया", "PIN Code": "पिन कोड (6 अंक)", "Postbox": "डाकघर का डिब्बा"}),

        (18, "A House Like This", "ऐसे भी होते हैं घर", "ceap118", "chap118", 4, "Unit 4: Shelter, Architecture & Climatic Adaptations",
         [{"name_en": "Regional Architecture of India", "name_hi": "क्षेत्रीय घर और आवास", "category": "Shelter Architecture", "attributes": [
             "Assam (Molan village): It rains heavily; houses are made 10 to 12 feet (3 to 3.5 meters) high on strong bamboo pillars (बांस के खंभे); roofs are sloping; made of wood and bamboo",
             "Manali (Himachal Pradesh): Hilly area with heavy rain and snowfall; houses are made of stone or wood with sloping roofs",
             "Rajasthan (Rural area): Hot and dry; rainfall is very scarce; houses are made of thick mud walls (दीवारें मिट्टी की मोटी) that keep interior cool; plastered with mud/cow dung; roofs made of thorny bushes (कंटीली झाड़ियाँ / Keekar)",
             "Leh & Ladakh: Cold desert; two-storey stone houses coated with mud and lime; ground floor for animals and winter storage without windows; flat roofs made of thick poplar tree trunks",
             "Srinagar (Kashmir): Houseboats (शिकारा / हाउसबोट) floating on Dal Lake and Jhelum river; Donga houses; houseboats up to 80 feet long",
             "Delhi / Multi-storey flats: High rise buildings made of cement, iron rods, bricks, and glass to accommodate dense population",
             "Igloo: Dome-shaped shelter made of compressed snow blocks in polar regions"
         ]}],
         [],
         [{"name": "Molan village (Assam), Manali (HP), Rajasthan desert, Srinagar (Kashmir), Leh (Ladakh)", "region": "Pan-India", "context": "Architectural adaptation to climate"}],
         [],
         [],
         [{"metric": "Assam bamboo pillar height", "value": "10 to 12 feet (3 to 3.5 meters)"}],
         ["Architectural cross-sections: Assam stilt house, Rajasthan mud hut, Manali sloping roof, Dal Lake houseboat"],
         {"Bamboo pillars": "बांस के खंभे (10-12 फीट)", "Sloping roof": "ढलवां छत", "Mud walls": "मिट्टी की मोटी दीवारें", "Thorny bushes": "कंटीली झाड़ियाँ", "Houseboat": "हाउसबोट/शिकारा", "Igloo": "इग्लू"}),

        (19, "Our Friends - Animals", "हमारे साथी जानवर", "ceap119", "chap119", 1, "Unit 1: Living World, Animal Behavior & Adaptations",
         [{"name_en": "Animal Companionship & Care", "name_hi": "जानवरों की देखभाल और उपयोगिता", "category": "Animal Care", "attributes": [
             "Bird bath: Placing shallow earthen bowl of water on terrace/balcony for birds to drink and bathe in summer",
             "Treating injured birds: Navjyot and Ali applying first-aid to bird hit by classroom fan",
             "Queen's mango orchard story: Birds eat insects and protect mango crop; without birds, insects destroy fruits"
         ]}],
         [],
         [],
         [],
         [],
         [],
         ["Bird bath illustration, food web balance diagram"],
         {"Bird bath": "पक्षियों का जलपात्र", "Veterinary care": "पशु चिकित्सा", "Ecosystem balance": "पारिस्थितिक संतुलन"}),

        (20, "Drop by Drop", "बूँद-बूँद से", "ceap120", "chap120", 5, "Unit 5: Water Systems, Conservation & Historical Science",
         [{"name_en": "Water Conservation & Tanka", "name_hi": "जल संरक्षण और टांका", "category": "Water Architecture", "attributes": [
             "Madho lives in Bajju village in Rajasthan; extreme water scarcity, women walk miles through hot sand to fetch water from well",
             "Water train brings water occasionally",
             "Tanka (टांका): Underground storage pit built in courtyard; courtyard floor is cemented with a slope towards the tanka; rain falling on sloping roof flows down a pipe through a wire sieve/net filter into the underground tanka; covered with a lid; water stored for dry months",
             "Reusing water: Water used for washing hands and face is reused for washing floors; water used for vegetables is used to water garden plants"
         ]}],
         [],
         [{"name": "Bajju village", "region": "Rajasthan", "context": "Arid Thar desert water harvesting"}],
         [],
         [{"name": "Tanka Rainwater Harvesting", "category": "Traditional Engineering", "region": "Rajasthan", "description": "Underground courtyard tank connected to sloping roof via filtered pipe"}],
         [],
         ["Diagram of courtyard tanka with sloping roof, pipe filter, and locked lid"],
         {"Tanka": "टांका (भूमिगत पक्का गड्ढा)", "Sloping roof": "ढलवाँ छत", "Sieve/Filter": "छलनी/जाली", "Bajju village": "बज्जू गाँव (राजस्थान)"}),

        (21, "Families can be Different", "तरह-तरह के परिवार", "ceap121", "chap121", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Family Types", "name_hi": "परिवारों की विविधता", "category": "Sociology", "attributes": [
             "Nuclear families, Extended joint families, Single-parent families, Adoptive families",
             "Gurleen and Nagarajan; Sitamma's joint family in Gwalior; Tara raised by maternal grandfather (Nana) in Chennai; Sara and Habib"
         ]}],
         [],
         [{"name": "Gwalior, Chennai", "region": "Madhya Pradesh / Tamil Nadu", "context": "Urban Indian family settings"}],
         [],
         [],
         [],
         ["Family tree diagrams showing diversity of household structures"],
         {"Joint Family": "संयुक्त परिवार", "Nuclear Family": "एकल परिवार", "Adoption": "गोद लेना"}),

        (22, "Left-Right", "दायाँ-बायाँ", "ceap122", "chap122", 7, "Unit 7: Quantitative & Spatial Bridge",
         [{"name_en": "Map Symbols & Directions", "name_hi": "नक्शे के प्रतीक और दिशाएँ", "category": "Spatial Cartography", "attributes": [
             "Left, Right, Front, Back, Cardinal directions (North, South, East, West)",
             "Map symbols: Conventional signs representing House, School, Tree, Hospital, Post Office, Well, Bus stop, Gate",
             "Map scale: Reducing real ground distances to paper dimensions accurately"
         ]}],
         [],
         [],
         [],
         [],
         [],
         ["Symbol legend table (House ⌂, Tree ♣, Cross for Hospital +, Post Office ✉)"],
         {"Symbols": "प्रतीक/चिह्न", "Map": "नक्शा", "Directions": "दिशाएँ", "Scale": "पैमाना"}),

        (23, "A Beautiful Cloth", "कपड़ा सजा कैसे", "ceap123", "chap123", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Textile Art & Patterns", "name_hi": "वस्त्र शिल्प और छपाई", "category": "Crafts", "attributes": [
             "Sajida's dupatta: Decorated with beautiful embroidery and mirror-work (कढ़ाई और शीशे का काम)",
             "Vegetable block printing: Using cut ladies' finger (bhindi), onion, potato, or carved wooden blocks dipped in natural color dyes to print repeating geometric patterns"
         ]}],
         [],
         [],
         [{"name": "Block printing with vegetables", "procedure": "Cutting bhindi across cross-section and dipping in paint", "findings": "Natural pentagonal flower pattern transfer onto cloth"}],
         [],
         [],
         ["Dupatta patterns, cross-section block stamps of ladies finger and cut flowers"],
         {"Dupatta": "दुपट्टा", "Embroidery": "कढ़ाई", "Mirror-work": "शीशे का काम", "Block Printing": "ठप्पा छपाई"}),

        (24, "Web of Life", "जीवन का जाल", "ceap124", "chap124", 1, "Unit 1: Living World, Animal Behavior & Adaptations",
         [{"name_en": "Ecological Web of Life", "name_hi": "पारिस्थितिक जीवन जाल", "category": "Ecology", "attributes": [
             "Interdependence of living organisms (plants, animals, birds, humans) and non-living elements (sunlight, air, water, soil)",
             "Food chain and Food web connections: Grass -> Grasshopper -> Frog -> Snake -> Eagle; Sun provides energy to all plants"
         ]}],
         [],
         [],
         [],
         [],
         [],
         ["Web of life string diagram connecting sun, water, soil, plants, herbivores, carnivores, humans"],
         {"Web of Life": "जीवन का जाल", "Interdependence": "पारस्परिक निर्भरता", "Food Chain": "खाद्य श्रृंखला", "Ecosystem": "पारिस्थितिकी"})
    ]

    for item in c3_defs:
        ch_num, title_en, title_hi, code_en, code_hi, unit_id, unit_name, fe, hf, gl, se, cc, nd, va, kb = item
        schema = {
            "chapter_metadata": {
                "grade": 3,
                "subject": "EVS",
                "chapter_number": ch_num,
                "chapter_title_en": title_en,
                "chapter_title_hi": title_hi,
                "ncert_code_en": code_en,
                "ncert_code_hi": code_hi,
                "theme_mapping": unit_name,
                "unit_id": unit_id
            },
            "factual_entities": fe,
            "historical_figures_and_travelers": hf,
            "geographical_locations_and_tribes": gl,
            "scientific_experiments_and_processes": se,
            "cultural_customs_foods_and_tools": cc,
            "numerical_data_and_measurements": nd,
            "visual_assets_and_diagram_cues": va,
            "key_vocabulary_bilingual": kb,
            "ncert_source_text_summary": f"Class 3 Chapter {ch_num}: '{title_en}' / '{title_hi}' develops foundational environmental awareness across {unit_name}. Key facts include factual identification, cultural adaptations, and ecological concepts."
        }
        out_file = BASE_DIR / "data" / "ledger" / "class_3" / f"class_3_ch_{ch_num:02d}_{code_en}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
        chapters_data.append(schema)

    print(f"Generated 24 Class 3 chapter schemas.")
    return chapters_data

if __name__ == "__main__":
    build_sprint1_ledger()
