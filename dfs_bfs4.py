# 그래프 자체가 들어오는 케이스
from collections import deque

n = int(input())
adj = [list(input()) for _ in range(n)] 
s_arr = [0]
s = 0 #단지 인덱스
for i in range(n): #리스트 정수화
    for j in range(n):
        adj[i][j] = int(adj[i][j])
        
def dfs(x,y):
    if x < 0 or x > n - 1 or y < 0 or y > n - 1:
        return False
    if adj[x][y] == 1:
        adj[x][y] = 0
        s_arr[s] += 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            s_arr.append(0)
            s += 1

s_arr = sorted(s_arr)
s_arr.remove(0)
print(len(s_arr))
for i in s_arr:
    print(i)