"""Continuous Assessment
Dublin Business School
B8IT105 Programming for Big Data (B8IT105_1819_TME1S)
Lecturer: Darren Redmond
Student: Daniel Pereira (10391381@mydbs.ie)
________________________________________________________________________________

Assignment 1 - A 10 Function Calculator (10%):
Based on the Calculator Example in the class lectures and practical you are 
expected to improve upon the calculator class and testsuite to deliver 
functionality and associated testsuites for 10 functions that one would expect 
to find on a scientific calculator.

Please ensure your code is in calculator.py and test_calculator.py and that they run
That your code is properly formatted and documented with sufficient tests to cover 
possible scenarios.
"""
import os
import math

# Class Calculator
class Calculator(object):
    '''
    This class represents a calculator, the methods are:
    Add 
    Cosine
    Divide
    LogBase10
    Multiply
    Power
    Sine
    SquareRoot
    Subtract
    Tangent
    '''

    def Add(self, number1, number2):
        '''
        This method add two numbers
        E.g. 1 + 2 = 3
        Args:
            number1 (number): the first number
            number2 (number): the second number
        Returns:
            (float) : the sum of two numbers
        Exceptions:
            ValueError : return message 'The arguments must be numbers'
        '''
        try:
            return float(number1) + float(number2)
        except ValueError:
            raise ValueError("The arguments must be numbers")

    def Cosine(self, number):
        '''
        This method returns the cosine of a radians
        Args:
            number (number): the radians number
        Returns:
            (float) : the cosine of radians rounded to two digits
        Exceptions:
            ValueError : return message 'The argument must be number'
        '''
        try:
            return round(math.cos(float(number)),2)
        except ValueError:
            raise ValueError("The arguments must be numbers")

    def Divide(self, number1, number2):
        '''
        This method divides two numbers
        E.g. 1 / 2 = 0.5
        Args:
            number1 (number): the first number
            number2 (number): the divisor number
        Returns:
            (float) : the result of first number divided by the second number
        Exceptions:
            ValueError : return message 'The arguments must be numbers'
            ZeroDivisionError : return message 'The second number cannot be zero'
        '''
        try:
            return float(number1) / float(number2)
        except ValueError:
            raise ValueError("The arguments must be numbers")
        except ZeroDivisionError:
            raise Exception("The second number cannot be zero")

    def LogBase10(self, number):
        '''
        This method returns the base 10 logarithm of a number
        E.g. Log base-10 of 10 = 1
        Args:
            number (number): the number
        Returns:
            (float) : the calculate logarithm base 10==
        Exceptions:
            ValueError : return message 'The argument must be number'
            Exception : return message 'The argument must be positive'
        '''
        try:
            if (float(number) <= 0):
                raise Exception("The argument must be positive")
            return round(math.log10(float(number)),2)
        except ValueError:
            raise ValueError("The arguments must be numbers")

    def Multiply(self, number1, number2):
        '''
        This method multiplies two numbers
        E.g. 1 * 2 = 2
        Args:
            number1 (number): the first number
            number2 (number): the second number
        Returns:
            (float) : the result of two numbers multiplied
        Exceptions:
            ValueError : return message 'The arguments must be numbers'
        '''
        try:
            return float(number1) * float(number2)
        except ValueError:
            raise ValueError("The arguments must be numbers")

    def Power(self, number1, number2):
        '''
        This method calculates a number elevated to a power of a second number
        E.g. 2 ** 2 = 4
        Args:
            number1 (number): the first number
            number2 (number): the exponent number
        Returns:
            (float) : the result of first number divided by the second number
        Exceptions:
            ValueError : return message 'The arguments must be numbers'
        '''
        try:
            return float(number1) ** float(number2)
        except ValueError:
            raise ValueError("The arguments must be numbers")

    def Sine(self, number):
        '''
        This method returns the sine of a radians
        Args:
            number (number): the radians number
        Returns:
            (float) : the sine of radians rounded to two digits
        Exceptions:
            ValueError : return message 'The argument must be number'
        '''
        try:
            return round(math.sin(float(number)),2)
        except ValueError:
            raise ValueError("The arguments must be numbers")

    def Subtract(self, number1, number2):
        '''
        This method subtract two numbers
        E.g. 2 - 1 = 1
        Args:
            number1 (number): the first number
            number2 (number): the subtractor number
        Returns:
            (float) : the result of first number minus the secod number
        Exceptions:
            ValueError : return message 'The arguments must be numbers'
        '''
        try:
            return float(number1) - float(number2)
        except ValueError:
            raise ValueError("The arguments must be numbers")

    def SquareRoot(self, number):
        '''
        This method returns the square root of a number
        E.g. square root of 4 = 2
        Args:
            number (number): the number to calculate the square root
        Returns:
            (float) : the square root of number
        Exceptions:
            ValueError : return message 'The argument must be a number'
            Exception : return message 'The number must be positive'
        '''
        try:
            if (float(number) < 0):
                raise Exception("The number must be positive")
            return math.sqrt(float(number))
        except ValueError:
            raise ValueError("The argument must be a number")

    def Tangent(self, number):
        '''
        This method returns the tangent of radians
        Args:
            number (number): the radian number
        Returns:
            (float) : the sine of radians rounded to two digits
        Exceptions:
            ValueError : return message 'The argument must be number'
        '''
        try:
            return round(math.tan(float(number)),2)
        except ValueError:
            raise ValueError("The arguments must be numbers")

