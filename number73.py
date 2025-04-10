q = []

def Fib(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib


def fibSearch(A, elem):
    # если искомый элемент за границами диапазона,то делать нечего
    if elem > max(A) or elem < min(A):
        return

    # вычисляем нужное число Фибоначчurnи
    list_fib = Fib(len(A))
    lna = len(A)
    for x in range(len(list_fib)):
        if list_fib[x] >= lna:
            k = x
    # вызываем рекурсивную функцию
    return fibSearchRec(A, elem, 0, list_fib[k-1], list_fib[k], len(A))

def fibSearchRec(A, elem, lo, fKm1, fK, n):
    global q
    q = []
    # если подмассив пустой ИЛИ из одного элемента, который не равен elem, то делать нечего
    if fK == 0 or (fK == 1 and A[lo] != elem):
        q.append(A[lo])
        return -1

    # если подмассив из одного элемента, который равен elem, то возвращаем ответ и завершаемся
    if fK == 1 and A[lo] == elem:
        q.append(A[lo])
        return lo

    # вычисляем (k-2)-е число Фибоначчи
    fKm2 = fK - fKm1

    # вычисляем mid - правый элемент первого подмассива (смотрим, чтобы он не выпал за границы)
    mid = min(lo + fKm2 - 1, n - 1)
    q.append(A[mid])

    # выполняем сравнение и рекурсивный вызов на одной из частей
    if A[mid] == elem:
        q.append(elem)
        return q
    elif A[mid] > elem: return fibSearchRec(A, elem, lo, fKm1 - fKm2, fKm2, n)
    else: return fibSearchRec(A, elem, lo + fKm2, fKm2, fKm1, n)

if __name__ == '__main__':
    elem = int(input())
    A = list(map(int, input().split()))

    if fibSearch(A, elem) == None:
        print('None')
    else:
        for x in q:
            print(x, end=' ')