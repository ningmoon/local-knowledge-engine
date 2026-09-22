# Limitations

[中文](../Limitations.md) | **English**

## Chunk boundaries

V1 divides long media into independent chunks and uses
`condition_on_previous_text=False`. This isolates errors and supports recovery,
but chunk boundaries may introduce:

- missing words;
- duplicated words;
- sentences split across chunks;
- temporary loss of context.

Possible improvements include 5–15 seconds of overlap, time-overlap
deduplication, text-similarity deduplication, and boundary warnings. V1 does not
yet implement these techniques.

## Recognition quality

Whisper may misrecognize technical terms, brands, standard identifiers, units,
and numbers. TXT/SRT output is machine-generated Evidence, not a
human-corrected transcript.

## Device support

The unified CLI provides CPU fallback and a CUDA 12.6 installation path. The
public release has not completed large-model end-to-end regression testing on
every target hardware, driver, and operating-system combination. Validate
installation, memory use, performance, and output quality in the intended
environment.

## Security boundary

Media parsing and model loading process complex third-party formats. Handle only
trusted media or media inspected in an isolated environment, keep FFmpeg,
PyTorch, and Whisper updated, and never load model checkpoints from an unknown
source. LKE is not a sandbox for malicious files.

## Knowledge Compilation

Knowledge Compilation is not deterministic. Reconstructing course structure,
judging duplication, recovering terminology, and assigning evidence levels all
require model understanding and human judgment. The workflow must not be
presented as unattended, production-grade reliability.

## Scope

V1 does not include a GUI, web service, RAG, embeddings, a vector database,
agent runtime, cloud synchronization, knowledge graph, or multi-user system.

“Lightweight toolchain” describes a narrow responsibility boundary, file-based
interfaces, and Markdown output. It does not mean that PyTorch, Whisper, or
model weights are small.
