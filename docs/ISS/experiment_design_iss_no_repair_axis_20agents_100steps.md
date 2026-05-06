# ISS追加実験設計: Step50以降の修復イベントなし軸

## 20人 / 100ステップ / A・E 後半修復イベントなし

この追加軸は、新しいRun名を増やすのではなく、既存のA/Eに対して「Step50以降は修復イベントを置かない」条件を足す。

目的は、修復イベントを設計したから会話が戻ったのか、それともナッジオブジェクトや場所の存在が、修復を指示しない状況でも再接触の足場になるのかを切り分けること。

## 条件

| 軸 | ベース | Step50以降 |
|---|---|---|
| A 後半修復イベントなし | A: ナッジなし | 摩擦は残すが、Step50以降の修復イベントは置かない。追跡観測だけを置く |
| E 後半修復イベントなし | E: ナッジのみ | 同じナッジオブジェクトを残し、Step50以降の修復イベントは置かない。追跡観測だけを置く |

## LLMに渡す文脈

- 摩擦イベントは渡す。
- Step50以降の `repair` イベントは渡さない。
- `followup` は摩擦後の追跡観測であり、解決を前提にしない。
- E 後半修復イベントなしでは、オブジェクト名と短い効果ラベルは見える。
- 「この物を使って修復してください」とは書かない。

## 見るもの

- 謝罪や言い換えが自然に出るか
- 会話が短い作業確認に逃げるか
- 回避や沈黙が増えるか
- E 後半修復イベントなしで、持ち寄り棚、OKサイン、聖域マークなどが再接触の媒介として言及されるか
- A 後半修復イベントなしと比べて、未修復、開いたまま、未解決の残り方が変わるか

## 生成対象

- state: `outputs/runs/iss20_no_nudge_no_repair_100_state`
- UI base: `outputs/runs/iss20_no_nudge_no_repair_100_ui`
- LLM: `outputs/runs/iss20_no_nudge_no_repair_100_ui_llm`
- state: `outputs/runs/iss20_nudge_only_no_repair_100_state`
- UI base: `outputs/runs/iss20_nudge_only_no_repair_100_ui`
- LLM: `outputs/runs/iss20_nudge_only_no_repair_100_ui_llm`

## 実行コマンド

```bash
python3 scripts/build_state.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_a_no_repair_20x100 \
  --output-dir outputs/runs/iss20_no_nudge_no_repair_100_state

python3 scripts/export_habitat_frames.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_a_no_repair_20x100 \
  --run-id run_a_no_repair \
  --state-tsv outputs/runs/iss20_no_nudge_no_repair_100_state/societal_state.tsv \
  --output-dir outputs/runs/iss20_no_nudge_no_repair_100_ui

python3 scripts/generate_habitat_conversations.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_a_no_repair_20x100 \
  --input-dir outputs/runs/iss20_no_nudge_no_repair_100_ui \
  --output-dir outputs/runs/iss20_no_nudge_no_repair_100_ui_llm \
  --llm-config examples/spatial_demo/configs/config.iss.codex.fast.20x100.run_a_no_repair.yaml \
  --start-step 50 \
  --end-step 100 \
  --conversation-types followup

python3 scripts/build_state.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_e_no_repair_20x100 \
  --output-dir outputs/runs/iss20_nudge_only_no_repair_100_state

python3 scripts/export_habitat_frames.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_e_no_repair_20x100 \
  --run-id run_e_no_repair \
  --state-tsv outputs/runs/iss20_nudge_only_no_repair_100_state/societal_state.tsv \
  --output-dir outputs/runs/iss20_nudge_only_no_repair_100_ui

python3 scripts/generate_habitat_conversations.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_e_no_repair_20x100 \
  --input-dir outputs/runs/iss20_nudge_only_no_repair_100_ui \
  --output-dir outputs/runs/iss20_nudge_only_no_repair_100_ui_llm \
  --llm-config examples/spatial_demo/configs/config.iss.codex.fast.20x100.run_e_no_repair.yaml \
  --start-step 50 \
  --end-step 100 \
  --conversation-types followup
```
