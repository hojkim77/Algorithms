n = int(input())
arr = list(map(int, input().split()))
dp = arr[:]

if n == 1:
    print(arr[0])
elif n == 2:
    print(max(arr[0], arr[1], sum(arr)))
else:
    dp[0] = max(dp[0], dp[0] + dp[1])

    for i in range(1,n - 1):
        if arr[i] >= 0:
            dp[i] = max(dp[i - 1] + dp[i + 1], dp[i - 1], arr[i], arr[i] + dp[i + 1])
        if arr[i] < 0:
            dp[i] = max(dp[i - 1] + arr[i] + dp[i + 1], dp[i - 1] + arr[i], arr[i], arr[i] + dp[i + 1])
    print(max(dp))