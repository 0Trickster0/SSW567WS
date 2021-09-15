# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(-1,1,1),'InvalidInput','-1,1,1 should be invalid')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(201,1,1),'InvalidInput','200,1,1 should be invalid')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1,2,10),'NotATriangle','1,2,10 is not a triangle')

    def testIsocelesTriangle(self):
        self.assertEqual(classifyTriangle(4,5,5),'Isoceles','4,5,5 should be isoceles')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(4,5,6),'Scalene','4,5,5 should be scalene')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

