# 이기거나 진게 (사람 수 - 1)만큼이면 확정된 사람.
# upper, lower 구해서 이게 위 조건 충족되면 answer++

# dp 적용은 안되나?
# 이미 관계 맺어봤던 선수면 그거 그대로 저장해두고 다시 방문했을때 또 쓰면 되겠네.
# 그럼 그래프 자체를 계속 업데이트? set으로 중복 제거하면서!

from collections import deque

def findUpper(graph, index):
    queue = deque(list(graph[index][0]))
    while(queue):
        current = queue.popleft()
        upperList = graph[current][0]
        for upper in upperList:
            if upper in graph[index][0]:
                continue
            graph[index][0].add(upper)
            queue.append(upper)

def findLower(graph, index):
    queue = deque(list(graph[index][1]))
    while(queue):
        current = queue.popleft()
        lowerList = graph[current][1]
        for lower in lowerList:
            if lower in graph[index][1]:
                continue
            graph[index][1].add(lower)
            queue.append(lower)
    
def solution(n, results):
    answer = 0
    graph = list((set(), set()) for _ in range(n + 1))
    for A,B in results:
        graph[A][1].add(B)
        graph[B][0].add(A)
    
    for i in range(1, n + 1):
        findUpper(graph, i)
        findLower(graph, i)
        upperSize = len(graph[i][0])
        lowerSize = len(graph[i][1])
        if(upperSize + lowerSize == n - 1):
            answer += 1
    return answer