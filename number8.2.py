class Graph:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self, V=None, E=None):
        self.vdict = {}
        self.edict = {}
        self.vset = []
        self.eset = []
        if V is not None:
            self.add_vertex(V)
        if E is not None:
            self.add_edge(E)

    # метод конструирования строкового представления графа
    def __str__(self):
        nl = '\n'
        return f"vertices:\n{' '.join(map(str, [i for i in sorted(self.vertices())]))}\nedges:\n{nl.join(map(str, [f'{x[0]} -> {x[1]}' for x in self.edges()]))}"


    # метод добавления метки вершине или ребру
    def __setitem__(self, x, d):
        if type(x) is tuple:
            self.edict[x] = d
        else:
            self.vdict[x] = d

    # метод возврата метки вершины или ребра
    def __getitem__(self, x):
        if type(x) is tuple:
            return self.edict[x] if x in self.eset else None
        return self.vdict[x] if x in self.vset else None

    @property
    def V(self):
        return tuple(self.vdict.keys())

    # Добавляет в граф вершину v. Метка вершины должна быть None.
    def add_vertex(self, ver):
        if type(ver) is list:
            for x in ver:
                self.vset.append(x)
                self.vdict[x] = None
        else:
            if ver not in self.vset:
                self.vdict[ver] = None
                self.vset.append(ver)

    # Добавляет в граф ориентированное ребро e. Ребро е представляется кортежем (класс tuple)
    # двух имён рёбер (v, u). Метка ребра устанавливается в None.
    def add_edge(self, e):
        if type(e) is list:
            for x in e:
                self.eset.append(x)
                self.edict[x] = None
        else:
            if e not in self.vset and type(e) is tuple:
                self.edict[e] = None
                self.eset.append(e)

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

# функция, создающая граф де Брёйна
def construct_de_Brujin(patterns):
    g = Graph()
    for pattern in patterns:
        prefix = pattern[:-1]
        suffix = pattern[1:]
        g.add_edge((prefix, suffix))
        g.add_vertex(prefix)
        g.add_vertex(suffix)
    return g

# считываем строки в patterns, пока не кончатся
q = input()
patterns = []
while q:
    patterns.append(q)
    try:
        q = input()
    except:
        break

G = construct_de_Brujin(patterns)
print(G)