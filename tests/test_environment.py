from __future__ import annotations

import unittest
from unittest.mock import patch

from local_knowledge_engine.environment import require_dependencies


class EnvironmentTests(unittest.TestCase):
    def test_missing_ffmpeg_is_reported(self) -> None:
        report = {
            "ffmpeg": None,
            "ffprobe": None,
            "pytorch": "test",
            "whisper": "test",
        }
        with patch("local_knowledge_engine.environment.environment_report", return_value=report):
            with self.assertRaisesRegex(RuntimeError, "FFmpeg/ffprobe"):
                require_dependencies()


if __name__ == "__main__":
    unittest.main()
