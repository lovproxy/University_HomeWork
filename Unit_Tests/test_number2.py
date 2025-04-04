import unittest
from number1 import binSearch as bS

class Test_number1(unittest.TestCase):

    def test_positive1(self):
        self.assertEqual(bS([1, 3, 5, 10, 25, 30, 40], 25), [10, 30, 25])

    def test_positive2(self):
        self.assertEqual(bS([1, 15, 25, 110, 265, 301, 405, 500, 600], 25), [265, 15, 25])

    def test_granical(self):
        self.assertEqual(bS([1, 15, 100, 200, 350, 400], 500), None)

    def test_granical2(self):
        self.assertEqual(bS([1, 15, 30, 35, 50, 60], 0), None)

    def test_special1(self):
        self.assertEqual(bS([1, 23, 35, 110, 225, 350, 400], 200), -1)

    def test_special2(self):
        self.assertEqual(bS([13, 35, 50, 210, 255, 303, 409], 14), -1)