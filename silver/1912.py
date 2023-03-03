n = int(input())
arr = list(map(int, input().split()))
dp = arr[:]

if n == 1:
    print(arr[0])
elif n == 2:
    print(max(arr[0], arr[1], sum(arr)))
else:
    for i in range(1,n):
        dp[i] = max(dp[i - 1] + arr[i], arr[i])
    print(max(dp)) 