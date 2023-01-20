import sys
N = int(sys.stdin.readline().strip())
g = [[' ' for _ in range(N)] for _ in range(N)] # 미리 모든 영역을 공백칸으로 만들어놓는다.

def solution(n, x, y):
    divn = ((0, 0),(0, n // 3),(0, n // 3 * 2),
        (n // 3, 0),(n // 3, n // 3 * 2),
        (n // 3 * 2, 0),(n // 3 * 2, n // 3),(n // 3 * 2, n // 3 * 2))
    if n == 3:
        for i in range(n):
            for j in range(n):
                if n // 3 <= i < (n // 3) * 2 and n // 3 <= j < (n // 3) * 2 :
                    g[x + i][y + j] = ' '
                else:
                    g[x + i][y + j] = '*'
    else:
        for i in range(n):
            for j in range(n):
                if (i, j) in divn:
                    #print(n // 3, i, j)
                    solution(int(n // 3), x + i, y + j)

solution(N // 3, 0, 0) # 1개의 영역 만들기
for i in range(0, N, N // 3): # 8개의 영역 복사
    for j in range(0, N, N // 3):
        if i != N // 3 or j != N // 3:
            for k in range(N // 3):
                g[i+k][j:j+N // 3] = g[k][:N // 3]
                
for i in range(N): # 정답 출력
    for j in range(N):
        print(g[i][j], end='')
    print()
print(g)