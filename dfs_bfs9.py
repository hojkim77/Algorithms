# 메모리 초과?
from collections import deque

N = int(input())
adj = [list(map(int,input().split())) for _ in range(N)]
mmax = max(max(adj))
ans = [0 for i in range(mmax + 1)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def solution():
    for k in range(0, mmax + 1):
        queue = deque()
        visited = [[0 for i in range(N)] for i in range(N)]
        cnt = 0
        for i in range(N): #물에 잠기는 영역
            for j in range(N):
                if adj[i][j] <= k:
                    visited[i][j] = 1
       #print(visited)
                
                    
        for i in range(N): # 유효한 영역
            for j in range(N):
                if not visited[i][j] :
                    cnt += 1
                    queue.append((i,j)) # bfs
                    visited[i][j] = 1
                    while queue:
                        #print(queue)
                        x, y = queue.popleft()
                        for a in range(4):
                            nx, ny = x + dx[a], y + dy[a]
                            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                                queue.append((nx,ny))
                                visited[nx][ny] = 1
        #print(cnt)
                                
        ans[k] = cnt
    return max(ans)
        
print(solution())