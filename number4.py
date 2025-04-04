def insert2Mas(A, n, i, elem):
    # если вставлять уже некуда, пишем full
    if len(A) == n:
        print('full')
        return

    # в цикле печатаем переносы элементов
    for j in range(n, i, - 1):
        print(f"A[{j}] = A[{j - 1}]")
    A[i] = elem

    # печатаем копирование элемента elem в нужное место
    print(f'A[{i}] = {elem}'.format(i, elem))


n, i, elem = map(int, input().split())
a = list(map(int, input().split()))
insert2Mas(a, n, i, elem)