# Environment Setup

[中文](../Environment_Setup.md) | **English**

## Prerequisites

- Python 3.11+
- FFmpeg, including both `ffmpeg` and `ffprobe`
- Sufficient disk space for Python dependencies, temporary WAV files, and the
  Whisper model cache

## CPU

```powershell
.\scripts\setup_environment.ps1 -Runtime cpu
```

CPU is the most portable path and is best suited to the `tiny`, `base`, or
`small` models. Long recordings will be substantially slower than on a GPU.
This path is defined but has not yet completed a full clean-machine validation
on a separate system without a GPU.

## CUDA

```powershell
.\scripts\setup_environment.ps1 -Runtime cuda
```

The current CUDA requirements target the PyTorch CUDA 12.6 wheel. Users must
verify NVIDIA driver compatibility for their own systems. CUDA is optional
acceleration, not a project prerequisite.

## Model trust

PyTorch and Whisper load model checkpoints. Use only official or otherwise
trusted models. Do not run `.pt`, `.pth`, or other model files from an unknown
source or with an unverified hash. The project pins PyTorch 2.13.0 to avoid
publicly disclosed checkpoint-deserialization vulnerabilities in older
versions.

## Verify

```powershell
.\.venv\Scripts\lke.exe check
```

The transcription command fails clearly when FFmpeg, PyTorch, or Whisper is
missing. Whisper downloads model weights on first use.
