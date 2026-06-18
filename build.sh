#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-python3}"

if command -v uv >/dev/null 2>&1; then
  exec uv run --with pyinstaller --project "$ROOT" python -m PyInstaller \
    --clean \
    --noconfirm \
    --onefile \
    --name bonesinfra \
    --paths "$ROOT/src" \
    --collect-data bonesinfra \
    --collect-submodules pyinfra \
    "$ROOT/src/bonesinfra/__main__.py"
fi

"$PYTHON" -m pip install --upgrade pyinstaller

exec "$PYTHON" -m PyInstaller \
  --clean \
  --noconfirm \
  --onefile \
  --name bonesinfra \
  --paths "$ROOT/src" \
  --collect-data bonesinfra \
  --collect-submodules pyinfra \
  "$ROOT/src/bonesinfra/__main__.py"
