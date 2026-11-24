import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas

# Palette
C_CARD_BORDER = colors.HexColor("#94A3B8")   # Slate border for cutting
C_CARD_HEADER = colors.HexColor("#0F172A")   # Dark Navy header pill
C_GOLD        = colors.HexColor("#D97706")   # Amber Gold for Century
C_NODE_BORDER = colors.HexColor("#CBD5E1")   # Light gray node border
C_ARROW       = colors.HexColor("#475569")   # Slate gray arrows

# Vibrant Colors for Names
C_NAVY   = colors.HexColor("#1D4ED8") # Royal Blue
C_RED    = colors.HexColor("#DC2626") # Crimson Red
C_GREEN  = colors.HexColor("#059669") # Emerald Green
C_PURPLE = colors.HexColor("#7C3AED") # Purple
C_TEAL   = colors.HexColor("#0D9488") # Teal
C_ORANGE = colors.HexColor("#EA580C") # Orange/Amber
C_BLUE   = C_NAVY

def draw_cut_card(c, x, y, w, h, dynasty_name, century_label, subtitle=""):
    """Draws a clean self-contained card with dashed cut border and clean header.
       Guarantees NO overlapping between title and century label."""
    # Outer cut border (dashed)
    c.setStrokeColor(C_CARD_BORDER)
    c.setLineWidth(0.8)
    c.setDash(3, 3)
    c.roundRect(x, y, w, h, 6, fill=0, stroke=1)
    c.setDash() # reset dash
    
    # Header bar
    header_h = 18
    bar_y = y + h - header_h - 6
    c.setFillColor(C_CARD_HEADER)
    c.roundRect(x + 6, bar_y, w - 12, header_h, 3, fill=1, stroke=0)
    
    # Calculate available space
    avail_w = w - 24
    
    # Format Century text
    cent_text = f"ERA: {century_label}" if not century_label.startswith("ERA") else century_label
    
    # Check widths
    c.setFont("Helvetica-Bold", 8)
    title_w = c.stringWidth(dynasty_name.upper(), "Helvetica-Bold", 8)
    
    c.setFont("Helvetica-Bold", 7.2)
    cent_w = c.stringWidth(cent_text, "Helvetica-Bold", 7.2)
    
    # If too tight, abbreviate century tag
    if title_w + cent_w + 14 > avail_w:
        cent_text = century_label.replace("Century", "C.").replace("century", "C.")
        cent_w = c.stringWidth(cent_text, "Helvetica-Bold", 7)
    
    # Draw Title
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(colors.white)
    c.drawString(x + 12, bar_y + 5, dynasty_name.upper())
    
    # Draw Century Badge
    c.setFont("Helvetica-Bold", 7.2)
    c.setFillColor(C_GOLD)
    c.drawRightString(x + w - 12, bar_y + 5, cent_text)

def draw_person_node(c, x, y, w, h, name, dates, century_and_role, name_color=C_NAVY):
    """Draws a person card with name in color, dates, and century/role.
       Handles multi-line names cleanly without square glyphs."""
    c.setFillColor(colors.white)
    c.setStrokeColor(C_NODE_BORDER)
    c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, 4, fill=1, stroke=1)
    
    # Check for multi-line name
    name_lines = [line.strip() for line in name.split("\n") if line.strip()]
    
    if len(name_lines) == 1:
        # Single line name
        c.setFont("Helvetica-Bold", 8.2)
        c.setFillColor(name_color)
        c.drawCentredString(x + w/2, y + h - 11, name_lines[0])
        
        c.setFont("Helvetica", 6.5)
        c.setFillColor(colors.HexColor("#64748B"))
        c.drawCentredString(x + w/2, y + h - 21.5, century_and_role)
        
        c.setFont("Helvetica-Bold", 7)
        c.setFillColor(colors.HexColor("#0F172A"))
        c.drawCentredString(x + w/2, y + 4.5, dates)
    else:
        # Multi-line name (e.g. 2 lines)
        c.setFont("Helvetica-Bold", 7.6)
        c.setFillColor(name_color)
        c.drawCentredString(x + w/2, y + h - 10, name_lines[0])
        c.drawCentredString(x + w/2, y + h - 19, name_lines[1])
        
        c.setFont("Helvetica", 6.3)
        c.setFillColor(colors.HexColor("#64748B"))
        c.drawCentredString(x + w/2, y + h - 28.5, century_and_role)
        
        c.setFont("Helvetica-Bold", 6.8)
        c.setFillColor(colors.HexColor("#0F172A"))
        c.drawCentredString(x + w/2, y + 4, dates)

def draw_arrow_down(c, x, y_start, y_end):
    """Clean downward arrow."""
    c.setStrokeColor(C_ARROW)
    c.setLineWidth(1)
    c.line(x, y_start, x, y_end)
    c.setFillColor(C_ARROW)
    p = c.beginPath()
    p.moveTo(x, y_end)
    p.lineTo(x - 2.5, y_end + 4)
    p.lineTo(x + 2.5, y_end + 4)
    p.close()
    c.drawPath(p, fill=1, stroke=0)

def draw_arrow_up(c, x, y_start, y_end):
    """Clean upward arrow."""
    c.setStrokeColor(C_ARROW)
    c.setLineWidth(1)
    c.line(x, y_start, x, y_end)
    c.setFillColor(C_ARROW)
    p = c.beginPath()
    p.moveTo(x, y_end)
    p.lineTo(x - 2.5, y_end - 4)
    p.lineTo(x + 2.5, y_end - 4)
    p.close()
    c.drawPath(p, fill=1, stroke=0)

def draw_arrow_right(c, x_start, x_end, y):
    """Clean rightward arrow."""
    c.setStrokeColor(C_ARROW)
    c.setLineWidth(1)
    c.line(x_start, y, x_end, y)
    c.setFillColor(C_ARROW)
    p = c.beginPath()
    p.moveTo(x_end, y)
    p.lineTo(x_end - 4, y + 2.5)
    p.lineTo(x_end - 4, y - 2.5)
    p.close()
    c.drawPath(p, fill=1, stroke=0)

def draw_arrow_left(c, x_start, x_end, y):
    """Clean leftward arrow."""
    c.setStrokeColor(C_ARROW)
    c.setLineWidth(1)
    c.line(x_start, y, x_end, y)
    c.setFillColor(C_ARROW)
    p = c.beginPath()
    p.moveTo(x_end, y)
    p.lineTo(x_end + 4, y + 2.5)
    p.lineTo(x_end + 4, y - 2.5)
    p.close()
    c.drawPath(p, fill=1, stroke=0)

def draw_fork_2(c, px, py_start, left_x, right_x, y_target):
    """Forks from 1 parent down to 2 children."""
    c.setStrokeColor(C_ARROW)
    c.setLineWidth(1)
    mid_y = (py_start + y_target) / 2
    c.line(px, py_start, px, mid_y)
    c.line(left_x, mid_y, right_x, mid_y)
    draw_arrow_down(c, left_x, mid_y, y_target)
    draw_arrow_down(c, right_x, mid_y, y_target)

def draw_fork_3(c, px, py_start, x1, x2, x3, y_target):
    """Forks from 1 parent down to 3 children."""
    c.setStrokeColor(C_ARROW)
    c.setLineWidth(1)
    mid_y = (py_start + y_target) / 2
    c.line(px, py_start, px, mid_y)
    c.line(x1, mid_y, x3, mid_y)
    draw_arrow_down(c, x1, mid_y, y_target)
    draw_arrow_down(c, x2, mid_y, y_target)
    draw_arrow_down(c, x3, mid_y, y_target)

print("Updated clean_tree_primitives successfully.")
