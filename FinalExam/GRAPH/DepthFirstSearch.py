# 기본 탐색 전략:
# – 깊이 우선 탐색 (Depth First Search, DFS)
# – 너비 우선 탐색 (Breadth First Search: BFS)

from queue import LifoQueue
vName = ['A','B','C','D','E','F','G','H']
visited = [False]*len(vName)

#List of indexes adjacent peak (인접 정점의 인덱스 리스트를)
AdjVar = [
    [1, 2],
    [0, 3],
    [0, 3, 4],
    [1, 2, 5],
    [2, 6, 7],
    [3],
    [4, 7],
    [4, 6],
]

class Stack(LifoQueue):
    def peek(self):
        if not self.empty():
            return self.queue[-1]
        raise Exception('Stack is empty')

def iDfs(s):
    S = Stack()
    S.put(s)
    visited[s] = True
    print('[%s]' % vName[s], end=' ')
    while not S.empty():
        s = S.peek()
        flag = False
        for t in AdjVar[s]:
            if not visited[t]:
                S.put(t)
                visited[t] = True  # Mark as visited here!
                print('[%s]' % vName[t], end=' ')
                flag = True
                break
        if not flag:
            S.get()

if __name__ == '__main__':
    print('\nDFC: ', end='')
    iDfs(1)

# Output:
# DFC: [B] [A] [C] [D] [F] [E] [G] [H]