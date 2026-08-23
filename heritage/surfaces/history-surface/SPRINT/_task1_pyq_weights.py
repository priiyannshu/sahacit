"""Task 1 — PYQ-entity mapping & frequency weighting.

Heterogeneous PYQ JSONs per era → uniform pool → word-boundary regex
matching against normalized era-node labels → per-era weighted entity list.

Output: HISTORY_SPRINT_PYQ_WEIGHTS.json (data) + .md (summary).
"""
import json, re, sys
from pathlib import Path
from collections import defaultdict, Counter

HERE = Path(__file__).parent

ERAS = [
    ('1.prehistoric',       'prehistoric'),
    ('2.ancient-indus',     'ancient-indus'),
    ('3.ancient-classical', 'ancient-classical'),
    ('4.early-medieval',    'early-medieval'),
    ('5.delhi-sultanate',   'delhi-sultanate'),
    ('6.mughal',            'mughal'),
    ('7.early-colonial',    'early-colonial'),
    ('8.high-colonial',     'high-colonial'),
    ('9.freedom-struggle',  'freedom-struggle'),
    ('10.post-independence','post-independence'),
    ('11.contemporary',     'contemporary'),
]


def pool_from(d):
    """Flat list of PYQ dicts regardless of file shape."""
    if isinstance(d, list): return d
    for k in ('pyqs', 'questions'):
        if k in d and isinstance(d[k], list):
            return list(d[k])
    out = []
    for k in ('high','medium','boundary','slip_through',
              'pyqs_high','pyqs_medium','pyqs_boundary','pyqs_slip_through'):
        if k in d and isinstance(d[k], list):
            out.extend(d[k])
    return out


# Aliases tuned to known patterns. Conservative — fewer false positives.
# Each entry: { primary_substring: [extra_aliases] }
MANUAL_ALIAS_BOOSTS = {
    # year parens stripped automatically; these are name-collapse aliases
}

# Stop-aliases — labels too generic to match on without false positives.
GENERIC_STOP = {
    'india','indian','indians','empire','state','war','battle','battle of',
    'system','culture','painting','school','art','architecture','dynasty',
    'kingdom','reform','reforms','movement','council','committee','party',
    'government','administration','society','economy','trade','agriculture',
    'religion','language','region','period','age','era','revolution',
}


def normalize_label(label):
    """Return (primary, aliases) — all lowercase, suitable for word-boundary regex.

    Conservative: strip year-parens; strip trailing non-year qualifier paren
    (e.g. "Gol Gumbaz (Bijapur)" → "Gol Gumbaz") but do NOT introduce the
    inside-paren term as an alias (it likely has its own node). Only safe
    rewrite: collapse "X's Y" → "Xs Y" punctuation variant so a PYQ writing
    "Akbars" matches "Akbar's" without bleeding into a separate "Akbar" node.
    """
    if not label: return None, []
    orig = label.strip()
    # Strip year-range parens: "Akbar (1556-1605)" → "Akbar"
    s = re.sub(r'\s*\(\s*\d{2,4}[^)]*\)\s*$', '', orig)
    # Strip non-year trailing qualifier paren without keeping it as alias.
    s = re.sub(r'\s*\(([^)]+)\)\s*$', '', s)
    primary = s.lower().strip()
    aliases = set()
    # Punctuation variant only: "akbar's social reforms" → "akbars social reforms".
    # Does NOT introduce the bare first word as a separate alias.
    if "'" in primary:
        aliases.add(primary.replace("'", ""))
    aliases = {a for a in aliases
               if a and len(a) >= 4 and a not in GENERIC_STOP and a != primary}
    return primary, sorted(aliases)


def build_node_index(nodes):
    """Return list of (node, primary, [aliases], compiled_pattern)."""
    out = []
    for n in nodes:
        primary, aliases = normalize_label(n.get('label', ''))
        if not primary: continue
        if primary in GENERIC_STOP: continue
        if len(primary) < 4: continue
        terms = [primary] + aliases
        # Sort longest first so the regex prefers longer multi-word matches
        terms = sorted(set(terms), key=lambda s: -len(s))
        pat = re.compile(
            r'\b(' + '|'.join(re.escape(t) for t in terms) + r')\b',
            re.IGNORECASE,
        )
        out.append({
            'node': n,
            'primary': primary,
            'aliases': aliases,
            'pattern': pat,
        })
    return out


def pyq_text(q):
    """Concatenate question + options text for matching."""
    parts = [q.get('question') or '']
    opts = q.get('options') or {}
    if isinstance(opts, dict):
        parts.extend(str(v) for v in opts.values() if v)
    elif isinstance(opts, list):
        parts.extend(str(v) for v in opts if v)
    return ' '.join(parts)


def main():
    out = {
        'metadata': {
            'task': 'Task 1 — PYQ-entity frequency weighting',
            'method': 'word-boundary regex of normalized node labels (+ aliases) vs question+options text. Stop-list filters generic single-word labels.',
            'generated': '2026-05-16',
            'per_era': {},
        },
        'eras': {},
    }
    grand_pyq = 0
    grand_nodes_matched = 0

    for slug, era in ERAS:
        era_dir = HERE / slug
        era_json = era_dir / f'{era}.json'
        pyq_json = era_dir / f'pyqs_{era}_era.json'
        with open(era_json) as fh: era_data = json.load(fh)
        with open(pyq_json) as fh: pyq_data = json.load(fh)

        nodes = era_data.get('nodes', [])
        pool = pool_from(pyq_data)
        idx = build_node_index(nodes)

        node_pyq_ids = defaultdict(set)  # node_id → set of pyq ids
        list_qs = []   # PYQs with >5 distinct node matches
        zero_qs = 0

        for q in pool:
            qid = q.get('id')
            txt = pyq_text(q)
            hits = set()
            for entry in idx:
                if entry['pattern'].search(txt):
                    hits.add(entry['node']['id'])
            if not hits:
                zero_qs += 1
            if len(hits) > 5:
                list_qs.append({'id': qid, 'n_hits': len(hits)})
            for nid in hits:
                node_pyq_ids[nid].add(qid)

        # Build weighted list
        node_by_id = {n['id']: n for n in nodes}
        weighted = []
        for nid, qids in node_pyq_ids.items():
            n = node_by_id[nid]
            weighted.append({
                'node_id': nid,
                'label': n.get('label'),
                'type': n.get('type'),
                'pyq_count': len(qids),
                'pyq_ids': sorted(qids),
            })
        weighted.sort(key=lambda r: (-r['pyq_count'], r['node_id']))

        out['eras'][era] = {
            'nodes_total': len(nodes),
            'pyqs_pool': len(pool),
            'pyqs_with_zero_hits': zero_qs,
            'pyqs_likely_list_questions': list_qs[:25],
            'weighted_nodes': weighted,
        }
        out['metadata']['per_era'][era] = {
            'nodes_total': len(nodes),
            'nodes_matched': len(weighted),
            'pyqs_pool': len(pool),
            'pyqs_zero': zero_qs,
            'pyqs_list_questions': len(list_qs),
        }
        grand_pyq += len(pool)
        grand_nodes_matched += len(weighted)
        print(f'{slug:25} pool={len(pool):4} nodes_matched={len(weighted):4}/{len(nodes):4}  zero={zero_qs:3}  list_qs={len(list_qs)}')

    print(f'\nTotals: {grand_pyq} PYQs processed; {grand_nodes_matched} (node,era) entries weighted')

    out_path = HERE.parent / 'HISTORY_SPRINT_PYQ_WEIGHTS.json'
    with open(out_path, 'w') as fh:
        json.dump(out, fh, indent=2, ensure_ascii=False)
    print(f'Wrote {out_path}')


if __name__ == '__main__':
    main()
