from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from local_knowledge_engine.media import discover_recordings, require_unique_stems, sha256_file


class MediaTests(unittest.TestCase):
    def test_filter_and_non_recursive_discovery(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "a.WAV").write_bytes(b"audio")
            (root / "notes.txt").write_text("ignore", encoding="utf-8")
            (root / "nested").mkdir()
            (root / "nested" / "b.mp3").write_bytes(b"audio")
            self.assertEqual([path.name for path in discover_recordings(root)], ["a.WAV"])

    def test_sha256(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "source.wav"
            path.write_bytes(b"abc")
            self.assertEqual(
                sha256_file(path),
                "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
            )

    def test_duplicate_stems_are_rejected(self) -> None:
        with self.assertRaises(RuntimeError):
            require_unique_stems([Path("lesson.wav"), Path("lesson.mp3")])


if __name__ == "__main__":
    unittest.main()
