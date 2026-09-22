"""Media discovery, inspection, and chunk extraction."""

from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path

from .config import SUPPORTED_EXTENSIONS
from .environment import find_executable


def discover_recordings(directory: Path) -> list[Path]:
    return sorted(path for path in directory.iterdir() if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS)


def require_unique_stems(recordings: list[Path]) -> None:
    seen: dict[str, Path] = {}
    for recording in recordings:
        key = recording.stem.casefold()
        if key in seen:
            raise RuntimeError(
                f"Media files would overwrite the same outputs: {seen[key].name} and {recording.name}"
            )
        seen[key] = recording


def sha256_file(path: Path, block_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        while block := source.read(block_size):
            digest.update(block)
    return digest.hexdigest()


def duration_seconds(path: Path) -> float:
    executable = find_executable("ffprobe") or "ffprobe"
    command = [
        executable,
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        str(path),
    ]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return float(result.stdout.strip())
    except (FileNotFoundError, subprocess.CalledProcessError, ValueError) as error:
        raise RuntimeError(f"Could not read duration for {path.name}; make sure FFmpeg is installed") from error


def extract_chunk(source: Path, destination: Path, start: float, duration: float) -> None:
    executable = find_executable("ffmpeg") or "ffmpeg"
    command = [
        executable,
        "-nostdin",
        "-hide_banner",
        "-loglevel",
        "error",
        "-y",
        "-ss",
        str(start),
        "-t",
        str(duration),
        "-i",
        str(source),
        "-vn",
        "-ac",
        "1",
        "-ar",
        "16000",
        str(destination),
    ]
    try:
        subprocess.run(command, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError) as error:
        raise RuntimeError(f"FFmpeg could not create a chunk for {source.name}") from error
