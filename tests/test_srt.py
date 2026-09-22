from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from local_knowledge_engine.srt import format_srt_timestamp, write_outputs


class SrtTests(unittest.TestCase):
    def test_timestamp_format(self) -> None:
        self.assertEqual(format_srt_timestamp(3661.234), "01:01:01,234")
        self.assertEqual(format_srt_timestamp(-1), "00:00:00,000")

    def test_utf8_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            text_path = root / "课程.txt"
            srt_path = root / "课程.srt"
            write_outputs([{"start": 0.0, "end": 1.5, "text": "本地知识"}], text_path, srt_path)
            self.assertEqual(text_path.read_text(encoding="utf-8"), "本地知识\n")
            self.assertIn("00:00:00,000 --> 00:00:01,500", srt_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
