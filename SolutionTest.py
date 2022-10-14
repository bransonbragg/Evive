import unittest
from Solution import Solution
from Meals import Breakfast, Lunch, Dinner

class TestSolutionMethods(unittest.TestCase):
    def testParse(self, query, intended):
        soln = Solution(query)
        self.assertEqual(soln._parse(), intended)
    def testValidateOrder(self, query, intended):
        soln = Solution(query)
        self.assertEqual(soln._validateOrder, intended)
    def testReturnString(self, Soln, Order, intended):
        self.assertEqual(Soln._returnString(Order), intended)
    def testDoOrder(self, query, intended):
        Soln = Solution(query)
        self.assertEqual(Soln.doOrder(), intended)
    def testBreakfast(self, items, intended):
        Order = Breakfast(items)
        self.assertEqual(Order, intended)
    def testLunch(self, items, intended):
        Order = Lunch(items)
        self.assertEqual(Order, intended)
    def testDinner(self, items, intended):
        Order = Dinner(items)
        self.assertEqual(Order, intended)