n = int(input())

dp = [0] * (n + 1)

def make_one(n):
    arr = [] # n에서 가능한 경우의 수
    if dp[n] != 0: # 이미 한 번 결정된 값은 dp에 넣어두며 필요할 때 또 쓸 수 있다
        return dp[n]
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else: # n에서 나올 수 있는 모든 경우 3가지
        if n % 2 == 0:
            arr.append(make_one(n // 2))
        if n % 3 == 0:
            arr.append(make_one(n // 3))
        if n % 2 != 0 or n % 3 != 0:
            arr.append(make_one(n - 1))
    dp[n] = min(arr) + 1 # 위의 3 경우중 가장 작은 값(최적의 경우)에 + 1('//3' or '//2' or '-1')
    #print(dp)
    return dp[n]

print(make_one(n))