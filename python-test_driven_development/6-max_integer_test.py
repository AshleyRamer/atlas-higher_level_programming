#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittest for max_integer"""

    def test_max_integer(self):
        self.assertIs(list, list)
        self.assertRaises(TypeError, max_integer("string"))
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-8, -6, -2, 0]), 0)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([]), None)

    if __name__ == "__main__":
        """run the main function"""


        unittest.main()
