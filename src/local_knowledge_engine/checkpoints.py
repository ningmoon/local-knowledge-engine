"""Atomic checkpoint persistence."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_checkpoint(path: Path) -> list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def save_checkpoint(path: Path, segments: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(segments, ensure_ascii=False, indent=2), encoding="utf-8")
    temporary.replace(path)
