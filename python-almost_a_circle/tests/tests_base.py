#!/usr/bin/python3
"""test module for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test Base"""

    def test_base_id(self):
        b = Base(12)
        self.assertEqual(b.id, 12)
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_id_number(self):
        b3 = Base(500)
        b4= Base(12790)
        self.assertIsInstance(b3.id, int)
        self.assertIsInstance(b4.id, int)

    def test_base_id_string(self):
        b5 = Base("hello")
        self.assertEqual(b5.id, "hello")

    def test_base_id_empty(self):
        b6 = Base("")
        self.assertEqual(b6.id, "")

if __name__ == "__main__":
    unittest.main()
    