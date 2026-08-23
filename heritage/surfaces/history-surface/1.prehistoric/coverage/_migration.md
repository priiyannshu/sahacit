# Migration Log — Prehistoric Era Setup (2026-04-17)

Records moves from `draft/universe.json` into era-specific structure under approach C (era + stage dual-axis).

## Source

`draft/universe.json` had 95 nodes tagged `era=prehistoric`:
- 55 history (legit core)
- 31 geography (mis-tagged — ocean currents, biomes, climate classification)
- 9 science (mis-tagged — evolution theory, fossils)

## Moves

### To `eras/1.prehistoric/prehistoric.json` — 46 nodes

All 55 history nodes **minus** 9 Mesopotamia nodes (bronze-age-urban, chronologically contemporary with Indus; staged for ancient_indus era).

Added per node: `stage` field (material-culture: paleolithic/mesolithic/neolithic/etc.), `_review_note` flag where ambiguous.

### To `eras/2.ancient-indus/_staged_nodes_from_prehistoric.json` — 9 nodes

Mesopotamia: hist_mesopotamia, hist_cuneiform, hist_clay_tablets, hist_sumerians, hist_uruk, hist_urbanisation_mesopotamia, hist_irrigation_mesopotamia, hist_social_hierarchy_mesopotamia, hist_trade_mesopotamia.

Pick up when ancient_indus era begins.

### To `processed/timeless/geography/` — 31 nodes, 5 chapter files

| File | Nodes | NCERT chapter |
|---|---|---|
| `11th_p1_ch12_world_climate_and_climate_change.json` | 12 | World Climate and Climate Change |
| `11th_p1_ch13_water_oceans.json` | 1 | Water (Oceans) |
| `11th_p1_ch14_movements_of_ocean_water.json` | 10 | Movements of Ocean Water |
| `11th_p1_ch15_life_on_the_earth.json` | 7 | Life on the Earth (biomes) |
| `11th_p2_ch04_climate.json` | 1 | India — Climate |

**Flag for later:** a few of these (Ice Ages, Milankovitch Cycles, Climate Change 12,000 years ago) have genuine prehistoric relevance. Can be re-promoted to prehistoric with dual-subject tag once timeline design lands.

### To `processed/timeless/science/` — 9 nodes, 2 chapter files

| File | Nodes | NCERT chapter |
|---|---|---|
| `12th_ch07_evolution.json` | 8 | Evolution (theories, mechanisms) |
| `10th_ch09_heredity_and_evolution.json` | 1 | Heredity and Evolution |

**Flag:** "Human Evolution" and "Fossils" from science bucket duplicate concepts already in prehistoric history. Resolve: either promote these two back to prehistoric or mark as cross-subject references.

## Edges

Of 8,470 edges in `draft/universe.json`, 97 touched a prehistoric-history node. 68 had both endpoints in the kept 46-node set — copied to `eras/1.prehistoric/prehistoric.json`. The other 29 touched outside nodes (Mesopotamia staging or other eras) — not copied; can be reconstructed when those eras are worked.

## PYQs

Of 2,839 PYQs, only 4 were linked to prehistoric-history nodes — and 3 of those 4 are false positives (matched on word "painting" but concern non-prehistoric paintings). Only PYQ 68 (Burzahom) is genuinely prehistoric.

Existing PYQ linkage is too sparse and noisy to trust. Will sweep fresh against node labels when work begins.

## What was NOT moved

- `draft/universe.json` itself — left untouched as historical baseline.
- Nodes in other eras, or with `era=None` — untouched.

## How to undo this migration

All moved nodes retain their original `id`. To revert, re-filter `draft/universe.json` for `era=prehistoric` and delete the new files. No data is lost.
