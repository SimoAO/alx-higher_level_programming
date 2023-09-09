#!/usr/bin/python3
"""Unittest for max_integer([..]).
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    
    """This function tests for ordered list"""
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    """This function tests for unordered list"""
    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
    
    """This function tests for one integer"""
    def test_one_integer(self):
        self.assertEqual(max_integer([5]), 5)
    
    """This function tests for an empty list"""
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
    
    """This function tests for reversed list"""
    def test_reversed_list(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
    
    """This function tests for identical integerss"""
    def test_identical_integers(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)
    
    """This function tests for a list of strings"""
    def test_list_strings(self):
        self.assertEqual(max_integer(['z', 'e', 'l', 'a']), 'a')

    """This function tests for raising error when None is passed"""
    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    """This function tests for True"""
    def test_True(self):
        with self.assertRaises(TypeError):
            max_integer(True)

if __name__ == '__main__':
    unittest.main()
