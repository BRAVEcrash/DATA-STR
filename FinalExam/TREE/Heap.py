N = 20  # Maximum heap size

class MaxiHeap:  # This is actually a Min-Heap
    def __init__(self):
        self.heap = [None] * N  # Index 0 is unused
        self.heapSize = 0  # Number of elements in heap

    def upHeap(self):  # Restore heap by bubbling up
        i = self.heapSize
        key = self.heap[i]

        while (i != 1) and (key < self.heap[i // 2]):  # Compare with parent
            self.heap[i] = self.heap[i // 2]  # Move parent down
            i = i // 2  # Move up to parent
        self.heap[i] = key  # Place key in correct position

    def insortingTime(self, item):  # Insert item into heap
        self.heapSize += 1
        self.heap[self.heapSize] = item  # Add at end
        self.upHeap()  # Restore heap property

    def downHeap(self):  # Restore heap by bubbling down
        p = 1  # Start at root
        c = 2  # Left child
        key = self.heap[p]

        while c <= self.heapSize:
            if (c < self.heapSize) and (self.heap[c+1] < self.heap[c]):  # Right child smaller
                c += 1
            if key < self.heap[c]:  # Key is smaller than both children
                break
            self.heap[p] = self.heap[c]  # Move child up
            p = c  # Move down
            c *= 2  # Next left child
        self.heap[p] = key  # Place key

    def deleteHeap(self):  # Remove root element
        key = self.heap[1]  # Min element
        self.heap[1] = self.heap[self.heapSize]  # Replace with last
        self.heapSize -= 1
        self.downHeap()  # Restore heap
        return key

if __name__ == "__main__":
    H = MaxiHeap()
    data = [9, 7, 6, 4, 3, 2, 2, 1, 3]

    for s in data:
        H.insortingTime(s)
        print('Heap : ', H.heap[1:H.heapSize + 1])  # Show heap

    H.insortingTime(8)
    print('Heap : ', H.heap[1:H.heapSize + 1])
    print()

    print('[%d] is deleted.' % H.deleteHeap())  # Delete root
    print('Heap : ', H.heap[1:H.heapSize + 1])

# Output:
# Heap :  [9]
# Heap :  [7, 9]
# Heap :  [6, 9, 7]
# Heap :  [4, 6, 7, 9]
# Heap :  [3, 4, 7, 9, 6]
# Heap :  [2, 4, 3, 9, 6, 7]
# Heap :  [2, 4, 2, 9, 6, 7, 3]
# Heap :  [1, 2, 2, 4, 6, 7, 3, 9]
# Heap :  [1, 2, 2, 3, 6, 7, 3, 9, 4]
# Heap :  [1, 2, 2, 3, 6, 7, 3, 9, 4, 8]
#
# [1] is deleted.
# Heap :  [2, 3, 2, 4, 6, 7, 3, 9, 8]