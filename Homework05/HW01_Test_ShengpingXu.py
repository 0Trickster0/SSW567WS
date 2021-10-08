"""
This is a test file for homework 01
Author: Shengping Xu
"""

from HW01_ShengpingXu import *
import unittest


class ClassifyTriangleTest(unittest.TestCase):
    """Test class of the classify_triangle function"""
    def test_invalid_triangle(self) -> None:
        """Test cases of invalid triangles"""
        self.assertEqual(classify_triangle(1, 1, 10), 'Not A Triangle')
        self.assertEqual(classify_triangle(0.1, 0.1, 0.99), 'Not A Triangle')
        self.assertEqual(classify_triangle('a', 'b', 1), 'Invalid Input')
        self.assertEqual(classify_triangle(0, 0, 1), 'Invalid Input')

    def test_right_triangle(self) -> None:
        """Test cases of right triangles"""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right Scalene Triangle')
        self.assertEqual(classify_triangle(5, 4, 3), 'Right Scalene Triangle')
        self.assertEqual(classify_triangle(1, 1.732, 2), 'Right Scalene Triangle')
        self.assertEqual(classify_triangle(2, 2.828, 2), 'Right Isosceles Triangle')

    def test_common_triangle(self) -> None:
        """Test cases of common triangles"""
        self.assertEqual(classify_triangle(2, 2, 2), 'Equilateral Triangle')
        self.assertEqual(classify_triangle(3, 3, 2), 'Common Isosceles Triangle')
        self.assertEqual(classify_triangle(0.2, 0.3, 0.3), 'Common Isosceles Triangle')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)