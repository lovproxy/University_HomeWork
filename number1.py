massiv = []

def binSearch(A, elem):
    # если искомый элемент за границами диапазона,то делать нечего
    if elem > A[len(A) - 1] or elem < A[0]:
        return None
    global massiv
    massiv = []

    # определим верхнюю границу и вызовем рекурсивную функцию
    right = len(A) - 1
    return binSearchRec(A, elem, 0, right)


def binSearchRec(A, elem, lo, hi):
    # если подмассив пустой, то делать нечего
    if lo > hi:
        return -1

    # определяем средний элемент
    mid = (lo + hi) // 2
    massiv.append(A[mid])

    # выполняем сравнение и рекурсивный вызов на одной из половин
    if A[mid] == elem:
        return massiv
    elif A[mid] > elem:
        return binSearchRec(A, elem, lo, mid - 1)
    else:
        return binSearchRec(A, elem, mid + 1, hi)

if  __name__ == '__main__':
    elem = int(input())
    mass = list(map(int, input().split()))
    if binSearch(mass, elem) == None:
        print(None)
    for x in massiv:
        print(x, end = ' ')
