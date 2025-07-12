class ArrayQueue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = [None] * capacity

    def isEmpty(self):
        return self.top == -1
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, e):
        if not self.isEmpty():
            self.front +=1
            return self.array[self.front]
        else:
            print("Underflow")
    def display(self):
        print("Front: %d, Rear : %d" % (self.front, self.rear))
        print(self.array[self.front])