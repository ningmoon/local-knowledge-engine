from __future__ import annotations

import unittest

from local_knowledge_engine.config import resolve_device


class ResolveDeviceTests(unittest.TestCase):
    def test_auto_selects_cpu_without_cuda(self) -> None:
        self.assertEqual(resolve_device("auto", False), "cpu")

    def test_auto_selects_cuda_when_available(self) -> None:
        self.assertEqual(resolve_device("auto", True), "cuda")

    def test_explicit_cpu_works_with_cuda_available(self) -> None:
        self.assertEqual(resolve_device("cpu", True), "cpu")

    def test_explicit_cuda_fails_when_unavailable(self) -> None:
        with self.assertRaises(RuntimeError):
            resolve_device("cuda", False)


if __name__ == "__main__":
    unittest.main()
