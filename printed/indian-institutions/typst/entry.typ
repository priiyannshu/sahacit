#import "theme.typ": *

#let identity-ribbon(inst) = {
  let a = inst.anchor
  box(
    width: 100%,
    stroke: (bottom: 1.2pt + rule-dark),
    inset: (bottom: 5pt),
    {
      grid(
        columns: (auto, 1fr),
        column-gutter: 10pt,
        align: (left + horizon, right + horizon),
        {
          text(font: font-mono, size: 7.4pt, fill: ink-soft, "#" + str(inst.order) + " · PART " + str(inst.part))
          h(6pt)
          status-pill(a.legal_status)
        },
        text(font: font-serif, size: 7.8pt, fill: ink-muted, "Est. " + a.established_year + " · " + a.headquarters),
      )
      v(3pt)
      text(font: font-sans, size: 14.5pt, weight: "bold", fill: ink, inst.name)
      if inst.acronym != "" and inst.acronym != inst.name {
        h(6pt)
        text(font: font-sans, size: 11pt, weight: "medium", fill: ink-soft, "(" + inst.acronym + ")")
      }
      v(2pt)
      grid(
        columns: (1fr, auto),
        column-gutter: 8pt,
        align: (left + horizon, right + horizon),
        {
          text(font: font-sans, size: 7.3pt, weight: "bold", fill: ink-soft, "MINISTRY / ANCHOR: ")
          text(font: font-sans, size: 7.6pt, weight: "bold", fill: ink, a.nodal_ministry)
        },
        stack(
          dir: ltr,
          spacing: 3pt,
          ..inst.links.upsc_categories.map(c => tag-pill(c))
        ),
      )
      v(3pt)
      box(
        width: 100%,
        stroke: (left: 2pt + rule-dark),
        fill: tint-subtle,
        inset: (x: 6pt, y: 3.5pt),
        {
          text(font: font-sans, size: 7.2pt, weight: "bold", fill: ink-soft, "ESSENCE: ")
          text(font: font-serif, size: 8.6pt, fill: ink, a.essential_summary)
        }
      )
    }
  )
}

#let traps-box(traps) = {
  block(
    width: 100%,
    stroke: 0.9pt + rule-dark,
    radius: 2pt,
    breakable: true,
    {
      block(
        width: 100%,
        fill: tint-panel,
        stroke: (bottom: 0.6pt + rule-mid),
        inset: (x: 7pt, y: 3.5pt),
        sticky: true,
        below: 0pt,
        text(font: font-sans, size: 8pt, weight: "bold", fill: ink, "UPSC PRELIMS TRAPS, NUANCES & LOOK-ALIKE TWINS")
      )
      block(width: 100%, inset: 6pt, above: 0pt, {
        bullet-list(traps.common_traps)
        if traps.twin_comparison.rows.len() > 0 {
          v(3pt)
          data-table(
            traps.twin_comparison.headers,
            traps.twin_comparison.rows,
            col-widths: auto,
          )
        }
      })
    }
  )
}

#let render-blueprint(inst) = {
  let a = inst.anchor
  let c = inst.composition
  let l = inst.lifecycle
  let m = inst.mandate
  let g = inst.genesis
  let lk = inst.links

  [
    #metadata(inst.id) #label("inst-" + inst.id)
    #identity-ribbon(inst)
    #v(5pt)

    // Vector lifecycle & command chain strip
    #text(font: font-sans, size: 6.8pt, weight: "bold", fill: ink-soft, tracking: 0.05em, "APPOINTMENT, TENURE & REMOVAL CHAIN")
    #v(2pt)
    #flow-strip((
      (label: "Selection Panel", text: l.selection_committee),
      (label: "Appointing Authority", text: l.appointing_authority),
      (label: "Tenure & Age Cap", text: l.tenure + " | Cap: " + l.age_limit),
      (label: "Exit & Removal", text: "Resigns: " + l.resignation_to + ". " + l.removal_procedure),
    ))
    #v(4pt)
    #text(font: font-sans, size: 6.8pt, weight: "bold", fill: ink-soft, tracking: 0.05em, "AUTHORITY, JURISDICTION & APPELLATE PATH")
    #v(2pt)
    #flow-strip((
      (label: "Nature of Power", text: m.power_nature),
      (label: "Reporting Chain", text: m.reporting_chain),
      (label: "Appellate Pathway", text: m.appellate_pathway),
    ))
    #v(5pt)

    // 2-Column Asymmetric Grid
    #grid(
      columns: (1.48fr, 1fr),
      column-gutter: 10pt,
      align: top,
      // Left Main Column
      {
        sec-heading("People Inside: Composition & Internal Wings")
        kv-item("Chairperson", c.chairperson)
        kv-item("Members", c.members)
        kv-item("Eligibility", c.eligibility_rules)
        kv-item("Wings / Benches", c.internal_wings)

        v(3pt)
        sec-heading("Who Handles What: Mandate & Statutory Powers")
        bullet-list(m.core_functions)
        kv-item("Special Powers", m.special_powers)
        kv-item("Jurisdiction Limits & Exclusions", m.jurisdiction_limits_and_exclusions)
      },
      // Right Contrast Rail
      {
        sec-heading("Legal Basis & Key Amendments")
        kv-item("Constitutional / Statutory Basis", a.basis)
        kv-item("Key Amendments", a.key_amendments)

        v(3pt)
        sec-heading("Post-Retirement & Safeguards")
        kv-item("Reappointment & Post-Term", l.reappointment_and_post_retirement)
        kv-item("Funding & Salary", l.funding_and_salary)

        v(3pt)
        sec-heading("Genesis & Landmark SC Verdicts")
        kv-item("Founding Committee", g.founding_committee)
        bullet-list(g.landmark_cases)
      }
    )

    #v(3pt)
    #box(
      width: 100%,
      stroke: 0.5pt + rule-mid,
      fill: tint-subtle,
      radius: 2pt,
      inset: (x: 6pt, y: 4pt),
      grid(
        columns: (1fr, 1fr),
        column-gutter: 10pt,
        {
          text(font: font-sans, size: 7.5pt, weight: "bold", fill: ink, "STATE COUNTERPARTS: ")
          text(font: font-serif, size: 8.3pt, fill: ink, lk.state_counterparts)
        },
        {
          text(font: font-sans, size: 7.5pt, weight: "bold", fill: ink, "LINKED ACTS & MISSIONS: ")
          text(font: font-serif, size: 8.3pt, fill: ink, lk.linked_acts_and_missions)
        }
      )
    )

    #v(4pt)
    #traps-box(inst.traps)
  ]
}

#let render-dossier(inst) = {
  let a = inst.anchor
  let c = inst.composition
  let l = inst.lifecycle
  let m = inst.mandate
  let g = inst.genesis
  let lk = inst.links

  [
    #metadata(inst.id) #label("inst-" + inst.id)
    #identity-ribbon(inst)
    #v(5pt)

    // Full-width Quick Legal & Lifecycle Matrix
    #data-table(
      ("Legal Basis & Amendments", "Selection & Appointment", "Tenure, Age & Reappointment", "Removal, Salary & Safeguards"),
      ((
        a.basis + "\n" + a.key_amendments,
        l.selection_committee + "\nAppointed by: " + l.appointing_authority,
        "Term: " + l.tenure + " | Cap: " + l.age_limit + "\n" + l.reappointment_and_post_retirement,
        "Resigns: " + l.resignation_to + "\nRemoval: " + l.removal_procedure + "\nFunding: " + l.funding_and_salary,
      ),),
      col-widths: (1.1fr, 1fr, 0.95fr, 1.15fr),
    )

    #v(4pt)
    #sec-heading("People Inside: Composition, Roles & Internal Organs")
    #grid(
      columns: (1fr, 1fr),
      column-gutter: 10pt,
      {
        kv-item("Chairperson / Presiding Authority", c.chairperson)
        kv-item("Members & Quotas", c.members)
      },
      {
        kv-item("Eligibility & Disqualifications", c.eligibility_rules)
        kv-item("Internal Wings / Sub-Organs", c.internal_wings)
      }
    )

    #v(4pt)
    #sec-heading("Who Handles What: Mandate, Powers, Jurisdiction & Appellate Path")
    #bullet-list(m.core_functions)
    #grid(
      columns: (1fr, 1fr),
      column-gutter: 10pt,
      {
        kv-item("Power Nature", m.power_nature)
        kv-item("Special Powers", m.special_powers)
      },
      {
        kv-item("Limits & Exclusions", m.jurisdiction_limits_and_exclusions)
        kv-item("Reporting & Appellate Path", m.reporting_chain + " | Appeals: " + m.appellate_pathway)
      }
    )

    // Extra structured comparison/detail tables for mega dossiers
    #if "extra_tables" in inst {
      for tbl in inst.extra_tables {
        v(4pt)
        sec-heading(tbl.title)
        data-table(tbl.headers, tbl.rows, col-widths: auto)
      }
    }

    #v(4pt)
    #grid(
      columns: (1.15fr, 1fr),
      column-gutter: 10pt,
      {
        sec-heading("Genesis Committee & Landmark Verdicts")
        kv-item("Founding Genesis", g.founding_committee)
        bullet-list(g.landmark_cases)
      },
      {
        sec-heading("State Counterparts & Ecosystem Links")
        kv-item("State Counterparts", lk.state_counterparts)
        kv-item("Connected Acts, Missions & Books", lk.linked_acts_and_missions)
      }
    )

    #v(5pt)
    #traps-box(inst.traps)
  ]
}

#let render-compact(inst) = {
  let a = inst.anchor
  let c = inst.composition
  let l = inst.lifecycle
  let m = inst.mandate
  let g = inst.genesis
  let lk = inst.links

  [
    #metadata(inst.id) #label("inst-" + inst.id)
    #block(
      width: 100%,
      stroke: 0.75pt + rule-dark,
      radius: 2pt,
      inset: 7pt,
      breakable: false,
      {
        grid(
          columns: (auto, 1fr),
          column-gutter: 8pt,
          align: (left + horizon, right + horizon),
          {
            text(font: font-mono, size: 7pt, fill: ink-soft, "#" + str(inst.order) + " · PART " + str(inst.part))
            h(5pt)
            status-pill(a.legal_status)
          },
          text(font: font-sans, size: 7.1pt, weight: "bold", fill: ink-muted, a.nodal_ministry + " · Est. " + a.established_year),
        )
        v(2pt)
        text(font: font-sans, size: 11.5pt, weight: "bold", fill: ink, inst.name + " (" + inst.acronym + ")")
        v(2pt)
        box(
          width: 100%,
          fill: tint-subtle,
          stroke: (left: 1.5pt + rule-dark),
          inset: (x: 5pt, y: 2.5pt),
          text(font: font-serif, size: 8.2pt, a.essential_summary)
        )
        v(3pt)
        grid(
          columns: (1.15fr, 1fr),
          column-gutter: 8pt,
          {
            kv-item("Legal Basis & Amendments", a.basis + " | " + a.key_amendments)
            kv-item("People Inside", c.chairperson + "; " + c.members + " (" + c.internal_wings + ")")
            kv-item("Eligibility", c.eligibility_rules)
            block(above: 1.5pt, below: 2pt, {
              text(font: font-sans, size: 7.8pt, weight: "bold", fill: ink, "Mandate & Powers: ")
              for (i, x) in m.core_functions.enumerate() {
                if i > 0 { text(font: font-serif, size: 8.4pt, " · ") }
                if type(x) == dictionary {
                  text(font: font-sans, size: 7.7pt, weight: "bold", fill: ink, x.label + ": ")
                  text(font: font-serif, size: 8.4pt, fill: ink, x.text)
                } else {
                  text(font: font-serif, size: 8.4pt, fill: ink, x)
                }
              }
            })
          },
          {
            kv-item("Selection & Appointment", l.selection_committee + " → " + l.appointing_authority)
            kv-item("Term, Cap & Exit", l.tenure + " / " + l.age_limit + " | Resigns: " + l.resignation_to + " | " + l.removal_procedure)
            kv-item("Limits, Reports & Appeals", m.jurisdiction_limits_and_exclusions + " | Appeals: " + m.appellate_pathway)
            kv-item("Genesis & Cases", g.founding_committee + " | " + g.landmark_cases.map(x => if type(x) == dictionary { x.label + ": " + x.text } else { x }).join("; "))
            kv-item("State & Links", lk.state_counterparts + " | " + lk.linked_acts_and_missions)
          }
        )
        v(3pt)
        traps-box(inst.traps)
      }
    )
  ]
}

#let render-institution(inst) = {
  if inst.layout_mode == "blueprint" {
    render-blueprint(inst)
  } else if inst.layout_mode == "dossier" {
    render-dossier(inst)
  } else {
    render-compact(inst)
  }
}
