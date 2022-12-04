# 그래프 자체가 들어오는 케이스
# 진짜 반례를 못찾겠음..
from collections import deque

def tomato():
    i, j, k = map(int,input().split())
    adj = [[list(input().split()) for _ in range(j)] for _ in range(k)]
    z = 0 # while문 끝내기 위해 조건걸기
    queue = deque()
    for a in range(k): #리스트 정수화
        for b in range(j):
            for c in range(i):
                adj[a][b][c] = int(adj[a][b][c])
                if (adj[a][b][c] == 0):
                    z += 1
                if (adj[a][b][c] == 1):
                    queue.append([a, b, c, 0])
    print(adj)
    if z == 0:
        if len(queue) > 0: # 1, -1만 있을 때
            return 0
        return 0 # -1만 있을 때
    while(z > 0):
        if (queue):
            cur = queue.popleft()
            l, m, n ,d = cur[0], cur[1], cur[2], cur[3]
            if l - 1 >= 0 and adj[l - 1][m][n] == 0:
                adj[l - 1][m][n] = d + 1
                z -= 1
                queue.append([l - 1, m, n, d + 1])
            if l + 1 < k and adj[l + 1][m][n] == 0:
                adj[l + 1][m][n] = d + 1
                z -= 1
                queue.append([l + 1, m, n, d + 1])
            if m - 1 >= 0 and adj[l][m - 1][n] == 0:
                adj[l][m - 1][n] = d + 1
                z -= 1
                queue.append([l, m - 1, n, d + 1])
            if m + 1 < j and adj[l][m + 1][n] == 0:
                adj[l][m + 1][n] = d + 1
                z -= 1
                queue.append([l, m + 1, n, d + 1])
            if n - 1 >= 0 and adj[l][m][n - 1] == 0:
                adj[l][m][n - 1] = d + 1
                z -= 1
                queue.append([l, m, n - 1, d + 1])
            if n + 1 < i and adj[l][m][n + 1] == 0:
                adj[l][m][n + 1] = d + 1
                z -= 1
                queue.append([l, m, n + 1, d + 1])
        print(adj)
    if z > 0 and not(queue):
        return -1
    return max(max(max(adj)))

print(tomato())