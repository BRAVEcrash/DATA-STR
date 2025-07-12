class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


# Insertion
def insert_bst(node, new_node):
    if node is None:
        return new_node
    if new_node.key < node.key:
        node.left = insert_bst(node.left, new_node)
    else:
        node.right = insert_bst(node.right, new_node)
    return node


# Deletion
def delete_bst(node, key):
    if node is None:
        return None
    if key < node.key:
        node.left = delete_bst(node.left, key)
    elif key > node.key:
        node.right = delete_bst(node.right, key)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        temp = search_min_bst(node.right)
        node.key, node.value = temp.key, temp.value
        node.right = delete_bst(node.right, temp.key)
    return node


# Search by key
def search_bst(node, key):
    if node is None or node.key == key:
        return node
    if key < node.key:
        return search_bst(node.left, key)
    else:
        return search_bst(node.right, key)


# Search by value
def search_value_bst(node, value):
    if node is None:
        return None
    if node.value == value:
        return node
    left_result = search_value_bst(node.left, value)
    if left_result:
        return left_result
    return search_value_bst(node.right, value)


# Find min
def search_min_bst(node):
    while node and node.left:
        node = node.left
    return node


# Find max
def search_max_bst(node):
    while node and node.right:
        node = node.right
    return node


# Inorder traversal (for display)
def inorder(node):
    if node:
        inorder(node.left)
        print(f'({node.key}:{node.value})', end=' ')
        inorder(node.right)


class BSTMap:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def findMax(self):
        return search_max_bst(self.root)

    def findMin(self):
        return search_min_bst(self.root)

    def search(self, key):
        return search_bst(self.root, key)

    def searchValue(self, value):
        return search_value_bst(self.root, value)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        self.root = insert_bst(self.root, n)

    def delete(self, key):
        self.root = delete_bst(self.root, key)

    def display(self, msg='BSTMap : '):
        print(msg, end='')
        inorder(self.root)
        print()


# Main program
if __name__ == '__main__':
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
    value = ["삼오", "일팔", "영칠", "이육", "일이", "영상", "육팔", "이이", "삼영", "구구"]

    map = BSTMap()
    map.display("[삽입 전 : ")

    for i in range(len(data)):
        map.insert(data[i], value[i])
        map.display("[삽입 %d : " % data[i])

    print("[최대 키 : ", map.findMax().key)
    print("[최소 키 : ", map.findMin().key)

    print("[탐색 26 : ", '성공' if map.search(26) else '실패')
    print("[탐색 25 : ", '성공' if map.search(25) else '실패')
    print("[탐색 일팔 : ", '성공' if map.searchValue("일팔") else '실패')
    print("[탐색 일칠 : ", '성공' if map.searchValue("일칠") else '실패')

    map.delete(3)
    map.display("[삭제 3 : ")

    map.delete(68)
    map.display("[삭제 68 : ")

    map.delete(18)
    map.display("[삭제 18 : ")

    map.delete(35)
    map.display("[삭제 35 : ")

# Output:
# [삽입 전 :
# [삽입 35 : (35:삼오)
# [삽입 18 : (18:일팔) (35:삼오)
# [삽입 7 : (7:영칠) (18:일팔) (35:삼오)
# [삽입 26 : (7:영칠) (18:일팔) (26:이육) (35:삼오)
# [삽입 12 : (7:영칠) (12:일이) (18:일팔) (26:이육) (35:삼오)
# [삽입 3 : (3:영상) (7:영칠) (12:일이) (18:일팔) (26:이육) (35:삼오)
# [삽입 68 : (3:영상) (7:영칠) (12:일이) (18:일팔) (26:이육) (35:삼오) (68:육팔)
# [삽입 22 : (3:영상) (7:영칠) (12:일이) (18:일팔) (22:이이) (26:이육) (35:삼오) (68:육팔)
# [삽입 30 : (3:영상) (7:영칠) (12:일이) (18:일팔) (22:이이) (26:이육) (30:삼영) (35:삼오) (68:육팔)
# [삽입 99 : (3:영상) (7:영칠) (12:일이) (18:일팔) (22:이이) (26:이육) (30:삼영) (35:삼오) (68:육팔) (99:구구)
# [최대 키 :  99
# [최소 키 :  3
# [탐색 26 :  성공
# [탐색 25 :  실패
# [탐색 일팔 :  성공
# [탐색 일칠 :  실패
# [삭제 3 : (7:영칠) (12:일이) (18:일팔) (22:이이) (26:이육) (30:삼영) (35:삼오) (68:육팔) (99:구구)
# [삭제 68 : (7:영칠) (12:일이) (18:일팔) (22:이이) (26:이육) (30:삼영) (35:삼오) (99:구구)
# [삭제 18 : (7:영칠) (12:일이) (22:이이) (26:이육) (30:삼영) (35:삼오) (99:구구)
# [삭제 35 : (7:영칠) (12:일이) (22:이이) (26:이육) (30:삼영) (99:구구)