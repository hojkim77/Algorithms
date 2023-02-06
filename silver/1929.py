import math
N, M = map(int,(input().split()))    
    
def prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
for i in range(N, M + 1):
    if (prime(i)):
        print(i)