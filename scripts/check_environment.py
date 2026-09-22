#!/usr/bin/env python3
"""Deprecated compatibility entry point for ``lke check``."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from local_knowledge_engine.cli import main  # noqa: E402


if __name__ == "__main__":
    print("Warning: use 'lke check' after installing the package.", file=sys.stderr)
    raise SystemExit(main(["check"]))
