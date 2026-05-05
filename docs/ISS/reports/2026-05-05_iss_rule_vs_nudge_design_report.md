# ISS Rule vs Nudge Additional Experiment Design Report

Date: 2026-05-05

## Summary

20人100stepの追加実験として、既存A/Bに加えてRun D/Run Eを設計した。
目的は「ナッジが効いた」のか、「短く終われる会話形式が効いた」のかを切り分けること。

## Added Runs

| Run | Scenario | Condition |
|---|---|---|
| D | `run_d_20x100` | ナッジなし・短時間会話ルールだけ |
| E | `run_e_20x100` | ナッジあり・明文化ルールなし |

Design doc:

- `docs/ISS/experiment_design_iss_rule_vs_nudge_20agents_100steps.md`

## Added Files

- `domain_packs/iss_benevolence/data/events_run_d_20x100.tsv`
- `domain_packs/iss_benevolence/data/events_run_e_20x100.tsv`
- `domain_packs/iss_benevolence/scenarios/run_d_20x100.yaml`
- `domain_packs/iss_benevolence/scenarios/run_e_20x100.yaml`
- `examples/spatial_demo/configs/config.iss.codex.fast.20x100.run_d.yaml`
- `examples/spatial_demo/configs/config.iss.codex.fast.20x100.run_e.yaml`

`domain_packs/iss_benevolence/domain.yaml` にD/Eのscenarioとruntime profileを登録済み。

## Model Setting For Later Report

- Inference backend: Codex CLI command backend
- GPT inference model: `gpt-5.3-codex-spark`
- Reasoning setting: `model_reasoning_effort=low`
- Sandbox setting: `read-only`
- Generation mode: prior-step conversation history enabled
- Planned history size: `4`

## Lightweight Output Check

LLMなしのUIベースデータは生成済み。

Run D:

- Output: `outputs/runs/iss20_rule_only_100_ui`
- Frames: 100
- Messages: 360
- Conversation threads: 180
- Timeline events: 34
- Nudge effects: 0
- Agents in positions: 20

Run E:

- Output: `outputs/runs/iss20_nudge_only_100_ui`
- Frames: 100
- Messages: 334
- Conversation threads: 167
- Timeline events: 36
- Nudge effects: 5
- Agents in positions: 20

Scripted proxy comparison:

- JSON: `outputs/runs/iss20_rule_vs_nudge_scripted_metrics.json`
- Note: This is not the final LLM comparison. It only confirms that the row shape and proxy metrics are readable.

## Validation

Passed:

- `python3 -m py_compile scripts/generate_habitat_conversations.py scripts/build_state.py scripts/export_habitat_frames.py`
- `python3 -m sim_core validate --pack domain_packs/iss_benevolence --scenario run_d_20x100`
- `python3 -m sim_core validate --pack domain_packs/iss_benevolence --scenario run_e_20x100`
- `python3 scripts/build_state.py --pack domain_packs/iss_benevolence --scenario run_d_20x100 --output-dir outputs/runs/iss20_rule_only_100_state`
- `python3 scripts/build_state.py --pack domain_packs/iss_benevolence --scenario run_e_20x100 --output-dir outputs/runs/iss20_nudge_only_100_state`
- `python3 scripts/export_habitat_frames.py` for D/E

## Notes

- Full LLM generation was executed after the design review fixes below.
- `scripts/generate_habitat_conversations.py` now treats `--history-size 0` as zero history instead of accidentally using all history.
- For strict A/B/D/E comparison, regenerate all runs with the same model setting, or keep the existing Run A mixed-model caveat in the report.

## Design Review Fixes Before Full Run

Sub-agent review found two pre-run risks:

- D/E event rows had result-leading labels: D sounded already bad (`手続き修復`, `本音保留`, `距離固定`) and E sounded already good (`場所修復`, `理解回復`, `謝意回復`).
- Rule-only rows could inherit nudge vocabulary from scripted drafts or the LLM prior.

Fixes applied:

- D/E conflict and repair event intensity/duration were aligned.
- D/E repair event names were neutralized to `...の修復`.
- D/E repair directions were normalized to `距離再調整↑ 継続観察↑`.
- Run D scripted drafts no longer contain `持ち寄り棚`, `OKサイン`, `聖域マーク`, `投票パネル`, or `ナッジ`.
- LLM prompt now forbids nudge/object vocabulary when `run_condition_hint` is `rule_only_no_nudge_objects` or `no_nudge_objects`.
- UI now includes D/E run selection and a rule timeline lane.

## Full LLM Results

Run D:

- Output: `outputs/runs/iss20_rule_only_100_ui_llm`
- Generated threads: 180 / 180
- Failed threads: 0
- Messages: 483
- LLM messages: 483
- Status counts: `repaired=175`, `open=3`, `unresolved=1`, `closed=1`
- Prohibited nudge/object terms in D output: no hits for `ナッジ`, `持ち寄り棚`, `OKサイン`, `聖域マーク`, `投票パネル`

Run E:

- Output: `outputs/runs/iss20_nudge_only_100_ui_llm`
- Generated threads: 180 / 180
- Failed threads: 0
- Messages: 512
- LLM messages: 512
- Status counts: `repaired=176`, `open=3`, `unresolved=1`

Comparison:

- KPI JSON: `outputs/runs/iss20_rule_vs_nudge_llm_metrics.json`
- E vs D message delta: `+29`
- Unique interaction pairs: no difference
- Repair-after-conflict rate: no difference in the proxy metric
- Bridge agent count: no difference
- Load fairness: E is slightly more concentrated (`-0.0186` delta)

Interpretation:

- This run did not produce a simple “nudge reduces everything” result.
- D and E both repaired most visible conflicts, suggesting the short-ending conversation form itself is a strong factor.
- E produced more messages and much more object language, suggesting the nudge may change the social medium and re-entry texture rather than simply reducing conversation volume.
- The interesting next read is qualitative: D tends to resolve through explicit short confirmation and quiet boundaries; E tends to resolve through shelf/sign/object-mediated re-entry.

## Full Validation

Passed after full generation:

- `python3 -m py_compile scripts/export_habitat_frames.py scripts/generate_habitat_conversations.py scripts/build_state.py scripts/build_pages_site.py`
- `python3 -m sim_core validate --pack domain_packs/iss_benevolence --scenario run_d_20x100`
- `python3 -m sim_core validate --pack domain_packs/iss_benevolence --scenario run_e_20x100`
- UI script syntax check for `public/visualization/iss_habitat_demo.html`
- `python3 scripts/build_pages_site.py`
