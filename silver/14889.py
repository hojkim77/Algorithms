from itertools import combinations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
allSum = sum([sum(i) for i in arr])
comb = list(combinations([i for i in range(N)], N // 2))
scoreArr = []
answer = 1000


def calScore(c):
    score = 0
    for i in range(N):
        if i not in c:
            for j in range(N):
                if j not in c:
                    score += arr[i][j]

    return score


for c in comb:
    scoreArr.append(calScore(c))

for i in range(len(scoreArr) // 2):
    answer = min(answer, abs(scoreArr[i] - scoreArr[len(scoreArr) - 1 - i]))

print(answer)
