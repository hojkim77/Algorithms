'''
greedy 실패
N = int(input())
arr = list(map(int, input().split()))
sarr = []
for i in range(N):
    sarr.append([arr[i] / (i + 1), (i + 1)])
sarr.sort(reverse=True)
sum = 0
sum_n = 0
i = 0
while(sum_n < N):
    if (N - sum_n) % sarr[i][1] == 0:
        sum += arr[sarr[i][1] - 1] * int((N - sum_n) / sarr[i][1])
        sum_n += sarr[i][1] * int((N - sum_n) / sarr[i][1])
    else:
        i += 1
    if sum_n == N:
        break


print(int(sum))
'''
N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
    if i == 0:
        dp[i] = arr[i]
    else:
        for j in range(i):
            dp[i] = max(dp[i - j - 1] + arr[j], dp[i], arr[i])
        # i를 조사하기 위해서는 0부터 i-1까지 j인덱스로 접근하여 모든 조합의 
        # 수를 조사해봐야했다.
print(dp[N - 1])