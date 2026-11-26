import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.calc import add


class AddTest(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self) -> None:
        self.assertEqual(add(-1, -2), -3)


if __name__ == "__main__":
    unittest.main()
