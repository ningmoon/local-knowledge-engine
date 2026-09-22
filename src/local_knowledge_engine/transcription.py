"""Unified resumable transcription engine."""

from __future__ import annotations

import tempfile
from collections.abc import Callable
from pathlib import Path
from typing import Any

from .checkpoints import load_checkpoint, save_checkpoint
from .config import TranscriptionConfig, resolve_device
from .environment import require_dependencies
from .media import discover_recordings, duration_seconds, extract_chunk, require_unique_stems, sha256_file
from .provenance import build_source_record, load_manifest, write_manifest
from .srt import write_outputs

EventHandler = Callable[[dict[str, Any]], None]


def _emit(handler: EventHandler | None, event: str, **details: Any) -> None:
    if handler:
        handler({"event": event, **details})


def transcribe(config: TranscriptionConfig, on_event: EventHandler | None = None) -> list[dict[str, Any]]:
    if not config.input_directory.is_dir():
        raise RuntimeError(f"Input directory does not exist: {config.input_directory}")
    if config.chunk_seconds < 30:
        raise RuntimeError("chunk_seconds must be at least 30")

    recordings = discover_recordings(config.input_directory)
    if not recordings:
        _emit(on_event, "warning", message="No supported media files found")
        return []
    require_unique_stems(recordings)
    runtime = require_dependencies()
    device = resolve_device(config.device, bool(runtime["cuda_available"]))

    config.output_directory.mkdir(parents=True, exist_ok=True)
    checkpoint_root = config.output_directory / ".checkpoints"
    checkpoint_root.mkdir(parents=True, exist_ok=True)
    manifest_path = config.output_directory / "manifest.json"
    source_records = load_manifest(manifest_path)
    model: Any | None = None

    for file_index, source in enumerate(recordings, start=1):
        text_path = config.output_directory / f"{source.stem}.txt"
        srt_path = config.output_directory / f"{source.stem}.srt"
        if config.overwrite:
            completed = False
        else:
            completed = text_path.exists() and srt_path.exists()
        if completed:
            _emit(on_event, "file_skipped", file=source.name, reason="outputs_exist")
            continue

        duration = duration_seconds(source)
        chunk_count = max(1, int((duration + config.chunk_seconds - 1) // config.chunk_seconds))
        checkpoint_directory = checkpoint_root / source.stem
        checkpoint_directory.mkdir(parents=True, exist_ok=True)
        _emit(
            on_event,
            "file_started",
            file=source.name,
            file_index=file_index,
            file_count=len(recordings),
            duration_seconds=duration,
            chunk_count=chunk_count,
        )

        if model is None:
            import whisper

            _emit(on_event, "model_loading", model=config.model, device=device)
            model = whisper.load_model(config.model, device=device)

        with tempfile.TemporaryDirectory(prefix="lke_whisper_") as temporary_directory:
            for chunk_index in range(chunk_count):
                checkpoint = checkpoint_directory / f"chunk_{chunk_index:05d}.json"
                if config.resume and checkpoint.exists() and not config.overwrite:
                    _emit(on_event, "chunk_skipped", file=source.name, chunk_index=chunk_index)
                    continue
                start = chunk_index * config.chunk_seconds
                length = min(config.chunk_seconds, max(0.1, duration - start))
                _emit(
                    on_event,
                    "chunk_started",
                    file=source.name,
                    chunk_index=chunk_index,
                    chunk_count=chunk_count,
                    start_seconds=start,
                    duration_seconds=length,
                )
                chunk_path = Path(temporary_directory) / f"chunk_{chunk_index:05d}.wav"
                extract_chunk(source, chunk_path, start, length)
                result = model.transcribe(
                    str(chunk_path),
                    language=config.language,
                    fp16=device == "cuda",
                    verbose=config.verbose,
                    condition_on_previous_text=False,
                )
                segments = [
                    {
                        "start": float(segment["start"]) + start,
                        "end": float(segment["end"]) + start,
                        "text": str(segment["text"]).strip(),
                    }
                    for segment in result["segments"]
                    if str(segment["text"]).strip()
                ]
                save_checkpoint(checkpoint, segments)
                _emit(on_event, "chunk_completed", file=source.name, chunk_index=chunk_index)

        all_segments: list[dict[str, Any]] = []
        for chunk_index in range(chunk_count):
            checkpoint = checkpoint_directory / f"chunk_{chunk_index:05d}.json"
            if not checkpoint.exists():
                raise RuntimeError(f"Missing checkpoint: {checkpoint}")
            all_segments.extend(load_checkpoint(checkpoint))
        write_outputs(all_segments, text_path, srt_path)
        source_record = build_source_record(
            source_file=source,
            source_sha256=sha256_file(source),
            duration_seconds=duration,
            model=config.model,
            language=config.language,
            device=device,
            chunk_seconds=config.chunk_seconds,
            whisper_version=str(runtime["whisper"]),
            text_path=text_path,
            subtitle_path=srt_path,
        )
        source_records = [record for record in source_records if record.get("source_file") != source.name]
        source_records.append(source_record)
        _emit(on_event, "file_completed", file=source.name, text=str(text_path), subtitle=str(srt_path))

    if source_records:
        write_manifest(manifest_path, sorted(source_records, key=lambda record: str(record.get("source_file", ""))))
    return source_records
