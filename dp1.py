n = int(input())

dp = [0] * (n + 1)

def make_one(n):
    arr = []
    if dp[n] != 0:
        return dp[n]
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        if n % 2 == 0:
            arr.append(make_one(n // 2))
        if n % 3 == 0:
            arr.append(make_one(n // 3))
        if n % 2 != 0 or n % 3 != 0:
            arr.append(make_one(n - 1))
    dp[n] = min(arr) + 1
    #print(dp)
    return dp[n]

print(make_one(n))