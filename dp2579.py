n = int(input())
arr =[0]
for _ in range(n):
    arr.append(int(input()))
dp = [0] * (n + 1)
pre_arr = [0, 0]
def solution(n):
    if n == 1:
        return arr[1]
    dp[1] = arr[1]
    pre_arr[0] = 1
    if n == 2:
        return arr[1] + arr[2]
    dp[2] = arr[1] + arr[2]
    pre_arr[1] = 2
    if n == 3:
        return max(arr[1] + arr[3], arr[2] + arr[3])
        
    for i in range(3, n + 1):
        if i == n:
            return dp[n]
        elif i == n - 1:
            if dp[i - 1] == dp[i - 2]:
                dp[i] = dp[i - 1] + arr[i]
                dp[i + 1] = dp[i] + arr[i + 1]
            else:
                dp[i] = dp[i - 1]
                dp[i + 1] = dp[i] + arr[i + 1]
        elif i == 3:
            dp[3] = max(arr[1] + arr[3], arr[2] + arr[3])
            if arr[1] + arr[3] > arr[2] + arr[3]:
                pre_arr[0] = 1
                pre_arr[1] = 3
            else:
                pre_arr[0] = 2
                pre_arr[1] = 3

        elif pre_arr[0] == i - 2 and pre_arr[1] == i - 1:#전전꺼 전꺼 둘 다 밟았을 경우.
            dp[i] = dp[i - 1]
        elif dp[i - 1] == dp[i - 2]: #전꺼를 안밟았을 경우
            dp[i] = dp[i - 1] + arr[i]
            pre_arr[0] = pre_arr[1]
            pre_arr[1] = i            
        else:# 전전 꺼는 건너 뛰고 전꺼는 밟았을 경우.
            if dp[i - 1] + arr[i] > dp[i - 1] + arr[i + 1]:
                dp[i] = dp[i - 1] + arr[i] 
                pre_arr[0] = i - 1
                pre_arr[1] = i
            else:
                dp[i] = dp[i - 1]
                dp[i + 1] = dp[i - 1] + arr[i + 1]
                pre_arr[0] = i - 1
                pre_arr[1] = i + 1
    return dp[n]

print(solution(n))
print(dp)