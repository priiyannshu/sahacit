import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from clean_tree_primitives import (
    draw_cut_card, draw_person_node, draw_arrow_down, 
    draw_arrow_right, draw_arrow_left, draw_fork_2, draw_fork_3,
    C_NAVY, C_RED, C_GREEN, C_PURPLE, C_TEAL, C_ORANGE, C_BLUE, C_ARROW
)

def create_clean_pdf(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    # Page dimensions: 595.28 x 841.89
    
    # =========================================================================
    # PAGE 1: MAGADHA & IMPERIAL MAURYAS
    # =========================================================================
    c.setFillColor(colors.white)
    c.rect(0, 0, 595.28, 841.89, fill=1, stroke=0)
    
    # Card 1: Haryanka Dynasty
    draw_cut_card(c, 25, 735, 545, 80, "Haryanka Dynasty (Magadha)", "6th – 5th Century BCE")
    w_h, h_h = 112, 34
    draw_person_node(c, 40, 746, w_h, h_h, "Bimbisara", "b. c.558 – d. 492 BCE", "6th–5th C. BCE • Founder", C_NAVY)
    draw_arrow_right(c, 40 + w_h, 172, 746 + h_h/2)
    draw_person_node(c, 172, 746, w_h, h_h, "Ajatashatru", "b. c.512 – d. 460 BCE", "5th C. BCE • Son", C_NAVY)
    draw_arrow_right(c, 172 + w_h, 304, 746 + h_h/2)
    draw_person_node(c, 304, 746, w_h, h_h, "Udayin", "b. c.480 – d. 444 BCE", "5th C. BCE • Son", C_NAVY)
    draw_arrow_right(c, 304 + w_h, 436, 746 + h_h/2)
    draw_person_node(c, 436, 746, w_h, h_h, "Nagadasaka", "b. c.450 – d. 413 BCE", "5th C. BCE • Last", C_RED)
    
    # Card 2: Shishunaga & Nanda Dynasties
    draw_cut_card(c, 25, 635, 545, 85, "Shishunaga & Nanda Dynasties", "5th – 4th Century BCE")
    draw_person_node(c, 40, 647, w_h, h_h, "Shishunaga", "b. c.440 – d. 395 BCE", "5th–4th C. BCE • Founder", C_PURPLE)
    draw_arrow_right(c, 40 + w_h, 172, 647 + h_h/2)
    draw_person_node(c, 172, 647, w_h, h_h, "Kalashoka", "b. c.415 – d. 367 BCE", "4th C. BCE • Son", C_PURPLE)
    draw_arrow_right(c, 172 + w_h, 304, 647 + h_h/2)
    draw_person_node(c, 304, 647, w_h, h_h, "Mahapadma Nanda", "b. c.400 – d. 345 BCE", "4th C. BCE • Usurper", C_ORANGE)
    draw_arrow_right(c, 304 + w_h, 436, 647 + h_h/2)
    draw_person_node(c, 436, 647, w_h, h_h, "Dhana Nanda", "b. c.360 – d. 321 BCE", "4th C. BCE • Last", C_RED)
    
    # Card 3: Imperial Mauryan Dynasty
    draw_cut_card(c, 25, 25, 545, 595, "Imperial Mauryan Dynasty", "4th – 2nd Century BCE")
    
    w_m, h_m = 140, 36
    cx_m = 297.64
    
    # Level 1: Chandragupta Maurya
    draw_person_node(c, cx_m - w_m/2, 525, w_m, h_m, "Chandragupta Maurya", "b. 340 – d. 297 BCE", "4th–3rd C. BCE • Founder", C_NAVY)
    
    # Level 2: Bindusara
    draw_arrow_down(c, cx_m, 525, 485)
    draw_person_node(c, cx_m - w_m/2, 445, w_m, h_m, "Bindusara Amitraghata", "b. c.320 – d. 273 BCE", "4th–3rd C. BCE • Son", C_NAVY)
    
    # Level 3: Ashoka the Great
    draw_arrow_down(c, cx_m, 445, 405)
    draw_person_node(c, cx_m - w_m/2, 365, w_m, h_m, "Ashoka the Great", "b. 304 – d. 232 BCE", "4th–3rd C. BCE • Son", C_NAVY)
    
    # Level 4: 3 branches from Ashoka (Kunala, Mahendra/Sanghamitta, Tivara)
    x_k = 150
    x_ms = 297.64
    x_t = 450
    draw_fork_3(c, cx_m, 365, x_k, x_ms, x_t, 315)
    draw_person_node(c, x_k - 65, 275, 130, h_m, "Prince Kunala", "b. c.265 – d. c.220 BCE", "3rd C. BCE • Son & Viceroy", C_NAVY)
    draw_person_node(c, x_ms - 65, 275, 130, h_m, "Mahendra & Sanghamitta", "b. c.285 – d. c.225 BCE", "3rd C. BCE • Envoys to Ceylon", C_TEAL)
    draw_person_node(c, x_t - 65, 275, 130, h_m, "Prince Tivara", "b. c.275 – d. c.230 BCE", "3rd C. BCE • Son of Karuvaki", C_NAVY)
    
    # Level 5: From Kunala down to Dasharatha & Samprati
    x_dash = 90
    x_samp = 210
    draw_fork_2(c, x_k, 275, x_dash, x_samp, 225)
    draw_person_node(c, x_dash - 55, 185, 110, h_m, "Dasharatha Maurya", "b. c.252 – d. 224 BCE", "3rd C. BCE • Grandson", C_NAVY)
    draw_person_node(c, x_samp - 55, 185, 110, h_m, "Samprati Maurya", "b. c.245 – d. 215 BCE", "3rd C. BCE • Grandson", C_NAVY)
    
    # Level 6: From Samprati down to Brihadratha
    draw_arrow_down(c, x_samp, 185, 135)
    draw_person_node(c, x_samp - 65, 95, 130, h_m, "Brihadratha (Last)", "b. c.220 – d. 185 BCE", "3rd–2nd C. BCE • Final Emperor", C_RED)
    
    c.showPage()
    
    # =========================================================================
    # PAGE 2: SHUNGA/KANVA, SATAVAHANA & IMPERIAL GUPTAS
    # =========================================================================
    c.setFillColor(colors.white)
    c.rect(0, 0, 595.28, 841.89, fill=1, stroke=0)
    
    # Card 1: Shunga & Kanva Dynasties
    draw_cut_card(c, 25, 700, 545, 120, "Shunga & Kanva Dynasties", "2nd – 1st Century BCE")
    # Row 1: Shunga
    draw_person_node(c, 40, 750, w_h, h_h, "Pushyamitra Shunga", "b. c.230 – d. 151 BCE", "3rd–2nd C. BCE • Founder", C_GREEN)
    draw_arrow_right(c, 40 + w_h, 172, 750 + h_h/2)
    draw_person_node(c, 172, 750, w_h, h_h, "Agnimitra", "b. c.195 – d. 141 BCE", "2nd C. BCE • Son", C_GREEN)
    draw_arrow_right(c, 172 + w_h, 304, 750 + h_h/2)
    draw_person_node(c, 304, 750, w_h, h_h, "Bhagabhadra", "b. c.140 – d. 83 BCE", "2nd–1st C. BCE • King", C_GREEN)
    draw_arrow_right(c, 304 + w_h, 436, 750 + h_h/2)
    draw_person_node(c, 436, 750, w_h, h_h, "Devabhuti", "b. c.105 – d. 73 BCE", "2nd–1st C. BCE • Last", C_RED)
    
    # Row 2: Kanva (overthrew Shunga)
    draw_person_node(c, 304, 708, w_h, h_h, "Vasudeva Kanva", "b. c.115 – d. 66 BCE", "2nd–1st C. BCE • Usurper", C_PURPLE)
    draw_arrow_right(c, 304 + w_h, 436, 708 + h_h/2)
    draw_person_node(c, 436, 708, w_h, h_h, "Susharman", "b. c.65 – d. 28 BCE", "1st C. BCE • Last Kanva", C_RED)
    
    # Card 2: Satavahana Dynasty
    draw_cut_card(c, 25, 555, 545, 135, "Satavahana Dynasty (Andhras)", "1st Century BCE – 3rd Century CE")
    w_sat = 150
    draw_person_node(c, 45, 615, w_sat, h_h, "Simuka", "b. c.120 – d. 70 BCE", "1st C. BCE • Founder", C_TEAL)
    draw_arrow_right(c, 45 + w_sat, 225, 615 + h_h/2)
    draw_person_node(c, 225, 615, w_sat, h_h, "Satakarni I", "b. c.95 – d. 40 BCE", "1st C. BCE • Great King", C_TEAL)
    draw_arrow_right(c, 225 + w_sat, 405, 615 + h_h/2)
    draw_person_node(c, 405, 615, w_sat, h_h, "Hala", "b. c.10 BCE – d. 45 CE", "1st C. CE • Poet King", C_TEAL)
    
    draw_person_node(c, 45, 565, w_sat, h_h, "Gautamiputra Satakarni", "b. c.60 – d. 130 CE", "1st–2nd C. CE • Ekabrahmana", C_TEAL)
    draw_arrow_right(c, 45 + w_sat, 225, 565 + h_h/2)
    draw_person_node(c, 225, 565, w_sat, h_h, "Vashishtiputra Pulumayi", "b. c.90 – d. 154 CE", "2nd C. CE • Son", C_TEAL)
    draw_arrow_right(c, 225 + w_sat, 405, 565 + h_h/2)
    draw_person_node(c, 405, 565, w_sat, h_h, "Yajna Sri Satakarni", "b. c.135 – d. 194 CE", "2nd C. CE • Maritime King", C_TEAL)
    
    # Card 3: Imperial Gupta Dynasty (Spaced evenly across 520 pt!)
    draw_cut_card(c, 25, 25, 545, 520, "Imperial Gupta Dynasty", "4th – 6th Century CE")
    w_gp = 135
    
    # Level 1: Sri Gupta -> Ghatotkacha
    draw_person_node(c, 155, 468, w_gp, h_m, "Sri Gupta", "b. c.240 – d. c.280 CE", "3rd C. CE • Founder", C_NAVY)
    draw_arrow_right(c, 155 + w_gp, 310, 468 + h_m/2)
    draw_person_node(c, 310, 468, w_gp, h_m, "Ghatotkacha", "b. c.265 – d. 319 CE", "3rd–4th C. CE • Maharaja", C_NAVY)
    
    # Level 2: Chandragupta I
    draw_arrow_down(c, 310 + w_gp/2, 468, 442)
    draw_person_node(c, 230, 406, w_gp, h_m, "Chandragupta I", "b. c.285 – d. 335 CE", "3rd–4th C. CE • Maharajadhiraja", C_NAVY)
    
    # Level 3: Samudragupta
    draw_arrow_down(c, 230 + w_gp/2, 406, 380)
    draw_person_node(c, 230, 344, w_gp, h_m, "Samudragupta", "b. c.315 – d. 375 CE", "4th C. CE • Kaviraja", C_NAVY)
    
    # Level 4: Ramagupta & Chandragupta II
    x_rg = 140
    x_cg2 = 360
    draw_fork_2(c, 230 + w_gp/2, 344, x_rg, x_cg2, 318)
    draw_person_node(c, x_rg - w_gp/2, 282, w_gp, h_m, "Ramagupta", "b. c.345 – d. 376 CE", "4th C. CE • Elder Son", C_NAVY)
    draw_person_node(c, x_cg2 - w_gp/2, 282, w_gp, h_m, "Chandragupta II 'Vikramaditya'", "b. c.348 – d. 415 CE", "4th–5th C. CE • Navaratnas", C_NAVY)
    
    # Level 5: Kumaragupta I & Prabhavatigupta
    x_kg1 = 260
    x_pb = 440
    draw_fork_2(c, x_cg2, 282, x_kg1, x_pb, 256)
    draw_person_node(c, x_kg1 - w_gp/2, 220, w_gp, h_m, "Kumaragupta I", "b. c.380 – d. 455 CE", "4th–5th C. CE • Nalanda Founder", C_NAVY)
    draw_person_node(c, x_pb - 60, 220, 120, h_m, "Prabhavatigupta", "b. c.385 – d. c.445 CE", "4th–5th C. CE • Vakataka Queen", C_PURPLE)
    
    # Level 6: Skandagupta & Purugupta
    x_sk = 160
    x_pu = 360
    draw_fork_2(c, x_kg1, 220, x_sk, x_pu, 194)
    draw_person_node(c, x_sk - w_gp/2, 158, w_gp, h_m, "Skandagupta", "b. c.410 – d. 467 CE", "5th C. CE • Repulsed Hunas", C_NAVY)
    draw_person_node(c, x_pu - w_gp/2, 158, w_gp, h_m, "Purugupta", "b. c.415 – d. 473 CE", "5th C. CE • Brother", C_NAVY)
    
    # Level 7: Narasimhagupta Baladitya
    draw_arrow_down(c, x_pu, 158, 132)
    draw_person_node(c, x_pu - w_gp/2, 96, w_gp, h_m, "Narasimhagupta", "b. c.450 – d. 520 CE", "5th–6th C. CE • Baladitya", C_NAVY)
    
    # Level 8: Vishnugupta (Last) — Fully spacious height h_m (36 pt)!
    draw_arrow_down(c, x_pu, 96, 70)
    draw_person_node(c, x_pu - w_gp/2, 34, w_gp, h_m, "Vishnugupta (Last)", "b. c.500 – d. c.550 CE", "6th C. CE • Final Emperor", C_RED)
    
    c.showPage()
    
    # =========================================================================
    # PAGE 3: VAKATAKAS, HARSHA, BADAMI CHALUKYAS & PALLAVAS
    # =========================================================================
    c.setFillColor(colors.white)
    c.rect(0, 0, 595.28, 841.89, fill=1, stroke=0)
    
    # 4 Quadrants: Left (25 to 290), Right (305 to 570)
    # Top: y = 430 to 815 (Height = 385)
    # Bottom: y = 25 to 415 (Height = 390)
    
    # Card 1 (Top-Left): Vakataka Dynasty
    draw_cut_card(c, 25, 430, 265, 385, "Vakataka Dynasty", "3rd – 6th C. CE")
    w_sub = 140
    cx_v = 157.5
    draw_person_node(c, cx_v - w_sub/2, 735, w_sub, h_m, "Vindhyashakti I", "b. c.220 – d. 280 CE", "3rd C. CE • Founder", C_PURPLE)
    draw_arrow_down(c, cx_v, 735, 695)
    draw_person_node(c, cx_v - w_sub/2, 655, w_sub, h_m, "Pravarasena I", "b. c.250 – d. 335 CE", "3rd–4th C. CE • Samrat", C_PURPLE)
    
    # Fork to Pravarapura & Vatsagulma branches
    draw_fork_2(c, cx_v, 655, 85, 220, 615)
    draw_person_node(c, 35, 565, 105, 44, "Rudrasena II\n(Pravarapura)", "b. c.360 – d. 390 CE", "4th C. CE • m. Prabhavati", C_PURPLE)
    draw_person_node(c, 168, 565, 105, 44, "Sarvasena\n(Vatsagulma)", "b. c.300 – d. 355 CE", "4th C. CE • Branch Founder", C_PURPLE)
    
    draw_arrow_down(c, 220, 565, 515)
    draw_person_node(c, 155, 475, 120, h_m, "Harishena", "b. c.440 – d. 510 CE", "5th–6th C. • Ajanta Caves", C_PURPLE)
    
    # Card 2 (Top-Right): Pushyabhuti & Maukhari Dynasties
    draw_cut_card(c, 305, 430, 265, 385, "Pushyabhuti & Maukharis", "6th – 7th C. CE")
    cx_p = 437.5
    draw_person_node(c, cx_p - 75, 735, 150, h_m, "Prabhakaravardhana", "b. c.545 – d. 605 CE", "6th–7th C. CE • Thanesar", C_GREEN)
    
    # Fork 3: Rajyavardhana, Harsha, Rajyashri
    draw_fork_3(c, cx_p, 735, 350, 437.5, 525, 685)
    draw_person_node(c, 315, 635, 70, 44, "Rajyavardhana", "b. 582 – d. 606", "6th–7th C. CE", C_GREEN)
    draw_person_node(c, 390, 635, 95, 44, "Harshavardhana", "b. 590 – d. 647 CE", "6th–7th C. • Kannauj", C_GREEN)
    draw_person_node(c, 490, 635, 70, 44, "Rajyashri", "b. 592 – d. 650", "6th–7th C. CE", C_TEAL)
    
    # Marriage link to Grahavarman Maukhari
    draw_arrow_down(c, 525, 635, 570)
    draw_person_node(c, 460, 520, 105, 44, "Grahavarman\nMaukhari", "b. c.580 – d. 606 CE", "Maukhari King of Kannauj", C_TEAL)
    
    # Card 3 (Bottom-Left): Badami Chalukyas
    draw_cut_card(c, 25, 25, 265, 395, "Chalukyas of Badami", "6th – 8th C. CE")
    draw_person_node(c, cx_v - w_sub/2, 345, w_sub, h_m, "Pulakeshin I", "b. c.505 – d. 566 CE", "6th C. CE • Vatapi Founder", C_NAVY)
    
    draw_fork_2(c, cx_v, 345, 88, 220, 305)
    draw_person_node(c, 35, 265, 105, h_m, "Kirtivarman I", "b. c.535 – d. 597 CE", "6th C. CE • King", C_NAVY)
    draw_person_node(c, 168, 265, 105, h_m, "Mangalesha", "b. c.540 – d. 610 CE", "6th–7th C. CE • Regent", C_NAVY)
    
    draw_arrow_down(c, 88, 265, 225)
    draw_person_node(c, 35, 185, 115, h_m, "Pulakeshin II", "b. c.570 – d. 642 CE", "6th–7th C. • Aihole Prashasti", C_NAVY)
    
    draw_arrow_down(c, 92, 185, 145)
    draw_person_node(c, 35, 105, 115, h_m, "Vikramaditya I", "b. c.620 – d. 680 CE", "7th C. CE • Son", C_NAVY)
    
    draw_arrow_right(c, 150, 168, 105 + h_m/2)
    draw_person_node(c, 168, 105, 115, h_m, "Vikramaditya II", "b. c.685 – d. 744 CE", "7th–8th C. • Pattadakal", C_NAVY)
    
    draw_arrow_down(c, 225, 105, 75)
    draw_person_node(c, 168, 38, 115, h_m, "Kirtivarman II (Last)", "b. c.720 – d. 753 CE", "8th C. CE • Overthrown", C_RED)
    
    # Card 4 (Bottom-Right): Pallavas of Kanchi
    draw_cut_card(c, 305, 25, 265, 395, "Pallavas of Kanchi", "6th – 9th C. CE")
    draw_person_node(c, cx_p - 75, 345, 150, h_m, "Simhavishnu", "b. c.540 – d. 600 CE", "6th C. CE • Avanisimha", C_PURPLE)
    draw_arrow_down(c, cx_p, 345, 305)
    draw_person_node(c, cx_p - 75, 265, 150, h_m, "Mahendravarman I", "b. c.570 – d. 630 CE", "6th–7th C. • Mattavilasa", C_PURPLE)
    draw_arrow_down(c, cx_p, 265, 225)
    draw_person_node(c, cx_p - 75, 185, 150, h_m, "Narasimhavarman I", "b. c.600 – d. 668 CE", "7th C. CE • Mahamalla", C_PURPLE)
    draw_arrow_down(c, cx_p, 185, 145)
    draw_person_node(c, cx_p - 75, 105, 150, h_m, "Rajasimha (Narasimha II)", "b. c.670 – d. 728 CE", "7th–8th C. • Shore Temple", C_PURPLE)
    draw_arrow_down(c, cx_p, 105, 75)
    draw_person_node(c, cx_p - 75, 38, 150, h_m, "Nandivarman II", "b. c.715 – d. 796 CE", "8th C. CE • Pallavamalla", C_PURPLE)
    
    c.showPage()
    
    # =========================================================================
    # PAGE 4: RASHTRAKUTAS, CHOLAS & VIJAYANAGARA
    # =========================================================================
    c.setFillColor(colors.white)
    c.rect(0, 0, 595.28, 841.89, fill=1, stroke=0)
    
    # Card 1: Rashtrakutas of Manyakheta
    draw_cut_card(c, 25, 715, 545, 105, "Rashtrakutas of Manyakheta", "8th – 10th Century CE")
    draw_person_node(c, 40, 735, w_h, h_m, "Dantidurga", "b. c.710 – d. 756 CE", "8th C. CE • Founder", C_GREEN)
    draw_arrow_right(c, 40 + w_h, 172, 735 + h_m/2)
    draw_person_node(c, 172, 735, w_h, h_m, "Krishna I", "b. c.715 – d. 774 CE", "8th C. CE • Ellora Kailasa", C_GREEN)
    draw_arrow_right(c, 172 + w_h, 304, 735 + h_m/2)
    draw_person_node(c, 304, 735, w_h, h_m, "Amoghavarsha I", "b. 800 – d. 878 CE", "9th C. CE • Kavirajamarga", C_GREEN)
    draw_arrow_right(c, 304 + w_h, 436, 735 + h_m/2)
    draw_person_node(c, 436, 735, w_h, h_m, "Krishna III", "b. c.910 – d. 967 CE", "10th C. CE • Takkolam Battle", C_GREEN)
    
    # Card 2: Imperial Cholas of Thanjavur (Left-to-Right natural flow!)
    draw_cut_card(c, 25, 455, 545, 245, "Imperial Cholas of Thanjavur", "9th – 13th Century CE")
    w_ch = 135
    # Row 1: Vijayalaya -> Aditya I -> Parantaka I
    draw_person_node(c, 45, 620, w_ch, h_m, "Vijayalaya", "b. c.815 – d. 871 CE", "9th C. CE • Founder", C_RED)
    draw_arrow_right(c, 45 + w_ch, 230, 620 + h_m/2)
    draw_person_node(c, 230, 620, w_ch, h_m, "Aditya I", "b. c.845 – d. 907 CE", "9th–10th C. CE • Son", C_RED)
    draw_arrow_right(c, 230 + w_ch, 410, 620 + h_m/2)
    draw_person_node(c, 410, 620, w_ch, h_m, "Parantaka I", "b. c.875 – d. 955 CE", "9th–10th C. • Uttaramerur", C_RED)
    
    # Down from Parantaka I to Rajaraja I (centered in row 2)
    draw_arrow_down(c, 410 + w_ch/2, 620, 582)
    c.line(410 + w_ch/2, 582, 297.64, 582)
    draw_arrow_down(c, 297.64, 582, 574)
    draw_person_node(c, 297.64 - w_ch/2, 538, w_ch, h_m, "Rajaraja I 'The Great'", "b. 947 – d. 1014 CE", "10th–11th C. • Brihadisvara", C_RED)
    
    # Down to Row 3: Rajendra I -> Rajadhiraja I -> Kulottunga I
    draw_arrow_down(c, 297.64, 538, 502)
    c.line(297.64, 502, 45 + w_ch/2, 502)
    draw_arrow_down(c, 45 + w_ch/2, 502, 494)
    
    draw_person_node(c, 45, 465, w_ch, h_m, "Rajendra I", "b. 971 – d. 1044 CE", "10th–11th C. • Gangaikonda", C_RED)
    draw_arrow_right(c, 45 + w_ch, 230, 465 + h_m/2)
    draw_person_node(c, 230, 465, w_ch, h_m, "Rajadhiraja I", "b. 1018 – d. 1054 CE", "11th C. CE • Battle of Koppam", C_RED)
    draw_arrow_right(c, 230 + w_ch, 410, 465 + h_m/2)
    draw_person_node(c, 410, 465, w_ch, h_m, "Kulottunga I", "b. 1040 – d. 1120 CE", "11th–12th C. • Chalukya-Chola", C_RED)
    
    # Card 3: Vijayanagara Empire
    draw_cut_card(c, 25, 25, 545, 415, "Vijayanagara Empire (Four Dynasties)", "14th – 17th Century CE")
    w_vj = 145
    
    # 1. Sangama Dynasty
    draw_person_node(c, 45, 360, w_vj, h_m, "Harihara I & Bukka I", "b. c.1300 – d. 1377 CE", "14th C. CE • Sangama Founders", C_BLUE)
    draw_arrow_right(c, 45 + w_vj, 225, 360 + h_m/2)
    draw_person_node(c, 225, 360, w_vj, h_m, "Deva Raya I", "b. c.1360 – d. 1422 CE", "14th–15th C. CE • Nicolo Conti", C_BLUE)
    draw_arrow_right(c, 225 + w_vj, 405, 360 + h_m/2)
    draw_person_node(c, 405, 360, w_vj, h_m, "Deva Raya II", "b. c.1405 – d. 1446 CE", "15th C. CE • Abdur Razzaq", C_BLUE)
    
    # 2. Saluva Dynasty Usurpation (Centered)
    draw_arrow_down(c, 405 + w_vj/2, 360, 328)
    c.line(405 + w_vj/2, 328, 297.64, 328)
    draw_arrow_down(c, 297.64, 328, 320)
    draw_person_node(c, 297.64 - w_vj/2, 284, w_vj, h_m, "Saluva Narasimha", "b. c.1435 – d. 1491 CE", "15th C. CE • Saluva Founder", C_PURPLE)
    
    # 3. Tuluva Dynasty
    draw_arrow_down(c, 297.64, 284, 250)
    c.line(297.64, 250, 45 + w_vj/2, 250)
    draw_arrow_down(c, 45 + w_vj/2, 250, 242)
    
    draw_person_node(c, 45, 206, w_vj, h_m, "Vira Narasimha", "b. c.1475 – d. 1509 CE", "15th–16th C. • Tuluva Founder", C_ORANGE)
    draw_arrow_right(c, 45 + w_vj, 225, 206 + h_m/2)
    draw_person_node(c, 225, 206, w_vj, h_m, "Krishnadevaraya", "b. 1471 – d. 1529 CE", "15th–16th C. • Amuktamalyada", C_ORANGE)
    draw_arrow_right(c, 225 + w_vj, 405, 206 + h_m/2)
    draw_person_node(c, 405, 206, w_vj, h_m, "Achyuta Deva Raya", "b. c.1485 – d. 1542 CE", "16th C. CE • Brother", C_ORANGE)
    
    draw_arrow_down(c, 225 + w_vj/2, 206, 172)
    draw_person_node(c, 225, 136, w_vj, h_m, "Rama Raya (Regent)", "b. 1484 – d. 1565 CE", "16th C. • Battle of Talikota", C_RED)
    
    # 4. Aravidu Dynasty
    draw_arrow_down(c, 225 + w_vj/2, 136, 102)
    draw_person_node(c, 225, 66, w_vj, h_m, "Tirumala Raya", "b. c.1510 – d. 1578 CE", "16th C. • Aravidu Founder", C_PURPLE)
    draw_arrow_right(c, 225 + w_vj, 405, 66 + h_m/2)
    draw_person_node(c, 405, 66, w_vj, h_m, "Venkata II", "b. c.1555 – d. 1614 CE", "16th–17th C. • Chandragiri", C_PURPLE)
    
    c.showPage()
    
    # =========================================================================
    # PAGE 5: DELHI SULTANATE DYNASTIES
    # =========================================================================
    c.setFillColor(colors.white)
    c.rect(0, 0, 595.28, 841.89, fill=1, stroke=0)
    
    # 4 Quadrants: Left (25 to 290), Right (305 to 570)
    # Top: y = 430 to 815 (Height = 385)
    # Bottom: y = 25 to 415 (Height = 390)
    
    # Card 1 (Top-Left): Mamluk / Slave Dynasty
    draw_cut_card(c, 25, 430, 265, 385, "Mamluk / Slave Dynasty", "1206 – 1290 CE")
    draw_person_node(c, 85, 735, w_sub, h_m, "Qutb-ud-din Aibak", "b. 1150 – d. 1210 CE", "12th–13th C. • Lakhbaksh", C_BLUE)
    draw_arrow_down(c, 85 + w_sub/2, 735, 695)
    draw_person_node(c, 85, 655, w_sub, h_m, "Shams-ud-din Iltutmish", "b. c.1175 – d. 1236 CE", "12th–13th C. • Iqta; Tanka", C_BLUE)
    
    draw_fork_2(c, 85 + w_sub/2, 655, 88, 220, 615)
    draw_person_node(c, 35, 575, 105, 44, "Razia Sultana", "b. 1205 – d. 1240 CE", "13th C. • First Female Sultan", C_BLUE)
    draw_person_node(c, 168, 575, 105, 44, "Nasir-ud-din Mahmud", "b. 1229 – d. 1266 CE", "13th C. • Son of Iltutmish", C_BLUE)
    
    # Arrow from Nasir-ud-din Mahmud to Balban (Balban was his regent and father-in-law)
    draw_arrow_down(c, 220, 575, 520)
    draw_person_node(c, 85, 475, w_sub, h_m, "Ghiyas-ud-din Balban", "b. 1200 – d. 1287 CE", "13th C. • Blood & Iron; Sijda", C_BLUE)
    
    # Card 2 (Top-Right): Khalji Dynasty
    draw_cut_card(c, 305, 430, 265, 385, "Khalji Dynasty", "1290 – 1320 CE")
    draw_person_node(c, 370, 735, w_sub, h_m, "Jalal-ud-din Khalji", "b. 1220 – d. 1296 CE", "13th C. • Founder", C_RED)
    draw_arrow_down(c, 370 + w_sub/2, 735, 680)
    draw_person_node(c, 370, 635, w_sub, h_m, "Ala-ud-din Khalji", "b. 1266 – d. 1316 CE", "13th–14th C. • Market Reforms", C_RED)
    draw_arrow_down(c, 370 + w_sub/2, 635, 580)
    draw_person_node(c, 370, 535, w_sub, h_m, "Mubarak Shah Khalji", "b. 1299 – d. 1320 CE", "14th C. • Son; Declared Caliph", C_RED)
    draw_arrow_down(c, 370 + w_sub/2, 535, 480)
    draw_person_node(c, 370, 445, w_sub, h_m, "Khusrau Khan (Last)", "r. 1320 CE • Slain 1320 CE", "14th C. • Usurper", C_RED)
    
    # Card 3 (Bottom-Left): Tughlaq Dynasty
    draw_cut_card(c, 25, 25, 265, 395, "Tughlaq Dynasty", "1320 – 1414 CE")
    draw_person_node(c, 85, 345, w_sub, h_m, "Ghiyas-ud-din Tughlaq", "b. c.1270 – d. 1325 CE", "13th–14th C. • Tughlaqabad", C_PURPLE)
    draw_arrow_down(c, 85 + w_sub/2, 345, 305)
    draw_person_node(c, 85, 260, w_sub, h_m, "Muhammad bin Tughlaq", "b. 1290 – d. 1351 CE", "14th C. • Token Currency", C_PURPLE)
    draw_arrow_down(c, 85 + w_sub/2, 260, 220)
    draw_person_node(c, 85, 175, w_sub, h_m, "Firoz Shah Tughlaq", "b. 1309 – d. 1388 CE", "14th C. • Canals; Jizya", C_PURPLE)
    draw_arrow_down(c, 85 + w_sub/2, 175, 135)
    draw_person_node(c, 85, 90, w_sub, h_m, "Nasir-ud-din Mahmud", "b. c.1375 – d. 1413 CE", "14th–15th C. • Timur Invasion", C_RED)
    
    # Card 4 (Bottom-Right): Sayyid & Lodi Dynasties
    draw_cut_card(c, 305, 25, 265, 395, "Sayyid & Lodi Dynasties", "1414 – 1526 CE")
    draw_person_node(c, 370, 345, w_sub, h_m, "Khizr Khan (Sayyid)", "b. c.1365 – d. 1421 CE", "14th–15th C. • Rayat-i-Ala", C_TEAL)
    draw_arrow_down(c, 370 + w_sub/2, 345, 300)
    draw_person_node(c, 370, 255, w_sub, h_m, "Bahlul Lodi", "b. 1401 – d. 1489 CE", "15th C. • 1st Afghan Empire", C_GREEN)
    draw_arrow_down(c, 370 + w_sub/2, 255, 210)
    draw_person_node(c, 370, 165, w_sub, h_m, "Sikandar Lodi", "b. 1458 – d. 1517 CE", "15th–16th C. • Founded Agra", C_GREEN)
    draw_arrow_down(c, 370 + w_sub/2, 165, 120)
    draw_person_node(c, 370, 75, w_sub, h_m, "Ibrahim Lodi (Last)", "b. 1480 – d. 1526 CE", "15th–16th C. • Panipat 1526", C_RED)
    
    c.showPage()
    
    # =========================================================================
    # PAGE 6: THE IMPERIAL MUGHALS & MARATHAS
    # =========================================================================
    c.setFillColor(colors.white)
    c.rect(0, 0, 595.28, 841.89, fill=1, stroke=0)
    
    # Card 1 (Top Half): The Imperial Mughal Dynasty
    # Two Top-to-Bottom columns: Left = Great Mughals; Right = Later Mughals
    draw_cut_card(c, 25, 400, 545, 415, "The Imperial Mughal Dynasty", "16th – 19th Century CE")
    w_mg = 135
    
    # Left Column: Babur -> Humayun -> Akbar -> Jahangir -> Shah Jahan -> Aurangzeb
    draw_person_node(c, 45, 735, w_mg, h_m, "Zahir-ud-din Babur", "b. 1483 – d. 1530 CE", "15th–16th C. • Panipat 1526", C_BLUE)
    draw_arrow_down(c, 45 + w_mg/2, 735, 695)
    
    draw_person_node(c, 45, 655, w_mg, h_m, "Nasir-ud-din Humayun", "b. 1508 – d. 1556 CE", "16th C. • Dinpanah", C_BLUE)
    # Sur Interregnum next to Humayun
    draw_person_node(c, 215, 655, w_mg, h_m, "Sher Shah Suri (Sur)", "b. 1472 – d. 1545 CE", "15th–16th C. • Rupiya; GT Road", C_RED)
    draw_arrow_right(c, 45 + w_mg, 215, 655 + h_m/2)
    
    draw_arrow_down(c, 45 + w_mg/2, 655, 615)
    draw_person_node(c, 45, 575, w_mg, h_m, "Jalal-ud-din Akbar", "b. 1542 – d. 1605 CE", "16th–17th C. • Mansabdari", C_BLUE)
    
    draw_arrow_down(c, 45 + w_mg/2, 575, 535)
    draw_person_node(c, 45, 495, w_mg, h_m, "Nur-ud-din Jahangir", "b. 1569 – d. 1627 CE", "16th–17th C. • Paintings", C_BLUE)
    
    draw_arrow_down(c, 45 + w_mg/2, 495, 455)
    draw_person_node(c, 45, 415, w_mg, h_m, "Shah Jahan", "b. 1592 – d. 1666 CE", "16th–17th C. • Taj Mahal", C_BLUE)
    
    # Aurangzeb next to Shah Jahan
    draw_arrow_right(c, 45 + w_mg, 215, 415 + h_m/2)
    draw_person_node(c, 215, 415, w_mg, h_m, "Aurangzeb Alamgir", "b. 1618 – d. 1707 CE", "17th–18th C. • Fatawa-i-Alamgiri", C_BLUE)
    
    # Connect from Aurangzeb up to Bahadur Shah I at top of Right Column!
    # Path: from (215 + w_mg, 415 + h_m/2) -> (365, 433) -> (365, 735 + h_m/2) -> (395, 735 + h_m/2)
    c.setStrokeColor(C_ARROW)
    c.setLineWidth(1)
    c.line(215 + w_mg, 415 + h_m/2, 365, 415 + h_m/2)
    c.line(365, 415 + h_m/2, 365, 735 + h_m/2)
    draw_arrow_right(c, 365, 395, 735 + h_m/2)
    
    # Right Column (Later Mughals flowing TOP-TO-BOTTOM!)
    draw_person_node(c, 395, 735, 150, h_m, "Bahadur Shah I", "b. 1643 – d. 1712 CE", "17th–18th C. • Shah-i-Bekhabar", C_BLUE)
    draw_arrow_down(c, 395 + 75, 735, 680)
    
    draw_person_node(c, 395, 640, 150, h_m, "Muhammad Shah 'Rangeela'", "b. 1702 – d. 1748 CE", "18th C. • Nadir Shah 1739", C_BLUE)
    draw_arrow_down(c, 395 + 75, 640, 585)
    
    draw_person_node(c, 395, 545, 150, h_m, "Shah Alam II", "b. 1728 – d. 1806 CE", "18th–19th C. • Buxar; Allahabad", C_BLUE)
    draw_arrow_down(c, 395 + 75, 545, 490)
    
    draw_person_node(c, 395, 450, 150, h_m, "Bahadur Shah II 'Zafar'", "b. 1775 – d. 1862 CE", "18th–19th C. • 1857 Revolt", C_RED)
    
    # Bottom Half: Maratha Chhatrapatis & Peshwas
    # Card 2 (Bottom-Left): House of Shivaji Maharaj
    draw_cut_card(c, 25, 25, 265, 360, "Maratha Chhatrapatis", "17th – 18th C. CE")
    draw_person_node(c, 85, 305, w_sub, h_m, "Shahaji Bhonsle", "b. 1594 – d. 1664 CE", "16th–17th C. • Jagirdar", C_GREEN)
    draw_arrow_down(c, 85 + w_sub/2, 305, 265)
    draw_person_node(c, 85, 225, w_sub, h_m, "Shivaji Maharaj", "b. 1630 – d. 1680 CE", "17th C. • Chhatrapati 1674", C_GREEN)
    
    draw_fork_2(c, 85 + w_sub/2, 225, 88, 220, 190)
    draw_person_node(c, 35, 145, 105, 44, "Chh. Sambhaji", "b. 1657 – d. 1689 CE", "17th C. • Elder Son", C_GREEN)
    draw_person_node(c, 168, 145, 105, 44, "Chh. Rajaram\n& Tarabai", "b. 1670 – d. 1700 CE", "17th–18th C. • Resistance", C_PURPLE)
    
    draw_arrow_down(c, 88, 145, 105)
    draw_person_node(c, 35, 60, 105, h_m, "Chh. Shahu I", "b. 1682 – d. 1749 CE", "17th–18th C. • Satara", C_GREEN)
    
    # Card 3 (Bottom-Right): Hereditary Bhat Peshwas of Pune
    draw_cut_card(c, 305, 25, 265, 360, "Hereditary Bhat Peshwas", "18th – 19th C. CE")
    draw_person_node(c, 365, 305, 145, h_m, "Balaji Vishwanath", "b. 1662 – d. 1720 CE", "17th–18th C. • 1st Hereditary Peshwa", C_ORANGE)
    draw_arrow_down(c, 365 + 145/2, 305, 265)
    draw_person_node(c, 365, 225, 145, h_m, "Baji Rao I", "b. 1700 – d. 1740 CE", "18th C. • Hindu-Pad-Padshahi", C_ORANGE)
    draw_arrow_down(c, 365 + 145/2, 225, 185)
    draw_person_node(c, 365, 145, 145, h_m, "Balaji Baji Rao (Nana)", "b. 1720 – d. 1761 CE", "18th C. • Sangola Pact; 3rd Panipat", C_ORANGE)
    
    draw_fork_2(c, 365 + 145/2, 145, 365, 495, 105)
    draw_person_node(c, 315, 60, 100, h_m, "Madhavrao I", "b. 1745 – d. 1772", "18th C. • Revival", C_ORANGE)
    draw_person_node(c, 445, 60, 100, h_m, "Baji Rao II (Last)", "b. 1775 – d. 1851", "18th–19th C. • Bassein", C_RED)
    
    c.showPage()
    c.save()
    print(f"Generated clean tree PDF at {filename}")

if __name__ == "__main__":
    target = "/data/data/com.termux/files/home/sahacit/lineages/UPSC_History_Family_Trees.pdf"
    create_clean_pdf(target)
