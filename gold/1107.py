n = int(input())
if n == 100: # case1. 100번 채널로 가야하는 예외 케이스
    print(0)
    exit()
    
answer_num = abs(n - 100) # 목표숫자까지의 초기 거리

N = list(str(n))
for i in range(len(N)): # 구해야하는 채널 정수 리스트
    if N[i] == 0:
        N[i] = 10
M = int(input())

if M == 0: # case2. 모든 번호를 다 쓸 수 있는 예외 케이스
    print(min(answer_num, len(N)))
    exit()
xnum = list(map(int, input().split()))
num = []

for i in range(10): # 사용할 수 있는 숫자 리스트
    if i not in xnum:
        num.append(str(i))
answer = ''
tmp = ''

def compare(tmp): # 목표숫자와 비교 가능한 모든 숫자를 비교하는 함수
    global answer
    global n
    global answer_num
    if abs(int(tmp) - n) + len(str(int(tmp))) < answer_num:
        answer = tmp
        answer_num = abs(int(tmp) - n) + len(str(int(tmp)))

for a in num: # 1의 자리부터 7자리까지 사용 가능한 수를 갖고 만든 모든 수를 compare함수에 넣어본다
    compare(a)
    for b in num:
        compare(a + b)
        for c in num:
            compare(a + b + c)
            for d in num:
                compare(a + b + c + d)
                for e in num:
                    compare(a + b + c + d + e)
                    for f in num:
                        compare(a + b + c + d + e + f)
                        for g in num:
                            compare(a + b + c + d + e + f + g)


if answer == '': # 100에서 +, - 만 사용한 케이스
    print(answer_num)
else: # 숫자버튼을 사용하여 접근 후 +, - 를 사용한 케이스
    print(abs(int(answer) - n) + len(str(int(answer))))