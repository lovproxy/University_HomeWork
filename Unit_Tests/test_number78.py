import unittest
from number78 import MyStack

class Test_number3(unittest.TestCase):

    def test_positive1(self):
        A = MyStack([5,10,20,None,None,None,None,None,None,None])
        p1 = A.pop()
        p2 = A.pop()
        p3 = A.pop()
        p = f"{p1}{p2}{p3}"
        self.assertEqual(p, ('20105'))

    def test_positive2(self):
        A = MyStack([55, 120, 20, 67, 1, 3, None, None, None, None])
        p1 = A.pop()
        p2 = A.pop()
        p3 = A.pop()
        A.push(100)
        p4 = A.pop()
        p5 = A.pop()
        p = f"{p1}{p2}{p3}{p4}{p5}"
        self.assertEqual(p, ('316710020'))

    def test_granical(self):
        A = MyStack([55, 120, 20, 67, 1, 3, 5, 10, 30, 50])
        p1 = A.push(100)
        p2 = A.push(200)
        A.pop()
        p3 = A.push(300)
        p4 = A.push(500)
        p = f"{p1}{p2}{p3}{p4}"
        self.assertEqual(p, ('FalseFalseTrueFalse'))

    def test_granical2(self):
        A = MyStack([55, 120, 20, 67, 1, 3, 5, 10, 30, 50])
        p1 = A.push(100)
        p2 = A.push(200)
        A.pop()
        p3 = A.push(300)
        p4 = A.push(500)
        p5 = A.isEmpty()
        p = f"{p1}{p2}{p3}{p4}{p5}"
        self.assertEqual(p, ('FalseFalseTrueFalseFalse'))

    def test_special1(self):
        A = MyStack([5, 10, 20, None, None, None, None, None, None, None])
        p1 = A.pop()
        p2 = A.pop()
        p3 = A.pop()
        p4 = A.isEmpty()
        A.push(100)
        p5 = A.pop()
        p6 = A.isEmpty()
        p = f"{p1}{p2}{p3}{p4}{p5}{p6}"
        self.assertEqual(p, ('20105True100True'))