"""Configuration shared by the CLI and future adapters."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

SUPPORTED_EXTENSIONS = frozenset({".mp3", ".wav", ".m4a", ".mp4", ".aac", ".flac", ".ogg", ".wma"})
MODELS = ("tiny", "base", "small", "medium", "large-v3")
DEVICES = ("auto", "cpu", "cuda")


@dataclass(frozen=True)
class TranscriptionConfig:
    input_directory: Path
    output_directory: Path
    model: str = "small"
    language: str = "zh"
    device: str = "auto"
    chunk_seconds: int = 600
    resume: bool = True
    overwrite: bool = False
    verbose: bool = False


def resolve_device(requested: str, cuda_available: bool) -> str:
    """Resolve a requested device without importing the ML runtime."""
    if requested not in DEVICES:
        raise ValueError(f"Unsupported device: {requested}")
    if requested == "cuda" and not cuda_available:
        raise RuntimeError("CUDA was requested but is not available")
    if requested == "auto":
        return "cuda" if cuda_available else "cpu"
    return requested
