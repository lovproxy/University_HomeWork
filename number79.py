class MyQueue:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self, mas=[None]*10, head=0, tail=-1):
        self.boolean = False
        self.mas = mas
        if mas[0] == None:
            self.head = 0
            self.tail = -1
        else:
            self.head = head
            self.tail = tail

    # метод добавления элемента в очередь
    def enqueue(self, x):
        if self.mas[self.head + 1] != None:
            return False
        self.mas[self.head] = x
        self.head += 1
        return True

    # метод удаления элемента из очереди
    def dequeue(self):
        if self.mas[self.tail + 1] == None:
            return None
        q = self.mas[self.tail + 1]
        self.mas = self.mas[1:] + [None]
        self.head -= 1
        return q
    # метод для определения, пуста ли очередь
    def isEmpty(self):
        if ((self.tail + 1) % 10) == (self.head % 10) and len(self.mas) != 0:
            return True
        return False
# Этот код менять не нужно. При корректной реализации класса MyQueue он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках
if __name__ == '__main__':
    A = MyQueue()
    print(A.isEmpty())
    A.enqueue(1)
    A.enqueue(2)
    print(A.dequeue())
    A.enqueue(3)
    print(A.dequeue())
    A.enqueue(4)
    A.enqueue(5)
    print(A.isEmpty())
    A.enqueue(6)
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
    print(A.isEmpty())
    A.enqueue(10)
    A.enqueue(11)
    A.enqueue(12)
    A.enqueue(13)
    A.enqueue(14)
    A.enqueue(15)
    A.enqueue(16)
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
