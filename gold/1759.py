import math
T = int(input())
TC = [list(map(int, input().split())) for _ in range(T)]
primenum = []

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True      

for i in range(1000, 9999):
    if prime(i):
        primenum.append(i)


def solution(a, b):
    if a == b:
        return 0
    
    cnt = 1
    aidx = primenum.index(a)
    bidx = primenum.index(b)
    promise = []
    
    for i in range(aidx, bidx):
        if str(primenum[i] - b).count('0') == cnt:
            promise.append(i)
            cnt += 1
            if cnt == 4:
                break
    for i in promise:
        print(primenum[i])
    print()
    
for i in range(T):
    solution(TC[i][0], TC[i][1])