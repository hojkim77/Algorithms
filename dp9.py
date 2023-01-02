n = int(input())

arr = [int(input()) for _ in range(n)]
dp =[0] * (n + 1)

for i in range(n):
    if i == 0:
        dp[i] = arr[i]
    elif i == 1:
        dp[i] = arr[1] + arr[0]
    elif i == 2:
        dp[i] = max(arr[0] + arr[1], arr[1] + arr[2], arr[0] + arr[2])
    else:
        dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i], dp[i - 1])
        
print(max(dp))