# 수도배관공사

import sys
input = sys.stdin.readline

d, p = map(int, input().split())
dp = [1e9]+[0]*d
for _ in range(p):
    # 파이프들을 하나씩 추가할 때 마다 이걸로 만들 수 있는 파이프(이어진 파이프)들의 용량을 갱신해준다.
    l, c = map(int, input().split())
    dp_max = dp.copy()
    for i in range(l, d+1):# l로 만들 수 있는 파이프의 범위
        if dp_max[i-l] :
            dp[i] = max(dp[i], min(dp_max[i-l], c)) # l로 만들 수 있는 파이프들을 만들 때 붙일 수 있는 파이프의 길이 = i - l
print(dp[d])