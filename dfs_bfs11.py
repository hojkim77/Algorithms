from collections import deque

n = int(input())

def solution(m):
    adj = [list(map(int, input().split())) for _ in range(m + 2)]
    visited = [0] * (m + 2)
    queue = deque()
    endidx = adj[m + 1]
    queue.append(adj[0])
    visited[0] = 1
    while(queue):
        curidx = queue.popleft()
        if abs(endidx[0] - curidx[0]) + abs(endidx[1] - curidx[1]) <= 1000:
            return "happy"
        else:
            for i in range(m + 2):
                if (abs(adj[i][0] - curidx[0]) + abs(adj[i][1] - curidx[1])) <= 1000 and visited[i] == 0:
                    queue.append(adj[i])
                    visited[i] = 1
                
    return "sad"

for i in range(n):
    m = int(input())
    print(solution(m))