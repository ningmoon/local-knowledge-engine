#!/usr/bin/env python3
"""Deprecated compatibility entry point; resume is now part of the main CLI."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from local_knowledge_engine.cli import main  # noqa: E402


if __name__ == "__main__":
    print("Warning: use 'lke transcribe <input> --resume'.", file=sys.stderr)
    arguments = sys.argv[1:]
    if "--input" in arguments:
        input_index = arguments.index("--input")
        if input_index + 1 < len(arguments):
            input_value = arguments[input_index + 1]
            arguments = arguments[:input_index] + arguments[input_index + 2 :]
            arguments = [input_value, *arguments]
    raise SystemExit(main(["transcribe", *arguments]))
