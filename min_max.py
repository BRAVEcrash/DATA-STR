import random

def find_min_max(A):
    min = max = A[0]
    for i in range(1,len(A)):
        if max < A[i]:
            max = A[i]
        if min > A[i]:
            min = A[i]

    return (min, max)

if __name__ == '__main__':
    A = []
    for _ in range(10):
        A.append(random.randint(1, 100))
    print(A)
    print(find_min_max(A))