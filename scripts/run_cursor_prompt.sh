#!/usr/bin/env bash

set -euo pipefail

if ! command -v cursor >/dev/null 2>&1; then
  echo "cursor CLI was not found on PATH." >&2
  exit 127
fi

prompt_from_args="${1:-}"
prompt_from_stdin=""
if [[ -z "${prompt_from_args}" ]]; then
  prompt_from_stdin="$(cat)"
fi
prompt="${prompt_from_args:-$prompt_from_stdin}"

if [[ -z "${prompt}" ]]; then
  echo "No prompt was provided to run_cursor_prompt.sh" >&2
  exit 1
fi

composite_prompt=$(
  cat <<EOF
You are being used as a pure text generation backend inside a simulation loop.
Do not run commands, inspect files, edit the repository, or use tools.
Return only the final answer requested by the prompt below.

$prompt
EOF
)

cursor_cmd=(cursor agent -p --output-format json --mode ask)
if [[ -n "${CURSOR_MODEL:-}" ]]; then
  cursor_cmd+=(--model "$CURSOR_MODEL")
fi

raw_json="$("${cursor_cmd[@]}" "$composite_prompt" 2>/dev/null)"

if [[ -z "${raw_json}" ]]; then
  echo "cursor agent returned empty output" >&2
  exit 1
fi

python3 - <<'PY' "$raw_json"
import json
import sys

raw = sys.argv[1]

def extract_text(payload):
    if isinstance(payload, str):
        return payload.strip()
    if isinstance(payload, dict):
        for key in ("result", "response", "output_text", "text", "content", "message"):
            value = payload.get(key)
            if isinstance(value, str) and value.strip():
                return value.strip()
        # Common nested shapes
        if isinstance(payload.get("message"), dict):
            maybe = payload["message"].get("content")
            if isinstance(maybe, str) and maybe.strip():
                return maybe.strip()
        if isinstance(payload.get("data"), dict):
            nested = extract_text(payload["data"])
            if nested:
                return nested
        return json.dumps(payload, ensure_ascii=False)
    if isinstance(payload, list):
        for item in payload:
            extracted = extract_text(item)
            if extracted:
                return extracted
        return ""
    return str(payload).strip()

try:
    parsed = json.loads(raw)
except json.JSONDecodeError:
    print(raw.strip())
    sys.exit(0)

result = extract_text(parsed)
if not result:
    sys.exit(1)
print(result)
PY
