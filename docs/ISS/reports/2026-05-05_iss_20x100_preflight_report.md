# ISS 20 Agents / 100 Steps Execution Report

Date: 2026-05-05

## Summary

20体100stepのISS実験を、既存の10体50stepとは別シナリオとして追加した。
LLMなしのrowデータ生成、GPT/Codex会話生成、KPI比較、UI/Pages用ビルドまで実行した。

## Canonical Inputs

- `docs/ISS/experiment_design_iss_20agents_100steps.md`
- `docs/ISS/experiment_design_iss_b_main_10agents_50steps.md`
- `docs/ISS/iss_objects_menu.md`
- `docs/ISS/personas_iss_10agents.md`
- `docs/ISS/places_iss_design.md`

## Added Domain-Pack Data

- `domain_packs/iss_benevolence/data/agents_20.tsv`: 20 agents
- `domain_packs/iss_benevolence/data/personas_20.tsv`: 20 personas
- `domain_packs/iss_benevolence/data/relationship_seed_20.tsv`: 20 relationship rows
- `domain_packs/iss_benevolence/data/places_iss_20.tsv`: 6 canonical simulation places
- `domain_packs/iss_benevolence/data/time_schedule_100.tsv`: 100 steps
- `domain_packs/iss_benevolence/data/events_run_a_20x100.tsv`: 31 events
- `domain_packs/iss_benevolence/data/events_run_b_20x100.tsv`: 36 events

Existing `ISS00`-`ISS09` IDs were preserved. New participants are appended as `ISS10`-`ISS19`.

## Added Scenarios

- `run_a_20x100`: no benevolence objects
- `run_b_20x100`: benevolence objects enabled

The domain pack validates successfully for both scenarios.

## GPT/Codex Model

Fast probe config:

- Run A config: `examples/spatial_demo/configs/config.iss.codex.fast.20x100.run_a.yaml`
- Run B config: `examples/spatial_demo/configs/config.iss.codex.fast.20x100.run_b.yaml`
- Model name: `gpt-5.3-codex-spark`
- Reasoning effort: `low`
- Backend wrapper: `scripts/run_codex_prompt.sh`

Recommended report wording:

- Inference backend: Codex CLI command backend
- GPT inference model: `gpt-5.3-codex-spark`
- Reasoning setting: `model_reasoning_effort=low`
- Sandbox setting: `read-only`
- Codex user config: ignored for simulation generation (`CODEX_IGNORE_USER_CONFIG=true`)
- Generation mode: prior-step conversation history enabled

Use this wording when the experiment report needs the model name.

`scripts/run_codex_prompt.sh` now reads:

- `CODEX_MODEL`
- `CODEX_REASONING_EFFORT`
- `CODEX_SANDBOX`
- `CODEX_IGNORE_USER_CONFIG`

## Generated Preflight Outputs

Local UI:

- URL: `http://127.0.0.1:8766/visualization/iss_habitat_demo.html`
- The local UI now checks the 20x100 run directories first.
- HTTP checks passed for the HTML and the 20x100 `habitat_frames.jsonl` / `messages.jsonl` data.

Run A:

- Directory: `outputs/runs/iss20_no_nudge_100_ui`
- Frames: 100
- Messages: 386
- Conversation threads: 193
- Timeline events: 31
- Nudge effects: 0
- Agent positions: 2,000 rows
- All 20 agents appear in positions, speakers, and listeners

Run B:

- Directory: `outputs/runs/iss20_nudge_100_ui`
- Frames: 100
- Messages: 314
- Conversation threads: 157
- Timeline events: 36
- Nudge effects: 5
- Agent positions: 2,000 rows
- All 20 agents appear in positions, speakers, and listeners

GPT probe:

- Directory: `outputs/runs/iss20_nudge_100_ui_gpt_probe`
- Generated threads: 1
- Failed threads: 0
- Output rows are stored in `messages.jsonl` and `conversation_threads.tsv`
- Generated rows are marked with `source: "llm"` / `summary_source: "llm_summary"`

Full GPT/Codex generation:

- Model: `gpt-5.3-codex-spark`
- Reasoning effort: `low`
- Run A directory: `outputs/runs/iss20_no_nudge_100_ui_llm`
- Run A result: 193 threads, 170 LLM-generated threads, 23 scripted fallback threads
- Run A messages: 485 total, 439 `source=llm`, 46 `source=scripted`
- Run A caveat: Codex CLI repeatedly returned empty/failed output during late steps 88-100; fallback rows were retained for those affected threads.
- Run B directory: `outputs/runs/iss20_nudge_100_ui_llm`
- Run B result: 157 threads, 157 LLM-generated threads, 0 failed threads
- Run B messages: 389 total, 389 `source=llm`

KPI comparison:

- JSON: `outputs/runs/iss20_ab_100step_metrics.json`
- Data source: `messages.jsonl`
- Note: this is still proxy KPI because the full A/B rows are scripted UI-derived messages, not full GPT-generated conversation rows.
- Run A total messages: 386
- Run B total messages: 314
- Unique interaction pairs: A 54 / B 60
- Repair-after-conflict rate: A 0.8043 / B 0.9730
- Bridge agent count: A 6 / B 9
- Isolated agents: A 0 / B 0

LLM/mixed KPI comparison:

- JSON: `outputs/runs/iss20_llm_ab_100step_metrics.json`
- Data source: `messages.jsonl`
- Note: Run A contains 23 scripted fallback threads, so this is a mixed LLM/proxy comparison. Run B is fully LLM-generated.
- Run A total messages: 485
- Run B total messages: 389
- Unique interaction pairs: A 54 / B 60
- Repair-after-conflict rate: A 0.9068 / B 1.0000
- Bridge agent count: A 6 / B 9
- Isolated agents: A 0 / B 0

## Validation

Passed:

- `python3 -m py_compile scripts/prepare_iss_20x100.py scripts/build_state.py scripts/export_habitat_frames.py scripts/generate_habitat_conversations.py`
- `bash -n scripts/run_codex_prompt.sh`
- `python3 -m sim_core validate --pack domain_packs/iss_benevolence --scenario run_a_20x100`
- `python3 -m sim_core validate --pack domain_packs/iss_benevolence --scenario run_b_20x100`
- LLM-free state and UI export for Run A/B
- GPT/Codex one-thread probe for Run B
- GPT/Codex full Run B generation
- GPT/Codex Run A generation with documented fallback for 23 late-step threads

## Notes

- Current UI `visualization/iss_habitat_demo.html` now includes all 20 agent dots.
- `scripts/build_pages_site.py` is updated so the Pages build copies the 20x100 LLM/mixed run data first, with scripted data as fallback.
- The 20x100 output is suitable for local inspection, Pages publication, and data handoff, with the Run A fallback caveat stated above.
