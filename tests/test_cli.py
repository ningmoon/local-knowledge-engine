from __future__ import annotations

import unittest

from local_knowledge_engine.cli import build_parser


class CliTests(unittest.TestCase):
    def test_transcribe_defaults_are_portable(self) -> None:
        args = build_parser().parse_args(["transcribe", "input"])
        self.assertEqual(args.model, "small")
        self.assertEqual(args.device, "auto")
        self.assertTrue(args.resume)


if __name__ == "__main__":
    unittest.main()
