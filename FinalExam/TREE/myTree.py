class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    # независимо от ветки, возвращаем корень текущего (под)дерева
    return root


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value, end=' ')
    inorder(node.right)


if __name__ == '__main__':
    root = None
    for x in [10, 5, 15]:
        root = insert(root, x)

    print("In-order before:", end=' ')
    inorder(root)
    print()

    # Вставляем ещё одну «5» и сохраняем результат
    root = insert(root, 5)

    print("In-order after inserting 5:", end=' ')
    inorder(root)
    print()
