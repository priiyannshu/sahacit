#import "theme.typ": *
#import "skeleton.typ": render-state-skeleton
#import "entry.typ": render-institution
#import "indexes.typ": render-indexes

#let payload = json("/generated/book_payload.json")

#set document(
  title: payload.meta.title,
  author: "Republic of India Institutional Atlas",
)

#set text(font: font-serif, size: 9pt, fill: ink, lang: "en")
#set par(leading: 0.56em, justify: false)

// A4 Duplex Spiral/Binder-Ready Page Setup with Mirrored Gutters (19mm inside, 11mm outside)
#set page(
  paper: "a4",
  margin: (inside: 19mm, outside: 11mm, top: 13mm, bottom: 13mm),
  header: context {
    let pg = here().page()
    if pg <= 1 { return }
    let hdr = if calc.odd(pg) {
      grid(
        columns: (1fr, auto),
        text(font: font-sans, size: 7.2pt, fill: ink-soft, "INDIAN INSTITUTIONS"),
        text(font: font-sans, size: 7.2pt, weight: "medium", fill: ink-muted, payload.meta.header_right),
      )
    } else {
      grid(
        columns: (auto, 1fr),
        text(font: font-sans, size: 7.2pt, weight: "medium", fill: ink-muted, payload.meta.header_right),
        align(right, text(font: font-sans, size: 7.2pt, fill: ink-soft, "INDIAN INSTITUTIONS")),
      )
    }
    stack(spacing: 2.5pt, hdr, line(length: 100%, stroke: 0.4pt + rule-light))
  },
  footer: context {
    let pg = here().page()
    if pg <= 1 { return }
    let pnum = str(counter(page).get().first())
    let ftr = if calc.odd(pg) {
      align(right, text(font: font-sans, size: 8pt, weight: "bold", fill: ink, pnum))
    } else {
      align(left, text(font: font-sans, size: 8pt, weight: "bold", fill: ink, pnum))
    }
    stack(spacing: 2.5pt, line(length: 100%, stroke: 0.4pt + rule-light), ftr)
  }
)

// ==================== TITLE PAGE & CONTENTS ====================
#v(6pt)
#text(font: font-sans, size: 8.5pt, weight: "bold", fill: ink-soft, tracking: 0.14em, "ATLAS OF THE INDIAN STATE")
#v(2pt)
#text(font: font-sans, size: 25pt, weight: "bold", fill: ink, "INDIAN INSTITUTIONS")
#v(-3pt)
#text(font: font-serif, size: 11pt, style: "italic", fill: ink-muted, payload.meta.subtitle)
#v(5pt)
#line(length: 100%, stroke: 1.4pt + rule-dark)
#v(7pt)

#sec-heading("Contents & Institutional Index (" + str(payload.meta.total_roster_count) + " Institutions Across 7 Functional Pillars)")
#v(2pt)

#for part in payload.roster.parts {
  block(
    width: 100%,
    breakable: true,
    above: 3.5pt,
    below: 3.5pt,
    {
      box(
        width: 100%,
        fill: tint-panel,
        stroke: (top: 0.8pt + rule-dark, bottom: 0.5pt + rule-mid),
        inset: (x: 6pt, y: 2.8pt),
        grid(
          columns: (1fr, auto),
          text(font: font-sans, size: 7.8pt, weight: "bold", "PART " + part.roman + " · " + upper(part.title)),
          text(font: font-mono, size: 6.9pt, fill: ink-muted, str(part.entries.len()) + " entries")
        )
      )
      v(2pt)
      columns(2, gutter: 10pt, {
        for e in part.entries {
          block(above: 0.8pt, below: 1.2pt, {
            if e.populated {
              text(font: font-mono, size: 6.9pt, weight: "bold", "#" + str(e.order) + " ")
              text(font: font-sans, size: 7.4pt, weight: "bold", fill: ink, e.name)
              h(4pt)
              text(font: font-sans, size: 7pt, weight: "bold", fill: ink-muted, "p. " + page-ref-for(e.id))
            } else {
              text(font: font-mono, size: 6.8pt, fill: ink-soft, "#" + str(e.order) + " ")
              text(font: font-serif, size: 7.4pt, fill: ink-muted, e.name + " [" + e.status + "]")
            }
          })
        }
      })
    }
  )
}

// ==================== FRONT MATTER: SKELETON OF THE INDIAN STATE ====================
#pagebreak(to: "odd")
#render-state-skeleton(payload.state_skeleton)

// ==================== BODY: FUNCTIONAL PARTS ====================
#let insts-by-part = (:)
#for inst in payload.institutions {
  let k = str(inst.part)
  let arr = insts-by-part.at(k, default: ())
  arr.push(inst)
  insts-by-part.insert(k, arr)
}

#for part in payload.roster.parts {
  let pkey = str(part.part_number)
  let entries = insts-by-part.at(pkey, default: ())
  if entries.len() > 0 {
    pagebreak(to: "odd")
    // Crisp Part Banner at top of Part's opening recto page
    box(
      width: 100%,
      stroke: (top: 1.5pt + rule-dark, bottom: 1pt + rule-dark),
      fill: tint-subtle,
      inset: (x: 8pt, y: 6pt),
      {
        text(font: font-sans, size: 8pt, weight: "bold", fill: ink-soft, tracking: 0.08em, "FUNCTIONAL PILLAR · PART " + part.roman)
        linebreak()
        text(font: font-sans, size: 15pt, weight: "bold", fill: ink, part.title)
        linebreak()
        text(font: font-serif, size: 8.8pt, style: "italic", fill: ink-muted, part.subtitle)
      }
    )
    v(8pt)
    for idx in range(entries.len()) {
      let inst = entries.at(idx)
      if idx > 0 {
        // Non-compact entries start fresh page; compact entries flow cleanly together
        let prev = entries.at(idx - 1)
        if inst.layout_mode != "compact" or prev.layout_mode != "compact" {
          pagebreak()
        } else {
          v(8pt)
        }
      }
      render-institution(inst)
    }
  }
}

// ==================== BACK MATTER: MASTER CROSS-INDEXES ====================
#pagebreak(to: "odd")
#render-indexes(payload)
