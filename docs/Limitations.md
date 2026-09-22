# Limitations

**中文** | [English](en/Limitations.md)

## Chunk Boundaries

V1 将长媒体切成独立分块，并使用 `condition_on_previous_text=False`。这有助于隔离错误和恢复任务，但边界可能出现：

- 漏词；
- 重复；
- 句子跨块断裂；
- 短暂上下文丢失。

候选改进包括 5–15 秒 overlap、时间重叠去重、文本相似度去重和 boundary warning。V1 尚未实现这些算法。

## Recognition Quality

Whisper 可能误识别专业术语、品牌、标准号、单位和数字。TXT/SRT 是机器生成 Evidence，不等同于经过人工校订的逐字稿。

## Device Support

统一 CLI 提供 CPU fallback 和 CUDA 12.6 安装文件，但公开版本尚未在所有目标硬件、驱动和操作系统组合上完成大型模型端到端回归。发布者应在自己的目标环境验证安装、显存、性能和输出质量。

## Security boundary

媒体解析和模型加载会处理复杂的第三方格式。仅处理可信或经过隔离检查的
媒体，保持 FFmpeg、PyTorch 和 Whisper 更新，并且不要加载来源不明的模型
checkpoint。LKE 不是恶意文件沙箱。

## Knowledge Compilation

Knowledge Compilation 不是确定性算法。课程结构重建、重复判断、术语恢复和证据等级需要模型理解与人工判断，不能宣称无人监督生产级可靠。

## Scope

V1 不包含 GUI、Web 服务、RAG、Embedding、向量数据库、Agent runtime、云同步、知识图谱和多用户系统。

“轻量工具链”描述的是较小的职责边界、文件接口和 Markdown 输出，并不表示 PyTorch、Whisper 或模型权重本身轻量。
