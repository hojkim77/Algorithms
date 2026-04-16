# 간선이 들어오는 케이스
from collections import deque

n, m, s = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)] #간선 입력값
visited = [0] * (n + 1)
adj = [[0] * (n+1) for _ in range(n+1)] # 간선의 정보를 인접행렬에 저장 (2중 리스트)

for i in range(m): # adj 작성(1 2가 들어오면 1, 2와 2, 1에 1)
    v1 = arr[i][0]
    v2 = arr[i][1]
    adj[v1][v2] = 1
    adj[v2][v1] = 1
    
def dfs(v):
    visited[v] = 1
    print(v, end = ' ')

    for w in range(n+1):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)

def bfs(v):
    queue = deque([v])
    visited[v] = 1
    while queue:
        i = queue.popleft() #방문처리
        print(i, end = ' ')
        for j in range(n + 1):
            if adj[i][j] == 1 and visited[j] == 0: #방문노드 인접노드 모두 방문처리
                queue.append(j)
                visited[j] = 1

dfs(s)
print("") 
visited = [0] * (n + 1) #bfs를 위해 visited초기화       
bfs(s)