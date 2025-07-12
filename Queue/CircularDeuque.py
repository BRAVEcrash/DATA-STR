from CirculeQueue import CircularQueue
class CircularDeque(CircularQueue):

    def __init__(self):
        super().__init__()
    def addRear(self, item): self.enqueue(item)
    def deleteFront(self): return self.dequeue()
    def getFront(self): return self.peek()

    def addFront(self, item):
        if not self.isFull():
            self.array[self.front] = item
            self.front= (self.front-1 + self.capacity) % self.capacity
        else:
            print("OverFlow")
    def deleteRear(self):
        if not self.isEmpty():
            item = self.array[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return item
        else:
            print("OverFlow")
