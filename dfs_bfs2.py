# 그래프 자체가 들어오는 케이스
from collections import deque

n, m = map(int, input().split())
adj = [list(input()) for _ in range(n)] #간선 입력값

for i in range(n):
    for j in range(m):
        adj[i][j] = int(adj[i][j])
def miro(i,j):
    
    queue = deque([[i, j]])

    while(not(i == n - 1 and j == m - 1)):
        print(adj[0])
        print(adj[1])
        print(adj[2])
        print(adj[3])
        print()
        cur = queue.popleft()
        i = cur[0]
        j = cur[1]
        print(i, j)
        if i - 1 >=0:
            if adj[i - 1][j] == 1 and not(i - 1 == 0 and j == 0):
                adj[i - 1][j] = adj[i][j] + 1
                queue.append([i - 1, j])
        if i + 1 < n:
            if adj[i + 1][j] == 1 and not(i + 1== 0 and j == 0):
                adj[i + 1][j] = adj[i][j] + 1
                queue.append([i + 1, j])
        if j - 1 >= 0:
            if adj[i][j - 1] == 1 and not(i == 0 and j - 1 == 0):
                adj[i][j - 1] = adj[i][j] + 1
                queue.append([i, j - 1])
        if j + 1 < m :
            if adj[i][j + 1] == 1 and not(i == 0 and j + 1 == 0):
                adj[i][j + 1] = adj[i][j] + 1
                queue.append([i, j + 1])
    print(adj[i][j])
miro(0, 0)