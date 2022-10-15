import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Solution.Solution import *
import unittest

class TestMethods(unittest.TestCase):
    def testParse(self, query, intended):
        soln = OrderUp(query)
        self.assertEqual(soln._parse(), intended)
    def testValidateOrder(self, query, intended):
        soln = OrderUp(query)
        self.assertEqual(soln._validateOrder, intended)
    def testReturnString(self, Soln, Order, intended):
        self.assertEqual(Soln._returnString(Order), intended)
    def testDoOrder(self, query, intended):
        Soln = OrderUp(query)
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