N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
times.sort(key = lambda x: (x[1],x[0]))
answer = 1 # 첫번째 회의실 확정
start, end = 0, 1
while(end < N): # end를 끝까지 보내본다
    if times[start][1] <= times[end][0]: # end의 시작 시간이 start의 끝나는 시간보다 커지면 start를 end로 업데이트
        answer += 1
        start = end
        end += 1
    else:
        end += 1 #기본적으로 end를 위의 if문에 걸릴 때 까지 +1 함
print(answer)