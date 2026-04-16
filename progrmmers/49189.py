# 가장 먼 노드
# 쉬운 DP + BFS
# 탐색 과정에서 현재의 거리를 갖고다녀야 DP(distance)를 비교 및 업데이트 할 수 있다는 점!

from collections import deque
INF = 20000

def getMaxDist(distance):
    return max(distance)

def bfs(graph, distance):
    queue = deque([[1, 0]])
    distance[0], distance[1] = 0, 0
    while(queue):
        curNode, curDist = queue.popleft()
        for nxtNode in graph[curNode]:
            nxtDist = curDist + 1
            if distance[nxtNode] <= nxtDist:
                continue
            queue.append([nxtNode, nxtDist])
            distance[nxtNode] = nxtDist
    

def solution(n, edge):
    answer = 0
    graph = list([] for _ in range(n + 1))
    for node1, node2 in edge:
        graph[node1].append(node2)
        graph[node2].append(node1)
    distance = list(INF for _ in range(n + 1))
    bfs(graph, distance)
    maxDist = getMaxDist(distance)
    print(maxDist)
    print(distance)
    for d in distance:
        if d == maxDist:
            answer += 1
    
    return answer