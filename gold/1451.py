N, M = map(int, input().split())
arr = [list(map(int,list(str(input())))) for _ in range(N)]

answer = 0
nemo = [0,0,0]
maxnemo = 0
if M >= 3:
    for i in range(1, M - 1): # case1. 세로 세줄
        for j in range(i + 1 , M):
            nemo[0] = sum(sum(arr[n][:i]) for n in range(N))
            nemo[1] = sum(sum(arr[n][i:j]) for n in range(N))
            nemo[2] = sum(sum(arr[n][j:]) for n in range(N))
            maxnemo = max(maxnemo, nemo[0]*nemo[1]*nemo[2])
            
if N >= 3:
    for i in range(1, N - 1): # case2. 가로 세줄
        for j in range(i + 1 , N):
            nemo[0] = sum(sum(arr[n][:]) for n in range(i))
            nemo[1] = sum(sum(arr[n][:]) for n in range(i,j))
            nemo[2] = sum(sum(arr[n][:]) for n in range(j,N))
            maxnemo = max(maxnemo, nemo[0]*nemo[1]*nemo[2])

if N >= 2 and M >= 2: # case3. 위 둘 아래 하나
    for i in range(1, N):
        for j in range(1, M):
            nemo[0] = sum(sum(arr[n][:j]) for n in range(i))
            nemo[1] = sum(sum(arr[n][j:]) for n in range(i))
            nemo[2] = sum(sum(arr[n][:]) for n in range(i,N))
            maxnemo = max(maxnemo, nemo[0]*nemo[1]*nemo[2])

    for i in range(1, N): # case4. 위 하나 아래 둘
        for j in range(1, M):
            nemo[0] = sum(sum(arr[n][:j]) for n in range(i, N))
            nemo[1] = sum(sum(arr[n][j:]) for n in range(i, N))
            nemo[2] = sum(sum(arr[n][:]) for n in range(i))
            maxnemo = max(maxnemo, nemo[0]*nemo[1]*nemo[2])

    for i in range(1,M): # case5. 왼 둘 오른 하나
        for j in range(1, N):
            nemo[0] = sum(sum(arr[n][:i]) for n in range(j))
            nemo[1] = sum(sum(arr[n][:i]) for n in range(j, N))
            nemo[2] = sum(sum(arr[n][i:]) for n in range(N))
            maxnemo = max(maxnemo, nemo[0]*nemo[1]*nemo[2])

    for i in range(1, M): # case6. 왼 하나 오른 둘
        for j in range(1, N):
            nemo[0] = sum(sum(arr[n][i:]) for n in range(j))
            nemo[1] = sum(sum(arr[n][i:]) for n in range(j, N))
            nemo[2] = sum(sum(arr[n][:i]) for n in range(N))
            maxnemo = max(maxnemo, nemo[0]*nemo[1]*nemo[2])
            

print(maxnemo)