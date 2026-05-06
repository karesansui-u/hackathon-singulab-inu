# ISS 全期間喧嘩イベントなし軸 / 20人 / 100ステップ

## 目的

この追加軸は、「喧嘩や言い合いが、現行パイプラインで本当に自然に発生するのか」を切り分けるための対照条件です。

通常のA/B/E系の条件では、閉鎖環境で起こりそうな摩擦を `conflict` イベントとして置き、その後に `repair` や `followup` の観測機会を置きます。これは修復のされ方を見るには有効ですが、「喧嘩そのものがどこまでイベントに依存しているか」は別問題です。

「全期間喧嘩イベントなし」軸では、Step1からStep100まで `conflict` / `repair` / `followup` イベントを置かず、`routine` 会話だけをLLM生成します。

## 条件

| 条件 | ベース | イベント | 目的 |
|---|---|---|---|
| A 全期間喧嘩イベントなし | A | 基礎状態のみ | ナッジなしで、全期間喧嘩イベントを置かないと形式的な衝突が出るか |
| E 全期間喧嘩イベントなし | E | 基礎状態 + 物のみ | ナッジだけがある状態で、全期間喧嘩イベントなしでも摩擦や距離調整が変わるか |

## データ

- Aイベント定義: `domain_packs/iss_benevolence/data/events_run_a_no_conflict_20x100.tsv`
- Eイベント定義: `domain_packs/iss_benevolence/data/events_run_e_no_conflict_20x100.tsv`
- Aシナリオ: `domain_packs/iss_benevolence/scenarios/run_a_no_conflict_20x100.yaml`
- Eシナリオ: `domain_packs/iss_benevolence/scenarios/run_e_no_conflict_20x100.yaml`
- A状態出力: `outputs/runs/iss20_no_nudge_no_conflict_100_state`
- A UI出力: `outputs/runs/iss20_no_nudge_no_conflict_100_ui`
- A生成結果: `outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm`
- E状態出力: `outputs/runs/iss20_nudge_only_no_conflict_100_state`
- E UI出力: `outputs/runs/iss20_nudge_only_no_conflict_100_ui`
- E生成結果: `outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm`

## 実行コマンド

```bash
python3 -m sim_core validate \
  --pack domain_packs/iss_benevolence \
  --scenario run_a_no_conflict_20x100

python3 scripts/build_state.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_a_no_conflict_20x100 \
  --output-dir outputs/runs/iss20_no_nudge_no_conflict_100_state

python3 scripts/export_habitat_frames.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_a_no_conflict_20x100 \
  --run-id run_a_no_conflict \
  --state-tsv outputs/runs/iss20_no_nudge_no_conflict_100_state/societal_state.tsv \
  --output-dir outputs/runs/iss20_no_nudge_no_conflict_100_ui

python3 scripts/generate_habitat_conversations.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_a_no_conflict_20x100 \
  --input-dir outputs/runs/iss20_no_nudge_no_conflict_100_ui \
  --output-dir outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm \
  --llm-config examples/spatial_demo/configs/config.iss.codex.fast.20x100.run_a_no_conflict.yaml \
  --start-step 50 \
  --end-step 100 \
  --conversation-types routine
```

```bash
python3 -m sim_core validate \
  --pack domain_packs/iss_benevolence \
  --scenario run_e_no_conflict_20x100

python3 scripts/build_state.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_e_no_conflict_20x100 \
  --output-dir outputs/runs/iss20_nudge_only_no_conflict_100_state

python3 scripts/export_habitat_frames.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_e_no_conflict_20x100 \
  --run-id run_e_no_conflict \
  --state-tsv outputs/runs/iss20_nudge_only_no_conflict_100_state/societal_state.tsv \
  --output-dir outputs/runs/iss20_nudge_only_no_conflict_100_ui

python3 scripts/generate_habitat_conversations.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_e_no_conflict_20x100 \
  --input-dir outputs/runs/iss20_nudge_only_no_conflict_100_ui \
  --output-dir outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm \
  --llm-config examples/spatial_demo/configs/config.iss.codex.fast.20x100.run_e_no_conflict.yaml \
  --start-step 50 \
  --end-step 100 \
  --conversation-types routine
```

## 読み方

この軸では、形式的な `conflict` スレッドが出るかどうかを第一に見る。もし `conversation_threads.tsv` がすべて `routine` のままなら、現行パイプラインにおける「喧嘩の発生」はイベント設計に強く依存していると読む。

一方で、routineの内部に「刺さる」「きつい」「急かす」「重い」「無理」などの摩擦語彙が出ることはありうる。これは形式的な喧嘩ではなく、閉鎖環境・人物関係・生活負荷に由来する小さな不穏さとして扱う。

つまり、この軸で見たいのは次の二段階です。

- 喧嘩そのもの: イベントなしで形式的な衝突として出るか
- 喧嘩未満の摩擦: routine会話の中に、距離調整や不満の言葉として出るか
