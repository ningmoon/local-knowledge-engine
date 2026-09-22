# Architecture

## Positioning

Local Knowledge Engine 是“方法论 + 轻量工具链 + 标准工作流”，不是完整知识库产品。文件系统是 Evidence Tooling 与模型辅助 Knowledge Compilation 之间的稳定接口；代码不导入或绑定任何 Agent、模型服务或云端 SDK。

```text
Local Knowledge Engine
├── Evidence Tooling
├── Knowledge Compilation Specification
├── Standard Workflow
├── Human Review Protocol
└── Optional Adapters
```

任何未来 Skill 都只是工作流 Adapter：`Skill ⊂ Workflow / Toolchain`。

## Five Layers

### Layer 0 — Source

输入包括音频、视频和课程材料。源文件是最终证据，不应被转录结果替代。默认保存在本地且不进入 Git。

### Layer 1 — Evidence

本地工具链负责生成 TXT、SRT、时间戳、SHA256、manifest 和 checkpoint。目标是尽量确定、可验证、可追溯；该层不总结知识，也不调用 LLM。

### Layer 2 — Knowledge Compilation

高理解模型读取整套 Transcript、Compilation Contract、Prompt、Template 和 provenance metadata，生成候选 `Course_Knowledge.md`。它是 model-assisted workflow，不是本地 Python 自动算法。

### Layer 3 — Human Review

人工核验数字、单位、标准号、品牌、专业术语、因果结论、模型推断、不确定内容和来源定位。

### Layer 4 — Knowledge Asset

只有人工批准后，`Course_Knowledge.md` 才成为最终知识资产。它保持为普通 Markdown，可进入 Git、文档站、搜索、RAG 或知识图谱，但这些消费系统不属于 V1。

## Stable Interface

跨层接口是开放文件：

```text
Transcript
SRT
manifest.json
Compilation Contract
Prompt
Template
Course_Knowledge.md
```

这使方法不依赖某个模型供应商、Agent 标准或专有知识库。
