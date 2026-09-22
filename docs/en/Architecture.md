# Architecture

[中文](../Architecture.md) | **English**

## Positioning

Local Knowledge Engine is a method, a lightweight toolchain, and a standard
workflow—not a complete knowledge-base product. The file system is the stable
interface between Evidence Tooling and model-assisted Knowledge Compilation.
The code does not import or bind to an agent framework, model service, or cloud
SDK.

```text
Local Knowledge Engine
├── Evidence Tooling
├── Knowledge Compilation Specification
├── Standard Workflow
├── Human Review Protocol
└── Optional Adapters
```

Any future Skill is only a workflow adapter: `Skill ⊂ Workflow / Toolchain`.

## Five layers

### Layer 0 — Source

Inputs include audio, video, and course materials. Source files are the ultimate
evidence and must not be replaced by transcription output. They remain local by
default and must not enter Git.

### Layer 1 — Evidence

The local toolchain generates TXT, SRT, timestamps, SHA256 hashes, manifests,
and checkpoints. This layer aims to be as deterministic, verifiable, and
traceable as possible. It neither summarizes knowledge nor calls an LLM.

### Layer 2 — Knowledge Compilation

A capable model reads the complete transcript set, Compilation Contract,
prompt, template, and provenance metadata, then produces a candidate
`Course_Knowledge.md`. This is a model-assisted workflow, not an automated local
Python algorithm.

### Layer 3 — Human Review

A human verifies numbers, units, standard identifiers, brands, technical terms,
causal claims, model inferences, uncertainties, and source references.

### Layer 4 — Knowledge Asset

`Course_Knowledge.md` becomes a final knowledge asset only after human approval.
It remains plain Markdown and can feed Git, documentation sites, search, RAG,
or knowledge graphs, but those consumer systems are outside V1.

## Stable interface

The cross-layer interface consists of open files:

```text
Transcript
SRT
manifest.json
Compilation Contract
Prompt
Template
Course_Knowledge.md
```

This keeps the method independent of any model vendor, agent standard, or
proprietary knowledge base.
