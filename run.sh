#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if [[ ! -d ".venv" ]]; then
  python3 -m venv .venv
fi

if ! .venv/bin/python -m pip show streamlit >/dev/null 2>&1; then
  .venv/bin/python -m pip install -r requirements.txt
fi

exec .venv/bin/python -m streamlit run app.py "$@"
