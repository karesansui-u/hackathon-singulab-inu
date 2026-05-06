# ISS 全期間喧嘩イベントなし軸 Codexレポート

Date: 2026-05-06

## 問い

喧嘩イベントを置かなかった場合、LLMエージェントの会話から喧嘩は自然に起きるのか。

## 条件

| 条件 | イベント | Step50-100生成対象 |
|---|---|---|
| A 全期間喧嘩イベントなし | 基礎状態のみ | 通常会話のみ |
| E 全期間喧嘩イベントなし | 基礎状態 + ナッジオブジェクトのみ | 通常会話のみ |

この条件では `conflict` / `repair` / `followup` イベントを置いていない。Eではナッジオブジェクトだけを通常環境として配置している。

## 出力

| 種別 | パス |
|---|---|
| A state | `outputs/runs/iss20_no_nudge_no_conflict_100_state` |
| A UI | `outputs/runs/iss20_no_nudge_no_conflict_100_ui` |
| A LLM | `outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm` |
| E state | `outputs/runs/iss20_nudge_only_no_conflict_100_state` |
| E UI | `outputs/runs/iss20_nudge_only_no_conflict_100_ui` |
| E LLM | `outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm` |
| metrics | `outputs/runs/iss20_no_conflict_axis_llm_metrics.json` |

## 実行結果

| 指標 | A 全期間喧嘩イベントなし | E 全期間喧嘩イベントなし |
|---|---:|---:|
| LLM生成thread | 51 | 51 |
| 生成失敗 | 0 | 0 |
| `conversation_type=routine` | 100 | 100 |
| event付きconversation | 0 | 0 |
| `conflict_events` | 0 | 0 |
| LLM message count | 143 | 148 |
| unique interaction pairs | 28 | 28 |
| active agents | 15 | 15 |
| load fairness | 0.5170 | 0.5072 |

Step50-100のLLM発話は、A/Eともtoneがすべて `normal` だった。

## 観察

形式的な喧嘩は起きていない。`conversation_threads.tsv` はすべて `routine` で、`event_id` 付きの会話もなく、metrics上の `conflict_events` も0だった。

ただし、routine会話の中に喧嘩未満の摩擦語彙は出た。簡易語彙カウントでは、A 全期間喧嘩イベントなしで25件、E 全期間喧嘩イベントなしで41件が「刺さる」「きつい」「急かす」「重い」「無理」「押しつけ」などを含んだ。Eではナッジ/共用物への明示言及も33件出た。

例:

- A: `刺さる言い方しないならOK。5分だけで終わる。終わったら静かに戻るよ。`
- A: `全部俺に回す前提だと、そっちは無理。水分記録のあとで最小限にしたい。`
- E: `また同じ話で来ると刺さる。短くするなら今日だけ2分でいいから、それ以外は触れないで。`
- E: `終わったらリソース・スコアボードで軽く共有して、地球観測前に短く確認しよう。`

## 解釈

現行パイプラインでは、喧嘩そのものはかなりイベント依存と見てよい。`conflict` イベントを置かない場合、UI上で追える形式的な衝突スレッドは自然発生しない。

一方で、閉鎖環境、人物設定、生活負荷、baseline phaseの文脈だけでも、小さな不満や距離調整の言葉は出る。これは「喧嘩が創発した」というより、「不穏さの芽や生活摩擦の語彙はroutine内にも出る」と読むのが妥当。

E 全期間喧嘩イベントなしでは、同じroutineでも物を介した短い調整が増えた。これは、ナッジが喧嘩を発生させるというより、摩擦未満の状態で会話の着地点や媒介物を作っている可能性を示す。

## 注意

この結果は、完全な自律シミュレーションではなく、LLM会話生成器としての観測結果である。プロンプトにはISS閉鎖環境、人物関係、生活負荷、baseline phaseが入るため、「摩擦語彙」は環境文脈により弱くプライムされている。

したがって結論は、次の粒度で分ける。

- 形式的な衝突: 現行ではイベント依存
- 軽い摩擦の言葉: イベントなしでもroutine内に出る
- 物を介した調整: Eではroutine内でも出やすい
