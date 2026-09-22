# Third-party software and content

Local Knowledge Engine is distributed under the [MIT License](LICENSE). That
license covers this repository's original code and documentation only. It does
not relicense user-provided media, generated transcripts, model weights, or
third-party software.

The project declares these direct dependencies or prerequisites:

| Component | Role | Upstream license |
|---|---|---|
| [OpenAI Whisper](https://github.com/openai/whisper) | Speech recognition and model weights | MIT |
| [PyTorch](https://github.com/pytorch/pytorch) | ML runtime | BSD-style license; see upstream `LICENSE` and bundled notices |
| [NumPy](https://numpy.org/) | Numerical runtime | BSD-3-Clause |
| [pytest](https://github.com/pytest-dev/pytest) | Development/test dependency | MIT |
| [Ruff](https://github.com/astral-sh/ruff) | Development/lint dependency | MIT |
| [FFmpeg](https://ffmpeg.org/legal.html) | External media tool; not redistributed here | LGPL-2.1-or-later, or GPL-2.0-or-later when built with GPL components |

Transitive dependencies retain their own licenses. Before redistributing a
binary environment, model cache, container, or FFmpeg build, review the exact
artifacts and preserve all notices required by their licenses. Codec patent or
media-rights obligations may also depend on jurisdiction and use case.
