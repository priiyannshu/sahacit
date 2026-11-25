#import "theme.typ": *

#let render-state-skeleton(skeleton) = {
  [
    #metadata("state-skeleton") <state-skeleton>
    #text(font: font-sans, size: 8pt, weight: "bold", fill: ink-soft, tracking: 0.08em, "FRONT MATTER · MACRO CONSTITUTIONAL ARCHITECTURE")
    #v(-4pt)
    #text(font: font-sans, size: 17pt, weight: "bold", fill: ink, skeleton.title)
    #v(-4pt)
    #text(font: font-serif, size: 10pt, style: "italic", fill: ink-muted, skeleton.subtitle)
    #v(4pt)
    #line(length: 100%, stroke: 1.2pt + rule-dark)
    #v(5pt)

    // Foundational architecture cards
    #grid(
      columns: (1fr, 1fr, 1fr),
      column-gutter: 7pt,
      ..skeleton.core_principles.map(p => box(
        width: 100%,
        stroke: 0.65pt + rule-mid,
        fill: tint-subtle,
        radius: 2pt,
        inset: 6pt,
        {
          text(font: font-sans, size: 7.8pt, weight: "bold", fill: ink, upper(p.label))
          v(2pt)
          text(font: font-serif, size: 8.2pt, fill: ink, p.detail)
        }
      ))
    )

    #v(7pt)
    #sec-heading("Institutional Pyramid of the Indian Republic (Macro Vector Map)")
    #v(3pt)

    // Clean monochrome architectural diagram
    #box(
      width: 100%,
      stroke: 0.8pt + rule-dark,
      fill: white,
      inset: 8pt,
      radius: 2pt,
      {
        align(center, box(
          stroke: 1pt + rule-dark,
          fill: tint-panel,
          inset: (x: 14pt, y: 4pt),
          radius: 2pt,
          {
            text(font: font-sans, size: 8.5pt, weight: "bold", "CONSTITUTION OF INDIA (SUPREME LAW)")
            linebreak()
            text(font: font-serif, size: 7.6pt, fill: ink-muted, "Sovereign Popular Mandate · 7th Schedule Division · Fundamental Rights & Basic Structure")
          }
        ))
        v(4pt)
        align(center, text(font: font-sans, size: 8pt, weight: "bold", "↓   Splits Sovereign Functions Across Four Horizontal & Two Vertical Pillars   ↓"))
        v(4pt)
        grid(
          columns: (1fr, 1fr, 1fr, 1fr),
          column-gutter: 5pt,
          box(stroke: 0.65pt + rule-dark, fill: tint-subtle, inset: 5pt, width: 100%, {
            text(font: font-sans, size: 7.5pt, weight: "bold", "1. LEGISLATURE")
            linebreak()
            text(font: font-serif, size: 7.6pt, "Parliament (LS + RS + Pres.)\n24 DRSCs + PAC/Est./COPU\nState Legislatures (28 + 3 UTs)")
          }),
          box(stroke: 0.65pt + rule-dark, fill: tint-subtle, inset: 5pt, width: 100%, {
            text(font: font-sans, size: 7.5pt, weight: "bold", "2. EXECUTIVE")
            linebreak()
            text(font: font-serif, size: 7.6pt, "President / Governor (Titular)\nPM + CoM + Cabinet Sec.\nMinistries, Services & Regulators")
          }),
          box(stroke: 0.65pt + rule-dark, fill: tint-subtle, inset: 5pt, width: 100%, {
            text(font: font-sans, size: 7.5pt, weight: "bold", "3. INTEGRATED JUDICIARY")
            linebreak()
            text(font: font-serif, size: 7.6pt, "Supreme Court (Apex + Collegium)\n25 High Courts (Art. 226)\nDistrict Courts + Tribunals")
          }),
          box(stroke: 0.65pt + rule-dark, fill: tint-subtle, inset: 5pt, width: 100%, {
            text(font: font-sans, size: 7.5pt, weight: "bold", "4. INSULATED WATCHDOGS")
            linebreak()
            text(font: font-serif, size: 7.6pt, "ECI · CAG · UPSC · FC · GSTC\nNCSC / NCST / NCBC\nLokpal · CVC · NHRC · NGT")
          }),
        )
        v(4pt)
        align(center, text(font: font-sans, size: 7.5pt, weight: "bold", "↓   Cooperative Federalism & 3rd-Tier Decentralization   ↓"))
        v(3pt)
        grid(
          columns: (1fr, 1fr),
          column-gutter: 6pt,
          box(stroke: 0.5pt + rule-mid, fill: white, inset: 4.5pt, width: 100%, {
            text(font: font-sans, size: 7.3pt, weight: "bold", "FEDERAL COORDINATORS: ")
            text(font: font-serif, size: 7.7pt, "Finance Commission · GST Council · Inter-State Council · Zonal Councils & NEC · NITI Aayog")
          }),
          box(stroke: 0.5pt + rule-mid, fill: white, inset: 4.5pt, width: 100%, {
            text(font: font-sans, size: 7.3pt, weight: "bold", "GRASSROOTS & SCHEDULED TIERS: ")
            text(font: font-serif, size: 7.7pt, "Panchayats (Part IX, PESA) · Municipalities (Part IXA) · 5th Sch. TACs · 6th Sch. ADCs")
          }),
        )
      }
    )

    #v(7pt)
    #sec-heading("Core Constitutional & Federal Organs Overview")
    #data-table(
      ("Organ / Tier", "Articles / Part", "Head & Structural Composition", "Primary Constitutional Mandate"),
      skeleton.union_organs_rows.map(r => (strong(r.organ), r.articles, r.head_and_composition, r.key_responsibility)),
      col-widths: (1.05fr, 0.85fr, 1.55fr, 1.75fr),
    )

    #pagebreak()

    #sec-heading("Constitutional Mechanics: Lists, Funds & Emergency Powers")
    #data-table(
      ("Axis", "Constitutional Mechanics & Prelims Anchors"),
      skeleton.schedule_summary.map(s => (strong(s.axis), s.detail)),
      col-widths: (1.2fr, 3.2fr),
    )

    #v(7pt)
    #sec-heading("Union Cabinet Committees (Extra-Constitutional Executive Nerve Centre)")
    #data-table(
      ("Cabinet Committee", "Chairperson", "Core Composition", "What It Controls"),
      skeleton.cabinet_committees.map(c => (strong(c.name), c.chair, c.members, c.role)),
      col-widths: (1.35fr, 0.95fr, 1.25fr, 1.85fr),
    )

    #v(6pt)
    #box(
      width: 100%,
      stroke: 0.9pt + rule-dark,
      fill: tint-panel,
      inset: 7pt,
      radius: 2pt,
      {
        text(font: font-sans, size: 8pt, weight: "bold", "PRELIMS STRUCTURAL TRAP: ")
        text(font: font-serif, size: 8.6pt, skeleton.skeleton_trap_note)
      }
    )
  ]
}
