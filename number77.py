class Item:
    # скопируйте сюда код из предыдущего упражнения
    def __init__ (self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class MyList:
    # скопируйте сюда методы, реализованные в предыдущем упражнении
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
            return "[]"
        result = []
        a = self.head.next
        while a:
            result.append(str(a.data))
            a = a.next
        return f'[{", ".join(result)}]'

    # реализуйте метод, добавляющий новый элемент со значением x после p. Помните об указателе tail!
    def addAfter(self, p, x):
        if p == None:
            raise Exception
        new = Item(x)

        new.next = p.next
        new.prev = p
        if p.next:
            p.next.prev = new
        p.next = new
        if p == self.tail:
            self.tail = new
        self.len += 1

    # реализуйте метод удаления элемента p. Также помните об указателе tail! Он не должен "съехать"
    def remove(self, p):
        if p == None or p == self.head:
            raise Exception
        if p.prev:
            p.prev.next = p.next
        if p.next:
            p.next.prev = p.prev
        if p == self.tail:
            self.tail = p.prev
        self.len += 1
    # реализуйте метод поиска элемента в списке
    def find(self, x):
        elem = self.head.next
        while elem:
            if elem.data == x:
                return elem
            elem = elem.next
        return None

    # реализуйте перегрузку индексации на чтение
    def __getitem__(self, idx):
        if idx < 0 or idx > self.len:
            raise Exception
        elem = self.head.next
        for x in range(idx):
            elem = elem.next
        return elem.data

    # реализуйте перегрузку индексации на запись
    def __setitem__(self, idx, x):
        if idx < 0 or idx >= self.len:
            raise Exception
        elem = self.head.next
        for i in range(idx):
            elem = elem.next
        elem.data = x


    # реализуйте перегрузку метода in (может можно воспользоваться уже реализованным find?)
    def __contains__(self, x):
        return True if self.find(x) != None else False

    # реализуйте сложение двух списков (попробуйте использовать уже написанные методы для упрощения кода)
    def __add__ (self, lst):
        new = MyList()
        elem = self.head.next
        while elem:
            new.append(elem.data)
            elem = elem.next
        elem = lst.head.next
        while elem:
            new.append(elem.data)
            elem = elem.next
        return new

    # реализуйте метод конкатенации двух списков. Второй список не забудьте "обнулить"
    def concat(self, lst):
        if self.head == self.tail:
            return
        self.tail.next = lst.head.next
        if lst.head.next:
            lst.head.next.prev = self.tail
        self.tail = lst.tail
        self.len += lst.len
        lst.head.next = None
        lst.tail = lst.head
        lst.len = 0

    # метод, возвращающий итератор, мы написали за вас. Вам осталось только дописать сам класс итератора
    def __iter__(self):
        return MyListIterator(self.head.next)

class MyListIterator:
    def __init__(self, item):
        self.currentItem = item

    def __next__(self):
        # здесь необходимо написать код, который вернет значение
        # элемента, на который ссылается currentItem, и передвинет его
        # на следующий элемент. Если currentItem никуда не ссылается
        # (т.е. равен None), то необходимо выбросить исключение
        # raise StopIteration
        if self.currentItem is None:
            raise StopIteration
        data = self.currentItem.data
        self.currentItem = self.currentItem.next
        return data


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
    if (1 in A):
    	print("True")
    else:
        print("False")
    if (2 in A):
    	print("True")
    else:
        print("False")
    for i in range(6,10):
        A.append(i)
    A[0] = 0
    A[4] = -1
    for i in range(len(A)):
        print(A[i])
    for i in A:
    	print(i)
    A.remove(A.find(-1))
    print(A)
    B = MyList()
    for i in range(6):
    	B.append(i)
    A = A + B
    A.append(100)
    B[0] = 100
    print(A)
    print(B)
    A.concat(B)
    A.append(100)
    print(A)
    print(B)