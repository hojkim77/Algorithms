# 간선이 들어오는 케이스
n = int(input())
a, b = map(int, input().split())
m = int(input())

arr = [list(map(int, input().split())) for _ in range(m)] #간선 입력값
visited = [0] * (n + 1)
adj = [[0] * (n+1) for _ in range(n+1)] # 간선의 정보를 인접행렬에 저장 (2중 리스트)
for i in range(m): # adj 작성(1 2가 들어오면 1, 2와 2, 1에 1)
    v1 = arr[i][0]
    v2 = arr[i][1]
    adj[v1][v2] = 1
    adj[v2][v1] = 1

visited[a] = 1
def dfs(v):

    for w in range(n+1):
        if adj[v][w] == 1 and visited[w] == 0:
            visited[w] = visited[v] + 1
            dfs(w)
    
    if visited[b]:
        return visited[b] -1
    else:
        return (-1)

print(dfs(a))