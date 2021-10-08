"""
This file contains a function that takes 3 edges as inputs and classify what triangle can those
3 edges form.
Author: Shengping Xu
"""

from typing import List


def classify_triangle(a_edge: float, b_edge: float, c_edge: float) -> str:
    """
    Classify if a triangle is a right triangle or not and classify it is a Equilateral, Isosceles
    or a Scalene
    :param a_edge: The first edge
    :param b_edge: The second edge
    :param c_edge: The third edge
    :return: The type of the triangle
    """
    try:
        a_edge = float(a_edge)
        b_edge = float(b_edge)
        c_edge = float(c_edge)
    except ValueError:
        return 'Invalid Input'
    if a_edge <= 0 or b_edge <= 0 or c_edge <= 0:
        return 'Invalid Input'
    edges: List[float] = [a_edge, b_edge, c_edge]
    # Sort the three edges
    edges.sort()
    a_edge, b_edge, c_edge = edges[0], edges[1], edges[2]
    if a_edge + b_edge <= c_edge:
        return 'Not A Triangle'
    # Classify if a triangle is a right triangle
    if round(a_edge ** 2, 2) + round(b_edge ** 2, 2) == round(c_edge ** 2, 2):
        if a_edge == b_edge or b_edge == c_edge or a_edge == c_edge:
            return 'Right Isosceles Triangle'
        return 'Right Scalene Triangle'
    if a_edge == b_edge == c_edge:
        return 'Equilateral Triangle'
    if a_edge == b_edge or b_edge == c_edge or a_edge == c_edge:
        return 'Common Isosceles Triangle'
    return 'Common Scalene Triangle'


# def run_classify_triangle(a_edge: float, b_edge: float, c_edge: float) -> None:
#     """
#     Print the result of classify_triangle function
#     :param a_edge: The first edge
#     :param b_edge: The second edge
#     :param c_edge: The third edge
#     :return: None
#     """
#     print(f'The triangle formed by {a_edge}, {b_edge} and {c_edge} is a'
#           f' {classify_triangle(a_edge, b_edge, c_edge)}')
#
#
# if __name__ == '__main__':
#     run_classify_triangle(4, 3, 2)
#     run_classify_triangle(5, 3, 4)
#     run_classify_triangle(1, 2, 1.732)
#     run_classify_triangle(1, -3, 4)
#     run_classify_triangle(5, 3, 20)
#     run_classify_triangle(5, 3, 'a')
