import unittest
from number76 import MyList, Item

class Test_number3(unittest.TestCase):

    def test_positive1(self):
        A = MyList()
        A.append(10)
        A.append(5)
        A.append(60)
        p1 = A.pop()
        p2 = A.pop()
        p3 = A.pop()
        p = f"{p1}{p2}{p3}"
        self.assertEqual(p, ('60510'))

    def test_positive2(self):
        A = MyList()
        A.append(100)
        A.append(15)
        p1 = A.pop()
        p2 = A.pop()
        p3 = A.pushFirst(30)
        A.append(100)
        p4 = A.popFirst()
        p5 = A.pop()
        p = f"{p1}{p2}{p3}{p4}{p5}"
        self.assertEqual(p, ('15100None30100'))

    def test_granical1(self):
        A = MyList()
        p1 = A.append(100)
        p2 = A.append(200)
        p3 = A.popFirst()
        p4 = A.popFirst()
        with self.assertRaises(Exception):
            A.pop()
        p = f"{p1}{p2}{p3}{p4}"
        self.assertEqual(p, ('NoneNone100200'))

    def test_granical2(self):
        A = MyList()
        A.append(100)
        A.append(200)
        A.append(300)
        A.append(500)
        p1 = A.popFirst()
        p2 = A.popFirst()
        p3 = A.popFirst()
        p4 = A.popFirst()
        with self.assertRaises(Exception):
            A.popFirst()
        p = f"{p1}{p2}{p3}{p4}"
        self.assertEqual(p, ('100200300500'))

    def test_special1(self):
        A = MyList()
        with self.assertRaises(Exception):
            A.pop()
            A.popFirst()
            A.popFirst()
            A.pop()
        A.append(100)
        p1 = A.pop()
        p2 = A.append(300)
        p3 = A.popFirst()
        with self.assertRaises(Exception):
            A.popFirst()
        p = f"{p1}{p2}{p3}"
        self.assertEqual(p, ('100None300'))