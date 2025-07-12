# Hashing:
# 1.Open Addressing
# 2.Chaining
M = 13  # Размер хеш-таблицы

class HashTableChaining:
    def __init__(self):
        self.table = [[] for _ in range(M)]  # Каждая ячейка — это список

    def hashFn(self, key):
        return key % M

    def insert(self, key):
        hashVal = self.hashFn(key)
        if key not in self.table[hashVal]:  # Проверка на дубликаты
            self.table[hashVal].append(key)

    def search(self, key):
        hashVal = self.hashFn(key)
        if key in self.table[hashVal]:
            return hashVal
        return -1

    def delete(self, key):
        hashVal = self.hashFn(key)
        if key in self.table[hashVal]:
            self.table[hashVal].remove(key)
            print(f"Deleted key {key} from bucket {hashVal}")
        else:
            print(f"Key {key} not found.")

    def display(self):
        print('\nBucket   Keys')
        print('=================')
        for i in range(M):
            print(f'HT[{i:2d}] : {self.table[i]}')

# === Пример использования ===

if __name__ == '__main__':
    HT = HashTableChaining()
    data = [10, 20, 30, 40, 33, 46, 50, 60]

    for d in data:
        print(f'h({d}) = {HT.hashFn(d)}')
        HT.insert(d)

    HT.display()

    print("\nSearch(33) ---->", HT.search(33))
    HT.delete(33)
    HT.delete(99)  # Не существует
    HT.display()

# Output:
# h(10) = 10
# h(20) = 7
# h(30) = 4
# h(40) = 1
# h(33) = 7
# h(46) = 7
# h(50) = 11
# h(60) = 8
#
# Bucket   Keys
# =================
# HT[ 0] : []
# HT[ 1] : [40]
# HT[ 2] : []
# HT[ 3] : []
# HT[ 4] : [30]
# HT[ 5] : []
# HT[ 6] : []
# HT[ 7] : [20, 33, 46]
# HT[ 8] : [60]
# HT[ 9] : []
# HT[10] : [10]
# HT[11] : [50]
# HT[12] : []
#
# Search(33) ----> 7
# Deleted key 33 from bucket 7
# Key 99 not found.
#
# Bucket   Keys
# =================
# HT[ 0] : []
# HT[ 1] : [40]
# HT[ 2] : []
# HT[ 3] : []
# HT[ 4] : [30]
# HT[ 5] : []
# HT[ 6] : []
# HT[ 7] : [20, 46]
# HT[ 8] : [60]
# HT[ 9] : []
# HT[10] : [10]
# HT[11] : [50]
# HT[12] : []