#!/usr/bin/env python3
"""Build a small GitHub Pages-ready static site.

The source UI keeps using local development paths under ``outputs/runs``.
This builder copies only the publishable artifacts into ``public/`` and rewrites
the copied HTML to read from ``public/data/runs``.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"

RUN_DIRS = [
    "iss10_nudge_removed_100_ui_claude_sonnet46",
    "iss20_no_nudge_100_ui_llm",
    "iss20_nudge_100_ui_llm",
    "iss20_no_nudge_100_ui",
    "iss20_nudge_100_ui",
    "iss20_nudge_100_ui_gpt_probe",
    "iss_no_nudge_smoke_ui_llm",
    "iss_nudge_smoke_ui_llm",
]

TEXT_SUFFIXES = {".html", ".json", ".jsonl", ".md", ".tsv", ".txt", ".yaml", ".yml"}


def copytree_clean(source: Path, target: Path) -> None:
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target)
    normalize_text_files(target)


def normalize_text_files(root: Path) -> None:
    for path in root.rglob("*"):
        if path.is_file() and path.suffix in TEXT_SUFFIXES:
            text = path.read_text(encoding="utf-8")
            path.write_text(text.replace("\r\n", "\n"), encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build_public_site() -> None:
    PUBLIC.mkdir(parents=True, exist_ok=True)
    (PUBLIC / "visualization").mkdir(parents=True, exist_ok=True)
    (PUBLIC / "data" / "runs").mkdir(parents=True, exist_ok=True)

    source_html = ROOT / "visualization" / "iss_habitat_demo.html"
    if not source_html.exists():
        raise SystemExit(f"Missing UI source: {source_html}")

    html = source_html.read_text(encoding="utf-8")
    html = html.replace("../outputs/runs/", "../data/runs/")
    html = html.replace(
        'a10: ["../data/runs/iss_no_nudge_smoke_ui_llm", "../data/runs/iss_no_nudge_smoke_ui", "../data/runs/iss_habitat_run_a"],',
        'a10: ["../data/runs/iss_no_nudge_smoke_ui_llm"],',
    )
    html = html.replace(
        'b10: ["../data/runs/iss_nudge_smoke_ui_llm", "../data/runs/iss_nudge_smoke_ui", "../data/runs/iss_habitat_run_b"],',
        'b10: ["../data/runs/iss_nudge_smoke_ui_llm"],',
    )
    write_text(PUBLIC / "visualization" / "iss_habitat_demo.html", html)

    for run_dir in RUN_DIRS:
        source = ROOT / "outputs" / "runs" / run_dir
        if not source.exists():
            raise SystemExit(f"Missing run output: {source}")
        copytree_clean(source, PUBLIC / "data" / "runs" / run_dir)

    for comparison_name in (
        "iss20_llm_ab_100step_metrics.json",
        "iss20_ab_100step_metrics.json",
        "iss_habitat_llm_ab_50step.json",
    ):
        comparison = ROOT / "outputs" / "runs" / comparison_name
        if comparison.exists():
            shutil.copy2(comparison, PUBLIC / "data" / "runs" / comparison.name)

    write_text(
        PUBLIC / "index.html",
        """<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>ISS Benevolence Habitat Demo</title>
  <meta http-equiv="refresh" content="0; url=visualization/iss_habitat_demo.html">
  <link rel="canonical" href="visualization/iss_habitat_demo.html">
</head>
<body>
  <p><a href="visualization/iss_habitat_demo.html">ISS Benevolence Habitat Demo</a></p>
</body>
</html>
""",
    )
    write_text(
        PUBLIC / "README.md",
        """# ISS Benevolence Habitat Demo

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
""",
    )
    write_text(PUBLIC / ".nojekyll", "")


def parse_args() -> argparse.Namespace:
    return argparse.ArgumentParser(description="Build public GitHub Pages site.").parse_args()


def main() -> None:
    parse_args()
    build_public_site()
    print(f"Wrote GitHub Pages site to {PUBLIC}")


if __name__ == "__main__":
    main()
