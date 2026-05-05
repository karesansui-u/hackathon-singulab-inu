# ISS追加実験設計: ルールだけか、ナッジか
## 20 agents / 100 steps / Run D・Run E

Date: 2026-05-05

## 目的

既存の20人100step実験では、Run Bで会話件数・摩擦件数・未修復が減り、「短く終われる会話」が増えた。
次の追加実験では、効果の本体が「善性オブジェクト」なのか、「短時間で終われる会話形式」なのかを切り分ける。

中心仮説:

- ナッジが効いたのではなく、短く終われる会話形式が効いた可能性がある。
- ただし、同じ会話形式でも、ルールだけで導入すると「従わされている」「切られた」「本音を飲み込む」という副作用が出る可能性がある。
- ナッジオブジェクトがある場合、短く終わることが拒絶ではなく、場所・物・合図に支えられた文化として残る可能性がある。

## 実験条件

| Run | 条件 | 目的 | 既存/追加 |
|---|---|---|---|
| Run A | ナッジなし・短時間会話ルールなし | 通常の閉鎖環境ベースライン | 既存 |
| Run B | ナッジあり・短い修復会話が起きやすい | ナッジと会話形式が揃った状態 | 既存 |
| Run D | ナッジなし・短時間会話ルールだけ | ルールだけで会話が短くなるか、副作用が出るか | 追加 |
| Run E | ナッジあり・明文化ルールなし | オブジェクトだけで短い会話形式が創発するか | 追加 |

## Run D: Rule Only

シナリオID: `run_d_20x100`

条件:

- 善性オブジェクトは置かない。
- Step 6以降に「短く確認して、長引くなら後で再開する」という明文化ルールを導入する。
- Step 18以降に静穏時間ルール、Step 33以降に確認テンプレートを追加する。

期待される観察:

- 目に見える言い合いは短くなる。
- ただし、未修復・open・unresolved・撤退系の会話が増える可能性がある。
- 弱い立場の参加者ほど「従う」「仕方ない」「時間切れ」「例外を言いにくい」といった語彙を出す可能性がある。
- Dmitri/Henri/Ingridなど、規律や説明力の強い参加者にルール運用の負荷が集中する可能性がある。

失敗パターン:

- compliance theater: 表面上は従うが、納得や修復が起きていない。
- rule weaponization: ルールを使って相手の話を切る。
- hidden withdrawal: 争いは減るが、避ける・黙る・話さないが増える。
- exception stigma: 礼拝、障害、ホームシック、識字差などの例外が言い出しにくくなる。

## Run E: Nudge Only

シナリオID: `run_e_20x100`

条件:

- Run Bと同じ善性オブジェクトを置く。
- 「2分ルール」「確認テンプレート」などの明文化ルールは入れない。
- 会話の短さは、持ち寄り棚、OKサイン、個室聖域マーク、リソース・スコアボード、移動投票パネルの使い方から創発するかを見る。

期待される観察:

- 会話が自然に短く区切られ、あとで戻る余地が残る。
- 修復が「誰かの説得」ではなく「棚の前で一言」「サインを見て一言」「個室の順番を短く確認」のような場所行為になる。
- 明文化ルールがないため、初期の摩擦はRun Bより少し長く残る可能性がある。
- ただし、修復語彙が命令ではなく「選べる」「あとで」「置いておく」「合図」「戻る」になりやすい。

失敗パターン:

- オブジェクトが一部の人だけに使われ、文化にならない。
- 文字・サイン中心のナッジがTariqなどに届きにくい。
- 使う人と使わない人の差が固定化する。

## 比較指標

一次指標:

- `conversation_threads.tsv` の件数
- conflict thread count
- repair thread count
- repair latency
- `status=open/unresolved` の件数
- recurrent conflict pair rate
- bridge agent count
- helper burden concentration

言語指標:

- ルール副作用語彙: `規則`, `従う`, `守る`, `時間切れ`, `仕方ない`, `違反`, `注意された`, `黙る`, `飲み込む`, `例外`, `不公平`
- ナッジ文化語彙: `サイン`, `棚`, `あとで`, `戻る`, `選べる`, `置いておく`, `合図`, `個室`, `短く確認`, `地球観測前`
- 修復の質: 謝罪だけでなく、次の接触方法・距離・再開タイミングが言語化されているか
- 沈黙の質: 落ち着くための沈黙か、関係断絶としての沈黙か

UI観察:

- ギザギザ線の発生回数と継続step
- 緑の修復線への移行step
- 個室・キューポラ・共用部に会話が偏りすぎていないか
- ナッジあり条件で、related_object_id付きrepairが発生するか

## 実行設定

推奨:

- agents: 20
- steps: 100
- model: `gpt-5.3-codex-spark`
- reasoning effort: `low`
- history size: 4

モデル名をレポートに書く場合:

- Inference backend: Codex CLI command backend
- GPT inference model: `gpt-5.3-codex-spark`
- Reasoning setting: `model_reasoning_effort=low`
- Sandbox setting: `read-only`
- Generation mode: prior-step conversation history enabled (`history_size=4`)

注意:

- 既存Run A 20x100は後半23スレッドだけ `gpt-5.4-mini` fallback を使っている。
- D/Eと厳密比較する場合は、A/B/D/Eを同じモデル設定で再生成するか、Run Aの混在 caveat を明記する。

## 想定出力

Run D:

- state: `outputs/runs/iss20_rule_only_100_state`
- UI base: `outputs/runs/iss20_rule_only_100_ui`
- LLM: `outputs/runs/iss20_rule_only_100_ui_llm`

Run E:

- state: `outputs/runs/iss20_nudge_only_100_state`
- UI base: `outputs/runs/iss20_nudge_only_100_ui`
- LLM: `outputs/runs/iss20_nudge_only_100_ui_llm`

## 実行手順

LLMなしのUIベースデータ:

```bash
python3 scripts/build_state.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_d_20x100 \
  --output-dir outputs/runs/iss20_rule_only_100_state

python3 scripts/export_habitat_frames.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_d_20x100 \
  --run-id run_d_20x100_rule_only \
  --state-tsv outputs/runs/iss20_rule_only_100_state/societal_state.tsv \
  --output-dir outputs/runs/iss20_rule_only_100_ui

python3 scripts/build_state.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_e_20x100 \
  --output-dir outputs/runs/iss20_nudge_only_100_state

python3 scripts/export_habitat_frames.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_e_20x100 \
  --run-id run_e_20x100_nudge_only \
  --state-tsv outputs/runs/iss20_nudge_only_100_state/societal_state.tsv \
  --output-dir outputs/runs/iss20_nudge_only_100_ui
```

LLM会話生成:

```bash
python3 scripts/generate_habitat_conversations.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_d_20x100 \
  --input-dir outputs/runs/iss20_rule_only_100_ui \
  --output-dir outputs/runs/iss20_rule_only_100_ui_llm \
  --llm-config examples/spatial_demo/configs/config.iss.codex.fast.20x100.run_d.yaml \
  --start-step 1 \
  --end-step 100 \
  --history-size 4

python3 scripts/generate_habitat_conversations.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_e_20x100 \
  --input-dir outputs/runs/iss20_nudge_only_100_ui \
  --output-dir outputs/runs/iss20_nudge_only_100_ui_llm \
  --llm-config examples/spatial_demo/configs/config.iss.codex.fast.20x100.run_e.yaml \
  --start-step 1 \
  --end-step 100 \
  --history-size 4
```

比較:

```bash
python3 examples/spatial_demo/analyze_iss_pair.py \
  --run-a outputs/runs/iss20_rule_only_100_ui_llm \
  --run-b outputs/runs/iss20_nudge_only_100_ui_llm \
  --out outputs/runs/iss20_rule_vs_nudge_llm_metrics.json
```

## 判定の読み方

最も面白い分岐は次の4つ。

| 観察 | 解釈 |
|---|---|
| DもBと同じくらい良い | 短時間会話形式そのものが主要因 |
| Dは静かだが未修復が多い | ルールは摩擦を隠すが、修復文化を作らない |
| EがBに近い | ナッジだけでも会話形式が創発する |
| Bだけが良い | 物理ナッジと短い会話形式の組み合わせが効く |

この実験の焦点は「ナッジが万能か」ではなく、会話の終わり方・戻り方がどのように文化化されるかである。
