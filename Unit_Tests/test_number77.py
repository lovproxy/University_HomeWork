import unittest
from number77 import MyList, Item

class Test_number77(unittest.TestCase):

    def test_positive1(self):
        A = MyList()
        A.append(10)
        A.append(5)
        A.append(60)
        p = []
        for x in A:
            p.append(x)
        self.assertEqual(p, ([10, 5, 60]))

    def test_positive2(self):
        A = MyList()
        A.append(100)
        A.append(15)
        A.append(500)
        A.append(200)
        A.append(10)
        p1 = A.pop()
        p2 = A.pop()
        p3 = A.pushFirst(30)
        A.append(100)
        p4 = A.popFirst()
        p5 = A.pop()
        p = f"{p1}{p2}{p3}{p4}{p5}"
        self.assertEqual(p, ('10200None30100'))

    def test_granical1(self):
        A = MyList()
        p1 = A.append(100)
        p2 = A.append(200)
        p3 = A.popFirst()
        with self.assertRaises(Exception):
            A.addAfter(-1, 30)
        p = f"{p1}{p2}{p3}"
        self.assertEqual(p, ('NoneNone100'))

    def test_granical2(self):
        A = MyList()
        A.append(100)
        A.append(200)
        A.append(300)
        A.append(500)
        p1 = A.popFirst()
        p2 = A.popFirst()
        p3 = A.popFirst()
        with self.assertRaises(Exception):
            A.remove(10)
            A.remove(0)
        p = f"{p1}{p2}{p3}"
        self.assertEqual(p, ('100200300'))

    def test_special1(self):
        A = MyList()
        with self.assertRaises(Exception):
            A.pop()
            A.popFirst()
            A.popFirst()
            A.pop()
        A.append(100)
        A.append(200)
        A.append(300)
        p1 = A.pop()
        A[0] = 1000
        p2 = A.popFirst()
        A.addAfter(A.find(A[0]),5000)
        p3 = A.pop()
        p4 = A.pop()
        with self.assertRaises(Exception):
            A.popFirst()
        p = f"{p1}{p2}{p3}{p4}"
        self.assertEqual(p, ('30010005000200'))