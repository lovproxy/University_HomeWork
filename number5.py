def insertMas2Mas(A, n, i, B):
    lenb = len(B)
    # если вставлять уже некуда, пишем full
    if len(A) - n < lenb:
        print('full')
        return

    # в цикле печатаем переносы элементов
    for x in range(n + lenb - 1, i + lenb - 1, -1):
        print(f"A[{x}] = A[{x - lenb}]")

    # в цикле печатаем копирование элементов из B в нужные места
    for x in range(lenb):
        print(f"A[{i + x}] = {B[x]}")

n, i = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
insertMas2Mas(a, n, i, b)