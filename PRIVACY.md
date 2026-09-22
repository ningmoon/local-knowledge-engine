# Privacy and data handling

Local Knowledge Engine processes media locally by default, but local execution
does not make the input safe to publish. Audio, video, transcripts, subtitles,
checkpoints, manifests, logs, and compiled knowledge may contain personal,
confidential, copyrighted, or otherwise restricted information.

## Repository boundary

- `data/` is ignored by Git and is reserved for local inputs and outputs.
- Public examples must be synthetic, self-created, Public Domain, or covered by
  explicit redistribution permission.
- Do not commit model caches, absolute local paths, private filenames,
  transcripts, customer material, credentials, or screenshots of private runs.
- `manifest.json` stores source filenames and hashes. Treat it as sensitive when
  filenames themselves reveal identities, projects, or business context.

## Cloud model use

The transcription tool does not upload media. Knowledge Compilation is a
separate workflow. If a cloud model is used for that stage, the supplied
transcripts and metadata leave the local boundary. Confirm consent, contractual
permissions, retention settings, and the provider's data terms first.

## Before publishing an output

Confirm the rights to the source material, speaker consent where applicable,
the absence or lawful handling of personal data, and the accuracy of redaction.
Machine-generated transcripts and summaries require human review.
