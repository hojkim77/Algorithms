import sys

def solution(PS):
    arr = []
    for i in range(len(PS) - 1):
        if PS[i] == "(":
            arr.append("(")
        else:
            if not arr:
                return("NO")
            arr.pop()
    if not arr:
        return("YES")
    else:
        return("NO")

T = int(sys.stdin.readline())

for i in range(T):
    PS = str(sys.stdin.readline())
    print(solution(PS))

