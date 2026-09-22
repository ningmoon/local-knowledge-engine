# Provenance

[中文](../Provenance.md) | **English**

## Purpose

Traceability should answer: Which source file produced this output? Did that
source change? Which model and parameters were used? When was the output
created? How can a reviewer return to the original evidence?

## Manifest contract

`lke transcribe` creates `manifest.json` in the output directory. Each source
record contains at least:

- `source_file`
- `source_sha256`
- `duration_seconds`
- `model`
- `language`
- `device`
- `chunk_seconds`
- `whisper_version`
- `created_at`
- `outputs.text`
- `outputs.subtitle`

The machine-readable schema is available at
[manifest.schema.json](../../templates/manifest.schema.json).

## Source references

Knowledge Compilation assigns each recording a stable identifier such as `F0`
or `F1`. Body references use a form such as `[F2 01:23:45]`. The source index
stores the identifier, real filename, duration, topic, and boundary decision.

## Integrity rules

- If a source SHA256 changes, treat it as new Evidence and retranscribe or
  reconfirm it.
- Keep the manifest with the TXT and SRT outputs. It must not contain absolute
  local paths.
- A checkpoint is recovery state, not final Evidence. TXT, SRT, and the manifest
  remain the completed deliverables.
- The current manifest records files actually transcribed in the current run.
  When every file is skipped, the old manifest is not rewritten. A future
  version should improve this behavior.
