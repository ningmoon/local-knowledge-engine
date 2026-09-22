from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from local_knowledge_engine.provenance import build_source_record, write_manifest


class ProvenanceTests(unittest.TestCase):
    def test_manifest_has_relative_names_and_required_fields(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "lesson.wav"
            record = build_source_record(
                source_file=source,
                source_sha256="a" * 64,
                duration_seconds=12.3456,
                model="small",
                language="zh",
                device="cpu",
                chunk_seconds=600,
                whisper_version="test",
                text_path=root / "lesson.txt",
                subtitle_path=root / "lesson.srt",
            )
            manifest = root / "manifest.json"
            write_manifest(manifest, [record])
            payload = json.loads(manifest.read_text(encoding="utf-8"))
            self.assertEqual(payload["schema_version"], "1.0")
            self.assertEqual(payload["sources"][0]["source_file"], "lesson.wav")
            self.assertNotIn(str(root), manifest.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
