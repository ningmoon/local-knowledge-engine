# Local Knowledge Engine

Local Knowledge Engine（LKE）是一套面向长课程与培训资料的、本地优先、
证据可追溯、人工可审阅、输出长期可复用的知识编译方法与轻量工具链。

> A local-first, traceable knowledge compilation workflow and lightweight
> toolchain for long-form courses and training materials.

LKE 不是一键式 AI 总结器。它将本地证据生成工具与模型辅助、人工审批的
知识编译方法组合起来：

> Tooling handles evidence. Models perform compilation. Humans approve knowledge.

## 工作流

```text
Long-form Course / Training Material
                ↓
       Local Transcription
                ↓
 Traceable Transcript / Evidence
                ↓
   Knowledge Compilation
                ↓
        Human Review
                ↓
 Durable Markdown Knowledge Asset
```

LKE 适用于长课程、技术培训、系列讲座和其他长时间教学音视频。V1 包含：

- 本地生成 TXT、SRT、checkpoint 和 provenance manifest；
- 可中断恢复的 Whisper 分块转录 CLI；
- 模型无关的 Knowledge Compilation Contract、Prompt 与模板；
- 明确的人工审阅门禁。

V1 不包含 GUI、Web 服务、RAG、向量数据库、云同步或无人监督知识发布。
详细边界见 [Architecture](docs/Architecture.md) 和 [Limitations](docs/Limitations.md)。

## 安装

需要 Python 3.11+、`ffmpeg` 和 `ffprobe`。PowerShell 安装脚本会创建项目内
虚拟环境；CPU 是默认路径，CUDA 是可选加速路径。

```powershell
# CPU
.\scripts\setup_environment.ps1 -Runtime cpu

# NVIDIA CUDA 12.6 wheel
.\scripts\setup_environment.ps1 -Runtime cuda
```

也可手工安装：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-cpu.txt
.\.venv\Scripts\python.exe -m pip install -e .
```

依赖文件将 PyTorch 固定在 `2.13.0`，以避开旧版本已公开的 checkpoint
反序列化安全问题。不要加载来源不可信的模型或 checkpoint；依赖和 FFmpeg
的许可证边界见 [Third-party notices](THIRD_PARTY_NOTICES.md)。

## 使用

```powershell
.\.venv\Scripts\lke.exe check
.\.venv\Scripts\lke.exe transcribe ".\data\raw\my-course" `
  --output ".\data\output\my-course\transcript" `
  --model small `
  --device auto `
  --language zh `
  --resume
```

正式 CLI 默认使用 `small`，自动选择 CPU 或 CUDA，并按分块保存 checkpoint：

```text
transcript/
├── .checkpoints/
├── recording_01.txt
├── recording_01.srt
└── manifest.json
```

`manifest.json` 记录源文件名、SHA256、时长、模型、语言、设备、分块长度、
Whisper 版本和输出文件。详见 [Provenance](docs/Provenance.md)。

## Knowledge Compilation

Knowledge Compilation 不是本地 Python 自动算法，也不由 `lke transcribe`
调用。使用者需要把 Transcript、SRT、manifest、
[Compilation Contract](docs/Knowledge_Compilation.md)、
[标准 Prompt](prompts/knowledge_compilation.md) 和
[输出模板](templates/Course_Knowledge.md) 提供给能够遵循 Contract 的模型。

候选知识文档必须经过 [Human Review](docs/Human_Review.md)；未经审阅的模型
输出不是已批准知识。若使用云端模型，Transcript 将离开本机，必须先确认
授权、保密要求和服务商数据政策。详见 [Privacy](PRIVACY.md)。

## 数据与隐私边界

公开仓库不包含真实课程、音视频、逐字稿、知识产物、运行日志、模型权重或
本机截图。`data/`、常见媒体格式、字幕与 checkpoint 默认被 Git 忽略。

使用者仍需自行确认源材料版权、说话人同意、保密义务与个人信息处理要求。
本地运行不等于内容可以公开。公开示例只能使用自制、合成、Public Domain
或获得明确再分发许可的材料。

## 项目状态

当前版本为 `0.1.0`（Alpha）：

- 16 个依赖无关单元测试覆盖 CLI、配置、媒体发现、checkpoint、SRT、
  manifest 和 mocked transcription 主流程；
- CI 在 Python 3.11 上编译源码并运行单元测试；
- CPU/CUDA 依赖分别声明，CPU 是可移植默认路径；
- 真正的模型推理、不同硬件性能和长媒体边界质量仍需在目标环境验证。

不要把 Alpha 状态理解为生产保证。Whisper 会误识别术语、品牌、数字和
标准号，独立分块也可能造成边界漏词或重复。

## 文档

| 文档 | 作用 |
|---|---|
| [Architecture](docs/Architecture.md) | 五层架构和系统边界 |
| [Workflow](docs/Workflow.md) | 标准端到端流程 |
| [Audio Transcription](docs/Audio_Transcription.md) | CLI 与 Evidence 生成 |
| [Environment Setup](docs/Environment_Setup.md) | CPU/CUDA 安装与验证 |
| [Knowledge Compilation](docs/Knowledge_Compilation.md) | 模型无关 Compilation Contract |
| [Provenance](docs/Provenance.md) | manifest 与来源追踪 |
| [Human Review](docs/Human_Review.md) | 人工审批协议 |
| [Model Guidance](docs/Model_Guidance.md) | 模型选择与数据边界 |
| [Limitations](docs/Limitations.md) | 已知限制与未验证边界 |
| [Release Review](docs/Release_Checklist.md) | 公开发布检查与复核方式 |

参与开发前请阅读 [Contributing](CONTRIBUTING.md) 和
[Code of Conduct](CODE_OF_CONDUCT.md)。安全问题请按
[Security Policy](SECURITY.md) 私密报告。

## License

本仓库原创代码与文档使用 [MIT License](LICENSE)。该许可证不覆盖用户输入、
生成内容、模型权重或第三方组件。完整说明见
[Third-party notices](THIRD_PARTY_NOTICES.md)。

> Evidence is preserved. Knowledge is compiled. Uncertainty is explicit.
> Approval is human. Outputs stay portable.
