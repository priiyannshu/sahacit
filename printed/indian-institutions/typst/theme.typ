// Monochrome, ink-efficient print design tokens & reusable primitives for A4 duplex print

#let ink = rgb("#111111")
#let ink-muted = rgb("#4a4a4a")
#let ink-soft = rgb("#6b6b6b")
#let rule-dark = rgb("#1a1a1a")
#let rule-mid = rgb("#8a8a8a")
#let rule-light = rgb("#c8c8c8")
#let tint-subtle = rgb("#f6f6f6")
#let tint-panel = rgb("#ededed")

#let font-serif = "Libertinus Serif"
#let font-sans = "Roboto"
#let font-mono = "DejaVu Sans Mono"

#let status-pill(label-text) = {
  box(
    stroke: 0.85pt + rule-dark,
    fill: tint-panel,
    radius: 2pt,
    inset: (x: 5pt, y: 2pt),
    text(font: font-sans, size: 7.2pt, weight: "bold", fill: ink, upper(label-text)),
  )
}

#let tag-pill(label-text) = {
  box(
    stroke: 0.5pt + rule-mid,
    fill: white,
    radius: 2pt,
    inset: (x: 4pt, y: 1.5pt),
    text(font: font-sans, size: 6.8pt, fill: ink-muted, label-text),
  )
}

#let sec-heading(title) = {
  block(above: 7pt, below: 4pt, sticky: true, {
    text(font: font-sans, size: 8.1pt, weight: "bold", fill: ink, tracking: 0.04em, upper(title))
    v(-4pt)
    line(length: 100%, stroke: 0.7pt + rule-dark)
  })
}

#let kv-item(k, v) = {
  block(above: 2pt, below: 3pt, {
    text(font: font-sans, size: 7.9pt, weight: "bold", fill: ink, k + ": ")
    text(font: font-serif, size: 8.7pt, fill: ink, v)
  })
}

#let bullet-list(items) = {
  for item in items {
    block(above: 1.5pt, below: 2.3pt, inset: (left: 8pt), {
      place(dx: -8pt, dy: 0pt, text(font: font-sans, size: 8pt, weight: "bold", "▪"))
      if type(item) == dictionary {
        text(font: font-sans, size: 7.9pt, weight: "bold", fill: ink, item.label + ": ")
        text(font: font-serif, size: 8.7pt, fill: ink, item.text)
      } else {
        text(font: font-serif, size: 8.7pt, fill: ink, item)
      }
    })
  }
}

#let flow-box(step-label, body-text) = {
  box(
    width: 100%,
    stroke: 0.65pt + rule-mid,
    fill: tint-subtle,
    radius: 2pt,
    inset: (x: 5pt, y: 4pt),
    {
      text(font: font-sans, size: 6.5pt, weight: "bold", fill: ink-soft, upper(step-label))
      linebreak()
      v(1pt)
      text(font: font-serif, size: 7.9pt, fill: ink, body-text)
    },
  )
}

#let flow-strip(steps) = {
  let cols = ()
  for idx in range(steps.len()) {
    cols.push(1fr)
    if idx < steps.len() - 1 {
      cols.push(10pt)
    }
  }
  let cells = ()
  for idx in range(steps.len()) {
    let s = steps.at(idx)
    cells.push(flow-box(s.label, s.text))
    if idx < steps.len() - 1 {
      cells.push(align(center + horizon, text(font: font-sans, size: 9pt, weight: "bold", fill: ink-muted, "→")))
    }
  }
  grid(columns: cols, column-gutter: 2pt, align: top, ..cells)
}

#let data-table(headers, rows, col-widths: auto) = {
  let widths = if col-widths == auto { (1fr,) * headers.len() } else { col-widths }
  show table.cell: set block(breakable: false)
  table(
    columns: widths,
    stroke: (x, y) => (
      top: if y == 0 { 0.9pt + rule-dark } else { 0.4pt + rule-light },
      bottom: if y == 0 { 0.8pt + rule-dark } else { 0.4pt + rule-light },
      left: 0.35pt + rule-light,
      right: 0.35pt + rule-light,
    ),
    fill: (x, y) => if y == 0 { tint-panel } else if calc.odd(y) { white } else { tint-subtle },
    inset: (x: 5.5pt, y: 3.6pt),
    align: left + top,
    table.header(
      ..headers.map(h => text(font: font-sans, size: 7.4pt, weight: "bold", fill: ink, h))
    ),
    ..rows.flatten().map(c => text(font: font-serif, size: 8.1pt, fill: ink)[#c]),
  )
}

#let page-ref-for(inst-id) = context {
  let hits = query(label("inst-" + inst-id))
  if hits.len() > 0 {
    str(counter(page).at(hits.first().location()).first())
  } else {
    "—"
  }
}
