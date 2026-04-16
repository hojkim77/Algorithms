n = int(input())

def solution(m):
    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * m for _ in range(2)]
    for i in range(m):
        if i == 0:
            dp[0][i] = arr[0][i]
            dp[1][i] = arr[1][i]
        elif i == 1:
            dp[0][i] = dp[1][i - 1] +  arr[0][i]
            dp[1][i] = dp[0][i - 1] +  arr[1][i]
        else:
            dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + arr[0][i]
            dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + arr[1][i]
    return(max(max(dp[0]), max(dp[1])))


for _ in range(n):
    m = int(input())
    print(solution(m))

