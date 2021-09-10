"""
This file contains a function that takes 3 edges as inputs and classify what triangle can those
3 edges form.
Author: Shengping Xu
"""

from typing import List
import unittest


def classify_triangle(a: float, b: float, c: float) -> str:
    """
    This function takes 3 edges as inputs and return the type of the
    inputted triangle.
    """
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return 'Invalid Input'
    if a <= 0 or b <= 0 or c <= 0:
        return 'Invalid Input'
    edges: List[float] = [a, b, c]
    # Sort the three edges
    edges.sort()
    a, b, c = edges[0], edges[1], edges[2]
    if a + b <= c:
        return 'Not A Triangle'
    # Classify if a triangle is a right triangle
    if round(a ** 2, 2) + round(b ** 2, 2) == round(c ** 2, 2):
        if a == b or b == c or a == c:
            return 'Right Isosceles Triangle'
        else:
            return 'Right Scalene Triangle'
    else:
        if a == b == c:
            return 'Equilateral Triangle'
        elif a == b or b == c or a == c:
            return 'Common Isosceles Triangle'
        else:
            return 'Common Scalene Triangle'


def run_classify_triangle(a: float, b: float, c: float) -> None:
    print(f'The triangle formed by {a}, {b} and {c} is a {classify_triangle(a, b, c)}')


if __name__ == '__main__':
    run_classify_triangle(4, 3, 2)
    run_classify_triangle(5, 3, 4)
    run_classify_triangle(1, 2, 1.732)
    run_classify_triangle(1, -3, 4)
    run_classify_triangle(5, 3, 20)
    run_classify_triangle(5, 3, 'a')
