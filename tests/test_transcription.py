from __future__ import annotations

import json
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

from local_knowledge_engine.config import TranscriptionConfig
from local_knowledge_engine.transcription import transcribe


class FakeModel:
    def __init__(self) -> None:
        self.calls: list[dict[str, object]] = []

    def transcribe(self, path: str, **kwargs: object) -> dict[str, object]:
        self.calls.append({"path": path, **kwargs})
        return {"segments": [{"start": 0.0, "end": 1.25, "text": " 测试课程 "}]}


class TranscriptionTests(unittest.TestCase):
    def test_empty_directory_does_not_require_ml_dependencies(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            events: list[dict[str, object]] = []
            config = TranscriptionConfig(input_directory=root, output_directory=root / "output")
            with patch("local_knowledge_engine.transcription.require_dependencies") as require:
                self.assertEqual(transcribe(config, events.append), [])
            require.assert_not_called()
            self.assertEqual(events[0]["event"], "warning")

    def test_one_chunk_creates_evidence_checkpoint_and_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            input_directory = root / "input"
            output_directory = root / "output"
            input_directory.mkdir()
            source = input_directory / "lesson.wav"
            source.write_bytes(b"authorized-test-placeholder")
            model = FakeModel()
            fake_whisper = types.SimpleNamespace(load_model=lambda name, device: model)
            events: list[dict[str, object]] = []

            def fake_extract(_source: Path, destination: Path, _start: float, _duration: float) -> None:
                destination.write_bytes(b"chunk")

            config = TranscriptionConfig(input_directory=input_directory, output_directory=output_directory)
            with (
                patch.dict(sys.modules, {"whisper": fake_whisper}),
                patch(
                    "local_knowledge_engine.transcription.require_dependencies",
                    return_value={"cuda_available": False, "whisper": "test"},
                ),
                patch("local_knowledge_engine.transcription.duration_seconds", return_value=12.0),
                patch("local_knowledge_engine.transcription.extract_chunk", side_effect=fake_extract),
            ):
                records = transcribe(config, events.append)

            self.assertEqual(len(records), 1)
            self.assertEqual((output_directory / "lesson.txt").read_text(encoding="utf-8"), "测试课程\n")
            self.assertTrue((output_directory / "lesson.srt").exists())
            self.assertTrue((output_directory / ".checkpoints" / "lesson" / "chunk_00000.json").exists())
            manifest = json.loads((output_directory / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["sources"][0]["device"], "cpu")
            self.assertFalse(model.calls[0]["fp16"])
            self.assertIn("file_completed", [event["event"] for event in events])

    def test_completed_outputs_skip_model_loading_and_preserve_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            input_directory = root / "input"
            output_directory = root / "output"
            input_directory.mkdir()
            output_directory.mkdir()
            (input_directory / "lesson.wav").write_bytes(b"source")
            (output_directory / "lesson.txt").write_text("done\n", encoding="utf-8")
            (output_directory / "lesson.srt").write_text("done\n", encoding="utf-8")
            existing = {"schema_version": "1.0", "sources": [{"source_file": "lesson.wav"}]}
            (output_directory / "manifest.json").write_text(json.dumps(existing), encoding="utf-8")
            config = TranscriptionConfig(input_directory=input_directory, output_directory=output_directory)
            with patch(
                "local_knowledge_engine.transcription.require_dependencies",
                return_value={"cuda_available": False, "whisper": "test"},
            ):
                records = transcribe(config)
            self.assertEqual(records, existing["sources"])


if __name__ == "__main__":
    unittest.main()
