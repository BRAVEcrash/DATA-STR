# MST stands for Minimum Spanning Tree.

graph = {
    'A': [('B', 29), ('F', 15)],
    'B': [('A', 29), ('D', 16), ('E', 12)],
    'C': [('A', 22), ('F', 18)],
    'D': [('B', 16)],
    'E': [('B', 12), ('F', 25)],
    'F': [('A', 15), ('C', 18), ('E', 25)]
}

INF = 1000
dist = [INF] * len(graph)
visited = [False] * len(graph)

def findMin():
    minDist = INF
    vNum = -1  # Initialize properly

    for i in range(len(dist)):
        if not visited[i] and dist[i] < minDist:
            minDist = dist[i]
            vNum = i
    return vNum

def prim(vName):
    vCnt = len(graph)
    dist[ord(vName) - 65] = 0

    for _ in range(vCnt):
        vNum = findMin()
        if vNum == -1:
            break  # No more reachable nodes
        vName = chr(vNum + 65)

        for j in range(vCnt):
            if dist[j] == INF:
                print(" * ", end=' ')
            else:
                print('[%c (%d)]' % (chr(j + 65), dist[j]), end=' ')
        print(' -> Visiting:', vName)

        visited[vNum] = True

        for e in graph[vName]:
            nextV = ord(e[0]) - 65
            if not visited[nextV] and e[1] < dist[nextV]:
                dist[nextV] = e[1]

if __name__ == '__main__':
    prim('A')

# Output:
# [A (0)]  *   *   *   *   *   -> Visiting: A
# [A (0)] [B (29)]  *   *   *  [F (15)]  -> Visiting: F
# [A (0)] [B (29)] [C (18)]  *  [E (25)] [F (15)]  -> Visiting: C
# [A (0)] [B (29)] [C (18)]  *  [E (25)] [F (15)]  -> Visiting: E
# [A (0)] [B (12)] [C (18)]  *  [E (25)] [F (15)]  -> Visiting: B
# [A (0)] [B (12)] [C (18)] [D (16)] [E (25)] [F (15)]  -> Visiting: D