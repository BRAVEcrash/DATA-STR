import queue
class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    def preorder(self, root):
        if root is not None:
            print ('[%c]'% root.data, end= ' ')
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print('[%c]'% root.data, end= ' ')
            self.inorder(root.right)
    def postorder(self, root):
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print('[%c]'% root.data, end= ' ')
    def levelOrder(self, root):
        if root is None:
            return
        Q = queue.Queue()
        Q.put(root)
        while not Q.empty():
            root = Q.get()
            print('[%c]'% root.data, end= ' ')
            if root.left:
                Q.put(root.left)
            if root.right:
                Q.put(root.right)

    def count_node(self, root):
        if root is  None:
            return 0
        else:
            return 1 + self.count_node(root.left) + self.count_node(root.right)
    def count_leaf(self,root):
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            return self.count_leaf(root.left) + self.count_leaf(root.right)

    def get_height(self, root):
        if root == None:
            return 0
        hLeft = self.get_height(root.left)
        hRight = self.get_height(root.right)
        if (hLeft > hRight):
            return hLeft + 1
        else:
            return hRight + 1

    def treeReverse(self, root):
        if root is not None:
            root.left, root.right = root.right, root.left
            self.treeReverse(root.left)
            self.treeReverse(root.right)


if __name__ == '__main__':
    T = BinaryTree()

    N6 = Node('F')
    N5 = Node('E')
    N4 = Node('D')
    N3 = Node('C', N6, None)
    N2 = Node('B',N4, N5)
    N1 = Node('A', N2, N3)

    print('Pre : ', end= ''); T.preorder(N1); print()
    print('In : ', end=''); T.inorder(N1); print()
    print('Post : ', end=''); T.postorder(N1); print()
    print('Level : ', end=''); T.levelOrder(N1); print()
    print('Count_node : ', end=''); print(T.count_node(N1))
    print('Count_leaf : ', end=''); print(T.count_leaf(N1))
    print('Count_height : ', end=''); print(T.get_height(N1))

    T.treeReverse(N1)
    print('Pre : ', end=''); T.preorder(N1); print()
    print('In : ', end=''); T.inorder(N1); print()
    print('Post : ', end=''); T.postorder(N1); print()
    print('Level : ', end=''); T.levelOrder(N1); print()

# Output:
# Pre : [A] [B] [D] [E] [C] [F]
# In : [D] [B] [E] [A] [F] [C]
# Post : [D] [E] [B] [F] [C] [A]
# Level : [A] [B] [C] [D] [E] [F]
# Count_node : 6
# Count_leaf : 3
# Count_height : 3
# Pre : [A] [C] [F] [B] [E] [D]
# In : [C] [F] [A] [E] [B] [D]
# Post : [F] [C] [E] [D] [B] [A]
# Level : [A] [C] [B] [F] [E] [D]