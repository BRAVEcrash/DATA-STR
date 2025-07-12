#(실기) (이진 트리 주어진 후) 해당 이진
#트리를 스택을 이용하여 반전 시켜라 (출력은 레벨 순회를 따르도록 출력함
#(이 조건은 문제에 직접제시가 아닌 출력형식으로 간접적으로 제시))


# # English Translation:
# # (Practical) (After a binary tree is given)
# Use a stack to reverse the binary tree.
# (The output should follow a level order traversal format.
# (This condition is not directly stated in the problem but is implied through the output format))

# # Interpretation:
# # You are given a binary tree and need to reverse it
# using a stack, and then print the nodes in level-order
# traversal after the reversal.
import queue

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def reverse_with_stack(self, root):
        if root is None:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left  # Swap children
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    def levelOrder(self, root):
        if root is None:
            return
        Q = queue.Queue()
        Q.put(root)
        while not Q.empty():
            root = Q.get()
            print(root.data, end= '')
            if root.left:
                Q.put(root.left)
            if root.right:
                Q.put(root.right)

if __name__ == '__main__':
    # 트리 구성
    T = BinaryTree()
    N6 = Node('F')
    N5 = Node('E')
    N4 = Node('D')
    N3 = Node('C', N6, None)
    N2 = Node('B', N4, N5)
    N1 = Node('A', N2, N3)  # Root
    T.root = N1

    print("Before Reverse (Level-order): ", end='')
    T.levelOrder(T.root)
    print()

    # 스택을 이용해 트리 반전
    T.reverse_with_stack(T.root)

    print("After Reverse (Level-order): ", end='')
    T.levelOrder(T.root)
    print()


# Before Reverse (Level-order): [A] [B] [C] [D] [E] [F]
# After Reverse (Level-order): [A] [C] [B] [F] [E] [D]
