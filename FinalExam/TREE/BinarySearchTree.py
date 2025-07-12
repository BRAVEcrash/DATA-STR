# Binary Search Tree (BST)
class TreeNode:
    def __init__(self, key):
        self.key = key           # Node key
        self.left = None         # Left child
        self.right = None        # Right child

def insert(root, key):
    if root is None:
        return TreeNode(key)     # Create new node if spot is empty
    if key < root.key:
        root.left = insert(root.left, key)   # Go left
    elif key > root.key:
        root.right = insert(root.right, key) # Go right
    else:
        pass  # Ignore duplicate keys
    return root

def preOrder(root):
    if root != None:
        print('%2d '% root.key, end=' ')  # Visit node
        preOrder(root.left)               # Visit left subtree
        preOrder(root.right)              # Visit right subtree

def delete(root, key):
    if root == None:
        return root  # Key not found
    if key < root.key:
        root.left = delete(root.left, key)    # Search left
    elif key > root.key:
        root.right = delete(root.right, key)  # Search right
    else:  # Found node to delete
        if root.left == None:
            return root.right  # One or zero children
        elif root.right == None:
            return root.left
        else:
            succ = getMinNode(root.right)  # In-order successor
            root.key = succ.key            # Replace with successor
            root.right = delete(root.right, succ.key)  # Delete successor
    return root

def getMinNode(root):
    while root != None and root.left != None:
        root = root.left  # Go to leftmost node
    return root

def display(root, msg):
    print(msg, end='')     # Show message
    preOrder(root)         # Show tree in pre-order
    print()

if __name__ == '__main__':
    root = None
    data = [35, 18, 7, 26, 3, 22, 30, 12, 26, 68, 99]

    for key in data:
        root = insert(root, key)
        display(root, '[Insert %2d] : ' % key)  # Show tree after each insert
    print()

    root = delete(root, 30)
    display(root, '[Delete 30] : ')  # Delete node 30

    root = delete(root, 26)
    display(root, '[Delete 26] : ')  # Delete node 26

    root = delete(root, 18)
    display(root, '[Delete 18] : ')  # Delete node 18


# Output:
# [Insert 35] : 35
# [Insert 18] : 35  18
# [Insert  7] : 35  18   7
# [Insert 26] : 35  18   7  26
# [Insert  3] : 35  18   7   3  26
# [Insert 22] : 35  18   7   3  26  22
# [Insert 30] : 35  18   7   3  26  22  30
# [Insert 12] : 35  18   7   3  12  26  22  30
# [Insert 26] : 35  18   7   3  12  26  22  30
# [Insert 68] : 35  18   7   3  12  26  22  30  68
# [Insert 99] : 35  18   7   3  12  26  22  30  68  99
#
# [Delete 30] : 35  18   7   3  12  26  22  68  99
# [Delete 26] : 35  18   7   3  12  22  68  99
# [Delete 18] : 35  22   7   3  12  68  99