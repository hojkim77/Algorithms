import itertools
N = int(input())
A = list(map(int, input().split()))
Acomb = list(itertools.permutations(A, N))
answer = 0

for a in Acomb:
    sum = 0
    for i in range(len(a) - 1):
        sum += abs(a[i] - a[i + 1])
    answer = max(answer, sum)
    
print(answer)