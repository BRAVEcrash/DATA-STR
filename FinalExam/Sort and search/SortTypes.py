# Sorting Types:
# 1.insertionSort
# 2.selectionSort
# 3.bubbleSort
def printStep(A, idx):
    print(' Step %d : ' %idx, end='')
    print(A)

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j + 1] = key
        printStep(A, i)

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        flag = False
        for j in range(1, n-i):
            if(A[j-1] > A[j]):
                A[j-1], A[j] = A[j], A[j-1]
                flag = True
        if not flag:
            break
        printStep(A, i+1)
def selectionSort(A):
    n = len(A)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if A[j] < A[min_idx]:
                min_idx = j
        # Меняем текущий элемент с наименьшим найденным
        A[i], A[min_idx] = A[min_idx], A[i]
        printStep(A, i + 1)
if __name__ == '__main__':
    data = [5,3,8,4,9,1,6,2,7]

    L = list(data)
    print(' Before :', L)
    insertionSort(L)
    print(" Insertion:",L)
    print()

    B = list(data)
    print(' Before :', B)
    bubbleSort(B)
    print(" Bubble :", B)
    print()

    S = list(data)
    print(' Before :', S)
    selectionSort(S)
    print(" Selection :", S)
    print()

