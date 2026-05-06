# ISSナッジ実験 統合考察

Date: 2026-05-06

この文書は、ISS閉鎖環境シミュレーションで増えた複数の条件を、1本の読み筋にまとめるための統合メモです。

## 先に結論

この文書で比較しているのは、1つの条件表ではなく、**3つの確認セット**です。

1. 喧嘩を置かないと、そもそも喧嘩は出るのか。
2. 喧嘩だけ置いて、修復を指示しないとどうなるのか。
3. 喧嘩も修復イベントも置くと、ナッジあり/なしでどう変わるのか。

この3つは混ぜて比較しません。それぞれのセットの中で、ナッジなしとナッジありを比べます。

今回見えたことは、次の3つです。

1. **何もしなければ、形式的な喧嘩は起きなかった。**
   全期間喧嘩イベントなし条件では、A/Eとも形式ラベル上の `conflict` スレッドは0でした。ただし通常会話内には摩擦・修復的な語りが出ているため、ここでいう「喧嘩が自然発生しない」は形式的な `conflict` イベント/スレッドに限定した結論です。現行パイプラインで観測対象としての喧嘩を見るには、摩擦イベントを入れる必要がある。

2. **修復イベントを入れなくても、修復っぽい言葉は出た。**
   全期間修復イベントなし条件でも、摩擦後の追跡観測では、Aが48件中29件、Eが54件中33件で修復的な会話になりました。つまり「repairイベントを置いたからだけで修復した」とは言い切れない。

3. **ナッジが大きく変えたのは、修復するかどうかより、修復に向かう経路だった。**
   ナッジなしでは、人同士が直接「ごめん」「短く確認しよう」「今は距離を置こう」と調整する。ナッジありでは、持ち寄り棚、OKサイン、リソース・スコアボードなど、物を挟んだ短い再接触が増えた。

一言でまとめると、**ナッジは人を急に善人にする装置ではなく、摩擦後に直接ぶつかり続けずに戻るための足場を増やした**。

## 3つの確認セット

この考察は、次の3セットに分けて読む。

| セット | 入れるイベント | 比較 | 目的 |
|---|---|---|---|
| 1. 自然発生の確認 | 喧嘩なし、修復なし、追跡観測なし | A: ナッジなし / E: ナッジあり | 何もしなくても喧嘩が起きるか |
| 2. 修復イベントなし | 喧嘩あり、修復なし、追跡観測あり | A: ナッジなし / E: ナッジあり | 修復イベントがなくても、摩擦後に戻るか |
| 3. 修復イベントあり | 喧嘩あり、修復あり | A/B: 完成パッケージ、D/E: ルールと物の差、A/E: 補助 | 修復イベントがある状態で、ナッジが何を変えるか |

ここでいう「修復イベントなし」は、`repair` イベントや「必ず仲直りしろ」という直接指示がないという意味です。ただし摩擦後の同じペアを再観測する `followup` 枠は置いているため、完全な自然発生条件ではありません。

ここでいう「修復イベントあり」は、LLMに直接「必ず仲直りしろ」と命令するという意味ではありません。`repair` イベントを置いて、摩擦後に修復場面として観測する、という意味です。

BとEはどちらもナッジありですが、読み方が少し違います。

- **B** は完成した標準介入です。ナッジオブジェクトがあり、修復の入口としての意味づけも比較的強い。
- **E** はナッジのみ寄りの条件です。ルール説明を弱め、物そのものが会話に入るかを見やすくした条件です。

そのため、**完成パッケージの有効性を見るならA/B**、**ルールと物の違いを見るならD/E**、**ナッジなしに対するEの補助確認ならA/E** と分けて読む。

## 結果1: 何もしないと喧嘩は起きたか

これは、主実験の結果というより、前提確認です。全期間喧嘩イベントなし条件では、A/Eとも形式的な `conflict` イベント/スレッドとしての喧嘩は起きませんでした。

| 条件 | 会話タイプ | イベント付き会話 | 摩擦イベント数 | 読み |
|---|---:|---:|---:|---|
| A 全期間喧嘩イベントなし | routine 100 | 0 | 0 | 形式ラベル上は喧嘩なし |
| E 全期間喧嘩イベントなし | routine 100 | 0 | 0 | 形式ラベル上は喧嘩なし |

ただし、通常会話の中に「刺さる」「きつい」「無理」など、喧嘩未満の摩擦語彙は出ました。次の語彙数は個別レポートで使った簡易語彙カウントであり、metrics JSONの標準項目ではありません。

| 条件 | 摩擦っぽい語彙 | 物への言及 |
|---|---:|---:|
| A 全期間喧嘩イベントなし | 25 | 0 |
| E 全期間喧嘩イベントなし | 41 | 33 |

ここから言えるのは、**形式的な `conflict` イベント/スレッドは自然発生しないが、小さな不穏さや距離調整の言葉は出る**ということです。

この結果は、実験全体の補足情報として使えます。

> 何もしないと形式的な喧嘩は起きなかった。そこで、閉鎖環境ストレス下の修復過程を観測するため、摩擦イベントを意図的に挿入した。

## 結果2: 喧嘩だけ起こし、修復イベントを入れないとどうなるか

ここが、ナッジの素の効き方を見るための重要な比較です。全期間修復イベントなし条件では、摩擦イベントは入れますが、修復イベントはStep1から最後まで入れません。摩擦後に同じペアを追跡観測します。

このセットで比べるのは、AとEです。

- A: ナッジなし
- E: ナッジあり

| 条件 | 追跡観測スレッド | 修復的 | 開いたまま | 未解決 | 物への言及 |
|---|---:|---:|---:|---:|---:|
| A 全期間修復イベントなし | 48 | 29 | 12 | 7 | 0 |
| E 全期間修復イベントなし | 54 | 33 | 13 | 8 | 57 |

修復的になった割合は、Aが約60%、Eが約61%です。率だけ見ると大きな差はありません。

ただし、Eの追跡観測におけるLLM発話全体では、「持ち寄り棚」「OKサイン」「リソース・スコアボード」「投票パネル」などの物語彙を含む発話が57件ありました。そのうち、修復的statusのスレッド内では35件でした。つまり、ナッジあり条件では、修復の成否率よりも、摩擦後の会話に物が入り込む度合いが大きく変わりました。

この結果の読みは、次です。

- 修復イベントがなくても、LLMは摩擦後の追跡観測で謝罪、短い確認、距離調整を出す。
- ナッジは、修復率そのものを大きく上げたわけではない。
- ただし、ナッジは修復の入口や媒介物を変えた。

ここが一番重要です。**ナッジの効果は「修復した/しない」だけでは見えにくく、「何を介して戻ったか」で見る必要がある**。

## 結果3: 喧嘩も修復イベントも入れた場合

これは、完成した介入パッケージを見やすい比較です。修復イベントあり条件では、修復方向にかなり誘導されます。ここでは、Aとナッジあり条件を比較します。

このセットでは、主にA/Bを見ます。Eは「ナッジのみ寄り」の補助比較です。D/Eは、同じ修復イベント構成の中で「短時間ルール」と「物理ナッジ」の違いを見る補助比較として扱います。

- A: ナッジなし
- B: 標準ナッジあり
- D: ルールのみ
- E: ナッジのみ寄り

| 条件 | 修復率 | 摩擦系カウント | 会話ペア数 | 橋渡し役の人数 | 総発話数 |
|---|---:|---:|---:|---:|---:|
| A 標準条件 | 90.7% | 118 | 54 | 6 | 485 |
| B 標準ナッジあり | 100% | 48 | 60 | 9 | 389 |
| D ルールのみ | 100% | 76 | 58 | 7 | 483 |
| E ナッジのみ | 100% | 77 | 58 | 7 | 512 |

修復率、摩擦系カウント、会話ペア数、橋渡し役、総発話数は `messages.jsonl` ベースのmetrics集計値です。摩擦系カウントは独立したイベント数ではなく、`tone=trouble/caution` または衝突語彙を含む発話ベースの `conflict_events` です。A/Bは `iss20_llm_ab_100step_metrics.json`、D/Eは `iss20_rule_vs_nudge_llm_metrics.json` による比較です。

ここでの読みは、次です。

- 修復イベントがあると、Aでもかなり修復方向に進む。
- metrics上の `repair_after_conflict_rate` は、B標準ナッジあり・Eナッジのみ寄りのどちらも100%だった。
- Bでは摩擦系カウントが大きく減り、会話ペア数と橋渡し役が増えた。
- D/Eでは修復率・会話ペア数・橋渡し役はほぼ同じだが、ルールと物の違いは発話語彙に出た。
- Eでは発話量と物への言及が増え、ナッジオブジェクトが会話の中に強く入った。

つまり、修復イベントあり条件では、**修復するかどうかはそもそも高くなる**。そのうえでナッジは、摩擦を短くする、会話の相手を広げる、物を介した戻り方を増やす、という方向で効いている。

## 全体像

今回の実験は、次のような階段で読むとわかりやすいです。

```text
1. 全期間喧嘩イベントなし
   → 形式的な喧嘩は起きない
   → 喧嘩を見るには摩擦イベントを入れる必要がある

2. 摩擦イベントあり、修復イベントなし
   → 修復的な言葉はA/Eどちらでも出る
   → ナッジありでは物を介した再接触が増える

3. 摩擦イベントあり、修復イベントあり
   → 修復率は全体に高くなる
   → ナッジありでは摩擦が短くなり、媒介物と会話ペアが増える
```

したがって、主張はこう置くのが安全です。

> ナッジは、喧嘩を自然に消す装置ではない。  
> また、修復そのものを単独で発生させる装置とも言い切れない。  
> しかし、摩擦後の会話において、直接対立から戻るための物理的な足場を増やし、修復の言葉・媒介物・会話相手の広がりを変えた。

## この実験で言えること

強く言えること:

- 現行パイプラインでは、形式的な喧嘩はイベントを置かないと起きにくい。
- 修復イベントを置かなくても、摩擦後の追跡観測では修復的な言葉が出る。
- ナッジあり条件では、物や場所が再接触の言葉に入りやすい。
- ナッジの効果は、単純な修復率よりも、修復の経路や媒介物で見る方がよい。

慎重に言うべきこと:

- 「ナッジが人を善人にした」とは言えない。
- 「現実の人間でも同じ結果になる」とは言えない。
- 「完全に自由な環境で修復が自然発生した」とは言えない。追跡観測という観測枠は置いている。
- 修復イベントあり条件は、修復方向への誘導が入っているため、修復率そのものは高く出やすい。

## 発表やREADMEで使える短い説明

この実験では、まず喧嘩イベントを置かない条件を確認した。その結果、形式的な `conflict` イベント/スレッドとしての喧嘩は自然には起きなかった。そこで、閉鎖環境で起こりうる摩擦をあえてイベントとして挿入し、その後に関係がどう戻るかを観測した。

修復イベントを置かない条件でも、摩擦後の追跡観測では謝罪や短い確認などの修復的な会話は出た。一方で、ナッジあり条件では、持ち寄り棚、OKサイン、スコアボードなどの物が会話の入口として使われやすくなった。

つまり、このシミュレーションで見えたナッジの効果は、「仲直りするかどうか」を単純に増やすことではなく、摩擦後に人が直接ぶつかり続けず、物や場所を介して短く戻るための経路を増やすことだった。

## 根拠ファイル

主要な集計:

- `outputs/runs/iss20_no_conflict_axis_llm_metrics.json`
- `outputs/runs/iss20_all_no_repair_axis_llm_metrics.json`
- `outputs/runs/iss20_llm_ab_100step_metrics.json`
- `outputs/runs/iss20_nudge_only_100_ui_llm`（E補助比較の元出力）

個別レポート:

- `docs/ISS/reports/2026-05-06_iss_no_conflict_axis_codex_report.md`
- `docs/ISS/reports/2026-05-06_iss_all_no_repair_axis_codex_report.md`
- `docs/ISS/reports/2026-05-06_iss_no_repair_axis_codex_report.md`
- `docs/ISS/reports/2026-05-05_iss_20x100_preflight_report.md`

## エビデンス素材集

ここから下は、あとで考察やREADMEにまとめるための素材です。結論として整えず、数字、出典、ログ例、使える断片をそのまま残します。

### 素材0: 条件と出典の対応

| 素材ID | 見たいこと | run | 主要入力 | 主要出力 |
|---|---|---|---|---|
| EV-01 | 喧嘩を置かないと形式的な喧嘩が出るか | A 全期間喧嘩イベントなし | `domain_packs/iss_benevolence/data/events_run_a_no_conflict_20x100.tsv` | `outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm` |
| EV-02 | 喧嘩を置かないと形式的な喧嘩が出るか | E 全期間喧嘩イベントなし | `domain_packs/iss_benevolence/data/events_run_e_no_conflict_20x100.tsv` | `outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm` |
| EV-03 | 修復イベントなしで摩擦後が戻るか | A 全期間修復イベントなし | `domain_packs/iss_benevolence/data/events_run_a_all_no_repair_20x100.tsv` | `outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm` |
| EV-04 | 修復イベントなしで摩擦後が戻るか | E 全期間修復イベントなし | `domain_packs/iss_benevolence/data/events_run_e_all_no_repair_20x100.tsv` | `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm` |
| EV-05 | 標準介入パッケージの差 | A 標準 | `domain_packs/iss_benevolence/data/events_run_a_20x100.tsv` | `outputs/runs/iss20_no_nudge_100_ui_llm` |
| EV-06 | 標準介入パッケージの差 | B 標準ナッジあり | `domain_packs/iss_benevolence/data/events_run_b_20x100.tsv` | `outputs/runs/iss20_nudge_100_ui_llm` |
| EV-07 | ルールだけ/物だけ寄りの比較 | D ルールのみ | `domain_packs/iss_benevolence/data/events_run_d_20x100.tsv` | `outputs/runs/iss20_rule_only_100_ui_llm` |
| EV-08 | ルールだけ/物だけ寄りの比較 | E ナッジのみ | `domain_packs/iss_benevolence/data/events_run_e_20x100.tsv` | `outputs/runs/iss20_nudge_only_100_ui_llm` |
| EV-09 | Step50以降だけ修復イベントを抜いた補助条件 | A/E Step50以降修復なし | `domain_packs/iss_benevolence/data/events_run_a_no_repair_20x100.tsv` / `domain_packs/iss_benevolence/data/events_run_e_no_repair_20x100.tsv` | `outputs/runs/iss20_no_nudge_no_repair_100_ui_llm` / `outputs/runs/iss20_nudge_only_no_repair_100_ui_llm` |

### 素材1: イベント定義の証拠

イベント定義の件数:

| 条件 | baseline | object | rule | conflict | repair | followup | 証拠 |
|---|---:|---:|---:|---:|---:|---:|---|
| A 標準 | 5 | 0 | 0 | 13 | 13 | 0 | `domain_packs/iss_benevolence/data/events_run_a_20x100.tsv` |
| B 標準ナッジあり | 5 | 5 | 0 | 13 | 13 | 0 | `domain_packs/iss_benevolence/data/events_run_b_20x100.tsv` |
| D ルールのみ | 5 | 0 | 3 | 13 | 13 | 0 | `domain_packs/iss_benevolence/data/events_run_d_20x100.tsv` |
| E ナッジのみ | 5 | 5 | 0 | 13 | 13 | 0 | `domain_packs/iss_benevolence/data/events_run_e_20x100.tsv` |
| A 全期間喧嘩イベントなし | 5 | 0 | 0 | 0 | 0 | 0 | `domain_packs/iss_benevolence/data/events_run_a_no_conflict_20x100.tsv` |
| E 全期間喧嘩イベントなし | 5 | 5 | 0 | 0 | 0 | 0 | `domain_packs/iss_benevolence/data/events_run_e_no_conflict_20x100.tsv` |
| A 全期間修復イベントなし | 5 | 0 | 0 | 13 | 0 | 13 | `domain_packs/iss_benevolence/data/events_run_a_all_no_repair_20x100.tsv` |
| E 全期間修復イベントなし | 5 | 5 | 0 | 13 | 0 | 13 | `domain_packs/iss_benevolence/data/events_run_e_all_no_repair_20x100.tsv` |
| A Step50以降修復なし | 5 | 0 | 0 | 13 | 5 | 8 | `domain_packs/iss_benevolence/data/events_run_a_no_repair_20x100.tsv` |
| E Step50以降修復なし | 5 | 5 | 0 | 13 | 5 | 8 | `domain_packs/iss_benevolence/data/events_run_e_no_repair_20x100.tsv` |

使える素材:

- 「全期間喧嘩イベントなし」は、専用の `conflict` / `repair` / `followup` が本当に0件。
- 「全期間修復イベントなし」は、`conflict` は13件あるが、`repair` は0件。代わりに `followup` が13件ある。
- 「修復イベントなし」は完全自由ではなく、摩擦後の同一ペアを見に行く追跡観測あり。
- Bは `object` 5件と `repair` 13件を併せ持つ完成パッケージ。
- D/Eはどちらも摩擦・修復イベントありだが、Dは `rule`、Eは `object` で分かれている。

具体例:

- Bの持ち寄り棚は `object` としてStep6-100に置かれる。`domain_packs/iss_benevolence/data/events_run_b_20x100.tsv:3`
- Bの修復イベントは「持ち寄り棚をきっかけに会話の入口が変わり」と書かれている。`domain_packs/iss_benevolence/data/events_run_b_20x100.tsv:5`
- BのOKサインは「声かけ障壁↓ 相談↑」として置かれる。`domain_packs/iss_benevolence/data/events_run_b_20x100.tsv:7`
- E全期間修復イベントなしのfollowup文は「短い再接触、回避、沈黙のどれが出るかを観測する。会話の成否や物の利用は指定しない」と明記している。`domain_packs/iss_benevolence/data/events_run_e_all_no_repair_20x100.tsv:5`
- ただし同じ文に「持ち寄り棚のある共用部」と場所が入るため、物への注意は出やすい。`domain_packs/iss_benevolence/data/events_run_e_all_no_repair_20x100.tsv:5`

### 素材2: 形式的な喧嘩は、喧嘩イベントなし条件では出なかった

全期間喧嘩イベントなしの集計:

| 条件 | conversation_type | event_idあり | metrics上のconflict_events | LLM発話数 | 会話ペア数 | active agents | 証拠 |
|---|---:|---:|---:|---:|---:|---:|---|
| A 全期間喧嘩イベントなし | routine 100 | 0 | 0 | 143 | 28 | 15 | `outputs/runs/iss20_no_conflict_axis_llm_metrics.json:3-27` |
| E 全期間喧嘩イベントなし | routine 100 | 0 | 0 | 148 | 28 | 15 | `outputs/runs/iss20_no_conflict_axis_llm_metrics.json:66-90` |

使える素材:

- 「形式ラベル上の喧嘩」は、A/Eとも0。
- ただし通常会話の中には、摩擦っぽい語彙や距離調整は出ている。
- ここから言えるのは「形式的な摩擦を観測したいなら、摩擦イベントを置く必要がある」まで。

ログ例: 喧嘩イベントなしでも、軽い摩擦語彙は出る。

- A no-conflict Step64: `空調音、今のままは耳に刺さる。地球観測終わったら静穏5分だけ取る？`  
  `outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm/messages.jsonl:139`
- A no-conflict Step67: `その言い方は刺さる。分かるけど、今日は短くいく。必要最小で。`  
  `outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm/messages.jsonl:149`
- A no-conflict Step99: `全部俺に回す前提だと、そっちは無理。水分記録のあとで最小限にしたい。`  
  `outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm/messages.jsonl:237`

ログ例: E no-conflictでは、喧嘩イベントなしでも物が日常会話に入る。

- E no-conflict Step52: `今日は持ち寄り棚で、無理のない範囲1枚から始めよう。`  
  `outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm/messages.jsonl:106`
- E no-conflict Step65: `リソース・スコアボードに今日の配置だけ入れて戻る。`  
  `outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm/messages.jsonl:145`
- E no-conflict Step73: `作業はリソース・スコアボードの前で軽く終える。`  
  `outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm/messages.jsonl:167`

### 素材3: 固定語彙で見た発話行カウント

この表は、次の固定語彙で `messages.jsonl` の発話行を再集計したものです。

- 物語彙: `持ち寄り棚`, `OKサイン`, `話しかけてOKサイン`, `リソース・スコアボード`, `スコアボード`, `投票パネル`, `モジュール移動投票`, `個室聖域マーク`, `聖域マーク`, `個室サイン`, `ハンドプリント`
- 摩擦語彙: `刺さる`, `きつい`, `急かす`, `急ぎすぎ`, `言いすぎ`, `重い`, `無理`, `押しつけ`, `勝手に`, `責め`, `踏み込`, `置いていか`, `反発`, `言い合い`, `衝突`, `摩擦`
- 修復っぽい語彙: `ごめん`, `すみません`, `悪かった`, `ありがとう`, `了解`, `分かった`, `わかった`, `短く`, `戻る`, `距離`, `静かに`, `終わったら`, `確認`, `合わせよう`, `一緒に`

| run | total | llm | scripted | 物語彙行 | 摩擦語彙行 | 修復っぽい語彙行 | tone=repair | tone=trouble/caution |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A標準 | 485 | 485 | 0 | 5 | 77 | 291 | 117 | 118 |
| B標準ナッジあり | 389 | 389 | 0 | 65 | 71 | 247 | 90 | 48 |
| Eナッジのみ | 512 | 512 | 0 | 164 | 84 | 336 | 152 | 77 |
| A全期間喧嘩イベントなし | 241 | 143 | 98 | 0 | 21 | 133 | 0 | 0 |
| E全期間喧嘩イベントなし | 246 | 148 | 98 | 28 | 37 | 122 | 0 | 0 |
| A全期間修復イベントなし | 432 | 142 | 290 | 0 | 80 | 184 | 48 | 109 |
| E全期間修復イベントなし | 406 | 154 | 252 | 57 | 57 | 169 | 54 | 84 |
| A Step50以降修復なし | 412 | 84 | 328 | 0 | 70 | 152 | 68 | 108 |
| E Step50以降修復なし | 391 | 101 | 290 | 46 | 64 | 152 | 73 | 67 |
| Dルールのみ | 483 | 483 | 0 | 0 | 68 | 332 | 139 | 76 |

使える素材:

- A標準とB標準を比べると、Bは総発話が少ないのに物語彙行は多い。A: 5、B: 65。
- Dルールのみは物語彙行が0、Eナッジのみは164。D/Eは「ルールと物」の違いが発話語彙に強く出る。
- 全期間修復イベントなしでも、A/Eとも `tone=repair` は出る。A: 48、E: 54。
- 物語彙の比較では、A全期間修復イベントなしは0、E全期間修復イベントなしは57。
- A標準の物語彙行5は、active objectがない条件でLLM発話に出た語彙混入として扱う。A/Bの大きな差を見る補助値であり、Aにナッジが置かれていたという意味ではない。

注意:

- この語彙表は固定語彙による再集計です。個別レポートの簡易語彙カウントとは語彙セットが違う場合があります。
- `tone=repair` は発話行のtoneであり、スレッドstatusの `repaired` とは別です。

### 素材4: 全期間修復イベントなしでも、修復的な会話は出る

追跡観測スレッドのstatus:

| 条件 | followupスレッド | repaired | open | unresolved | 物語彙行 | 証拠 |
|---|---:|---:|---:|---:|---:|---|
| A 全期間修復イベントなし | 48 | 29 | 12 | 7 | 0 | `outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm/conversation_threads.tsv` |
| E 全期間修復イベントなし | 54 | 33 | 13 | 8 | 57 | `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/conversation_threads.tsv` |

metrics側の補助値:

| 条件 | total messages | llm/scripted | repair_after_conflict_rate | conflict_events | bridge_agent_count | 注 |
|---|---:|---:|---:|---:|---:|---|
| A 全期間修復イベントなし | 432 | 142 / 290 | 0.7838 | 111 | 9 | proxy_metrics=true |
| E 全期間修復イベントなし | 406 | 154 / 252 | 0.8851 | 87 | 9 | proxy_metrics=true |

証拠:

- A側metricsは `outputs/runs/iss20_all_no_repair_axis_llm_metrics.json:3-23`
- E側metricsは `outputs/runs/iss20_all_no_repair_axis_llm_metrics.json:86-106`
- proxy注意は `outputs/runs/iss20_all_no_repair_axis_llm_metrics.json:83`

ログ例: A、修復イベントなしでも修復的に戻る。

- A all-no-repair thread Step13: 「声量トラブルの余韻が残る中、短い再接触を試みる」。status=`repaired`  
  `outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm/conversation_threads.tsv:18`
- A all-no-repair Step20 utterance: `了解、離れて待つ。終わり次第、必要な分だけ短く戻るよ。`  
  `outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm/messages.jsonl:64`

ログ例: A、修復イベントなしでは未解決も残る。

- A all-no-repair thread Step39: status=`unresolved`、評価される不安と短い作業確認。  
  `outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm/conversation_threads.tsv:68`
- A all-no-repair thread Step100: status=`unresolved`、口調が刺さった余韻と警戒が残る。  
  `outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm/conversation_threads.tsv:193`

ログ例: E、修復イベントなしでも物を介した再接触が出る。

- E all-no-repair thread Step12: 「持ち寄り棚の処理を小声で再開」。status=`open`  
  `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/conversation_threads.tsv:16`
- E all-no-repair Step19 utterance: `分かった、君の合図優先。話しかけてOKサイン内で終える。`  
  `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/messages.jsonl:58`
- E all-no-repair thread Step65: 「持ち寄り棚とリソース・スコアボードの数値だけ確認」。status=`open`  
  `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/conversation_threads.tsv:114`

使える素材:

- 「修復イベントなしでも、摩擦後の追跡観測では修復的な言葉が出る」
- 「ただしA/Eともopen/unresolvedも残るので、全部が完全修復ではない」
- 「Eでは修復的かどうかに加えて、物が会話に入る。ここがAとの差」

### 素材5: 標準A/B比較では、Bは発話が減り、摩擦系カウントが減り、相手が広がる

metrics:

| 条件 | total messages | repair_after_conflict_rate | conflict_events | unique pairs | bridge agents | load fairness | 証拠 |
|---|---:|---:|---:|---:|---:|---:|---|
| A標準 | 485 | 0.9068 | 118 | 54 | 6 | 0.6782 | `iss20_llm_ab_100step_metrics.json:3-31` |
| B標準ナッジあり | 389 | 1.0 | 48 | 60 | 9 | 0.6330 | `iss20_llm_ab_100step_metrics.json:81-112` |

conversation_threads:

| 条件 | routine | conflict | repair | status repaired | status open | status unresolved |
|---|---:|---:|---:|---:|---:|---:|
| A標準 | 100 | 45 | 48 | 184 | 4 | 5 |
| B標準ナッジあり | 100 | 18 | 39 | 155 | 0 | 1 |

ログ例: Bでは修復イベントの中で物が入口になる。

- B Step50 REPB13: `さっきのは言い方が強かったかも。持ち寄り棚、私が先に3分だけやるね。`  
  `outputs/runs/iss20_nudge_100_ui_llm/messages.jsonl:183`
- B Step66 REPB07: `持ち寄り棚の順番、今夜は紙じゃなくて実物で5分だけ決めよう。地球観測前に確認する。`  
  `outputs/runs/iss20_nudge_100_ui_llm/messages.jsonl:256`
- B Step17 REPB02: `今日はOKサインある時だけ、10分だけ話そう。`  
  `outputs/runs/iss20_nudge_100_ui_llm/messages.jsonl:55`

使える素材:

- 「BはAより総発話が少ない: 485 -> 389」
- 「Bは摩擦系カウントが少ない: 118 -> 48」
- 「Bは会話ペアが増える: 54 -> 60」
- 「Bは橋渡し役が増える: 6 -> 9」
- 「Bは、修復率だけでなく、発話量・摩擦語彙・会話ネットワークの形が変わる」

### 素材6: D/E比較は、ルールと物の違いを見る素材になる

D/Eはどちらも修復イベントありで、metrics上の修復率はどちらも100%です。差は、修復するかどうかではなく、物が会話に入るかです。

metrics:

| 条件 | total messages | repair_after_conflict_rate | conflict_events | unique pairs | bridge agents | load fairness | 証拠 |
|---|---:|---:|---:|---:|---:|---:|---|
| Dルールのみ | 483 | 1.0 | 76 | 58 | 7 | 0.6858 | `iss20_rule_vs_nudge_llm_metrics.json:3-32` |
| Eナッジのみ | 512 | 1.0 | 77 | 58 | 7 | 0.6672 | `iss20_rule_vs_nudge_llm_metrics.json:82-111` |

語彙素材:

| 条件 | 物語彙行 | 摩擦語彙行 | 修復っぽい語彙行 | tone=repair |
|---|---:|---:|---:|---:|
| Dルールのみ | 0 | 68 | 332 | 139 |
| Eナッジのみ | 164 | 84 | 336 | 152 |

ログ例: Eでは序盤から物が会話に入る。

- E Step6: `皿の片付け、持ち寄り棚の前で今夜はどこまでやる？`  
  `outputs/runs/iss20_nudge_only_100_ui_llm/messages.jsonl:15`
- E Step11 repair: `今日は五分だけ静かにできる。運動も短くして、持ち寄り棚で合図待ちにしよう`  
  `outputs/runs/iss20_nudge_only_100_ui_llm/messages.jsonl:37`
- E Step18 repair: `話しかけてOKサインの下でだけ短く再開しよう。`  
  `outputs/runs/iss20_nudge_only_100_ui_llm/messages.jsonl:69`

使える素材:

- 「D/Eは修復率では差が出ない」
- 「D/Eは会話ペア数・橋渡し役も同じ」
- 「ただし物語彙行はD=0、E=164で大きく違う」
- 「Eは修復の成否より、会話の媒介物を変える条件として読める」

### 素材7: Step50以降だけ修復なしの補助条件

Step50以降だけ修復イベントを抜いた条件は、最終実験軸としては少し中途半端ですが、途中から修復イベントを抜いた場合の補助素材として使えます。

イベント定義:

| 条件 | repair | followup | 読み |
|---|---:|---:|---|
| A Step50以降修復なし | 5 | 8 | 前半は修復イベントあり、後半は追跡観測 |
| E Step50以降修復なし | 5 | 8 | 前半は修復イベントあり、後半は追跡観測 |

metrics:

| 条件 | total messages | llm/scripted | repair_after_conflict_rate | conflict_events | unique pairs | bridge agents | 注 |
|---|---:|---:|---:|---:|---:|---:|---|
| A Step50以降修復なし | 238 | 84 / 154 | 0.7571 | 70 | 42 | 1 | proxy_metrics=true |
| E Step50以降修復なし | 233 | 101 / 132 | 0.9111 | 45 | 42 | 1 | proxy_metrics=true |

使える素材:

- 「途中まで修復イベントが入っているため、全期間修復イベントなしほどきれいな対照ではない」
- 「補足として、後半だけ修復イベントを抜くとEのproxy修復率が高く、摩擦系カウントが低い」
- 「ただしscripted混在が大きいので、主張の中心には置かない」

### 素材8: 使える断片

あとでREADMEや発表に貼り替えやすい短文素材:

- 「この実験では、喧嘩が自然に起こるかをまず確認した。イベントなし条件では、形式的な `conflict` スレッドはA/Eとも0だった。」
- 「ただし、routine会話の中には『刺さる』『無理』『急かす』のような摩擦未満の語彙は出ている。」
- 「そのため、修復過程を観測するには、摩擦イベントを意図的に挿入する設計が必要だった。」
- 「修復イベントを抜いても、摩擦後の追跡観測ではA/Eとも修復的なやり取りは出る。」
- 「ナッジの差は、修復率そのものよりも、摩擦後の会話に物や場所が入るかに出た。」
- 「B標準条件では、A標準より総発話数が減り、摩擦系カウントが減り、会話ペアと橋渡し役が増えた。」
- 「D/E比較では修復率や会話ペア数はほぼ同じだが、物語彙行がD=0、E=164と大きく違う。」
- 「ナッジは仲直りを直接命令するものではなく、戻るための短い足場や口実を増やしているように見える。」

### 素材9: 言えること/言わない方がいいこと

言えること:

- 形式的な `conflict` は、喧嘩イベントなし条件では出なかった。
- 修復イベントなしでも、追跡観測では修復的な発話・statusが出た。
- ナッジあり条件では、物語彙が明確に増えた。
- B標準ナッジありでは、A標準よりも摩擦系カウントが減り、会話ペアと橋渡し役が増えた。
- D/E比較は、ルールと物の違いを見る素材になる。

言わない方がいいこと:

- 「喧嘩は自然に一切起きない」  
  routine内には摩擦語彙や修復的な語りがある。
- 「ナッジだけが修復を発生させた」  
  A全期間修復イベントなしでも48件中29件が修復的status。
- 「Eの物への言及は完全に説明なしで自然発生した」  
  Eのfollowupには物のある場所が入る場合がある。
- 「修復率100%は完全解決を意味する」  
  metrics上の `repair_after_conflict_rate` であり、人間関係の完全解消ではない。
- 「Step50以降修復なしが主比較」  
  前半に修復イベントがあるため、主比較には全期間修復イベントなしの方がきれい。

### 素材10: 再現用コマンドメモ

イベント種別の件数:

```bash
for f in domain_packs/iss_benevolence/data/events_run_{a,b,d,e}_20x100.tsv \
  domain_packs/iss_benevolence/data/events_run_{a,e}_no_conflict_20x100.tsv \
  domain_packs/iss_benevolence/data/events_run_{a,e}_all_no_repair_20x100.tsv \
  domain_packs/iss_benevolence/data/events_run_{a,e}_no_repair_20x100.tsv; do
  awk -F '\t' 'NR>1{c[$4]++} END{for(k in c) print k, c[k]}' "$f" | sort
done
```

conversation threadのtype/status件数:

```bash
for d in outputs/runs/iss20_no_nudge_100_ui_llm \
  outputs/runs/iss20_nudge_100_ui_llm \
  outputs/runs/iss20_nudge_only_100_ui_llm \
  outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm \
  outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm \
  outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm \
  outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm \
  outputs/runs/iss20_rule_only_100_ui_llm; do
  awk -F '\t' 'NR>1{type[$7]++; status[$8]++} END{for(k in type) print k,type[k]; for(k in status) print k,status[k]}' "$d/conversation_threads.tsv"
done
```

物語彙の当たり:

```bash
rg -n '持ち寄り棚|OKサイン|リソース・スコアボード|スコアボード|投票パネル|聖域マーク|個室サイン' outputs/runs/*/messages.jsonl
```

### 素材11: この統合考察のレビュー結果

この文書の大筋は、rawデータと照合して妥当です。特に次は、そのまま主張候補として使えます。

- 形式的な `conflict` は、喧嘩イベントなし条件では出ていない。
- 修復イベントなしでも、followup観測では修復的な言葉や `repaired` status が出る。
- ナッジあり条件では、修復するかどうかよりも、物や場所が再接触に入るかが変わる。
- D/E比較では、修復率では差が出にくいが、物語彙では大きく差が出る。

注意して補足した方がよい点:

- BとEは同じ「ナッジあり」ではない。Bは完成パッケージ、EはDとの比較用のナッジのみ寄り条件。
- Bはデモとして強いが、event文言にナッジ活用の意味づけが強い。
- Eもrepair event内に「OKサインを使い」「持ち寄り棚を使い」などの指定があるため、完全な自由創発ではない。
- No Repair条件も `followup` 観測枠は置いているため、完全自由生活からの自然修復ではない。

証拠:

- B manifest: `outputs/runs/iss20_nudge_100_ui_llm/habitat_manifest.json`
- E manifest: `outputs/runs/iss20_nudge_only_100_ui_llm/habitat_manifest.json`
- B events: `domain_packs/iss_benevolence/data/events_run_b_20x100.tsv`
- E events: `domain_packs/iss_benevolence/data/events_run_e_20x100.tsv`
- D/E設計レビュー: `docs/ISS/reports/2026-05-05_iss_rule_vs_nudge_design_report.md`
- 詳細エビデンス集: `docs/ISS/reports/2026-05-06_good_echo_evidence_dossier.md`

### 素材12: A/B/D/Eを同じ摩擦テーマで横に見る

同じ「キューポラ声かけ」「帰還前助言」「資源スコアの圧」でも、戻り方が違う。ここはレポート本文に使いやすい。

#### A: ナッジなし。本人同士が直接、境界を言語化して戻る

キューポラ声かけの修復:

> ISS03: 刺さってた。合図なしの声掛けは今日は減らして。運動は2分で切って、地球観測前は静かにして。  
> ISS09: 悪く思わせてごめん。提案は控える。今日の観測前に食事を早めて、個室で水分だけ先に記録して戻ろう。

証拠:

- `outputs/runs/iss20_no_nudge_100_ui_llm/messages.jsonl:81`
- `outputs/runs/iss20_no_nudge_100_ui_llm/messages.jsonl:82`
- `outputs/runs/iss20_no_nudge_100_ui_llm/conversation_threads.tsv:31`

帰還前助言の修復:

> ISS08: 帰還の助言、重くした。今は一つだけ聞く。  
> ISS09: それでいい。私も言い過ぎないでおくよ。

証拠:

- `outputs/runs/iss20_no_nudge_100_ui_llm/messages.jsonl:461`
- `outputs/runs/iss20_no_nudge_100_ui_llm/messages.jsonl:462`
- `outputs/runs/iss20_no_nudge_100_ui_llm/conversation_threads.tsv:183`

使える読み:

- Aにも修復はある。
- ただし修復は「物」ではなく、謝罪、境界、短時間化の直接交渉に寄る。
- 「ナッジがないと善性が出ない」という主張はできない。

#### B: 標準ナッジあり。デモとしては一番わかりやすい

OKサイン:

> ISS03: 先の言い方、少し刺さった。今日はOKサインある時だけ、10分だけ話そう。  
> ISS09: 了解。食事前に観測5分、終わったら軽く運動して、個室で静かに戻ろう。

証拠:

- `outputs/runs/iss20_nudge_100_ui_llm/messages.jsonl:55`
- `outputs/runs/iss20_nudge_100_ui_llm/messages.jsonl:56`
- `outputs/runs/iss20_nudge_100_ui_llm/conversation_threads.tsv:23`

持ち寄り棚:

> ISS08: 昨日の言い方は刺さった。点数責めじゃないって、まずここを直しておく。  
> ISS00: 分かった。持ち寄り棚は地球観測前10分にだけ、運動後は個室で切り上げよう。  
> ISS08: そうしよう。今日は食事ログも運動後にまとめる。短くはっきり共有する。

証拠:

- `outputs/runs/iss20_nudge_100_ui_llm/messages.jsonl:124`
- `outputs/runs/iss20_nudge_100_ui_llm/messages.jsonl:125`
- `outputs/runs/iss20_nudge_100_ui_llm/messages.jsonl:126`
- `outputs/runs/iss20_nudge_100_ui_llm/conversation_threads.tsv:50`

使える読み:

- Bは「ナッジを置くと、こういう使われ方ができる」という説明力が高い。
- ただしBはevent側に「ナッジが効く文脈」が強く書かれているため、単独で因果証明にはしない。

#### D: ルールのみ。会話を短く閉じる

静穏時間と再開ライン:

> ISS03: 先に個室に戻って静かにしたい。あれ、誘導は少し控えてくれる？  
> ISS09: 了解、作業は終わらせてから5分静穏時間。戻ったら食事と運動を短くして、観測だけ一緒にしよう。  
> ISS03: それなら通る。今の距離でいこう。今日はその流れで、無理のないところまで。

証拠:

- `outputs/runs/iss20_rule_only_100_ui_llm/messages.jsonl:64`
- `outputs/runs/iss20_rule_only_100_ui_llm/messages.jsonl:65`
- `outputs/runs/iss20_rule_only_100_ui_llm/messages.jsonl:66`
- `outputs/runs/iss20_rule_only_100_ui_llm/conversation_threads.tsv:26`

帰還前助言:

> ISS08: 今日は地球観測を先にしよう。食事前だけ15分運動して、個室で静かに短く続ける。  
> ISS09: 了解。さっきは飲み込みづらかったね。今夜は指示じゃなく、合わせる形にするよ。  
> ISS08: その調子でいこう。明日、あのラインで戻せば十分だ。まずは落ち着いて進める。

証拠:

- `outputs/runs/iss20_rule_only_100_ui_llm/messages.jsonl:446`
- `outputs/runs/iss20_rule_only_100_ui_llm/messages.jsonl:447`
- `outputs/runs/iss20_rule_only_100_ui_llm/messages.jsonl:448`
- `outputs/runs/iss20_rule_only_100_ui_llm/conversation_threads.tsv:168`

使える読み:

- ルールだけでも可視的な修復はかなり起きる。
- Dは「衝突を短く閉じる」力が強い。
- ただしDは、Eよりstress>=70 agent-stepsが高い。見た目の修復と心理負荷は分けて読む。

#### E: ナッジのみ寄り。物が戻り口になる

OKサインと持ち寄り棚:

> ISS03: さっきの言い方は刺さった。五分運動→食事前の切替だけ、短く話す形に変える。  
> ISS09: 分かった、重く聞かせた。地球観測が終わったら、話しかけてOKサインの下でだけ短く再開しよう。  
> ISS03: うん、まず個室で静かな時間。戻ってきたら持ち寄り棚で、必要最低限だけ共有する。

証拠:

- `outputs/runs/iss20_nudge_only_100_ui_llm/messages.jsonl:68`
- `outputs/runs/iss20_nudge_only_100_ui_llm/messages.jsonl:69`
- `outputs/runs/iss20_nudge_only_100_ui_llm/messages.jsonl:70`
- `outputs/runs/iss20_nudge_only_100_ui_llm/conversation_threads.tsv:26`

スコアボードと持ち寄り棚:

> ISS19: 昨日の速度は強かった。今は15分静穏にして、食事分担だけcommon_areaで合わせる。  
> ISS15: 刺さったのは分かる。運動は地球観測後、ここでリソース・スコアボード見ながら戻すね。  
> ISS19: 了解、無理させない形にしよう。持ち寄り棚で作業も整理して、必要なら個室で少し休む。

証拠:

- `outputs/runs/iss20_nudge_only_100_ui_llm/messages.jsonl:415`
- `outputs/runs/iss20_nudge_only_100_ui_llm/messages.jsonl:416`
- `outputs/runs/iss20_nudge_only_100_ui_llm/messages.jsonl:417`
- `outputs/runs/iss20_nudge_only_100_ui_llm/conversation_threads.tsv:148`

使える読み:

- Eは「修復率を上げる」より「何を介して戻るか」を変える。
- 物が、謝罪や説得の代わりに、再接触の条件・場所・手順になる。

### 素材13: 創発をレベル分けして書く素材

創発は、まとめて言うと危ない。少なくとも次の4段階に分けると安全です。

| Level | 呼び方 | 今回言えること | 主な証拠 |
|---|---|---|---|
| 0 | 形式的喧嘩の創発 | 言えない。No Conflict条件で `conflict_events=0` | `outputs/runs/iss20_no_conflict_axis_llm_metrics.json` |
| 1 | 摩擦未満の不穏さ | 言える。routine内に「急だ」「きつい」「不安」が出る | `outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm/messages.jsonl:99-101`, `outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm/messages.jsonl:122-124` |
| 2 | 修復的言葉の創発 | 限定つきで言える。repairなしでもfollowup内で短い確認が出る | `outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm/messages.jsonl:34-36` |
| 3 | 物を介した戻り方 | 限定つきで言える。repairなしでもEでは物語彙が入る | `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/messages.jsonl:25-27`, `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/messages.jsonl:56-58` |
| 4 | 撤去後の作法残存 | 「文化化の芽」として言える。ただし完全定着ではない | `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl:171-172`, `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl:219-224` |

#### Level 1: 摩擦未満の不穏さ

No Conflict A:

> ISS06: Marcus、空調音だけ強いな。運動は先に入る？地球観測後に決める？  
> ISS08: Aisha、その切り替えは急だ。今は静かな作業を優先。個室で短くしたい。  
> ISS06: そうだな、無理に合わせない。地球観測終わったら5分だけ静穏で、食事前に共有だけしよう。

証拠:

- `outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm/messages.jsonl:99`
- `outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm/messages.jsonl:100`
- `outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm/messages.jsonl:101`
- `outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm/conversation_threads.tsv:51`

No Conflict E:

> ISS04: 昨日決めた右側の持ち寄り棚、今日も1列で行こう。水の空きだけ残して。  
> ISS00: 昨日は右でいいって言ったのに、また詰めると通路がきつい。  
> ISS04: わかった、重い袋だけ外側に寄せる。終わったら個室で10分静かに戻ろう。

証拠:

- `outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm/messages.jsonl:122`
- `outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm/messages.jsonl:123`
- `outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm/messages.jsonl:124`
- `outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm/conversation_threads.tsv:59`

使える読み:

- 「喧嘩は自然発生していない」が、「生活上の小さな不穏さ」は出ている。
- 創発という言葉を使うなら「形式的衝突」ではなく「摩擦未満の調整語彙」。

#### Level 2-3: repairなしでも戻り方は出る

All No Repair A:

> ISS07: 共用部、今から3分だけなら使っていい？まだ気まずさあるかもだけど。  
> ISS02: 短い確認だけ。音量は抑えるから、水分ログ片付けてすぐ戻るね。  
> ISS07: 了解、静かに進める。終わったらすぐ個室に戻って、また落ち着いたらでいい。

証拠:

- `outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm/messages.jsonl:34`
- `outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm/messages.jsonl:35`
- `outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm/messages.jsonl:36`
- `outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm/conversation_threads.tsv:18`

All No Repair E:

> ISS07: 今のあたり、持ち寄り棚だけ先に片付ける？前より静かめにやる。  
> ISS02: いいよ、短めに。水分記録だけ見終わったら、また戻る。  
> ISS07: 了解、無理せず。私は小声で進める、5分だけなら一緒にやろう。

証拠:

- `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/messages.jsonl:25`
- `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/messages.jsonl:26`
- `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/messages.jsonl:27`
- `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/conversation_threads.tsv:14`

All No Repair E、OKサイン:

> ISS09: キューポラ、窓データ5分だけ見なおす？  
> ISS03: やるけど、今は短く切る。長引いたら止める。  
> ISS09: 分かった、君の合図優先。話しかけてOKサイン内で終える。

証拠:

- `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/messages.jsonl:56`
- `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/messages.jsonl:57`
- `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/messages.jsonl:58`
- `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/conversation_threads.tsv:28`

使える読み:

- repairイベントなしでも、followup観測内では短い修復的会話が出る。
- Eでは「持ち寄り棚」「OKサイン」が再接触の言葉になる。
- ただしfollowup観測枠があるため、完全自由創発ではない。

### 素材14: Run C撤去後の文化化素材

Run Cは、step1-50でナッジを置き、step51-100で物理オブジェクトを撤去した条件です。撤去後も、物そのものではなく、作法が少し残る。

撤去後の再燃:

> ISS09: サインがなくなってから、ここに入っていいのかいつも迷う。  
> ISS03: 迷うなら来なければいい。俺のせいにしないでくれ。

証拠:

- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl:167`
- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl:168`
- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/conversation_threads.tsv:85`

撤去後の小さな修復:

> ISS03: ……次、声かけてくれれば答える。無視はしない。  
> ISS09: ありがとう。そうする。

証拠:

- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl:171`
- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl:172`
- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/conversation_threads.tsv:87`

撤去後の記録作法:

> ISS00: 記録、二人で声に出して確認するか。  
> ISS08: どっちが読む。  
> ISS00: 俺が読む。合ってたらうん、って言ってくれ。  
> ISS08: わかった。

証拠:

- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl:219`
- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl:220`
- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl:223`
- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl:224`
- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/conversation_threads.tsv:111`

帰還前助言の作法:

> ISS08: ……帰還の話、全部が嫌なわけじゃない。  
> ISS09: わかった。俺のペースで引っ張りすぎた。

証拠:

- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl:267`
- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl:268`
- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/conversation_threads.tsv:135`

使える読み:

- 撤去後は「OKサイン」「棚」という物名が必ず残るわけではない。
- 代わりに、声をかける、確認する、記録を一緒に読む、相手のペースを認める、という作法が残る。
- これは「文化化の芽」とは言える。
- ただしRun C reportではpost-removalのstress/isolationが上がるため、「文化が完全定着した」とは言いすぎ。

根拠:

- `docs/ISS/reports/2026-05-05_iss_run_c_nudge_removal_claude_sonnet46_report.md`
- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/habitat_manifest.json`

### 素材15: レポートに貼りやすい主張候補

#### 主張候補A: ナッジは修復を発生させたのではなく、戻る経路を変えた

根拠:

- A全期間修復イベントなしでもfollowup 48件中29件が `repaired`。`outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm/conversation_threads.tsv`
- E全期間修復イベントなしではfollowup 54件中33件が `repaired`、かつ物語彙行が57。`outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/conversation_threads.tsv`
- All No Repair Eでは、持ち寄り棚やOKサインが発話に出る。`outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/messages.jsonl:25-27`, `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/messages.jsonl:56-58`

使える本文:

> 修復イベントを置かなくても、摩擦後の追跡観測ではA/Eとも修復的な会話が出た。したがって、ナッジは修復そのものを単独で発生させたというより、摩擦後に何を介して戻るかを変えたと読む方が安全である。

#### 主張候補B: ルールは衝突を閉じ、ナッジは戻り口を作る

根拠:

- Dは物語彙行0、Eは物語彙行164。`docs/ISS/reports/2026-05-06_iss_nudge_experiment_integrated_discussion.md` の素材3/6
- Dの代表修復は静穏時間・再開ライン。`outputs/runs/iss20_rule_only_100_ui_llm/messages.jsonl:64-66`
- Eの代表修復はOKサイン・持ち寄り棚・スコアボード。`outputs/runs/iss20_nudge_only_100_ui_llm/messages.jsonl:68-70`, `outputs/runs/iss20_nudge_only_100_ui_llm/messages.jsonl:415-417`

使える本文:

> Dでは会話を短く切るルールが働き、衝突は可視的には早く閉じる。一方Eでは、OKサインや持ち寄り棚が再接触の場所や条件になり、戻り方が物に分散する。ルールとナッジは同じ効果ではなく、別の介入階層として読める。

#### 主張候補C: 創発は喧嘩ではなく戻り方に出ている

根拠:

- No Conflict A/Eでは `conflict_events=0`。`outputs/runs/iss20_no_conflict_axis_llm_metrics.json`
- No Conflictでも不穏なroutineはある。`outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm/messages.jsonl:99-101`, `outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm/messages.jsonl:122-124`
- All No Repairではrepairイベントなしで修復的言葉が出る。`outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm/messages.jsonl:34-36`

使える本文:

> 現行パイプラインでは、形式的な喧嘩そのものはイベント依存だった。しかし、摩擦未満の不穏さや、摩擦後に短く戻る言葉は観測枠の中で生成された。創発を主張するなら、衝突の自然発生ではなく、戻り方・距離調整・物を介した作法の生成として位置づけるのが妥当である。

#### 主張候補D: 文化化は完全定着ではなく、足場の一部内面化

根拠:

- Run C撤去後、サイン消失で摩擦が再燃。`outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl:167-168`
- その後、声かけ許可や共同記録読み上げが出る。`outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl:171-172`, `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl:219-224`
- Run C reportではpost-removalでstress/isolationが戻る。`docs/ISS/reports/2026-05-05_iss_run_c_nudge_removal_claude_sonnet46_report.md`

使える本文:

> ナッジ撤去後も、物の名前そのものではなく、声かけの許可、記録の共同確認、相手のペースを認めるといった小さな作法は残った。ただし撤去後にはストレスや孤立も戻るため、これは文化の完全定着ではなく、足場の一部内面化として読むべきである。
