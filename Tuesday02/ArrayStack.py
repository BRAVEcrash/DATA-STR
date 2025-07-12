from math import e


class ArrayStack:

    def __init__(self, capacity = 20):
        self.capacity = capacity
        self.top = -1
        self.array = [None] * capacity

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity -1

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else:
            print("OverFlow")

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else:
            print("UnderFlow")

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            print("UnderFlow")

    #Exam part;
    def sortedInsert(self, data):
        if(self.isEmpty() or data < self.peek()):
            self.push(data)
        else:
            temp = self.pop()
            self.sortedInsert(data)
            self.push(temp)

    def displayStack(self):
        print()
        for i in range(self.top, -1, -1):
            print(f"| {self.array[i]} |")
            print("--------")
        print()


if __name__ == "__main__":
    # S = ArrayStack()
    #
    # data = [4,2,3,1,5,6,7,8,9,10]
    # for i in data:
    #     S.push(e)
    # S.displayStack()
    #
    # print("Poped", S.pop())
    # S.displayStack()
    # print("Peeked", S.peek())
    # S.displayStack()

    S = ArrayStack()
    input = ['A', 'C', 'B', 'F', 'D', 'C']
    for i in range(6):
        S.print[i]
        S.sprint
