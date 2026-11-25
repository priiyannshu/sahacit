#import "theme.typ": *

#let render-indexes(payload) = {
  let idx = payload.indexes
  [
    #metadata("master-indexes") <master-indexes>
    #text(font: font-sans, size: 8pt, weight: "bold", fill: ink-soft, tracking: 0.08em, "REFERENCE INDEXES · CROSS-CLASSIFICATION TABLES")
    #v(-4pt)
    #text(font: font-sans, size: 17pt, weight: "bold", fill: ink, "Master Cross-Indexes")
    #v(-4pt)
    #text(font: font-serif, size: 9.5pt, style: "italic", fill: ink-muted, "Cross-referenced by enabling legal basis, nodal ministry, appointment mechanics, appellate forums, and title.")
    #v(4pt)
    #line(length: 100%, stroke: 1.2pt + rule-dark)
    #v(6pt)

    #sec-heading("Index A · Legal Origin & Enabling Anchor")
    #for grp in idx.legal_status_groups {
      text(font: font-sans, size: 8pt, weight: "bold", fill: ink, grp.status)
      v(2pt)
      data-table(
        ("#", "Institution", "Constitutional Article / Enabling Act", "Nodal Ministry", "Pg"),
        grp.items.map(it => (
          "#" + str(it.order),
          strong(it.name) + " (" + it.acronym + ")",
          it.basis,
          it.nodal_ministry,
          page-ref-for(it.id),
        )),
        col-widths: (28pt, 1.4fr, 1.5fr, 1.1fr, 24pt),
      )
      v(4pt)
    }

    #sec-heading("Index B · Nodal Ministry-to-Institution Matrix")
    #data-table(
      ("Nodal Ministry / Sovereign Anchor", "Institutions Under Jurisdiction"),
      idx.ministry_groups.map(mg => (
        strong(mg.ministry),
        mg.items.map(i => "#" + str(i.order) + " " + i.name + " (" + i.acronym + ")").join("  |  "),
      )),
      col-widths: (1.5fr, 2.8fr),
    )

    #v(5pt)
    #sec-heading("Index C · Selection Panels, Tenure, Age Caps & Removal Matrix")
    #data-table(
      ("Institution", "Selection Committee", "Appointment", "Tenure / Cap", "Removal & Reappointment"),
      idx.lifecycle_matrix.map(r => (
        strong(r.acronym) + "\n" + text(size: 7.4pt, r.name),
        r.selection_committee,
        r.appointing_authority,
        r.tenure + "\n(" + r.age_limit + ")",
        r.removal + "\nReappt: " + r.reappointment,
      )),
      col-widths: (1.05fr, 1.25fr, 0.85fr, 0.75fr, 1.35fr),
    )

    #v(5pt)
    #sec-heading("Index D · Power Nature, Reporting & Appellate Pathways")
    #data-table(
      ("Institution", "Power Nature", "Reporting Chain", "Appellate Pathway"),
      idx.appellate_matrix.map(r => (
        strong(r.acronym),
        r.power_nature,
        r.reporting_chain,
        r.appellate_pathway,
      )),
      col-widths: (0.75fr, 1.25fr, 1.2fr, 1.3fr),
    )

    #v(5pt)
    #sec-heading("Index E · Alphabetical Quick Lookup")
    #data-table(
      ("Institution Name", "Acronym", "Part", "Legal Status", "Pg"),
      idx.alphabetical.map(a => (
        strong(a.name),
        a.acronym,
        "Part " + str(a.part),
        a.legal_status,
        page-ref-for(a.id),
      )),
      col-widths: (2fr, 0.75fr, 0.55fr, 0.9fr, 26pt),
    )
  ]
}
