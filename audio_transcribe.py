#!/usr/bin/env python3
"""Deprecated compatibility entry point for the historical transcription CLI."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from local_knowledge_engine.cli import main  # noqa: E402


def legacy_main() -> int:
    print(
        "Warning: audio_transcribe.py is deprecated; install the package and use 'lke transcribe'.",
        file=sys.stderr,
    )
    arguments = sys.argv[1:]
    if arguments == ["--check"]:
        return main(["check"])
    if "--input" not in arguments:
        return main(["transcribe", *arguments])
    input_index = arguments.index("--input")
    if input_index + 1 >= len(arguments):
        return main(["transcribe", *arguments])
    input_value = arguments[input_index + 1]
    translated = arguments[:input_index] + arguments[input_index + 2 :]
    return main(["transcribe", input_value, *translated])


if __name__ == "__main__":
    raise SystemExit(legacy_main())
