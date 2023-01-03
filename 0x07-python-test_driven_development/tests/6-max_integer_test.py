#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        # Test empty list
        self.assertEqual(max_integer([]), None)
        # Test negative numbers
        self.assertEqual(max_integer([-1, -4, -6, -5]), -1)
        self.assertEqual(max_integer([0]), 0)
