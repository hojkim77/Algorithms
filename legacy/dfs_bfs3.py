# 간선이 들어오는 케이스

from collections import deque

n = int(input())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(m)] #간선 입력값
visited = [0] * (n + 1)
adj = [[0] * (n+1) for _ in range(n+1)] # 간선의 정보를 인접행렬에 저장 (2중 리스트)
for i in range(m): # adj 작성(1 2가 들어오면 1, 2와 2, 1에 1)
    v1 = arr[i][0]
    v2 = arr[i][1]
    adj[v1][v2] = 1
    adj[v2][v1] = 1
    
def bfs(v):

    queue = deque([v])
    visited[v] = 1
    while queue:
        i = queue.popleft() #방문처리
        for j in range(n + 1):
            if adj[i][j] == 1 and visited[j] == 0: #방문노드 인접노드 모두 방문처리
                queue.append(j)
                visited[j] = 1
    return(sum(visited) - 1)

print(bfs(1))