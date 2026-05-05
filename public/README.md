# ISS Benevolence Habitat Demo

GitHub Pages公開用の静的サイトです。

- Main UI: `visualization/iss_habitat_demo.html`
- 20x100: `data/runs/iss20_no_nudge_100_ui_llm`, `data/runs/iss20_nudge_100_ui_llm`
- 10x50: `data/runs/iss_no_nudge_smoke_ui_llm`, `data/runs/iss_nudge_smoke_ui_llm`
- 10x100 Run C: `data/runs/iss10_nudge_removed_100_ui_claude_sonnet46`
- Scripted fallback: `data/runs/iss20_no_nudge_100_ui`, `data/runs/iss20_nudge_100_ui`
- GPT probe: `data/runs/iss20_nudge_100_ui_gpt_probe`
- KPI: `data/runs/iss20_llm_ab_100step_metrics.json`

Source files live outside this directory. Rebuild this folder with:

```bash
python3 scripts/build_pages_site.py
```
