N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [1] + [0] * (N -1)
mincost = 1000000 * 1000

def travel(start, cost):
    global mincost
    if sum(visited) == N and arr[start][0]: # 순환이 되면 mincost를 업데이트해준다.
        mincost = min(mincost, cost + arr[start][0])
        return

    for i in range(N): # 시작인 0부터 재귀(backtracking)을 통해 완전탐색한다.
        if not visited[i] and arr[start][i]:
            print(visited)
            visited[i] = 1
            travel(i,cost + arr[start][i])
            visited[i] = 0
            

travel(0,0)
print(mincost)