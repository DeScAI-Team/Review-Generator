# Articles Pipeline

This folder contains the full claim extraction and evidence review pipeline for empirical research papers. All scripts live under `pipeline/` and are driven end-to-end by `run_pipe2.py` at the repo root.

## Pipeline overview (13 steps)

| Step | Script | Input | Output |
|------|--------|-------|--------|
| 1 | `pipeline/claim-extract/spacy_test.py` | `text_knowledge_base.jsonl` | `test_output_tagged.jsonl` |
| 2 | `pipeline/claim-extract/LLM_extract.py` | `test_output_tagged.jsonl` | `final_claims_for_audit.jsonl` |
| 3 | `pipeline/claim-extract/claim_validator.py` | `final_claims_for_audit.jsonl` | `validated_claims.jsonl` |
| 4 | `pipeline/classify_claims.py` | `validated_claims.jsonl` | `classified_claims.jsonl` |
| 5 | `pipeline/group.py` | `classified_claims.jsonl` | `grouped.json` |
| 6 | `pipeline/empirical/triage.py` | `grouped.json` | `triaged.json` |
| 7 | `pipeline/empirical/retrieve_compare.py` | `triaged.json` + KB + `full.md` | `retrieve_compare_llm.json` |
| 8 | `pipeline/empirical/prep.py` | `retrieve_compare_llm.json` | `prepped_evidence.json` |
| 9 | `pipeline/empirical/review.py` | `prepped_evidence.json` | `review.json` |
| 10 | `pipeline/empirical/originality_check.py` | KB + `full.md` | `originality.json` (patches `review.json`) |
| 11 | `pipeline/empirical/screener.py` | `full.md` + caches | `screener.json` (patches `review.json`) |
| 12 | `pipeline/empirical/score.py` | `review.json` + all intermediates | `review.json` (final scores + composite) |
| 13 | `pipeline/empirical/evidence-doc.py` | `review.json` + intermediates | `evidence_audit.md` |

Steps 1–5 extract, validate, classify, and group claims. Steps 6–13 (the **empirical evidence pipeline**) grade those claims against cited references, assess originality, screen the full document, compute unified scores, and produce an audit trail. See [`pipeline/empirical/PIPELINE.md`](pipeline/empirical/PIPELINE.md) for detailed documentation of steps 6–13.

## Prerequisites

- Python 3.10+
- `openai`, `python-dotenv` (LLM steps)
- `docling`, `spacy`, `transformers` (PDF chunking and tagging — step 0 / `add_data.py`)
- A reachable vLLM (or OpenAI-compatible) server; see the root [README.md](../README.md) for base URL and model configuration.

## Running

From the **repository root**:

```bash
python run_pipe2.py                  # full run (steps 1-13)
python run_pipe2.py --from-step 4    # resume from classify
python run_pipe2.py --from-step 6    # triage onward (empirical pipeline)
python run_pipe2.py --from-step 12   # unified scoring + evidence audit
python run_pipe2.py --skip-llm       # skip LLM evidence grading
```

`run_pipe2.py` expects a pre-existing `text_knowledge_base.jsonl` (produced by `pipeline/claim-extract/add_data.py` or copied manually). Use `--model` to override the vLLM model name.

## Directory layout

```
articles/
├── pipeline/
│   ├── claim-extract/        Steps 1-3: spaCy tagging, LLM extraction, validation
│   │   ├── add_data.py       PDF → text_knowledge_base.jsonl (step 0)
│   │   ├── spacy_test.py
│   │   ├── LLM_extract.py
│   │   └── claim_validator.py
│   ├── classify_claims.py    Step 4: semantic claim-type tags
│   ├── group.py              Step 5: group by scoring dimension
│   ├── prep.py               Legacy prep (claim narratives only)
│   ├── review.py             Legacy review (claim-only rationales)
│   ├── read-paper.py         Standalone PDF reader
│   ├── classify-paper.py     Standalone paper classifier
│   ├── journal-article.py    Journal-article helper
│   ├── mappings.json         Dimension definitions, tag index, weights, rubrics
│   └── empirical/            Steps 6-13: evidence grading pipeline
│       ├── PIPELINE.md       Detailed docs for empirical stages
│       ├── triage.py
│       ├── retrieve_compare.py
│       ├── prep.py
│       ├── review.py
│       ├── originality_check.py
│       ├── screener.py
│       ├── score.py
│       ├── evidence-doc.py
│       ├── empirical-pipe.py  Standalone empirical driver (steps/ + output/ layout)
│       └── prompts/           LLM prompt templates for each empirical stage
├── prompts/                   Shared prompts (classification, verdict fallbacks, etc.)
└── data/                      Per-paper run folders (gitignored)
```

## Configuration

All LLM steps share the same environment variables. Set via `.env` in the repo root.

| Variable | Default | Description |
|----------|---------|-------------|
| `VLLM_BASE_URL` | `http://localhost:8000/v1` | vLLM OpenAI API base URL |
| `VLLM_API_KEY` | `none` | API key if required by the server |
| `VALIDATOR_MODEL` | `mixtral-8x7b-instruct` | Model id used across all LLM steps |
| `CLASSIFIER_MODEL` | (same as `VALIDATOR_MODEL`) | Optional override for step 4 |
| `VALIDATOR_CONCURRENCY` | `15` | Max concurrent validation requests (step 3) |

## Key outputs

| File | Description |
|------|-------------|
| `review.json` | Final structured review: per-dimension scores, `composite_score`, rationales, review statement |
| `overview.json` | Plain-language companion (when LLM overview is enabled in `score.py`) |
| `evidence_audit.md` | Human-readable audit trail: provenance, scores, claim/citation trace, screener quotes, originality |

## Related documentation

- Root pipeline overview and vLLM config: [README.md](../README.md)
- Empirical evidence pipeline details: [pipeline/empirical/PIPELINE.md](pipeline/empirical/PIPELINE.md)
- Cluster / full-run notes: [RUN_FULL_PIPELINE.md](../RUN_FULL_PIPELINE.md)
