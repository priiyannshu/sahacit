import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def draw_header(c, title, subtitle, page_num, total_pages=5):
    # White background
    c.setFillColor(colors.white)
    c.rect(0, 0, 595.28, 841.89, fill=1, stroke=0)
    
    # Outer thin border
    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.setLineWidth(0.8)
    c.rect(20, 20, 555.28, 801.89)
    
    # Header bar
    c.setFillColor(colors.HexColor("#1E3A8A"))
    c.rect(20, 785, 555.28, 36.89, fill=1, stroke=0)
    
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(297.64, 804, title)
    
    c.setFont("Helvetica", 9)
    c.drawCentredString(297.64, 791, subtitle)
    
    # Footer
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.HexColor("#64748B"))
    c.drawString(30, 26, "UPSC Civil Services Examination | Ancient & Medieval Indian History Lineages")
    c.drawRightString(565.28, 26, f"Sheet {page_num} of {total_pages}")

def draw_section_banner(c, y, title, century_badge, capital=None):
    c.setFillColor(colors.HexColor("#0F172A"))
    c.rect(30, y, 535.28, 20, fill=1, stroke=0)
    
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(38, y + 5.5, title.upper())
    
    # Century Badge
    badge_text = f"Century: {century_badge}"
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(colors.HexColor("#FEF08A"))
    c.drawRightString(555, y + 5.5, badge_text)
    
    if capital:
        c.setFont("Helvetica-Oblique", 8)
        c.setFillColor(colors.HexColor("#E2E8F0"))
        c.drawString(240, y + 5.5, f"Capital: {capital}")

def draw_node(c, x, y, w, h, name, dates, century, note="", name_color=colors.HexColor("#1D4ED8"), bg=colors.white, border=colors.HexColor("#94A3B8")):
    # Draw box
    c.setFillColor(bg)
    c.setStrokeColor(border)
    c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, 3, fill=1, stroke=1)
    
    # Name (colored)
    c.setFillColor(name_color)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawCentredString(x + w/2, y + h - 11, name)
    
    # Birth & Death / Reign
    c.setFillColor(colors.HexColor("#0F172A"))
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(x + w/2, y + h - 21, dates)
    
    # Century
    c.setFillColor(colors.HexColor("#475569"))
    c.setFont("Helvetica", 6.5)
    c.drawCentredString(x + w/2, y + h - 30, f"Era: {century}")
    
    # Note/UPSC Hook (if space)
    if note and h >= 42:
        c.setFillColor(colors.HexColor("#B45309"))
        c.setFont("Helvetica-Oblique", 6.2)
        c.drawCentredString(x + w/2, y + 4.5, note)

def draw_arrow_down(c, x, y_start, y_end, label=""):
    c.setStrokeColor(colors.HexColor("#64748B"))
    c.setLineWidth(0.9)
    c.line(x, y_start, x, y_end)
    # arrow head
    c.setFillColor(colors.HexColor("#64748B"))
    p = c.beginPath()
    p.moveTo(x, y_end)
    p.lineTo(x - 2.5, y_end + 4)
    p.lineTo(x + 2.5, y_end + 4)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    if label:
        c.setFont("Helvetica", 6)
        c.setFillColor(colors.HexColor("#64748B"))
        c.drawString(x + 4, (y_start + y_end)/2 - 2, label)

def draw_branch_2(c, parent_x, parent_bottom_y, left_x, right_x, child_top_y, label_l="", label_r=""):
    c.setStrokeColor(colors.HexColor("#64748B"))
    c.setLineWidth(0.9)
    mid_y = (parent_bottom_y + child_top_y) / 2
    c.line(parent_x, parent_bottom_y, parent_x, mid_y)
    c.line(left_x, mid_y, right_x, mid_y)
    draw_arrow_down(c, left_x, mid_y, child_top_y, label_l)
    draw_arrow_down(c, right_x, mid_y, child_top_y, label_r)

def draw_branch_3(c, parent_x, parent_bottom_y, left_x, mid_x, right_x, child_top_y):
    c.setStrokeColor(colors.HexColor("#64748B"))
    c.setLineWidth(0.9)
    mid_y = (parent_bottom_y + child_top_y) / 2
    c.line(parent_x, parent_bottom_y, parent_x, mid_y)
    c.line(left_x, mid_y, right_x, mid_y)
    draw_arrow_down(c, left_x, mid_y, child_top_y)
    draw_arrow_down(c, mid_x, mid_y, child_top_y)
    draw_arrow_down(c, right_x, mid_y, child_top_y)

def draw_branch_4(c, parent_x, parent_bottom_y, x1, x2, x3, x4, child_top_y):
    c.setStrokeColor(colors.HexColor("#64748B"))
    c.setLineWidth(0.9)
    mid_y = (parent_bottom_y + child_top_y) / 2
    c.line(parent_x, parent_bottom_y, parent_x, mid_y)
    c.line(x1, mid_y, x4, mid_y)
    draw_arrow_down(c, x1, mid_y, child_top_y)
    draw_arrow_down(c, x2, mid_y, child_top_y)
    draw_arrow_down(c, x3, mid_y, child_top_y)
    draw_arrow_down(c, x4, mid_y, child_top_y)

print("Helper definitions loaded successfully.")
