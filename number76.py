class Item:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__ (self, data=None):
        self.data = data
        self.next = 0
        self.prev = 0

class MyList:
    # конструктор, который корректно инициализирует голову и хвост списка
    def __init__(self):
        self.head = Item()
        self.tail = self.head
        self.len = 0

    # метод добавления элемента в конец списка
    def append(self, x):
        new = Item(x)
        new.prev = self.tail
        self.tail.next = new
        self.tail = new
        self.len += 1

    # метод удаления элемента из конца списка (не забываем про пустой список!)
    def pop(self):
        if self.head == self.tail:
            raise Exception
        last = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        self.len -= 1
        return last.data

    # метод добавления элемента в начало списка (помним про указатель tail!)
    def pushFirst(self, x):
        new = Item(x)
        new.next = self.head.next
        if self.head.next:
            self.head.next.prev = new
        new.prev = self.head
        self.head.next = new
        if self.tail == self.head:
            self.tail = new
        self.len += 1

    # метод удаления элемента из начала списка (опять не забываем про пустой список!)
    def popFirst(self):
        if self.head == self.tail:
            raise Exception
        first = self.head.next
        self.head.next = first.next
        if first.next:
            first.next.prev = self.head
        if self.tail == first:
            self.tail = self.head
        self.len -= 1
        return first.data

    # метод определения длины списка
    def __len__(self):
        return self.len
    # метод конструирования строкового представления списка
    def __str__(self):
        if self.head == self.tail:
            return []
        result = []
        a = self.head.next
        while a:
            result.append(str(a.data))
            a = a.next
        return f'[{", ".join(result)}]'


# Этот код менять не нужно. При корректной реализации класса MyList он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках
if __name__ == '__main__':
    A = MyList()
    A.append(1)
    A.pushFirst(3)
    A.append(5)
    A.append(1)
    A.pushFirst(5)
    print(A)
    print(A.popFirst())
    print(A.pop())
    print(A)
    print(len(A))