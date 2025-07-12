class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DLlistype:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def insert(self, pos, data):
        if pos < 1 or pos > self.size + 1:
            print("Invalid Pos")
            return

        p = self.head
        for _ in range(pos):
            p = p.next

        newNode = Node(data, p.prev, p)
        p.prev.next = newNode
        p.prev = newNode

        self.size += 1

    def printList(self):
        p = self.head.next
        while p != self.tail:
            print("[%s] <=> " % p.data, end=" ")
            p = p.next
        print("NULL")

# 테스트 코드
if __name__ == '__main__':
    Dl = DLlistype()
    Dl.insert(1, 'C'); Dl.printList()
    Dl.insert(2, 'A'); Dl.printList()
    Dl.insert(3, 'B'); Dl.printList()
    Dl.insert(4, 'C'); Dl.printList()
