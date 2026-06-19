#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-python3}"
VENV="$ROOT/.venv"

if [ ! -x "$VENV/bin/python" ]; then
  "$PYTHON" -m venv "$VENV"
fi

"$VENV/bin/python" -m pip install --upgrade pyinstaller

exec "$VENV/bin/python" -m PyInstaller \
  --clean \
  --noconfirm \
  --onefile \
  --name bonesinfra \
  --paths "$ROOT/src" \
  --collect-data bonesinfra \
  --collect-submodules pyinfra \
  "$ROOT/src/bonesinfra/__main__.py"
