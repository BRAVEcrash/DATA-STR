from queue import Queue

# Adjacent peak set (인접 정점 집합)
Adjacent = {
    'A': {'B', 'C'},
    'B': {'A', 'D'},
    'C': {'A', 'D', 'E'},
    'D': {'B', 'C', 'F'},
    'E': {'C', 'G', 'H'},
    'F': {'D'},
    'G': {'E', 'H'},
    'H': {'E', 'G'}
}

visited = {}

def BFS(s):
    Q = Queue()
    Q.put(s)
    visited[s] = True
    print('[%c] ' % s, end='')

    while not Q.empty():
        c = Q.get()
        for t in Adjacent[c]:
            if t not in visited:
                Q.put(t)
                visited[t] = True
                print('[%c] ' % t, end='')

if __name__ == '__main__':
    print('BFS: ', end='')
    BFS('D')
