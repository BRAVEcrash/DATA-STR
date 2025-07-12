class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class ListType:
    def __init__(self):
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def insertFirst(self, data):
        node = Node(data, None)

        if self.isEmpty():
            node.next = node
            self.tail = node
        else:
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insertLast(self, data):
        node = Node(data, None)

        if self.isEmpty():
            node.next = node
            self.tail = node
        else:
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node
        self.size += 1

    def deleteFirst(self):
        if not self.isEmpty():
            p = self.tail
            q = p.next

            if p == q:
                self.tail = None
            else:
                p.next = q.next
            self.size -= 1
            return q.data
        else:
            print("The list is empty")

    def deleteLast(self):
        if not self.isEmpty():
            p = self.tail
            q = p.next

            if p == q:
                self.tail = None
            else:
                while q.next != p:
                    q = q.next
                q.next = p.next
                self.tail = q
            self.size -= 1
            return q.data
        else:
            print("The list is empty")

    def printList(self):
        p = self.tail
        if not self.isEmpty():
            while True:
                print('[%s] -> ' % (p.next.data), end='')
                p = p.next

                if p == self.tail:
                    break
        print("\b\b\b   ")

if __name__ == "__main__":
    L = ListType()

    L.insertLast('C'); L.printList()
    L.insertFirst('A'); L.printList()
    L.insertFirst('B'); L.printList()
    L.insertLast('C'); L.printList()

    print('[%c] is deleted' % L.deleteFirst()); L.printList()
    print('[%c] is deleted' % L.deleteLast()); L.printList()

