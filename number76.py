class Item:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__ (self, data=[], next=0, prev=0):
        self.data = data
        self.next = next
        self.prev = prev

class MyList:
    # конструктор, который корректно инициализирует голову и хвост списка
    def __init__(self):
        self.item = Item()
        self.data = self.item.data
        if len(self.data) != 0:
            self.head = self.data[0]
            self.tail = self.item[len(self.data)-1]
        else:
            self.head = 0
            self.tail = 0

    # метод добавления элемента в конец списка
    def append(self, x):
        self.data += [x]
        self.tail += 1

    # метод удаления элемента из конца списка (не забываем про пустой список!)
    def pop(self):
        if len(self.data) == 0:
            raise Exception
        else:
            del_number = self.data[-1]
            self.data = self.data[:self.tail - 2]
            self.tail -= 1
            return del_number
    # метод добавления элемента в начало списка (помним про указатель tail!)
    def pushFirst(self, x):
        self.data = [x] + self.data
        self.tail += 1
        self.head = self.data[0]

    # метод удаления элемента из начала списка (опять не забываем про пустой список!)
    def popFirst(self):
        if len(self.data) == 0:
            raise Exception
        del_number = self.data[0]
        self.data = self.data[1:]
        self.head = self.data[0]
        return del_number
    # метод определения длины списка
    def __len__(self):
        return len(self.data)
    # метод конструирования строкового представления списка
    def __str__(self):
        return f"{self.data}"

# Этот код менять не нужно. При корректной реализации класса MyList он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках
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