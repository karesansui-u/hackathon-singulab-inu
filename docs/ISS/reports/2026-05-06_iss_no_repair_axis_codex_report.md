# ISS 後半修復イベントなし軸 Codexレポート

## Summary

Step50以降の `repair` イベントを置かない追加軸を、A/Eの2条件で生成した。

- A 後半修復イベントなし: ナッジなし。Step50以降は `conflict` と `followup` のみ。
- E 後半修復イベントなし: Eと同じナッジオブジェクトあり。Step50以降は `conflict` と `followup` のみ。
- Codex生成対象: Step50-100 の `followup` スレッドのみ。
- `repair` イベントはどちらもStep50以降ゼロ。

## Outputs

| 条件 | output |
|---|---|
| A 後半修復イベントなし state | `outputs/runs/iss20_no_nudge_no_repair_100_state` |
| A 後半修復イベントなし UI | `outputs/runs/iss20_no_nudge_no_repair_100_ui` |
| A 後半修復イベントなし LLM | `outputs/runs/iss20_no_nudge_no_repair_100_ui_llm` |
| E 後半修復イベントなし state | `outputs/runs/iss20_nudge_only_no_repair_100_state` |
| E 後半修復イベントなし UI | `outputs/runs/iss20_nudge_only_no_repair_100_ui` |
| E 後半修復イベントなし LLM | `outputs/runs/iss20_nudge_only_no_repair_100_ui_llm` |
| metrics | `outputs/runs/iss20_no_repair_axis_llm_metrics.json` |

## Generation Result

| 条件 | Codex生成followup | 失敗 |
|---|---:|---:|
| A 後半修復イベントなし | 29 | 0 |
| E 後半修復イベントなし | 35 | 0 |

Step50以降のthread内訳:

| 条件 | routine | conflict | followup | repair |
|---|---:|---:|---:|---:|
| A 後半修復イベントなし | 51 | 26 | 29 | 0 |
| E 後半修復イベントなし | 51 | 15 | 35 | 0 |

LLM生成followupのstatus:

| 条件 | repaired | open | unresolved |
|---|---:|---:|---:|
| A 後半修復イベントなし | 15 | 10 | 4 |
| E 後半修復イベントなし | 20 | 8 | 7 |

## Metrics

Step50-100のみを集計。

| 指標 | A 後半修復イベントなし | E 後半修復イベントなし |
|---|---:|---:|
| total_messages | 238 | 233 |
| llm_message_count | 84 | 101 |
| unique_interaction_pairs | 42 | 42 |
| repair_after_conflict_rate | 0.7571 | 0.9111 |
| conflict_events | 70 | 45 |
| isolated_agents | 0 | 0 |

注: conflict/routine は scripted が混在しているため、このKPIは部分的にproxyを含む。解釈では、Codex生成したfollowup部分を中心に見る。

## Initial Reading

修復イベントを置かなくても、followup会話の中で謝罪、短い確認、距離の取り直しが出た。

特にE 後半修復イベントなしでは、followupのLLM発話101件中42件で、持ち寄り棚、OKサイン、リソース・スコアボードなどのナッジオブジェクトが言及された。A 後半修復イベントなしでは同じナッジ語彙は0件だった。

このため、現時点では次の読みができる。

- 修復の発生自体は、repairイベントなしでもLLMが生成しうる。
- ナッジあり条件では、修復イベントを置かなくても、物や合図が再接触の言葉に入りやすい。
- ただしLLM followupのみを生成した部分実験なので、最終比較では全thread生成版またはfollowup専用指標で再集計する。

## Caveat: prior repair exposure

この追加軸は「完全に修復経験のない世界」ではない。Step50以前には、A/Eともに既存のrepairイベントが残っている。

- A 後半修復イベントなし: Step50以前に `REPA01`-`REPA05` がある。
- E 後半修復イベントなし: Step50以前に `REPE01`-`REPE05` がある。
- Step50以降の `repair` イベントはどちらも0件。

同じペアに限ると、Step50以降のfollowupペアがStep50以前にrepairしていた例はほぼない。一方で、参加者個人が別ペアでrepair会話を経験していたり、同じfollowup期間の前のstepでrepairっぽい会話が出て、それが次stepの履歴として入る場合がある。

したがって、この結果は「初見のエージェントがナッジを完全に自発発見した」と読むより、

> すでに前半で閉鎖環境の修復作法を経験した後、後半で明示的なrepairイベントを抜いても、ナッジあり条件では物や合図が再接触の言葉に残るか

を見る実験として扱うのが安全。

より純粋に見る場合は、次の追加対照が必要。

- history-off: `previous_related_messages` を渡さずにfollowupだけ再生成する。
- 全期間修復イベントなし: Step1からrepairイベントを置かない。
- no-draft: `scripted_draft_do_not_copy` も渡さず、followup観測だけで生成する。
- tone-free: followupで `tone=repair` を出させず、外部の語彙分析で修復性を判定する。
