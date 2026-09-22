# Provenance

**中文** | [English](en/Provenance.md)

## Purpose

可追溯性用于回答：输出来自哪个源文件、源文件是否变化、使用什么模型和参数、何时生成，以及如何回到原始证据。

## Manifest Contract

`lke transcribe` 在输出目录生成 `manifest.json`。每个 source record 至少包含：

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

机器可读 schema 位于 [manifest.schema.json](../templates/manifest.schema.json)。

## Source References

Knowledge Compilation 为每个录音建立稳定编号，例如 `F0`、`F1`。正文引用使用 `[F2 01:23:45]`，来源索引保存编号、真实文件名、时长、主题和边界判断。

## Integrity Rules

- 如果源文件 SHA256 改变，应视为新的 Evidence 并重新转录或重新确认。
- manifest 应与 TXT/SRT 一起保存，不包含本机绝对路径。
- checkpoint 是恢复状态，不是最终 Evidence；完成后仍应以 TXT/SRT/manifest 为交付对象。
- 当前 manifest 只写入本次实际转录的文件；全部文件被跳过时不会重写旧 manifest。该行为将在后续版本完善。
