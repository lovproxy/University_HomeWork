massiv = []

def interpolSearch(A, elem):
    # если искомый элемент за границами диапазона,то делать нечего
    if elem > A[len(A) - 1] or elem < A[0]:
        return None
    global massiv
    massiv = []

    # определим верхнюю границу и вызовем рекурсивную функцию
    right = len(A) - 1
    return interpolSearchRec(A, elem, 0, right)

def interpolSearchRec(A, elem, lo, hi):
    # если подмассив пустой ИЛИ elem за границами диапазона, то делать нечего
    if lo > hi or elem > A[hi] or elem < A[lo]:
        return -1
    # если левая и правая границы совпадают, то mid по формуле вычислять нельзя! (почему?)
    if lo == hi:
        mid = lo
    # иначе - вычисляем mid по формуле
    else:
        mid = lo + round((elem - A[lo]) * (hi - lo) / (A[hi] - A[lo]))
        massiv.append(A[mid])

    # выполняем сравнение и рекурсивный вызов на одной из частей
    if A[mid] == elem:
        return massiv
    elif A[mid] > elem:
        return interpolSearchRec(A, elem, lo, mid - 1)
    else:
        return interpolSearchRec(A, elem, mid + 1, hi)

if __name__ == '__main__':
    elem = int(input())
    mass = list(map(int, input().split()))
    if interpolSearch(mass, elem) == None:
        print(None)
    for x in massiv:
            print(x, end = ' ')