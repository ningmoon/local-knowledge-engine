"""Runtime discovery and dependency checks."""

from __future__ import annotations

import importlib.metadata
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


def find_executable(name: str) -> str | None:
    return shutil.which(name)


def environment_report() -> dict[str, Any]:
    report: dict[str, Any] = {
        "python": sys.version.split()[0],
        "python_executable": sys.executable,
        "ffmpeg": find_executable("ffmpeg"),
        "ffprobe": find_executable("ffprobe"),
    }
    try:
        import torch

        report.update(
            {
                "pytorch": torch.__version__,
                "cuda_available": torch.cuda.is_available(),
                "cuda_version": torch.version.cuda,
                "device": "cuda" if torch.cuda.is_available() else "cpu",
            }
        )
    except ImportError:
        report.update({"pytorch": None, "cuda_available": False, "cuda_version": None, "device": None})
    try:
        report["whisper"] = importlib.metadata.version("openai-whisper")
    except importlib.metadata.PackageNotFoundError:
        report["whisper"] = None
    return report


def require_dependencies() -> dict[str, Any]:
    report = environment_report()
    missing = []
    if not report["ffmpeg"] or not report["ffprobe"]:
        missing.append("FFmpeg/ffprobe")
    if not report["pytorch"]:
        missing.append("PyTorch")
    if not report["whisper"]:
        missing.append("openai-whisper")
    if missing:
        raise RuntimeError("Missing dependency: " + ", ".join(missing))
    return report


def ffmpeg_version(executable: str | None) -> str | None:
    if not executable:
        return None
    try:
        return subprocess.run(
            [executable, "-version"], check=True, capture_output=True, text=True
        ).stdout.splitlines()[0]
    except (OSError, subprocess.CalledProcessError, IndexError):
        return None


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]
