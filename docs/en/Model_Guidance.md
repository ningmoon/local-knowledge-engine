# Model Guidance

[中文](../Model_Guidance.md) | **English**

## Required capabilities

A model performing Knowledge Compilation should be able to:

- read the complete course context, or preserve global structure through a
  controlled multi-stage process;
- follow the Compilation Contract strictly;
- handle long transcripts, SRT files, and source indexes;
- produce structured Markdown;
- mark uncertainty explicitly;
- avoid silently adding content from its own prior knowledge.

## Model independence

Any long-context model that can satisfy the same Contract may perform the
workflow. A model or Agent Adapter must not create a second set of rules; the
normative source remains `docs/Knowledge_Compilation.md` or its corresponding
English translation.

“Local-first” primarily constrains Source and Evidence Tooling. If a cloud model
is used for Knowledge Compilation, the transcript leaves the local boundary.
Users must verify that course authorization, confidentiality requirements,
service terms, and data policies permit this transfer. If the full process must
remain offline, choose a locally runnable model that can still satisfy the
Contract.

## Context limit

If the complete course does not fit in one context window, first create
traceable intermediate materials in controlled segments and then perform a
global structural integration. Do not concatenate independent segment
summaries and call the result a final knowledge asset.

## External knowledge

Web access and external factual supplementation are disabled by default. When
the user requests verification, separate “what the course claims” from “what
external sources verify” and cite each layer independently.
