# Local Transcription

本地工具层只负责从媒体生成 Evidence，不调用 LLM，也不生成最终知识文档。

## Commands

```powershell
lke check
lke transcribe <input-directory> `
  --output <output-directory> `
  --model small `
  --device auto `
  --language zh `
  --chunk-seconds 600 `
  --resume
```

支持 `mp3`、`wav`、`m4a`、`mp4`、`aac`、`flac`、`ogg` 和 `wma`，只扫描输入目录第一层。
同一输入目录中的媒体文件不能使用相同主文件名（例如同时存在 `lesson.wav` 与 `lesson.mp3`），否则 TXT/SRT 和 checkpoint 会冲突，CLI 将拒绝运行。

## Behavior

- 默认模型为 `small`。
- `--device auto` 优先使用 CUDA，不可用时使用 CPU。
- `--device cpu|cuda` 可显式选择；请求 CUDA 但不可用时失败并给出错误。
- `--resume` 默认启用，已有 checkpoint 会跳过。
- TXT 和 SRT 同时存在时默认跳过整个文件。
- `--overwrite` 重新转录并忽略已有完成输出和 checkpoint。
- 完成文件采用原子替换写入，降低中断时留下半文件的风险。

## Deprecated Entry Points

根目录 `audio_transcribe.py` 和 `scripts/audio_transcribe_resumable.py` 暂时保留兼容性，但不再作为正式入口。新功能只进入 `lke transcribe`。
