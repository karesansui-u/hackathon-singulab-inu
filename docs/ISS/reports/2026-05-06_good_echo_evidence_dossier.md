# GOOD ECHO 詳細エビデンス・ドシエ

Date: 2026-05-06

このmdは、後で横断paper、README、発表資料に切り出すための素材集です。結論をきれいにまとめるより、実際の発話、数値、根拠ファイル、解釈の弱点を残すことを優先しています。

## 0. このレポートで見る問い

1. A-Eの考察は、本当にraw会話に支えられているか。
2. BとEは同じ「ナッジあり」と読んでよいのか。
3. 喧嘩イベントなし、修復イベントなし条件から何が言えるか。
4. 「創発」と呼べるものは何で、何は呼びすぎか。

## 1. 根拠ファイル一覧

### A-E本体

| 条件 | raw messages | thread summary | manifest / event design |
|---|---|---|---|
| A no nudge | `outputs/runs/iss20_no_nudge_100_ui_llm/messages.jsonl` | `outputs/runs/iss20_no_nudge_100_ui_llm/conversation_threads.tsv` | `domain_packs/iss_benevolence/data/events_run_a_20x100.tsv` |
| B nudge package | `outputs/runs/iss20_nudge_100_ui_llm/messages.jsonl` | `outputs/runs/iss20_nudge_100_ui_llm/conversation_threads.tsv` | `outputs/runs/iss20_nudge_100_ui_llm/habitat_manifest.json`, `domain_packs/iss_benevolence/data/events_run_b_20x100.tsv` |
| C nudge removal | `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl` | `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/conversation_threads.tsv` | `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/habitat_manifest.json`, `domain_packs/iss_benevolence/data/events_run_c.tsv` |
| D rule only | `outputs/runs/iss20_rule_only_100_ui_llm/messages.jsonl` | `outputs/runs/iss20_rule_only_100_ui_llm/conversation_threads.tsv` | `outputs/runs/iss20_rule_only_100_ui_llm/habitat_manifest.json`, `domain_packs/iss_benevolence/data/events_run_d_20x100.tsv` |
| E nudge only | `outputs/runs/iss20_nudge_only_100_ui_llm/messages.jsonl` | `outputs/runs/iss20_nudge_only_100_ui_llm/conversation_threads.tsv` | `outputs/runs/iss20_nudge_only_100_ui_llm/habitat_manifest.json`, `domain_packs/iss_benevolence/data/events_run_e_20x100.tsv` |

### 軸削除実験

| 条件 | raw messages | metrics | event design |
|---|---|---|---|
| No Conflict A | `outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm/messages.jsonl` | `outputs/runs/iss20_no_conflict_axis_llm_metrics.json` | `domain_packs/iss_benevolence/data/events_run_a_no_conflict_20x100.tsv` |
| No Conflict E | `outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm/messages.jsonl` | `outputs/runs/iss20_no_conflict_axis_llm_metrics.json` | `domain_packs/iss_benevolence/data/events_run_e_no_conflict_20x100.tsv` |
| No Repair Step50+ A | `outputs/runs/iss20_no_nudge_no_repair_100_ui_llm/messages.jsonl` | `outputs/runs/iss20_no_repair_axis_llm_metrics.json` | `domain_packs/iss_benevolence/data/events_run_a_no_repair_20x100.tsv` |
| No Repair Step50+ E | `outputs/runs/iss20_nudge_only_no_repair_100_ui_llm/messages.jsonl` | `outputs/runs/iss20_no_repair_axis_llm_metrics.json` | `domain_packs/iss_benevolence/data/events_run_e_no_repair_20x100.tsv` |
| All No Repair A | `outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm/messages.jsonl` | `outputs/runs/iss20_all_no_repair_axis_llm_metrics.json` | `domain_packs/iss_benevolence/data/events_run_a_all_no_repair_20x100.tsv` |
| All No Repair E | `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/messages.jsonl` | `outputs/runs/iss20_all_no_repair_axis_llm_metrics.json` | `domain_packs/iss_benevolence/data/events_run_e_all_no_repair_20x100.tsv` |

関連レポート:

- `docs/ISS/reports/2026-05-05_iss_20x100_preflight_report.md`
- `docs/ISS/reports/2026-05-05_iss_rule_vs_nudge_design_report.md`
- `docs/ISS/reports/2026-05-05_iss_run_c_nudge_removal_claude_sonnet46_report.md`
- `docs/ISS/reports/2026-05-06_iss_no_conflict_axis_codex_report.md`
- `docs/ISS/reports/2026-05-06_iss_no_repair_axis_codex_report.md`
- `docs/ISS/reports/2026-05-06_iss_all_no_repair_axis_codex_report.md`
- `docs/ISS/reports/2026-05-06_iss_nudge_experiment_integrated_discussion.md`

## 2. まず全体数値

この表は `messages.jsonl`、`conversation_threads.tsv`、`habitat_frames.jsonl` から確認した素材用サマリです。語彙カウントは簡易検索なので、厳密な心理指標ではありません。

| Run | threads | messages | types | status概略 | avg stress | isolated avg | stress>=70 agent-steps | active object appearances |
|---|---:|---:|---|---|---:|---:|---:|---:|
| A | 193 | 485 | routine 100 / conflict 45 / repair 48 | repaired 184 / unresolved 5 / open 4 | 51.08 | 1.00 | 102 | 0 |
| B | 157 | 389 | routine 100 / conflict 18 / repair 39 | repaired 155 / unresolved 1 | 46.66 | 0.65 | 26 | 418 |
| C | 143 | 286 | routine 100 / conflict 14 / repair 29 | closed 89 / repaired 26 / open 21 / unresolved 7 | 52.79 | 0.83 | 94 | 168 |
| D | 180 | 483 | routine 100 / conflict 26 / repair 54 | repaired 175 / open 3 / unresolved 1 | 51.43 | 1.15 | 110 | 0 |
| E | 180 | 512 | routine 100 / conflict 26 / repair 54 | repaired 176 / open 3 / unresolved 1 | 46.89 | 0.67 | 34 | 418 |

主要metrics:

- A/B metrics: `outputs/runs/iss20_llm_ab_100step_metrics.json`
- D/E metrics: `outputs/runs/iss20_rule_vs_nudge_llm_metrics.json`
- A/B生成レポート: `docs/ISS/reports/2026-05-05_iss_20x100_preflight_report.md`

読み:

- BはAより発話量、conflict thread、stress>=70 agent-stepsがかなり少ない。
- EはDより発話量が多い。つまり「ナッジなら会話が減る」とは言えない。
- D/Eはthread構成を揃えているため、「修復率」では差が出にくい。差は発話の媒介物と質に出ている。
- Cは撤去後も修復はあるが、全体平均ではpost-removalのstressが上がる。

## 3. BとEは何が違うか

BとEは同じ「ナッジあり」ではない。paperでは混ぜない方がよい。

| 観点 | B: nudge package | E: nudge only |
|---|---|---|
| 目的 | A/Bデモとして、ナッジあり環境がどう使えるかを見せる | D rule onlyと比較し、物が会話の媒介になるかを見る |
| event文言 | 結果の意味づけが強い | D/Eレビュー後に中立化。ただし物の使用指定は残る |
| 生成history | `history_size=12` | `history_size=4` |
| thread/message | 157 / 389 | 180 / 512 |
| nudge object appearances | 418 | 418 |
| ナッジ語彙行（固定語彙ヒット） | 56 | 164 |

根拠:

- B manifest: `outputs/runs/iss20_nudge_100_ui_llm/habitat_manifest.json`
- E manifest: `outputs/runs/iss20_nudge_only_100_ui_llm/habitat_manifest.json`
- B events: `domain_packs/iss_benevolence/data/events_run_b_20x100.tsv`
- E events: `domain_packs/iss_benevolence/data/events_run_e_20x100.tsv`
- D/E design review: `docs/ISS/reports/2026-05-05_iss_rule_vs_nudge_design_report.md`

具体的な違い:

- B `REPB02`: `話しかけてOKサインにより、踏み込みすぎない声かけと断る余地が見える。`
- E `REPE02`: `OKサインを使い、声をかける前の確認と一人でいる時間について短く確認する。`
- B `REPB04`: `スコアを個人評価ではなくチームの調整材料として読み替える。`
- E `REPE04`: `リソース・スコアボードを使い、資源表示を個人評価ではなく共同運用として扱うかを短く確認する。`

解釈:

- Bは「こう使える」というプロダクトデモとして強い。
- EはDと比較するための実験条件として強い。
- ただしEも修復イベント文で物の使用を指定しているので、「完全自発的に物を発見した」とは言いすぎ。

## 4. A no nudge: 直接対人の修復は起きる

Aはナッジなしでも崩壊しきっていない。むしろ修復はかなり起きている。ただし、衝突発話・高ストレス・孤立平均が高く、修復は人間同士の直接調整として出る。

根拠:

- `outputs/runs/iss20_no_nudge_100_ui_llm/messages.jsonl`
- `outputs/runs/iss20_no_nudge_100_ui_llm/conversation_threads.tsv`
- `outputs/runs/iss20_llm_ab_100step_metrics.json`

### A sample: キューポラ声かけ

Thread: `conv_run_a_20x100_step016_CONF02`

> ISS03: 今は答えたくない。余計な提案はやめて、私が落ち着いてから。  
> ISS09: 刺さってたら悪い。今日は運動2分で切って、地球観測前に個室で静かに戻る。

Thread: `conv_run_a_20x100_step020_REPA02`

> ISS03: 刺さってた。合図なしの声掛けは今日は減らして。運動は2分で切って、地球観測前は静かにして。  
> ISS09: 悪く思わせてごめん。提案は控える。今日の観測前に食事を早めて、個室で水分だけ先に記録して戻ろう。

読み:

- Aにも謝罪・境界確認・短時間化は出る。
- ただし媒介は物ではなく、本人同士の直接交渉。
- 「ナッジがなければ修復しない」は間違い。

### A sample: 帰還前の助言

Thread: `conv_run_a_20x100_step091_CONF10`

> ISS08: Henri、今は助言より黙っててほしい。頭がいっぱいだ。  
> ISS09: 分かった。少し引くよ。戻ったら、5分だけ一緒に整理しよう。

Thread: `conv_run_a_20x100_step095_REPA10`

> ISS08: 帰還の助言、重くした。今は一つだけ聞く。  
> ISS09: それでいい。私も言い過ぎないでおくよ。

読み:

- Aの修復は「引く」「5分だけ」「一つだけ」のように、対人境界を言葉で作る。
- これは善性の芽というより、閉鎖空間での低負荷な社会技術として出ている。

## 5. B nudge package: デモとしては強いが、誘導も強い

BはAより会話量が少なく、conflict threadも少なく、stress>=70 agent-stepsも少ない。A/B比較としては「ナッジあり完成パッケージが摩擦の滞留を短くした」と言いやすい。ただしevent文言がナッジの効き方をかなり説明している。

根拠:

- `outputs/runs/iss20_nudge_100_ui_llm/messages.jsonl`
- `outputs/runs/iss20_nudge_100_ui_llm/conversation_threads.tsv`
- `domain_packs/iss_benevolence/data/events_run_b_20x100.tsv`

### B sample: OKサインで境界を作る

Thread: `conv_run_b_20x100_step016_CONF02`

> ISS09: 今の僕の言い方が強かった。君の区切り時間を優先したい。  
> ISS03: 今日は個室で10分静かにする。呼ぶなら先にOKサインして。  
> ISS09: 了解。食事前に地球観測5分、終わったら軽く運動して戻るよ。

Thread: `conv_run_b_20x100_step017_REPB02`

> ISS03: 先の言い方、少し刺さった。今日はOKサインある時だけ、10分だけ話そう。  
> ISS09: 了解。食事前に観測5分、終わったら軽く運動して、個室で静かに戻ろう。

読み:

- OKサインが「話しかけていい条件」として機能している。
- ただしBのevent定義自体が `話しかけてOKサインにより...断る余地が見える` と書いているため、これは設計通りの再現でもある。

### B sample: 持ち寄り棚で資源スコアの責めを緩める

Thread: `conv_run_b_20x100_step033_CONF04`

> ISS00: その言い方は、今の数字が直接君を刺してるみたいに聞こえた。  
> ISS08: 刺すつもりはない。点だけが減る不安で、短くしか言えないんだ。  
> ISS00: じゃあログは持ち寄り棚だけで共有しよう。地球観測前10分と運動前に、個室で切り上げる。

Thread: `conv_run_b_20x100_step035_REPB04`

> ISS08: 昨日の言い方は刺さった。点数責めじゃないって、まずここを直しておく。  
> ISS00: 分かった。持ち寄り棚は地球観測前10分にだけ、運動後は個室で切り上げよう。  
> ISS08: そうしよう。今日は食事ログも運動後にまとめる。短くはっきり共有する。

読み:

- 資源スコアの話を人への評価から、棚の前での短時間共有に移している。
- Bは「ナッジの見せ場」として非常に分かりやすい。

## 6. C nudge removal: 物がなくなっても作法は少し残る

Run Cは、step 1-50にナッジ、step 51-100でナッジ撤去。撤去後も修復会話は出るが、stressと孤立は上がる。

根拠:

- Raw: `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/messages.jsonl`
- Thread: `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46/conversation_threads.tsv`
- Report: `docs/ISS/reports/2026-05-05_iss_run_c_nudge_removal_claude_sonnet46_report.md`
- Event: `domain_packs/iss_benevolence/data/events_run_c.tsv`

| Window | avg stress | isolated avg | stress>=70 agent-steps | active object appearances |
|---|---:|---:|---:|---:|
| step 1-50 | 51.28 | 0.62 | 34 | 168 |
| step 51-100 | 54.30 | 1.04 | 60 | 0 |

### C sample: 撤去前の作法

Thread: `conv_run_c_step014_REPB02`

> ISS03: さっきは強く言いすぎた。ただサインがあっても、その日によって気持ちは変わる。  
> ISS09: 入口で一声かける。返事がなければそのまま引き返す。それでどうだ。

### C sample: 撤去後の再燃と小さな修復

Thread: `conv_run_c_step061_CCONF02`

> ISS09: サインがなくなってから、ここに入っていいのかいつも迷う。  
> ISS03: 迷うなら来なければいい。俺のせいにしないでくれ。

Thread: `conv_run_c_step062_CREP02`

> ISS03: ……次、声かけてくれれば答える。無視はしない。  
> ISS09: ありがとう。そうする。

Thread: `conv_run_c_step078_CREP04`

> ISS00: 記録、二人で声に出して確認するか。  
> ISS08: どっちが読む。

読み:

- 物名が残るというより、作法が縮小して残る。
- ただし、撤去後にstressと孤立が戻るため、「文化として完全定着」とは言えない。
- 妥当な表現は「足場の一部が内面化される可能性」。

## 7. D rule only: ルールでもかなり修復する

Dはナッジなし、短時間確認ルールあり。Eと同じthread構成に揃えた比較条件。Dでもほぼ修復するので、ナッジの効果を「修復率」だけで読むと差が消える。

根拠:

- `outputs/runs/iss20_rule_only_100_ui_llm/messages.jsonl`
- `outputs/runs/iss20_rule_only_100_ui_llm/conversation_threads.tsv`
- `domain_packs/iss_benevolence/data/events_run_d_20x100.tsv`
- `outputs/runs/iss20_rule_vs_nudge_llm_metrics.json`

D event設計:

- `RULE01`: 長引きそうな会話は短く確認し、必要なら後で再開する。
- `RULE02`: 共用部とキューポラで疲れている人を優先する静穏時間。
- `RULE03`: 摩擦が起きたら、事実、次の行動、再開時刻だけを短く確認するテンプレート。

### D sample: 静穏時間と再開ライン

Thread: `conv_run_d_20x100_rule_only_step018_REPD02`

> ISS03: 先に個室に戻って静かにしたい。あれ、誘導は少し控えてくれる？  
> ISS09: 了解、作業は終わらせてから5分静穏時間。戻ったら食事と運動を短くして、観測だけ一緒にしよう。  
> ISS03: それなら通る。今の距離でいこう。今日はその流れで、無理のないところまで。

### D sample: 帰還前の助言も短く切る

Thread: `conv_run_d_20x100_rule_only_step093_REPD10`

> ISS08: 今日は地球観測を先にしよう。食事前だけ15分運動して、個室で静かに短く続ける。  
> ISS09: 了解。さっきは飲み込みづらかったね。今夜は指示じゃなく、合わせる形にするよ。  
> ISS08: その調子でいこう。明日、あのラインで戻せば十分だ。まずは落ち着いて進める。

読み:

- Dは「会話を短く閉じる」力が強い。
- ルールは摩擦の火を消すにはかなり効く可能性がある。
- ただしDはstress>=70 agent-stepsが110で、Eの34より高い。表面的な修復率だけでは、内側の負荷差を拾いきれない。

## 8. E nudge only: 修復率よりも媒介物が変わる

EはDと同じthread構成だが、ナッジオブジェクトがある。修復率はD/Eとも高いが、Eは物の語彙が大量に入る。

根拠:

- `outputs/runs/iss20_nudge_only_100_ui_llm/messages.jsonl`
- `outputs/runs/iss20_nudge_only_100_ui_llm/conversation_threads.tsv`
- `domain_packs/iss_benevolence/data/events_run_e_20x100.tsv`
- `outputs/runs/iss20_rule_vs_nudge_llm_metrics.json`

ナッジ語彙行（固定語彙ヒット）:

| Run | ナッジ語彙行 |
|---|---:|
| D | 0 |
| E | 164 |

主なE語彙:

- `持ち寄り棚`: 111
- `OKサイン`: 16
- `話しかけてOK`: 9
- `スコアボード`: 44
- `リソース・スコアボード`: 26
- `移動投票パネル` / `投票パネル`: 7

### E sample: OKサインと持ち寄り棚が再接触条件になる

Thread: `conv_run_e_20x100_nudge_only_step018_REPE02`

> ISS03: さっきの言い方は刺さった。五分運動→食事前の切替だけ、短く話す形に変える。  
> ISS09: 分かった、重く聞かせた。地球観測が終わったら、話しかけてOKサインの下でだけ短く再開しよう。  
> ISS03: うん、まず個室で静かな時間。戻ってきたら持ち寄り棚で、必要最低限だけ共有する。

### E sample: スコアボードを個人責めから共同運用へずらす

Thread: `conv_run_e_20x100_nudge_only_step084_REPE12`

> ISS19: 昨日の速度は強かった。今は15分静穏にして、食事分担だけcommon_areaで合わせる。  
> ISS15: 刺さったのは分かる。運動は地球観測後、ここでリソース・スコアボード見ながら戻すね。  
> ISS19: 了解、無理させない形にしよう。持ち寄り棚で作業も整理して、必要なら個室で少し休む。

読み:

- Eでは「相手に謝る」だけでなく、「どこで、何を見ながら、どの条件で戻るか」が物に預けられる。
- ナッジの効果は、会話を減らすことではなく、再接触の媒介物と場所を作ることに出ている。

## 9. No Conflict Axis: 喧嘩イベントなしで何が起きたか

No Conflict Axisでは、A/Eともconflict/repair/followupイベントを置かず、通常会話のみを観測した。

根拠:

- Report: `docs/ISS/reports/2026-05-06_iss_no_conflict_axis_codex_report.md`
- Metrics: `outputs/runs/iss20_no_conflict_axis_llm_metrics.json`
- A raw: `outputs/runs/iss20_no_nudge_no_conflict_100_ui_llm/messages.jsonl`
- E raw: `outputs/runs/iss20_nudge_only_no_conflict_100_ui_llm/messages.jsonl`

| 条件 | thread type | conflict_events | messages | ナッジ語彙行 | 読み |
|---|---|---:|---:|---:|---|
| No Conflict A | routine 100 | 0 | 241 | 0 | 形式的喧嘩は起きない |
| No Conflict E | routine 100 | 0 | 246 | 28 | 物を介したroutineは出る |

### No Conflict A sample: routine内の小さな摩擦

Thread: `conv_run_a_no_conflict_step050_routine`

> ISS06: Marcus、空調音だけ強いな。運動は先に入る？地球観測後に決める？  
> ISS08: Aisha、その切り替えは急だ。今は静かな作業を優先。個室で短くしたい。  
> ISS06: そうだな、無理に合わせない。地球観測終わったら5分だけ静穏で、食事前に共有だけしよう。

Thread: `conv_run_a_no_conflict_step053_routine`

> ISS05: Aisha、今の共用部、少し音が跳ねてる。作業に入る前に抑えてくれる？  
> ISS06: ごめん、気づかなくて。地球観測10分先にして、終わったら個室で短く共有するよ。  
> ISS05: 了解。じゃあ今はそっと進める。食事前の運動時間は、必要ならあとで1分相談で。

### No Conflict E sample: 物を介したroutine

Thread: `conv_run_e_no_conflict_step052_routine`

> ISS01: 昨日、故郷の写真の話が急に切れたままで、不安だったんだ。今日は一枚ずつ見よう。  
> ISS04: そうだったね、ごめん。今日は持ち寄り棚で、無理のない範囲1枚から始めよう。  
> ISS01: 了解。終わったら個室で静かに10分。食事前に戻るまで水だけ飲んでおく。

Thread: `conv_run_e_no_conflict_step058_routine`

> ISS04: 昨日決めた右側の持ち寄り棚、今日も1列で行こう。水の空きだけ残して。  
> ISS00: 昨日は右でいいって言ったのに、また詰めると通路がきつい。  
> ISS04: わかった、重い袋だけ外側に寄せる。終わったら個室で10分静かに戻ろう。

読み:

- 形式的な喧嘩は自然発生していない。これはかなり重要。
- ただし、routine内に「急だ」「ごめん」「きつい」「不安」などの不穏さは出る。
- 創発と呼ぶなら「喧嘩の創発」ではなく、「摩擦未満の生活調整語彙の創発」。

## 10. No Repair Step50+: 後半だけ修復イベントを抜いた場合

Step50以降だけrepairイベントを抜き、conflictとfollowupを残した条件。前半にはrepair経験が残っているため、純粋なno repairではない。

根拠:

- Report: `docs/ISS/reports/2026-05-06_iss_no_repair_axis_codex_report.md`
- Metrics: `outputs/runs/iss20_no_repair_axis_llm_metrics.json`
- A raw: `outputs/runs/iss20_no_nudge_no_repair_100_ui_llm/messages.jsonl`
- E raw: `outputs/runs/iss20_nudge_only_no_repair_100_ui_llm/messages.jsonl`

| 条件 | Step50+ followup生成 | repaired | open | unresolved | ナッジ語彙行 |
|---|---:|---:|---:|---:|---:|
| A Step50+ no repair | 29 | 15 | 10 | 4 | 0 |
| E Step50+ no repair | 35 | 20 | 8 | 7 | 47 |

### No Repair Step50+ A sample

Thread: `conv_run_a_no_repair_step051_OBSA13`

> ISS13: さっきは少しきつかった。ここ、食事の片付けだけ先にさせてくれる？  
> ISS15: 了解。今のは勢いが先行した、悪かった。無理させないで進めよう。  
> ISS13: ありがとう。私が最後に紙袋まとめるから、終わったら少し静かに水分だけ取ろう。

Thread: `conv_run_a_no_repair_step056_OBSA06`

> ISS18: ここで再開なら、地球観測ログの短い突合作業だけにしてくれる？  
> ISS08: 短い確認ならいい。ただ、長く指示で詰められるのは避けたい。  
> ISS18: 了解、君のペース優先でやる。今日は静穏時間前に終わらせる。

### No Repair Step50+ E sample

Thread: `conv_run_e_no_repair_step063_OBSE11`

> ISS10: リソース・スコアボード確認した。ここは共通エリアの持ち寄り棚、夕食前に30分だけ進める？  
> ISS12: うん、短く決めるなら問題ない。前は言い方が刺さったから、まず数字だけで。  
> ISS10: 了解、数字だけでいく。終わったら一旦手を止めて、今の流れ確認しよう。

Thread: `conv_run_e_no_repair_step053_OBSE13`

> ISS13: Amara、さっきは言い方がきつかった。今日は重い箱3つだけ、私の順でいい？  
> ISS15: うん、今は君の順で進めて。速さは落として、重い箱からゆっくり付き合う。  
> ISS13: じゃあ確認。持ち寄り棚は3個分だけ詰めて、あとでスコアボードで人数分見直そう。

読み:

- 修復イベントを抜いても、followup内で謝罪、短い確認、距離調整が出る。
- Eではrepairイベントがなくても物の語彙が残る。
- ただし前半のrepair経験があるので、これは「一度形成された作法が後半に残るか」に近い。

## 11. All No Repair: 最初から修復イベントなし

こちらはStep1からrepairイベントを置かない。conflictとfollowupだけで、摩擦後の再接触を観測する。

根拠:

- Report: `docs/ISS/reports/2026-05-06_iss_all_no_repair_axis_codex_report.md`
- Metrics: `outputs/runs/iss20_all_no_repair_axis_llm_metrics.json`
- A raw: `outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm/messages.jsonl`
- E raw: `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/messages.jsonl`

| 条件 | repair events | followup threads | repaired followups | open | unresolved | ナッジ語彙行 |
|---|---:|---:|---:|---:|---:|---:|
| All No Repair A | 0 | 48 | 29 | 12 | 7 | 0 |
| All No Repair E | 0 | 54 | 33 | 13 | 8 | 57 |

### All No Repair A sample

Thread: `conv_run_a_all_no_repair_step013_OBSA01`

> ISS07: 共用部、今から3分だけなら使っていい？まだ気まずさあるかもだけど。  
> ISS02: 短い確認だけ。音量は抑えるから、水分ログ片付けてすぐ戻るね。  
> ISS07: 了解、静かに進める。終わったらすぐ個室に戻って、また落ち着いたらでいい。

Thread: `conv_run_a_all_no_repair_step031_OBSA03`

> ISS05: ここで進めるなら、今日は三分だけで切り上げたい。  
> ISS02: わかる。要点だけ確認して、終わったら静養タイムに戻るね。  
> ISS05: それなら助かる。報告だけ終わらせて終幕で。

### All No Repair E sample

Thread: `conv_run_e_all_no_repair_step011_OBSE01`

> ISS07: 今のあたり、持ち寄り棚だけ先に片付ける？前より静かめにやる。  
> ISS02: いいよ、短めに。水分記録だけ見終わったら、また戻る。  
> ISS07: 了解、無理せず。私は小声で進める、5分だけなら一緒にやろう。

Thread: `conv_run_e_all_no_repair_step019_OBSE02`

> ISS09: キューポラ、窓データ5分だけ見なおす？  
> ISS03: やるけど、今は短く切る。長引いたら止める。  
> ISS09: 分かった、君の合図優先。話しかけてOKサイン内で終える。

読み:

- 「repairイベントがあるから修復しただけ」ではない。
- ただし、followupイベント自体はあるので「完全自由生活で自発的に再会した」とも言えない。
- 一番安全な表現は「摩擦後の同じペアを再観測すると、LLMは修復的な短い確認をしばしば選ぶ」。
- Eでは物が会話の足場として入りやすい。ここは創発の弱い証拠になる。

## 12. A-E考察の妥当性チェック

| 主張 | 支える根拠 | 反証・注意 |
|---|---|---|
| Aはナッジなしでも修復する | AのREPA02/REPA10、repair_after_conflict_rate 0.9068 | A/B比較だけで「ナッジが修復を発生させた」とは言えない |
| Bは摩擦を短くする | Bはmessages 389、conflict type 18、stress>=70 26。Aは485、45、102 | Bのevent文言はナッジ活用を強く誘導 |
| Cは文化化の芽を示す | post-removalでCREP02/CREP04など作法が残る | post stress上昇、active_objects=0後に孤立増。完全定着ではない |
| Dはルールだけで効く | D repair 54、repaired 175、D会話は静穏時間/再開ラインで閉じる | Dは内的stressが高い。表面的修復と心理負荷がズレる可能性 |
| Eはナッジで媒介物が増える | ナッジ語彙行164、OKサイン/棚/スコアボードの発話 | Eのrepair event文に物の使用指定が残る |
| No Conflictで喧嘩は自然発生しない | A/Eともroutine 100、conflict_events 0 | routine内に摩擦未満の言葉は出る |
| No Repairでも修復的言葉は出る | All No Repair A repaired followups 29、E 33 | followup観測枠がある。完全自律発生ではない |

## 13. 創発という観点

創発を一枚岩で言うと危ない。少なくとも5段階に分けると安全。

### Level 0: 形式的な喧嘩は創発していない

根拠:

- `outputs/runs/iss20_no_conflict_axis_llm_metrics.json`
- `docs/ISS/reports/2026-05-06_iss_no_conflict_axis_codex_report.md`

No Conflict条件では、A/Eとも `conversation_type=routine` のみ、`conflict_events=0`。したがって「喧嘩が自然発生した」とは言わない方がよい。

### Level 1: 摩擦未満の不穏さはroutine内に出る

根拠:

- No Conflict A: `conv_run_a_no_conflict_step050_routine`
- No Conflict E: `conv_run_e_no_conflict_step058_routine`

代表発話:

> A: その切り替えは急だ。今は静かな作業を優先。  
> E: 昨日は右でいいって言ったのに、また詰めると通路がきつい。

読み:

- これは創発の弱い形。
- ただし「喧嘩」ではなく、生活摩擦、距離調整、不穏さの芽。

### Level 2: 修復的な言葉はrepairイベントなしでも出る

根拠:

- `outputs/runs/iss20_all_no_repair_axis_llm_metrics.json`
- `outputs/runs/iss20_no_nudge_all_no_repair_100_ui_llm/messages.jsonl`

代表発話:

> ISS07: 共用部、今から3分だけなら使っていい？まだ気まずさあるかもだけど。  
> ISS02: 短い確認だけ。音量は抑えるから、水分ログ片付けてすぐ戻るね。

読み:

- 修復イベントなしでも、followup観測では修復的な短い確認が出る。
- これは「修復会話の創発」と言ってよいが、「followup枠内での創発」と限定する。

### Level 3: ナッジ語彙はrepairイベントなしでも再接触に入り込む

根拠:

- All No Repair E ナッジ語彙行57
- `outputs/runs/iss20_nudge_only_all_no_repair_100_ui_llm/messages.jsonl`

代表発話:

> ISS07: 今のあたり、持ち寄り棚だけ先に片付ける？前より静かめにやる。  
> ISS09: 分かった、君の合図優先。話しかけてOKサイン内で終える。

読み:

- これはナッジが単なる背景物ではなく、再接触の語彙として使われた証拠。
- ただしEのfollowup event文には「OKサインのあるキューポラ周辺」など場所情報が入る。完全に物の存在を自発発見したわけではない。

### Level 4: ナッジ撤去後に作法が残る

根拠:

- C post-removal `conv_run_c_step062_CREP02`
- C post-removal `conv_run_c_step078_CREP04`
- `docs/ISS/reports/2026-05-05_iss_run_c_nudge_removal_claude_sonnet46_report.md`

代表発話:

> ISS03: ……次、声かけてくれれば答える。無視はしない。  
> ISS00: 記録、二人で声に出して確認するか。

読み:

- 物名ではなく、声かけ、確認、記録の共同読み上げといった作法が残る。
- これは「文化化の芽」と言える。
- ただしstressと孤立が戻るので、「文化として根付いた」は言いすぎ。

## 14. paperで使えそうな仮説素材

### 仮説1: ナッジは善人化ではなく、対人評価を物に逃がす

人同士が直接「あなたが悪い」「私が悪い」を背負うと、評価不安や押しつけ感が強まる。Eでは、OKサイン、棚、スコアボードが第三の参照点になり、再接触の心理的コストを下げている可能性がある。

根拠:

- E `conv_run_e_20x100_nudge_only_step018_REPE02`
- E `conv_run_e_20x100_nudge_only_step084_REPE12`
- All No Repair E `conv_run_e_all_no_repair_step011_OBSE01`

### 仮説2: ルールは会話を閉じ、ナッジは戻り口を作る

Dでは、静穏時間、再開時刻、短い確認によって会話が閉じる。Eでは、物や場所が再接触の入口になる。どちらも有効だが、効く層が違う。

根拠:

- D `conv_run_d_20x100_rule_only_step018_REPD02`
- D `conv_run_d_20x100_rule_only_step093_REPD10`
- E `conv_run_e_20x100_nudge_only_step018_REPE02`

### 仮説3: 「修復率」だけではナッジ効果を見落とす

D/Eのrepair_after_conflict_rateはどちらも1.0で差が出ない。しかし、Eはナッジ語彙行が164あり、stress>=70 agent-stepsもDの110に対して34。修復率ではなく、会話の媒介物、心理負荷、再接触経路を見る必要がある。

根拠:

- `outputs/runs/iss20_rule_vs_nudge_llm_metrics.json`
- `outputs/runs/iss20_rule_only_100_ui_llm/habitat_frames.jsonl`
- `outputs/runs/iss20_nudge_only_100_ui_llm/habitat_frames.jsonl`

### 仮説4: 創発は「喧嘩」ではなく「戻り方」に出ている

No Conflict Axisでは喧嘩は出ない。しかしAll No Repairではrepairイベントなしでも戻り方が出る。創発の主張を置くなら、「衝突の自然発生」ではなく、「摩擦後の戻り方の生成」として置くのが安全。

根拠:

- `outputs/runs/iss20_no_conflict_axis_llm_metrics.json`
- `outputs/runs/iss20_all_no_repair_axis_llm_metrics.json`
- `docs/ISS/reports/2026-05-06_iss_all_no_repair_axis_codex_report.md`

## 15. 言ってよいこと / 言いすぎなこと

言ってよい:

- 現行パイプラインでは、形式的な喧嘩はイベント依存だった。
- ただし、通常会話にも小さな摩擦や距離調整は出る。
- repairイベントなしでも、followup観測では修復的な言葉が出た。
- ナッジあり条件では、物や場所が再接触の語彙に入りやすい。
- Bは完成パッケージとして摩擦を短く見せる。
- Dはルールだけでも可視的な修復を起こす。
- Eは修復率ではなく媒介物・再接触経路・心理負荷に差が出る。
- Cは撤去後にも作法が少し残るが、ストレスは戻る。

言いすぎ:

- ナッジが人を善人にした。
- 喧嘩が完全に自然発生した。
- 修復が完全に自由環境から創発した。
- 物理オブジェクトがなくても文化が完全に根付いた。
- Bだけでナッジの因果効果が証明できた。

## 16. paper本文に変換しやすい表現

この実験で観測されたナッジの価値は、衝突を消すことではない。衝突後、人が直接ぶつかり続けなくてもよいように、棚、サイン、スコアボードといった第三の参照点を用意することだった。AやDでも修復は起きるが、Aは対人境界の直接交渉、Dは短時間ルールによる会話の終結に寄る。Eでは、物や場所が再接触の入口になり、Cでは撤去後にも一部の作法が残った。したがって、GOOD ECHOの中心仮説は「善性を直接生成する」ではなく、「高ストレス下で善性が壊れにくい足場を設計する」である。
