# Knowledge Compilation Contract

[中文](../Knowledge_Compilation.md) | **English**

## Purpose

Knowledge Compilation turns the traceable Evidence for a complete long-form
course into a structured, durable candidate Markdown knowledge asset. A capable
model assists the process and a human approves the result. It is neither a local
Python algorithm nor an unattended one-click summary.

## Input contract

Allowed inputs are:

- course TXT transcripts;
- corresponding SRT files and timestamps;
- `manifest.json`;
- course metadata explicitly supplied by the user;
- this Contract, the standard prompt, and the output template.

By default, do not browse the web or use model memory to silently correct the
course. If the task explicitly permits external verification, identify external
material separately and never present it as course content.

## Evidence contract

1. Never present prior model knowledge as course content.
2. Never add facts, causes, or conclusions that are absent from the transcript.
3. Distinguish explicit course content, instructor views, course examples,
   learner speculation, model inference, and content that cannot be confirmed.
4. Whenever possible, link critical conclusions, important examples, disputes,
   and uncertainties to stable source identifiers and timestamps, such as
   `[F2 01:23:45]`.
5. Mark brands, standards, product models, units, exact numbers, and unusual
   technical expressions as `[TO CONFIRM]` when the Evidence is insufficient.
6. Preserve explicit instructor uncertainty, inability to answer, and disputed
   topics as boundaries of the course's authority.

For Chinese-language output, use the equivalent marker `[待确认]`.

## Compilation contract

1. Read the complete course before designing the final section structure. Do not
   summarize each file independently and concatenate the results.
2. Reconstruct the course semantically rather than turning filenames, recording
   counts, or dates into artificial sections.
3. Remove greetings, connection checks, and spoken repetition that adds no
   knowledge.
4. Merge duplicated slices while preserving every newly introduced condition,
   exception, example, or derivation.
5. Preserve essential context, applicability conditions, limitations,
   counterexamples, failure cases, and course boundaries.
6. Do not remove conditions for brevity or change meaning for fluency.
7. Place consolidated Q&A content under the relevant knowledge topic. Put
   unconfirmed answers under uncertainties or course boundaries.
8. Build a stable source map that records real filenames, duration, primary
   topics, and boundary decisions.

## Boundary rules

Classify adjacent files as at least one of: confirmed duplicate, suspected
duplicate, direct continuation, or normal transition. Remove content as a
duplicate only when sentence order, examples, numbers, and time relationships
provide enough evidence that the recording is the same. When evidence is weak,
preserve the material and record the uncertainty.

## Output contract

Produce one candidate file by default:

```text
Course_Knowledge.md
```

It should contain:

- a status label such as candidate or human-approved;
- course overview, scope, and intended audience;
- a knowledge map;
- main content reconstructed by meaning;
- principles, methods, conditions, limitations, examples, and common mistakes;
- items to confirm and boundaries of the course's authority;
- a stable source index and key source references;
- compilation and human-review records.

Adapt the structure to the actual course. Never invent knowledge merely to fill
the template.

## Uncertainty contract

Use `[TO CONFIRM]` consistently when:

- the transcript is ambiguous or likely mistranscribed;
- a term, number, unit, brand, standard, or product model lacks sufficient
  support inside the course;
- file order, duplicate boundaries, or context is incomplete;
- the course contradicts itself;
- a statement is model inference rather than direct Evidence.

Do not hide uncertainty behind fluent text that merely sounds plausible. Keep
the marker until human review resolves it.

## Completion gate

After producing the candidate, stop and wait for human review. The document may
be promoted to a final Knowledge Asset only after it passes
[Human Review](Human_Review.md).
