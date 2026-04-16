import sys
D, P = map(int,sys.stdin.readline().split())
LC = [list(map(int, sys.stdin.readline().split())) for i in range(P)]
LC.sort(reverse=True, key=lambda x : x[1])
#print(LC)

dp = [1e9]+[0]*7

'''
answer = []
sum = 0
min = 2 ** 23
for i in range(P):
    sum += LC[i][0]
    print(sum)
    for j in range(P - i):
        if sum + LC[j][0] == D:
            print(i, j)
            sum += LC[j][0]
            if min > LC[j][1]:
                min = LC[j][1]
            answer.append(min)
        if sum + LC[j][0] < D:
            sum += LC[j][0]
            if min > LC[j][1]:
                min = LC[j][1]
    sum = 0
    min = 0
'''
print(dp)
        
