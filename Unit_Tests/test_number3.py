import unittest
from number73 import fibSearch as iS

class Test_number3(unittest.TestCase):

    def test_positive1(self):
        self.assertEqual(iS([1, 4, 7, 8, 10, 17, 21, 23, 26, 32, 36, 40, 41, 43, 44, 47, 49], 8), [8, 8])

    def test_positive2(self):
        self.assertEqual(iS([1, 15, 25, 110, 265, 301, 405, 500, 600], 25), [25, 25])

    def test_granical(self):
        self.assertEqual(iS([1, 15, 100, 200, 350, 400], 500), None)

    def test_granical2(self):
        self.assertEqual(iS([1, 15, 30, 35, 50, 60], 0), None)

    def test_special1(self):
        self.assertEqual(iS([1, 23, 35, 110, 225, 350, 400], 200), -1)

    def test_special2(self):
        self.assertEqual(iS([13, 35, 50, 210, 255, 303, 409], 14), -1)