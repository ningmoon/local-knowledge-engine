# Model Guidance

## Required Capabilities

执行 Knowledge Compilation 的模型应能够：

- 读取完整课程上下文，或通过受控分批流程保持全局结构；
- 严格遵守 Compilation Contract；
- 处理长 Transcript、SRT 和来源索引；
- 输出结构化 Markdown；
- 显式标记不确定性；
- 不使用自身知识静默补写课程内容。

## Model Independence

任何能够满足相同 Contract 的高上下文模型都可以执行该工作流。模型或 Agent Adapter 不得复制出另一套规则；规范来源始终是 `docs/Knowledge_Compilation.md`。

“本地优先”首先约束 Source 和 Evidence Tooling。若选择云端模型执行 Knowledge Compilation，Transcript 将离开本机边界；使用者必须确认课程授权、保密要求、服务条款和数据策略允许这样做。需要全程离线时，应选择能够在本地运行且满足 Contract 的模型。

## Context Limit

如果整套课程不能一次放入上下文，应先生成可追溯的分段中间材料，再进行全局结构整合。不能把独立分段摘要直接拼接为最终知识资产。

## External Knowledge

默认关闭联网和外部事实补充。如果用户要求核验，应将“课程声称”和“外部核验结果”分层书写并分别引用来源。
