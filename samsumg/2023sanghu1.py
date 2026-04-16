# 디버그용 함수 하나 따로 만들어놓는것도 좋으듯! 이거 주석 처리하면서 하면 되니까.
# !!! 이번엔 한 칸에 2명이 들어갈 수 있다는걸 간과했다.
# !!! 2명 이상 있을때 다같이 회전되어야하는데 하나만 회전됐던거임!
# !!! 움직여서 두명이 될 수 있다는것, 두명이 움직일 수 있다는건 캐치했지만
# !!! 회전에서의 케이스를 신경쓰지 못함!ㅠ

# 장면을 상상하면서 구현하면 실수를 덜할듯! 
from collections import deque

def minusOne(input):
    return int(input) - 1
def plusOne(input):
    return str(input + 1)
N, M, K = map(int, input().split(' '))
matrix = list(list(map(int, input().split(' '))) for _ in range(N))
people = list(list(map(minusOne, input().split(' '))) for _ in range(M))
exit = list(map(minusOne, input().split(' ')))
directions = [[-1, -1, 0, 0], [-1, 0, 0, 1], [0, -1, 1, 0], [0, 0, 1, 1]]
EMPTY = 0
EXIT = -1

def checkFinish(distance):
    if (M == 0):
        print(distance)
        print(' '.join(map(plusOne, exit)))
        return True
    return False

def checkExit():
    global people, M
    people = list(filter(lambda x: x != exit, people))
    M = len(people)

def movePeople():
    global people
    distance = 0
    for i in range(M):
        p = people[i]
        if (p[0] != exit[0]):
            rowDiff = (exit[0] - p[0]) // abs(exit[0] - p[0])
            if(matrix[p[0] + rowDiff][p[1]] == 0):
                people[i] = [p[0] + rowDiff, p[1]]
                distance += 1
                continue
        if (p[1] != exit[1]):
            colmnDiff = (exit[1] - p[1]) // abs(exit[1] - p[1])
            if(matrix[p[0]][p[1] + colmnDiff] == 0):
                people[i] = [p[0], p[1] + colmnDiff]
                distance += 1
    
    return distance


def getSmallestSquare():
    exitR, exitC = exit
    size = 2
    while(size <= N):
        for i in range(N - size + 1):
            for j in range(N - size + 1):
                isExit = False
                isPerson = False
                for r in range(i, i + size):
                    for c in range(j, j + size):
                        if [r,c] == exit:
                            isExit = True
                        if [r,c] in people:
                            isPerson = True
                if (isExit and isPerson):
                    return [i, j, i + size -1 , j + size - 1]
        size += 1

def rotateMatrix():
    global exit
    startR, startC, endR, endC = getSmallestSquare()
    parsedSquare = deque([])
    rotatedPeopleOrExit = deque([])
    for i in range(startC, endC + 1):
        for j in range(endR, startR - 1, -1):
            parsedSquare.append(matrix[j][i])
            
            if exit == [j, i]:
                rotatedPeopleOrExit.append('exit')
                continue
            
            tmpPeople = []
            for m in range(M):
                if people[m] == [j,i]:
                    tmpPeople.append(m)
            rotatedPeopleOrExit.append(tmpPeople)

    for i in range(startR, endR + 1):
        for j in range(startC, endC + 1):
            current = parsedSquare.popleft()
            if current > 0:
                current -= 1
            matrix[i][j]  = current
            
            what = rotatedPeopleOrExit.popleft()
            if what == 'exit':
                exit = [i, j]
            elif len(what) > 0:
                for w in what:
                    people[w] = [i, j]

            
def debug(distance):
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i][j] = matrix[i][j]
        
    tmp[exit[0]][exit[1]] = 'E'
    for p in people:
        tmp[p[0]][p[1]] = 'P'
    print(K, distance)
    for t in tmp:
        print(' '.join(map(str, t)))
    print()
    
def solution():
    global K
    distance = 0
    while(K > 0):
        K -= 1
        # debug(distance)
        distance += movePeople()
        checkExit()
        if (checkFinish(distance)):
            return
        rotateMatrix()

    print(distance)
    print(' '.join(map(plusOne, exit)))

solution()