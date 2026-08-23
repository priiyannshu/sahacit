#!/usr/bin/env python3
"""
Sprint 1 Extractor: Generates 77 NCERT Atomic JSON Schemas and LEDGER.md
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def generate_all_77_chapters():
    ledger_entries = []

    # --------------------------------------------------------------------------
    # CLASS 3 (24 CHAPTERS)
    # --------------------------------------------------------------------------
    c3_data = [
        (1, "Poonam's Day Out", "पूनम की दया", "ceap101", "chap101", 1, "Unit 1: Living World, Animal Behavior & Adaptations",
         [{"name_en": "Pond Animals", "name_hi": "तालाब के जीव", "category": "Animal", "attributes": ["Goat, tortoise, crane (बगुला), frog, buffalo, egret", "Locomotion modes: flying, crawling, walking, hopping, swimming"]}],
         [], [{"name": "Local pond/garden", "region": "Rural/Suburban India", "context": "Freshwater habitat"}],
         [{"name": "Animal Locomotion Observation", "procedure": "Classifying animals by feet, wings, crawling, swimming", "findings": "Different anatomical adaptations dictate movement"}],
         [], [{"metric": "Locomotion classification", "value": "Wings (birds), 6 legs (insects), 4 legs (mammals)"}],
         ["Drawings of crow, pigeon, squirrel, monkey, butterfly, frog on tree and in pond"],
         {"Pond": "तालाब", "Crane": "बगुला", "Tortoise": "कछुआ", "Frog": "मेंढक", "Locomotion": "चाल"}),

        (2, "The Plant Fairy", "पौधों की परी", "ceap102", "chap102", 2, "Unit 2: Flora, Seeds, Forest Rights & Agriculture",
         [{"name_en": "Leaves and Trunks", "name_hi": "पत्तियाँ और तने", "category": "Plant", "attributes": ["Leaves have diverse shapes, margins (straight, saw-toothed), colors, and smells", "Lemon, mango, neem, tulsi, pudina, dhaniya identified by rubbing and smelling"]}],
         [{"name": "Vishnu Chinchalkar", "role": "Artist", "era": "20th Century (Indore, MP)", "key_contributions": "Created famous artistic collages and animal pictures using dry fallen leaves"}],
         [{"name": "Neighbourhood garden", "region": "India", "context": "Flora diversity"}],
         [{"name": "Leaf Venation and Bark Rubbing", "procedure": "Rubbing crayons over paper pressed on leaf veins or tree bark", "findings": "Reveals surface texture and structural vein patterns"}],
         [{"name": "Dry leaf collage art", "category": "Craft", "region": "Indore, MP", "description": "Vishnu Chinchalkar's technique of dry leaf mosaics"}],
         [{"metric": "Leaf margin types", "value": "Smooth, serrated/saw-toothed, lobed"}],
         ["Visual cues for tree bark rubbing, dry leaves collage art by Vishnu Chinchalkar"],
         {"Plant Fairy": "पौधों की परी", "Trunk": "तना", "Margin": "किनारा", "Bark": "छाल", "Rubbing": "छाप"}),

        (3, "Water O' Water!", "पानी रे पानी!", "ceap103", "chap103", 5, "Unit 5: Water Systems, Conservation & Historical Science",
         [{"name_en": "Water Forms & Sources", "name_hi": "जल के रूप और स्रोत", "category": "Natural Resource", "attributes": ["Exists as liquid (rivers, lakes, taps), solid (ice, snow), gas (steam, water vapor)", "Essential for drinking, agriculture, cooking, sanitation"]}],
         [{"name": "Shri Prasad", "role": "Poet", "era": "Modern", "key_contributions": "Composed poem 'Water O' Water!' celebrating hydrological diversity"}],
         [{"name": "River, Lake, Spring, Waterfall", "region": "Pan-India", "context": "Freshwater sources"}],
         [{"name": "States of Water", "procedure": "Freezing and heating water", "findings": "Demonstrates three reversible states of matter"}],
         [], [{"metric": "Primary water sources", "value": "Ponds, rivers, springs, tubewells, handpumps, bawris"}],
         ["Water cycle illustrations, container capacity comparisons, traditional earthen water pots"],
         {"Water": "पानी/जल", "Spring": "झरना", "Snow": "बर्फ", "Steam": "भाप", "Drought": "सूखा", "Flood": "बाढ़"}),

        (4, "Our First School", "हमारा पहला स्कूल", "ceap104", "chap104", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Family", "name_hi": "परिवार", "category": "Social Unit", "attributes": ["Family is our primary socialization institution", "Anwari's family dhobi trade (washing, ironing)"]}],
         [], [], [], [{"name": "Removing shoes before entering home", "category": "Custom", "region": "Indian tradition", "description": "Cleanliness practice"}],
         [], ["Family tree charts, facial resemblance sketches"],
         {"Family": "परिवार", "First School": "पहला स्कूल", "Resemblance": "समानता", "Custom": "रिवाज"}),

        (5, "Chhotu's House", "छोटू का घर", "ceap105", "chap105", 4, "Unit 4: Shelter, Architecture & Climatic Adaptations",
         [{"name_en": "Uninvited Household Organisms & Makeshift Housing", "name_hi": "घर के बिन बुलाए जीव और अस्थायी आवास", "category": "Shelter/Fauna", "attributes": ["Rats (poor vision, high olfactory and tactile sensitivity), lizards, spiders, mosquitoes", "Chhotu transformed a large concrete pipe into a multi-utility shelter in Mumbai"]}],
         [], [{"name": "Mumbai", "region": "Maharashtra", "context": "Urban migration and shelter adaptation"}],
         [], [{"name": "Rangoli", "category": "Art", "region": "India", "description": "Floor and courtyard decoration"}],
         [{"metric": "Rat senses", "value": "Poor eyesight, acute smell, touch, and taste"}],
         ["Concrete pipe home layout (cooking, sleeping, storage divisions)"],
         {"House": "घर", "Concrete Pipe": "सीमेंट का पाइप", "Uninvited Guests": "बिन बुलाए मेहमान", "Rangoli": "रंगोली"}),

        (6, "Foods We Eat", "खाना अपना-अपना", "ceap106", "chap106", 3, "Unit 3: Food, Digestion, Cooking & Vector Diseases",
         [{"name_en": "Regional Staple Cuisines", "name_hi": "क्षेत्रीय खान-पान", "category": "Food Culture", "attributes": [
             "Hong Kong: Snake meat dish and soup called Ling-hu-fen (लिंग-हू-फेन)",
             "Kashmir: Freshwater fish cooked in mustard oil (सरसों का तेल)",
             "Goa: Marine sea fish cooked in coconut oil (नारियल का तेल)",
             "Kerala: Boiled tapioca (कप्पा) with coconut curry; grown in domestic yards",
             "Gujarat/Maharashtra: Sweetened dal (दाल में चीनी) with dalia/rice"
         ]}],
         [], [{"name": "Hong Kong, Kashmir, Goa, Kerala", "region": "Global / India", "context": "Ecological cuisine adaptation"}],
         [], [{"name": "Ling-hu-fen & Tapioca", "category": "Food", "region": "Hong Kong / Kerala", "description": "Locally harvested delicacies"}],
         [], ["Geographical food origin map, tapioca root and plant, coconut trees"],
         {"Ling-hu-fen": "लिंग-हू-फेन (सांप का मांस)", "Tapioca": "टैपियोका (कप्पा)", "Mustard Oil": "सरसों का तेल", "Coconut Oil": "नारियल का तेल"}),

        (7, "Saying Without Speaking", "बिन बोले बात", "ceap107", "chap107", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Non-Verbal Expression & Mudras", "name_hi": "सांकेतिक संवाद और मुद्राएँ", "category": "Communication/Art", "attributes": ["Sign language for deaf/mute individuals", "Indian Classical Dance: Mudras (hand gestures) and Bhavas (facial expressions) convey emotional narratives"]}],
         [], [], [], [{"name": "Mudras & Bhavas", "category": "Classical Dance", "region": "India", "description": "Gesture-based non-verbal communication"}],
         [], ["Sketches of classical dance Mudras and emotion expressions"],
         {"Sign Language": "सांकेतिक भाषा", "Mudras": "मुद्राएँ", "Bhavas": "भाव", "Non-verbal": "अशाब्दिक संवाद"}),

        (8, "Flying High", "पंख फैलाएं", "ceap108", "chap108", 1, "Unit 1: Living World, Animal Behavior & Adaptations",
         [{"name_en": "Avian Diversity, Beak Structures & Neck Mobility", "name_hi": "पक्षी, चोंच की बनावट और गर्दन की गति", "category": "Ornithology", "attributes": [
             "Peacock: National bird, iridescent crest and tail plumes, rain dance",
             "Eagle/Hawk: Grooved tail, high-altitude flight, rodent predator",
             "Parrot: Red hooked beak, green feathers, eats chillies/guava, vocal mimicry",
             "Koel: Sings 'kuhoo-kuhoo', brood parasite laying eggs in crow nests",
             "Vulture: Scavenger eating carrion, bald head, environmental sanitation",
             "Woodpecker: Chisel beak boring tree trunks for insects",
             "Owl: Rotates neck backwards to a large extent (~270 degrees), nocturnal",
             "Myna: Moves neck back and forth with a jerk (झटके से गर्दन हिलाना)",
             "Feathers: Provide aerodynamic lift, insulation, molting cycles"
         ]}],
         [], [], [], [],
         [{"metric": "Neck rotation comparison", "value": "Owl = ~270° backward rotation; Myna = Jerky back-and-forth motion"}],
         ["Beak types: Hooked (meat), Chisel (wood), Probe (nectar), Strainer (mud)"],
         {"Peacock": "मोर", "Woodpecker": "कटफोड़वा", "Owl": "उल्लू", "Myna": "मैना", "Vulture": "गिद्ध", "Beak": "चोंच", "Jerk": "झटका"}),

        (9, "It's Raining", "बादल आए, बारिश लाए", "ceap109", "chap109", 5, "Unit 5: Water Systems, Conservation & Historical Science",
         [{"name_en": "Precipitation & Botanical Hydration", "name_hi": "वर्षा और पौधों का जल अवशोषण", "category": "Hydrology/Botany", "attributes": ["Appu elephant hydrating wilted banana trees with trunk", "Rainfall replenishes soil moisture, ending plant wilting"]}],
         [{"name": "Harish Nigam", "role": "Poet", "era": "Contemporary", "key_contributions": "Poem 'Clouds'"}],
         [], [{"name": "Plant Turgidity Recovery", "procedure": "Watering dry banana foliage", "findings": "Root xylem conduits restore leaf turgor pressure"}],
         [], [], ["Rainbow refraction diagrams, cloud formations"],
         {"Elephant": "हाथी", "Trunk": "सूँड", "Banana": "केला", "Rainbow": "इन्द्रधनुष", "Clouds": "बादल"}),

        (10, "What is Cooking", "पकाएँ, खाएँ", "ceap110", "chap110", 3, "Unit 3: Food, Digestion, Cooking & Vector Diseases",
         [{"name_en": "Culinary Thermodynamics & Utensil Metallurgy", "name_hi": "खाना पकाने की विधियाँ और बर्तन धातु विज्ञान", "category": "Food Science", "attributes": [
             "Methods: Roasting (सेंकना), Boiling (उबालना), Frying (तलना), Baking (बेक करना)",
             "Utensil materials: Clay, brass (पीतल = copper + zinc), bronze (कांसा = copper + tin), copper, iron, stainless steel",
             "Fuels & Solar Cooker: Wood, coal, LPG, biogas, electricity, solar cooker (black interior, glass reflector traps radiant heat)"
         ]}],
         [], [], [{"name": "Solar Cooking", "procedure": "Trapping solar radiation in insulated black-box cooker", "findings": "Converts light energy to heat without smoke or fossil fuels"}],
         [], [], ["Stove schematics: Chulha, Angithi, Biogas burner, Solar oven"],
         {"Roasting": "सेंकना", "Boiling": "उबालना", "Frying": "तलना", "Baking": "बेक करना", "Solar Cooker": "सौर कुकर", "Bronze": "कांसा", "Brass": "पीतल"}),

        (11, "From Here to There", "यहाँ से वहाँ", "ceap111", "chap111", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Transportation Networks", "name_hi": "परिवहन प्रणालियाँ", "category": "Transportation", "attributes": ["Land (train, bus, bullock cart), Water (ship, ferry), Air (airplane, helicopter), Emergency (ambulance, fire truck)"]}],
         [{"name": "Harendranath Chattopadhyay", "role": "Poet", "era": "20th Century", "key_contributions": "Poem 'The Train'"}],
         [], [], [], [], ["Drawings of railway network, metro rail, ambulances"],
         {"Train": "रेलगाड़ी", "Ferry": "फेरी", "Ambulance": "एम्बुलेंस", "Transport": "यातायात"}),

        (12, "Work We Do", "काम अपने-अपने", "ceap112", "chap112", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Division of Labour & Educational Rights", "name_hi": "श्रम विभाजन और शिक्षा का अधिकार", "category": "Sociology", "attributes": ["Community trades: Cobbler (Jaggu), mason, sweeper, traffic police, tea vendor", "Child domestic labour vs Right to Education: Deepali's story"]}],
         [], [], [], [], [], ["Busy town square with multiple synchronous occupations"],
         {"Cobbler": "मोची", "Mason": "राजमिस्त्री", "Sweeper": "सफाईकर्मी", "RTE": "शिक्षा का अधिकार"}),

        (13, "Sharing Our Feelings", "छूकर देखें", "ceap113", "chap113", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Braille Embossed Tactile System", "name_hi": "ब्रेल लिपि और स्पर्श संवेदन", "category": "Assistive Technology", "attributes": [
             "Invented by Louis Braille from France (blinded by tool accident at age 3)",
             "Embossed dots on thick paper read by finger touch",
             "Standard Braille is based on 6 DOTS arranged in 2x3 matrix cells",
             "Can now be typed on computerized braille embossers"
         ]}],
         [{"name": "Louis Braille", "role": "Inventor", "era": "1809–1852 (France)", "key_contributions": "Created the 6-dot embossed tactile Braille writing code"}],
         [{"name": "France", "region": "Europe", "context": "Invention of Braille system"}],
         [], [], [{"metric": "Braille matrix dots", "value": "6 raised dots in 2x3 cell"}],
         ["Braille 6-dot cell diagram with alphabet representations"],
         {"Braille": "ब्रेल लिपि", "Louis Braille": "लुई ब्रेल", "6 Raised Dots": "6 उभरे बिंदु", "Tactile": "स्पर्शनीय"}),

        (14, "The Story of Food", "कहाँ से आया, किसने पकाया", "ceap114", "chap114", 2, "Unit 2: Flora, Seeds, Forest Rights & Agriculture",
         [{"name_en": "Ethnobotany & Edible Plant Anatomy", "name_hi": "पारंपरिक औषधीय पौधे और खाने योग्य भाग", "category": "Ethnobotany", "attributes": [
             "Home remedies: Cough/cold (Tulsi, ginger), Stomach ache (Ajwain), Toothache (Clove oil), Wounds (Turmeric)",
             "Edible organs: Flowers (Kachnar in UP, Banana flowers in Kerala, Sahjan in Maharashtra), Roots (carrot, radish), Stems (potato, lotus stem), Leaves (spinach, mustard)"
         ]}],
         [], [], [], [], [], ["Classification matrix: Roots, Stems, Leaves, Flowers, Fruits"],
         {"Kachnar": "कचनार (यूपी)", "Banana flowers": "केले के फूल (केरल)", "Sahjan": "सहजन (महाराष्ट्र)", "Clove": "लौंग", "Turmeric": "हल्दी"}),

        (15, "Making Pots", "आओ बनाएँ बर्तन", "ceap115", "chap115", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Pottery Ceramic Technology", "name_hi": "मृद्भाण्ड और चाक शिल्प", "category": "Ceramics/History", "attributes": ["Steps: Clay digging, kneading with water, shaping on potter's wheel (चाक), drying, kiln firing (आवाँ) for vitrification and strength"]}],
         [], [], [{"name": "Clay Vitrification", "procedure": "Firing shaped clay pots in kiln", "findings": "High temperature causes silicate fusion, hardening the vessel"}],
         [], [], ["Potter's wheel, kiln firing, ancient grain storage urns"],
         {"Potter's Wheel": "चाक", "Kiln": "आवाँ/भट्टी", "Clay": "चिकनी मिट्टी", "Vitrification": "पकाना"}),

        (16, "Games We Play", "खेल-खेल में", "ceap116", "chap116", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Indigenous Sports & Games", "name_hi": "पारंपरिक खेल", "category": "Sports Culture", "attributes": [
             "Stapoo (Hopscotch / टिप्पी): Chalk grid 1-8, throwing marker into box, single-leg hopping",
             "Pitthoo (Seven stones), Gilli-Danda, Marbles (कंचे), Kabaddi, Chess (शतरंज), Chaupar, Snakes and Ladders"
         ]}],
         [], [], [], [], [], ["Stapoo numbered hopscotch court, Pitthoo stone pile"],
         {"Stapoo": "स्टापू/टिप्पी", "Pitthoo": "पिट्ठू (सात पत्थर)", "Gilli Danda": "गिल्ली डंडा", "Hopscotch": "लंगड़ी टांग"}),

        (17, "Here comes a Letter", "चिट्ठी आई है", "ceap117", "chap117", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Postal System & PIN Routing", "name_hi": "डाक व्यवस्था और पिन कोड", "category": "Logistics", "attributes": [
             "Postal sequence: Writing postcard -> Red postbox -> Postal van -> Post office date stamping -> Regional sorting -> Transport via train/air -> Postman delivery",
             "PIN Code: 6-digit Postal Index Number for algorithmic geographical sorting"
         ]}],
         [], [{"name": "Agartala (Tripura) to New Delhi", "region": "Tripura / Delhi", "context": "Interstate mail routing"}],
         [], [], [{"metric": "PIN code digits", "value": "6 digits"}],
         ["Postcard template with 6-box PIN grid, post office cancellation stamp"],
         {"Postcard": "पोस्टकार्ड", "PIN Code": "पिन कोड (6 अंक)", "Postman": "डाकिया", "Sorting": "छंटाई"}),

        (18, "A House Like This", "ऐसे भी होते हैं घर", "ceap118", "chap118", 4, "Unit 4: Shelter, Architecture & Climatic Adaptations",
         [{"name_en": "Climatic Vernacular Architecture of India", "name_hi": "जलवायु आधारित भारतीय क्षेत्रीय आवास", "category": "Vernacular Architecture", "attributes": [
             "Assam (Molan village): High rainfall; houses built 10 to 12 feet (3-3.5 m) high on strong bamboo pillars; sloping roofs of wood/thatch",
             "Manali (HP): Mountainous heavy snowfall and rain; stone and wood houses with sloping roofs",
             "Rajasthan: Arid hot desert; thick mud walls keep interior cool; plastered with cow dung; roofs of thorny Keekar bushes (कंटीली झाड़ियाँ)",
             "Leh Ladakh: Cold desert; 2-storey stone houses coated with mud/lime; windowless ground floor for livestock/winter storage; flat poplar trunk roofs",
             "Srinagar (Kashmir): Houseboats on Dal lake (up to 80 ft long); Donga boats; Shikara; Khatamband ceiling puzzle woodwork",
             "Plains/Delhi: Multi-storey brick, cement, and steel apartments",
             "Polar regions: Igloo dome shelters of compressed snow blocks"
         ]}],
         [], [{"name": "Molan (Assam), Manali (HP), Rajasthan, Leh, Srinagar", "region": "Pan-India", "context": "Climatic architectural adaptation"}],
         [], [], [{"metric": "Assam bamboo stilt height", "value": "10 to 12 feet (3 to 3.5 meters)"}],
         ["Drawings of Assam bamboo stilt house, Rajasthan mud hut, Manali sloping roof, Dal Lake houseboat"],
         {"Bamboo stilts": "बांस के खंभे (10-12 फीट)", "Sloping roof": "ढलवां छत", "Mud walls": "मिट्टी की मोटी दीवारें", "Thorny bushes": "कंटीली झाड़ियाँ", "Houseboat": "हाउसबोट"}),

        (19, "Our Friends - Animals", "हमारे साथी जानवर", "ceap119", "chap119", 1, "Unit 1: Living World, Animal Behavior & Adaptations",
         [{"name_en": "Faunal Coexistence & Biological Pest Control", "name_hi": "जीव सह-अस्तित्व और जैविक कीट नियंत्रण", "category": "Animal Care/Ecology", "attributes": ["Bird baths for summer hydration; Queen's mango orchard lesson: birds consume agricultural insect pests, maintaining orchard health"]}],
         [], [], [], [], [], ["Bird bath setup, ecological food web balance diagram"],
         {"Bird bath": "पक्षियों का जलपात्र", "Pest control": "जैविक कीट नियंत्रण", "Coexistence": "सह-अस्तित्व"}),

        (20, "Drop by Drop", "बूँद-बूँद से", "ceap120", "chap120", 5, "Unit 5: Water Systems, Conservation & Historical Science",
         [{"name_en": "Arid Water Harvesting & Tanka Architecture", "name_hi": "मरुस्थलीय जल संचयन और टांका संरचना", "category": "Water Engineering", "attributes": [
             "Bajju village (Rajasthan) water scarcity; Tanka: Underground paved masonry cistern in paved courtyard; rain from sloping roof flows down pipe through mesh filter into tanka; sealed with lid for dry season storage"
         ]}],
         [], [{"name": "Bajju village", "region": "Rajasthan", "context": "Thar desert rainwater harvesting"}],
         [], [{"name": "Tanka Rainwater Cistern", "category": "Traditional Engineering", "region": "Rajasthan", "description": "Filtered roof catchment tanka"}],
         [], ["Courtyard tanka cutaway diagram with sloped floor, inflow pipe, and wire mesh filter"],
         {"Tanka": "टांका (भूमिगत पक्का गड्ढा)", "Sloping roof": "ढलवाँ छत", "Filter mesh": "छलनी/जाली", "Bajju": "बज्जू गाँव (राजस्थान)"}),

        (21, "Families can be Different", "तरह-तरह के परिवार", "ceap121", "chap121", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Family Typologies & Social Structures", "name_hi": "परिवार संरचना की विविधता", "category": "Sociology", "attributes": ["Nuclear, Joint, Single-parent, Adoptive family structures across urban and rural India"]}],
         [], [{"name": "Gwalior, Chennai", "region": "MP / Tamil Nadu", "context": "Urban Indian family settings"}],
         [], [], [], ["Comparative family tree structures"],
         {"Joint Family": "संयुक्त परिवार", "Nuclear Family": "एकल परिवार", "Adoption": "गोद लेना"}),

        (22, "Left-Right", "दायाँ-बायाँ", "ceap122", "chap122", 7, "Unit 7: Quantitative & Spatial Bridge",
         [{"name_en": "Spatial Mapping Symbols & Scale", "name_hi": "मानचित्र प्रतीक और पैमाना", "category": "Cartography", "attributes": ["Relative position (left, right, cardinal directions), conventional map symbols, scale representation"]}],
         [], [], [], [], [], ["Conventional symbol key (Hospital, School, Well, Tree, Post Office)"],
         {"Map": "नक्शा", "Symbols": "प्रतीक", "Scale": "पैमाना", "Directions": "दिशाएँ"}),

        (23, "A Beautiful Cloth", "कपड़ा सजा कैसे", "ceap123", "chap123", 6, "Unit 6: Travel, Culture, Traditional Arts & Space",
         [{"name_en": "Textile Embellishment & Vegetable Block Printing", "name_hi": "वस्त्र सज्जा और ठप्पा छपाई", "category": "Textile Crafts", "attributes": ["Sajida's dupatta with embroidery and mirror-work; natural block printing using cut bhindi and carved wooden blocks"]}],
         [], [], [{"name": "Vegetable Stamping", "procedure": "Dipping cross-section of bhindi in vegetable dyes", "findings": "Creates symmetrical pentagonal floral prints on fabrics"}],
         [], [], ["Dupatta geometric patterns, block prints"],
         {"Embroidery": "कढ़ाई", "Mirror-work": "शीशे का काम", "Block Printing": "ठप्पा छपाई"}),

        (24, "Web of Life", "जीवन का जाल", "ceap124", "chap124", 1, "Unit 1: Living World, Animal Behavior & Adaptations",
         [{"name_en": "Biotic-Abiotic Ecological Interdependence", "name_hi": "पारिस्थितिक जीवन जाल", "category": "Ecology", "attributes": ["Sunlight, soil, air, water sustain plants; trophic food webs link herbivores, carnivores, decomposers, and humans"]}],
         [], [], [], [], [], ["Web of life string network diagram"],
         {"Web of Life": "जीवन का जाल", "Food Web": "खाद्य जाल", "Interdependence": "पारस्परिक निर्भरता"})
    ]

    for item in c3_data:
        ch_num, title_en, title_hi, code_en, code_hi, unit_id, unit_name, fe, hf, gl, se, cc, nd, va, kb = item
        schema = {
            "chapter_metadata": {
                "grade": 3, "subject": "EVS", "chapter_number": ch_num,
                "chapter_title_en": title_en, "chapter_title_hi": title_hi,
                "ncert_code_en": code_en, "ncert_code_hi": code_hi,
                "theme_mapping": unit_name, "unit_id": unit_id
            },
            "factual_entities": fe, "historical_figures_and_travelers": hf,
            "geographical_locations_and_tribes": gl, "scientific_experiments_and_processes": se,
            "cultural_customs_foods_and_tools": cc, "numerical_data_and_measurements": nd,
            "visual_assets_and_diagram_cues": va, "key_vocabulary_bilingual": kb,
            "ncert_source_text_summary": f"Class 3 Chapter {ch_num}: '{title_en}' / '{title_hi}' covers {unit_name} foundational facts, regional adaptations, and ecological concepts."
        }
        out_file = BASE_DIR / "data" / "ledger" / "class_3" / f"class_3_ch_{ch_num:02d}_{code_en}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
        ledger_entries.append(schema)

    # --------------------------------------------------------------------------
    # CLASS 4 (27 CHAPTERS)
    # --------------------------------------------------------------------------
    # Will execute in next step
    print("Class 3 (24 chapters) written to data/ledger/class_3/")
    return ledger_entries

if __name__ == "__main__":
    generate_all_77_chapters()
