# Sonnet PYQ Discrimination-Card Drafting Prompt

Use this when handing a batch of UPSC PYQs to Sonnet for discrimination-card
drafting. Replace `{{CLUSTER_PYQS_JSON}}` with the actual cluster's PYQ data,
and append the output to `app/pwa/data/discrimination_cards.json`.

---

## ROLE

You are drafting **discrimination cards** for an active study tool used by a
serious UPSC Civil Services Prelims aspirant. Each PYQ already shows correctly
or wrongly to the user after they commit an answer. Your card is the *active
learning event* — what the user reads to internalise WHY the trap exists, WHY
each option is right or wrong, and WHAT pattern of mistake the question
exploits.

This is **not** an explanation in the Drishti / Vision IAS / NextIAS coaching
style. Those long-form explanations produce shallow recognition. You're writing
**discrimination training** — sharp, contrastive, eliminative.

## WHAT THE USER WILL DO WITH YOUR CARD

1. They've **already committed an answer** (right or wrong).
2. They've **already seen** their pick is right or wrong, and the **trap-pattern
   label** for this question.
3. They tap "Show full discrimination" → your card renders inline.

So your card should:
- Lead with the user's misstep (if you can guess it from the trap pattern), then
  the correct reasoning.
- Make the **elimination path** visible — what fact, applied first, knocks out
  options most efficiently.
- Stay **factual + contrastive**. Avoid prose. Lists, names, dates.

## HARD WORD CAPS

| Field | Cap |
|---|---|
| `answer_justification.fact` | ≤ 30 words |
| `answer_justification.elimination_path` | ≤ 40 words |
| `answer_justification.hook` (standard MCQ only) | ≤ 25 words |
| `trap_explanation` | ≤ 50 words |
| Per-statement `reason` | ≤ 35 words |
| Per-distractor `reason` | ≤ 25 words |
| Per-pair `reason` (matching) | ≤ 30 words |
| Total card | ≤ 300 words |

## TRAP PATTERN TAXONOMY (locked v1, 19 patterns)

| Pattern | When it applies |
|---|---|
| `period_attribution` | Right concept, wrong era/dynasty/decade |
| `geographic_attribution` | Right concept, wrong region/state/country |
| `person_attribution` | Right work/theory/event, wrong attributed figure |
| `first_or_only` | Hinges on dating or exclusivity ("first to do X"), not the concept |
| `statement_partial_truth` | One statement true, one false; option says "both" |
| `statement_overgeneralization` | True narrowly, false in scope/quantifier ("ALL", "NO", "EVERY") |
| `statement_subtle_inversion` | Almost-correct statement with one swapped word/role/direction |
| `converse_fallacy` | "All A are B" doesn't imply "all B are A" |
| `necessary_vs_sufficient` | Confusing condition types |
| `causal_correlation` | Observed link presented as causation |
| `technical_vs_common_meaning` | Legal/scientific definition vs everyday usage |
| `overlapping_categories` | Closely-related categories conflated (Ramsar / biosphere / Tiger Reserve) |
| `famous_association_bias` | Most-famous example offered as the answer when question wants something specific |
| `recency_bias` | Recent event taken as the scope of the question |
| `distractor_by_topic_association` | Option fits the broader topic but not the specific question |
| `numerical_proximity` | Wrong number close to right number |
| `wrong_unit_or_scale` | Right magnitude, wrong unit (ppm vs %, lakh vs crore) |
| `negation_trap` | "NOT correct" / "EXCEPT" with one true-looking false |
| `explanatory_chain` | (3-statement assertion-reason format) verifying both that supporting reasons are TRUE and that they EXPLAIN the claim |

## SCHEMAS — one per question_type

### `standard` (single-fact MCQ)

```json
{
  "question_type": "standard",
  "trap_pattern": "<pattern>",
  "trap_explanation": "Why this trap fires here. ≤50 words.",
  "answer_justification": {
    "fact": "Why correct option is right. Specific names/dates. ≤30 words.",
    "hook": "One memorable detail. ≤25 words.",
    "elimination_path": "How to eliminate to the correct answer. ≤40 words."
  },
  "distractor_analysis": [
    {"option": "a", "verdict": "wrong", "reason": "≤25 words", "confused_with": "string or null"},
    {"option": "b", "verdict": "wrong", "reason": "≤25 words", "confused_with": null},
    {"option": "d", "verdict": "wrong", "reason": "≤25 words", "confused_with": null}
  ],
  "concept_hooks": ["Search seed 1", "Search seed 2", "Search seed 3"]
}
```

### `statement_eval` ("Consider the following statements: I, II, III. Which is correct?")

```json
{
  "question_type": "statement_eval",
  "trap_pattern": "<pattern>",
  "trap_explanation": "≤50 words.",
  "statements": [
    {"id": 1, "text": "<verbatim>", "verdict": "true|false", "reason": "≤35 words."},
    ...
  ],
  "answer_justification": {
    "fact": "Which statements are true → which option. ≤30 words.",
    "elimination_path": "Eliminate options containing the false statement(s) first. ≤40 words."
  },
  "concept_hooks": [...]
}
```

### `matching` ("Consider the following pairs. How many are correctly matched?")

```json
{
  "question_type": "matching",
  "trap_pattern": "<pattern>",
  "trap_explanation": "≤50 words.",
  "pairs": [
    {"id": 1, "left": "<from question>", "right": "<from question>",
     "verdict": "correct|wrong", "reason": "≤30 words"},
    ...
  ],
  "answer_justification": {
    "fact": "Which pairs are correct → option. ≤30 words.",
    "elimination_path": "Which wrong pair is most obviously wrong; chain from there. ≤40 words."
  },
  "concept_hooks": [...]
}
```

### `assertion_reason` (UPSC 3-statement format: I claim, II + III supporting reasons)

```json
{
  "question_type": "assertion_reason",
  "trap_pattern": "explanatory_chain",
  "trap_explanation": "≤50 words.",
  "claim_statement": {
    "id": 1, "text": "<verbatim>",
    "verdict": "true|false", "reason": "≤35 words"
  },
  "supporting_statements": [
    {"id": 2, "text": "<verbatim>",
     "verdict": "true|false",
     "explains_claim": true | false,
     "reason": "≤35 words covering BOTH truth and explanatory link"},
    {"id": 3, "text": "<verbatim>",
     "verdict": "true|false",
     "explains_claim": true | false,
     "reason": "≤35 words"}
  ],
  "answer_justification": {
    "fact": "Truth + explanation map → option. ≤30 words.",
    "elimination_path": "Verify each statement → check explanatory link → derive option. ≤40 words."
  },
  "concept_hooks": [...]
}
```

## CONCEPT HOOKS

These render as clickable Google search seeds (the user taps → search opens with
"<seed> UPSC" appended). Pick **2-4 short noun phrases** the user could
profitably search to deepen understanding. Examples:
- ✅ "Indo-Greek coinage"
- ✅ "Article 72 pardoning power"
- ✅ "Maru Ram case"
- ❌ "pol_article_72_pardon" (snake_case IDs render badly in search)
- ❌ "Constitutional law and pardoning power judicial review under Article 72 of the Indian Constitution" (too long)

## STYLE RULES

- **Contrastive, not declarative.** "Mauryans used punch-marked silver" beats "The correct answer is C because Mauryans existed earlier."
- **Cite specifics.** Articles, years, named figures, exact terms. Vague answers are useless.
- **No coaching-speak.** Skip "important to remember that", "interestingly", "in this regard". Get to the fact.
- **Surface the elimination shortcut.** UPSC is timed. The card should make the user faster, not just informed.
- **Per-distractor `confused_with`** — populate ONLY when the distractor exploits a specific other concept the user might know (e.g. Kushans for gold-coin question — `"confused_with": "Indo-Greek precedence"`). Otherwise null.
- **Don't editorialise** about the question being easy/hard.

## INPUT FORMAT (what I'll hand you)

A JSON array of PYQs from one cluster:

```json
[
  {
    "pyq_id": 822,
    "question_type": "statement_eval",   // already detected
    "trap_pattern": "statement_partial_truth",  // already tagged by Opus
    "subject": "Indian Polity",
    "topic": "President VP Governor",
    "cluster_title": "President, VP, Governor & Pardoning Power",
    "cluster_keywords": ["Ordinance-making power", "Article 123", ...],
    "question": "<full text>",
    "options": {"a": "...", "b": "...", "c": "...", "d": "..."},
    "answer": "c"
  },
  ...
]
```

## OUTPUT FORMAT

A JSON object you append to `discrimination_cards.json`:

```json
{
  "<pyq_id>": { ...card schema for this question_type... },
  "<pyq_id>": { ... },
  ...
}
```

## CALIBRATION

For the FIRST cluster in a session, draft cards then **stop**. Wait for QC
notes from Opus + the user before continuing. Calibration is the protocol.

## EXAMPLES (read these before drafting)

The 5 hand-drafted MVP cards in `discrimination_cards.json`:
- `607` — `standard` MCQ (Self-Respect Movement) → demonstrates per-distractor schema
- `81` — `matching` (Mahajanapada rivers) → demonstrates pairs schema
- `2285` — `assertion_reason` (Circular economy) → demonstrates 3-statement schema
- `822`, `823`, `824`, `825` — `statement_eval` (President/Governor) → demonstrates statement schema with varied trap patterns

Match their tone and density. If your draft is longer than the MVP for a
similar question type, cut.
