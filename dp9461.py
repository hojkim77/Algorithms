n = int(input())
t = [0] * n
for i in range(n):
    t[i] = int(input())
    
dp = [0] * 101
dp[0:5] = [1,1,1,2,2,3,4,5,7,9]
        
def padovan(n):
    if n < 10:
        return dp[n]
    else:
        for i  in range(n - 9):
            i += 10
            dp[i] = dp[i - 1] + dp[i - 5]
    return dp[n]

def solution():
    for i in range(n):
        print(padovan(t[i] - 1))
solution()