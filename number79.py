class MyQueue:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self):
        self.boolean = False
        self.mas = [None] * 10
        self.head = 0
        self.tail = -1

    # метод добавления элемента в очередь
    def enqueue(self, x):
        if self.boolean:
            return False
        if self.tail == -1:
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % 10
        self.mas[self.tail] = x
        if self.head == (self.tail + 1) % 10:
            self.boolean = True
        else:
            self.boolean = False
        return True

    # метод удаления элемента из очереди
    def dequeue(self):
        if self.isEmpty():
            return None
        q = self.mas[self.head]
        self.mas[self.head] = None
        self.head = (self.head + 1) % 10
        return q
    # метод для определения, пуста ли очередь
    def isEmpty(self):
        if (self.head > self.tail) and (self.mas[self.head] == None) and (self.mas[self.tail] == None):
            return True
        return False
# Этот код менять не нужно. При корректной реализации класса MyQueue он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках
if __name__ == '__main__':
    A = MyQueue()
    print(A.enqueue(1))
    print(A.enqueue(2))
    print(A.enqueue(3))
    print(A.enqueue(4))
    print(A.enqueue(5))
    print(A.enqueue(6))
    print(A.enqueue(10))
    print(A.enqueue(11))
    print(A.enqueue(12))
    print(A.enqueue(13))
    print(A.enqueue(14))
    print(A.enqueue(15))
    print(A.enqueue(16))