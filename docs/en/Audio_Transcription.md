# Local Transcription

[中文](../Audio_Transcription.md) | **English**

The local tooling layer only turns media into Evidence. It does not call an LLM
or generate the final knowledge document.

## Commands

```powershell
lke check
lke transcribe <input-directory> `
  --output <output-directory> `
  --model small `
  --device auto `
  --language en `
  --chunk-seconds 600 `
  --resume
```

Supported formats are `mp3`, `wav`, `m4a`, `mp4`, `aac`, `flac`, `ogg`, and
`wma`. Only the first level of the input directory is scanned.

Media files in one input directory must not share the same filename stem. For
example, `lesson.wav` and `lesson.mp3` would collide in TXT/SRT and checkpoint
paths, so the CLI rejects that input.

## Behavior

- The default model is `small`.
- `--device auto` prefers CUDA and falls back to CPU.
- `--device cpu|cuda` selects a device explicitly. Requesting unavailable CUDA
  fails with a clear error.
- `--resume` is enabled by default and skips existing checkpoints.
- A source file is skipped when both its TXT and SRT outputs already exist.
- `--overwrite` retranscribes a file and ignores completed outputs and existing
  checkpoints.
- Completed files are written through atomic replacement to reduce the risk of
  partial output after interruption.

## Deprecated entry points

The root `audio_transcribe.py` and `scripts/audio_transcribe_resumable.py`
scripts remain temporarily for compatibility, but they are no longer the
primary interface. New behavior belongs in `lke transcribe`.
