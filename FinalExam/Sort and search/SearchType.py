# Searching Types:
# 1.순차 탐색 (sequential search)
# 2.이진 탐색 (binary search)
# 3.보간 탐색 (interpolation search)

import random

def sequential_search(A, key, low, high):
    for i in range(low, high + 1):
        if A[i] == key:
            return i
    return -1


def binary_search(A, key, low, high):
    if low > high:
        return -1
    middle = (low + high) // 2

    if key == A[middle]:
        return middle
    elif key < A[middle]:
        return binary_search(A, key, low, middle - 1)
    else:
        return binary_search(A, key, middle + 1, high)

def interpolation_search(A, key, low, high):
    if low > high or A[low] == A[high]:
        return -1

    pos = low + (high - low) * (key - A[low]) // (A[high] - A[low])

    if pos < low or pos > high:
        return -1

    if A[pos] == key:
        return pos
    elif A[pos] < key:
        return interpolation_search(A, key, pos + 1, high)
    else:
        return interpolation_search(A, key, low, pos - 1)

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A

if __name__ == '__main__':
    A = []
    for i in range(15):
        A.append(random.randint(1, 100))
    print('A[] =', A)

    key = int(input('Enter key to search: '))

    # 순차 탐색
    idx = sequential_search(A, key, 0, len(A) - 1)
    if idx != -1:
        print('%d 위치에서 발견 (Sequential Search)' % idx)
    else:
        print('Sequential Search: Key not found')

    key = int(input('Enter key to search: '))

    # 정렬 후 이진 탐색 수행
    A_sorted = insertionSort(A[:])
    print('Sorted A[] =', A_sorted)

    idx = binary_search(A_sorted, key, 0, len(A_sorted) - 1)
    if idx != -1:
        print('%d 위치에서 발견 (Binary Search)' % idx)
    else:
        print('Binary Search: Key not found')

    key = int(input('Enter key to search: '))

    # 정렬 후 보간 탐색 수행
    A_sorted = insertionSort(A[:])
    print('Sorted A[] =', A_sorted)

    idx = binary_search(A_sorted, key, 0, len(A_sorted) - 1)
    if idx != -1:
        print('%d 위치에서 발견 (Interpolation Search)' % idx)
    else:
        print('Binary Search: Key not found')

#Output:
# A[] = [70, 93, 49, 8, 28, 3, 11, 95, 44, 12, 71, 64, 65, 21, 68]
# Enter key to search: 8
# 3 위치에서 발견 (Sequential Search)
# Enter key to search: 3
# Sorted A[] = [3, 8, 11, 12, 21, 28, 44, 49, 64, 65, 68, 70, 71, 93, 95]
# 0 위치에서 발견 (Binary Search)
# Enter key to search: 44
# Sorted A[] = [3, 8, 11, 12, 21, 28, 44, 49, 64, 65, 68, 70, 71, 93, 95]
# 6 위치에서 발견 (Interpolation Search)

