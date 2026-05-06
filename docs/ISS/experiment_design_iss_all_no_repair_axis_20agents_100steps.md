# ISS 全期間修復イベントなし軸 / 20人 / 100ステップ

## 目的

この追加軸は、「前半で修復作法を経験していない状態でも、摩擦後の会話に修復的な言葉が出るのか」を見るための対照条件です。

以前の「後半修復イベントなし」軸では、Step50以降の `repair` イベントだけを外していたため、Step50以前には修復経験が残っていました。「全期間修復イベントなし」軸では、Step1からStep100まで `repair` イベントを置かず、摩擦の後には `followup` だけを置きます。

## 条件

| 条件 | ベース | イベント | 目的 |
|---|---|---|---|
| A 全期間修復イベントなし | A | 基礎状態 + 摩擦 + 追跡観測 | ナッジなしで、修復経験なしでも再接触や謝罪が出るか |
| E 全期間修復イベントなし | E | 基礎状態 + 物 + 摩擦 + 追跡観測 | ナッジだけがある状態で、修復経験なしでも物を介した再接触が出るか |

`followup` は摩擦後の追跡観測であり、会話の成否は指定しません。E側でも「この物を使って修復してね」とは書かず、物がある場所で再接触が起きるかを観測するだけにしています。

## データ

- Aイベント定義: `domain_packs/iss_benevolence/data/events_run_a_all_no_repair_20x100.tsv`
- Eイベント定義: `domain_packs/iss_benevolence/data/events_run_e_all_no_repair_20x100.tsv`
- Aシナリオ: `domain_packs/iss_benevolence/scenarios/run_a_all_no_repair_20x100.yaml`
- Eシナリオ: `domain_packs/iss_benevolence/scenarios/run_e_all_no_repair_20x100.yaml`
- A生成結果: `outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm`
- E生成結果: `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm`
- 集計: `outputs/runs/iss20_all_no_repair_axis_llm_metrics.json`

## 実行コマンド

```bash
python3 -m sim_core validate \
  --pack domain_packs/iss_benevolence \
  --scenario run_a_all_no_repair_20x100

python3 scripts/build_state.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_a_all_no_repair_20x100 \
  --output-dir outputs/runs/iss20_no_nudge_all_no_repair_100_state

python3 scripts/export_habitat_frames.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_a_all_no_repair_20x100 \
  --run-id run_a_all_no_repair \
  --state-tsv outputs/runs/iss20_no_nudge_all_no_repair_100_state/societal_state.tsv \
  --output-dir outputs/runs/iss20_no_nudge_all_no_repair_100_ui

python3 scripts/generate_habitat_conversations.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_a_all_no_repair_20x100 \
  --input-dir outputs/runs/iss20_no_nudge_all_no_repair_100_ui \
  --output-dir outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm \
  --llm-config examples/spatial_demo/configs/config.iss.codex.fast.20x100.run_a_all_no_repair.yaml \
  --start-step 1 \
  --end-step 100 \
  --conversation-types followup
```

```bash
python3 -m sim_core validate \
  --pack domain_packs/iss_benevolence \
  --scenario run_e_all_no_repair_20x100

python3 scripts/build_state.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_e_all_no_repair_20x100 \
  --output-dir outputs/runs/iss20_nudge_only_all_no_repair_100_state

python3 scripts/export_habitat_frames.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_e_all_no_repair_20x100 \
  --run-id run_e_all_no_repair \
  --state-tsv outputs/runs/iss20_nudge_only_all_no_repair_100_state/societal_state.tsv \
  --output-dir outputs/runs/iss20_nudge_only_all_no_repair_100_ui

python3 scripts/generate_habitat_conversations.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_e_all_no_repair_20x100 \
  --input-dir outputs/runs/iss20_nudge_only_all_no_repair_100_ui \
  --output-dir outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm \
  --llm-config examples/spatial_demo/configs/config.iss.codex.fast.20x100.run_e_all_no_repair.yaml \
  --start-step 1 \
  --end-step 100 \
  --conversation-types followup
```

## 読み方

この軸で「修復が出た」と読む場合も、followup観測自体は置いている点に注意する。つまり、完全な自由生活から修復が創発したのではなく、摩擦後の同じペアを再観測したときに、LLMが謝罪、短い確認、距離の取り直し、回避、沈黙のどれを選ぶかを見ている。

「全期間喧嘩イベントなし」軸と合わせると、次のように分けられる。

- 全期間喧嘩イベントなし: 形式的な喧嘩は起きにくい
- 後半修復イベントなし: `repair` イベントがなくても `followup` 内に修復的な言葉は出る
- 全期間修復イベントなし: 前半の修復経験なしでも `followup` 内に修復的な言葉は出るかを観測する
