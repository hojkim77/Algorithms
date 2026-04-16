N, M = map(int, input().split())
arr = [list(str(input())) for _ in range(N)] # 공백없어서 일부러 str로 받음
def issquare(n):
	return int(n ** 0.5) ** 2 == n


def solution():
    answer = -1

    for i in range(N): # 입력배열 완전탐색
        for j in range(M): # 입력배열 완전탐색
            for di in range(-N, N + 1): # 가능한 공차의 경우의 수 모두
                for dj in range(-M, M + 1): # 가능한 공차의 경우의 수 모두
                    if di == 0 and dj == 0: # 아래 while문의 무한 루프를 막기 위함
                        continue
                    s = ''
                    x = i
                    y = j
                    while 0<=x<N and 0<=y<M:
                        s+=str(arr[x][y])
                        x += di
                        y += dj    
                        if issquare(int(s)) and int(s) > answer: # 해당 공차를 가진 수의 배열이 제곱수이고 직전 answer 보다 크다면 answer 초기화
                            answer = int(s)
            '''
            # 공차가 '+'
            for di in range(N - i): 
                for dj in range(M - j):
                    if di == 0 and dj == 0:
                        continue
                    s = ''
                    x = i
                    y = j
                    while x<N and y<M:
                        s+=str(arr[x][y])
                        x += di
                        y += dj
                        #print(s)
                        if issquare(int(s)) and int(s) > answer:
                            answer = int(s)
            # 공차가 '-'
            s = ''
            #print('s ', i, j)
            for di in range(i + 1): 
                for dj in range(j + 1):
                    #print(di, dj)
                    if di == 0 and dj == 0:
                        continue
                    s = ''
                    x = i
                    y = j
                    while 0<=x and 0<=y:
                        s+=str(arr[x][y])
                        x -= di
                        y -= dj
                        if issquare(int(s)) and int(s) > answer:
                            print(s)
                            print(x, y)
                            answer = int(s)
                            '''
    print(answer)
print(issquare(95481))
solution()