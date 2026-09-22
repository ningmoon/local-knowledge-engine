# Environment Setup

## Prerequisites

- Python 3.11+
- FFmpeg（同时包含 `ffmpeg` 和 `ffprobe`）
- 足够的磁盘空间用于 Python 依赖、临时 WAV 和 Whisper 模型缓存

## CPU

```powershell
.\scripts\setup_environment.ps1 -Runtime cpu
```

CPU 是最通用的安装路径，适合 `tiny`、`base` 或 `small`。长录音会明显慢于 GPU。该路径已定义但尚未在独立无 GPU 干净机器上完成全流程验证。

## CUDA

```powershell
.\scripts\setup_environment.ps1 -Runtime cuda
```

当前 CUDA requirements 面向 PyTorch CUDA 12.6 wheel。用户需自行确认 NVIDIA 驱动兼容性。CUDA 是可选加速，不是项目运行前提。

## Model trust

PyTorch 和 Whisper 会加载模型 checkpoint。只使用官方或其他可信来源的模型，
不要运行来源不明、哈希未经核验的 `.pt`、`.pth` 或其他模型文件。项目依赖
固定在 PyTorch 2.13.0，以避开旧版本已公开的 checkpoint 反序列化漏洞。

## Verify

```powershell
.\.venv\Scripts\lke.exe check
```

FFmpeg、PyTorch 或 Whisper 缺失时，转录命令会明确失败。首次使用模型时 Whisper 会下载权重。
