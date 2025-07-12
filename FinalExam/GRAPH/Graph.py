# Multiple ways to store a graph:

# 1.Adjacency Matrix Representation
# 2.Adjacency List Representation

#1.무방향 그래프: 인접 행렬 표현 (MATRIX)
vName = ['A','B','C','D','E','F','G','H']
visited = [False]*len(vName)
Graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]

]
def printGraph():
    n = len(vName)
    print(" ABCDEFGH")
    for i in range(n):
        print('[%c]' % vName[i], end=' ')
        for j in range(n):
            print('%d' % Graph[i][j], end=' ')
        print("  !")

def rDfs(s):
    visited[s] = True
    print('[%s]' % vName[s], end=' ')
    for t in range(len(vName)):
        if (Graph[s][t] == 1 and visited[t] == False):
            rDfs(t)
if __name__ == '__main__':
    printGraph()
    print('\nDFC: ', end='')
    rDfs(1)

# Output:
#  ABCDEFGH
# [A] 0 1 1 0 0 0 0 0   !
# [B] 1 0 0 1 0 0 0 0   !
# [C] 1 0 0 1 1 0 0 0   !
# [D] 0 1 1 0 0 1 0 0   !
# [E] 0 0 1 0 0 0 1 1   !
# [F] 0 0 0 1 0 0 0 0   !
# [G] 0 0 0 0 1 0 0 1   !
# [H] 0 0 0 0 1 0 1 0   !
#
# DFC: [B] [A] [C] [D] [F] [E] [G] [H] Total Weight =  174
# [AB 29][AF 10]
# [BC 16][BG 15]
# [CD 12]
# [DE 22][DG 18]
# [EF 27][EG 25]

######################################################################

#2.가중치 그래프: 인접 행렬 표현 (MATRIX)
Graph = {
    'A': [('B', 29), ('F', 10)],
    'B': [('A', 29), ('C', 16), ('G', 15)],
    'C': [('B', 16), ('D', 12)],
    'D': [('C', 12), ('E', 22), ('G', 18)],
    'E': [('D', 22), ('F', 27), ('G', 25)],
    'F': [('A', 10), ('E', 27)],
    'G': [('B', 15), ('D', 18), ('E', 25)]
}
def weightSum():
    sum = 0
    for v in Graph:
        for e in Graph[v]:
            sum += e[1]
    return sum//2
def display():
    for v in Graph:
        for e in Graph[v]:
            if v < e[0]:
                print('[%s%s %d]' % (v,e[0], e[1]), end='')
        print()
if __name__ == '__main__':
    print('Total Weight = ', weightSum())
    display()

# Output:
# Total Weight =  174
# [AB 29][AF 10]
# [BC 16][BG 15]
# [CD 12]
# [DE 22][DG 18]
# [EF 27][EG 25]