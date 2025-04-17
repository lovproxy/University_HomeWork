import unittest
from number79 import MyQueue

class Test_number3(unittest.TestCase):

    def test_positive1(self):
        A = MyQueue()
        A.enqueue(10)
        A.enqueue(5)
        p1 = A.dequeue()
        p2 = A.dequeue()
        p3 = A.dequeue()
        p = f"{p1}{p2}{p3}"
        self.assertEqual(p, ('105None'))

    def test_positive2(self):
        A = MyQueue()
        A.enqueue(100)
        A.enqueue(15)
        p1 = A.dequeue()
        p2 = A.dequeue()
        p3 = A.dequeue()
        A.enqueue(100)
        p4 = A.dequeue()
        p5 = A.dequeue()
        p = f"{p1}{p2}{p3}{p4}{p5}"
        self.assertEqual(p, ('10015None100None'))

    def test_granical1(self):
        A = MyQueue()
        p1 = A.enqueue(100)
        p2 = A.enqueue(200)
        p3 = A.enqueue(300)
        p4 = A.enqueue(500)
        p5 = A.enqueue(500)
        p6 = A.enqueue(500)
        p7 = A.enqueue(500)
        p8 = A.enqueue(500)
        p9 = A.enqueue(500)
        p10 = A.enqueue(500)
        p11 = A.enqueue(500)
        p = f"{p1}{p2}{p3}{p4}{p5}{p6}{p7}{p8}{p9}{p10}{p11}"
        self.assertEqual(p, ('TrueTrueTrueTrueTrueTrueTrueTrueTrueTrueFalse'))

    def test_granical2(self):
        A = MyQueue()
        p1 = A.enqueue(100)
        p2 = A.enqueue(200)
        p3 = A.enqueue(300)
        p4 = A.enqueue(500)
        p5 = A.isEmpty()
        p6 = A.dequeue()
        p = f"{p1}{p2}{p3}{p4}{p5}{p6}"
        self.assertEqual(p, ('TrueTrueTrueTrueFalse100'))

    def test_special1(self):
        A = MyQueue()
        p1 = A.dequeue()
        p2 = A.dequeue()
        p3 = A.dequeue()
        p4 = A.isEmpty()
        A.enqueue(100)
        p5 = A.dequeue()
        p6 = A.isEmpty()
        p = f"{p1}{p2}{p3}{p4}{p5}{p6}"
        self.assertEqual(p, ('NoneNoneNoneTrue100True'))