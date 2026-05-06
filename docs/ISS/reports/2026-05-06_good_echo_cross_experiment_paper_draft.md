# GOOD ECHO 横断実験ペーパー草案

Date: 2026-05-06

## Title

GOOD ECHO: 閉鎖高ストレス環境で「善性を育む環境設計」は、衝突と修復の経路をどう変えるか

## Abstract

本研究は、ISS型の閉鎖居住環境を題材に、ナッジオブジェクト、会話ルール、摩擦イベント、修復イベントの有無を切り替え、LLMエージェントの会話と状態変化を比較した。結果として、現行パイプラインでは形式的な喧嘩はイベント依存であり、完全な自然発生とは言えない。一方で、修復イベントを置かない条件でも、摩擦後の追跡観測では謝罪、短い確認、距離の取り直しが出た。ナッジの主効果は、修復率を単純に上げることではなく、持ち寄り棚、OKサイン、スコアボードなどの物を介して、直接対立から戻るための経路を増やすことに見える。

## Research Question

問いは3つに分ける。

1. 閉鎖高ストレス環境では、衝突は自然に創発するのか。
2. 明示的な修復イベントがなくても、摩擦後に修復的な会話は生まれるのか。
3. ナッジオブジェクトは「修復するかどうか」ではなく「何を介して戻るか」を変えるのか。

## Experiment Map

| 条件 | 人数/step | ナッジ | ルール | 摩擦 | 修復 | 主な役割 | 根拠 |
|---|---:|---|---|---|---|---|---|
| A no nudge | 20/100 | なし | なし | あり | あり | 標準対照 | `outputs/runs/iss20_no_nudge_100_ui_llm` |
| B nudge package | 20/100 | あり | なし | あり | あり | 完成ナッジデモ | `outputs/runs/iss20_nudge_100_ui_llm` |
| C nudge removal | 10/100 | 1-50あり、51-100撤去 | なし | あり | あり | ナッジ経験が残るか | `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46` |
| D rule only | 20/100 | なし | あり | あり | あり | 短時間会話ルールのみ | `outputs/runs/iss20_rule_only_100_ui_llm` |
| E nudge only | 20/100 | あり | なし | あり | あり | ナッジのみ比較 | `outputs/runs/iss20_nudge_only_100_ui_llm` |
| No Conflict A/E | 20/100 | Aなし/Eあり | なし | なし | なし | 衝突が自然発生するか | `outputs/runs/iss20_no_conflict_axis_llm_metrics.json` |
| All No Repair A/E | 20/100 | Aなし/Eあり | なし | あり | なし | 修復イベントなしで戻るか | `outputs/runs/iss20_all_no_repair_axis_llm_metrics.json` |

主要な設計レポート:

- `docs/ISS/reports/2026-05-05_iss_20x100_preflight_report.md`
- `docs/ISS/reports/2026-05-05_iss_rule_vs_nudge_design_report.md`
- `docs/ISS/reports/2026-05-05_iss_run_c_nudge_removal_claude_sonnet46_report.md`
- `docs/ISS/reports/2026-05-06_iss_no_conflict_axis_codex_report.md`
- `docs/ISS/reports/2026-05-06_iss_all_no_repair_axis_codex_report.md`
- `docs/ISS/reports/2026-05-06_iss_nudge_experiment_integrated_discussion.md`

## B と E の正確な違い

BとEはどちらもナッジありだが、同じ意味ではない。

| 観点 | B: standard nudge package | E: nudge only |
|---|---|---|
| 目的 | A/Bデモとして「ナッジあり環境がどう使えるか」を見せる | D rule only と比較し、ルールではなく物が何を変えるかを見る |
| イベント定義 | ナッジが効く文脈を強めに書いている | D/E比較前に文言を中立化。修復方向は `距離再調整↑ 継続観察↑` に統一 |
| 修復文言 | 「持ち寄り棚をきっかけに」「声かけ許可」「共同達成」「経験共有」など、結果の意味づけが強い | 「OKサインを使い」「スコアボードを使い」など物の使用は指定するが、勝敗を先取りする語は弱めた |
| 会話履歴 | `history_size=12` | `history_size=4` |
| 生成スレッド | 157 threads / 389 messages | 180 threads / 512 messages |
| 読み方 | 完成パッケージの効果を見る条件 | Dとの比較で、ルールではなくナッジが媒介物として働くかを見る条件 |

根拠:

- B manifest: `outputs/runs/iss20_nudge_100_ui_llm/habitat_manifest.json`
- E manifest: `outputs/runs/iss20_nudge_only_100_ui_llm/habitat_manifest.json`
- B event定義: `domain_packs/iss_benevolence/data/events_run_b_20x100.tsv`
- E event定義: `domain_packs/iss_benevolence/data/events_run_e_20x100.tsv`
- D event定義: `domain_packs/iss_benevolence/data/events_run_d_20x100.tsv`
- D/E設計レビュー: `docs/ISS/reports/2026-05-05_iss_rule_vs_nudge_design_report.md`

重要な注意: Bは「創発の証明」には使いすぎない方がよい。Bはプロダクトデモとして強く、Eや軸削除実験の方がメカニズム検証に向いている。

## Quantitative Results

### 1. A/B 20人100step: 完成ナッジ条件は摩擦を短くした

| 指標 | A no nudge | B nudge package | 読み |
|---|---:|---:|---|
| messages | 485 | 389 | Bは会話量が少ない |
| unique pairs | 54 | 60 | Bは接触相手が広い |
| repair_after_conflict_rate | 0.9068 | 1.0000 | Bは衝突後の修復到達が高い |
| conflict_events metric | 118 | 48 | Bは摩擦発話が少ない |
| bridge agents | 6 | 9 | Bは橋渡し役が広い |

根拠:

- Metrics: `outputs/runs/iss20_llm_ab_100step_metrics.json`
- A raw messages: `outputs/runs/iss20_no_nudge_100_ui_llm/messages.jsonl`
- B raw messages: `outputs/runs/iss20_nudge_100_ui_llm/messages.jsonl`
- A/B report: `docs/ISS/reports/2026-05-05_iss_20x100_preflight_report.md`

ただしAの20/100は途中でモデルが切り替わった caveat がある。主張は「Bが絶対に優れている」ではなく、「完成ナッジ条件では摩擦の滞留が短く見える」と置く。

### 2. D/E: ルールだけでも修復するが、ナッジは媒介物を変えた

| 指標 | D rule only | E nudge only | 読み |
|---|---:|---:|---|
| messages | 483 | 512 | Eはむしろ発話が増えた |
| conversation threads | 180 | 180 | 条件は揃っている |
| conflict threads | 26 | 26 | 摩擦イベント数は揃っている |
| repair threads | 54 | 54 | 修復イベント数も揃っている |
| repair_after_conflict_rate | 1.0 | 1.0 | 修復率だけでは差が見えない |
| object mention messages | 1 | 174 | Eは物が会話に大量に入る |

根拠:

- Metrics: `outputs/runs/iss20_rule_vs_nudge_llm_metrics.json`
- D raw: `outputs/runs/iss20_rule_only_100_ui_llm/messages.jsonl`
- E raw: `outputs/runs/iss20_nudge_only_100_ui_llm/messages.jsonl`
- D/E design report: `docs/ISS/reports/2026-05-05_iss_rule_vs_nudge_design_report.md`

D/Eの結果は「ナッジありなら会話が減る」とは言っていない。むしろEでは発話が増えた。面白いのは、Eでは修復が人間同士の直接交渉だけでなく、棚、サイン、スコアボードなどを介した再接触になる点。

### 3. No Conflict Axis: 形式的な喧嘩は自然発生しなかった

全期間喧嘩イベントなしでは、A/Eとも `conversation_type=routine` のみで、`conflict_events=0` だった。

根拠:

- Metrics: `outputs/runs/iss20_no_conflict_axis_llm_metrics.json`
- A raw: `outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm/messages.jsonl`
- E raw: `outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm/messages.jsonl`
- Report: `docs/ISS/reports/2026-05-06_iss_no_conflict_axis_codex_report.md`

解釈: 現行パイプラインでは、形式的な衝突はイベント依存。創発と呼べるのは「喧嘩そのもの」ではなく、routine内に出る小さな不満、距離調整、生活摩擦の語彙である。

### 4. All No Repair Axis: 修復イベントなしでも修復的な言葉は出た

全期間修復イベントなしでも、摩擦後の追跡観測では修復的な会話が出た。

| 指標 | A all no repair | E all no repair | 読み |
|---|---:|---:|---|
| repair events | 0 | 0 | 修復イベントは置いていない |
| followup threads | 48 | 54 | 摩擦後の追跡観測のみ |
| repaired followups | 29 | 33 | 修復的な会話は出る |
| object mentions | 0 | 57 | Eでは物が再接触に入る |

根拠:

- Metrics: `outputs/runs/iss20_all_no_repair_axis_llm_metrics.json`
- A raw: `outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm/messages.jsonl`
- E raw: `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/messages.jsonl`
- Event定義A: `domain_packs/iss_benevolence/data/events_run_a_all_no_repair_20x100.tsv`
- Event定義E: `domain_packs/iss_benevolence/data/events_run_e_all_no_repair_20x100.tsv`
- Report: `docs/ISS/reports/2026-05-06_iss_all_no_repair_axis_codex_report.md`

解釈: 修復的な言葉は、修復イベントだけで発生しているわけではない。ただし「完全自由環境から自然発生した」とは言えない。摩擦後の同じペアを追跡観測する枠があり、その枠の中でLLMが謝罪、確認、回避、距離調整を選んだ。

### 5. Run C: ナッジ撤去後も作法は残るが、文化として完全固定はしない

Run Cは、step 1-50でナッジを置き、step 51-100で物理オブジェクトを撤去した条件である。撤去後も修復会話は出たが、ストレスや孤立は上がる傾向があった。

根拠:

- Raw: `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl`
- Threads: `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/conversation_threads.tsv`
- Manifest: `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/habitat_manifest.json`
- Report: `docs/ISS/reports/2026-05-05_iss_run_c_nudge_removal_claude_sonnet46_report.md`
- Event定義: `domain_packs/iss_benevolence/data/events_run_c.tsv`

解釈: ナッジは撤去後も一部の言葉や作法として残る。しかし物がなくなると、境界や許可の手がかりは弱くなり、ストレスは戻る。これは「文化が完全に根付いた」ではなく、「物理的足場が消えても一部の実践が残った」と読む。

## Qualitative Evidence

### D: rule only は短く閉じる

Raw path:

- `outputs/runs/iss20_rule_only_100_ui_llm/messages.jsonl`
- `outputs/runs/iss20_rule_only_100_ui_llm/conversation_threads.tsv`

Thread: `conv_run_d_20x100_rule_only_step018_REPD02`

> ISS03: 先に個室に戻って静かにしたい。あれ、誘導は少し控えてくれる？  
> ISS09: 了解、作業は終わらせてから5分静穏時間。戻ったら食事と運動を短くして、観測だけ一緒にしよう。  
> ISS03: それなら通る。今の距離でいこう。今日はその流れで、無理のないところまで。

読み: Dは、相手を説得するより、境界、時間、再開条件を短く決める。これはかなり効いている。だから「ナッジだけが効いた」とは言えない。

### E: nudge only は物を介して戻る

Raw path:

- `outputs/runs/iss20_nudge_only_100_ui_llm/messages.jsonl`
- `outputs/runs/iss20_nudge_only_100_ui_llm/conversation_threads.tsv`

Thread: `conv_run_e_20x100_nudge_only_step018_REPE02`

> ISS03: さっきの言い方は刺さった。五分運動→食事前の切替だけ、短く話す形に変える。  
> ISS09: 分かった、重く聞かせた。地球観測が終わったら、話しかけてOKサインの下でだけ短く再開しよう。  
> ISS03: うん、まず個室で静かな時間。戻ってきたら持ち寄り棚で、必要最低限だけ共有する。

読み: Eでは、謝罪や確認だけでなく、OKサインや持ち寄り棚が「再接触してよい場所/条件」として使われている。

### B: package condition は効き方がきれいに出るが、誘導も強い

Raw path:

- `outputs/runs/iss20_nudge_100_ui_llm/messages.jsonl`
- `outputs/runs/iss20_nudge_100_ui_llm/conversation_threads.tsv`

Thread: `conv_run_b_20x100_step092_REPB10`

> ISS08: さっきは助言が重くなったかも。今日は観測前2分だけ、私のペースで受ける形で。  
> ISS09: 刺さる言い方は省く。運動後にOKサインで共有、重くなったら観測後すぐ個室で静かに戻ろう。

読み: Bはデモとして非常にわかりやすい。ナッジの使い方が会話に出る。ただしイベント定義側もナッジ活用を強く書いているため、因果検証にはEや軸削除実験を併用する。

### No Conflict Axis: 喧嘩ではなく、摩擦未満の語彙が出る

Raw path:

- `outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm/messages.jsonl`
- `outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm/messages.jsonl`

Example thread: `conv_run_e_no_conflict_step052_routine`

> ISS01: 昨日、故郷の写真の話が急に切れたままで、不安だったんだ。今日は一枚ずつ見よう。  
> ISS04: そうだったね、ごめん。今日は持ち寄り棚で、無理のない範囲1枚から始めよう。

読み: 形式的なconflictイベントがなくても、小さな不安や再調整は出る。これは「衝突の創発」ではなく、「不穏さの芽」の創発に近い。

### All No Repair Axis: 修復イベントなしでも物が再接触に入る

Raw path:

- `outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm/messages.jsonl`
- `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/messages.jsonl`

Thread: `conv_run_e_all_no_repair_step011_OBSE01`

> ISS07: 今のあたり、持ち寄り棚だけ先に片付ける？前より静かめにやる。  
> ISS02: いいよ、短めに。水分記録だけ見終わったら、また戻る。  
> ISS07: 了解、無理せず。私は小声で進める、5分だけなら一緒にやろう。

読み: 修復イベントを置いていなくても、追跡観測の中で持ち寄り棚が「衝突後に短く戻る場所」として出ている。これはナッジ語彙の文化化の弱い証拠として扱える。

### Run C: 撤去後は物の名前より作法が残る

Raw path:

- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl`
- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/conversation_threads.tsv`

Thread: `conv_run_c_step062_CREP02`

> ISS03: ……次、声かけてくれれば答える。無視はしない。  
> ISS09: ありがとう。そうする。

Thread: `conv_run_c_step078_CREP04`

> ISS00: 記録、二人で声に出して確認するか。  
> ISS08: どっちが読む。

読み: 撤去後は「OKサイン」や「棚」という物名が必ず出るわけではない。代わりに、声をかける、確認する、記録を一緒に読む、といった小さな作法として残る。

## Claim Ladder

強く言えること:

- 現行パイプラインでは、形式的な喧嘩はイベントを置かないと起きにくい。
- 修復イベントなしでも、摩擦後の追跡観測では修復的な会話が出る。
- D rule only は、短く閉じる会話形式としてかなり効く。
- E nudge only は、修復率よりも、物を介した再接触の語彙を増やす。
- B package は、プロダクトデモとして「ナッジの使い方」を最もわかりやすく示す。
- C removal は、物がなくなっても一部の作法が残るが、文化として完全固定したとは言えない。

慎重に言うべきこと:

- 「ナッジが人を善人にした」とは言えない。
- 「喧嘩が完全に自然発生した」とは言えない。
- 「現実の人間でも同じ結果になる」とは言えない。
- Eも修復イベントの中で物の使用を指定しているため、純粋な自由創発ではない。
- A/B/D/Eは履歴サイズやイベント文言に差があるため、完全な統制実験ではなく、探索的シミュレーションとして読む。

## Main Interpretation

この一連の実験の中心仮説は、次のように置くのが安全で強い。

> 善性を育む環境設計は、人を直接「善くする」装置ではない。  
> 高ストレス下で衝突が起きたとき、人が面子、評価、押しつけ感を背負って直接ぶつかり続けなくてよいように、物、場所、合図、短い作法を用意する。  
> その結果、修復は「説得」ではなく、「棚の前で一言」「OKサインの下で短く」「スコアボードを個人責めではなくチーム運用として読む」といった行為に分散される。

## New Hypotheses

1. 物は第三者になる  
   ナッジオブジェクトは、人間同士の直接評価を避ける「第三の参照点」になる。これにより、謝罪や再接触が個人の敗北ではなく、場所の作法になる。

2. ルールは衝突を閉じ、ナッジは戻り口を作る  
   Dは短く閉じる力が強い。Eは物を挟んで戻る力が強い。つまりルールとナッジは競合ではなく、異なる介入階層かもしれない。

3. 創発は3段階に分けるべき  
   形式的な喧嘩の創発、修復的な言葉の創発、物を介した作法の創発は別物。今回強く言えるのは後者2つに近い。

4. 文化化は完全定着ではなく、足場の内面化として起きる  
   Run Cでは、物が消えても作法が残る。ただしストレスや孤立は戻る。これは文化の勝利ではなく、物理的足場の一部内面化と読む。

## Product Framing

GOOD ECHOは、単なるISSデモではなく、高ストレス環境を強制構築して、心理と関係の崩壊に対する環境介入を試すシミュレーション基盤として位置づけられる。

転用先:

- 災害避難所
- 病棟・介護施設
- 寮
- 企業の高圧プロジェクト環境
- 長期滞在施設

プロダクト上の価値は、秩序やルールの強化だけでは解けない「心理と関係の崩壊」を、会話ログ、イベントタイムライン、ナッジ効果、撤去後の文化化として観測できる点にある。

## Evidence Index

Raw conversation logs:

- `outputs/runs/iss20_no_nudge_100_ui_llm/messages.jsonl`
- `outputs/runs/iss20_nudge_100_ui_llm/messages.jsonl`
- `outputs/runs/iss20_rule_only_100_ui_llm/messages.jsonl`
- `outputs/runs/iss20_nudge_only_100_ui_llm/messages.jsonl`
- `outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm/messages.jsonl`
- `outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm/messages.jsonl`
- `outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm/messages.jsonl`
- `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/messages.jsonl`
- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl`

Thread summaries:

- `outputs/runs/iss20_no_nudge_100_ui_llm/conversation_threads.tsv`
- `outputs/runs/iss20_nudge_100_ui_llm/conversation_threads.tsv`
- `outputs/runs/iss20_rule_only_100_ui_llm/conversation_threads.tsv`
- `outputs/runs/iss20_nudge_only_100_ui_llm/conversation_threads.tsv`
- `outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm/conversation_threads.tsv`
- `outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm/conversation_threads.tsv`
- `outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm/conversation_threads.tsv`
- `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/conversation_threads.tsv`
- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/conversation_threads.tsv`

Metrics:

- `outputs/runs/iss20_llm_ab_100step_metrics.json`
- `outputs/runs/iss20_rule_vs_nudge_llm_metrics.json`
- `outputs/runs/iss20_no_conflict_axis_llm_metrics.json`
- `outputs/runs/iss20_all_no_repair_axis_llm_metrics.json`

Event designs:

- `domain_packs/iss_benevolence/data/events_run_a_20x100.tsv`
- `domain_packs/iss_benevolence/data/events_run_b_20x100.tsv`
- `domain_packs/iss_benevolence/data/events_run_d_20x100.tsv`
- `domain_packs/iss_benevolence/data/events_run_e_20x100.tsv`
- `domain_packs/iss_benevolence/data/events_run_a_no_conflict_20x100.tsv`
- `domain_packs/iss_benevolence/data/events_run_e_no_conflict_20x100.tsv`
- `domain_packs/iss_benevolence/data/events_run_a_all_no_repair_20x100.tsv`
- `domain_packs/iss_benevolence/data/events_run_e_all_no_repair_20x100.tsv`
- `domain_packs/iss_benevolence/data/events_run_c.tsv`

Manifests:

- `outputs/runs/iss20_nudge_100_ui_llm/habitat_manifest.json`
- `outputs/runs/iss20_rule_only_100_ui_llm/habitat_manifest.json`
- `outputs/runs/iss20_nudge_only_100_ui_llm/habitat_manifest.json`
- `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/habitat_manifest.json`

