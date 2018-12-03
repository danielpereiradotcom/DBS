"""Continuous Assessment
Dublin Business School
B8IT105 Programming for Big Data (B8IT105_1819_TME1S)
Lecturer: Darren Redmond
Student: Daniel Pereira (10391381@mydbs.ie)
________________________________________________________________________________

CA4 - Analysis of Control

This is the test file to run the test
"""
##################################################

import unittest

from CA4 import readFile, getCommits, getAuthors, getMonths, getDates, getTimes

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.fileData = readFile('changes_python.log')

    def testNumberOfLinesCorrectResult(self):
        self.assertEqual(5255, len(self.fileData))

    def testNumberOfCommitsCorrectResult(self):
        commitsList = getCommits(self.fileData)
        self.assertEqual(422, len(commitsList))

    def testNumberOfAuthorsCorrectResult(self):
        commitsList = getCommits(self.fileData)
        authorsList = getAuthors(commitsList)
        self.assertEqual(10, len(authorsList))
    
    def testTopCommiterCorrectResult(self):
        commitsList = getCommits(self.fileData)
        authorsList = getAuthors(commitsList)
        self.assertEqual(191, authorsList['Thomas']['commits'])
        self.assertEqual(234, authorsList['Thomas']['lines'])

    def testLowestCommiterCorrectResult(self):
        commitsList = getCommits(self.fileData)
        authorsList = getAuthors(commitsList)
        self.assertEqual(1, authorsList['murari.krishnan']['commits'])
        self.assertEqual(1, authorsList['murari.krishnan']['lines'])

    def testNumberOfMonthsCorrectResult(self):
        commitsList = getCommits(self.fileData)
        monthsList = getMonths(commitsList)
        self.assertEqual(5, len(monthsList))

    def testNumberOfDatesCorrectResult(self):
        commitsList = getCommits(self.fileData)
        datesList = getDates(commitsList)
        self.assertEqual(76, len(datesList))

    def testNumberOfTimesCorrectResult(self):
        commitsList = getCommits(self.fileData)
        timesList = getTimes(commitsList)
        self.assertEqual(419, len(timesList))

if __name__ == '__main__':
    unittest.main()
