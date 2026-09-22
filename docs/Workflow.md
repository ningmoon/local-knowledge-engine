# Standard Workflow

## 1. Prepare Source

确认课程材料具有合法使用权限，将原始媒体放在本地私有目录。不要将未授权课程复制到公开仓库。

## 2. Generate Evidence

运行 `lke check`，再通过 `lke transcribe` 生成 TXT、SRT、checkpoint 和 `manifest.json`。检查文件数量、音频时长、字幕时间轴与明显异常。

## 3. Prepare Compilation Inputs

向模型提供：

- 全部 TXT；
- 全部 SRT；
- `manifest.json`；
- [Knowledge Compilation Contract](Knowledge_Compilation.md)；
- [标准 Prompt](../prompts/knowledge_compilation.md)；
- [输出模板](../templates/Course_Knowledge.md)。

## 4. Compile Whole-course Knowledge

模型先盘点全部材料、判断顺序和边界，再重建课程语义结构。不得把逐文件摘要简单拼接，也不得用模型已有知识静默补写课程内容。

## 5. Human Review

按 [Human Review](Human_Review.md) 检查候选文档。AI output ≠ approved knowledge。

## 6. Approve and Preserve

审阅通过后，将 `Course_Knowledge.md` 标记为已批准知识入口。保留原始媒体和 Evidence，以便争议、缺失、原话和时间定位查证。

## 7. Reuse

后续优先读取知识资产，只有在信息不足、存在争议、需要原话或重新编译时返回 Transcript/SRT/原音频。
