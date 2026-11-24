import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from generate_pdf_helpers import (
    draw_header, draw_section_banner, draw_node, 
    draw_arrow_down, draw_branch_2, draw_branch_3, draw_branch_4
)

def build_pdf(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    total_pages = 5
    
    # Color palette for names
    C_BLUE = colors.HexColor("#1D4ED8")    # Royal Blue
    C_RED = colors.HexColor("#DC2626")     # Crimson Red
    C_GREEN = colors.HexColor("#047857")   # Deep Emerald
    C_PURPLE = colors.HexColor("#7C3AED")  # Royal Purple
    C_AMBER = colors.HexColor("#B45309")   # Warm Amber
    C_TEAL = colors.HexColor("#0F766E")    # Dark Teal
    
    # -------------------------------------------------------------
    # PAGE 1: ANCIENT MAGADHA, MAURYAS & SHUNGAS
    # -------------------------------------------------------------
    draw_header(c, "UPSC CSE: ROYAL GENEALOGICAL TREES & LINEAGES", 
                "Sheet 1: Ancient Magadha, Imperial Mauryas & Shungas", 1, total_pages)
    
    # 1.1 Haryanka Dynasty
    draw_section_banner(c, 755, "1. Haryanka Dynasty", "6th – 5th Century BCE", "Rajgriha / Pataliputra")
    # Tree: Bimbisara -> Ajatashatru -> Udayin -> Nagadasaka
    w, h = 115, 36
    draw_node(c, 40, 710, w, h, "Bimbisara", "b. c.558 – d.492 BCE", "6th–5th C. BCE", "Matrimonial Alliances", C_BLUE)
    draw_arrow_down(c, 155, 728, 175) # right horizontal connection
    c.line(155, 728, 175, 728) # horizontal line
    # Actually let's do a vertical or horizontal flow
    # Let's place 4 nodes across horizontally!
    # Available width: 30 to 565 = 535 pt.
    # 4 nodes: w=115 each, gap = (535 - 460) / 3 = 25 pt.
    x0, x1, x2, x3 = 35, 175, 315, 455
    y_h = 708
    draw_node(c, x0, y_h, w, h, "Bimbisara", "b. c.558 – d.492 BCE", "6th–5th C. BCE", "Founder; Anga; Jivaka", C_BLUE)
    draw_node(c, x1, y_h, w, h, "Ajatashatru", "b. c.512 – d.460 BCE", "5th C. BCE", "1st Buddhist Council", C_BLUE)
    draw_node(c, x2, y_h, w, h, "Udayin", "b. c.480 – d.444 BCE", "5th C. BCE", "Founded Pataliputra", C_BLUE)
    draw_node(c, x3, y_h, w, h, "Nagadasaka", "b. c.450 – d.413 BCE", "5th C. BCE", "Last Haryanka King", C_BLUE)
    
    # Arrows between horizontal steps
    for xa in [x0 + w, x1 + w, x2 + w]:
        c.setStrokeColor(colors.HexColor("#64748B"))
        c.setLineWidth(1)
        c.line(xa, y_h + h/2, xa + 25, y_h + h/2)
        # arrow head pointing right
        c.setFillColor(colors.HexColor("#64748B"))
        p = c.beginPath()
        p.moveTo(xa + 25, y_h + h/2)
        p.lineTo(xa + 20, y_h + h/2 + 2.5)
        p.lineTo(xa + 20, y_h + h/2 - 2.5)
        p.close()
        c.drawPath(p, fill=1, stroke=0)

    # 1.2 Shishunaga & Nanda Dynasties
    draw_section_banner(c, 672, "2. Shishunaga & Nanda Dynasties", "5th – 4th Century BCE", "Pataliputra")
    y_sn = 625
    draw_node(c, x0, y_sn, w, h, "Shishunaga", "b. c.440 – d.395 BCE", "5th–4th C. BCE", "Destroyed Avanti", C_PURPLE)
    draw_node(c, x1, y_sn, w, h, "Kalashoka", "b. c.415 – d.367 BCE", "4th C. BCE", "2nd Buddhist Council", C_PURPLE)
    draw_node(c, x2, y_sn, w, h, "Mahapadma Nanda", "b. c.400 – d.345 BCE", "4th C. BCE", "Title: Ekarat; Empire", C_RED)
    draw_node(c, x3, y_sn, w, h, "Dhana Nanda", "b. c.360 – d.321 BCE", "4th C. BCE", "Alexander's Invasion", C_RED)
    
    for xa in [x0 + w, x1 + w, x2 + w]:
        c.setStrokeColor(colors.HexColor("#64748B"))
        c.setLineWidth(1)
        c.line(xa, y_sn + h/2, xa + 25, y_sn + h/2)
        c.setFillColor(colors.HexColor("#64748B"))
        p = c.beginPath()
        p.moveTo(xa + 25, y_sn + h/2)
        p.lineTo(xa + 20, y_sn + h/2 + 2.5)
        p.lineTo(xa + 20, y_sn + h/2 - 2.5)
        p.close()
        c.drawPath(p, fill=1, stroke=0)

    # 1.3 Mauryan Imperial Dynasty
    draw_section_banner(c, 590, "3. Imperial Mauryan Dynasty", "4th – 2nd Century BCE", "Pataliputra")
    # CGM at top
    w_m, h_m = 130, 36
    x_cgm = 297.64 - w_m/2
    draw_node(c, x_cgm, 542, w_m, h_m, "Chandragupta Maurya", "b. 340 – d. 297 BCE", "4th–3rd C. BCE", "Founder; Chanakya; Sallekhana", C_BLUE)
    
    draw_arrow_down(c, 297.64, 542, 524, "son")
    draw_node(c, x_cgm, 488, w_m, h_m, "Bindusara Amitraghata", "b. c.320 – d. 273 BCE", "4th–3rd C. BCE", "Ajivika Patron; Deimachus", C_BLUE)
    
    draw_arrow_down(c, 297.64, 488, 470, "son")
    draw_node(c, x_cgm, 434, w_m, h_m, "Ashoka the Great", "b. 304 – d. 232 BCE", "4th–3rd C. BCE", "Dhamma; Edicts; 3rd Council", C_BLUE)
    
    # 3 children branches of Ashoka
    # Kunala (Governor/Successor line), Mahendra & Sanghamitta (Buddhist envoys), Jalauka (Kashmir)
    draw_branch_3(c, 297.64, 434, 110 + w_m/2, 297.64, 355 + w_m/2, 404)
    draw_node(c, 110, 368, w_m, h_m, "Prince Kunala", "b. c.265 – d. c.220 BCE", "3rd C. BCE", "Viceroy of Taxila", C_BLUE)
    draw_node(c, x_cgm, 368, w_m, h_m, "Mahendra & Sanghamitta", "b. c.285 – d. c.225 BCE", "3rd C. BCE", "Ceylon Dhamma Mission", C_TEAL)
    draw_node(c, 355, 368, w_m, h_m, "Tivara / Jalauka", "b. c.275 – d. c.230 BCE", "3rd C. BCE", "Queen Karuvaki's son", C_BLUE)
    
    # Down from Kunala -> Dasharatha & Samprati
    draw_branch_2(c, 110 + w_m/2, 368, 55 + w_m/2, 210 + w_m/2, 338, "grandson", "grandson")
    draw_node(c, 55, 302, w_m, h_m, "Dasharatha Maurya", "b. c.252 – d. 224 BCE", "3rd C. BCE", "Barabar Cave Edicts", C_BLUE)
    draw_node(c, 210, 302, w_m, h_m, "Samprati Maurya", "b. c.245 – d. 215 BCE", "3rd C. BCE", "Jain Patron (Suhastin)", C_BLUE)
    
    # Brihadratha (Last Maurya)
    draw_arrow_down(c, 210 + w_m/2, 302, 274, "lineage")
    draw_node(c, 210, 238, w_m, h_m, "Brihadratha (Last)", "b. c.220 – d. 185 BCE", "3rd–2nd C. BCE", "Slain by Pushyamitra Shunga", C_RED)

    # 1.4 Shunga Dynasty
    draw_section_banner(c, 204, "4. Shunga Dynasty (Post-Mauryan)", "2nd – 1st Century BCE", "Vidisha / Pataliputra")
    y_sh = 158
    draw_node(c, x0, y_sh, w, h, "Pushyamitra Shunga", "b. c.230 – d. 151 BCE", "3rd–2nd C. BCE", "Ashvamedha; Patanjali", C_GREEN)
    draw_node(c, x1, y_sh, w, h, "Agnimitra", "b. c.195 – d. 141 BCE", "2nd C. BCE", "Malavikagnimitram Hero", C_GREEN)
    draw_node(c, x2, y_sh, w, h, "Bhagabhadra", "b. c.140 – d. 83 BCE", "2nd–1st C. BCE", "Heliodorus Garuda Pillar", C_GREEN)
    draw_node(c, x3, y_sh, w, h, "Devabhuti (Last)", "b. c.105 – d. 73 BCE", "2nd–1st C. BCE", "Killed by Vasudeva Kanva", C_RED)
    
    for xa in [x0 + w, x1 + w, x2 + w]:
        c.setStrokeColor(colors.HexColor("#64748B"))
        c.setLineWidth(1)
        c.line(xa, y_sh + h/2, xa + 25, y_sh + h/2)
        c.setFillColor(colors.HexColor("#64748B"))
        p = c.beginPath()
        p.moveTo(xa + 25, y_sh + h/2)
        p.lineTo(xa + 20, y_sh + h/2 + 2.5)
        p.lineTo(xa + 20, y_sh + h/2 - 2.5)
        p.close()
        c.drawPath(p, fill=1, stroke=0)

    # Notes box at bottom
    c.setFillColor(colors.HexColor("#F8FAFC"))
    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.roundRect(30, 42, 535.28, 98, 3, fill=1, stroke=1)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(colors.HexColor("#1E3A8A"))
    c.drawString(40, 126, "KEY UPSC GENEALOGICAL & CHRONOLOGICAL HIGHLIGHTS:")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(colors.HexColor("#1E293B"))
    c.drawString(40, 112, "• Magadhan Succession: Haryanka (Bimbisara) -> Shishunaga (Kalashoka) -> Nanda (Mahapadma) -> Maurya (Chandragupta).")
    c.drawString(40, 99, "• Buddhist Councils: 1st Council at Rajgriha (Ajatashatru), 2nd Council at Vaishali (Kalashoka), 3rd Council at Pataliputra (Ashoka).")
    c.drawString(40, 86, "• Foreign Chronological Anchors: Alexander's Invasion (326 BCE, contemporary with Dhana Nanda & Chandragupta Maurya).")
    c.drawString(40, 73, "• Matrimonial Diplomacy: Bimbisara with Kosala/Lichchhavi; Chandragupta Maurya with Seleucid Greek princess (Treaty of 303 BCE).")
    c.drawString(40, 60, "• Dynasty Transitions: Shishunaga minister replaced Nagadasaka; Pushyamitra Shunga (Senapati) assassinated Brihadratha in 185 BCE.")
    c.drawString(40, 48, "• Epigraphic Records: Hathigumpha Inscription (Nanda canal); Ashokan Major Rock Edict XIII (Kalinga War, 261 BCE).")

    c.showPage()

    # -------------------------------------------------------------
    # PAGE 2: GUPTAS, VAKATAKAS & HARSHAVARDHANA
    # -------------------------------------------------------------
    draw_header(c, "UPSC CSE: ROYAL GENEALOGICAL TREES & LINEAGES", 
                "Sheet 2: Imperial Guptas, Vakatakas & Pushyabhuti (Harsha)", 2, total_pages)
    
    # 2.1 Imperial Guptas
    draw_section_banner(c, 755, "1. Imperial Gupta Dynasty", "4th – 6th Century CE", "Pataliputra & Ujjain")
    w_g, h_g = 120, 35
    
    # Row 1: Sri Gupta & Ghatotkacha
    draw_node(c, 160, 712, w_g, h_g, "Sri Gupta (Founder)", "b. c.240 – d. c.280 CE", "3rd C. CE", "Title: Maharaja", C_BLUE)
    draw_arrow_down(c, 280, 729.5, 315) # horizontal right
    c.line(280, 729.5, 315, 729.5)
    c.setFillColor(colors.HexColor("#64748B"))
    p = c.beginPath()
    p.moveTo(315, 729.5); p.lineTo(310, 732); p.lineTo(310, 727); p.close()
    c.drawPath(p, fill=1, stroke=0)
    draw_node(c, 315, 712, w_g, h_g, "Ghatotkacha", "b. c.265 – d. 319 CE", "3rd–4th C. CE", "Title: Maharaja", C_BLUE)
    
    # Down to Chandragupta I
    draw_arrow_down(c, 375, 712, 694, "son")
    draw_node(c, 315, 658, w_g, h_g, "Chandragupta I", "b. c.285 – d. 335 CE", "3rd–4th C. CE", "Gupta Era 319; m. Kumaradevi", C_BLUE)
    
    # Down to Samudragupta
    draw_arrow_down(c, 375, 658, 640, "son")
    draw_node(c, 315, 604, w_g, h_g, "Samudragupta", "b. c.315 – d. 375 CE", "4th C. CE", "Prayag Prashasti; Kaviraja", C_BLUE)
    
    # Branch to Chandragupta II & Ramagupta
    draw_branch_2(c, 375, 604, 235 + w_g/2, 395 + w_g/2, 586, "elder", "son")
    draw_node(c, 235, 550, w_g, h_g, "Ramagupta", "b. c.345 – d. 376 CE", "4th C. CE", "Copper coins; Devichandraguptam", C_BLUE)
    draw_node(c, 395, 550, w_g, h_g, "Chandragupta II 'Vikramaditya'", "b. c.348 – d. 415 CE", "4th–5th C. CE", "Navaratnas; Fa-Hien; Sakas", C_BLUE)
    
    # Branch from CG II to Kumaragupta I & Prabhavatigupta
    draw_branch_2(c, 395 + w_g/2, 550, 315 + w_g/2, 455 + w_g/2, 532, "son", "daughter")
    draw_node(c, 315, 496, w_g, h_g, "Kumaragupta I", "b. c.380 – d. 455 CE", "4th–5th C. CE", "Founded Nalanda Mahavihara", C_BLUE)
    draw_node(c, 455, 496, w_g, h_g, "Prabhavatigupta", "b. c.385 – d. c.445 CE", "4th–5th C. CE", "m. Rudrasena II (Vakataka Regent)", C_PURPLE)
    
    # Branch from Kumaragupta I to Skandagupta & Purugupta
    draw_branch_2(c, 315 + w_g/2, 496, 235 + w_g/2, 375 + w_g/2, 478, "son", "son")
    draw_node(c, 235, 442, w_g, h_g, "Skandagupta", "b. c.410 – d. 467 CE", "5th C. CE", "Bhitari Pillar; repulsed Hunas", C_BLUE)
    draw_node(c, 375, 442, w_g, h_g, "Purugupta", "b. c.415 – d. 473 CE", "5th C. CE", "Later Gupta succession", C_BLUE)
    
    # Later Guptas
    draw_arrow_down(c, 375 + w_g/2, 442, 424, "son")
    draw_node(c, 375, 388, w_g, h_g, "Narasimhagupta Baladitya", "b. c.450 – d. 520 CE", "5th–6th C. CE", "Defeated Huna Mihirakula", C_BLUE)
    draw_arrow_down(c, 375 + w_g/2, 388, 370, "grandson")
    draw_node(c, 375, 334, w_g, h_g, "Vishnugupta (Last)", "b. c.500 – d. c.550 CE", "6th C. CE", "Last Imperial Gupta Dinars", C_RED)

    # 2.2 Vakataka Dynasty (Left Side of Middle/Lower Page)
    draw_section_banner(c, 410, "2. Vakataka Dynasty (Deccan)", "3rd – 6th Century CE", "Pravarapura & Vatsagulma")
    w_v, h_v = 115, 35
    draw_node(c, 35, 362, w_v, h_v, "Vindhyashakti I", "b. c.220 – d. 280 CE", "3rd C. CE", "Founder; Purana praise", C_PURPLE)
    draw_arrow_down(c, 35 + w_v/2, 362, 344, "son")
    draw_node(c, 35, 308, w_v, h_v, "Pravarasena I", "b. c.250 – d. 335 CE", "3rd–4th C. CE", "Assumed 'Samrat'; 4 Ashvamedhas", C_PURPLE)
    draw_branch_2(c, 35 + w_v/2, 308, 35 + w_v/2, 160 + w_v/2, 290, "Pravarapura", "Vatsagulma")
    draw_node(c, 35, 254, w_v, h_v, "Rudrasena II", "b. c.360 – d. 390 CE", "4th C. CE", "m. Prabhavatigupta (Gupta link)", C_PURPLE)
    draw_node(c, 160, 254, w_v, h_v, "Harishena", "b. c.440 – d. 510 CE", "5th–6th C. CE", "Ajanta Rock Caves 16, 17, 19", C_PURPLE)

    # 2.3 Pushyabhuti & Maukhari Dynasty (7th C.)
    draw_section_banner(c, 230, "3. Pushyabhuti & Maukhari Dynasties", "6th – 7th Century CE", "Thanesar & Kannauj")
    w_p, h_p = 120, 35
    draw_node(c, 237.64, 182, w_p, h_p, "Prabhakaravardhana", "b. c.545 – d. 605 CE", "6th–7th C. CE", "Pushyabhuti King of Thanesar", C_GREEN)
    
    draw_branch_3(c, 297.64, 182, 85 + w_p/2, 237.64 + w_p/2, 390 + w_p/2, 164)
    draw_node(c, 85, 128, w_p, h_p, "Rajyavardhana", "b. c.582 – d. 606 CE", "6th–7th C. CE", "Slain by Shashanka of Gauda", C_GREEN)
    draw_node(c, 237.64, 128, w_p, h_p, "Harshavardhana", "b. 590 – d. 647 CE", "6th–7th C. CE", "Kannauj Capital; Xuanzang visit", C_GREEN)
    draw_node(c, 390, 128, w_p, h_p, "Rajyashri (Princess)", "b. c.592 – d. c.650 CE", "6th–7th C. CE", "m. Grahavarman Maukhari", C_TEAL)
    
    # Husband Grahavarman
    draw_arrow_down(c, 390 + w_p/2, 128, 110, "married")
    draw_node(c, 390, 74, w_p, h_p, "Grahavarman Maukhari", "b. c.580 – d. 606 CE", "6th–7th C. CE", "Maukhari King of Kannauj", C_TEAL)

    # Marriage connection between Prabhavatigupta and Rudrasena II
    c.setStrokeColor(colors.HexColor("#DC2626"))
    c.setLineWidth(0.8)
    c.setDash(2, 2)
    c.line(455, 513.5, 440, 513.5)
    c.line(440, 513.5, 440, 271.5)
    c.line(440, 271.5, 150, 271.5)
    c.setDash()
    c.setFont("Helvetica-Bold", 6)
    c.setFillColor(colors.HexColor("#DC2626"))
    c.drawString(443, 400, "Matrimonial Alliance: Guptas & Vakatakas")

    c.showPage()

    # -------------------------------------------------------------
    # PAGE 3: PENINSULAR & EARLY MEDIEVAL EMPIRES
    # -------------------------------------------------------------
    draw_header(c, "UPSC CSE: ROYAL GENEALOGICAL TREES & LINEAGES", 
                "Sheet 3: Peninsular & South Indian Dynasties (6th – 13th C. CE)", 3, total_pages)
    
    # 3.1 Badami Chalukyas
    draw_section_banner(c, 755, "1. Early Western Chalukyas of Badami", "6th – 8th Century CE", "Vatapi (Badami)")
    y_c1 = 708
    draw_node(c, x0, y_c1, w, h, "Pulakeshin I", "b. c.505 – d. 566 CE", "6th C. CE", "Founded Vatapi Fortress", C_BLUE)
    draw_node(c, x1, y_c1, w, h, "Kirtivarman I", "b. c.535 – d. 597 CE", "6th C. CE", "Expanded Konkan/Goa", C_BLUE)
    draw_node(c, x2, y_c1, w, h, "Mangalesha (Regent)", "b. c.540 – d. 610 CE", "6th–7th C. CE", "Badami Vaishnava Cave 4", C_BLUE)
    draw_node(c, x3, y_c1, w, h, "Pulakeshin II", "b. c.570 – d. 642 CE", "6th–7th C. CE", "Aihole Inscription; Harsha war", C_BLUE)
    
    for xa in [x0 + w, x1 + w, x2 + w]:
        c.setStrokeColor(colors.HexColor("#64748B")); c.setLineWidth(1)
        c.line(xa, y_c1 + h/2, xa + 25, y_c1 + h/2)
        c.setFillColor(colors.HexColor("#64748B"))
        p = c.beginPath(); p.moveTo(xa + 25, y_c1 + h/2); p.lineTo(xa + 20, y_c1 + h/2 + 2.5); p.lineTo(xa + 20, y_c1 + h/2 - 2.5); p.close()
        c.drawPath(p, fill=1, stroke=0)

    # Next generation Chalukya
    y_c2 = 660
    draw_node(c, x1, y_c2, w, h, "Vikramaditya I", "b. c.620 – d. 680 CE", "7th C. CE", "Recovered Vatapi from Pallavas", C_BLUE)
    draw_node(c, x2, y_c2, w, h, "Vikramaditya II", "b. c.685 – d. 744 CE", "7th–8th C. CE", "Virupaksha Temple (Pattadakal)", C_BLUE)
    draw_node(c, x3, y_c2, w, h, "Kirtivarman II (Last)", "b. c.720 – d. 753 CE", "8th C. CE", "Overthrown by Dantidurga", C_RED)
    
    draw_arrow_down(c, x3 + w/2, y_c1, y_c2 + h, "son")
    c.line(x1 + w, y_c2 + h/2, x2, y_c2 + h/2)
    c.line(x2 + w, y_c2 + h/2, x3, y_c2 + h/2)

    # 3.2 Pallavas of Kanchipuram
    draw_section_banner(c, 625, "2. Pallavas of Kanchipuram", "6th – 9th Century CE", "Kanchipuram & Mamallapuram")
    y_p1 = 578
    draw_node(c, x0, y_p1, w, h, "Simhavishnu", "b. c.540 – d. 600 CE", "6th C. CE", "Avanisimha; Bharavi patron", C_PURPLE)
    draw_node(c, x1, y_p1, w, h, "Mahendravarman I", "b. c.570 – d. 630 CE", "6th–7th C. CE", "Mattavilasa Prahasana", C_PURPLE)
    draw_node(c, x2, y_p1, w, h, "Narasimhavarman I", "b. c.600 – d. 668 CE", "7th C. CE", "Mahamalla; Vatapikonda", C_PURPLE)
    draw_node(c, x3, y_p1, w, h, "Rajasimha (Narasimha II)", "b. c.670 – d. 728 CE", "7th–8th C. CE", "Shore & Kailasanatha Temples", C_PURPLE)
    
    for xa in [x0 + w, x1 + w, x2 + w]:
        c.setStrokeColor(colors.HexColor("#64748B")); c.setLineWidth(1)
        c.line(xa, y_p1 + h/2, xa + 25, y_p1 + h/2)
        c.setFillColor(colors.HexColor("#64748B"))
        p = c.beginPath(); p.moveTo(xa + 25, y_p1 + h/2); p.lineTo(xa + 20, y_p1 + h/2 + 2.5); p.lineTo(xa + 20, y_p1 + h/2 - 2.5); p.close()
        c.drawPath(p, fill=1, stroke=0)

    # Conflict Indicator between Chalukyas & Pallavas
    c.setFont("Helvetica-Bold", 7)
    c.setFillColor(colors.HexColor("#DC2626"))
    c.drawCentredString(297.64, 648, "Inter-Dynastic Clashes: Pulakeshin II checks Mahendravarman I (610 CE) | Narasimhavarman I sacks Vatapi (642 CE)")

    # 3.3 Rashtrakutas of Manyakheta
    draw_section_banner(c, 540, "3. Rashtrakutas of Manyakheta", "8th – 10th Century CE", "Manyakheta (Malkhed)")
    y_r = 492
    draw_node(c, x0, y_r, w, h, "Dantidurga (Founder)", "b. c.710 – d. 756 CE", "8th C. CE", "Hiranyagarbha at Ujjain", C_GREEN)
    draw_node(c, x1, y_r, w, h, "Krishna I", "b. c.715 – d. 774 CE", "8th C. CE", "Kailasa Temple (Ellora Cave 16)", C_GREEN)
    draw_node(c, x2, y_r, w, h, "Amoghavarsha I", "b. 800 – d. 878 CE", "9th C. CE", "Kavirajamarga; 64-yr rule", C_GREEN)
    draw_node(c, x3, y_r, w, h, "Krishna III", "b. c.910 – d. 967 CE", "10th C. CE", "Battle of Takkolam (949 CE)", C_GREEN)
    
    for xa in [x0 + w, x1 + w, x2 + w]:
        c.setStrokeColor(colors.HexColor("#64748B")); c.setLineWidth(1)
        c.line(xa, y_r + h/2, xa + 25, y_r + h/2)
        c.setFillColor(colors.HexColor("#64748B"))
        p = c.beginPath(); p.moveTo(xa + 25, y_r + h/2); p.lineTo(xa + 20, y_r + h/2 + 2.5); p.lineTo(xa + 20, y_r + h/2 - 2.5); p.close()
        c.drawPath(p, fill=1, stroke=0)

    # 3.4 Imperial Cholas of Thanjavur
    draw_section_banner(c, 455, "4. Imperial Cholas of Thanjavur", "9th – 13th Century CE", "Thanjavur & Gangaikondacholapuram")
    # Tree: Vijayalaya -> Aditya I -> Parantaka I -> Rajaraja I -> Rajendra I -> Rajadhiraja I -> Kulottunga I
    y_ch1 = 405
    draw_node(c, x0, y_ch1, w, h, "Vijayalaya (Founder)", "b. c.815 – d. 871 CE", "9th C. CE", "Captured Tanjore", C_RED)
    draw_node(c, x1, y_ch1, w, h, "Aditya I", "b. c.845 – d. 907 CE", "9th–10th C. CE", "Ended Pallava Rule", C_RED)
    draw_node(c, x2, y_ch1, w, h, "Parantaka I", "b. c.875 – d. 955 CE", "9th–10th C. CE", "Uttaramerur Inscription", C_RED)
    draw_node(c, x3, y_ch1, w, h, "Rajaraja I 'The Great'", "b. 947 – d. 1014 CE", "10th–11th C. CE", "Brihadisvara Temple (1010 CE)", C_RED)
    
    for xa in [x0 + w, x1 + w, x2 + w]:
        c.setStrokeColor(colors.HexColor("#64748B")); c.setLineWidth(1)
        c.line(xa, y_ch1 + h/2, xa + 25, y_ch1 + h/2)
        c.setFillColor(colors.HexColor("#64748B"))
        p = c.beginPath(); p.moveTo(xa + 25, y_ch1 + h/2); p.lineTo(xa + 20, y_ch1 + h/2 + 2.5); p.lineTo(xa + 20, y_ch1 + h/2 - 2.5); p.close()
        c.drawPath(p, fill=1, stroke=0)

    y_ch2 = 356
    draw_node(c, x1, y_ch2, w, h, "Rajendra I", "b. 971 – d. 1044 CE", "10th–11th C. CE", "Gangaikondachola; Srivijaya", C_RED)
    draw_node(c, x2, y_ch2, w, h, "Rajadhiraja I", "b. 1018 – d. 1054 CE", "11th C. CE", "Battle of Koppam (on elephant)", C_RED)
    draw_node(c, x3, y_ch2, w, h, "Kulottunga I", "b. 1040 – d. 1120 CE", "11th–12th C. CE", "Chalukya-Chola; China trade", C_RED)
    
    draw_arrow_down(c, x3 + w/2, y_ch1, y_ch2 + h, "son")
    c.line(x1 + w, y_ch2 + h/2, x2, y_ch2 + h/2)
    c.line(x2 + w, y_ch2 + h/2, x3, y_ch2 + h/2)

    # 3.5 Tripartite Struggle & Regional Powers Summary Tree
    draw_section_banner(c, 320, "5. Tripartite Contestants & 12th-14th C. Deccan Succession", "8th – 14th Century CE", "Kannauj & Peninsular Centers")
    
    y_reg = 265
    draw_node(c, x0, y_reg, w, h, "Mihir Bhoja (Pratihara)", "b. c.816 – d. 885 CE", "9th C. CE", "Title: Adivaraha; Kannauj", C_BLUE)
    draw_node(c, x1, y_reg, w, h, "Dharmapala (Pala)", "b. c.770 – d. 810 CE", "8th–9th C. CE", "Founded Vikramashila", C_GREEN)
    draw_node(c, x2, y_reg, w, h, "Vishnuvardhana (Hoysala)", "b. c.1080 – d. 1152 CE", "11th–12th C. CE", "Belur & Halebidu Temples", C_PURPLE)
    draw_node(c, x3, y_reg, w, h, "Rani Rudramadevi", "b. c.1245 – d. 1289 CE", "13th C. CE", "Kakatiya Queen; Marco Polo", C_TEAL)

    # Bottom notes
    c.setFillColor(colors.HexColor("#F8FAFC"))
    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.roundRect(30, 42, 535.28, 205, 3, fill=1, stroke=1)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(colors.HexColor("#1E3A8A"))
    c.drawString(40, 234, "CRITICAL UPSC PRELIMS & MAINS EXAM ANCHORS:")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(colors.HexColor("#1E293B"))
    c.drawString(40, 220, "• Badami Chalukyas: Introduced Vesara style of temple architecture at Aihole, Badami, and Pattadakal (UNESCO World Heritage Site).")
    c.drawString(40, 206, "• Pallava Architecture: 4 Stages: Mahendra style (rock-cut mandapas), Mamalla style (monolithic rathas), Rajasimha (structural stone), Nandivarman.")
    c.drawString(40, 192, "• Rashtrakuta Significance: Bridge between North and South; Ellora Kailasa Temple excavated top-down out of a single basalt cliff.")
    c.drawString(40, 178, "• Chola Local Self-Government: Village autonomy divided into Ur (peasant assembly) and Sabha/Mahasabha (Brahmin assemblies).")
    c.drawString(40, 164, "• Uttaramerur Inscriptions (919 & 921 CE): Prescribe qualifications (age 35-70, owning tax-paying land, knowledge of Vedas) and disqualifications.")
    c.drawString(40, 150, "• Kudavolai Electoral System: Village wards chose representatives through pot-drawing ballots by young boys.")
    c.drawString(40, 136, "• Chola Maritime Supremacy: Bay of Bengal referred to as the 'Chola Lake'; protected Indian merchant guilds (Manigramam, Ayyavole-500).")
    c.drawString(40, 122, "• Tripartite Struggle: 200-year conflict between Gurjara-Pratiharas, Palas of Bengal, and Rashtrakutas for control of Kannauj's fertile Doab.")
    c.drawString(40, 108, "• Hoysala Art: Soapstone (chloritic schist) temples with star-shaped (stellate) ground plans, sculpted friezes, and Jagati platforms.")
    c.drawString(40, 94, "• Kakatiya Trade Charter: Motupalli Abhaya Shasana issued by Ganapatideva guaranteeing merchant safety and fixed ad valorem duties.")
    c.drawString(40, 80, "• Inscriptions to Memorize: Aihole Prashasti (Ravikirti, praises Pulakeshin II); Nasik Prashasti (Gautami Balashri); Barah Plate (Mihir Bhoja).")
    c.drawString(40, 66, "• Foreign Chroniclers: Hiuen Tsang / Xuanzang (visited Pulakeshin II, Narasimhavarman I, Harsha); Sulaiman & Al-Masudi (Rashtrakutas).")
    c.drawString(40, 52, "• Battle of Takkolam (949 CE): Rashtrakuta Krishna III killed Chola crown prince Rajaditya; halted Chola northern expansion for decades.")

    c.showPage()

    # -------------------------------------------------------------
    # PAGE 4: DELHI SULTANATE & VIJAYANAGARA EMPIRE
    # -------------------------------------------------------------
    draw_header(c, "UPSC CSE: ROYAL GENEALOGICAL TREES & LINEAGES", 
                "Sheet 4: Medieval Delhi Sultanate & Vijayanagara Empire (13th – 16th C. CE)", 4, total_pages)
    
    # 4.1 Delhi Sultanate Dynasties
    draw_section_banner(c, 755, "1. Delhi Sultanate: Key Rulers & Dynasties", "13th – 16th Century CE", "Delhi (Qila Rai Pithora, Siri, Tughlaqabad)")
    
    # Mamluk / Slave
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(colors.HexColor("#1D4ED8"))
    c.drawString(35, 742, "A. MAMLUK / SLAVE DYNASTY (1206–1290 CE)")
    y_mam = 700
    draw_node(c, x0, y_mam, w, h, "Qutb-ud-din Aibak", "b. 1150 – d. 1210 CE", "12th–13th C. CE", "Lakhbaksh; Qutb Minar start", C_BLUE)
    draw_node(c, x1, y_mam, w, h, "Shams-ud-din Iltutmish", "b. c.1175 – d. 1236 CE", "12th–13th C. CE", "Iqta; Tanka/Jital; Chahalgani", C_BLUE)
    draw_node(c, x2, y_mam, w, h, "Razia Sultana", "b. 1205 – d. 1240 CE", "13th C. CE", "First Female Delhi Monarch", C_BLUE)
    draw_node(c, x3, y_mam, w, h, "Ghiyas-ud-din Balban", "b. 1200 – d. 1287 CE", "13th C. CE", "Blood & Iron; Sijda; Paibos", C_BLUE)
    
    for xa in [x0 + w, x1 + w, x2 + w]:
        c.setStrokeColor(colors.HexColor("#64748B")); c.setLineWidth(1)
        c.line(xa, y_mam + h/2, xa + 25, y_mam + h/2)
        c.setFillColor(colors.HexColor("#64748B"))
        p = c.beginPath(); p.moveTo(xa + 25, y_mam + h/2); p.lineTo(xa + 20, y_mam + h/2 + 2.5); p.lineTo(xa + 20, y_mam + h/2 - 2.5); p.close()
        c.drawPath(p, fill=1, stroke=0)

    # Khalji & Tughlaq
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(colors.HexColor("#DC2626"))
    c.drawString(35, 686, "B. KHALJI DYNASTY (1290–1320 CE) & TUGHLAQ DYNASTY (1320–1414 CE)")
    y_kt = 644
    draw_node(c, x0, y_kt, w, h, "Jalal-ud-din Khalji", "b. 1220 – d. 1296 CE", "13th C. CE", "Clemency Policy; Founder", C_RED)
    draw_node(c, x1, y_kt, w, h, "Ala-ud-din Khalji", "b. 1266 – d. 1316 CE", "13th–14th C. CE", "Market Control; Dagh/Chehra", C_RED)
    draw_node(c, x2, y_kt, w, h, "Muhammad bin Tughlaq", "b. 1290 – d. 1351 CE", "13th–14th C. CE", "Token Currency; Diwan-i-Kohi", C_PURPLE)
    draw_node(c, x3, y_kt, w, h, "Firoz Shah Tughlaq", "b. 1309 – d. 1388 CE", "14th C. CE", "Canals; Diwan-i-Bandagan", C_PURPLE)
    
    for xa in [x0 + w, x1 + w, x2 + w]:
        c.setStrokeColor(colors.HexColor("#64748B")); c.setLineWidth(1)
        c.line(xa, y_kt + h/2, xa + 25, y_kt + h/2)
        c.setFillColor(colors.HexColor("#64748B"))
        p = c.beginPath(); p.moveTo(xa + 25, y_kt + h/2); p.lineTo(xa + 20, y_kt + h/2 + 2.5); p.lineTo(xa + 20, y_kt + h/2 - 2.5); p.close()
        c.drawPath(p, fill=1, stroke=0)

    # Lodi Dynasty
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(colors.HexColor("#047857"))
    c.drawString(35, 630, "C. LODI AFGHAN DYNASTY (1451–1526 CE)")
    y_lod = 588
    draw_node(c, x0, y_lod, w, h, "Bahlul Lodi", "b. 1401 – d. 1489 CE", "15th C. CE", "First Afghan Sultanate", C_GREEN)
    draw_node(c, x1, y_lod, w, h, "Sikandar Lodi", "b. 1458 – d. 1517 CE", "15th–16th C. CE", "Founded Agra 1504; Gaz unit", C_GREEN)
    draw_node(c, x2, y_lod, w, h, "Ibrahim Lodi (Last)", "b. 1480 – d. 1526 CE", "15th–16th C. CE", "1st Battle of Panipat (1526)", C_RED)
    
    for xa in [x0 + w, x1 + w]:
        c.setStrokeColor(colors.HexColor("#64748B")); c.setLineWidth(1)
        c.line(xa, y_lod + h/2, xa + 25, y_lod + h/2)
        c.setFillColor(colors.HexColor("#64748B"))
        p = c.beginPath(); p.moveTo(xa + 25, y_lod + h/2); p.lineTo(xa + 20, y_lod + h/2 + 2.5); p.lineTo(xa + 20, y_lod + h/2 - 2.5); p.close()
        c.drawPath(p, fill=1, stroke=0)

    # 4.2 Vijayanagara Empire (4 Dynasties)
    draw_section_banner(c, 550, "2. Vijayanagara Empire: Four Royal Dynasties", "14th – 17th Century CE", "Vijayanagara (Hampi) & Penukonda")
    
    # Sangama
    c.setFont("Helvetica-Bold", 8); c.setFillColor(colors.HexColor("#1D4ED8"))
    c.drawString(35, 537, "A. SANGAMA DYNASTY (1336–1485 CE)")
    y_sang = 495
    draw_node(c, x0, y_sang, w, h, "Harihara I & Bukka I", "b. c.1300 – d. 1377 CE", "14th C. CE", "Guided by Sage Vidyaranya", C_BLUE)
    draw_node(c, x1, y_sang, w, h, "Deva Raya I", "b. c.1360 – d. 1422 CE", "14th–15th C. CE", "Tungabhadra Dam; Nicolo Conti", C_BLUE)
    draw_node(c, x2, y_sang, w, h, "Deva Raya II", "b. c.1405 – d. 1446 CE", "15th C. CE", "Gajabetekara; Abdur Razzaq", C_BLUE)
    draw_node(c, x3, y_sang, w, h, "Saluva Narasimha", "b. c.1435 – d. 1491 CE", "15th C. CE", "1st Usurpation (Saluva Dyn.)", C_PURPLE)
    
    for xa in [x0 + w, x1 + w, x2 + w]:
        c.setStrokeColor(colors.HexColor("#64748B")); c.setLineWidth(1)
        c.line(xa, y_sang + h/2, xa + 25, y_sang + h/2)
        c.setFillColor(colors.HexColor("#64748B"))
        p = c.beginPath(); p.moveTo(xa + 25, y_sang + h/2); p.lineTo(xa + 20, y_sang + h/2 + 2.5); p.lineTo(xa + 20, y_sang + h/2 - 2.5); p.close()
        c.drawPath(p, fill=1, stroke=0)

    # Tuluva Dynasty
    c.setFont("Helvetica-Bold", 8); c.setFillColor(colors.HexColor("#B45309"))
    c.drawString(35, 481, "B. TULUVA DYNASTY (1505–1570 CE) — THE GOLDEN AGE")
    y_tul = 439
    draw_node(c, x0, y_tul, w, h, "Vira Narasimha", "b. c.1475 – d. 1509 CE", "15th–16th C. CE", "2nd Usurpation; Tuluva Founder", C_AMBER)
    draw_node(c, x1, y_tul, w, h, "Krishnadevaraya", "b. 1471 – d. 1529 CE", "15th–16th C. CE", "Amuktamalyada; Ashtadiggajas", C_AMBER)
    draw_node(c, x2, y_tul, w, h, "Achyuta Deva Raya", "b. c.1485 – d. 1542 CE", "16th C. CE", "Fernao Nuniz visit", C_AMBER)
    draw_node(c, x3, y_tul, w, h, "Rama Raya (Regent)", "b. 1484 – d. 1565 CE", "16th C. CE", "Battle of Talikota (1565)", C_RED)
    
    for xa in [x0 + w, x1 + w, x2 + w]:
        c.setStrokeColor(colors.HexColor("#64748B")); c.setLineWidth(1)
        c.line(xa, y_tul + h/2, xa + 25, y_tul + h/2)
        c.setFillColor(colors.HexColor("#64748B"))
        p = c.beginPath(); p.moveTo(xa + 25, y_tul + h/2); p.lineTo(xa + 20, y_tul + h/2 + 2.5); p.lineTo(xa + 20, y_tul + h/2 - 2.5); p.close()
        c.drawPath(p, fill=1, stroke=0)

    # Aravidu Dynasty
    c.setFont("Helvetica-Bold", 8); c.setFillColor(colors.HexColor("#7C3AED"))
    c.drawString(35, 425, "C. ARAVIDU DYNASTY (1570–1646 CE) — POST-TALIKOTA PHASE")
    y_ara = 383
    draw_node(c, x1, y_ara, w, h, "Tirumala Raya", "b. c.1510 – d. 1578 CE", "16th C. CE", "Founded Aravidu at Penukonda", C_PURPLE)
    draw_node(c, x2, y_ara, w, h, "Venkata II", "b. c.1555 – d. 1614 CE", "16th–17th C. CE", "Chandragiri Capital; Dutch ties", C_PURPLE)
    draw_node(c, x3, y_ara, w, h, "Sriranga III (Last)", "b. c.1610 – d. 1678 CE", "17th C. CE", "Annexed by Bijapur & Golconda", C_RED)
    
    c.line(x1 + w, y_ara + h/2, x2, y_ara + h/2)
    c.line(x2 + w, y_ara + h/2, x3, y_ara + h/2)

    # Bottom notes
    c.setFillColor(colors.HexColor("#F8FAFC"))
    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.roundRect(30, 42, 535.28, 325, 3, fill=1, stroke=1)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(colors.HexColor("#1E3A8A"))
    c.drawString(40, 353, "HIGH-YIELD SULTANATE & VIJAYANAGARA COMPARISON FOR UPSC:")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(colors.HexColor("#1E293B"))
    c.drawString(40, 339, "• Iqta System: Land grant given to military officers (Iqtadars/Muqtis) for collection of revenue and maintenance of troops; non-hereditary under early sultans.")
    c.drawString(40, 325, "• Alauddin Khalji's Market Control: Set up four distinct markets in Delhi: Grain (Mandi), Cloth/Sugar/Dry Fruits (Sarai-i-Adl), Horses/Slaves/Cattle, and Misc.")
    c.drawString(40, 311, "• Officials under Alauddin: Shahna-i-Mandi (market superintendent), Barids (intelligence officers), and Munhiyans (secret spies).")
    c.drawString(40, 297, "• Muhammad bin Tughlaq's Reforms: Created Diwan-i-Amir-Kohi to bring uncultivated land under farming; provided Sondhar agricultural loans.")
    c.drawString(40, 283, "• Firoz Shah Tughlaq: Built over 300 towns (Jaunpur, Firozabad, Hissar, Fatehabad); repaired Qutb Minar; collected Jizya as separate tax from non-Muslims.")
    c.drawString(40, 269, "• Delhi Sultanate Departments: Diwan-i-Wizarat (Finance), Diwan-i-Arz (Military), Diwan-i-Insha (Correspondence), Diwan-i-Risasat (Foreign Affairs).")
    c.drawString(40, 255, "• Vijayanagara Nayankara System: Military governors (Amaranāyakas) held amaram territories; provided designated contingents of infantry/cavalry/elephants.")
    c.drawString(40, 241, "• Ayagar Village System: Village community administered by a council of 12 hereditary officials (Karnam/accountant, Talayari/policeman) paid by tax-free land (manya).")
    c.drawString(40, 227, "• Krishnadevaraya's Literature: Wrote 'Amuktamalyada' in Telugu (portraying Andal's devotion) and 'Jambavati Kalyanam' in Sanskrit.")
    c.drawString(40, 213, "• Ashtadiggajas (Eight Literary Giants): Allasani Peddana (title Andhrakavita Pitamaha, author of Manu Charitramu), Tenali Ramakrishna, Nandi Timmana, etc.")
    c.drawString(40, 199, "• Vijayanagara Architecture: Monolithic pillars, mythical beasts (Yali), Kalyana Mandapas with sculpted stone pillars, Raya Gopurams.")
    c.drawString(40, 185, "• Foreign Visitors to Vijayanagara: Nicolo de Conti (Italian, 1420), Abdur Razzaq (Persian, 1443), Duarte Barbosa & Domingo Paes (Portuguese, 1518-1520), Fernao Nuniz (1535).")
    c.drawString(40, 171, "• Battle of Talikota (Jan 23, 1565): Combined coalition of 4 Deccan Sultanates (Bijapur, Golconda, Ahmadnagar, Bidar; Berar stayed away); sacked Hampi.")
    c.drawString(40, 157, "• Bahmani Sultanate Disintegration: Fractured into 5 independent sultanates: Nizam Shahi (Ahmadnagar), Adil Shahi (Bijapur), Qutb Shahi (Golconda), Imad Shahi (Berar), Barid Shahi (Bidar).")
    c.drawString(40, 143, "• Coins: Vijayanagara gold 'Varaha' / 'Pagoda' (embossed with deities Vishnu, Shiva-Parvati) vs Sultanate silver 'Tanka' and copper 'Jital'.")
    c.drawString(40, 129, "• Women's Position in Vijayanagara: Chronicler Nuniz noted that women served as royal bodyguards, wrestlers, astrologers, accountants, and musicians.")
    c.drawString(40, 115, "• Sikandar Lodi's Agrarian Measure: Introduced Gaz-i-Sikandari (measuring rod of 39 digits / 32 inches) used until Akbar's time.")
    c.drawString(40, 101, "• First Battle of Panipat (April 21, 1526): Babur utilized field artillery (Topkhana) and Tulghuma flanking strategy to defeat Ibrahim Lodi.")
    c.drawString(40, 87, "• Water Management: Krishnadevaraya built the great dam at Korragal and the Basavanna canal to supply water to Vijayanagara capital.")
    c.drawString(40, 73, "• Social Groups: Idangai (Left-hand castes - artisans/traders) and Valangai (Right-hand castes - agriculturists/landlords) tensions in South India.")
    c.drawString(40, 59, "• Administrative Divisions (Vijayanagara): Rajya/Mandala (Province) -> Kottam/Valanadu (District) -> Nadu (Sub-district) -> Grama (Village).")

    c.showPage()

    # -------------------------------------------------------------
    # PAGE 5: IMPERIAL MUGHALS & MARATHAS
    # -------------------------------------------------------------
    draw_header(c, "UPSC CSE: ROYAL GENEALOGICAL TREES & LINEAGES", 
                "Sheet 5: The Imperial Mughals & Marathas (Chhatrapatis & Peshwas)", 5, total_pages)
    
    # 5.1 Imperial Mughal Dynasty
    draw_section_banner(c, 755, "1. Imperial Mughal Dynasty", "16th – 19th Century CE", "Agra, Fatehpur Sikri, Delhi (Shahjahanabad)")
    
    # Vertical tree down the left-to-middle: Babur -> Humayun -> Akbar -> Jahangir -> Shah Jahan -> Aurangzeb
    w_mgh, h_mgh = 125, 34
    x_m1 = 35
    draw_node(c, x_m1, 712, w_mgh, h_mgh, "Zahir-ud-din Babur", "b. 1483 – d. 1530 CE", "15th–16th C. CE", "Tuzuk-i-Baburi; Panipat 1526", C_BLUE)
    draw_arrow_down(c, x_m1 + w_mgh/2, 712, 694, "son")
    draw_node(c, x_m1, 660, w_mgh, h_mgh, "Nasir-ud-din Humayun", "b. 1508 – d. 1556 CE", "16th C. CE", "Dinpanah; ousted by Sher Shah", C_BLUE)
    
    # Sur Interregnum alongside Humayun
    draw_node(c, 175, 660, w_mgh, h_mgh, "Sher Shah Suri (Sur Dyn.)", "b. 1472 – d. 1545 CE", "15th–16th C. CE", "Rupiya; Grand Trunk Road", C_RED)
    c.setStrokeColor(colors.HexColor("#DC2626")); c.setLineWidth(0.8); c.setDash(2, 2)
    c.line(x_m1 + w_mgh, 677, 175, 677)
    c.setDash()
    
    draw_arrow_down(c, x_m1 + w_mgh/2, 660, 642, "son")
    draw_node(c, x_m1, 608, w_mgh, h_mgh, "Jalal-ud-din Akbar", "b. 1542 – d. 1605 CE", "16th–17th C. CE", "Mansabdari; Dahsala; Sulh-i-Kul", C_BLUE)
    draw_arrow_down(c, x_m1 + w_mgh/2, 608, 590, "son")
    draw_node(c, x_m1, 556, w_mgh, h_mgh, "Nur-ud-din Jahangir", "b. 1569 – d. 1627 CE", "16th–17th C. CE", "Chain of Justice; Paintings zenith", C_BLUE)
    draw_arrow_down(c, x_m1 + w_mgh/2, 556, 538, "son")
    draw_node(c, x_m1, 504, w_mgh, h_mgh, "Shahab-ud-din Shah Jahan", "b. 1592 – d. 1666 CE", "16th–17th C. CE", "Taj Mahal; Red Fort; Architecture", C_BLUE)
    draw_arrow_down(c, x_m1 + w_mgh/2, 504, 486, "son")
    draw_node(c, x_m1, 452, w_mgh, h_mgh, "Muhi-ud-din Aurangzeb", "b. 1618 – d. 1707 CE", "17th–18th C. CE", "Alamgir; Fatawa; Jizya renewed", C_BLUE)
    
    # Later Mughals (Horizontal chain from Aurangzeb)
    draw_arrow_down(c, x_m1 + w_mgh, 469, 175) # rightward line
    c.line(x_m1 + w_mgh, 469, 175, 469)
    draw_node(c, 175, 452, w_mgh, h_mgh, "Bahadur Shah I", "b. 1643 – d. 1712 CE", "17th–18th C. CE", "Shah-i-Bekhabar", C_BLUE)
    
    c.line(175 + w_mgh, 469, 315, 469)
    draw_node(c, 315, 452, w_mgh, h_mgh, "Muhammad Shah 'Rangeela'", "b. 1702 – d. 1748 CE", "18th C. CE", "Nadir Shah Invasion 1739", C_BLUE)
    
    c.line(315 + w_mgh, 469, 445, 469)
    draw_node(c, 445, 452, 115, h_mgh, "Bahadur Shah II 'Zafar'", "b. 1775 – d. 1862 CE", "18th–19th C. CE", "1857 Revolt; Exiled to Burma", C_RED)

    # 5.2 Maratha Empire: House of Shivaji Maharaj
    draw_section_banner(c, 420, "2. Maratha Empire: Royal House of Bhonsle (Chhatrapatis)", "17th – 18th Century CE", "Raigad & Satara")
    y_mar = 368
    draw_node(c, x0, y_mar, w, h, "Shahaji Bhonsle", "b. 1594 – d. 1664 CE", "16th–17th C. CE", "Jagirdar of Pune & Supa", C_GREEN)
    draw_node(c, x1, y_mar, w, h, "Shivaji Maharaj", "b. 1630 – d. 1680 CE", "17th C. CE", "Coronation 1674; Ashtapradhan", C_GREEN)
    draw_node(c, x2, y_mar, w, h, "Chhatrapati Sambhaji", "b. 1657 – d. 1689 CE", "17th C. CE", "Executed by Aurangzeb", C_GREEN)
    draw_node(c, x3, y_mar, w, h, "Chhatrapati Shahu I", "b. 1682 – d. 1749 CE", "17th–18th C. CE", "Appointed Peshwa Balaji Vishwanath", C_GREEN)
    
    for xa in [x0 + w, x1 + w, x2 + w]:
        c.setStrokeColor(colors.HexColor("#64748B")); c.setLineWidth(1)
        c.line(xa, y_mar + h/2, xa + 25, y_mar + h/2)
        c.setFillColor(colors.HexColor("#64748B"))
        p = c.beginPath(); p.moveTo(xa + 25, y_mar + h/2); p.lineTo(xa + 20, y_mar + h/2 + 2.5); p.lineTo(xa + 20, y_mar + h/2 - 2.5); p.close()
        c.drawPath(p, fill=1, stroke=0)

    # Tarabai collateral branch
    draw_node(c, x2, 320, w, h, "Maharani Tarabai", "b. 1675 – d. 1761 CE", "17th–18th C. CE", "Kolhapur Branch; War of Succession", C_PURPLE)
    c.setStrokeColor(colors.HexColor("#64748B")); c.setLineWidth(0.8); c.setDash(1, 2)
    c.line(x2 + w/2, y_mar, x2 + w/2, 320 + h)
    c.setDash()

    # 5.3 Hereditary Peshwas of Pune
    draw_section_banner(c, 288, "3. Hereditary Bhat Peshwas of Pune (De Facto Rulers)", "18th – 19th Century CE", "Shaniwar Wada (Pune)")
    y_pes1 = 238
    draw_node(c, x0, y_pes1, w, h, "Balaji Vishwanath", "b. 1662 – d. 1720 CE", "17th–18th C. CE", "Hereditary Peshwaship; 1719 Treaty", C_AMBER)
    draw_node(c, x1, y_pes1, w, h, "Baji Rao I", "b. 1700 – d. 1740 CE", "18th C. CE", "Hindu-Pad-Padshahi; Palkhed 1728", C_AMBER)
    draw_node(c, x2, y_pes1, w, h, "Balaji Baji Rao (Nana)", "b. 1720 – d. 1761 CE", "18th C. CE", "Sangola Agreement; 3rd Panipat", C_AMBER)
    draw_node(c, x3, y_pes1, w, h, "Madhavrao I", "b. 1745 – d. 1772 CE", "18th C. CE", "Restored Maratha Superiority", C_AMBER)
    
    for xa in [x0 + w, x1 + w, x2 + w]:
        c.setStrokeColor(colors.HexColor("#64748B")); c.setLineWidth(1)
        c.line(xa, y_pes1 + h/2, xa + 25, y_pes1 + h/2)
        c.setFillColor(colors.HexColor("#64748B"))
        p = c.beginPath(); p.moveTo(xa + 25, y_pes1 + h/2); p.lineTo(xa + 20, y_pes1 + h/2 + 2.5); p.lineTo(xa + 20, y_pes1 + h/2 - 2.5); p.close()
        c.drawPath(p, fill=1, stroke=0)

    # Last Peshwa Baji Rao II
    draw_arrow_down(c, x3 + w/2, y_pes1, 220, "lineage")
    draw_node(c, x3, 172, w, h, "Baji Rao II (Last)", "b. 1775 – d. 1851 CE", "18th–19th C. CE", "Treaty of Bassein; 3rd Maratha War", C_RED)

    # Bottom notes
    c.setFillColor(colors.HexColor("#F8FAFC"))
    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.roundRect(30, 42, 535.28, 118, 3, fill=1, stroke=1)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(colors.HexColor("#1E3A8A"))
    c.drawString(40, 148, "ESSENTIAL MUGHAL & MARATHA UPSC PRELIMS/MAINS SYNTHESIS:")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(colors.HexColor("#1E293B"))
    c.drawString(40, 134, "• Mansabdari System: Institutionalized by Akbar; dual rank of Zat (personal status/salary) and Sawar (number of cavalrymen maintained).")
    c.drawString(40, 121, "• Dahsala Land Revenue (Todar Mal's Bandobast): Average produce of previous 10 years calculated; state share fixed at 1/3rd in cash.")
    c.drawString(40, 108, "• Shivaji's Ashtapradhan: Peshwa (Prime Minister), Amatya (Finance), Mantri (Intelligence), Sachiv (Royal decrees), Sumant (Foreign),")
    c.drawString(40, 95, "  Senapati (Military commander), Panditrao (Charities), Nyayadhish (Chief Justice). All except Panditrao & Nyayadhish led military commands.")
    c.drawString(40, 82, "• Maratha Taxation: Chauth (1/4th of revenue paid to avert Maratha raids) and Sardeshmukhi (additional 10% levy claimed as hereditary overlord).")
    c.drawString(40, 69, "• Sangola Agreement (1750): Chhatrapati Ramraja formalized the Peshwa as the supreme de facto executive head of the Maratha Confederacy.")
    c.drawString(40, 56, "• Third Battle of Panipat (Jan 14, 1761): Ahmad Shah Abdali crushed the Maratha forces under Sadashivrao Bhau; shattered dream of unified Maratha rule.")

    c.showPage()
    c.save()
    print(f"Successfully generated {filename}")

if __name__ == "__main__":
    out_pdf = "/data/data/com.termux/files/home/sahacit/lineages/UPSC_History_Family_Trees.pdf"
    build_pdf(out_pdf)
