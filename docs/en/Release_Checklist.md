# Open Source Release Review

[中文](../Release_Checklist.md) | **English**

This file records the release gates for the public repository. The checks apply
to the current working tree and public history. Repeat the relevant checks
whenever files are added.

## Completed

- [x] Created the public copy from a clean directory without inheriting the
      private repository's Git history.
- [x] Excluded real media, transcripts, checkpoints, knowledge outputs, runtime
      logs, and unredacted screenshots.
- [x] Excluded internal validation statistics, internal audit records, and
      one-off agent research drafts.
- [x] Scanned public files for common secret patterns, private email addresses,
      absolute local paths, and internal filenames.
- [x] Added `data/`, media, subtitles, model weights, environment files, and
      common private-key formats to `.gitignore` by default.
- [x] Added an MIT `LICENSE` and declared it in `pyproject.toml`.
- [x] Documented license boundaries for dependencies, FFmpeg, model weights, and
      user content.
- [x] Upgraded PyTorch from an older version covered by public advisories to
      `2.13.0`.
- [x] Raised the pytest lower bound to `9.0.3`, which fixes CVE-2025-71176.
- [x] Compiled the source, ran 16 unit tests, and ran `git diff --check`.
- [x] Confirmed CPU, CUDA, and development dependency resolution with dry runs.
- [x] Queried OSV for the resolved direct-dependency versions; no current matches
      were returned at the time of review.
- [x] Built a wheel and confirmed that it contains the MIT `LICENSE`, package
      metadata, and CLI entry point.

## Publisher confirmations

- [x] The publisher confirmed the right to release the repository's original
      code and documentation under the MIT License.
- [ ] Install `requirements-cpu.txt` in a clean CPU environment and run
      `lke check`.
- [ ] Install the CUDA 12.6 dependencies on the target NVIDIA environment and
      complete a short-media end-to-end test.
- [ ] If a public example is added, retain its source record, speaker consent,
      and redistribution license.
- [ ] Before creating release assets, rescan archives, wheels, containers, and
      model caches.
- [ ] Before changing repository visibility to public, inspect remote branches,
      tags, releases, Actions logs, and attached assets.

## Checks for every release

```powershell
$env:PYTHONPATH = "src"
python -m compileall -q src tests
python -m unittest discover -s tests -v
git diff --check
git ls-files
```

Use a dedicated secret scanner and dependency-vulnerability scanner when
possible. Automated scan results are evidence, not a substitute for human
review of copyright, privacy, contracts, or export controls.

> This checklist is not legal advice. Code ownership, media rights, personal
> data, confidentiality duties, and third-party licenses require final review
> by the relevant rights holder or a qualified professional.
