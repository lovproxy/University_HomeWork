class Graph:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self, V = None, E = None):
        self.vdict = {}
        self.edict = {}
        if V != None:
            for x in V:
                self.vdict[x] = None
        if E != None:
            for x in E:
                self.edict[x] = None
        self.vlist = []
    # метод конструирования строкового представления графа
    def __str__ (self):
        nl = '\n'
        return f"vertices:\n{' '.join(map(str, [x for x in self.vertices()]))}\nedges:\n{nl.join(map(str, [f'{x[0]} -> {x[1]}' for x in self.edges()]))}"

    # метод добавления метки вершине или ребру
    def __setitem__ (self, x, d):
        if type(x) is tuple:
            self.edict[x] = d
        else:
            self.vdict[x] = d

    # метод возврата метки вершины или ребра
    def __getitem__(self, x):
        if type(x) is tuple:
            return self.edict[x]
        return self.vdict[x]

    def V(self):
        return tuple(self.vdict.keys())

    # Добавляет в граф вершину v. Метка вершины должна быть None.
    def add_vertex(self, ver):
        if ver not in self.vdict:
            self.vdict[ver] = None
            self.vlist.append(ver)

    # Добавляет в граф ориентированное ребро e. Ребро е представляется кортежем (класс tuple)
    # двух имён рёбер (v, u). Метка ребра устанавливается в None.
    def add_edge(self, e):
        self.edict[e] = None

    # генератор или итератор, перечисляющий все рёбра графа
    def edges(self):
        return list(self.edict.keys())
    # генератор или итератор, перечисляющий все вершины графа
    def vertices(self):
        return (x for x in self.vdict)
    # генератор или итератор, перечисляющий все рёбра, выходящие из вершины v
    def outgoing(self, v):
        for x in self.edict:
            if x[0] == v:
                yield x



# Этот код менять не нужно. При корректной реализации класса Graph он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках
'''
g = Graph()
g.add_vertex("u")
g.add_vertex("v")
g.add_vertex("w")
g.add_edge(("u", "v"))
g.add_edge(("u", "w"))
g.add_edge(("v", "w"))
print(g)
print(list(g.vertices()))
print(list(g.edges()))
print(list(g.outgoing("u")))
print(list(g.outgoing("w")))
g["u"] = 1
g[("u", "v")] = 42
print(g["v"])
print(g["u"])
print(g[("u", "v")])
print(g[("v", "w")])
g2 = Graph(["a", "b"], [("a", "b"), ("b", "a")])
print(g2)'''