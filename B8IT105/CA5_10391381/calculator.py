"""Continuous Assessment
Dublin Business School
B8IT105 Programming for Big Data (B8IT105_1819_TME1S)
Lecturer: Darren Redmond
Student: Daniel Pereira (10391381@mydbs.ie)
________________________________________________________________________________

Assignment 5 - A 10 Function Calculator (Refactor):
CA5 involves modifying your calculator class from CA1 to ensure that it can handle lists of data.
You will be required to refactor / rewrite your functions so that they can handle lists.
You will need to use lambda, map, filter, reduce, generator, and list comprehension in any manner you deem necessary to achieve this.
"""
import os
import math
from functools import reduce


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

    def Add(self, numbers):
        '''
        This method add numbers from a list
        E.g. 1 + 2 + 3 = 6
        Args:
            numbers (list): a list of numbers 
        Returns:
            (float) : the sum of elements of the list
        Exceptions:
            ValueError : return message 'The arguments must be numbers'
        '''
        try:
            return reduce((lambda x,y: float(x)+float(y)), numbers)
        except Exception:
            raise ValueError("The arguments must be numbers")

    def Cosine(self, numbers):
        '''
        This method returns the cosine of a radians from a list of numbers
        Args:
            numbers (list): a list of radians numbers
        Returns:
            (float) : the cosine of radians rounded to two digits from a list of numbers
        Exceptions:
            ValueError : return message 'The argument must be number'
        '''
        try:
            return list(map(lambda x: round(math.cos(float(x)),2), numbers))            
        except ValueError:
            raise ValueError("The arguments must be numbers")

    def Divide(self, numbers):
        '''
        This method divides numbers of a list
        E.g. 1 / 2 = 0.5
        Args:
            numbers (list): a list of numbers
        Returns:
            (float) : the result of first element divided by the second element of the list
        Exceptions:
            ValueError : return message 'The arguments must be numbers'
            ZeroDivisionError : return message 'The second element cannot be zero'
        '''
        try:

            if all(lambda y: y != 0 for y in numbers):
                return reduce((lambda x,y: float(x)/float(y)), numbers) 
            else:
                raise ZeroDivisionError()
        except ValueError:
            raise ValueError("The arguments must be numbers")
        except ZeroDivisionError:
            raise Exception("The second number cannot be zero")

    def LogBase10(self, numbers):
        '''
        This method returns the base 10 logarithm of a list of number
        E.g. Log base-10 of 10 = 1
        Args:
            number (list): a list of numbers
        Returns:
            (list) : (float) the calculate logarithm base 10 of the numbers
        Exceptions:
            ValueError : return message 'The argument must be numbers'
            Exception : return message 'The argument must be positive'
        '''
        try:
            if all(lambda y: y <= 0 for y in numbers):
                return list(map(lambda x: round(math.log10(float(x)),2), numbers))                
            else:
                raise Exception("The argument must be positive")
        except ValueError:
            raise ValueError("The arguments must be numbers")

    def Multiply(self, numbers):
        '''
        This method multiplies numbers from a list
        E.g. 1 * 2 * 2 = 4
        Args:
            numbers (list): a list of numbers
        Returns:
            (float) : the result of numbers multiplied
        Exceptions:
            ValueError : return message 'The arguments must be numbers'
        '''
        try:
            return reduce((lambda x,y: float(x)*float(y)), numbers)
        except ValueError:
            raise ValueError("The arguments must be numbers")

    def Power(self, numbers):
        '''
        This method calculates a number elevated to a power of a second element of the list
        E.g. 2 ** 2 = 4
        Args:
            number (list): a list of numbers
        Returns:
            (float) : the result of first number divided by the second element number
        Exceptions:
            ValueError : return message 'The arguments must be numbers'
        '''
        try:
            return reduce((lambda x,y: float(x)**float(y)), numbers)
        except ValueError:
            raise ValueError("The arguments must be numbers")

    def Sine(self, numbers):
        '''
        This method returns a list of the sine of a radians from a list
        Args:
            number (list): the radians numbers
        Returns:
            (list) : a list of (float) the sine of radians rounded to two digits
        Exceptions:
            ValueError : return message 'The argument must be number'
        '''
        try:
            return list(map(lambda x: round(math.sin(float(x)),2), numbers))
        except ValueError:
            raise ValueError("The arguments must be numbers")

    def Subtract(self, numbers):
        '''
        This method subtract numbers from a list
        E.g. 2 - 1 - 2 = -1
        Args:
            numbers (list): a list of numbers 
        Returns:
            (float) : the result of numbers subtracted
        Exceptions:
            ValueError : return message 'The arguments must be numbers'
        '''
        try:
            return reduce((lambda x,y: float(x)-float(y)), numbers)
        except ValueError:
            raise ValueError("The arguments must be numbers")

    def SquareRoot(self, numbers):
        '''
        This method returns a list of square root of numbers from a list
        E.g. square root of 4 = 2
        Args:
            numbers (list): a list of numbers to calculate the square root
        Returns:
            (list) : a list (float) with the square root of numbers
        Exceptions:
            ValueError : return message 'The argument must be a number'
            Exception : return message 'The number must be positive'
        '''
        try:
            if all(lambda y: y <= 0 for y in numbers):
                return list(map(lambda x: math.sqrt(float(x)), numbers))
            else:
                raise Exception("The number must be positive")
        except ValueError:
            raise ValueError("The argument must be a number")

    def Tangent(self, numbers):
        '''
        This method returns a list of tangent of radians
        Args:
            numbers (list): a list of the radian number
        Returns:
            (list) : a list (float) the tangent of radians rounded to two digits
        Exceptions:
            ValueError : return message 'The argument must be number'
        '''
        try:
            return list(map(lambda x: round(math.tan(float(x)),2), numbers))
        except ValueError:
            raise ValueError("The arguments must be numbers")

