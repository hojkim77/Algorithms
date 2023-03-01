# 피로도
from itertools import permutations

def dungeon(k, permutation, dungeons):
    result = 0
    for i in permutation:
        if dungeons[i][0] <= k:
            k -= dungeons[i][1]
            result += 1
        else:
            break
    return result

def solution(k, dungeons):
    answer = -1
    arr = []
    for i in range(len(dungeons)):
        arr.append(i)
    for p in permutations(range(len(dungeons))):
        answer = max(answer, dungeon(k, p, dungeons))
    return answer