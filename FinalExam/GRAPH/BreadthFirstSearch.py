# 기본 탐색 전략:
# – 깊이 우선 탐색 (Depth First Search, DFS)
# – 너비 우선 탐색 (Breadth First Search: BFS)

from queue import Queue
def BFS_AL(vtx, aList, s):
    n = len(vtx)
    visited = [False] * n
    Q = Queue()

    Q.put(s)
    visited[s] = True

    while not Q.empty():
        s = Q.get()
        print(vtx[s], end=' ')
        for v in aList[s]:
            if not visited[v]:
                Q.put(v)
                visited[v] = True

# Vertex list
vtx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Adjacency list (each index corresponds to a vertex in `vtx`)
aList = [
    [1, 2],    # A -> B, C
    [0, 3],    # B -> A, D
    [0, 4],    # C -> A, E
    [1, 5],    # D -> B, F
    [2, 6],    # E -> C, G
    [3, 7],    # F -> D, H
    [4],       # G -> E
    [5]        # H -> F
]

# Run BFS starting from vertex 'A' (index 0)
print('BFS_AL(출발:A): ', end='')
BFS_AL(vtx, aList, 0)
print()

# Output:
# BFS_AL(출발:A): A B C D E F G H
