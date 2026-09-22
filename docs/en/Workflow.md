# Standard Workflow

[中文](../Workflow.md) | **English**

## 1. Prepare source

Confirm that you have the right to use the course materials. Store original
media in a private local directory. Never copy an unauthorized course into a
public repository.

## 2. Generate Evidence

Run `lke check`, then use `lke transcribe` to produce TXT, SRT, checkpoints, and
`manifest.json`. Verify the file count, media duration, subtitle timeline, and
obvious anomalies.

## 3. Prepare compilation inputs

Provide the model with:

- every TXT file;
- every SRT file;
- `manifest.json`;
- the [Knowledge Compilation Contract](Knowledge_Compilation.md);
- the standard prompt;
- the output template.

The current standard prompt and template live under `prompts/` and `templates/`
at the repository root.

## 4. Compile whole-course knowledge

The model first inventories all materials, determines their order and
boundaries, and then reconstructs the semantic course structure. It must not
concatenate per-file summaries or silently add facts from prior model knowledge.

## 5. Human Review

Review the candidate with the [Human Review Protocol](Human_Review.md).
AI output ≠ approved knowledge.

## 6. Approve and preserve

After review, mark `Course_Knowledge.md` as approved. Preserve the original media
and Evidence so reviewers can investigate disputes, omissions, exact wording,
and timestamps.

## 7. Reuse

Use the approved knowledge asset first. Return to the transcript, SRT, or source
media only when information is missing, disputed, requires exact quotation, or
needs recompilation.
