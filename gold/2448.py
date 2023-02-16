N = int(input())
graph = [[' '] * 2 * N for _ in range(N)]


def recursive(x, y, N):
    if N == 3:
        graph[x][y] = '*'
        graph[x + 1][y - 1] = graph[x + 1][y + 1] = '*'
        for i in range(-2, 3):
            graph[x + 2][y + i] = '*'
    else:
        nextN = N // 2
        recursive(x, y, nextN) # 상단 큰 삼각형
        recursive(x + nextN, y - nextN, nextN) # 왼쪽 큰 삼각형
        recursive(x + nextN, y + nextN, nextN) # 오른쪽 큰 삼각형

recursive(0, N - 1, N)
for i in graph:
    print("".join(i))