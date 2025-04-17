class Graph:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self, V=None, E=None):
        self.vdict = {}
        self.edict = {}
        self.vset = []
        self.eset = []
        if V is not None:
            for x in V:
                self.add_vertex(x)
        if E is not None:
            for x in E:
                self.add_edge(x)

    # метод конструирования строкового представления графа
    def __str__(self):
        nl = '\n'
        return f"vertices:\n{' '.join(map(str, [i for i in sorted(self.vertices())]))}\nedges:\n{nl.join(map(str, [f'{x[0]} -> {x[1]}' for x in self.edges()]))}"

    # метод добавления метки вершине или ребру
    def __setitem__(self, x, d):
        if type(x) is tuple:
            self.add_vertex(x[0])
            self.add_vertex(x[1])
            if x not in self.eset:
                self.eset.append(x)
            self.edict[x] = d
        else:
            if x in self.vset:
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
        if ver not in self.vset:
            self.vdict[ver] = None
            self.vset.append(ver)

    # Добавляет в граф ориентированное ребро e. Ребро е представляется кортежем (класс tuple)
    # двух имён рёбер (v, u). Метка ребра устанавливается в None.
    def add_edge(self, e):
        if e not in self.eset and type(e) is tuple:
            self.edict[e] = 1
            self.eset.append(e)
        else:
            self.edict[e] += 1

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


def walk(G, path=None):
    # если граф пустой, то делать ничего не нужно, завершаем рекурсию
    if len(G.vset) == 0:
        return path or []

    # если путь пустой, то добавляем в него первую в лексикографическом порядке вершину графа
    if path is None:
        path = [min(G.vset)]

    # С помощью outgoing() пытаемся найти ребро из последней в пути path вершины.
    # Если нашли, модифицируем метку, добавляем новую вершину в path и делаем рекурсивный вызов.
    # Не забудьте, что функция walk должна вернуть путь!
    for x in G.outgoing(path[-1]):
        if G[x] > 0:
            G[x] -= 1
            return walk(G, path + [x[1]])

    # если свободных ребер нет, то просто возвращаем path
    return path


# Этот код менять не нужно. При корректной реализации класса Graph он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках

g = Graph([1, 2, 3], [(1, 2), (2, 3), (3, 1)])
g[(1, 2)] = 1
g[(2, 3)] = 1
g[(3, 1)] = 0
print(walk(g, [1]))
print(g[(1, 2)])
print(g[(2, 3)])
