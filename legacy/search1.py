# 단어 변환
from collections import deque

def check(s1, s2):
    result = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            result += 1
        if result > 1:
            return False
    return True

def solution(begin, target, words):
    queue = deque([])
    visited = [0] * len(words)
    queue.append([begin, 0])
    while(queue):
        cur, answer = queue.popleft()
        if cur == target:
            return answer
        else:
            for i in range(len(words)):
                if words[i] != cur and check(cur, words[i]) and not visited[i]:
                    queue.append([words[i], answer + 1])
                    visited[i] = 1
    if cur != target:
        return 0
    return answer