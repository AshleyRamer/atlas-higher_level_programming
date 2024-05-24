#!/usr/bin/python3
"""test module for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test Base"""

    def test_base_id(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 2)

    def test_base_id_type(self):
        b = Base(500)
        b1= Base()
        self.assertIsInstance(b.id, int)
        self.assertIsInstance(b1.id, int)
