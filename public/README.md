# ISS Benevolence Habitat Demo

GitHub Pages公開用の静的サイトです。

- メインUI: `visualization/iss_habitat_demo.html`
- デモURL: `https://karesansui-u.github.io/hackathon-singulab-inu/visualization/iss_habitat_demo.html`
- READMEプレビューGIF: `assets/iss20_100_demo.gif`
- 20x100デモ動画: `assets/iss20_100_demo.mp4`
- 20x100: `data/runs/iss20_no_nudge_100_ui_llm`, `data/runs/iss20_nudge_100_ui_llm`
- 20x100 ルールのみ/ナッジのみ追加実験: `data/runs/iss20_rule_only_100_ui_llm`, `data/runs/iss20_nudge_only_100_ui_llm`
- 20x100 後半修復イベントなし追加軸: `data/runs/iss20_no_nudge_no_repair_100_ui_llm`, `data/runs/iss20_nudge_only_no_repair_100_ui_llm`
- 20x100 全期間修復イベントなし追加軸: `data/runs/iss20_no_nudge_all_no_repair_100_ui_llm`, `data/runs/iss20_nudge_only_all_no_repair_100_ui_llm`
- 20x100 全期間喧嘩イベントなし追加軸: `data/runs/iss20_no_nudge_no_conflict_100_ui_llm`, `data/runs/iss20_nudge_only_no_conflict_100_ui_llm`
- 10x50: `data/runs/iss_no_nudge_smoke_ui_llm`, `data/runs/iss_nudge_smoke_ui_llm`
- 10x100 C条件: `data/runs/iss10_nudge_removed_100_ui_claude_sonnet46`
- スクリプト生成の予備データ: `data/runs/iss20_no_nudge_100_ui`, `data/runs/iss20_nudge_100_ui`
- GPT試行データ: `data/runs/iss20_nudge_100_ui_gpt_probe`
- 指標: `data/runs/iss20_llm_ab_100step_metrics.json`

元ファイルはこのディレクトリの外にあります。次のコマンドで再生成します。

```bash
python3 scripts/build_pages_site.py
```
