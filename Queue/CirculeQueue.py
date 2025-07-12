class CircularQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = [None] * capacity
    def isEmpty(self):
        return self.front == self.rear
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity
    def enqueue(self,e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = e
        else:
            print("OverFlow")
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            print("OverFlow")

    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1)% self.capacity]
        else:
            print("UnderFlow")
    def displayQueue(self):
        print('Front: %d, Rear: %d' % (self.front, self.rear))

        i = self.front
        while i != self.rear:
            i = (i+1) % self.capacity
            print('[%c]'% self.array[i], end='')
        print()

if __name__ == '__main__':
    Q = CircularQueue()
    data = ['A','B','C,''D','E']

    for e in data:
        Q.enqueue(e)
    Q. displayQueue()