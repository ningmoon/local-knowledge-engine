# Security Policy

## Supported versions

安全修复仅面向当前 `main` 和最新发布版本。Alpha 阶段不承诺旧版本的长期
安全维护。

请不要在公开 Issue 中粘贴课程内容、Transcript、个人信息、客户资料、密钥或本机绝对路径。

对于代码安全问题，请优先使用仓库的私密安全报告或 Security Advisory 渠道联系维护者。报告应包含受影响版本、复现条件、影响和建议修复方式，但不得附带无关的敏感课程数据。

当前 V1 是本地工具链，不提供网络服务。用户仍需自行保护输入媒体、输出 Evidence、模型缓存和编译后的知识资产。

媒体文件、FFmpeg 解析器和 ML checkpoint 都属于不可信输入边界。只加载
可信来源的模型；不要因为 `weights_only=True` 或本地执行就假定 checkpoint
绝对安全。保持 PyTorch、Whisper 和 FFmpeg 在项目支持的安全版本上。
