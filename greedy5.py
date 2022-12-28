from collections import deque

def solution(n, costs):
    answer = 0
    visited = [0] * n
    visited[0] = 1
    tmp = []
    while(sum(visited) != n):

        for i in range(len(visited)):
            if visited[i] == 1:
                for cost in costs:
                    if (cost[0] == i or cost[1] == i) and not(visited[cost[0]] == 1 and visited[cost[1]]==1):
                        tmp.append(cost)
        #print(tmp)
        min = tmp[0]
        for t in tmp:
            if t[2] <= min[2]:
                min = t
        visited[min[0]] = 1
        visited[min[1]] = 1
        answer += min[2]
        tmp.clear()

    '''costs.sort(key=lambda x:x[2])
    costs = deque(costs)
    while (sum(visited) != n):
        cur = costs.popleft()
        print(cur)
        if (not visited[cur[0]] or not visited[cur[1]]):
            visited[cur[0]], visited[cur[1]]= 1, 1
            answer += cur[2]
        else:
            costs.append(cur)'''
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))