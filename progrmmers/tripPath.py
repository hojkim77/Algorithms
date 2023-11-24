from collections import deque


def solution(tickets):
    answer = []
    queue = deque([])

    # ICN에서 출발하는 항공권으로 시작
    for idx in range(len(tickets)):
        if tickets[idx][0] == "ICN":
            queue.append([tickets[idx][1], tickets[idx], [idx]])

    while queue:
        start, path, used = queue.popleft()
        if len(used) == len(tickets):
            answer.append(path)
            continue

        for idx in range(len(tickets)):
            if tickets[idx][0] == start and idx not in used:
                queue.append([tickets[idx][1], path + [tickets[idx][1]], used + [idx]])

    answer.sort()
    return answer[0]


print(
    solution(
        [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    )
)

# 여행경로
# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# DFS/BFS
