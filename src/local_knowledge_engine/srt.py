"""TXT and SRT serialization."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Iterable


def format_srt_timestamp(seconds: float) -> str:
    milliseconds = max(0, round(seconds * 1000))
    hours, milliseconds = divmod(milliseconds, 3_600_000)
    minutes, milliseconds = divmod(milliseconds, 60_000)
    seconds, milliseconds = divmod(milliseconds, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"


def _atomic_write(path: Path, content: str) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8", newline="\n")
    temporary.replace(path)


def write_outputs(segments: Iterable[dict[str, Any]], text_path: Path, srt_path: Path) -> None:
    materialized = list(segments)
    text = "\n".join(str(segment["text"]).strip() for segment in materialized if str(segment["text"]).strip())
    if text:
        text += "\n"
    subtitles = []
    for number, segment in enumerate(materialized, start=1):
        subtitles.append(
            f"{number}\n{format_srt_timestamp(float(segment['start']))} --> "
            f"{format_srt_timestamp(float(segment['end']))}\n{str(segment['text']).strip()}\n"
        )
    _atomic_write(text_path, text)
    _atomic_write(srt_path, "\n".join(subtitles))
