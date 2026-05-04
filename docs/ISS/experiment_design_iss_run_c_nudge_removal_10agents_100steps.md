# ISS Run C 実験設計
## 10 agents / 100 steps / ナッジ撤去後の文化定着

最終更新: 2026/05/05

---

## 目的

Run C は、Run B の「善性オブジェクトあり」環境を 1〜50 step で経験したあと、51 step 以降に物理ナッジを撤去し、行動様式だけが残るかを見る実験。

見る問い:

- ナッジオブジェクトが消えたあとも、声かけ許可・一人時間尊重・資源のチーム語りが残るか
- 修復会話が「物体を介した修復」から「作法を思い出す修復」へ移るか
- 51〜100 step で摩擦が再燃しても、Run B で学習した作法により短く戻れるか

---

## 実験構造

| 区間 | 状態 | 観察対象 |
|---|---|---|
| 1〜50 | Run B 相当。持ち寄り棚、OKサイン、聖域マーク、スコアボード、移動投票パネルあり | ナッジ経験の獲得 |
| 51〜55 | ナッジ撤去直後 | 物理手がかり喪失への反応 |
| 56〜80 | 道具なし運用 | 作法が人同士の確認へ移るか |
| 81〜100 | 帰還前ストレス | 高ストレス下でも文化として残るか |

正準データ:

- Scenario: `domain_packs/iss_benevolence/scenarios/run_c.yaml`
- Events: `domain_packs/iss_benevolence/data/events_run_c.tsv`
- Claude Sonnet 4.6 config: `examples/spatial_demo/configs/config.iss.claude.sonnet46.run_c.yaml`

---

## 評価方針

Run C 単体では、51〜100 step の以下を見る。

- conflict 後の repair 発生率
- repair までの step 差
- repair detail に「昔のオブジェクト」ではなく「自発ルール」「短い言葉」「口頭運用」が出るか
- active_objects が 51 step 以降 0 であること
- related_object_id は残ってもよい。ただし意味は「物理的に稼働中」ではなく「過去のナッジ経験に由来する作法」

比較するなら:

- Run B 1〜50: ナッジありの修復
- Run C 51〜100: ナッジ撤去後の修復
- 任意で Run A 51〜100 相当を作り、ナッジ経験なしの自然経過と比較する

---

## 生成コマンド想定

まず scripted UI frame を作る。

```bash
python3 scripts/export_habitat_frames.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_c \
  --output-dir outputs/runs/iss10_nudge_removed_100_ui
```

次に Claude Sonnet 4.6 で会話を差し替える。

```bash
python3 scripts/generate_habitat_conversations.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_c \
  --input-dir outputs/runs/iss10_nudge_removed_100_ui \
  --output-dir outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46 \
  --llm-config examples/spatial_demo/configs/config.iss.claude.sonnet46.run_c.yaml \
  --start-step 1 \
  --end-step 100
```

軽く確認する場合は 51〜60 だけでよい。

```bash
python3 scripts/generate_habitat_conversations.py \
  --pack domain_packs/iss_benevolence \
  --scenario run_c \
  --input-dir outputs/runs/iss10_nudge_removed_100_ui \
  --output-dir outputs/runs/iss10_nudge_removed_100_ui_claude_sonnet46_probe \
  --llm-config examples/spatial_demo/configs/config.iss.claude.sonnet46.run_c.yaml \
  --start-step 51 \
  --end-step 60
```

レポート記載モデル名:

- `claude-sonnet-4-6`
- Backend: Claude Code CLI
- CLI versionは実行時に `claude --version` で記録する

---

## 注意点

- 51 step 以降、物理オブジェクトは active_objects に出ないことを必ず確認する
- 会話生成プロンプトには、51 step 以降のイベント説明として「物理ナッジは撤去済み」と明示される
- related_object_id が post-removal の conflict/repair に残るのは、UI/分析上「過去のナッジ経験由来」と読む
- 10人100stepなので、20x100とは分けて保存する
