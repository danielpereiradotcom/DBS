"""Continuous Assessment
Dublin Business School
B8IT105 Programming for Big Data (B8IT105_1819_TME1S)
Lecturer: Darren Redmond
Student: Daniel Pereira (10391381@mydbs.ie)
________________________________________________________________________________

Assignment 1 - A 10 Function Calculator (10%):

This is a test file for the calculator
"""

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    '''
    This is the test class for the calculator
    Args: (unittest.TestCase) : receives the unit test case class
    '''

    def setUp(self):
        self.calc = Calculator()

    def testAddReturnCorrectResult(self):
        self.assertEqual(4, self.calc.Add(2,2))
        self.assertEqual(1, self.calc.Add(0,1))
        self.assertEqual(-2, self.calc.Add(-4,2))
        self.assertEqual(-6, self.calc.Add(-2,-4))
        self.assertEqual(0, self.calc.Add(0,0))

    def testAddReturnValueError(self):
        self.assertRaises(ValueError, self.calc.Add, 'one','two')

    def testCosineReturnCorrectResult(self):
        self.assertEqual(0.65, self.calc.Cosine(6/7))
        self.assertEqual(0.53, self.calc.Cosine(45))
        self.assertEqual(0.53, self.calc.Cosine(-45))
        self.assertEqual(-0.95, self.calc.Cosine(60))
        self.assertEqual(1, self.calc.Cosine(0))

    def testCoineReturnValueError(self):
        self.assertRaises(ValueError, self.calc.Cosine, 'thirteen')

    def testDivideReturnCorrectResult(self):
        self.assertEqual(1, self.calc.Divide(1,1))
        self.assertEqual(0.5, self.calc.Divide(1,2))
        self.assertEqual(1, self.calc.Divide(2,2))
        self.assertEqual(2, self.calc.Divide(4,2))
        self.assertEqual(10, self.calc.Divide(20,2))
        self.assertEqual(0, self.calc.Divide(0,4))
        self.assertEqual(-1, self.calc.Divide(-2,2))
        self.assertEqual(0.75, self.calc.Divide(-3,-4))
        self.assertNotEqual(-12, self.calc.Divide(-3,-4))

    def testDivideReturnValueError(self):
        self.assertRaises(ValueError, self.calc.Divide, 'seven', 'eight')

    def testDivideReturnException(self):
        self.assertRaises(Exception, self.calc.Divide, 3,0)

    def testLogBase10ReturnCorrectResult(self):
        self.assertEqual(0, self.calc.LogBase10(1))
        self.assertEqual(0.30, self.calc.LogBase10(2))
        self.assertEqual(1, self.calc.LogBase10(10))
        self.assertEqual(2, self.calc.LogBase10(100))
        self.assertEqual(-1, self.calc.LogBase10(0.1))
        self.assertEqual(-2, self.calc.LogBase10(0.01))

    def testLogBase10ReturnException(self):
        self.assertRaises(Exception, self.calc.LogBase10, 0)
        self.assertRaises(Exception, self.calc.LogBase10, -2)

    def testLogBase10ReturnValueError(self):
        self.assertRaises(ValueError, self.calc.LogBase10, 'fifteen')

    def testMultiplyReturnCorrectResult(self):
        self.assertEqual(1, self.calc.Multiply(1,1))
        self.assertEqual(2, self.calc.Multiply(1,2))
        self.assertEqual(4, self.calc.Multiply(2,2))
        self.assertEqual(10, self.calc.Multiply(2,5))
        self.assertEqual(0, self.calc.Multiply(0,4))
        self.assertEqual(-4, self.calc.Multiply(-2,2))
        self.assertEqual(12, self.calc.Multiply(-3,-4))
        self.assertNotEqual(-12, self.calc.Multiply(-3,-4))

    def testMultiplyReturnValueError(self):
        self.assertRaises(ValueError, self.calc.Multiply, 'five', 'six')

    def testPowerReturnCorrectResult(self):
        self.assertEqual(1, self.calc.Power(1,1))
        self.assertEqual(1, self.calc.Power(2,0))
        self.assertNotEqual(0, self.calc.Power(2,0))
        self.assertEqual(4, self.calc.Power(2,2))
        self.assertEqual(16, self.calc.Power(2,4))
        self.assertEqual(4, self.calc.Power(-2,2))
        self.assertEqual(0.25, self.calc.Power(2,-2))

    def testPowerReturnValueError(self):
        self.assertRaises(ValueError, self.calc.Power, 'nine', 'ten')

    def testSquareRootReturnCorrectResult(self):
        self.assertEqual(1, self.calc.SquareRoot(1))
        self.assertEqual(0, self.calc.SquareRoot(0))
        self.assertEqual(5, self.calc.SquareRoot(25))
        self.assertEqual(9, self.calc.SquareRoot(81))

    def testSquareRootReturnTypeError(self):
        self.assertRaises(ValueError, self.calc.SquareRoot, 'eleven')

    def testSquareRootReturnValueError(self):
        self.assertRaises(Exception, self.calc.SquareRoot, -9)

    def testSineReturnCorrectResult(self):
        self.assertEqual(0.28, self.calc.Sine(2/7))
        self.assertEqual(0.85, self.calc.Sine(45))
        self.assertEqual(-0.85, self.calc.Sine(-45))
        self.assertEqual(-0.3, self.calc.Sine(60))
        self.assertEqual(0, self.calc.Sine(0))

    def testSineReturnValueError(self):
        self.assertRaises(ValueError, self.calc.Sine, 'twelve')

    def testSubtractReturnCorrectResult(self):
        self.assertEqual(1, self.calc.Subtract(3,2))
        self.assertEqual(3, self.calc.Subtract(3,0))
        self.assertEqual(0, self.calc.Subtract(5,5))
        self.assertEqual(-2, self.calc.Subtract(0,2))
        self.assertEqual(-2, self.calc.Subtract(2,4))
        self.assertEqual(1, self.calc.Subtract(-2,-3))

    def testSubtractReturnValueError(self):
        self.assertRaises(ValueError, self.calc.Subtract, 'three', 'four')

    def testTangentReturnCorrectResult(self):
        self.assertEqual(0.35, self.calc.Tangent(2/6))
        self.assertEqual(1.62, self.calc.Tangent(45))
        self.assertEqual(-1.62, self.calc.Tangent(-45))
        self.assertEqual(0.32, self.calc.Tangent(60))
        self.assertEqual(0, self.calc.Tangent(0))

    def testSineReturnValueError(self):
        self.assertRaises(ValueError, self.calc.Tangent, 'fourteen')

# execute the unit test
if __name__ == '__main__':
    unittest.main()

