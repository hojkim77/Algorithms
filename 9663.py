N = int(input())
queens = [0] * N
    
answer = 0
def check(x, y):
    for i in range(x):
        if queens[i] == y or abs((i - x) / (queens[i] - y)) == 1:
            return False
    return True
        
def nqueens(x):
    global answer   

    if x == N :
        answer += 1
        return
    else:
        for i in range(N): # i 는 열번호 0부터 N 전까지 옮겨가면서 유망한곳 찾기
            if check(x, i): # 행,열,대각선 체크함수 true이면 백트래킹 안하고 계속 진행
                queens[x] = i
                nqueens(x + 1) 

            
nqueens(0)
print(answer)

# 시간을 줄여야함