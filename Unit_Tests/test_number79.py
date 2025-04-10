import unittest
from number79 import MyQueue

class Test_number3(unittest.TestCase):

    def test_positive1(self):
        A = MyQueue([5,10,20,None,None,None,None,None,None,None])
        p1 = A.dequeue()
        p2 = A.dequeue()
        p3 = A.dequeue()
        p = f"{p1}{p2}{p3}"
        self.assertEqual(p, ('51020'))

    def test_positive2(self):
        A = MyQueue([55, 120, 20, 67, 1, 3, None, None, None, None], 5,-1)
        p1 = A.dequeue()
        p2 = A.dequeue()
        p3 = A.dequeue()
        A.enqueue(100)
        p4 = A.dequeue()
        p5 = A.dequeue()
        p = f"{p1}{p2}{p3}{p4}{p5}"
        self.assertEqual(p, ('5512020671'))

    def test_granical(self):
        A = MyQueue([55, 120, 20, 67, 1, 3, 5, 10, 30, 50],9,-1)
        p1 = A.enqueue(100)
        p2 = A.enqueue(200)
        A.dequeue()
        print(A.mas, A.head)
        p3 = A.enqueue(300)
        p4 = A.enqueue(500)
        p = f"{p1}{p2}{p3}{p4}"
        self.assertEqual(p, ('FalseFalseTrueFalse'))

    def test_granical2(self):
        A = MyQueue([55, 120, 20, 67, 1, 3, 5, 10, 30, 50],9,-1)
        print(A.head, A.tail)
        p1 = A.enqueue(100)
        p2 = A.enqueue(200)
        A.dequeue()
        p3 = A.enqueue(300)
        p4 = A.enqueue(500)
        p5 = A.isEmpty()
        p = f"{p1}{p2}{p3}{p4}{p5}"
        self.assertEqual(p, ('FalseFalseFalseFalseFalse'))

    def test_special1(self):
        A = MyQueue([55, 120, 20, 67, 1, 3, 5, 10, 30, 50],9,-1)
        p1 = A.pop()
        p2 = A.pop()
        p3 = A.pop()
        p4 = A.isEmpty()
        A.push(100)
        p5 = A.pop()
        p6 = A.isEmpty()
        p = f"{p1}{p2}{p3}{p4}{p5}{p6}"
        self.assertEqual(p, ('20105True100True'))