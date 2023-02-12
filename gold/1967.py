from collections import deque
# 트리 완성
N = int(input())
if N == 1:
    print(0)
    exit(0)
adj = [[] for _ in range(N + 1)]
maxn = 0
for _ in range(N - 1): 
    n, m, x = map(int, input().split())
    adj[n].append([m, x]) # n에 m이 연결되어있고 x의 가중치를 가짐
    adj[m].append([n, x]) # m에 n이 연결되어있고 x의 가중치를 가짐
    maxn = n

# bfs로 탐색하며 visted에 가중치 초기화
def bfs(n):
    queue = deque([n])
    while(queue):
        v = queue.popleft()
        for node in adj[v]:
            if not visited[node[0]] and node[0] != n:
                queue.append(node[0])
                visited[node[0]] += visited[v] + node[1]
    return max(visited)

# 루트노드로부터 가장 멀리 떨어진 leafnode 탐색
visited = [0] * (N + 1) 
maxleaf = visited.index(bfs(1))
# 찾은 leafnode로 bfs()
visited = [0] * (N + 1)
print(bfs(maxleaf))

