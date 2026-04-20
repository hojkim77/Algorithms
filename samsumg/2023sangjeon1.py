# 진짜 모르겠다 무슨 조건을 놓친거지..

# RAVALIDATEOFFSET을 공격 관여 터렛에 미리 빼고 revalidate할때 얘네도 다시 더해주면 되겠다!
# 라는 오만한 생각을 했다..
# 이러면 미리 뺄때 DESTROIED되어버리면 revalidate 대상에 들어오지 못해버린다..
# 뭔가 정석적인지 않은 방법을 활용할때는 꼭 예외가 없는지 확인하자!!!!!

from collections import deque

DESTROIED = 0
RAVALIDATEOFFSET = 1
N, M , K = map(int, input().split(' '))
matrix = list(list(map(int, input().split(' '))) for _ in range(N))
attackTurn = [[0] * M for _ in range(N)]
attackedTurn = [[0] * M for _ in range(N)]
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
recentAttacker = [-1, -1]
turn = 0

def checkAlive():
    count = 0
    for n in range(N):
        for m in range(M):
            if matrix[n][m] != DESTROIED:
                count += 1
            if count > 1:
                return True
    return False

def revalidate(nowTurn):
    global matrix
    for n in range(N):
        for m in range(M):
            if attackedTurn[n][m] < nowTurn and matrix[n][m] != DESTROIED:
                matrix[n][m] += RAVALIDATEOFFSET

def bomb(attacker, target, attackValue, turn):
    global matrix
    allDirections = directions[:] + [[1, 1], [1, -1], [-1, 1], [-1, -1], [0, 0]]
    for d in allDirections:
        row, colmn = [(target[0] + d[0]) % N, (target[1] + d[1]) % M]
        attackedTurn[row][colmn] = turn
        if row == attacker[0] and colmn == attacker[1]:
            continue
        if row == target[0] and colmn == target[1]:
            matrix[row][colmn] -= (attackValue)
        else:
            matrix[row][colmn] -= (attackValue // 2)
        if matrix[row][colmn] < 0:
            matrix[row][colmn] = DESTROIED
    attackedTurn[attacker[0]][attacker[1]] = turn

def layzer(attacker, path, target, attackValue, turn):
    global matrix
    for p in path:
        row, colmn = p
        attackedTurn[row][colmn] = turn
        if row == target[0] and colmn == target[1]:
            matrix[row][colmn] -= (attackValue)
        else:
            matrix[row][colmn] -= (attackValue // 2)
        if matrix[row][colmn] < 0:
            matrix[row][colmn] = DESTROIED
        
    attackedTurn[attacker[0]][attacker[1]] = turn

def attackBfs(attacker, target):
    targetR, targetC = target
    visited = [[False] * M for _ in range(N)]
    bfsQueue = deque([[attacker[0], attacker[1], []]])
    visited[attacker[0]][attacker[1]] = True
    while(len(bfsQueue) > 0):
        row, colmn, path = bfsQueue.popleft()
        if (row == targetR and colmn == targetC): return path
        for d in directions:
            nextR, nextC = [(row + d[0]) % N, (colmn + d[1]) % M]
            if (matrix[nextR][nextC] != DESTROIED and visited[nextR][nextC] == False):
                newPath = path[:]
                newPath.append([nextR, nextC])
                bfsQueue.append([nextR, nextC, newPath])
                visited[nextR][nextC] = True

    return []

def attack(attacker, target, turn):
    matrix[attacker[0]][attacker[1]] += (N + M)
    attackValue = matrix[attacker[0]][attacker[1]]
    path = attackBfs(attacker, target)
    if (len(path) == 0):
        bomb(attacker, target, attackValue, turn)
    else:
        layzer(attacker, path, target, attackValue, turn)

def selectTarget(turn):
    candidate = []
    maxValue = max(map(max, matrix))
    for n in range(N):
        for m in range(M):
            if matrix[n][m] == maxValue:
                candidate.append([n, m])

    if len(candidate) > 1:
        print('target!!!', candidate, turn)
        tmpCandidate = []
        minTurn = K + 1
        for c in candidate:
            if (attackTurn[c[0]][c[1]] < minTurn):
                minTurn = attackTurn[c[0]][c[1]]
        for c in candidate:
            row, colmn = c
            if attackTurn[row][colmn] == minTurn:
                tmpCandidate.append(c)
        candidate = tmpCandidate

    if len(candidate) > 1:
        tmpCandidate = []
        minSum = min(map(sum, candidate))
        for c in candidate:
            if c[0] + c[1] == minSum:
                tmpCandidate.append(c)
        candidate = tmpCandidate
    
    if len(candidate) > 1:
        candidate.sort(key=lambda x: (x[1]))
        print('!!!', candidate, turn)
    
    target = candidate[0]

    return target

def selectAttacker(turn):
    for a in attackTurn:
        print(a)
    candidate = []
    minValue = 100000
    for n in range(N):
        for m in range(M):
            if matrix[n][m] != DESTROIED and matrix[n][m] < minValue:
                minValue = matrix[n][m]

    for n in range(N):
        for m in range(M):
            if matrix[n][m] == minValue:
                candidate.append([n, m])
    
    if len(candidate) > 1:
        print('attacker!!!', candidate, turn)
        tmpCandidate = []
        maxTurn = 0
        for c in candidate:
            if (attackTurn[c[0]][c[1]] > maxTurn):
                maxTurn = attackTurn[c[0]][c[1]]
        for c in candidate:
            row, colmn = c
            if attackTurn[row][colmn] == maxTurn:
                tmpCandidate.append(c)
        candidate = tmpCandidate

    if len(candidate) > 1:
        tmpCandidate = []
        maxSum = max(map(sum, candidate))
        for c in candidate:
            if c[0] + c[1] == maxSum:
                tmpCandidate.append(c)
        candidate = tmpCandidate

    if len(candidate) > 1:
        candidate.sort(key=lambda x: (-x[1]))
        print('!!!', candidate, turn)

    
    attacker = candidate[0]
    attackTurn[attacker[0]][attacker[1]] = turn
    return attacker

def solution(K):
    turn = 0
    while(K > turn):
        turn += 1

        if (not checkAlive()):
            break
        attacker = selectAttacker(turn)
        target = selectTarget(turn)
        print(attacker, target)
        for m in matrix:
            print(m)
        print()
        attack(attacker, target, turn)
        revalidate(turn)
        

    maxValue = max(map(max, matrix))

    print(maxValue)

solution(K)