from collections import deque
n, m = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(m)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    answer = 0
    queue = deque()
    for i in range(m): # 첫 토마토
        for j in range(n):
            if tomatos[i][j] == 1:
                queue.append([i, j, 0])
    while(queue): # 익은 토마토 기준 사방면을 탬색하며 
    			  # 안익은 토마토가 있으면 queue에 담고 익음 처리 한다.
        cur = queue.popleft()
        x = cur[1]
        y = cur[0]
        d = cur[2]
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m:
                if tomatos[yy][xx] == 0:
                    queue.append([yy, xx, d + 1])
                    tomatos[yy][xx] = 1
                    answer = d + 1
    for i in range(m): # 익지 않은 토마토 탐색
        for j in range(n):
            if tomatos[i][j] == 0:
                return -1
    return answer

print(bfs())