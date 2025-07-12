# Hashing:
# 1.Open Addressing
# 2.Chaining
M = 13  # Table size

class Hashtable:
    def __init__(self):
        self.table = [0] * M  # Initialize table with 0s (empty)

    def hashFn(self, key):
        return key % M  # Simple modulo hash function

    def insert(self, key):
        hashVal = self.hashFn(key)
        for i in range(M):
            bucket = (hashVal + i) % M  # Linear probing
            if self.table[bucket] == 0:  # Empty slot found
                self.table[bucket] = key
                break

    def search(self, key):
        hashVal = self.hashFn(key)
        for i in range(M):
            bucket = (hashVal + i) % M  # Linear probing
            if self.table[bucket] == 0: return -1  # Key not found
            elif self.table[bucket] == key: return bucket  # Key found
        return -1

    def delete(self, key):
        hashVal = self.hashFn(key)
        for i in range(M):
            bucket = (hashVal + i) % M  # Linear probing
            if self.table[bucket] == 0:
                print("No key to delete")  # Key not found
                return
            elif self.table[bucket] == key:
                print("Delete Key (%d) at bucket (%d)." % (key, bucket))
                self.table[bucket] = 0  # Mark as empty
                return bucket

    def display(self):
        print('\nBucket   Key')
        print('=================')
        for i in range(M):
            print('HT[%2d] : %2d' % (i, self.table[i]))

if __name__ == '__main__':
    HT = Hashtable()
    data = [10, 20, 30, 40, 33, 46, 50, 60]  # Data to insert
    for d in data:
        print('h(%d)=%2d' % (d, HT.hashFn(d)), end = ' ')  # Show hash
        HT.insert(d)
        print(HT.table)
    HT.display(); print()

    print("Search(46) ----> ", HT.search(46))  # Search test
    HT.delete(9)  # Delete non-existent key
    HT.display(); print()

# Output:
# h(10)=10 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0]
# h(20)= 7 [0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 10, 0, 0]
# h(30)= 4 [0, 0, 0, 0, 30, 0, 0, 20, 0, 0, 10, 0, 0]
# h(40)= 1 [0, 40, 0, 0, 30, 0, 0, 20, 0, 0, 10, 0, 0]
# h(33)= 7 [0, 40, 0, 0, 30, 0, 0, 20, 33, 0, 10, 0, 0]
# h(46)= 7 [0, 40, 0, 0, 30, 0, 0, 20, 33, 46, 10, 0, 0]
# h(50)=11 [0, 40, 0, 0, 30, 0, 0, 20, 33, 46, 10, 50, 0]
# h(60)= 8 [0, 40, 0, 0, 30, 0, 0, 20, 33, 46, 10, 50, 60]
#
# Bucket   Key
# =================
# HT[ 0] :  0
# HT[ 1] : 40
# HT[ 2] :  0
# HT[ 3] :  0
# HT[ 4] : 30
# HT[ 5] :  0
# HT[ 6] :  0
# HT[ 7] : 20
# HT[ 8] : 33
# HT[ 9] : 46
# HT[10] : 10
# HT[11] : 50
# HT[12] : 60
#
# Search(46) ---->  9
# No key to delete
#
# Bucket   Key
# =================
# HT[ 0] :  0
# HT[ 1] : 40
# HT[ 2] :  0
# HT[ 3] :  0
# HT[ 4] : 30
# HT[ 5] :  0
# HT[ 6] :  0
# HT[ 7] : 20
# HT[ 8] : 33
# HT[ 9] : 46
# HT[10] : 10
# HT[11] : 50
# HT[12] : 60

