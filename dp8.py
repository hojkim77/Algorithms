n = int(input())
dp = [0] * (n + 1)

def solution(n):
    if n == 1 or n == 2:
        return 1
    if dp[n] != 0:
        return dp[n]
    dp[n] = solution(n - 2) + solution(n - 1)
    
    return dp[n]

print(solution(n))
    