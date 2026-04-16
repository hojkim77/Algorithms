n = int(input())
d = [0] * (n + 1)
def solution(x):
    if x == 1:
        return 9
    elif x == 2:
        return 17
    if d[x] != 0:
        return d[x]
    d[x] = 2* solution(x - 1) - (x - 1)
    
    return d[x]

print(solution(n) % 1000000000)