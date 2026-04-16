# simulation
# bfs
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(i, j, boardOrTable, isChecked, findNum):
    returnArr = []
    q = deque([(i, j)])
    n = len(boardOrTable)
    isChecked[i][j] = True
    while q:
        x, y = q.popleft()
        returnArr.append([x, y])
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if boardOrTable[nx][ny] == findNum and isChecked[nx][ny] == False:
                q.append((nx, ny))
                isChecked[nx][ny] = True
    return returnArr


def normalization(boardOrPuzzle):
    print(boardOrPuzzle)
    minY = min(boardOrPuzzle, key=lambda y: y[0])[
        0
    ]  # 받은 조각들 중 왼쪽 위 모서리 y값
    maxY = max(boardOrPuzzle, key=lambda y: y[0])[
        0
    ]  # 받은 조각들 중 왼쪽 위 모서리 y값
    minX = min(boardOrPuzzle, key=lambda x: x[1])[
        1
    ]  # 받은 조각들 중 왼쪽 위 모서리 x값
    maxX = max(boardOrPuzzle, key=lambda x: x[1])[
        1
    ]  # 받은 조각들 중 왼쪽 위 모서리 x값
    returnArr = [[0] * (1 + maxX - minX) for _ in range(1 + maxY - minY)]
    for i in range(len(boardOrPuzzle)):
        boardOrPuzzle[i][0] -= minY
        boardOrPuzzle[i][1] -= minX
        returnArr[boardOrPuzzle[i][0]][boardOrPuzzle[i][1]] = 1

    print(returnArr)
    return returnArr


def rotation(puzzle):
    n = len(puzzle)
    m = len(puzzle[0])
    result = [[0] * n for _ in range(m)]
    for r in range(n):
        for c in range(m):
            result[c][n - 1 - r] = puzzle[r][c]

    return result


def sumPuzzle(puzzle):
    answer = 0
    for p in puzzle:
        answer += sum(p)
    return answer


def solution(game_board, table):
    answer = 0
    n = len(game_board)
    checkedBoard = [[False] * n for _ in range(n)]
    checkedTable = [[False] * n for _ in range(n)]
    boards = []
    puzzles = []
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0 and checkedBoard[i][j] == False:
                board = bfs(i, j, game_board, checkedBoard, 0)
                normalizatedBoard = normalization(board)
                boards.append(normalizatedBoard)
            if table[i][j] == 1 and checkedTable[i][j] == False:
                puzzle = bfs(i, j, table, checkedTable, 1)
                normalizatedPuzzle = normalization(puzzle)
                puzzles.append(normalizatedPuzzle)

    print(boards)
    print(puzzles)
    for i, board in enumerate(boards):
        for j, puzzle in enumerate(puzzles):
            if board != -1 and puzzle != -1:
                for _ in range(4):
                    puzzle = rotation(puzzle)
                    if board == puzzle:
                        answer += sumPuzzle(puzzle)
                        boards[i] = -1
                        puzzles[j] = -1
                        break
    return answer


solution(
    [
        [1, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 0, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 0],
    ],
    [
        [1, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0],
    ],
)
