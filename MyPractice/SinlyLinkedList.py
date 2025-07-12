class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def insertFirst(self, data):
        node = Node(data, self.head)
        self.head = node
        self.size += 1

    def getNode(self, pos):
        p = self.head
        for _ in range(1, pos - 1):
            if p is None:
                return None
            p = p.next
        return p

    def insert(self, pos, data):
        if pos == 1:
            self.insertFirst(data)
        elif pos <= self.size + 1:
            p = self.getNode(pos - 1)
            if p:
                node = Node(data, p.next)
                p.next = node
                self.size += 1
            else:
                print("Invalid position (null node)")
        else:
            print("Invalid position")

    def deleteFirst(self):
        if not self.isEmpty():
            p = self.head
            self.head = p.next
            self.size -= 1
            return p.data
        else:
            print("UnderFlow")
        return None

    def delete(self, pos):
        if pos == 1:
            return self.deleteFirst()
        elif pos <= self.size:
            q = self.getNode(pos - 1)
            if q and q.next:
                p = q.next
                q.next = p.next
                self.size -= 1
                return p.data
            else:
                print("Invalid Pos")
                return None
        else:
            print("InvalidPos")
        return None

    def display(self):
        p = self.head
        while p is not None:
            print('[%s] - > ' % (p.data), end='')
            p = p.next
        print("None")

if __name__ == '__main__':
    L = LinkedList()
    L.insertFirst('A')
    L.insertFirst('B')
    L.insert(2, 'C')
    L.display()

    print('[%s] is deleted' % L.deleteFirst())
    L.display()
    print('[%s] is deleted' % L.delete(0))
    L.display()
