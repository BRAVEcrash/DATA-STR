# INF = 1000
#
# vName = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# Graph = [
#     [ 0, 7, INF, INF, 3, 10, INF],
#     [ 7, 0, 4, 10, 2, 6, INF],
#     [INF, 4, 0, 2, INF, INF, INF],
#     [INF, 10, 2, 0, 11, 9, 4],
#     [ 3, 2, INF, 11, 0, 13, 5],
#     [ 10, 6, INF, 9, 13, 0, INF],
#     [INF, INF, INF, 4, 5, INF, 0]
# ]
#
# vCnt = len(vName)
# dist = [INF] * vCnt
# visited = [False] * vCnt
#
# def findMin():
#     minDist = INF
#     minV = 0
#     for v in range(vCnt):
#         if visited[v] == False and dist[v] < minDist:
#             minDist = dist[v]
#             minV = v
#         return minV
#
# def display():
#     for i in range(vCnt):
#         if dist[i] < INF:
#             print(f"{vName[i]}: {dist[i]}")
#         else:
#             print(f"{vName[i]}: INF")
# def dijkstra(s):
#     dist[ord(s) -65] = 0
#
#     for i in range(vCnt):
#         s = findMin()
#         visited[s] = True
#
#         for t in range(vCnt):
#             if dist[t] < dist[s] + Graph[s][t]:
#                 dist[t] = dist[s] + Graph[s][t]
# if __name__ == '__main__':
#     dijkstra()
INF = 1000

vName = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
Graph = [
    [ 0, 7, INF, INF, 3, 10, INF],
    [ 7, 0, 4, 10, 2, 6, INF],
    [INF, 4, 0, 2, INF, INF, INF],
    [INF, 10, 2, 0, 11, 9, 4],
    [ 3, 2, INF, 11, 0, 13, 5],
    [10, 6, INF, 9, 13, 0, INF],
    [INF, INF, INF, 4, 5, INF, 0]
]

vCnt = len(vName)
dist = [INF] * vCnt
visited = [False] * vCnt

def findMin():
    minDist = INF
    minV = -1
    for v in range(vCnt):
        if not visited[v] and dist[v] < minDist:
            minDist = dist[v]
            minV = v
    return minV

def display():
    for i in range(vCnt):
        if dist[i] < INF:
            print(f"{vName[i]}: {dist[i]}")
        else:
            print(f"{vName[i]}: INF")

def dijkstra(startChar):
    start = ord(startChar) - 65
    dist[start] = 0

    for _ in range(vCnt):
        u = findMin()
        if u == -1:
            break
        visited[u] = True

        for v in range(vCnt):
            if not visited[v] and Graph[u][v] != INF:
                if dist[v] > dist[u] + Graph[u][v]:
                    dist[v] = dist[u] + Graph[u][v]

if __name__ == '__main__':
    dijkstra('A')
    display()
# Output:
# A: 0
# B: 5
# C: 9
# D: 11
# E: 3
# F: 10
# G: 8