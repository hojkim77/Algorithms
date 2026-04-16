from collections import deque
F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F + 1)] # not index. thus, + 1
tup = []
def bfs():
    queue = deque()
    queue.append(S)
    while queue:
        s = queue.popleft()
        if s == G:
            return visited[s]
        if U == 0: #U or D is 0 > cnt + 1 error
            arr = [s - D]
        elif D == 0:
            arr = [s + U]
        else:
            arr = [s + U, s - D]
        for i in arr: # +U or -D case
            if i > 0 and i <= F and not visited[i]:
                visited[i] = visited[s] + 1
                queue.append(i)
                
    return("use the stairs")

print(bfs())