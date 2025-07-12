class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = CircularNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # 처음 노드는 자기 자신 가리킴
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head

    def print_list(self, count=10):  # 무한 순환 방지를 위해 제한 출력
        curr = self.head
        for _ in range(count):
            if curr:
                print(curr.data, end=' → ')
                curr = curr.next
        print('...')
