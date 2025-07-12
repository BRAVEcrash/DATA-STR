# AVL Tree
class TreeNode:
    def __init__(self, key):
        self.key = key              # Node key
        self.left = None            # Left child
        self.right = None           # Right child

def getHeight(root):
    if root == None:
        return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))  # Height of node

def getBalance(root):
    if root == None:
        return 0
    return getHeight(root.left) - getHeight(root.right)  # Balance factor

def rotateleft(p):  # RR or RL case rotation
    c = p.right
    p.right = c.left
    c.left = p
    return c

def rotateright(p):  # LL or LR case rotation
    c = p.left
    p.left = c.right
    c.right = p
    return c

def insert(root, key):  # AVL insert
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert(root.left, key)   # Go left
    elif key > root.key:
        root.right = insert(root.right, key) # Go right
    else:
        pass  # Ignore duplicates

    balance = getBalance(root)  # Check balance after insert

    # LL case
    if balance > 1 and key < root.left.key:
        print('------ LL Type -------')
        return rotateright(root)
    # LR case
    if balance > 1 and key > root.left.key:
        print('------ LR Type -------')
        root.left = rotateleft(root.left)
        return rotateright(root)
    # RL case
    if balance < -1 and key < root.right.key:
        print('------ RL Type -------')
        root.right = rotateright(root.right)
        return rotateleft(root)
    # RR case
    if balance < -1 and key > root.right.key:
        print('------ RR Type -------')
        return rotateleft(root)

    return root  # Return unchanged (or updated) root

def preOrder(root):  # Pre-order traversal
    if root != None:
        print('%2d ' % root.key, end=' ')
        preOrder(root.left)
        preOrder(root.right)

def delete(root, key):  # BST delete (not AVL-balanced here)
    if root == None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            succ = getMinNode(root.right)  # Get successor
            root.key = succ.key            # Replace key
            root.right = delete(root.right, succ.key)  # Delete successor
    return root

def getMinNode(root):  # Minimum value node
    while root != None and root.left != None:
        root = root.left
    return root

def display(root, msg):  # Show tree with message
    print(msg, end='')
    preOrder(root)
    print()

if __name__ == '__main__':
    root = None
    data = [7, 8, 9, 2, 1, 5, 3, 6, 4]  # Data to insert

    for i in range(9):
        root = insert(root, data[i])  # Insert into AVL tree
        display(root, '[Insert %2d] : ' % data[i])
    print()

# Output:
# [Insert  7] :  7
# [Insert  8] :  7   8
# ------ RR Type -------
# [Insert  9] :  8   7   9
# [Insert  2] :  8   7   2   9
# ------ LL Type -------
# [Insert  1] :  8   2   1   7   9
# ------ LR Type -------
# [Insert  5] :  7   2   1   5   8   9
# [Insert  3] :  7   2   1   5   3   8   9
# [Insert  6] :  7   2   1   5   3   6   8   9
# ------ RL Type -------
# [Insert  4] :  7   3   2   1   5   4   6   8   9