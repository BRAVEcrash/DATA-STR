class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLinkedList:
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
            print("Invalid Position")
            return
        p = self.head
        for _ in range(pos):
            p = p.next
        newNode = Node(data, p.prev, p)
        p.prev.next = newNode
        p.prev = newNode
        self.size += 1

    def delete(self, key):
        if key < 1 or key > self.size:
            return print("Invalid Position")
            
        p = self.head
        for _ in range(key):
            p = p.next

        p.prev.next = p.next
        p.next.prev = p.prev
        data = p.data

        self.size -= 1
        return data

    def printList(self):
        p = self.head.next
        while p != self.tail:
            print("[%s] <=> " % p.data, end='')
            p = p.next
        print("Null")

    def insertFirst(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def insertLast(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def displayForward(self):
        temp = self.head
        print("Forward: ", end='')
        while temp:
            print(f"[{temp.data}]", end='<->')
            temp = temp.next
        print("None")

    def displayBackward(self):
        temp = self.head
        if temp is None:
            print("Backward: None")
            return
        while temp.next:
            temp = temp.next

        print("Backward: ", end='')
        while temp:
            print(f"[{temp.data}]", end=" <-> ")
            temp = temp.prev
        print("None")


if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.insertFirst(10)
    dll.insertFirst(5)
    dll.insertLast(15)
    dll.insertLast(20)

    dll.displayForward()
    dll.displayBackward()
    Dl = DoubleLinkedList()
    Dl.insert(1, 'C');
    Dl.printList()
    Dl.insert(2, 'A');
    Dl.printList()
    Dl.insert(3, 'B');
    Dl.printList()
    Dl.insert(4, 'C');
    Dl.printList()

# Forward: [5]<->[10]<->[None]<->[None]<->[15]<->[20]<->None
# Backward: [20] <-> [15] <-> [None] <-> [None] <-> [10] <-> [5] <-> None
# [C] <=> Null
# [C] <=> [A] <=> Null
# [C] <=> [A] <=> [B] <=> Null
# [C] <=> [A] <=> [B] <=> [C] <=> Null