# Changelog

本项目处于 V1 Alpha 阶段。

## Unreleased

- 冻结本地优先、可追溯、人工审阅的产品定位。
- 建立五层架构、Knowledge Compilation Contract 和 Human Review Protocol。
- 建立模型无关 Prompt、知识模板和 manifest schema。
- 新增包化 `lke check` / `lke transcribe` CLI。
- 将 resume、checkpoint、原子输出和 manifest 合并到统一内核。
- 分离 CPU、CUDA 和开发依赖。
- 新增基础单元测试和 CI。
- 建立不继承内部历史的公开仓库边界，排除真实课程与私人运行资料。
- 添加 MIT 许可证、隐私政策和第三方许可证说明。
- 将 PyTorch 基线提升至 2.13.0，并将 CUDA wheel 更新至 12.6。
