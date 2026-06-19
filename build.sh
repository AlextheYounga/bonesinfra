#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-python3}"
VENV="$ROOT/.venv"

if [ ! -x "$VENV/bin/python" ]; then
  "$PYTHON" -m venv "$VENV"
fi

if [ ! -x "$VENV/bin/pip" ]; then
  "$VENV/bin/python" -m ensurepip --upgrade
fi

"$VENV/bin/python" -m pip install --upgrade pip
"$VENV/bin/python" -m pip install --upgrade --group dev "$ROOT"

exec "$VENV/bin/python" -m PyInstaller \
  --clean \
  --noconfirm \
  --onefile \
  --name bonesinfra \
  --paths "$ROOT/src" \
  --collect-data bonesinfra \
  --collect-submodules pyinfra \
  "$ROOT/src/bonesinfra/__main__.py"
