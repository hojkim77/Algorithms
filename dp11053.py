n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (n + 1)
def solution(n):
    for i in range(n):
        if (n == 1):
            return 1
        if (n == 2):
            if arr[1] > arr[0]:
                return 2
            else:
                return 1
        if (n > 2):
            current = i
            i -= 1
            while dp[i] == dp[current - 1]:
                i -= 1
                if arr[i] < arr[current]:
                    dp[current] = dp[current - 1] + 1
                    break
            if dp[current] == 0:
                dp[current] = dp[current - 1]
        
    return dp[n]

print(solution(n))