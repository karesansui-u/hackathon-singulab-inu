# ISS Run C Nudge Removal Report

Date: 2026-05-05

## Summary

Run C tests whether practices learned from benevolence objects remain after the physical nudge objects are removed.

- Steps 1-50: Run B-like environment with active nudge objects
- Steps 51-100: physical nudge objects removed
- Agents: 10
- Conversation model: `claude-sonnet-4-6`
- Backend: Claude Code CLI `2.1.126`
- Output: `outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46`

## Generation Result

| Item | Value |
|---|---:|
| Frames | 100 |
| Conversation threads | 143 |
| Messages | 286 |
| LLM threads | 143 |
| LLM messages | 286 |
| Failed threads | 0 |
| Active objects in steps 1-50 | 168 frame-object appearances |
| Active objects in steps 51-100 | 0 |

Manifest records:

- `model`: `claude-sonnet-4-6`
- `provider`: `command`
- `prompt_mode`: `stdin`
- `generated_thread_count`: 143
- `failed_thread_count`: 0

## Before / After Removal

| Window | Threads | Messages | Unique pairs | Conflict | Repair | Routine |
|---|---:|---:|---:|---:|---:|---:|
| Steps 1-50 | 70 | 140 | 20 | 7 | 13 | 50 |
| Steps 51-100 | 73 | 146 | 17 | 7 | 16 | 50 |

The post-removal window has no active nudge objects, but repair threads still occur after each designed conflict.

## Post-Removal Conflict/Repair Map

| Conflict | Step | Repair | Step | Prior nudge practice |
|---|---:|---|---:|---|
| `CCONF01` 持ち寄り棚なき声量摩擦 | 53 | `CREP01` 声量ルールの自発再現 | 54 | `OBJ07` 持ち寄り棚 |
| `CCONF02` OKサイン撤去後のキューポラ境界 | 61 | `CREP02` 言葉だけのOKサイン | 62 | `OBJ06` 話しかけてOKサイン |
| `CCONF03` 聖域マーク撤去後の個室待ち | 68 | `CREP03` 個室聖域の口頭運用 | 69 | `OBJ09` 個室聖域マーク |
| `CCONF04` スコアボード撤去後の資源疑心 | 76 | `CREP04` チーム記録の口頭化 | 78 | `OBJ03` リソース・スコアボード |
| `CCONF05` 移動投票パネル撤去後の運動枠 | 84 | `CREP05` 運動前の自発チェックイン | 85 | `OBJ10` モジュール移動投票パネル |
| `CCONF06` 帰還前の助言の再燃 | 93 | `CREP06` 経験共有の作法が残る | 94 | `OBJ07` 持ち寄り棚 |

## Sample Checks

Step 53 conflict:

> Sofia: Fatima、ここ音拾いやすいから。気に、してもらえると。  
> Fatima: 今、誰とも話してない。静かにしてる。

Step 54 repair:

> Sofia: ……食事の後、ここ片付けとく。  
> Fatima: ……ありがとう。

Step 61 conflict:

> Henri: サインがなくなってから、ここに入っていいのかいつも迷う。  
> Amir: 迷うなら来なければいい。俺のせいにしないでくれ。

Step 62 repair:

> Amir: ……次、声かけてくれれば答える。無視はしない。  
> Henri: ありがとう。そうする。

## Interpretation

The run is usable as a first Run C dataset. It shows that once physical objects disappear, conflicts can reappear around the same boundaries, but short repair practices continue to occur without active objects.

The strongest evidence is not that every repair explicitly names the old object. Rather, the repairs shift into smaller behavioral conventions: quiet practical help, verbal permission, scheduled privacy, team-level wording, and experience-sharing instead of advice.
