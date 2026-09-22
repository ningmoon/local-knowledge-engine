"""Traceability manifest generation."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_manifest(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    sources = payload.get("sources", [])
    if not isinstance(sources, list):
        raise RuntimeError(f"Invalid manifest sources: {path}")
    return sources


def build_source_record(
    *,
    source_file: Path,
    source_sha256: str,
    duration_seconds: float,
    model: str,
    language: str,
    device: str,
    chunk_seconds: int,
    whisper_version: str,
    text_path: Path,
    subtitle_path: Path,
) -> dict[str, Any]:
    return {
        "source_file": source_file.name,
        "source_sha256": source_sha256,
        "duration_seconds": round(duration_seconds, 3),
        "model": model,
        "language": language,
        "device": device,
        "chunk_seconds": chunk_seconds,
        "whisper_version": whisper_version,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "outputs": {"text": text_path.name, "subtitle": subtitle_path.name},
    }


def write_manifest(path: Path, sources: list[dict[str, Any]]) -> None:
    payload = {"schema_version": "1.0", "sources": sources}
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    temporary.replace(path)
