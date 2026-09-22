# Contributing

感谢参与 Local Knowledge Engine。贡献应保持 V1 边界：本地 Evidence Tooling、Knowledge Compilation 规范、Human Review 和可移植 Markdown 资产。

## Development Setup

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

## Contribution Rules

- 不提交真实课程、私人音视频、未授权 Transcript、客户资料或模型缓存。
- 测试使用自制、合成、Public Domain 或明确授权的材料。
- 新 CLI 行为必须同时更新测试和文档。
- Knowledge Compilation 规则只在 `docs/Knowledge_Compilation.md` 定义；Prompt 和 Adapter 引用它，不复制另一套 Contract。
- 不在 Evidence Tooling 中绑定特定 LLM、Agent SDK 或云端 API。
- GUI、RAG、数据库和 Agent runtime 不属于当前 V1。

提交 Pull Request 前运行单元测试和 `git diff --check`，并说明验证范围与未验证项。
