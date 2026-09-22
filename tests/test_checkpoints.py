from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from local_knowledge_engine.checkpoints import load_checkpoint, save_checkpoint


class CheckpointTests(unittest.TestCase):
    def test_save_and_resume_unicode_segments(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "chunks" / "chunk_00000.json"
            expected = [{"start": 0.0, "end": 1.0, "text": "测试"}]
            save_checkpoint(path, expected)
            self.assertEqual(load_checkpoint(path), expected)
            self.assertFalse(path.with_suffix(".json.tmp").exists())


if __name__ == "__main__":
    unittest.main()
