# 그래프 자체가 들어오는 케이스
from collections import deque

n, m = map(int, input().split())
adj = [list(input()) for _ in range(n)] # 그래프
for i in range(n): # 그래프 int
    for j in range(m):
        adj[i][j] = int(adj[i][j])
        
dx = [1, 0, -1, 0] # 4방향
dy = [0, 1, 0, -1] # 4방향

def miro(i,j):
    
    queue = deque([[i, j]])

    while(queue):
        cur = queue.popleft()
        x = cur[0]
        y = cur[1]
        
        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m and not(x + dx[i] == 0 and y + dy[i] == 0): # 0,0이면 무한루프에 빠질 가능성이 있음
                if adj[x + dx[i]][y + dy[i]] == 1: # 1일때 인 것은 아직 도착하지 않은 유효한 칸을 뜻함
                    adj[x + dx[i]][y + dy[i]] = adj[x][y] + 1 # 이전 칸의 숫자 + 1
                    queue.append([x + dx[i], y + dy[i]]) 
                    
    print(adj[n - 1][m - 1])
    
miro(0, 0)