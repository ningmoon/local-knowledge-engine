# Open Source Release Review

本文件记录公开仓库的发布门禁。检查针对当前工作树和即将创建的公开历史；
任何新增文件都必须重新执行相关检查。

## 已完成

- [x] 从干净目录建立公开副本，不继承内部仓库 Git 历史。
- [x] 排除真实音视频、Transcript、checkpoint、知识产物、运行日志和截图。
- [x] 排除内部验证统计、内部审计记录和一次性 Agent 调研稿。
- [x] 扫描当前公开文件中的常见密钥模式、私人邮箱、本机绝对路径和内部文件名。
- [x] `data/`、媒体、字幕、模型权重、环境文件和常见私钥格式默认加入 `.gitignore`。
- [x] 添加 MIT `LICENSE`，并在 `pyproject.toml` 中声明许可证。
- [x] 添加第三方依赖、FFmpeg、模型权重和用户内容的许可证边界说明。
- [x] 将 PyTorch 从存在公开安全公告的旧版本提升至 `2.13.0`。
- [x] 将 pytest 下限提升至修复 CVE-2025-71176 的 `9.0.3`。
- [x] 运行源码编译、16 个单元测试和 `git diff --check`。
- [x] dry-run 验证 CPU、CUDA 和开发依赖可以解析。
- [x] 使用 OSV 复查实际解析出的直接依赖版本，当前未返回匹配公告。
- [x] 构建 wheel，并确认包内包含 MIT `LICENSE`、元数据与 CLI entry point。

## 发布者仍需确认

- [ ] 确认提交者确实拥有本仓库原创代码和文档的 MIT 授权权利。
- [ ] 在干净 CPU 环境安装 `requirements-cpu.txt` 并运行 `lke check`。
- [ ] 在目标 NVIDIA 环境安装 CUDA 12.6 依赖并运行短媒体端到端测试。
- [ ] 如加入公开示例，保存音频来源、说话人同意与再分发许可证记录。
- [ ] 创建任何 Release 附件前，再扫描压缩包、wheel、容器和模型缓存。
- [ ] 将仓库可见性改为 public 前，检查远端分支、tag、release、Actions 日志和附件。

## 每次发布的检查命令

```powershell
$env:PYTHONPATH = "src"
python -m compileall -q src tests
python -m unittest discover -s tests -v
git diff --check
git ls-files
```

建议同时使用专业 secret scanner 和依赖漏洞扫描器。扫描结果只是证据之一，
不能替代版权、隐私、合同或出口管制方面的人工判断。

> 本清单不是法律意见。代码权属、媒体版权、个人信息、保密义务和第三方
> 许可证应由权利人或合格专业人士最终确认。
