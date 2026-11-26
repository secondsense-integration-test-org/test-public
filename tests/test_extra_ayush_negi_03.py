import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.extra_ayush_negi_03 import divide


class DivideTest(unittest.TestCase):
    def test_divide(self) -> None:
        self.assertEqual(divide(6, 3), 2)

    def test_divide_by_zero(self) -> None:
        with self.assertRaises(ValueError):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main()
