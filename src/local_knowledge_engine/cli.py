"""Command-line interface for Local Knowledge Engine."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from .config import DEVICES, MODELS, TranscriptionConfig
from .environment import environment_report, ffmpeg_version
from .transcription import transcribe


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="lke", description="Local Knowledge Engine evidence tooling")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check", help="Report Python, Whisper, PyTorch, CUDA, and FFmpeg status")
    transcribe_parser = commands.add_parser("transcribe", help="Create traceable TXT/SRT evidence from local media")
    transcribe_parser.add_argument("input", type=Path, help="Directory containing local audio or video files")
    transcribe_parser.add_argument("--output", type=Path, help="Output directory (default: <input>/transcript)")
    transcribe_parser.add_argument("--model", choices=MODELS, default="small")
    transcribe_parser.add_argument("--device", choices=DEVICES, default="auto")
    transcribe_parser.add_argument("--language", default="zh")
    transcribe_parser.add_argument("--chunk-seconds", type=int, default=600)
    transcribe_parser.add_argument("--resume", action=argparse.BooleanOptionalAction, default=True)
    transcribe_parser.add_argument("--overwrite", action="store_true")
    transcribe_parser.add_argument("--verbose", action="store_true")
    return parser


def _print_event(event: dict[str, Any]) -> None:
    kind = event["event"]
    if kind == "model_loading":
        print(f"Loading model '{event['model']}' on {event['device']}...", flush=True)
    elif kind == "file_started":
        print(
            f"[{event['file_index']}/{event['file_count']}] {event['file']} "
            f"({event['chunk_count']} chunk(s))",
            flush=True,
        )
    elif kind == "chunk_started":
        print(f"  chunk {event['chunk_index'] + 1}/{event['chunk_count']}", flush=True)
    elif kind == "chunk_skipped":
        print(f"  chunk {event['chunk_index'] + 1}: checkpoint exists; skipped", flush=True)
    elif kind == "file_skipped":
        print(f"Skip {event['file']}: outputs already exist", flush=True)
    elif kind == "file_completed":
        print(f"  saved {Path(event['text']).name} and {Path(event['subtitle']).name}", flush=True)
    elif kind == "warning":
        print(f"Warning: {event['message']}", file=sys.stderr, flush=True)


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "check":
        report = environment_report()
        report["ffmpeg_version"] = ffmpeg_version(report["ffmpeg"])
        print(json.dumps(report, ensure_ascii=False, indent=2))
        required = ("ffmpeg", "ffprobe", "pytorch", "whisper")
        return 0 if all(report[item] for item in required) else 1

    output = args.output or args.input / "transcript"
    config = TranscriptionConfig(
        input_directory=args.input,
        output_directory=output,
        model=args.model,
        language=args.language,
        device=args.device,
        chunk_seconds=args.chunk_seconds,
        resume=args.resume,
        overwrite=args.overwrite,
        verbose=args.verbose,
    )
    try:
        transcribe(config, _print_event)
        return 0
    except RuntimeError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
